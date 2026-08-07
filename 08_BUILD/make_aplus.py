"""
A+ MODÜLLERİNİ ÜRETİR — PDF (vektör) · PNG · JPEG · SVG ana kaynak.
================================================================================
TEK RENDER, ÜÇ BİÇİM
    Tipografi yalnızca bir kez, reportlab ile VEKTÖR olarak çizilir. PNG'ler bu
    PDF'ten pdftoppm ile rasterlenir. Böylece PDF, PNG@1x ve PNG@2x birbirinin
    matematiksel olarak aynı çıktısıdır — biçimler arası kayma imkânsızdır.
    (Kapak boru hattında aynı ilke uygulandı.)

    Sayfa = modül ölçüsü kadar PUNTO (970×600 pt). 72 DPI'da rasterlenirse
    970×600 px, 144 DPI'da 1940×1200 px verir.

ÇIKTI
    03_APLUS/exports/<key>.pdf          baskı kalitesinde, fontlar gömülü
    03_APLUS/exports/<key>@1x.png       Amazon'a yüklenecek (≤2 MB)
    03_APLUS/exports/<key>@2x.png       retina yedeği
    03_APLUS/exports/<key>@1x.jpg       PNG 2 MB'ı aşarsa alternatif
    03_APLUS/masters/<key>.svg          düzenlenebilir ana kaynak
    03_APLUS/spec/aplus-typography.json tipografi belirtimi
    03_APLUS/spec/aplus-bboxes.json     sınırlayıcı kutu belirtimi

Kullanım: python3 08_BUILD/make_aplus.py
"""

from __future__ import annotations
import html
import json
import os
import subprocess
import sys

from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aplus_spec as A          # noqa: E402
import aplus_copy as C          # noqa: E402
import aplus_layout as L        # noqa: E402
import typography as T          # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "03_APLUS")
PLATES = os.path.join(ROOT, "07_ASSETS", "aplus_plates")

PDF_FONT = {
    "cinzel-500": "CinzelC-Med", "cinzel-400": "CinzelC-Reg",
    "garamond-400": "GaramondC-Reg", "garamond-italic-400": "GaramondC-It",
}
FAM = {"cinzel-500": ("CinzelC", 500, "normal"),
       "cinzel-400": ("CinzelC", 400, "normal"),
       "garamond-400": ("GaramondC", 400, "normal"),
       "garamond-italic-400": ("GaramondC", 400, "italic")}

E = lambda s: html.escape(str(s), quote=True)   # noqa: E731


def register(fb: T.FontBook):
    for k, name in PDF_FONT.items():
        pdfmetrics.registerFont(TTFont(name, fb[k].path))
    # reportlab her Canvas'ı Helvetica ile başlatır ve o font gömülmeden
    # sayfaya yazılır; temel fontu kendi gömülü fontumuzla değiştiriyoruz.
    from reportlab import rl_config
    rl_config.canvas_basefontname = PDF_FONT["cinzel-400"]


# =============================================================================
# PDF
# =============================================================================

def render_pdf(mod: dict, fb: T.FontBook, path: str):
    W, H = float(mod["w"]), float(mod["h"])
    c = rl_canvas.Canvas(path, pagesize=(W, H), pageCompression=1)
    c.setTitle(f"Codex Mythologica — A+ {mod['key']}")
    c.setAuthor("Emre Doğan")
    c.setSubject(mod["alt_text"])
    c.setCreator("08_BUILD/make_aplus.py")

    plate = os.path.join(PLATES, f"{mod['key']}@{A.RETINA_SCALE}x.png")
    c.drawImage(ImageReader(plate), 0, 0, width=W, height=H,
                preserveAspectRatio=False, mask=None)

    def _y(v):                       # üst-orijin → PDF alt-orijin
        return H - v

    for b in mod["blocks"]:
        face = fb[b["font"]]
        cs = b["tracking_em"] * b["size_pt"]

        if b.get("rule"):
            r = b["rule"]
            c.setStrokeColor(HexColor(A.RULE))
            c.setLineWidth(max(0.6, W / 1400))
            c.line(r["x1"], _y(r["y"]), r["x2"], _y(r["y"]))

        y = b["y"]
        for ln in b["lines"]:
            w = face.width(ln, b["size_pt"], b["tracking_em"]) * 72
            if b["align"] == "center":
                x = b["x"] - w / 2
            elif b["align"] == "right":
                x = b["x"] - w
            else:
                x = b["x"]
            to = c.beginText(x, _y(y))
            to.setFont(PDF_FONT[b["font"]], b["size_pt"])
            to.setFillColor(HexColor(b["color"]))
            to.setCharSpace(cs)      # sıfır olsa bile: reportlab durumu taşır
            to.textOut(ln)
            c.drawText(to)
            y += b["leading_pt"]

    c.showPage()
    c.save()


