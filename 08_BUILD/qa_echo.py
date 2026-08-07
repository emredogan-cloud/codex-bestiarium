#!/usr/bin/env python3
"""
CODEX BESTIARIUM — TEKRAR (EKO) TARAMASI
================================================================================
Yol haritası Bölüm 09, Faz 4 kalite kapısı:

    "qa_echo.py — maddeler arası 8+ kelimelik birebir tekrar var mı?"

120 madde aynı yedi bölümlü iskeleti taşır. İskelet tekrarı istenir; CÜMLE
tekrarı istenmez. Bir okur iki maddeyi yan yana okuduğunda aynı cümleyi
görüyorsa kitap bir derlemeye düşer.

DENETLENEN
    · maddeler arası 8+ kelimelik birebir öbek tekrarı
    · aynı madde içinde tekrar eden cümle
    · tekrar eden madde AÇILIŞ cümlesi (en görünür kusur)
    · aynı paragrafın iki yerde bulunması (birebir kopya paragraf)

KULLANIM
    python3 08_BUILD/qa_echo.py --verbose
    python3 08_BUILD/qa_echo.py --n 8 --json 06_REPORTS/qa-echo.json
"""

from __future__ import annotations

import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ROOT, Result  # noqa: E402
from textutil import (  # noqa: E402
    all_prose_blocks,
    iter_entries,
    normalize,
    require_book,
    sentences,
    words,
)

DEFAULT_N = 8

# KAYNAK NOTU ÇAPRAZ TEKRAR TARAMASINDAN MUAFTIR.
#
# Faz 3'te bulundu. Aynı başvuru eseri (Rose'un ansiklopedisi, Thompson'ın
# dizini) 112 maddenin çoğunda anılır ve künye biçimi TUTARLI olmak
# zorundadır — bir başvuru cildinde künyeyi maddeden maddeye değiştirmek
# kusurun ta kendisidir. Bu kapı, tutarlı künyeyi "üslup tekrarı" sayıp
# yazarı her maddede farklı bir künye biçimi uydurmaya zorluyordu.
#
# `qa_voice` aynı bölümü aynı gerekçeyle zaten muaf tutuyor (EXEMPT_SECTIONS):
# kaynak notu prozanın değil, künyenin yeridir. Muafiyet YALNIZCA maddeler
# arası n-gram taramasındadır; birebir kopya paragraf, madde içi tekrar ve
# açılış cümlesi denetimleri kaynak notunu görmeye devam eder.
ECHO_EXEMPT_SECTIONS = {"sources"}

# İskeletin doğal tekrarları. Bir n-gram bu ifadelerden birinin İÇİNDE
# kalıyorsa kusur değildir.
#
# DİKKAT — eskiden `gram in ALLOWED_ECHOES` diye denetleniyordu, yani 8
# kelimelik bir gram'ın buradaki bir öğeye BİREBİR EŞİT olması gerekiyordu.
# Kümedeki en uzun öğe 4 kelimeydi; hiçbir gram hiçbir öğeye eşit olamazdı.
# Muafiyet hiç devreye girmedi: ÖLÜ KURAL (D28 ve D32'nin üçüncü örneği).
# Artık kapsama ilişkisine bakılıyor ve öğeler n-gram'dan uzun tutuluyor.
ALLOWED_ECHOES = {
    "compare the entry on the same image in the tradition of",
    "see also the kin image chart at the back of the book",
    "thompson motif index of folk literature revised edition",
}


def allowed_echo(gram: str) -> bool:
    """n-gram, izin verilen bir ifadenin içinde mi kalıyor?"""
    return any(gram in phrase for phrase in ALLOWED_ECHOES)


