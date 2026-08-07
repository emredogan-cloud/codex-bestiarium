"""
Kod üretimli SVG ANA ŞABLON.
================================================================================
İki dosya üretir:

  1) 03_COVER/<SÜRÜM>/templates/cover-template-<kâğıt>-guides.svg
     Teknik şablon: taşma / kesim / katlama / güvenli alan / barkod kılavuzları
     + her metin bloğunun ölçülü yer tutucusu. Illustrator, Inkscape, Affinity
     veya Figma'da açılıp referans katman olarak kullanılabilir.

  2) 03_COVER/<SÜRÜM>/templates/cover-master-<kâğıt>.svg
     Düzenlenebilir ANA KAYNAK: yerleştirilmiş görsel + canlı vektör metin.
     Görsele göreli yolla bağlanır (dosya küçük ve düzenlenebilir kalsın diye).

Tüm koordinatlar cover_spec.py + typography.py'den gelir. Elle hiçbir sayı yok.
SVG kullanıcı birimi = 1 punto (1/72 inç); width/height inç olarak yazılır.
"""

from __future__ import annotations
import argparse
import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cover_spec as S       # noqa: E402
import typography as T       # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PT = 72.0

GUIDE = {
    "bleed": "#FF3B30",
    "trim": "#FF3B30",
    "fold": "#00B0FF",
    "safe": "#34C759",
    "barcode": "#FFD60A",
    "text": "#FF00FF",
}


def _esc(s: str) -> str:
    return html.escape(s, quote=True)


