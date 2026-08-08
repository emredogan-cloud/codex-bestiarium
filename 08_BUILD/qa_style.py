#!/usr/bin/env python3
"""
CODEX BESTIARIUM — ÜSLUP UYUMLAMA ÖLÇÜMÜ (Faz 5 · Geçiş 2 · D40)
================================================================================
`qa_echo`nun GÖREMEDİĞİNİ ölçer.

    qa_echo bir KAPIDIR ve sekiz kelimelik BİREBİR çakışmayı arar. Üslup
    sürüklenmesi oradan geçer: yazar aynı cümleyi kurmaz, aynı KALIBI
    kurar. "That is the whole of it" on dokuz maddede, "belongs to the
    same tradition" sekiz maddede, kısıtlılık cümlesi yedi maddede aynı
    iskeletle. Hiçbiri sekiz kelimelik birebir tekrar değildir ve hepsi
    okurun fark ettiği şeydir.

    Faz 4 raporu bu üç kümeyi adıyla devretti (§ 16):
      ① yazarın çözümleyici kalıpları
      ② yaşayan gelenek kısıt cümlesinin boilerplate'e dönmesi
      ③ karşılıklı çapraz referansların aynı cümleyle kurulması
    Bu betik onları SAYAR, böylece uyumlama geçişinin işe yarayıp
    yaramadığı tartışılmaz.

    NEDEN KAPI DEĞİL
    ────────────────
    Bir dilde tekrar eden dört kelimelik öbek kaçınılmazdır ve sıfırlamak
    metni bozar. Kurucunun Faz 5 emri de bunu söylüyor: *"sayıyı yapay
    olarak küçültme; hedef tutarlı bir yazar sesi, aynı cümle yapısı
    değil."* Dolayısıyla bu bir ÖLÇÜMDÜR (D25/D47 içtihadı): rapor eder,
    kırmızı yakmaz. Kırmızı yakan qa_echo'dur ve o dokunulmadı.

KAYNAK NOTU HARİÇTİR
    D34 künyeyi tekrar taramasından muaf tutar: aynı kitabı gösteren iki
    madde aynı künyeyi yazmak ZORUNDADIR. Aynı muafiyet burada da
    geçerlidir — ve yalnızca 7. bölüm için. Faz 4'te künye ekosu 2.
    bölüme sızmıştı ve o muaf değildi.

KULLANIM
    python3 08_BUILD/qa_style.py
    python3 08_BUILD/qa_style.py --top 40
    python3 08_BUILD/qa_style.py --json 06_REPORTS/qa-style.json
    python3 08_BUILD/qa_style.py --family restriction
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ROOT, load_book  # noqa: E402
from textutil import all_prose_blocks, normalize  # noqa: E402

MIN_N, MAX_N = 5, 7          # şablon uzunluğu
MIN_ENTRIES = 4              # kaç FARKLI maddede geçerse şablon sayılır

# Adlandırılmış kümeler — Faz 4 raporunun devrettiği hedefler. Anahtar
# öbek metinde geçiyorsa o madde kümeye girer. Liste kapı değil NİŞANDIR:
# sayı düştükçe geçişin işe yaradığı görülür.
FAMILIES = {
    "whole-of": [
        "that is the whole of", "is the whole of it", "the whole of the",
    ],
    "restriction": [
        "only published material is used", "are not set out here",
        "the material used here is published", "stays with them",
        "is not reproduced here", "belongs to that tradition",
    ],
    "crossref": [
        "belongs to the same tradition", "comes out of the same",
        "shares the tradition", "to the same tradition and",
    ],
    "analytic": [
        "what is being described is", "what this creature supplies is",
        "what the belief supplies is", "what the tradition supplies is",
        "what can be said is", "what separates this entry from",
        "every other creature in this", "nothing else in this book",
        "is the part that matters", "the family this entry belongs",
        "is the mistake this entry", "that is a description of",
    ],
}


def blocks_for(book: dict) -> list[tuple[str, str]]:
    """Künye HARİÇ bütün proza blokları (D34)."""
    return [(k, t) for k, t in all_prose_blocks(book)
            if not k.endswith("/sources")]


def templates(blocks) -> dict[str, set[str]]:
    seen: dict[str, set[str]] = collections.defaultdict(set)
    for key, text in blocks:
        owner = key.split("/")[0]
        words = normalize(text).split()
        for n in range(MIN_N, MAX_N + 1):
            for i in range(len(words) - n + 1):
                seen[" ".join(words[i:i + n])].add(owner)
    return {p: v for p, v in seen.items() if len(v) >= MIN_ENTRIES}


def intra_entry(book: dict, n: int = 5) -> list[tuple[str, str, int]]:
    """Bir MADDENİN kendi içinde tekrarlanan öbek.

    `qa_echo` maddeler ARASINA bakar; Faz 4 raporu Tikbalang'ın madde içi
    tekrarını yakalayamadığını açıkça yazdı (§ 18, açık kalan 4).
    """
    out = []
    for cid, entry in (book.get("entries") or {}).items():
        sec = entry.get("sections") or {}
        text = " ".join(v for k, v in sec.items() if k != "sources" and v)
        words = normalize(text).split()
        counts = collections.Counter(
            " ".join(words[i:i + n]) for i in range(len(words) - n + 1))
        for phrase, c in counts.items():
            if c >= 2:
                out.append((cid, phrase, c))
    return sorted(out, key=lambda x: -x[2])


def family_hits(blocks, family: str) -> dict[str, list[str]]:
    hits: dict[str, list[str]] = {}
    for needle in FAMILIES[family]:
        owners = sorted({k.split("/")[0] for k, t in blocks
                         if needle in normalize(t)})
        if owners:
            hits[needle] = owners
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--json", metavar="YOL")
    ap.add_argument("--family", choices=sorted(FAMILIES))
    ap.add_argument("--book")
    args = ap.parse_args()

    book = load_book(args.book)
    if book is None or not book.get("entries"):
        print("ATLANDI: metin yok.")
        return 2

    blocks = blocks_for(book)
    tpl = templates(blocks)
    intra = intra_entry(book)

    if args.family:
        print(f"KÜME: {args.family}")
        for needle, owners in sorted(family_hits(blocks, args.family).items(),
                                     key=lambda x: -len(x[1])):
            print(f"\n  “{needle}” — {len(owners)} madde")
            print("     " + ", ".join(owners))
        return 0

    print("=" * 78)
    print("ÜSLUP UYUMLAMA ÖLÇÜMÜ (qa_style) — ölçüm, kapı DEĞİL")
    print("=" * 78)

    fam_counts = {}
    for name in sorted(FAMILIES):
        owners: set[str] = set()
        for needle in FAMILIES[name]:
            owners |= {k.split("/")[0] for k, t in blocks
                       if needle in normalize(t)}
        fam_counts[name] = len(owners)

    print("\n▸ adlandırılmış kümeler (Faz 4 § 16 devri)")
    labels = {"whole-of": "“that is the whole of…” kalıbı",
              "restriction": "yaşayan gelenek kısıt cümlesi",
              "crossref": "çapraz referans kalıbı",
              "analytic": "yazarın çözümleyici kalıpları"}
    for name in sorted(FAMILIES):
        print(f"  {fam_counts[name]:>4} madde   {labels.get(name, name)}")

    ranked = sorted(((len(v), p) for p, v in tpl.items()), reverse=True)
    print(f"\n▸ en sık şablonlar ({MIN_N}–{MAX_N} kelime, "
          f"≥{MIN_ENTRIES} maddede) — toplam {len(ranked)}")
    for n, p in ranked[:args.top]:
        print(f"  {n:>4} madde   “{p}”")

    print(f"\n▸ madde İÇİ tekrar (5 kelime, aynı maddede ≥2) — "
          f"toplam {len(intra)}")
    for cid, phrase, c in intra[:10]:
        print(f"  {c}×  [{cid}] “{phrase}”")

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({
                "families": fam_counts,
                "templateCount": len(ranked),
                "topTemplates": [{"entries": n, "phrase": p}
                                 for n, p in ranked[:60]],
                "intraEntry": [{"id": c, "phrase": p, "times": n}
                               for c, p, n in intra],
            }, fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    print(f"\nÖzet: {len(ranked)} şablon · madde içi tekrar {len(intra)}")
    print("Bu bir ölçümdür. Düşürme işi metindedir, eşikte değil.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
