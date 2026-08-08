#!/usr/bin/env python3
"""
CODEX BESTIARIUM — EDİTORYAL DÜZELTME DEFTERİ (Faz 5 · Geçiş 2)
================================================================================
Her düzeltme bir KAYITTIR. Metne elle dokunulmaz.

    NEDEN
    ─────
    Yol haritası bunu açıkça istiyor: *"Her düzeltme `edits.json`'a
    kaydedilir: id, öncesi, sonrası, kategori, gerekçe. Elle düzenleme
    yapılmaz."*

    Gerekçesi tek cümlede şudur: elle düzeltilen bir metinde neyin neden
    değiştiği altı ay sonra hiç kimsede yoktur. Defterle düzeltilen bir
    metinde her değişiklik geri alınabilir, sayılabilir ve savunulabilir.
    Cilt 1'de bu defter otuz yedi düzeltme taşıdı ve üçü sonradan
    yanlış çıkıp geri alındı — defter olmasaydı hangi cümleye
    dokunulduğu bilinemezdi.

    Ayrıca `before` alanı bir SINAMADIR. Metin defterin yazıldığı günden
    beri değiştiyse eşleşme tutmaz ve betik kırmızı yanar; sessizce
    yanlış yere uygulanmaz.

BİÇİM  ·  01_SOURCE/edits.json
    [
      {
        "id": "each-uisce",          // madde kimliği · ön/arka madde için
                                     //   "front/introduction" biçimi
        "section": "where",          // yedi bölümden biri · matter'da "body"
        "before": "…",               // metinde BİREBİR bulunmalı
        "after":  "…",
        "category": "Olgu — kaynak atfı",
        "rationale": "…"             // neden; boş bırakılamaz
      }
    ]

DEPO SÖZLEŞMESİ
    `edits.json` ve `book-edited.json` proza taşır → `.gitignore`'dadır.
    Depoda kalan `01_SOURCE/edits_summary.json`'dır: kategori sayıları,
    kaç kelime eklendi/çıkarıldı, hangi maddeler dokunuldu. Proza yok.

ÇIKIŞ KODLARI
    0  tamam        1  eşleşmeyen veya eksik kayıt        2  metin yok

KULLANIM
    python3 08_BUILD/edits.py --apply      # book-edited.json üret
    python3 08_BUILD/edits.py --check      # defter metne uyuyor mu
    python3 08_BUILD/edits.py --report
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import BOOK_PATH, ROOT, load_book  # noqa: E402
from textutil import word_count  # noqa: E402

EDITS_PATH = os.path.join(ROOT, "01_SOURCE", "edits.json")
EDITED_PATH = os.path.join(ROOT, "01_SOURCE", "book-edited.json")
SUMMARY_PATH = os.path.join(ROOT, "01_SOURCE", "edits_summary.json")

REQUIRED = ("id", "section", "before", "after", "category", "rationale")


def load_edits() -> list[dict]:
    if not os.path.exists(EDITS_PATH):
        return []
    with open(EDITS_PATH, encoding="utf-8") as fh:
        edits = json.load(fh)
    for i, e in enumerate(edits):
        missing = [k for k in REQUIRED if not str(e.get(k, "")).strip()]
        if missing:
            raise SystemExit(
                f"HATA: kayıt {i} eksik alan taşıyor: {', '.join(missing)}\n"
                f"      Gerekçesiz düzeltme kabul edilmez.")
        if e["before"] == e["after"]:
            raise SystemExit(f"HATA: kayıt {i} hiçbir şeyi değiştirmiyor.")
    return edits


def get_block(book: dict, eid: str, section: str):
    """(okuyucu, yazıcı) — madde bölümü ya da ön/arka madde gövdesi."""
    if "/" in eid:
        group, key = eid.split("/", 1)
        mapping = book.get(group + "Matter") or {}
        item = mapping.get(key)
        if item is None:
            return None, None
        return (lambda: item.get("body", ""),
                lambda v: item.__setitem__("body", v))
    entry = (book.get("entries") or {}).get(eid)
    if entry is None:
        return None, None
    sec = entry.get("sections") or {}
    if section not in sec:
        return None, None
    return (lambda: sec.get(section, ""),
            lambda v: sec.__setitem__(section, v))


def apply_edits(book: dict, edits: list[dict]) -> tuple[list[str], list[dict]]:
    problems: list[str] = []
    applied: list[dict] = []
    for i, e in enumerate(edits):
        read, write = get_block(book, e["id"], e["section"])
        if read is None:
            problems.append(f"kayıt {i}: {e['id']}/{e['section']} metinde yok")
            continue
        body = read()
        n = body.count(e["before"])
        if n == 0:
            problems.append(
                f"kayıt {i}: {e['id']}/{e['section']} — 'before' bulunamadı "
                f"(metin defterden sonra değişmiş olabilir)")
            continue
        if n > 1:
            problems.append(
                f"kayıt {i}: {e['id']}/{e['section']} — 'before' {n} kez "
                f"geçiyor; hangisi olduğu belirsiz")
            continue
        write(body.replace(e["before"], e["after"], 1))
        applied.append({
            "id": e["id"], "section": e["section"], "category": e["category"],
            "wordsBefore": word_count(e["before"]),
            "wordsAfter": word_count(e["after"]),
        })
    return problems, applied


def write_summary(applied: list[dict]) -> None:
    """Depoda kalan ÖLÇÜ — proza yok (karar A1/D29)."""
    by_cat: dict[str, int] = {}
    for a in applied:
        by_cat[a["category"]] = by_cat.get(a["category"], 0) + 1
    with open(SUMMARY_PATH, "w", encoding="utf-8") as fh:
        json.dump({
            "note": "Editoryal düzeltme defterinin ÖLÇÜSÜ. Proza içermez "
                    "(karar A1/D29). Üreten: 08_BUILD/edits.py --apply",
            "total": len(applied),
            "byCategory": dict(sorted(by_cat.items())),
            "entriesTouched": sorted({a["id"] for a in applied}),
            "wordsRemoved": sum(a["wordsBefore"] for a in applied),
            "wordsAdded": sum(a["wordsAfter"] for a in applied),
        }, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--into-book", action="store_true",
                    help="düzeltilmiş metni book.json'a GERİ yazar")
    args = ap.parse_args()

    # DEFTER HER ZAMAN HAM METNİ OKUR. `load_book()` varsa
    # `book-edited.json`'ı tercih eder — doğru davranıştır, ama defter için
    # yanlıştır: düzeltmeler bir kez uygulandıktan sonra `before` dizgeleri
    # artık orada bulunmaz ve defter kendi ürettiği metinle "ayrışmış"
    # görünür. Kaynak her zaman yazımın çıktısıdır.
    book = load_book(BOOK_PATH)
    if book is None or not book.get("entries"):
        print("ATLANDI: metin yok — düzeltme defteri yazımdan sonradır.")
        return 2

    edits = load_edits()
    if not edits:
        print("Defter boş: 01_SOURCE/edits.json yok veya kayıt içermiyor.")
        return 0

    problems, applied = apply_edits(book, edits)

    print("=" * 78)
    print(f"EDİTORYAL DÜZELTME DEFTERİ — {len(edits)} kayıt")
    print("=" * 78)

    if problems:
        for p in problems:
            print(f"[FAIL] {p}")
        print(f"\n{len(problems)} kayıt uygulanamadı. Defter metinle "
              f"ayrışmış.")
        return 1

    by_cat: dict[str, int] = {}
    for a in applied:
        by_cat[a["category"]] = by_cat.get(a["category"], 0) + 1
    for cat, n in sorted(by_cat.items()):
        print(f"  {n:>3}  {cat}")
    dw = sum(a["wordsAfter"] - a["wordsBefore"] for a in applied)
    print(f"\n  {len(applied)} düzeltme · {len({a['id'] for a in applied})} "
          f"madde · kelime farkı {dw:+d}")

    if args.check:
        print("\n[  ok ] defter metne birebir uyuyor")
        return 0

    if args.apply or args.into_book:
        write_summary(applied)
        target = BOOK_PATH if args.into_book else EDITED_PATH
        with open(target, "w", encoding="utf-8") as fh:
            json.dump(book, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"\nyazıldı: {os.path.relpath(target, ROOT)}")
        print(f"yazıldı: {os.path.relpath(SUMMARY_PATH, ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