def _rect(r: S.Rect, stroke, w=1.0, dash=None, fill="none", label=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    out = (f'<rect x="{r.x*PT:.3f}" y="{r.y*PT:.3f}" '
           f'width="{r.w*PT:.3f}" height="{r.h*PT:.3f}" fill="{fill}" '
           f'stroke="{stroke}" stroke-width="{w}"{d}/>')
    if label:
        out += (f'\n  <text x="{(r.x+0.06)*PT:.3f}" y="{(r.y+0.20)*PT:.3f}" '
                f'font-family="monospace" font-size="7" fill="{stroke}">'
                f'{_esc(label)}</text>')
    return out


def _geo(paper, ed=None):
    """Sürüm verilmişse onun geometrisi (sayfa sayısı iç bloktan okunur)."""
    if ed is None:
        return S.geometry(paper=paper)
    return S.geometry_for(ed, paper=paper)


def guides_svg(paper: str, ed=None) -> str:
    g = _geo(paper, ed)
    p = S.art_placement(g)
    W, H = g.cover_w * PT, g.cover_h * PT
    o = []
    a = o.append

    a(f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
      f'width="{g.cover_w:.4f}in" height="{g.cover_h:.4f}in" '
      f'viewBox="0 0 {W:.3f} {H:.3f}">')
    a(f'<title>CODEX MYTHOLOGICA — KDP ciltsiz kapak şablonu '
      f'({paper}, {g.page_count} sayfa)</title>')
    a('<rect width="100%" height="100%" fill="#0B0B0C"/>')

    # panel dolguları
    a('<g id="panels" opacity="0.30">')
    for r, c in [(g.back, "#1E3A5F"), (g.spine, "#5F1E1E"), (g.front, "#1E5F35")]:
        a("  " + _rect(r, "none", fill=c))
    a('</g>')

    a('<g id="guides" fill="none">')
    a('  <!-- taşma kenarı = tuvalin dış sınırı -->')
    a("  " + _rect(S.Rect(0, 0, g.cover_w, g.cover_h), GUIDE["bleed"], 1.5,
                   label=f'BLEED {g.cover_w:.4f} x {g.cover_h:.4f} in'))
    a('  <!-- kesim çizgisi -->')
    a("  " + _rect(g.trim, GUIDE["trim"], 1.5, label="TRIM"))
    a('  <!-- katlama çizgileri -->')
    for x, lb in [(g.spine.x, "FOLD"), (g.spine.x2, "FOLD")]:
        a(f'  <line x1="{x*PT:.3f}" y1="0" x2="{x*PT:.3f}" y2="{H:.3f}" '
          f'stroke="{GUIDE["fold"]}" stroke-width="1.5"/>')
    a('  <!-- güvenli alan (canlı metin sınırı) -->')
    for r in (g.back_safe, g.front_safe, g.spine_safe):
        a("  " + _rect(r, GUIDE["safe"], 1.0, dash="6 4"))
    a(f'  <text x="{(g.back_safe.x+0.06)*PT:.3f}" y="{(g.back_safe.y+0.20)*PT:.3f}"'
      f' font-family="monospace" font-size="7" fill="{GUIDE["safe"]}">'
      f'SAFE {S.SAFE}in</text>')
    a('  <!-- barkod: KDP buraya beyaz kutu basar -->')
    a("  " + _rect(g.barcode, GUIDE["barcode"], 1.5,
                   fill="#FFD60A22", label="BARCODE 2.0 x 1.2 in"))
    a("  " + _rect(g.barcode_mirror, GUIDE["barcode"], 1.0, dash="3 3",
                   label="ihtiyat"))
    a('  <!-- görseldeki altın filetolar -->')
    for x in (p.rule_l_in, p.rule_r_in):
        a(f'  <line x1="{x*PT:.3f}" y1="0" x2="{x*PT:.3f}" y2="{H:.3f}" '
          f'stroke="#C9A227" stroke-width="0.6" stroke-dasharray="2 6"/>')
    a('</g>')

    # tipografi yer tutucuları
    fb = T.FontBook().build()
    a('<g id="type-placeholders">')
    for b in T.layout(fb, g):
        x1, y1, x2, y2 = T.bbox_of(b)
        a(f'  <rect x="{x1*PT:.3f}" y="{y1*PT:.3f}" width="{(x2-x1)*PT:.3f}" '
          f'height="{(y2-y1)*PT:.3f}" fill="none" stroke="{GUIDE["text"]}" '
          f'stroke-width="0.7" stroke-dasharray="4 3"/>')
        a(f'  <text x="{x1*PT:.3f}" y="{(y1-0.045)*PT:.3f}" '
          f'font-family="monospace" font-size="6" fill="{GUIDE["text"]}">'
          f'{_esc(b.id)} · {b.font} · {b.size_pt:.1f}pt · '
          f'trk {b.tracking_em:.3f}em</text>')
    a('</g>')

    a(f'<text x="{0.14*PT:.1f}" y="{H-10:.1f}" font-family="monospace" '
      f'font-size="8" fill="#8A8A8E">CODEX MYTHOLOGICA · {paper} · '
      f'{g.page_count}p · sırt {g.spine_w:.4f}in · '
      f'{g.canvas_px[0]}x{g.canvas_px[1]}px @{S.DPI}dpi · '
      f'üretildi: 08_BUILD/make_cover_svg.py</text>')
    a('</svg>')
    return "\n".join(o)


def master_svg(paper: str, ed=None) -> str:
    g = _geo(paper, ed)
    W, H = g.cover_w * PT, g.cover_h * PT
    fb = T.FontBook().build()
    plate = f"../plates/cover-plate-{paper}-{S.DPI}dpi.png"

    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" '
      f'xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" '
      f'width="{g.cover_w:.4f}in" height="{g.cover_h:.4f}in" '
      f'viewBox="0 0 {W:.3f} {H:.3f}">')
    a(f'<title>CODEX MYTHOLOGICA — ciltsiz kapak ANA KAYNAK ({paper})</title>')
    a('<desc>Düzenlenebilir ana kaynak. Metinler canlı vektördür. '
      'Görsel göreli yolla bağlıdır; SVG ile aynı klasör ağacında tutun.</desc>')
    a('<defs><style type="text/css"><![CDATA[')
    a('  @font-face{font-family:"CinzelC";'
      'src:url("../../07_ASSETS/fonts/static/cinzel-500.ttf") format("truetype");'
      'font-weight:500}')
    a('  @font-face{font-family:"CinzelC";'
      'src:url("../../07_ASSETS/fonts/static/cinzel-400.ttf") format("truetype");'
      'font-weight:400}')
    a('  @font-face{font-family:"GaramondC";'
      'src:url("../../07_ASSETS/fonts/static/garamond-400.ttf") format("truetype");'
      'font-style:normal}')
    a('  @font-face{font-family:"GaramondC";'
      'src:url("../../07_ASSETS/fonts/static/garamond-italic-400.ttf") '
      'format("truetype");font-style:italic}')
    a(']]></style></defs>')

    a(f'<image xlink:href="{plate}" href="{plate}" x="0" y="0" '
      f'width="{W:.3f}" height="{H:.3f}" preserveAspectRatio="none"/>')

    FAM = {"cinzel-500": ('CinzelC', 500, 'normal'),
           "cinzel-400": ('CinzelC', 400, 'normal'),
           "garamond-400": ('GaramondC', 400, 'normal'),
           "garamond-italic-400": ('GaramondC', 400, 'italic')}

    a('<g id="typography">')
    for b in T.layout(fb, g):
        fam, wt, st = FAM[b.font]
        anchor = {"left": "start", "center": "middle", "right": "end"}[b.align]
        common = (f'font-family="{fam}" font-weight="{wt}" font-style="{st}" '
                  f'font-size="{b.size_pt:.3f}" fill="{b.color}" '
                  f'letter-spacing="{b.tracking_em*b.size_pt:.4f}"')
        if b.rotation == -90:
            # yukarıdan aşağı okunan sırt metni
            a(f'  <text id="{_esc(b.id)}" {common} text-anchor="start" '
              f'transform="translate({b.x*PT:.3f},{b.y*PT:.3f}) rotate(90)" '
              f'dominant-baseline="central">{_esc(b.text)}</text>')
        elif b.lines:
            a(f'  <text id="{_esc(b.id)}" {common} text-anchor="start" '
              f'x="{b.x*PT:.3f}" y="{b.y*PT:.3f}">')
            for i, ln in enumerate(b.lines):
                dy = 0 if i == 0 else b.leading_pt
                a(f'    <tspan x="{b.x*PT:.3f}" dy="{dy:.3f}">{_esc(ln)}</tspan>')
            a('  </text>')
        else:
            a(f'  <text id="{_esc(b.id)}" {common} text-anchor="{anchor}" '
              f'x="{b.x*PT:.3f}" y="{b.y*PT:.3f}">{_esc(b.text)}</text>')
    a('</g>')
    a('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    import editions as E
    import paths as P
    ap = argparse.ArgumentParser()
    E.add_argument(ap)
    ap.add_argument("--paper", default=None, choices=list(S.PAPER_THICKNESS))
    ap.add_argument("--all-papers", action="store_true")
    args = ap.parse_args()

    ed = E.get(args.edition)
    out_dir = P.cover_dir(ed, "templates")
    for paper in (ed.papers if args.all_papers else [args.paper or ed.paper]):
        for name, fn in [(f"cover-template-{paper}-guides.svg", guides_svg),
                         (f"cover-master-{paper}.svg", master_svg)]:
            path = os.path.join(out_dir, name)
            with open(path, "w", encoding="utf-8") as f:
                f.write(fn(paper, ed))
            print(f"  → {P.rel(path)}  ({os.path.getsize(path)/1024:.1f} KB)")
