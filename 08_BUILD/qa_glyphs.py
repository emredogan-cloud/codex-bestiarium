#!/usr/bin/env python3
"""
CODEX BESTIARIUM — GLİF KAPSAMI DENETİMİ (Faz 6)
================================================================================
Kitapta basılan HER karakterin, o karakteri basacak FONTTA glifi var mı?

    NEDEN AYRI BİR KAPI
    ───────────────────
    Eksik glif sessiz bir kusurdur. reportlab uyarı vermez; PDF üretilir,
    doğrulayıcılar yeşil yanar ve karakter sayfada boş kutu ya da hiçlik
    olarak çıkar. Faz 6'nın görsel denetimi kaynaklar sayfasında "ʿArab"
    yerine bozuk bir kutu buldu — ʿayn (U+02BF) Cinzel'de yok.
    Gözle bulunan bir kusurun ikizi vardır ve gözle bulunmaz.

    İKİ FONT, İKİ İŞ. EB Garamond gövdeyi dizer ve diakritik kapsaması
    geniştir. Cinzel bir BAŞLIK yüzüdür ve kapsaması dardır — ama başlıklar
    yaratık ve gelenek adlarını taşır, yani kitabın en fazla diakritik
    taşıyan metni oradadır. Kapı bu yüzden metni FONTUNA göre ayırır.

    Kapı, sigil sorununu da makineyle yakalar: kırk gelenek işaretinin otuz
    yedisi hiçbir metin fontunda yoktur (hiyeroglif, çivi yazısı, runa,
    hangul, Maya rakamı). Faz 6 bu yüzden sigilleri kitaptan çıkardı.

NE TARANIR
    başlık yüzü (Cinzel)  : yaratık adları · sınıf adları · aile adları ·
                            gelenek adları · ön/arka madde başlıkları
    gövde yüzü (Garamond) : bütün proza · künye · dizinler · kaynak notları

ÇIKIŞ KODLARI
    0  eksik glif yok      1  eksik glif var      2  font veya metin yok

KULLANIM
    python3 08_BUILD/qa_glyphs.py
    python3 08_BUILD/qa_glyphs.py --json 06_REPORTS/qa-glyphs.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    MATTER_SECTIONS,
    ROOT,
    load_book,
    load_spec,
    matter_group,
    region_en,
)

FONT_DIR = os.path.join(ROOT, "07_ASSETS", "fonts")
FACES = {
    "Cinzel": "Cinzel[wght].ttf",
    "EB Garamond": "EBGaramond[wght].ttf",
    "EB Garamond Italic": "EBGaramond-Italic[wght].ttf",
}

# Dizgi bunları hiç basmaz: biçimlendirme ve boşluk.
IGNORE = set(" \t\n\r ")


def cmap_of(path: str) -> set[int]:
    from fontTools.ttLib import TTFont

    with TTFont(path, lazy=True) as f:
        return set(f.getBestCmap().keys())


def collect(book, spec) -> tuple[set[str], set[str]]:
    """(başlık yüzüyle dizilen metin, gövde yüzüyle dizilen metin)."""
    display, body = set(), set()

    def add(target, text):
        if text:
            target.update(str(text))

    for c in spec["creatures"]:
        add(display, c["name"])                     # madde başlığı
        add(body, c.get("pronunciation", ""))
        add(body, " ".join(c.get("motif", [])))
    for t in spec["traditions"]:
        add(display, t["name"])                     # kaynaklar + dizin başlığı
        add(body, t["name"])
    for k in spec["classes"]:
        add(display, k["en"])
    for f in spec["kinFamilies"]:
        add(display, f["en"])
        add(body, f.get("divergenceEn", ""))
    for t in spec["traditions"]:
        add(display, region_en(t["regionGroup"]))
    for _g, _key, title, _p in MATTER_SECTIONS:
        add(display, title)

    if book:
        for entry in (book.get("entries") or {}).values():
            for v in (entry.get("sections") or {}).values():
                add(body, v)
        for group in ("classOpenings", "kinOpenings"):
            for v in (book.get(group) or {}).values():
                add(body, v)
        for _g, key, _t, _p in MATTER_SECTIONS:
            item = (book.get(matter_group(key)) or {}).get(key) or {}
            add(body, item.get("body", ""))

    import front_matter as FM
    for line in FM.COPYRIGHT:
        add(body, line)
    add(display, FM.HALF_TITLE)
    for v in FM.TITLE_PAGE.values():
        add(display, v)
    add(body, FM.DEDICATION)
    for v in list(FM.INDEX_TITLES.values()) + [FM.SOURCES_TITLE,
                                               FM.CONTENTS_TITLE,
                                               FM.MAP_TITLE]:
        add(display, v)
    for v in list(FM.INDEX_NOTES.values()) + [FM.SOURCES_NOTE, FM.MAP_NOTE]:
        add(body, v)

    return display - IGNORE, body - IGNORE


def describe(ch: str) -> str:
    try:
        name = unicodedata.name(ch)
    except ValueError:
        name = "?"
    return f"U+{ord(ch):04X} {ch!r} {name}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", metavar="YOL")
    args = ap.parse_args()

    try:
        import fontTools  # noqa: F401
    except ImportError:
        print("ATLANDI: fontTools yok — ./08_BUILD/bootstrap.sh")
        return 2
    for name, fn in FACES.items():
        if not os.path.exists(os.path.join(FONT_DIR, fn)):
            print(f"ATLANDI: font yok — {fn}")
            return 2

    book = load_book()
    spec = load_spec()
    display, body = collect(book, spec)

    cin = cmap_of(os.path.join(FONT_DIR, FACES["Cinzel"]))
    gar = cmap_of(os.path.join(FONT_DIR, FACES["EB Garamond"]))
    gari = cmap_of(os.path.join(FONT_DIR, FACES["EB Garamond Italic"]))

    missing, fallback = [], []
    for ch in sorted(display):
        if ord(ch) not in cin:
            # `entry_page.display_safe` bu karakteri gövde yüzüne düşürür.
            # Düşüm bir kusur değil, tasarlanmış davranıştır — ama gövde
            # yüzünde de yoksa kurtarma yoktur.
            if ord(ch) in gar:
                fallback.append(ch)
            else:
                missing.append(("hiçbir yüzde yok", ch))
    for ch in sorted(body):
        if ord(ch) not in gar:
            missing.append(("EB Garamond (gövde)", ch))
        elif ord(ch) not in gari:
            missing.append(("EB Garamond Italic", ch))

    print("=" * 78)
    print("GLİF KAPSAMI DENETİMİ (qa_glyphs)")
    print("=" * 78)
    print(f"  başlık yüzüyle dizilen ayrı karakter : {len(display)}")
    print(f"  gövde yüzüyle dizilen ayrı karakter  : {len(body)}")
    if fallback:
        print(f"  başlıkta gövde yüzüne düşen karakter : {len(fallback)} "
              f"→ {' '.join(fallback)}")

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"displayChars": len(display), "bodyChars": len(body),
                       "displayFallback": fallback,
                       "missing": [{"face": f, "char": c,
                                    "codepoint": f"U+{ord(c):04X}"}
                                   for f, c in missing]},
                      fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    if not missing:
        print("\n[  ok ] basılan her karakterin glifi var")
        return 0

    print(f"\n[FAIL] {len(missing)} karakterin glifi YOK — sayfada boş "
          f"kutu olarak çıkar:")
    for face, ch in missing:
        print(f"         {face:22} {describe(ch)}")
    print("\n  Çözüm: karakteri kitaptan çıkarın, yerine glifi olan bir "
          "biçim koyun,\n  veya o metni glifi olan yüzle dizin. Fontu "
          "değiştirmek seri kimliğini bozar.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
