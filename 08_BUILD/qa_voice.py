#!/usr/bin/env python3
"""
CODEX BESTIARIUM — SES VE YASAK KALIP DENETİMİ
================================================================================
Yol haritası Bölüm 08.1. Bu kitabın tek savunması kaynak göstermesidir; ses
kuralları o savunmanın cümle düzeyindeki hâlidir.

    "It waits at the ford."          ✓ bildirici kip
    "It is said to wait at the ford." ✗ belirsizlik cümlede yönetilmez

Belirsizlik KAYNAK NOTUNDA yönetilir (7. bölüm), cümlede değil. Bu yüzden
yasak kalıp taraması 7. bölümü (kaynak notu) muaf tutar: orada "reported",
"attested" gibi ifadeler yerindedir.

DENETLENEN
    · yasak kalıplar ("it is said", "legend has it", …)
    · oyun terminolojisi (hit points, saving throw, …)
    · ölçülemez üstünlük ("the most terrifying", …)
    · sevimlileştirme ("actually quite", "misunderstood creature", …)
    · ünlem işareti (tüm kitapta sıfır)
    · modern kurgu kaynağı ("modern" etiketi olmadan Tolkien/D&D anılamaz)
    · cümle uzunluğu ortalaması (14–18 kelime bandı)

KULLANIM
    python3 08_BUILD/qa_voice.py --verbose
    python3 08_BUILD/qa_voice.py --json 06_REPORTS/qa-voice.json
"""

from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    FORBIDDEN_GAME_TERMS,
    FORBIDDEN_PHRASES,
    FORBIDDEN_SOFTENERS,
    FORBIDDEN_SUPERLATIVES,
    MAX_EXCLAMATIONS,
    MODERN_FICTION_MARKERS,
    ROOT,
    Result,
)
from textutil import all_prose_blocks, require_book, sentences, word_count  # noqa: E402

# Ortalama cümle uzunluğu bandı (Bölüm 08.1: "Ortalama 14–18 kelime")
SENTENCE_BAND = (14.0, 18.0)

# Kaynak notu bölümü yasak kalıp taramasından muaftır.
EXEMPT_SECTIONS = {"sources"}


def _hits(text: str, phrases: list[str]) -> list[tuple[str, str]]:
    """(kalıp, bağlam) — kelime sınırına saygılı, büyük/küçük harf duyarsız."""
    found = []
    low = text.lower()
    for phrase in phrases:
        for m in re.finditer(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", low):
            start = max(0, m.start() - 40)
            end = min(len(text), m.end() + 40)
            found.append((phrase, "…" + text[start:end].replace("\n", " ") + "…"))
    return found


def _scan(blocks, phrases, r: Result, name: str, note: str = "") -> None:
    all_hits = []
    for label, text in blocks:
        for phrase, ctx in _hits(text, phrases):
            all_hits.append(f"{label} → “{phrase}”  {ctx}")
    r.add(
        not all_hits,
        name,
        ("\n         ".join(all_hits[:12]) + (f"\n         {note}" if note and all_hits else "")),
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--book", default=None)
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    r = Result("SES VE YASAK KALIP DENETİMİ (qa_voice)")
    book, why = require_book(args.book)
    if book is None:
        r.ok("metin kapısı henüz açık değil", why)
        code = r.report(verbose=args.verbose)
        if args.json_out:
            r.to_json(os.path.join(ROOT, args.json_out))
        return code

    blocks = all_prose_blocks(book)
    scannable = [
        (label, text)
        for label, text in blocks
        if label.rsplit("/", 1)[-1] not in EXEMPT_SECTIONS
    ]

    _scan(scannable, FORBIDDEN_PHRASES, r,
          "yasak belirsizlik kalıbı yok",
          "belirsizlik kaynak notunda yönetilir, cümlede değil")
    _scan(blocks, FORBIDDEN_GAME_TERMS, r,
          "oyun terminolojisi yok",
          "bu bir oyun kitabı değildir")
    _scan(scannable, FORBIDDEN_SUPERLATIVES, r,
          "ölçülemez üstünlük iddiası yok")
    _scan(scannable, FORBIDDEN_SOFTENERS, r,
          "sevimlileştirme kalıbı yok",
          "yaratıkları sevimlileştiren her cümle kitabın gücünü düşürür")

    # --- ünlem işareti ---
    bangs = []
    for label, text in blocks:
        n = text.count("!")
        if n:
            bangs.append(f"{label}: {n}")
    r.add(
        sum(int(b.split(": ")[1]) for b in bangs) <= MAX_EXCLAMATIONS,
        f"ünlem işareti sayısı ≤ {MAX_EXCLAMATIONS}",
        "; ".join(bangs[:12]),
    )

    # --- modern kurgu ---
    # Geçebilir, ama tek cümlede ve "modern" etiketiyle.
    modern_bad = []
    for label, text in blocks:
        for phrase, ctx in _hits(text, MODERN_FICTION_MARKERS):
            if "modern" not in ctx.lower():
                modern_bad.append(f"{label} → “{phrase}”  {ctx}")
    r.add(
        not modern_bad,
        "modern kurgu göndermesi yalnızca 'modern' etiketiyle geçiyor",
        "\n         ".join(modern_bad[:10]),
    )

    # --- cümle uzunluğu ---
    lo, hi = SENTENCE_BAND
    long_entries = []
    lengths = []
    for label, text in scannable:
        sents = sentences(text)
        if not sents:
            continue
        avg = sum(word_count(s) for s in sents) / len(sents)
        lengths.append(avg)
        if not lo - 3 <= avg <= hi + 4:
            long_entries.append(f"{label}: {avg:.1f}")
    if lengths:
        overall = sum(lengths) / len(lengths)
        r.add(
            lo <= overall <= hi,
            f"kitap geneli ortalama cümle uzunluğu {lo}–{hi} kelime",
            f"ölçülen: {overall:.1f}",
        )
        if long_entries:
            r.warn(
                "bant dışına çıkan blok var",
                "; ".join(long_entries[:12]) + " — ritim sözlü anlatının ritmidir",
            )
        else:
            r.ok("blok bazında cümle uzunluğu dağılımı bantta")

    # --- tırnak dengesi (Faz 5 kapısı, erken uyarı olarak burada da) ---
    unbalanced = []
    for label, text in blocks:
        if text.count("“") != text.count("”"):
            unbalanced.append(f"{label} (“{text.count('“')} ”{text.count('”')})")
    r.add(not unbalanced, "tipografik tırnak dengesi 1:1",
          "; ".join(unbalanced[:12]))

    # --- düz tırnak / kısa çizgi sızıntısı ---
    straight = [
        label for label, text in blocks if '"' in text or " - " in text
    ]
    if straight:
        r.warn(
            "düz tırnak veya kısa çizgi sızıntısı",
            f"{straight[:12]} — dizgide tipografik karakterler kullanılır",
        )
    else:
        r.ok("tipografik karakterler temiz (düz tırnak/kısa çizgi yok)")

    code = r.report(verbose=args.verbose)
    if args.json_out:
        r.to_json(os.path.join(ROOT, args.json_out))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