# =============================================================================
# SVG ana kaynak
# =============================================================================

def render_svg(mod: dict, path: str):
    W, H = mod["w"], mod["h"]
    plate = f"../../07_ASSETS/aplus_plates/{mod['key']}@{A.RETINA_SCALE}x.png"
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" '
         f'xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" '
         f'width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<title>Codex Mythologica — A+ {E(mod["key"])}</title>',
         f'<desc>{E(mod["alt_text"])}</desc>',
         '<defs><style type="text/css"><![CDATA[']
    for key, fn in (("CinzelC", "cinzel-500"), ("CinzelC", "cinzel-400"),
                    ("GaramondC", "garamond-400"),
                    ("GaramondC", "garamond-italic-400")):
        fam, wt, st = FAM[fn]
        o.append(f'  @font-face{{font-family:"{fam}";'
                 f'src:url("../../07_ASSETS/fonts/static/{fn}.ttf") '
                 f'format("truetype");font-weight:{wt};font-style:{st}}}')
    o.append(']]></style></defs>')
    o.append(f'<image xlink:href="{plate}" href="{plate}" x="0" y="0" '
             f'width="{W}" height="{H}" preserveAspectRatio="none"/>')
    o.append('<g id="typography">')
    for b in mod["blocks"]:
        fam, wt, st = FAM[b["font"]]
        anchor = {"left": "start", "center": "middle", "right": "end"}[b["align"]]
        if b.get("rule"):
            r = b["rule"]
            o.append(f'  <line x1="{r["x1"]:.2f}" y1="{r["y"]:.2f}" '
                     f'x2="{r["x2"]:.2f}" y2="{r["y"]:.2f}" '
                     f'stroke="{A.RULE}" stroke-width="0.8"/>')
        o.append(f'  <text id="{E(b["id"])}" font-family="{fam}" '
                 f'font-weight="{wt}" font-style="{st}" '
                 f'font-size="{b["size_pt"]:.3f}" fill="{b["color"]}" '
                 f'letter-spacing="{b["tracking_em"]*b["size_pt"]:.4f}" '
                 f'text-anchor="{anchor}" x="{b["x"]:.2f}" y="{b["y"]:.2f}">')
        for i, ln in enumerate(b["lines"]):
            dy = 0 if i == 0 else b["leading_pt"]
            o.append(f'    <tspan x="{b["x"]:.2f}" dy="{dy:.3f}">{E(ln)}</tspan>')
        o.append('  </text>')
    o.append('</g></svg>')
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(o))


# =============================================================================
# raster
# =============================================================================

def rasterise(pdf: str, base: str, scale: int) -> dict:
    dpi = 72 * scale
    tmp = f"{base}.tmp"
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", "-singlefile",
                    pdf, tmp], check=True, capture_output=True)
    src = tmp + ".png"
    png = f"{base}@{scale}x.png"
    im = Image.open(src).convert("RGB")
    im.save(png, "PNG", optimize=True)
    jpg = f"{base}@{scale}x.jpg"
    im.save(jpg, "JPEG", quality=92, optimize=True, progressive=True)
    os.remove(src)
    return {"png": png, "png_bytes": os.path.getsize(png),
            "jpg": jpg, "jpg_bytes": os.path.getsize(jpg),
            "size": im.size}


# =============================================================================
# ana akış
# =============================================================================

