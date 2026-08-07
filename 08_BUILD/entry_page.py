#!/usr/bin/env python3
"""
CODEX BESTIARIUM — MADDE SAYFASI TASARIMI VE PROVA DİZGİSİ
================================================================================
Yol haritası Faz 2, dizgi görevleri:

    · Madde başlığı bloğu (Cinzel 500 · 16 pt · 0,06 em aralık + altında
      gelenek · sınıf · motif satırı)
    · Sınıf işareti (dış üst köşe, Cinzel 8 pt, %30 opaklık)
    · Akraba satırı stili (0,4 pt altın fileto + EB Garamond 9,5 pt)
    · **Bir madde sayfasının prova dizgisi** — plaka + başlık bloğu + yedi
      bölüm gerçekten sığıyor mu?

SON SORU EN ÖNEMLİSİ. Sayfa bütçesi (madde başına 2,5 sayfa) bir MODELDİR;
model 112 maddeyi 280 sayfaya, kitabı 380 sayfaya ve fiyatı bir bandın içine
koyuyor. Model yanlışsa bu Faz 6'da değil ŞİMDİ bilinmelidir — Faz 6'da
müdahale etmek bütün metni yeniden akıtmak demektir.

PROZA YOK
    Bu faz proza yazmaz. Prova, bölüm bantlarının ORTA NOKTASINDA üretilmiş
    ölçüm dolgusuyla dizilir (`tests/make_fixtures.py` ile aynı üreteç).
    Ölçülen şey geometridir, üslup değil.

KULLANIM
    python3 08_BUILD/entry_page.py --proof                # PDF üret + ölç
    python3 08_BUILD/entry_page.py --proof --id kerberos
    python3 08_BUILD/entry_page.py --check                # bütçeyi denetle
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    ENTRY_SECTIONS,
    REPORT_DIR,
    ROOT,
    WORD_TARGET,
    Result,
    load_spec,
)

PROOF_DIR = os.path.join(ROOT, "04_PRINT", "PROOF")
PROOF_REPORT = os.path.join(REPORT_DIR, "entry-page-proof.json")

# --- madde sayfası şartnamesi (yol haritası Bölüm 05.2 · Faz 2) -----------
# Bütün sayılar burada; `entry_style()` bunlardan ParagraphStyle üretir.
ENTRY_SPEC = {
    # Başlık bloğu
    "title_font": "Cinzel",
    "title_pt": 16.0,
    "title_tracking_em": 0.06,      # 0,96 pt @ 16 pt
    "meta_font": "Gara",
    "meta_pt": 9.5,
    "meta_color": "#555555",
    # Sınıf işareti — dış üst köşe
    "classmark_font": "Cinzel",
    "classmark_pt": 8.0,
    "classmark_opacity": 0.30,
    # Akraba satırı (6. bölüm)
    "kin_rule_pt": 0.4,
    "kin_rule_color": "#8A6E2F",    # altın fileto
    "kin_font": "Gara",
    "kin_pt": 9.5,
    # Plaka — madde sayfasının ÜST YARISI (STYLE_PLATES § 7.2)
    "plate_height_frac": 0.50,      # metin bloğunun yüksekliğine oran
    "plate_aspect": 1.25,           # 1:1,25 dikey
    "plate_gap_pt": 14.0,           # plaka ile başlık bloğu arası
}

# Sayfa bütçesi — `classify.py` ile AYNI sayı olmak zorunda; ayrışırsa bu
# betik kırmızı yanar. Değer bir model değil, bu betiğin ÖLÇÜMÜDÜR.
PAGES_PER_ENTRY = 3.0

# Ölçülen içerik yüksekliği bu bandın içinde olmalı. Üst sınır PAGES_PER_ENTRY
# olmalıdır: aşarsa madde dördüncü sayfaya taşar ve bütçe kayar. Alt sınır,
# bütçenin gereksiz yere şişmediğini gösterir.
CONTENT_BAND = (2.0, 3.0)


def _require_reportlab():
    try:
        import reportlab  # noqa: F401
    except ImportError as exc:
        raise SystemExit(
            "HATA: prova dizgisi reportlab gerektirir.\n"
            "      ./08_BUILD/bootstrap.sh çalıştırın.\n"
            f"      ({exc})"
        )


# =============================================================================
# STİL
# =============================================================================

def entry_styles(L):
    """Madde sayfasının stilleri. `make_pdf.Layout`'un gövde stilini devralır."""
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    from reportlab.lib.styles import ParagraphStyle

    s = ENTRY_SPEC
    k = L.ed.display_scale
    ink = "#111111"
    return {
        "title": ParagraphStyle(
            "entry_title", fontName=s["title_font"], fontSize=s["title_pt"] * k,
            leading=s["title_pt"] * k * 1.30, alignment=TA_CENTER,
            textColor=ink, spaceAfter=3 * k,
        ),
        "meta": ParagraphStyle(
            "entry_meta", fontName=s["meta_font"], fontSize=s["meta_pt"] * k,
            leading=s["meta_pt"] * k * 1.45, alignment=TA_CENTER,
            textColor=s["meta_color"], spaceAfter=11 * k,
        ),
        "opening": ParagraphStyle(
            "entry_opening", fontName="GaraIt", fontSize=L.BODY_PT,
            leading=L.LEAD_PT, alignment=TA_JUSTIFY, textColor=ink,
            firstLineIndent=0, spaceAfter=L.LEAD_PT * 0.35,
        ),
        "body": L.S["body"],
        "body1": L.S["body1"],
        "kin": ParagraphStyle(
            "entry_kin", fontName=s["kin_font"], fontSize=s["kin_pt"] * k,
            leading=s["kin_pt"] * k * 1.45, alignment=TA_JUSTIFY,
            textColor="#333333", spaceBefore=6 * k, spaceAfter=4 * k,
        ),
        "sources": ParagraphStyle(
            "entry_sources", fontName="GaraIt", fontSize=(s["kin_pt"] - 0.5) * k,
            leading=(s["kin_pt"] - 0.5) * k * 1.45, alignment=TA_JUSTIFY,
            textColor="#444444", spaceBefore=5 * k,
        ),
    }


