#!/usr/bin/env python3
"""
CODEX BESTIARIUM — ÜSLUP SÜRÜKLENMESİ DENETİMİ
================================================================================
120 madde uzun bir üretimdir. Yol haritası Bölüm 13, Risk 8: üslup
sürüklenmesi olasılığı YÜKSEK, etkisi ORTA. Erken uyarı ölçütü şudur:

    "en sık 50 kelimede yükselen eğim"

Yani: kitabın en sık kullandığı 50 içerik kelimesinin madde başına kullanım
sıklığı, madde sırası boyunca YÜKSELİYORSA yazar bir kalıba kilitleniyor
demektir. Bu göz kararıyla görülmez; ölçülür.

YÖNTEM
    1. Bütün maddelerin birleşik metninden durak kelimeler çıkarılır.
    2. En sık 50 içerik kelimesi belirlenir.
    3. Her madde için "bu 50 kelimenin bin kelimede kaç kez geçtiği" hesaplanır.
    4. Madde sırasına göre bu diziye en küçük kareler doğrusu uydurulur.
    5. Eğim, 120 madde boyunca toplam değişime çevrilir.

KAPI
    · toplam değişim ≤ %20  → geçer
    · %20–%35               → uyarı
    · %35 üstü              → başarısız

Ayrıca iki ek ölçü raporlanır: tip/token oranı eğimi (kelime dağarcığı
daralıyor mu) ve ortalama cümle uzunluğu eğimi (ritim uzuyor mu).

KULLANIM
    python3 08_BUILD/qa_drift.py --verbose
    python3 08_BUILD/qa_drift.py --top 50 --json 06_REPORTS/qa-drift.json
"""

from __future__ import annotations

import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ROOT, Result  # noqa: E402
from textutil import entry_text, iter_entries, require_book, sentences, words  # noqa: E402

WARN_AT = 0.20
FAIL_AT = 0.35
MIN_ENTRIES = 8   # bu sayının altında eğim istatistiksel olarak anlamsız

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on", "at",
    "by", "for", "with", "from", "as", "is", "are", "was", "were", "be", "been",
    "being", "it", "its", "he", "she", "they", "them", "his", "her", "their",
    "this", "that", "these", "those", "there", "here", "not", "no", "nor",
    "so", "than", "then", "when", "where", "which", "who", "whom", "what",
    "into", "out", "up", "down", "over", "under", "again", "once", "all",
    "any", "both", "each", "few", "more", "most", "other", "some", "such",
    "only", "own", "same", "too", "very", "can", "will", "would", "should",
    "could", "may", "might", "must", "shall", "do", "does", "did", "have",
    "has", "had", "one", "two", "three", "you", "your", "we", "our", "i",
}


def _slope(ys: list[float]) -> tuple[float, float]:
    """En küçük kareler eğimi ve kesişimi. x = 0..n-1."""
    n = len(ys)
    if n < 2:
        return 0.0, ys[0] if ys else 0.0
    xs = list(range(n))
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    slope = num / den if den else 0.0
    return slope, my - slope * mx


