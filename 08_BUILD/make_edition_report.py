"""
SÜRÜM ÜRETİM RAPORU (HTML) — doğrulama JSON'larından üretilir.
================================================================================
Her sürüm için tek dosyalık, dış bağlantısız bir HTML rapor yazar:

    06_REPORTS/<SÜRÜM>/<SÜRÜM>_PRODUCTION_REPORT.html

İçerik: KDP yükleme ayarları · geometri şeması (ölçekli SVG, sayılar spec'ten)
· iç blok ve kapak doğrulama tabloları · birim ekonomi · bilinen sınırlar.

Kullanım:
    python3 08_BUILD/make_edition_report.py --edition hardcover
    python3 08_BUILD/make_edition_report.py --all-editions
"""

from __future__ import annotations

import argparse
import html
import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editions as ED   # noqa: E402
import cover_spec as S  # noqa: E402
import paths as P       # noqa: E402

ROOT = P.ROOT
H = lambda s: html.escape(str(s))   # noqa: E731

CSS = """
:root{--bg:#14130f;--s1:#1b1a15;--s2:#232219;--ink:#f4f1e8;--ink2:#c3bda9;
--ink3:#8d8778;--rule:#2e2c23;--gold:#d8ae3f;--ok:#5fce5f;--warn:#fab219;--bad:#ef7f7f;
--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
--serif:"Iowan Old Style",Palatino,Georgia,serif;--mono:ui-monospace,Menlo,Consolas,monospace}
@media(prefers-color-scheme:light){:root{--bg:#faf7f0;--s1:#fffdf7;--s2:#f1ece0;
--ink:#17150f;--ink2:#4b463a;--ink3:#7d7767;--rule:#ddd6c4;--gold:#8a6a15;
--ok:#186418;--warn:#8a5c00;--bad:#a52a2a}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font-family:var(--serif);font-size:16px;line-height:1.7;padding:0 20px 80px}
.wrap{max-width:1080px;margin:0 auto}
header{padding:44px 0 26px;border-bottom:1px solid var(--rule)}
.kick{font-family:var(--sans);font-size:11px;letter-spacing:.2em;
text-transform:uppercase;color:var(--gold)}
h1{font-size:clamp(26px,4vw,40px);margin:14px 0 8px;font-weight:500}
h2{font-size:23px;margin:44px 0 12px;font-weight:500;padding-top:22px;
border-top:1px solid var(--rule)}
h3{font-size:17px;margin:26px 0 8px;font-family:var(--sans);font-weight:600}
p{max-width:74ch;margin:0 0 14px}
code{font-family:var(--mono);font-size:.87em;background:var(--s2);padding:1px 5px;
border-radius:2px}
.grid{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));
margin:20px 0}
.tile{background:var(--s1);border:1px solid var(--rule);border-left:2px solid var(--gold);
border-radius:3px;padding:14px}
.tile .l{font-family:var(--sans);font-size:10.5px;letter-spacing:.09em;
text-transform:uppercase;color:var(--ink3);margin-bottom:6px}
.tile .v{font-family:var(--sans);font-size:25px;font-weight:600;line-height:1.1}
.tile .n{font-family:var(--sans);font-size:11px;color:var(--ink3);margin-top:5px}
.tw{overflow-x:auto;border:1px solid var(--rule);border-radius:3px;margin:18px 0;
background:var(--s1)}
table{border-collapse:collapse;width:100%;font-family:var(--sans);font-size:13px;
min-width:520px}
th,td{padding:8px 11px;text-align:left;border-bottom:1px solid var(--rule);
vertical-align:top}
th{font-size:10px;letter-spacing:.09em;text-transform:uppercase;color:var(--ink3);
background:var(--s2);white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.ok{color:var(--ok);font-weight:700}.wn{color:var(--warn);font-weight:700}
.bd{color:var(--bad);font-weight:700}
.card{background:var(--s1);border:1px solid var(--rule);border-radius:3px;
padding:16px 18px;margin:18px 0}
.card.w{border-left:3px solid var(--warn)}.card.b{border-left:3px solid var(--bad)}
.card.g{border-left:3px solid var(--ok)}
.cap{font-family:var(--sans);font-size:10.5px;letter-spacing:.13em;
text-transform:uppercase;color:var(--gold);margin-bottom:8px}
ul{max-width:74ch}li{margin-bottom:6px}
footer{margin-top:60px;padding-top:22px;border-top:1px solid var(--rule);
font-family:var(--sans);font-size:12px;color:var(--ink3)}
svg{display:block;max-width:100%;height:auto}
@media print{body{background:#fff;color:#000}.tw,.card,.tile{border-color:#ccc}}
"""