def main():
    fb = T.FontBook().build()
    probs = fb.check_glyphs()
    if probs:
        raise SystemExit("EKSİK GLİF:\n  " + "\n  ".join(probs))
    register(fb)

    for d in ("exports", "masters", "spec"):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)

    lay = L.build(fb)
    typo, bboxes, summary = [], [], []

    print("=" * 92)
    print("A+ MODÜLLERİ")
    print("=" * 92)

    for mod in lay["modules"]:
        key = mod["key"]
        pdf = os.path.join(OUT, "exports", f"{key}.pdf")
        render_pdf(mod, fb, pdf)
        render_svg(mod, os.path.join(OUT, "masters", f"{key}.svg"))

        base = os.path.join(OUT, "exports", key)
        r1 = rasterise(pdf, base, 1)
        r2 = rasterise(pdf, base, A.RETINA_SCALE)

        upload = "PNG" if r1["png_bytes"] <= A.MAX_BYTES else "JPEG"
        summary.append({
            "key": key, "type": mod["type"], "size": [mod["w"], mod["h"]],
            "pdf_bytes": os.path.getsize(pdf),
            "png1x_bytes": r1["png_bytes"], "jpg1x_bytes": r1["jpg_bytes"],
            "png2x_bytes": r2["png_bytes"], "jpg2x_bytes": r2["jpg_bytes"],
            "upload_format": upload,
            "upload_file": os.path.relpath(
                r1["png"] if upload == "PNG" else r1["jpg"], ROOT),
            "alt_text": mod["alt_text"], "collisions": mod["collisions"],
        })
        typo.append({"key": key, "blocks": [
            {k: b[k] for k in ("id", "style", "font", "size_pt",
                               "tracking_em", "leading_pt", "color",
                               "align", "x", "y", "box_w", "cap", "lines")}
            for b in mod["blocks"]]})
        bboxes.append({"key": key, "module": [mod["w"], mod["h"]],
                       "boxes": [{"id": b["id"], "bbox": b["bbox"],
                                  "height": b["height"],
                                  "lines": len(b["lines"])}
                                 for b in mod["blocks"]]})

        flag = "✓" if r1["png_bytes"] <= A.MAX_BYTES else "→ JPEG"
        print(f"\n── {key}  {mod['w']}×{mod['h']}  ({mod['type']})")
        print(f"   PDF {os.path.getsize(pdf)/1024:7.0f} KB · "
              f"PNG@1x {r1['png_bytes']/1024:7.0f} KB {flag} · "
              f"JPG@1x {r1['jpg_bytes']/1024:6.0f} KB")
        print(f"   PNG@2x {r2['png_bytes']/1024:7.0f} KB · "
              f"JPG@2x {r2['jpg_bytes']/1024:6.0f} KB · "
              f"{len(mod['blocks'])} metin bloğu")
        if mod["collisions"]:
            print(f"   ⚠ çakışma: {', '.join(mod['collisions'])}")

    with open(os.path.join(OUT, "spec", "aplus-typography.json"), "w",
              encoding="utf-8") as f:
        json.dump({"type_scale": A.TYPE_SCALE, "leading": A.LEADING,
                   "colors": {"gold": A.GOLD, "gold_light": A.GOLD_LIGHT,
                              "parchment": A.PARCHMENT, "dim": A.DIM,
                              "rule": A.RULE},
                   "modules": typo}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT, "spec", "aplus-bboxes.json"), "w",
              encoding="utf-8") as f:
        json.dump({"origin": "modülün sol ÜST köşesi; birim punto (= @1x piksel)",
                   "modules": bboxes}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT, "spec", "aplus-manifest.json"), "w",
              encoding="utf-8") as f:
        json.dump({"limits": {"max_bytes": A.MAX_BYTES,
                              "formats": list(A.ACCEPTED_FORMATS),
                              "color_space": A.COLOR_SPACE},
                   "modules": summary,
                   "author_bio": C.AUTHOR_BIO}, f, ensure_ascii=False, indent=2)

    print(f"\n→ 03_APLUS/exports/ · masters/ · spec/")


if __name__ == "__main__":
    main()