def tracked(text: str, tracking_em: float, size_pt: float) -> str:
    """reportlab'de harf aralığı bir Paragraph özelliği değildir; `<font>`
    etiketiyle de verilemez. Tek taşınabilir yol, harfler arasına ince boşluk
    koymaktır — 0,06 em'lik aralık başlıkta böyle kurulur."""
    space = f'<font size="{size_pt * tracking_em:.2f}"> </font>'
    return space.join(text)


# =============================================================================
# AKIŞ
# =============================================================================

def plate_box(L) -> tuple[float, float]:
    """(genişlik, yükseklik) — plaka madde sayfasının üst yarısına oturur.

    Kısıt çift yönlüdür: yükseklik metin bloğunun yarısını geçemez, genişlik
    de metin sütununu. 1:1,25 dikey oranda ikisinden hangisi bağlarsa o
    belirler.
    """
    # `Edition.text_w/text_h` İNÇ döner; buradaki hesap PUANLA yapılır.
    max_h = L.ed.text_h * 72.0 * ENTRY_SPEC["plate_height_frac"]
    max_w = L.ed.text_w * 72.0
    h = min(max_h, max_w * ENTRY_SPEC["plate_aspect"])
    w = h / ENTRY_SPEC["plate_aspect"]
    return w, h


def entry_flow(rec: dict, spec: dict, sections: dict, L, S) -> list:
    """Bir maddenin akış nesneleri: plaka kutusu · başlık bloğu · yedi bölüm."""
    from reportlab.platypus import Paragraph, Spacer
    from reportlab.platypus.flowables import Flowable

    s = ENTRY_SPEC
    k = L.ed.display_scale
    trads = {t["id"]: t for t in spec["traditions"]}
    classes = {c["id"]: c for c in spec["classes"]}
    kin = {f["id"]: f for f in spec["kinFamilies"]}
    by_id = {c["id"]: c for c in spec["creatures"]}

    class PlateFrame(Flowable):
        """Plakanın yerini tutan çerçeve.

        Faz 2'de gerçek plaka YOKTUR ve olmamalıdır — pilot set kilidi
        açılmadan üretim plakası çizilmez. Ama plakanın KAPLADIĞI ALAN
        şimdiden ölçülmelidir; sayfa bütçesi buna bağlıdır. Çerçeve tam
        o alanı kaplar.
        """

        def __init__(self, w, h, label):
            super().__init__()
            self.width, self.height = w, h
            self.label = label

        def draw(self):
            c = self.canv
            c.saveState()
            c.setStrokeColor("#BBBBBB")
            c.setLineWidth(0.4)
            c.setDash(3, 3)
            c.rect(0, 0, self.width, self.height)
            c.setDash()
            c.setFillColor("#999999")
            c.setFont("Cinzel", 7.5 * k)
            c.drawCentredString(self.width / 2, self.height / 2 - 3,
                                self.label)
            c.setFont("Gara", 7 * k)
            c.drawCentredString(self.width / 2, self.height / 2 - 14,
                                f"{self.width / 72:.2f} × {self.height / 72:.2f} in"
                                " · 1:1,25")
            c.restoreState()

    class GoldRule(Flowable):
        """Akraba satırının altın filetosu — 0,4 pt."""

        def __init__(self, w):
            super().__init__()
            self.width, self.height = w, s["kin_rule_pt"] + 4 * k

        def draw(self):
            c = self.canv
            c.saveState()
            c.setStrokeColor(s["kin_rule_color"])
            c.setLineWidth(s["kin_rule_pt"])
            c.line(0, 2 * k, self.width, 2 * k)
            c.restoreState()

    flow: list = []
    pw, ph = plate_box(L)
    flow.append(PlateFrame(pw, ph, rec["plate"].upper()))
    flow.append(Spacer(1, s["plate_gap_pt"] * k))

    flow.append(Paragraph(
        tracked(rec["name"], s["title_tracking_em"], s["title_pt"] * k),
        S["title"]))

    trad = trads.get(rec["tradition"], {})
    klass = classes.get(rec["class"], {})
    meta = (f"{trad.get('name', '?')} {trad.get('sigil', '')} &nbsp;·&nbsp; "
            f"{rec['class']} · {klass.get('en', '')} &nbsp;·&nbsp; "
            f"{' '.join(rec['motif'])}")
    if rec.get("pronunciation"):
        meta += f" &nbsp;·&nbsp; [{rec['pronunciation']}]"
    flow.append(Paragraph(meta, S["meta"]))

    for key, _label, _lo, _hi in ENTRY_SECTIONS:
        text = sections.get(key, "")
        if not text:
            continue
        if key == "opening":
            flow.append(Paragraph(text, S["opening"]))
        elif key == "kin":
            flow.append(GoldRule(L.ed.text_w * 72.0))
            fam = kin.get(rec.get("kinFamily"))
            lead = f"<b>{fam['en']}</b> — " if fam else ""
            names = ", ".join(
                by_id[r]["name"] for r in rec.get("crossRefs", []) if r in by_id
            )
            flow.append(Paragraph(f"{lead}{text} <i>See also:</i> {names}.",
                                  S["kin"]))
        elif key == "sources":
            flow.append(Paragraph(text, S["sources"]))
        else:
            style = S["body1"] if key == "where" else S["body"]
            flow.append(Paragraph(text, style))
    return flow


