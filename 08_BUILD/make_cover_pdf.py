"""
KDP'ye yüklenmeye hazır ciltsiz kapak PDF'i.
================================================================================
  * Sayfa kutusu TAM ölçüde  (13.0725 x 9.2500 inç — krem kâğıt, 329 sayfa)
  * Görsel 300 DPI, kayıpsız
  * Tüm metin CANLI VEKTÖR, fontlar gömülü ve alt kümelenmiş
  * Saydamlık yok, katman yok, dış bağlantı yok

Aynı betik iki dosya üretir:
  03_COVER/<SÜRÜM>/exports/…_<SÜRÜM>_<kâğıt>_KDP.pdf   ← yüklenecek dosya
  03_COVER/<SÜRÜM>/proofs/…_<SÜRÜM>_<kâğıt>_PROOF.pdf  ← kılavuzlu kontrol

Kalibre edilmemiş ciltlemede export adı _KDP yerine _PROVISIONAL olur.

reportlab'in orijini SOL-ALT; bu proje SOL-ÜST kullanır. Dönüşüm tek yerde
(_y fonksiyonu) yapılır ki koordinat karışıklığı imkânsız olsun.
"""

from __future__ import annotations
import argparse
import os
import sys

from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cover_spec as S       # noqa: E402
import typography as T       # noqa: E402
import editions as E         # noqa: E402
import paths as P            # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PT = 72.0

PDF_FONT = {
    "cinzel-500": "CinzelC-Med",
    "cinzel-400": "CinzelC-Reg",
    "garamond-400": "GaramondC-Reg",
    "garamond-italic-400": "GaramondC-It",
}


def register_fonts(fb: T.FontBook):
    for key, pdfname in PDF_FONT.items():
        pdfmetrics.registerFont(TTFont(pdfname, fb[key].path))
    # reportlab her Canvas'ı Helvetica ile başlatır ve bu font hiç kullanılmasa
    # bile sayfanın kaynak sözlüğüne GÖMÜLMEDEN yazılır. KDP gömülü olmayan
    # fontu reddeder. Temel fontu kendi gömülü fontumuzla değiştiriyoruz.
    from reportlab import rl_config
    rl_config.canvas_basefontname = PDF_FONT["cinzel-400"]


def draw_text(c, b: T.TextBox, fb: T.FontBook, H: float):
    """Bir metin kutusunu çizer. H = kapak yüksekliği (inç)."""
    def _y(y_in):                       # üst-orijin → PDF alt-orijin
        return (H - y_in) * PT

    face = fb[b.font]
    char_space = b.tracking_em * b.size_pt

    def _put(x_pt, y_pt, s):
        """Harf aralıklı tek satır. reportlab'de harf aralığı yalnızca metin
        nesnesinde ayarlanabilir — canvas'ta setCharSpace yoktur.

        setCharSpace HER ZAMAN çağrılır, sıfır olsa bile: reportlab bu değeri
        canvas'ın grafik durumunda taşır, aksi hâlde önceki kutunun aralığı
        sonrakine sızar (arka kapak metni sırtın üstünden taşmıştı)."""
        to = c.beginText(x_pt, y_pt)
        to.setFont(PDF_FONT[b.font], b.size_pt)
        to.setFillColor(HexColor(b.color))
        to.setCharSpace(char_space)
        to.textOut(s)
        c.drawText(to)

    if b.rotation == -90:
        # Sırt: yukarıdan aşağı okunur (ABD/İngiltere standardı).
        # rotate(-90) sonrası metin aşağı akar, glif üstü sağa bakar; bu yüzden
        # büyük harf yüksekliği sırt ENİNDE yer kaplar → yarısı kadar sola kay.
        c.saveState()
        c.translate((b.x - b.h / 2) * PT, _y(b.y))
        c.rotate(-90)
        _put(0, 0, b.text)
        c.restoreState()

    elif b.lines:
        y = b.y
        for ln in b.lines:
            _put(b.x * PT, _y(y), ln)
            y += b.leading_pt / PT

    else:
        w = face.width(b.text, b.size_pt, b.tracking_em)
        x = {"left": b.x, "center": b.x - w / 2, "right": b.x - w}[b.align]
        _put(x * PT, _y(b.y), b.text)