def schematic(g, w_px: int = 1000) -> str:
    """Kapak geometrisinin ölçekli şeması — bütün sayılar spec'ten gelir."""
    k = w_px / g.cover_w
    Hh = g.cover_h * k
    o = [f'<svg viewBox="0 0 {w_px:.1f} {Hh+52:.1f}" role="img" '
         f'aria-label="{H(g.binding)} kapak geometri şeması">']
    o.append(f'<rect x="0" y="0" width="{w_px:.1f}" height="{Hh:.1f}" '
             f'fill="#232219" stroke="#d8ae3f" stroke-width="1.5"/>')

    def rect(r, fill, stroke, label=None, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s = (f'<rect x="{r.x*k:.1f}" y="{r.y*k:.1f}" width="{r.w*k:.1f}" '
             f'height="{r.h*k:.1f}" fill="{fill}" stroke="{stroke}" '
             f'stroke-width="1.2"{d}/>')
        if label:
            s += (f'<text x="{r.cx*k:.1f}" y="{(r.y+0.32)*k:.1f}" '
                  f'text-anchor="middle" font-family="monospace" font-size="11" '
                  f'fill="{stroke}">{H(label)}</text>')
        return s

    o.append(rect(g.back, "rgba(216,174,63,.05)", "#8d8778", "arka"))
    if g.hinge_back.w > 0:
        o.append(rect(g.hinge_back, "rgba(175,82,222,.18)", "#af52de"))
        o.append(rect(g.hinge_front, "rgba(175,82,222,.18)", "#af52de"))
    o.append(rect(g.spine, "rgba(216,174,63,.16)", "#d8ae3f", "sırt"))
    o.append(rect(g.front, "rgba(216,174,63,.05)", "#8d8778", "ön"))
    for r in (g.back_safe, g.front_safe, g.spine_safe):
        o.append(rect(r, "none", "#34c759", None, "5,4"))
    o.append(rect(g.barcode, "rgba(255,214,10,.20)", "#ffd60a", "barkod"))
    # kesim çizgisi
    o.append(f'<rect x="{g.trim.x*k:.1f}" y="{g.trim.y*k:.1f}" '
             f'width="{g.trim.w*k:.1f}" height="{g.trim.h*k:.1f}" fill="none" '
             f'stroke="#ff3b30" stroke-width="1.4"/>')
    lab = (f'tuval {g.cover_w:.4f} × {g.cover_h:.4f} in  ·  '
           f'sırt {g.spine_w:.4f} in ({g.spine_w*25.4:.2f} mm)  ·  '
           f'{g.canvas_px[0]}×{g.canvas_px[1]} px @ 300 DPI')
    o.append(f'<text x="0" y="{Hh+20:.1f}" font-family="monospace" '
             f'font-size="12" fill="#8d8778">{H(lab)}</text>')
    leg = ('kırmızı = kesim · yeşil kesikli = güvenli alan · '
           'sarı = barkod' + (' · mor = menteşe oluğu' if g.hinge_back.w > 0 else ''))
    o.append(f'<text x="0" y="{Hh+40:.1f}" font-family="monospace" '
             f'font-size="11" fill="#8d8778">{H(leg)}</text>')
    o.append("</svg>")
    return "".join(o)


def checks_table(rows) -> str:
    ic = {"pass": '<span class="ok">✓</span>', "warn": '<span class="wn">!</span>',
          "fail": '<span class="bd">✗</span>'}
    o = ['<div class="tw"><table><thead><tr><th></th><th>Grup</th><th>Kontrol</th>'
         '<th>Beklenen</th><th>Gelen</th><th>Not</th></tr></thead><tbody>']
    for r in rows:
        o.append(f'<tr><td>{ic[r["status"]]}</td><td>{H(r["group"])}</td>'
                 f'<td>{H(r["name"])}</td><td>{H(r["expected"])}</td>'
                 f'<td>{H(r["actual"])}</td><td>{H(r["note"])}</td></tr>')
    o.append("</tbody></table></div>")
    return "".join(o)


def load(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def royalty(ed, pages, paper="cream"):
    """KDP resmî ABD baskı maliyeti + telif."""
    large = ed.trim_w > 6.12 or ed.trim_h > 9.0
    if ed.binding == "hardcover":
        cost = 6.80 if pages <= 108 else 5.65 + pages * 0.012
    else:
        if pages <= 110:
            cost = 2.84 if large else 2.30
        else:
            cost = 1.00 + pages * (0.017 if large else 0.012)
    rate = 0.60 if ed.price_usd >= 9.99 else 0.50
    return round(cost, 2), round(rate * ed.price_usd - cost, 2), rate


def build(edition: str) -> str:
    ed = ED.get(edition)
    inter = load(P.validation_json(ed, "interior"))
    covers = {p: load(P.validation_json(ed, "cover", p)) for p in ed.papers}
    covers = {k: v for k, v in covers.items() if v}

    pages = inter["pages"] if inter else S.interior_pages(ed)
    g = S.geometry_for(ed, paper=ed.paper, pages=pages)
    cost, roy, rate = royalty(ed, pages, ed.paper)

    def summ(d):
        return d["summary"] if d else {"total": 0, "pass": 0, "warn": 0, "fail": 0}
    si, sc = summ(inter), summ(next(iter(covers.values()), None))
    tot_fail = si["fail"] + sum(summ(c)["fail"] for c in covers.values())
    tot_warn = si["warn"] + sum(summ(c)["warn"] for c in covers.values())
    tot_all = si["total"] + sum(summ(c)["total"] for c in covers.values())

    o = ['<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{H(ed.label)} — Üretim Raporu · Codex Mythologica</title>',
         f'<style>{CSS}</style></head><body><div class="wrap">']

    o.append(f'<header><div class="kick">Codex Mythologica · Üretim Raporu · '
             f'{datetime.now():%d.%m.%Y}</div>'
             f'<h1>{H(ed.label)} sürümü</h1>'
             f'<p>{H(ed.profile.label)} · {ed.trim_w:g}×{ed.trim_h:g} inç · '
             f'{pages} sayfa · gövde {ed.body_pt:g}/{ed.lead_pt:g} pt</p></header>')

    # ── özet ──
    o.append('<div class="grid">')
    for lab, val, note in [
        ("Sayfa", pages, f"KDP sınırı {ed.profile.min_pages}–{ed.profile.max_pages}"),
        ("Sırt", f"{g.spine_w:.4f}\"", f"{g.spine_w*25.4:.2f} mm · {ed.paper} kâğıt"),
        ("Tam kapak", f"{g.cover_w:.3f}×{g.cover_h:.3f}", "inç, sarım/taşma dahil"),
        ("Doğrulama", f"{tot_all-tot_fail-tot_warn}/{tot_all}",
         f"{tot_warn} uyarı · {tot_fail} başarısız"),
        ("Baskı maliyeti", f"{cost:.2f} $", "KDP resmî ABD tablosu"),
        ("Birim telif", f"{roy:.2f} $", f"{ed.price_usd:.2f} $ liste · %{rate*100:.0f}"),
    ]:
        o.append(f'<div class="tile"><div class="l">{H(lab)}</div>'
                 f'<div class="v">{H(val)}</div><div class="n">{H(note)}</div></div>')
    o.append('</div>')

    if not g.calibrated:
        o.append('<div class="card b"><div class="cap">⚠ Kalibrasyon gerekiyor</div>'
                 '<p>Bu ciltlemenin geometrisi KDP\'nin resmî şablonundan '
                 '<strong>ölçülmedi</strong>; varsayılan değerler kullanıldı. '
                 'Kapak <code>_PROVISIONAL</code> adıyla üretildi ve '
                 '<strong>KDP\'ye yüklenmemelidir</strong>.</p>'
                 '<p style="margin:0">Düzeltme: '
                 '<code>python3 08_BUILD/calibrate_cover.py --template &lt;şablon&gt; '
                 '--spine &lt;inç&gt;</code> → sonra '
                 f'<code>./08_BUILD/build_{ed.key}.sh</code></p></div>')

    # ── KDP ayarları ──
    o.append('<h2>KDP yükleme ayarları</h2>')
    o.append('<div class="tw"><table><thead><tr><th>Alan</th><th>Değer</th>'
             '<th>Not</th></tr></thead><tbody>')
    rows = [
        ("Format", ed.profile.label, "KDP Bookshelf → + Create"),
        ("Trim size", f"{ed.trim_w:g} × {ed.trim_h:g} inç", "iç blok bu ölçüde"),
        ("Bleed", "No bleed", "metin taşmıyor"),
        ("Paper", ed.paper.capitalize(),
         "kapak dosyası kâğıda bağlıdır — yanlış eşleşme sırtı kaydırır"),
        ("Ink", "Black &amp; white", "iç blok tamamen siyah"),
        ("Cover finish", "Matte", "koyu kapakta parmak izi göstermez"),
        ("ISBN", "Get a free KDP ISBN", "her format kendi ISBN'ini alır"),
        ("Liste fiyatı", f"{ed.price_usd:.2f} $",
         f"telif hesaplayıcı {roy:.2f} $ göstermeli"),
        ("AI beyanı", "Metin: AI destekli · Kapak: AI üretimi",
         "beyan edilmemesi hesap kapatma sebebidir"),
        ("Seri", "Codex · Cilt 1", "üç formatta birebir aynı yazılmalı"),
    ]
    if ed.title_suffix:
        rows.insert(1, ("Başlık eki", ed.title_suffix.strip(),
                        "ayrı ASIN — arama niyeti farklı"))
    for a, b, c in rows:
        o.append(f'<tr><td>{a}</td><td><strong>{b}</strong></td><td>{H(c)}</td></tr>')
    o.append('</tbody></table></div>')

    # ── dosyalar ──
    o.append('<h2>Yüklenecek dosyalar</h2><div class="tw"><table><thead><tr>'
             '<th>Ne</th><th>Dosya</th><th class="n">Boyut</th></tr></thead><tbody>')
    files = [("İç blok", P.interior_pdf(ed))]
    for p in ed.papers:
        files.append((f"Kapak ({p})", P.cover_pdf(ed, p, provisional=not g.calibrated)))
    for lab, f in files:
        if os.path.exists(f):
            o.append(f'<tr><td>{H(lab)}</td><td><code>{H(P.rel(f))}</code></td>'
                     f'<td class="n">{os.path.getsize(f)/1e6:.2f} MB</td></tr>')
    o.append('</tbody></table></div>')

    # ── geometri ──
    o.append('<h2>Kapak geometrisi</h2>')
    o.append(f'<p>Şemadaki her sayı <code>08_BUILD/cover_spec.py</code>\'den '
             f'türetilmiştir; elle konumlandırma yoktur.</p>')
    o.append(schematic(g))

    # ── doğrulama ──
    o.append('<h2>İç blok doğrulaması</h2>')
    if inter:
        o.append(f'<p>{si["total"]} kontrol · <span class="ok">{si["pass"]} geçti</span> · '
                 f'<span class="wn">{si["warn"]} uyarı</span> · '
                 f'<span class="bd">{si["fail"]} başarısız</span></p>')
        o.append(checks_table(inter["checks"]))
    else:
        o.append('<div class="card w"><p style="margin:0">Doğrulama çalıştırılmamış: '
                 f'<code>python3 08_BUILD/validate_interior.py --edition {ed.key}</code>'
                 '</p></div>')

    for paper, cv in covers.items():
        s = cv["summary"]
        o.append(f'<h2>Kapak doğrulaması — {H(paper)} kâğıt</h2>')
        o.append(f'<p>{s["total"]} kontrol · <span class="ok">{s["pass"]} geçti</span> · '
                 f'<span class="wn">{s["warn"]} uyarı</span> · '
                 f'<span class="bd">{s["fail"]} başarısız</span></p>')
        o.append(checks_table(cv["checks"]))

    # ── yeniden üretim ──
    o.append('<h2>Yeniden üretim</h2>')
    o.append(f'<div class="card g"><div class="cap">Tek komut</div>'
             f'<p style="margin:0"><code>./08_BUILD/build_{ed.key}.sh --all-papers</code>'
             f'</p></div>')
    o.append('<p>Bu rapordaki bütün dosyalar yukarıdaki komutla birebir yeniden '
             'üretilir. Elle konumlandırılmış tek bir koordinat yoktur; sayfa '
             'sayısı, kâğıt veya kesim ölçüsü değişirse geometri ve tipografi '
             'kendiliğinden yeniden çözülür.</p>')

    o.append(f'<footer>Codex Mythologica · {H(ed.label)} üretim raporu · '
             f'{datetime.now():%d.%m.%Y %H:%M} · '
             f'<code>08_BUILD/make_edition_report.py</code><br>'
             f'Baskı maliyeti ve telif KDP resmî ABD tablolarından hesaplanmıştır; '
             f'satış tahmini içermez.</footer>')
    o.append('</div></body></html>')

    out = P.edition_report_html(ed)
    with open(out, "w", encoding="utf-8") as f:
        f.write("".join(o))
    print(f"  → {P.rel(out)}  ({os.path.getsize(out)/1024:.1f} KB)")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ED.add_argument(ap)
    ap.add_argument("--all-editions", action="store_true")
    a = ap.parse_args()
    for k in (ED.ORDER if a.all_editions else [a.edition]):
        build(k)