# =============================================================================
# PROVA
# =============================================================================

def filler_sections() -> dict:
    """Bölüm bantlarının ORTA NOKTASINDA ölçüm dolgusu. Proza değil."""
    from tests.make_fixtures import body

    out = {}
    for i, (key, _label, lo, hi) in enumerate(ENTRY_SECTIONS):
        out[key] = body((lo + hi) // 2, seed=1009 + i * 37)
    return out


def build_proof(entry_id: str, edition: str, out_path: str) -> dict:
    """Bir maddeyi gerçekten dizer ve KAÇ SAYFA tuttuğunu ölçer."""
    _require_reportlab()
    import make_pdf as MP
    from reportlab.lib.units import inch as IN
    from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate,
                                    Paragraph)

    spec = load_spec()
    rec = next((c for c in spec["creatures"] if c["id"] == entry_id), None)
    if rec is None:
        raise SystemExit(f"HATA: madde yok: {entry_id}")

    L = MP.configure(edition)
    S = entry_styles(L)
    sections = filler_sections()
    words = sum(len(v.split()) for v in sections.values())

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    classes = {c["id"]: c for c in spec["classes"]}
    mark_text = f"{rec['class']} · {classes[rec['class']]['en']}"
    k = L.ed.display_scale

    def chrome(canvas, doc):
        """Sınıf işareti: DIŞ üst köşe, Cinzel 8 pt, %30 opaklık."""
        recto = canvas.getPageNumber() % 2 == 1
        x = (L.PW - L.OUTER) if recto else L.OUTER
        canvas.saveState()
        canvas.setFont(ENTRY_SPEC["classmark_font"],
                       ENTRY_SPEC["classmark_pt"] * k)
        canvas.setFillColor("#111111")
        canvas.setFillAlpha(ENTRY_SPEC["classmark_opacity"])
        y = L.PH - L.TOPM + 14 * k
        if recto:
            canvas.drawRightString(x, y, mark_text)
        else:
            canvas.drawString(x, y, mark_text)
        canvas.restoreState()

    doc = BaseDocTemplate(
        out_path, pagesize=(L.PW, L.PH),
        leftMargin=L.GUTTER, rightMargin=L.OUTER,
        topMargin=L.TOPM, bottomMargin=L.BOTM,
        title=f"{rec['name']} — prova dizgisi",
        author="Vâliçe Press", subject="Codex Bestiarium · Faz 2 prova",
    )
    frame = Frame(L.GUTTER, L.BOTM, L.ed.text_w * IN, L.ed.text_h * IN,
                  id="body",
                  leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="entry", frames=[frame],
                                       onPage=chrome)])
    flow = entry_flow(rec, spec, sections, L, S)

    # İçeriğin GERÇEK yüksekliği. Sayfa sayısı tam sayıya yuvarlar ve
    # bütçenin nerede israf edildiğini gizler; bu ölçüm göstermez.
    text_w_pt = L.ed.text_w * 72.0
    text_h_pt = L.ed.text_h * 72.0
    content_pt = 0.0
    heights = []
    for f in flow:
        sb = f.getSpaceBefore() if hasattr(f, "getSpaceBefore") else 0
        sa = f.getSpaceAfter() if hasattr(f, "getSpaceAfter") else 0
        _w, h = f.wrap(text_w_pt, text_h_pt)
        content_pt += sb + h + sa
        heights.append({"flowable": type(f).__name__,
                        "inches": round((sb + h + sa) / 72.0, 3)})

    doc.build(flow)

    pages = _page_count(out_path)
    pw, ph = plate_box(L)
    return {
        "contentPages": round(content_pt / text_h_pt, 3),
        "contentInches": round(content_pt / 72.0, 2),
        "flowHeights": heights,
        "id": rec["id"],
        "name": rec["name"],
        "edition": edition,
        "file": os.path.relpath(out_path, ROOT),
        "words": words,
        "wordTarget": WORD_TARGET,
        "pages": pages,
        "textWidthIn": round(L.ed.text_w, 3),
        "textHeightIn": round(L.ed.text_h, 3),
        "plateWidthIn": round(pw / 72.0, 3),
        "plateHeightIn": round(ph / 72.0, 3),
        "linesPerPage": L.ed.lines_per_page,
    }


