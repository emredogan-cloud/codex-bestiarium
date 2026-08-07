#!/usr/bin/env python3
"""
CODEX BESTIARIUM — KELİME BANDI DENETİMİ
================================================================================
Yol haritası Bölüm 05.2: her madde 700 kelime ± %12, yani 620–790. Bu bant
SERT bir kısıttır:

    620'nin altı  → madde yüzeysel, "başvuru cildi" iddiası düşer
    790'ın üstü   → kitap 440 sayfaya taşar, baskı maliyeti ve fiyat bozulur

Ayrıca yedi bölümün her birinin kendi bandı vardır (Bölüm 05.2 tablosu).
Toplam bandı tutturup bölüm bandını kaçıran madde, biçimi doğru ama
oranı bozuk maddedir — o da yakalanır.

KULLANIM
    python3 08_BUILD/qa_length.py
    python3 08_BUILD/qa_length.py --sections --verbose
    python3 08_BUILD/qa_length.py --json 06_REPORTS/qa-length.json
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ENTRY_SECTIONS, ROOT, WORD_BAND, WORD_TARGET, Result  # noqa: E402
from textutil import iter_entries, require_book, word_count  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--book", default=None)
    ap.add_argument("--sections", action="store_true",
                    help="bölüm bantlarını da denetle")
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    r = Result("KELİME BANDI DENETİMİ (qa_length)")
    book, why = require_book(args.book)
    if book is None:
        r.ok("metin kapısı henüz açık değil", why)
        code = r.report(verbose=args.verbose)
        if args.json_out:
            r.to_json(os.path.join(ROOT, args.json_out))
        return code

    lo, hi = WORD_BAND
    totals: list[tuple[str, int]] = []
    below: list[str] = []
    above: list[str] = []

    for key, entry in iter_entries(book):
        sec = entry.get("sections", {})
        total = sum(word_count(sec.get(k, "")) for k, _, _, _ in ENTRY_SECTIONS)
        totals.append((key, total))
        if total < lo:
            below.append(f"{key}: {total} (−{lo - total})")
        elif total > hi:
            above.append(f"{key}: {total} (+{total - hi})")

    r.add(not below, f"hiçbir madde {lo} kelimenin altında değil",
          "; ".join(below[:15]))
    r.add(not above, f"hiçbir madde {hi} kelimenin üstünde değil",
          "; ".join(above[:15]))

    if totals:
        counts = [t for _, t in totals]
        mean = sum(counts) / len(counts)
        book_total = sum(counts)
        r.ok(
            "madde uzunluğu özeti",
            f"n={len(counts)} · ort={mean:.0f} (hedef {WORD_TARGET}) · "
            f"en kısa={min(counts)} · en uzun={max(counts)} · "
            f"toplam madde metni={book_total:,} kelime".replace(",", "."),
        )
        # Ortalama hedeften %5'ten fazla saparsa sayfa bütçesi kayar.
        drift = abs(mean - WORD_TARGET) / WORD_TARGET
        r.add(
            drift <= 0.05,
            "ortalama madde uzunluğu hedefin %5'i içinde",
            f"sapma: %{drift * 100:.1f} → 120 maddede "
            f"{abs(mean - WORD_TARGET) * len(counts):.0f} kelimelik fark, "
            f"~{abs(mean - WORD_TARGET) * len(counts) / 260:.0f} sayfa",
        )

    if args.sections:
        for skey, label, slo, shi in ENTRY_SECTIONS:
            bad = []
            missing = []
            for key, entry in iter_entries(book):
                body = entry.get("sections", {}).get(skey, "")
                if not body.strip():
                    missing.append(key)
                    continue
                n = word_count(body)
                if not slo <= n <= shi:
                    bad.append(f"{key}: {n}")
            r.add(
                not missing,
                f"'{label}' bölümü her maddede var",
                f"{missing[:12]} — bir bölüm boşsa madde yazılmamıştır, "
                "kısaltılmamıştır",
            )
            r.add(
                not bad,
                f"'{label}' bandı {slo}–{shi}",
                "; ".join(bad[:10]),
            )

    code = r.report(verbose=args.verbose)
    if args.json_out:
        r.to_json(os.path.join(ROOT, args.json_out))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
