#!/usr/bin/env python3
"""
CODEX BESTIARIUM — ÖN/ARKA MADDE DİZGİSİ VE SAYFA ÖLÇÜMÜ
================================================================================
`entry_page.py` bir MADDENİN üç sayfaya sığdığını ölçer. Bu betik aynı işi
ön ve arka madde için yapar: giriş, "bu kitap nasıl okunur", sonsöz ve arka
madde bölümleri gerçekten dizilir ve KAÇ SAYFA tuttukları sayılır.

    NEDEN AYRI BİR ÖLÇÜM GEREKİYOR
    ──────────────────────────────
    Sayfa bütçesi (BRIEF § 7) bu bölümlere sabit SLOT ayırır: giriş 8,
    nasıl okunur 6, sonsöz 4, arka madde 2+2+2+2. Bu sayılar kitabın
    436 sayfasının parçasıdır ve kayarsa baskı maliyeti, fiyat ve telif
    tablosu birlikte kayar.

    Kelime sayarak sayfa tahmin etmek bu işi görmez. "Sayfada yaklaşık
    480 kelime" bir ORTALAMADIR; başlığı, ilk sayfadaki boşluğu, paragraf
    aralığını ve son sayfanın yarısını içermez. Cilt 1'de büyük punto için
    540 sayfa MODELLENMİŞ, 578 ÇIKMIŞTI. Bu depoda geçerli olan kural
    oradan geliyor: model değil ÖLÇÜM.

    Bölüm başlıkları ve slotlar `bestiarium.MATTER_SECTIONS`'tan gelir.
    Bu betikte kitaba özgü tek bir sabit yoktur.

KAPI
    Ölçülen sayfa slotu AŞARSA kırmızı yanar. Altında kalmak kusur değildir
    — boşluk ön maddede tasarımdır — ama bütçe israfı büyükse raporlanır.

ÇIKIŞ KODLARI
    0  geçti          1  bütçe aşıldı          2  reportlab/pypdf yok

KULLANIM
    python3 08_BUILD/matter_page.py --measure
    python3 08_BUILD/matter_page.py --measure --edition large-print
    python3 08_BUILD/matter_page.py --check          # kapı kipi, sessiz
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    MATTER_PAGES,
    MATTER_SECTIONS,
    MATTER_STRUCTURAL_PAGES,
    ROOT,
    load_book,
    matter_group,
)
from textutil import word_count  # noqa: E402

REPORT_PATH = os.path.join(ROOT, "06_REPORTS", "matter-measurement.json")
# ÖLÇÜM DEPODA KALIR — plaka manifestosuyla aynı sözleşme (D38/D51).
# `06_REPORTS/*.json` `.gitignore`'dadır; CI'da bulunmaz. Ölçüyü oraya
# bırakıp `update_docs`a okutmak, Faz 4'te iki kez yaşanan kırmızıyı
# üretir: yerelde bir sayı, CI'da başka bir sayı. Bu dosya PROZA
# İÇERMEZ — anahtar, başlık, kelime ve sayfa sayısı. Başlıklar zaten
# `bestiarium.MATTER_SECTIONS`'ta, yani depodadır.
MEASURE_PATH = os.path.join(ROOT, "01_SOURCE", "matter_measurement.json")

# Bölüm başlığının stili. Madde başlığıyla AYNI aileden ama daha büyük:
# bunlar kitabın bölüm açılışlarıdır, madde değil.
MATTER_SPEC = {
    "title_font": "Cinzel",
    "title_pt": 20.0,
    "title_tracking_em": 0.06,
    "title_space_after": 26.0,   # punto
    "top_drop": 1.10,            # inç — başlığın üstünde bırakılan boşluk
    "subhead_font": "Cinzel",    # ara başlık — `## ` ile yazılır
    "subhead_pt": 10.5,
}


def _require_reportlab() -> None:
    missing = []
    for mod, why in (("reportlab", "dizgi"), ("pypdf", "sayfa sayımı")):
        try:
            __import__(mod)
        except ImportError:
            missing.append(f"{mod} ({why})")
    if missing:
        print("ATLANDI: ön/arka madde dizgisi şunları gerektirir: "
              + ", ".join(missing))
        print("         ./08_BUILD/bootstrap.sh çalıştırın.")
        raise SystemExit(2)


def inline(text: str) -> str:
    """`**koyu**` → reportlab etiketi; XML özel karakterleri kaçırılır.

    Ön/arka maddede tanım listesi vardır ("Nerede anlatılır — …") ve satır
    içi koyu başlangıç oralarda standarttır. MADDE metninde koyu YOKTUR;
    bu yüzden dönüşüm burada, `entry_page`de değil.

    Kaçırma önce yapılır: metinde geçen bir `&` veya `<`, dönüşümden sonra
    kaçırılırsa üretilen etiketleri de bozar.
    """
    out = (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    parts = out.split("**")
    if len(parts) % 2 == 0:            # tek sayıda `**` → eşleşmemiş
        raise SystemExit(f"HATA: eşleşmemiş '**' → {text[:60]}…")
    return "".join(p if i % 2 == 0 else f"<b>{p}</b>"
                   for i, p in enumerate(parts))


def matter_flow(title: str, body: str, L, S) -> list:
    """Bir ön/arka madde bölümünün akış nesneleri: başlık + paragraflar."""
    from reportlab.lib.units import inch as IN
    from reportlab.platypus import Paragraph, Spacer

    from entry_page import tracked

    flow = [Spacer(1, MATTER_SPEC["top_drop"] * IN)]
    flow.append(Paragraph(
        tracked(title.upper(), MATTER_SPEC["title_tracking_em"],
                MATTER_SPEC["title_pt"] * L.ed.display_scale),
        S["matter_title"]))
    # ARA BAŞLIK: `## ` ile başlayan paragraf. Sekiz sayfalık bir giriş
    # bölümü ara başlıksız okunmaz; madde metninde ise ara başlık YOKTUR
    # (yedi bölümün kendi başlıkları vardır) ve bu yüzden kural buraya özgü.
    # `textutil.sentences` paragraf sonunu cümle sonu sayar, dolayısıyla
    # noktalamasız başlık ölçümü bozmaz.
    fresh = True
    for p in [x.strip() for x in body.split("\n\n") if x.strip()]:
        if p.startswith("## "):
            flow.append(Paragraph(inline(p[3:].strip()), S["subhead"]))
            fresh = True
            continue
        flow.append(Paragraph(inline(p), S["body1"] if fresh else S["body"]))
        fresh = False
    return flow


def matter_styles(L):
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.styles import ParagraphStyle

    k = L.ed.display_scale
    return {
        "matter_title": ParagraphStyle(
            "matter_title", fontName=MATTER_SPEC["title_font"],
            fontSize=MATTER_SPEC["title_pt"] * k,
            leading=MATTER_SPEC["title_pt"] * k * 1.30,
            alignment=TA_CENTER, textColor="#111111",
            spaceAfter=MATTER_SPEC["title_space_after"] * k,
        ),
        "subhead": ParagraphStyle(
            "matter_subhead", fontName=MATTER_SPEC["subhead_font"],
            fontSize=MATTER_SPEC["subhead_pt"] * k,
            leading=MATTER_SPEC["subhead_pt"] * k * 1.30,
            textColor="#111111",
            spaceBefore=MATTER_SPEC["subhead_pt"] * k * 1.10,
            spaceAfter=MATTER_SPEC["subhead_pt"] * k * 0.45,
        ),
        "body": L.S["body"],
        "body1": L.S["body1"],
    }


def build_one(key: str, title: str, body: str, edition: str) -> dict:
    """Tek bölümü gerçekten dizer ve sayfa sayar. PDF ATILIR (A1/D29)."""
    import make_pdf as MP
    from reportlab.lib.units import inch as IN
    from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate

    L = MP.configure(edition)
    S = matter_styles(L)

    fd, path = tempfile.mkstemp(suffix=".pdf", prefix=f"matter-{key}-")
    os.close(fd)
    try:
        doc = BaseDocTemplate(
            path, pagesize=(L.PW, L.PH),
            leftMargin=L.GUTTER, rightMargin=L.OUTER,
            topMargin=L.TOPM, bottomMargin=L.BOTM,
            title=f"{title} — prova dizgisi", author="Vâliçe Press",
            subject="Codex Bestiarium · ön/arka madde ölçümü",
        )
        frame = Frame(L.GUTTER, L.BOTM, L.ed.text_w * IN, L.ed.text_h * IN,
                      id="body", leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
        doc.addPageTemplates([PageTemplate(id="matter", frames=[frame])])

        flow = matter_flow(title, body, L, S)
        text_w_pt = L.ed.text_w * 72.0
        text_h_pt = L.ed.text_h * 72.0
        content_pt = 0.0
        for f in flow:
            sb = f.getSpaceBefore() if hasattr(f, "getSpaceBefore") else 0
            sa = f.getSpaceAfter() if hasattr(f, "getSpaceAfter") else 0
            _w, h = f.wrap(text_w_pt, text_h_pt)
            content_pt += sb + h + sa

        doc.build(flow)

        from pypdf import PdfReader
        pages = len(PdfReader(path).pages)
    finally:
        if os.path.exists(path):
            os.remove(path)

    return {
        "key": key,
        "title": title,
        "words": word_count(body),
        "pages": pages,
        "budget": MATTER_PAGES[key],
        "contentPages": round(content_pt / text_h_pt, 3),
        "edition": edition,
    }


def measure(edition: str, verbose: bool = True) -> int:
    _require_reportlab()
    book = load_book()
    if book is None:
        print("ATLANDI: book.json yok — ön/arka madde henüz yazılmadı.")
        return 2

    rows: list[dict] = []
    missing: list[str] = []
    for _group, key, title, _pages in MATTER_SECTIONS:
        item = (book.get(matter_group(key)) or {}).get(key) or {}
        body = (item.get("body") or "").strip()
        if not body:
            missing.append(key)
            continue
        # Başlık tek yerden gelir; book.json'daki kopya AYRIŞMIŞSA kusurdur.
        stored = (item.get("title") or "").strip()
        if stored and stored != title:
            print(f"[FAIL] {key}: book.json başlığı '{stored}', "
                  f"MATTER_SECTIONS '{title}' — ayrışma")
            return 1
        rows.append(build_one(key, title, body, edition))

    if not rows:
        print("ATLANDI: yazılmış ön/arka madde yok.")
        return 2

    used = sum(r["pages"] for r in rows)
    budget = sum(MATTER_PAGES[r["key"]] for r in rows)
    over = [r for r in rows if r["pages"] > r["budget"]]

    if verbose:
        print("=" * 78)
        print("ÖN VE ARKA MADDE — GERÇEK DİZGİ ÖLÇÜMÜ")
        print("=" * 78)
        print(f"  baskı: {edition}\n")
        print(f"  {'bölüm':<16}{'kelime':>8}{'sayfa':>8}{'slot':>7}"
              f"{'içerik':>9}   durum")
        for r in rows:
            state = "AŞTI" if r["pages"] > r["budget"] else "ok"
            print(f"  {r['key']:<16}{r['words']:>8}{r['pages']:>8}"
                  f"{r['budget']:>7}{r['contentPages']:>9.2f}   {state}")
        print(f"\n  {'toplam':<16}{sum(r['words'] for r in rows):>8}"
              f"{used:>8}{budget:>7}")
        if missing:
            print(f"\n  yazılmamış: {', '.join(missing)}")
        print(f"\n  yapısal ön madde (başlık · künye · ithaf · içindekiler · "
              f"harita): {MATTER_STRUCTURAL_PAGES} sayfa")

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        json.dump({
            "edition": edition,
            "sections": rows,
            "missing": missing,
            "pagesUsed": used,
            "pagesBudget": budget,
            "structuralPages": MATTER_STRUCTURAL_PAGES,
        }, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    # Ölçüm depoda kalır: proza dışarıda yaşar, SAYI içeride (D38/D51).
    # Bu dosyanın TEK yazarı bu betiktir; `update_docs.py` yalnızca okur.
    # İki yazarlı bir ölçü dosyası, iki doğruluk kaynağıdır.
    with open(MEASURE_PATH, "w", encoding="utf-8") as fh:
        json.dump({
            "note": "Ön/arka maddenin ÖLÇÜSÜ. Proza içermez (karar A1/D29). "
                    "Üreten: 08_BUILD/matter_page.py --measure",
            "edition": edition,
            "sections": [
                {"key": r["key"], "words": r["words"], "pages": r["pages"],
                 "budget": r["budget"]}
                for r in rows
            ],
            "missing": missing,
            "pagesUsed": used,
            "pagesBudget": budget,
            "structuralPages": MATTER_STRUCTURAL_PAGES,
        }, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    if over:
        print()
        for r in over:
            print(f"[FAIL] {r['key']}: {r['pages']} sayfa, slot "
                  f"{r['budget']} — bütçe aşıldı")
        print("\n  Sayfa bütçesi 436'nın parçasıdır. Kısaltın; slotu "
              "büyütmek fiyat tablosunu bozar.")
        return 1

    if verbose:
        print(f"\n{len(rows)}/{len(MATTER_SECTIONS)} bölüm ölçüldü · "
              f"bütçe aşımı yok")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="kapı kipi — yalnızca sonuç")
    ap.add_argument("--edition", default="paperback")
    args = ap.parse_args()

    if args.measure or args.check:
        return measure(args.edition, verbose=not args.check)
    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
