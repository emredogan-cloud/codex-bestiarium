#!/usr/bin/env python3
"""
CODEX BESTIARIUM — DÜŞMAN OLGU DENETİMİ (Faz 5 · Geçiş 1)
================================================================================
Bitmiş metnin her olgusal iddiasını KAYDA karşı sınar ve dayanağı olmayanı
çıkarır. Sorusu tek: *"metin, kaydın söylemediği bir şey söylüyor mu?"*

    NEDEN MEKANİK BİR ARAÇ
    ──────────────────────
    Yol haritası bu geçişi ayrı bir oturum olarak istiyor: metin, araştırma
    notları verilmeden okunacak ve çürütülmeye çalışılacak. O okumanın
    yerini hiçbir betik tutmaz — ama okumanın ÖNÜNE bir tarama koymak,
    okuyucunun zamanını gerçekten tartışmalı olan iddialara ayırmasını
    sağlar.

    Bu betik, ucuz ama gerçek bir kusur sınıfını kapatıyor: prozada geçen
    bir TARİH, bir SOYADI veya bir SAYININ `spec.json`'da karşılığı yoksa,
    o cümle kaydın ötesine geçmiştir. Faz 5'in araştırma turu altı maddede
    iki künye kusuru buldu; bu tarama aynı sınıfın kalanını arar.

    Ne YAPMAZ: bir kaynağın içeriğinin doğru olup olmadığını söylemez.
    Onun için kaynağın kendisi okunur. Bu betik yalnızca metin ile kayıt
    arasındaki AYRIŞMAYI bulur.

NE ARANIYOR

    ① Dayanaksız yıl      Prozadaki 1000–2029 arası her yıl, o maddenin
                          künyelerinde, `attested` alanında veya motif
                          tanımında geçmelidir. Geçmiyorsa iddia edilmiş
                          ama kaydedilmemiştir.
    ② Dayanaksız soyadı   Prozada "Croker printed…" gibi ATIF konumunda
                          geçen özel ad, künyelerde bulunmalıdır.
    ③ Sayı ayrışması      "nine traditions", "eight other members" gibi
                          sayı iddiaları akraba ailesinin GERÇEK üye
                          sayısıyla karşılaştırılır.
    ④ Motif kodu          Prozada geçen her Thompson kodu maddenin
                          `motif` listesinde olmalıdır.
    ⑤ Sınıf/gelenek adı   Metin başka bir maddeyi anarken adı doğru
                          yazmalıdır (diakritik kapısı ayrıca bakar).

ÇIKIŞ KODLARI
    0  itiraz yok        1  itiraz var        2  metin yok

KULLANIM
    python3 08_BUILD/factcheck.py
    python3 08_BUILD/factcheck.py --json 06_REPORTS/adversarial-review.json
    python3 08_BUILD/factcheck.py --allow 01_SOURCE/factcheck_allow.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ROOT, load_book, load_spec  # noqa: E402
from textutil import iter_entries, sentences  # noqa: E402

ALLOW_PATH = os.path.join(ROOT, "01_SOURCE", "factcheck_allow.json")

YEAR_RE = re.compile(r"\b(1[0-9]{3}|20[0-2][0-9])\b")

# Künyeler aralığı KISALTARAK yazar: "1855–63", "1916–20", "1896–1901".
# Proza ise açık yazar: "between 1855 and 1863". Aralığı genişletmeden
# ikinci yıl "dayanaksız" görünür ve tarama gerçek kusurları on tane
# yanlış pozitifin altında gömer — bir denetim aracının en pahalı hatası.
RANGE_RE = re.compile(r"\b(1[0-9]{3}|20[0-2][0-9])\s*[–—-]\s*(\d{2,4})\b")


def expand_years(text: str) -> set[str]:
    """Kayıttaki yıllar + kısaltılmış aralıkların KAPALI aralığı."""
    out = set(YEAR_RE.findall(text))
    for a, b in RANGE_RE.findall(text):
        start = int(a)
        end = int(b) if len(b) == 4 else int(str(start)[: 4 - len(b)] + b)
        if end < start or end - start > 200:
            continue
        out.update(str(y) for y in range(start, end + 1))
    return out
MOTIF_RE = re.compile(r"\b([A-HJ-NP-XZ]\d{1,4}(?:\.\d+)*)\b")

# Atıf konumundaki özel ad: "Croker printed", "Skeat collected",
# "Murgoci published", "… recorded by Andrews". Yalnızca bunlar aranır;
# metindeki her büyük harfli sözcük değil — yer ve yaratık adları da
# büyük harflidir ve onların yeri burası değildir.
CITE_VERBS = (
    r"printed|published|collected|recorded|wrote|gathered|reported|"
    r"entered|edited|translated|compiled|noted|set (?:it )?down"
)
CITE_RE = re.compile(
    rf"\b([A-ZÀ-Þ][\w'’À-ɏ-]+)\s+(?:{CITE_VERBS})\b")

# Cümle başındaki zamir ve belirteç de büyük harflidir ve fiilin öznesi
# olur: "He published…", "Only published material is used…". Bunlar atıf
# DEĞİLDİR. Listeye girmeyen her büyük harfli özne itiraz üretir — kapsayıcı
# olmak, sessizce dar olmaktan iyidir.
NOT_A_NAME = {
    "he", "she", "it", "they", "we", "i", "this", "that", "these", "those",
    "only", "nobody", "nothing", "no", "none", "both", "all", "each",
    "english", "the", "a", "an", "what", "who", "which", "there", "here",
    "most", "much", "many", "some", "few", "several", "one", "two", "three",
    "later", "earlier", "modern", "colonial", "european", "western",
}
CITE_BY_RE = re.compile(
    rf"\b(?:{CITE_VERBS})\s+(?:by|in)\s+([A-ZÀ-Þ][\w'’À-ɏ-]+)")

NUMBER_WORDS = {
    "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
}
# Yalnızca AİLE BOYUTU iddiası: ya "eight OTHER members" gibi açıkça
# "öteki"leri sayan bir ifade, ya da cümlesi akraba imgesinden söz eden
# bir sayı. "the two entries have to be read together" bir aile iddiası
# değildir ve sayılmamalıdır — sayarsa araç, gerçek kusurları gürültüye
# gömer.
KIN_COUNT_RE = re.compile(
    r"\b(" + "|".join(NUMBER_WORDS) + r")\s+(other\s+)?"
    r"(traditions|members|entries|creatures|peoples)\b", re.I)
KIN_CONTEXT_RE = re.compile(r"kin image|this family|the family|its family",
                            re.I)


def load_allow() -> dict:
    """Gerekçesi yazılmış istisnalar.

    İSTİSNA BİR GEVŞETME DEĞİLDİR: her satır bir GEREKÇE taşır ve
    gerekçesiz satır kabul edilmez. Amaç, taramanın doğası gereği
    üreteceği yanlış pozitifleri (bir yaratık adının soyadına benzemesi,
    bir motif kodunun cümle içinde örnek olarak anılması) sessizce
    boğmak değil, YAZILI olarak geçmek.
    """
    if not os.path.exists(ALLOW_PATH):
        return {}
    with open(ALLOW_PATH, encoding="utf-8") as fh:
        data = json.load(fh)
    bad = [k for k, v in data.items()
           if not isinstance(v, str) or len(v.strip()) < 20]
    if bad:
        raise SystemExit(
            "HATA: gerekçesiz istisna: " + ", ".join(bad) +
            "\n      Her istisna en az bir cümlelik gerekçe taşır.")
    return data


def record_text(rec: dict) -> str:
    """Bir maddenin KAYDI: künyeler, tarihçe, motif tanımları, notlar."""
    parts = [rec.get("attested", ""), rec.get("region", "")]
    for s in rec.get("sources", []):
        parts += [str(s.get(k, "")) for k in
                  ("ref", "locus", "note", "access", "quote")]
    parts += list((rec.get("motifDefs") or {}).values())
    parts.append(rec.get("motifNote", ""))
    # Düzeltilen kod, maddede "tohum kodu yanlıştı" diye ANILIR ve bu
    # kasıtlıdır: kitap işini gösteriyor. Kayıt o düzeltmeyi taşıyorsa
    # metnin onu anması bir ayrışma değildir.
    parts.append(str(rec.get("motifChanged", "") or ""))
    for v in rec.get("variants", []) or []:
        parts += [str(v.get("where", "")), str(v.get("what", ""))]
    parts.append(rec.get("variantNote", "") or "")
    parts.append(rec.get("incident", "") or "")
    parts.append(rec.get("restriction", "") or "")
    for n in rec.get("writingNotes", []) or []:
        parts.append(str(n))
    return " ".join(p for p in parts if p)


def find_sentence(text: str, needle: str) -> str:
    for s in sentences(text):
        if needle in s:
            return s.strip()
    return text[:120]


def check(book: dict, spec: dict, allow: dict) -> list[dict]:
    by_id = {c["id"]: c for c in spec["creatures"]}
    kin_size: dict[str, int] = {}
    for c in spec["creatures"]:
        k = c.get("kinFamily")
        if k:
            kin_size[k] = kin_size.get(k, 0) + 1

    objections: list[dict] = []

    def add(cid, section, kind, claim, detail, sentence):
        key = f"{cid}/{section}/{kind}/{claim}"
        if key in allow:
            return
        objections.append({
            "id": cid, "section": section, "kind": kind, "claim": claim,
            "detail": detail, "sentence": sentence, "key": key,
        })

    for cid, entry in iter_entries(book):
        rec = by_id.get(cid)
        if rec is None:
            continue
        rtext = record_text(rec)
        rec_years = expand_years(rtext)
        rec_motifs = set(rec.get("motif") or [])
        # Künyelerdeki her sözcük — soyadı denetimi için
        rec_words = set(re.findall(r"[\w'’À-ɏ-]+", rtext.lower()))

        for section, body in (entry.get("sections") or {}).items():
            if not body:
                continue

            # ① yıl
            for y in set(YEAR_RE.findall(body)):
                if y not in rec_years:
                    add(cid, section, "year", y,
                        "prozada geçiyor, kayıtta yok",
                        find_sentence(body, y))

            # ② atıf konumundaki soyadı
            names = set(CITE_RE.findall(body)) | set(CITE_BY_RE.findall(body))
            for name in names:
                # "Philippi's published translations" — iyelik eki adı
                # künyedekinden ayırır ve sahte itiraz üretir.
                bare = re.sub(r"['’]s$", "", name)
                if bare.lower() in NOT_A_NAME:
                    continue
                if bare.lower() in rec_words:
                    continue
                add(cid, section, "citation", bare,
                    "atıf konumunda geçiyor, künyelerde yok",
                    find_sentence(body, name))

            # ④ motif kodu
            for code in set(MOTIF_RE.findall(body)):
                if code in rec_motifs:
                    continue
                # Alternatif kod, "reddedildi" diye ANILMIŞ olabilir;
                # kayıtta geçiyorsa itiraz yok.
                if code in rtext:
                    continue
                add(cid, section, "motif", code,
                    "prozada geçiyor, maddenin motif listesinde ve kayıtta yok",
                    find_sentence(body, code))

            # ③ akraba sayısı
            fam = rec.get("kinFamily")
            if fam and fam in kin_size:
                for word, other, noun in KIN_COUNT_RE.findall(body):
                    sent = find_sentence(body, word)
                    if not other and not KIN_CONTEXT_RE.search(sent):
                        continue
                    n = NUMBER_WORDS[word.lower()]
                    real = kin_size[fam]
                    if n in (real, real - 1):   # "eight OTHER members"
                        continue
                    add(cid, section, "kincount", f"{word} {noun}".strip(),
                        f"aile {fam} gerçekte {real} üyeli", sent)
    return objections


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", metavar="YOL")
    ap.add_argument("--book")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    book = load_book(args.book)
    if book is None or not book.get("entries"):
        print("ATLANDI: metin yok — düşman denetimi yazımdan sonradır.")
        return 2

    spec = load_spec()
    allow = load_allow()
    objections = check(book, spec, allow)

    print("=" * 78)
    print("DÜŞMAN OLGU DENETİMİ (factcheck)")
    print("=" * 78)

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"objections": objections,
                       "allowed": len(allow)}, fh,
                      ensure_ascii=False, indent=2)
            fh.write("\n")

    if not objections:
        print(f"\n[  ok ] kaydın ötesine geçen iddia yok "
              f"· {len(allow)} gerekçeli istisna")
        return 0

    by_kind: dict[str, list[dict]] = {}
    for o in objections:
        by_kind.setdefault(o["kind"], []).append(o)

    labels = {"year": "dayanaksız tarih", "citation": "dayanaksız atıf",
              "motif": "kayıtta olmayan motif kodu",
              "kincount": "akraba sayısı ayrışması"}
    for kind, items in by_kind.items():
        print(f"\n▸ {labels.get(kind, kind)} — {len(items)}")
        for o in items if not args.quiet else items[:8]:
            print(f"  [{o['id']}/{o['section']}] “{o['claim']}” — {o['detail']}")
            print(f"        … {o['sentence'][:150]}")

    print(f"\n{len(objections)} itiraz. Her biri ya DÜZELTİLİR ya da "
          f"gerekçesiyle\n01_SOURCE/factcheck_allow.json'a yazılır. "
          f"Sessizce geçilmez.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