def ngrams(tokens: list[str], n: int):
    for i in range(len(tokens) - n + 1):
        yield i, " ".join(tokens[i : i + n])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--book", default=None)
    ap.add_argument("--n", type=int, default=DEFAULT_N,
                    help="birebir tekrar sayılan en kısa öbek (kelime)")
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    r = Result(f"TEKRAR TARAMASI (qa_echo · {args.n}+ kelime)")
    book, why = require_book(args.book)
    if book is None:
        r.ok("metin kapısı henüz açık değil", why)
        code = r.report(verbose=args.verbose)
        if args.json_out:
            r.to_json(os.path.join(ROOT, args.json_out))
        return code

    blocks = all_prose_blocks(book)

    # --- 1. bloklar arası n-gram tekrarı ---
    # Kaynak notu bu taramadan muaftır (ECHO_EXEMPT_SECTIONS); künye
    # tutarlılığı kusur değil, kuraldır.
    scannable = [
        (label, text)
        for label, text in blocks
        if label.rsplit("/", 1)[-1] not in ECHO_EXEMPT_SECTIONS
    ]

    seen: dict[str, list[str]] = collections.defaultdict(list)
    for label, text in scannable:
        toks = [w.lower() for w in words(text)]
        for _, gram in ngrams(toks, args.n):
            if allowed_echo(gram):
                continue
            if label not in seen[gram]:
                seen[gram].append(label)

    cross = {
        gram: labels
        for gram, labels in seen.items()
        # farklı MADDELERde geçiyorsa tekrar; aynı maddenin iki bölümü değil
        if len({lbl.split("/")[0] for lbl in labels}) > 1
    }
    # Alt öbekleri ele: "a b c d e f g h" ve "b c d e f g h i" aynı olayı sayar.
    trimmed = {
        gram: labels
        for gram, labels in cross.items()
        if not any(gram != other and gram in other for other in cross)
    }
    detail = "\n         ".join(
        f"“{gram}”  →  {', '.join(labels[:4])}"
        for gram, labels in sorted(trimmed.items(), key=lambda kv: -len(kv[1]))[:12]
    )
    r.add(
        not trimmed,
        f"maddeler arası {args.n}+ kelimelik birebir tekrar yok",
        detail + (f"\n         toplam {len(trimmed)} öbek" if trimmed else ""),
    )

    # --- 2. birebir kopya paragraf ---
    paras: dict[str, list[str]] = collections.defaultdict(list)
    for label, text in blocks:
        for para in (p for p in text.split("\n\n") if len(words(p)) >= 15):
            paras[normalize(para)].append(label)
    dupe_paras = {k: v for k, v in paras.items() if len(v) > 1}
    r.add(
        not dupe_paras,
        "birebir kopya paragraf yok",
        "\n         ".join(
            f"{', '.join(v[:3])}: “{k[:70]}…”" for k, v in list(dupe_paras.items())[:8]
        ),
    )

    # --- 3. tekrar eden açılış cümlesi ---
    openings: dict[str, list[str]] = collections.defaultdict(list)
    for key, entry in iter_entries(book):
        opening = entry.get("sections", {}).get("opening", "").strip()
        if opening:
            openings[normalize(opening)].append(key)
    dupe_open = {k: v for k, v in openings.items() if len(v) > 1}
    r.add(
        not dupe_open,
        "tekrar eden açılış cümlesi yok",
        "; ".join(f"{v}: “{k[:60]}…”" for k, v in list(dupe_open.items())[:8]),
    )

    # --- 4. madde içi tekrar eden cümle ---
    inner = []
    for key, entry in iter_entries(book):
        counts: collections.Counter = collections.Counter()
        for skey, body in (entry.get("sections", {}) or {}).items():
            for s in sentences(body):
                if len(words(s)) >= 6:
                    counts[normalize(s)] += 1
        repeats = [s for s, n in counts.items() if n > 1]
        if repeats:
            inner.append(f"{key}: “{repeats[0][:60]}…”")
    r.add(not inner, "madde içinde tekrar eden cümle yok",
          "; ".join(inner[:10]))

    # --- 5. istatistik ---
    total_words = sum(len(words(t)) for _, t in blocks)
    r.ok(
        "tarama kapsamı",
        f"{len(blocks)} blok · {total_words:,} kelime".replace(",", ".")
        + f" · {len(seen):,} benzersiz {args.n}-gram".replace(",", "."),
    )

    code = r.report(verbose=args.verbose)
    if args.json_out:
        r.to_json(os.path.join(ROOT, args.json_out))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
