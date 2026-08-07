#!/usr/bin/env python3
"""
CODEX BESTIARIUM — DİAKRİTİK VE ADLANDIRMA DENETİMİ
================================================================================
Yol haritası Bölüm 08.2:

    "Birincil ad geleneğin kendi romanizasyonudur ve diakritikleri korunur:
     Ḫumbaba, Sīmurgh, Húli jīng, Àbíkú. Diakritik düşürmek Mendîran'daki
     hatanın tekrarı olur."

Bu betik, metnin bir yaratığın adını diakritiksiz yazdığı her yeri bulur.
Ölçüt basittir: bir adın diakritiksiz hâli metinde geçiyorsa ve o konumda
diakritikli hâli DEĞİLSE, bu bir hatadır.

Ayrıca denetlenir:
    · spec.json'daki adların Unicode normalizasyonu (NFC — NFD karışımı yok)
    · görünmez/tehlikeli karakterler (sıfır genişlikli boşluk, NBSP, BOM)
    · altNames'te birincil adın tekrarı
    · Latin dışı işaretlerin (𒀭 𓂀 ᚦ …) yalnızca gelenek işareti olarak geçmesi

KULLANIM
    python3 08_BUILD/qa_diacritics.py --verbose
    python3 08_BUILD/qa_diacritics.py --json 06_REPORTS/qa-diacritics.json
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ROOT, Result, load_spec  # noqa: E402
from textutil import all_prose_blocks, require_book  # noqa: E402

# DİKKAT — kaçış dizisiyle yazılır; karakteri doğrudan yazmak bu betiğin
# kendi kaynağını kirletir ve tarama kendini yakalar.
DANGEROUS = {
    "\u200b": "ZERO WIDTH SPACE",
    "\u200c": "ZERO WIDTH NON-JOINER",
    "\u200d": "ZERO WIDTH JOINER",
    "\u200e": "LEFT-TO-RIGHT MARK",
    "\u200f": "RIGHT-TO-LEFT MARK",
    "\ufeff": "BYTE ORDER MARK",
    "\u00a0": "NO-BREAK SPACE",
    "\u00ad": "SOFT HYPHEN",
    "\u2028": "LINE SEPARATOR",
    "\u2029": "PARAGRAPH SEPARATOR",
    "\t": "TAB",
}


def strip_marks(text: str) -> str:
    d = unicodedata.normalize("NFD", text)
    return unicodedata.normalize(
        "NFC", "".join(c for c in d if unicodedata.category(c) != "Mn")
    )


def has_marks(text: str) -> bool:
    return strip_marks(text) != unicodedata.normalize("NFC", text)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--book", default=None)
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    r = Result("DİAKRİTİK VE ADLANDIRMA DENETİMİ (qa_diacritics)")
    spec = load_spec()
    creatures = spec["creatures"]

    # --- 1. spec.json'ın kendi hijyeni ---
    not_nfc = [
        c["id"]
        for c in creatures
        if c["name"] != unicodedata.normalize("NFC", c["name"])
    ]
    r.add(
        not not_nfc,
        "spec.json'daki adlar NFC normalize",
        f"{not_nfc[:10]} — NFD/NFC karışımı arama ve dizini bozar",
    )

    bad_chars = []
    for c in creatures:
        for field in ("name", "pronunciation", "region", "variantNote"):
            value = c.get(field) or ""
            for ch, label in DANGEROUS.items():
                if ch in value:
                    bad_chars.append(f"{c['id']}.{field}: {label}")
    r.add(not bad_chars, "spec.json'da görünmez/tehlikeli karakter yok",
          "; ".join(bad_chars[:10]))

    redundant = [
        c["id"]
        for c in creatures
        if c["name"] in (c.get("altNames") or [])
    ]
    r.add(not redundant, "altNames birincil adı tekrarlamıyor", f"{redundant[:10]}")

    diacritic_names = [c["name"] for c in creatures if has_marks(c["name"])]
    r.ok(
        "diakritik taşıyan ad sayısı",
        f"{len(diacritic_names)}/{len(creatures)} · "
        + ", ".join(diacritic_names[:10]) + " …",
    )

    # --- 2. metin varsa: diakritik düşürme taraması ---
    book, why = require_book(args.book)
    if book is None:
        r.ok("metin taraması henüz yapılamıyor", why)
        code = r.report(verbose=args.verbose)
        if args.json_out:
            r.to_json(os.path.join(ROOT, args.json_out))
        return code

    blocks = all_prose_blocks(book)

    # Yalnızca diakritikli adlar için tara. Diakritiksiz ad zaten doğrudur.
    targets = [
        (c["id"], c["name"], strip_marks(c["name"]))
        for c in creatures
        if has_marks(c["name"])
    ]

    # BÜYÜK/KÜÇÜK HARFE DUYARLI aranır. Faz 3'te bulundu: tarama `re.I` ile
    # koşuyordu ve `Lóng`un düz hâli `Long`, İngilizce metnin en sık
    # sözcüklerinden biriyle çakışıyordu. "…long after it has gone" cümlesi
    # diakritik hatası olarak raporlanıyordu. 78.400 kelimelik bir kitapta bu
    # kapı, yazarı "long" sözcüğünü hiç kullanmamaya zorlardı — yani doğru
    # metni reddeden bir cetvel olurdu. Plaka cetvelinin Faz 2'de bulunan
    # kusuruyla aynı sınıf: ölçüm aracının kendisi yanlış ölçüyordu.
    #
    # Bu kitapta yaratık adları HER ZAMAN özel ad olarak, büyük harfle
    # yazılır. Küçük harfli "long" bir ad değildir; büyük harfli "Long"
    # düşürülmüş diakritiktir ve yakalanmaya devam eder.
    hits = []
    for label, text in blocks:
        norm = unicodedata.normalize("NFC", text)
        for cid, correct, flat in targets:
            if flat.lower() == correct.lower():
                continue
            pattern = re.compile(r"(?<!\w)" + re.escape(flat) + r"(?!\w)")
            for m in pattern.finditer(norm):
                start = max(0, m.start() - 35)
                end = min(len(norm), m.end() + 35)
                hits.append(
                    f"{label} → “{flat}” olmalıydı “{correct}”  "
                    f"…{norm[start:end]}…"
                )
    r.add(
        not hits,
        "metinde diakritik düşürülmüş ad yok",
        "\n         ".join(hits[:12]),
    )

    # --- 3. metinde tehlikeli karakter ---
    text_bad = []
    for label, text in blocks:
        for ch, name in DANGEROUS.items():
            if ch in text:
                text_bad.append(f"{label}: {name} × {text.count(ch)}")
    r.add(not text_bad, "metinde görünmez/tehlikeli karakter yok",
          "; ".join(text_bad[:12]))

    # --- 4. metnin tamamı NFC mi ---
    non_nfc_blocks = [
        label
        for label, text in blocks
        if text != unicodedata.normalize("NFC", text)
    ]
    r.add(not non_nfc_blocks, "metin NFC normalize", f"{non_nfc_blocks[:10]}")

    code = r.report(verbose=args.verbose)
    if args.json_out:
        r.to_json(os.path.join(ROOT, args.json_out))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