def _page_count(path: str) -> int:
    try:
        from pypdf import PdfReader
    except ImportError:
        from PyPDF2 import PdfReader  # type: ignore
    return len(PdfReader(path).pages)


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--id", default="each-uisce",
                    help="prova dizilecek madde (varsayılan: vitrin maddesi)")
    ap.add_argument("--edition", default="paperback")
    ap.add_argument("--proof", action="store_true", help="PDF üret")
    ap.add_argument("--check", action="store_true",
                    help="sayfa bütçesi modeli tutuyor mu")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    out = os.path.join(PROOF_DIR, f"entry-{args.id}-{args.edition}.pdf")
    m = build_proof(args.id, args.edition, out)

    r = Result("MADDE SAYFASI PROVA DİZGİSİ (entry_page)")
    r.ok("prova dizildi",
         f"{m['name']} · {m['words']} kelime · {m['pages']} sayfa · "
         f"{m['file']}")
    r.ok("metin bloğu",
         f"{m['textWidthIn']} × {m['textHeightIn']} inç · "
         f"{m['linesPerPage']} satır/sayfa")
    r.ok("plaka alanı",
         f"{m['plateWidthIn']} × {m['plateHeightIn']} inç · 1:1,25 · "
         f"metin bloğunun üst %{ENTRY_SPEC['plate_height_frac'] * 100:.0f}'si")

    # ASIL SORU: plaka + başlık bloğu + yedi bölüm bütçeye sığıyor mu?
    lo, hi = CONTENT_BAND
    n = len(load_spec()["creatures"])
    r.add(
        lo <= m["contentPages"] <= hi,
        f"ölçülen içerik {lo}–{hi} sayfa bandında",
        f"ölçülen {m['contentPages']} sayfa ({m['contentInches']} inç) — "
        f"üst sınır aşılırsa madde dördüncü sayfaya taşar",
    )
    r.add(
        m["pages"] == int(PAGES_PER_ENTRY),
        f"dizilen sayfa sayısı bütçeyle birebir ({int(PAGES_PER_ENTRY)})",
        f"dizilen {m['pages']} · {n} madde → {m['pages'] * n} sayfa "
        f"(bütçe {int(PAGES_PER_ENTRY * n)})",
    )
    r.ok(
        "bütçe israfı",
        f"{PAGES_PER_ENTRY - m['contentPages']:.3f} sayfa/madde boş kalıyor — "
        f"plaka kuralının bedeli (madde sayfa başından başlamak zorunda); "
        f"{n} maddede {round((PAGES_PER_ENTRY - m['contentPages']) * n)} sayfa",
    )
    r.add(
        m["plateHeightIn"] + 0.4 < m["textHeightIn"],
        "plaka metin bloğuna sığıyor ve altında metin için yer kalıyor",
        f"plaka {m['plateHeightIn']} inç · metin bloğu {m['textHeightIn']} inç",
    )

    # Bütçe iki yerde yazılı; ayrışırlarsa hangisinin doğru olduğu bilinemez.
    import classify  # noqa: PLC0415

    r.add(
        classify.PAGES_PER_ENTRY == PAGES_PER_ENTRY,
        "sayfa bütçesi classify.py ile aynı",
        f"entry_page {PAGES_PER_ENTRY} · classify {classify.PAGES_PER_ENTRY}",
    )

    code = r.report(verbose=args.verbose)
    os.makedirs(REPORT_DIR, exist_ok=True)
    with open(PROOF_REPORT, "w", encoding="utf-8") as fh:
        json.dump({**m, "spec": ENTRY_SPEC, "pagesPerEntryModel": PAGES_PER_ENTRY,
                   "passed": len(r.passed), "failed": len(r.failures)},
                  fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"rapor: {os.path.relpath(PROOF_REPORT, ROOT)}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