def _relative_change(ys: list[float]) -> tuple[float, float]:
    """Eğimin dizinin tamamına yayılmış göreli değişimi."""
    slope, intercept = _slope(ys)
    n = len(ys)
    start = intercept
    total = slope * (n - 1)
    if abs(start) < 1e-9:
        return 0.0, slope
    return total / start, slope


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--book", default=None)
    ap.add_argument("--top", type=int, default=50)
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    r = Result("ÜSLUP SÜRÜKLENMESİ DENETİMİ (qa_drift)")
    book, why = require_book(args.book)
    if book is None:
        r.ok("metin kapısı henüz açık değil", why)
        code = r.report(verbose=args.verbose)
        if args.json_out:
            r.to_json(os.path.join(ROOT, args.json_out))
        return code

    texts = [(key, entry_text(entry)) for key, entry in iter_entries(book)]
    texts = [(k, t) for k, t in texts if t.strip()]

    if len(texts) < MIN_ENTRIES:
        r.ok(
            "eğim ölçümü için madde sayısı yetersiz",
            f"{len(texts)} madde · en az {MIN_ENTRIES} gerekir — "
            "haftalık ölçüm Faz 3'ün 1. haftasından itibaren anlamlıdır",
        )
        code = r.report(verbose=args.verbose)
        if args.json_out:
            r.to_json(os.path.join(ROOT, args.json_out))
        return code

    # --- en sık N içerik kelimesi ---
    tokens_per_entry = [[w.lower() for w in words(t)] for _, t in texts]
    freq = collections.Counter(
        w for toks in tokens_per_entry for w in toks
        if w not in STOPWORDS and len(w) > 2
    )
    top_words = {w for w, _ in freq.most_common(args.top)}
    r.ok(
        f"en sık {args.top} içerik kelimesi",
        ", ".join(w for w, _ in freq.most_common(12)) + " …",
    )

    # --- madde başına yoğunluk (bin kelimede) ---
    density = []
    for toks in tokens_per_entry:
        if not toks:
            density.append(0.0)
            continue
        hits = sum(1 for w in toks if w in top_words)
        density.append(1000.0 * hits / len(toks))

    change, slope = _relative_change(density)
    detail = (
        f"eğim {slope:+.3f}/madde · {len(density)} madde boyunca "
        f"toplam değişim %{change * 100:+.1f} "
        f"(başlangıç ~{density[0]:.0f}‰, bitiş ~{density[-1]:.0f}‰)"
    )
    if abs(change) > FAIL_AT:
        r.fail(f"en sık {args.top} kelimede eğim ≤ %{FAIL_AT * 100:.0f}", detail)
    elif abs(change) > WARN_AT:
        r.warn(f"en sık {args.top} kelimede eğim ≤ %{WARN_AT * 100:.0f}", detail)
    else:
        r.ok(f"en sık {args.top} kelimede yükselen eğim yok", detail)

    # --- kelime dağarcığı zenginliği (tip/token) ---
    ttr = [len(set(t)) / len(t) if t else 0.0 for t in tokens_per_entry]
    ttr_change, ttr_slope = _relative_change(ttr)
    ttr_detail = (
        f"eğim {ttr_slope:+.5f}/madde · toplam değişim %{ttr_change * 100:+.1f} · "
        f"ortalama {sum(ttr) / len(ttr):.3f}"
    )
    if ttr_change < -WARN_AT:
        r.warn("kelime dağarcığı daralıyor (tip/token düşüyor)", ttr_detail)
    else:
        r.ok("kelime dağarcığı zenginliği kararlı", ttr_detail)

    # --- ritim ---
    avg_sent = []
    for _, t in texts:
        s = sentences(t)
        avg_sent.append(sum(len(words(x)) for x in s) / len(s) if s else 0.0)
    sent_change, sent_slope = _relative_change(avg_sent)
    sent_detail = (
        f"eğim {sent_slope:+.4f} kelime/madde · toplam değişim "
        f"%{sent_change * 100:+.1f} · ortalama {sum(avg_sent) / len(avg_sent):.1f}"
    )
    if abs(sent_change) > WARN_AT:
        r.warn("cümle uzunluğu ritmi sürükleniyor", sent_detail)
    else:
        r.ok("cümle uzunluğu ritmi kararlı", sent_detail)

    # --- açılış cümlesi kalıplaşması ---
    openers = collections.Counter()
    for _, entry in iter_entries(book):
        opening = entry.get("sections", {}).get("opening", "")
        first = words(opening)[:2]
        if first:
            openers[" ".join(w.lower() for w in first)] += 1
    if openers:
        top, count = openers.most_common(1)[0]
        share = count / sum(openers.values())
        r.add(
            share <= 0.25,
            "açılış cümleleri aynı iki kelimeyle başlamıyor",
            f"en sık açılış “{top}” — {count} madde (%{share * 100:.0f})",
        )

    code = r.report(verbose=args.verbose)
    if args.json_out:
        r.to_json(os.path.join(ROOT, args.json_out))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