def draw_guides(c, g: S.CoverGeometry, boxes, H: float):
    def _y(y_in):
        return (H - y_in) * PT

    def rect(r, col, w=1.0, dash=None):
        c.setStrokeColor(HexColor(col)); c.setLineWidth(w)
        c.setDash(dash or [])
        c.rect(r.x * PT, _y(r.y2), r.w * PT, r.h * PT, stroke=1, fill=0)
        c.setDash([])

    rect(S.Rect(0, 0, g.cover_w, g.cover_h), "#FF3B30", 1.5)
    rect(g.trim, "#FF3B30", 1.5)
    # katlama / menteşe çizgileri
    c.setStrokeColor(HexColor("#00B0FF")); c.setLineWidth(1.5)
    for x in (g.spine.x, g.spine.x2):
        c.line(x * PT, 0, x * PT, g.cover_h * PT)
    if g.hinge_back.w > 0:      # ciltli: menteşe oluğunun dış kenarları
        c.setStrokeColor(HexColor("#AF52DE")); c.setLineWidth(1.2)
        c.setDash([8, 4])
        for x in (g.hinge_back.x, g.hinge_front.x2):
            c.line(x * PT, 0, x * PT, g.cover_h * PT)
        c.setDash([])
    for r in (g.back_safe, g.front_safe, g.spine_safe):
        rect(r, "#34C759", 1.0, [6, 4])
    c.setStrokeColor(HexColor("#FFD60A")); c.setLineWidth(1.5)
    c.setFillColor(HexColor("#FFD60A")); c.setFillAlpha(0.15)
    c.rect(g.barcode.x * PT, _y(g.barcode.y2), g.barcode.w * PT,
           g.barcode.h * PT, stroke=1, fill=1)
    c.setFillAlpha(1)
    rect(g.barcode_mirror, "#FFD60A", 1.0, [3, 3])

    c.setStrokeColor(HexColor("#FF00FF")); c.setLineWidth(0.7)
    c.setDash([4, 3])
    for b in boxes:
        x1, y1, x2, y2 = T.bbox_of(b)
        c.rect(x1 * PT, _y(y2), (x2 - x1) * PT, (y2 - y1) * PT, stroke=1, fill=0)
    c.setDash([])

    c.setFont(PDF_FONT["cinzel-400"], 7)
    c.setFillColor(HexColor("#FF00FF"))
    for b in boxes:
        x1, y1, x2, y2 = T.bbox_of(b)
        c.drawString(x1 * PT, _y(y1) + 3,
                     f"{b.id} · {b.font} · {b.size_pt:.1f}pt")


def build(paper: str, proof: bool = False, edition: str = "paperback") -> str:
    ed = E.get(edition)
    g = S.geometry_for(ed, paper=paper)
    fb = T.FontBook().build()
    problems = fb.check_glyphs()
    if problems:
        raise SystemExit("EKSİK GLİF:\n  " + "\n  ".join(problems))
    register_fonts(fb)
    boxes = T.layout(fb, g)

    plate = P.cover_plate(ed, paper, S.DPI)
    if not os.path.exists(plate):
        raise SystemExit(f"plaka yok: {P.rel(plate)}\n"
                         f"önce: python3 08_BUILD/make_cover_art.py "
                         f"--edition {edition} --all-papers")

    # Kalibre edilmemiş ciltleme profiliyle üretilen kapak KDP'ye yüklenmemeli;
    # bunu dosya ADINDA taşımak, yanlış dosyanın yüklenmesini imkânsız kılar.
    provisional = not g.calibrated
    if proof:
        out = P.cover_proof_pdf(ed, paper)
    else:
        out = P.cover_pdf(ed, paper, provisional=provisional)

    W, H = g.cover_w * PT, g.cover_h * PT
    c = rl_canvas.Canvas(out, pagesize=(W, H), pageCompression=1)
    c.setTitle(f"Codex Mythologica — {ed.label} kapak ({paper}, {g.page_count}s)")
    c.setAuthor("Emre Doğan")
    c.setSubject(f"KDP {g.binding} full cover · trim {ed.trim_w}x{ed.trim_h}in · "
                 f"spine {g.spine_w:.4f}in · {paper} paper")
    c.setCreator("08_BUILD/make_cover_pdf.py")

    c.drawImage(ImageReader(plate), 0, 0, width=W, height=H,
                preserveAspectRatio=False, mask=None)

    for b in boxes:
        draw_text(c, b, fb, g.cover_h)

    if proof:
        draw_guides(c, g, boxes, g.cover_h)

    c.showPage()
    c.save()

    flag = "  ⚠ PROVISIONAL — kalibrasyon gerekiyor" if (provisional and not proof) else ""
    print(f"  → {P.rel(out)}  ({os.path.getsize(out)/1e6:.2f} MB)  "
          f"{g.cover_w:.4f}x{g.cover_h:.4f} in{flag}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    E.add_argument(ap)
    ap.add_argument("--paper", default=None, choices=list(S.PAPER_THICKNESS))
    ap.add_argument("--all-papers", action="store_true")
    ap.add_argument("--no-proof", action="store_true")
    a = ap.parse_args()
    ed = E.get(a.edition)
    for paper in (ed.papers if a.all_papers else [a.paper or ed.paper]):
        print(f"\n=== {ed.slug} · {paper.upper()} ===")
        build(paper, proof=False, edition=a.edition)
        if not a.no_proof:
            build(paper, proof=True, edition=a.edition)
