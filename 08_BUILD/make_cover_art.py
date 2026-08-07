"""
Sanat eserini tam KDP tuvaline yerleştirir.
================================================================================
GİRDİ : 03_COVER/artwork/paperback-artwork-textless.png   (1472 x 1069, metinsiz)
ÇIKTI : 03_COVER/artwork/cover-plate-<kâğıt>-300dpi.png    (3922 x 2775)

Tasarım DEĞİŞTİRİLMEZ. Yalnızca:
  * tek ve aynı ölçek çarpanı (X ve Y'de eşit — eski dosyadaki kaymanın kökü)
  * sırt bandının merkezi, hesaplanmış sırt merkezine oturur
  * taşma alanı gerçek görselle dolar (beyaz kenar / uzatma yok)

Kullanım:
    python3 08_BUILD/make_cover_art.py [--paper cream|white] [--no-sharpen]
"""

from __future__ import annotations
import argparse
import os
import sys

from PIL import Image, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cover_spec as S  # noqa: E402
import editions as E     # noqa: E402
import paths as P        # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(paper: str = S.PAPER, sharpen: bool = True, dpi: int = S.DPI,
          edition: str = "paperback") -> str:
    ed = E.get(edition)
    g = S.geometry_for(ed, paper=paper, dpi=dpi)
    p = S.art_placement(g, dpi=dpi)
    CW, CH = g.canvas_px

    src = os.path.join(ROOT, S.ART_FILE)
    art = Image.open(src)
    if art.size != (S.ART_W, S.ART_H):
        raise SystemExit(
            f"Görsel boyutu beklenenden farklı: {art.size} != "
            f"{(S.ART_W, S.ART_H)}.\n"
            f"Görsel değiştiyse cover_spec.py içindeki ART_W/ART_H ve "
            f"ART_SPINE_CENTER_FRAC değerlerini audit_cover.py ile yeniden ölçün.")

    # Alfa varsa siyah üzerine düzleştir (kapakta saydamlık olamaz)
    if art.mode in ("RGBA", "LA", "P"):
        art = art.convert("RGBA")
        flat = Image.new("RGB", art.size, (0, 0, 0))
        flat.paste(art, mask=art.split()[-1])
        art = flat
    else:
        art = art.convert("RGB")

    sw, sh = int(round(p.scaled_w)), int(round(p.scaled_h))
    art = art.resize((sw, sh), Image.LANCZOS)

    # 2.77x yükseltmenin yumuşamasını dengeler. Hale yapmayacak kadar hafif.
    if sharpen:
        art = art.filter(ImageFilter.UnsharpMask(radius=2.2, percent=55, threshold=3))

    canvas = Image.new("RGB", (CW, CH), (0, 0, 0))
    canvas.paste(art, (int(round(p.offset_x)), int(round(p.offset_y))))

    out = os.path.join(P.cover_dir(ed, "plates"),
                       f"cover-plate-{paper}-{dpi}dpi.png")
    canvas.save(out, "PNG", dpi=(dpi, dpi), optimize=True)

    print(f"  sürüm        : {ed.label} ({g.profile.label})")
    print(f"  kâğıt        : {paper}   sırt {g.spine_w:.4f} inç")
    print(f"  tuval        : {CW} x {CH} px  = {g.cover_w:.4f} x {g.cover_h:.4f} inç")
    print(f"  ölçek        : {p.scale:.6f}  (X ve Y eşit)")
    print(f"  yerleşim     : offset ({p.offset_x:.0f}, {p.offset_y:.0f}) px")
    print(f"  kırpma       : sol {p.crop_left:.0f}  sağ {p.crop_right:.0f}  "
          f"üst {p.crop_top:.0f}  alt {p.crop_bottom:.0f} px")
    print(f"  altın fileto : {p.rule_l_in:.4f} / {p.rule_r_in:.4f} inç "
          f"→ kattan {p.rule_inset_in*25.4:.2f} mm içeride")
    print(f"  yerel çöz.   : {p.native_ppi} PPI  (yükseltildi → {dpi} PPI)")
    print(f"  → {os.path.relpath(out, ROOT)}  "
          f"({os.path.getsize(out)/1e6:.2f} MB)")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    E.add_argument(ap)
    ap.add_argument("--paper", default=None, choices=list(S.PAPER_THICKNESS))
    ap.add_argument("--no-sharpen", action="store_true")
    ap.add_argument("--all-papers", action="store_true",
                    help="sürümün tanımlı bütün kâğıt varyantlarını üret")
    a = ap.parse_args()
    ed = E.get(a.edition)
    papers = ed.papers if a.all_papers else [a.paper or ed.paper]
    for pp in papers:
        print(f"\n=== {ed.slug} · {pp.upper()} ===")
        build(paper=pp, sharpen=not a.no_sharpen, edition=a.edition)
