"""
Doğrulama raporu (HTML) — denetim + doğrulama JSON'larından üretilir.
================================================================================
Çıktı: 06_REPORTS/COVER_VALIDATION_REPORT.html  (tek dosya, dış bağlantı yok)
Kullanım: python3 08_BUILD/make_validation_report.py
"""

from __future__ import annotations
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cover_spec as S  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PT = 72.0
E = lambda s: html.escape(str(s))  # noqa: E731


def schematic(paper: str, w_px: int = 980) -> str:
    """Kapak geometrisinin ölçekli şeması — sayılar spec'ten gelir."""
    g = S.geometry(paper=paper)
    p = S.art_placement(g)
    k = w_px / g.cover_w
    H = g.cover_h * k
    o = [f'<svg viewBox="0 0 {w_px:.1f} {H+46:.1f}" width="100%" '
         f'role="img" aria-label="Kapak geometri şeması">']
    o.append(f'<rect x="0" y="0" width="{w_px:.1f}" height="{H:.1f}" '
             f'fill="#12100E" stroke="#E4572E" stroke-width="1.5"/>')
    for r, fill, lab in [(g.back, "#1B2B3A", "ARKA"), (g.spine, "#3A1B1B", "SIRT"),
                         (g.front, "#16301F", "ÖN")]:
        o.append(f'<rect x="{r.x*k:.1f}" y="{r.y*k:.1f}" width="{r.w*k:.1f}" '
                 f'height="{r.h*k:.1f}" fill="{fill}" stroke="#E4572E" '
                 f'stroke-width="1.2"/>')
        o.append(f'<text x="{r.cx*k:.1f}" y="{(r.y+0.62)*k:.1f}" '
                 f'text-anchor="middle" font-size="12" font-weight="600" '
                 f'fill="#C9A227" letter-spacing="1.5">{lab}</text>')
    for r in (g.back_safe, g.front_safe):
        o.append(f'<rect x="{r.x*k:.1f}" y="{r.y*k:.1f}" width="{r.w*k:.1f}" '
                 f'height="{r.h*k:.1f}" fill="none" stroke="#3DBE7B" '
                 f'stroke-width="1" stroke-dasharray="5 4"/>')
    b = g.barcode
    o.append(f'<rect x="{b.x*k:.1f}" y="{b.y*k:.1f}" width="{b.w*k:.1f}" '
             f'height="{b.h*k:.1f}" fill="#E8B62733" stroke="#E8B627" '
             f'stroke-width="1.2"/>')
    o.append(f'<text x="{b.cx*k:.1f}" y="{b.cy*k+4:.1f}" text-anchor="middle" '
             f'font-size="10" fill="#E8B627">BARKOD 2×1.2"</text>')
    for x in (p.rule_l_in, p.rule_r_in):
        o.append(f'<line x1="{x*k:.1f}" y1="0" x2="{x*k:.1f}" y2="{H:.1f}" '
                 f'stroke="#C9A227" stroke-width="0.9" stroke-dasharray="2 5"/>')
    # ölçü çizgileri
    y = H + 16
    for x1, x2, lab in [(0, g.cover_w, f'{g.cover_w:.4f} inç'),
                        (g.spine.x, g.spine.x2, f'sırt {g.spine_w:.4f}')]:
        o.append(f'<line x1="{x1*k:.1f}" y1="{y:.1f}" x2="{x2*k:.1f}" '
                 f'y2="{y:.1f}" stroke="#8B8680" stroke-width="1"/>')
        o.append(f'<text x="{(x1+x2)/2*k:.1f}" y="{y+14:.1f}" '
                 f'text-anchor="middle" font-size="11" fill="#B9B2A8">{lab}</text>')
        y += 0
    o.append('</svg>')
    return "\n".join(o)


def checks_table(rows) -> str:
    ic = {"pass": ("✓", "ok"), "warn": ("!", "wa"), "fail": ("✗", "fa")}
    out = ['<table class="chk"><thead><tr><th></th><th>Kontrol</th>'
           '<th>Beklenen</th><th>Ölçülen</th><th>Not</th></tr></thead><tbody>']
    grp = None
    for r in rows:
        if r["group"] != grp:
            grp = r["group"]
            out.append(f'<tr class="grp"><td colspan="5">{E(grp)}</td></tr>')
        sym, cls = ic[r["status"]]
        out.append(f'<tr class="{cls}"><td class="s">{sym}</td>'
                   f'<td>{E(r["name"])}</td><td class="m">{E(r["expected"])}</td>'
                   f'<td class="m">{E(r["actual"])}</td>'
                   f'<td class="n">{E(r["note"])}</td></tr>')
    out.append("</tbody></table>")
    return "\n".join(out)


def main():
    audit = json.load(open(os.path.join(ROOT, "06_REPORTS", "cover-audit.json"),
                           encoding="utf-8"))
    vals = {}
    for paper in ("cream", "white"):
        f = os.path.join(ROOT, "06_REPORTS", f"cover-validation-{paper}.json")
        if os.path.exists(f):
            vals[paper] = json.load(open(f, encoding="utf-8"))

    g = S.geometry()
    p = S.art_placement(g)
    sev = {"blocker": "Engelleyici", "high": "Yüksek", "medium": "Orta"}

    find_html = []
    for f in audit["findings"]:
        find_html.append(
            f'<div class="find {f["severity"]}">'
            f'<div class="fh"><span class="fid">{E(f["id"])}</span>'
            f'<span class="fsev">{E(sev.get(f["severity"], f["severity"]))}</span>'
            f'<span class="ft">{E(f["title"])}</span></div>'
            f'<p>{E(f["detail"])}</p></div>')

    tabs, panes = [], []
    for i, (paper, v) in enumerate(vals.items()):
        s = v["summary"]
        act = " active" if i == 0 else ""
        tabs.append(f'<button class="tab{act}" data-t="{paper}">'
                    f'{"Krem" if paper=="cream" else "Beyaz"} kâğıt '
                    f'<span class="pill">{s["pass"]}/{s["total"]}</span></button>')
        gg = S.geometry(paper=paper)
        panes.append(
            f'<section class="pane{act}" id="p-{paper}">'
            f'<p class="lede">Sırt <b>{gg.spine_w:.4f} inç</b> · tuval '
            f'<b>{gg.cover_w:.4f} × {gg.cover_h:.4f} inç</b> · '
            f'<b>{gg.canvas_px[0]}×{gg.canvas_px[1]} px</b> @ {S.DPI} DPI · '
            f'yüklenecek dosya <code>{E(os.path.basename(v["pdf"]))}</code></p>'
            f'{schematic(paper)}{checks_table(v["checks"])}</section>')

    total = sum(v["summary"]["total"] for v in vals.values())
    passed = sum(v["summary"]["pass"] for v in vals.values())
    failed = sum(v["summary"]["fail"] for v in vals.values())

    doc = f"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Codex Mythologica — Ciltsiz Kapak Doğrulama Raporu</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#0C0B0A;color:#E6E1D8;
 font:15px/1.65 ui-serif,Georgia,'Times New Roman',serif}}
.wrap{{max-width:1120px;margin:0 auto;padding:40px 22px 90px}}
h1{{font-size:clamp(26px,4vw,40px);line-height:1.15;margin:0 0 6px;
 letter-spacing:.01em;color:#EFE9DD}}
.sub{{color:#9C948A;margin:0 0 34px;font-size:15px}}
h2{{font-size:22px;margin:52px 0 14px;color:#C9A227;
 border-bottom:1px solid #2A2724;padding-bottom:8px;font-weight:600}}
h3{{font-size:16px;margin:26px 0 10px;color:#E6E1D8}}
p{{margin:0 0 14px}}
code{{font:13px/1.5 ui-monospace,'SF Mono',Menlo,monospace;
 background:#1A1815;padding:2px 6px;border-radius:4px;color:#D9C98A}}
.hero{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));
 gap:12px;margin:26px 0 8px}}
.stat{{background:#141210;border:1px solid #2A2724;border-radius:10px;padding:14px 16px}}
.stat .v{{font-size:26px;font-weight:600;color:#C9A227;line-height:1.1}}
.stat .k{{font-size:12px;color:#9C948A;margin-top:4px;letter-spacing:.03em}}
.find{{background:#141210;border-left:3px solid #6B6560;border-radius:0 8px 8px 0;
 padding:14px 18px;margin:0 0 12px}}
.find.blocker{{border-left-color:#E4572E}}
.find.high{{border-left-color:#E8B627}}
.find.medium{{border-left-color:#5B8DEF}}
.fh{{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin-bottom:6px}}
.fid{{font:12px ui-monospace,monospace;color:#8B8680}}
.fsev{{font-size:11px;letter-spacing:.08em;text-transform:uppercase;
 padding:2px 8px;border-radius:99px;background:#241F1B;color:#D9C98A}}
.find.blocker .fsev{{background:#3A1A12;color:#F3A88C}}
.ft{{font-weight:600;color:#EFE9DD}}
.find p{{margin:0;color:#B9B2A8;font-size:14.5px}}
.tabs{{display:flex;gap:8px;margin:22px 0 16px;flex-wrap:wrap}}
.tab{{background:#141210;border:1px solid #2A2724;color:#9C948A;
 padding:9px 16px;border-radius:8px;cursor:pointer;font:15px inherit}}
.tab.active{{background:#1F1B16;border-color:#C9A227;color:#EFE9DD}}
.pill{{font:12px ui-monospace,monospace;background:#2A2724;padding:1px 7px;
 border-radius:99px;margin-left:6px;color:#8FD4A8}}
.pane{{display:none}}.pane.active{{display:block}}
.lede{{color:#9C948A;font-size:14px}}
svg{{display:block;margin:18px 0 26px;max-width:100%;height:auto}}
.tblwrap{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:13.5px}}
.chk td,.chk th{{padding:7px 10px;text-align:left;
 border-bottom:1px solid #201D1A;vertical-align:top}}
.chk th{{color:#9C948A;font-weight:600;font-size:12px;letter-spacing:.05em;
 text-transform:uppercase}}
.chk .grp td{{background:#17140F;color:#C9A227;font-weight:600;font-size:12px;
 letter-spacing:.08em;text-transform:uppercase;padding-top:12px}}
.chk .s{{width:26px;font-weight:700;text-align:center}}
.chk .ok .s{{color:#5FBF87}} .chk .wa .s{{color:#E8B627}} .chk .fa .s{{color:#E4572E}}
.chk .fa{{background:#1E1310}}
.chk .m{{font:12.5px ui-monospace,monospace;color:#D9C98A;white-space:nowrap}}
.chk .n{{color:#8B8680;font-size:12.5px}}
table.geo td,table.geo th{{padding:7px 12px;border-bottom:1px solid #201D1A;
 text-align:left}}
table.geo th{{color:#9C948A;font-size:12px;text-transform:uppercase;
 letter-spacing:.05em}}
table.geo td:nth-child(n+2){{font:12.5px ui-monospace,monospace;color:#D9C98A}}
.note{{background:#141210;border:1px solid #2A2724;border-radius:10px;
 padding:16px 18px;margin:18px 0}}
.note b{{color:#C9A227}}
.warn{{border-color:#5A4415;background:#191510}}
ul{{margin:0 0 14px;padding-left:20px}} li{{margin:5px 0;color:#B9B2A8}}
footer{{margin-top:60px;padding-top:20px;border-top:1px solid #2A2724;
 color:#6B6560;font-size:12.5px}}
@media (prefers-color-scheme:light){{
  body{{background:#FBF9F5;color:#221F1B}}
  .stat,.find,.note{{background:#FFF;border-color:#E3DED4}}
  h1,.ft{{color:#171512}} .sub,.lede,.chk .n,li{{color:#6B655C}}
  .chk .grp td{{background:#F3EFE6}} .chk .fa{{background:#FDF0EC}}
  code{{background:#F3EFE6;color:#7A5E10}}
  .tab{{background:#FFF;border-color:#E3DED4;color:#6B655C}}
  .tab.active{{background:#FFF8E6;border-color:#C9A227;color:#171512}}
}}
</style></head><body><div class="wrap">

<h1>Ciltsiz kapak — doğrulama raporu</h1>
<p class="sub">CODEX MYTHOLOGICA · {g.page_count} sayfa · {S.TRIM_W:g}×{S.TRIM_H:g} inç ·
Amazon KDP tam sarım kapak</p>

<div class="hero">
  <div class="stat"><div class="v">{passed}/{total}</div>
    <div class="k">DOĞRULAMA KONTROLÜ</div></div>
  <div class="stat"><div class="v">{failed}</div>
    <div class="k">BAŞARISIZ</div></div>
  <div class="stat"><div class="v">{g.spine_w:.4f}"</div>
    <div class="k">SIRT (KREM KÂĞIT)</div></div>
  <div class="stat"><div class="v">{S.DPI}</div>
    <div class="k">DPI</div></div>
</div>

<h2>Sorun neydi</h2>
<p>Eski kapak dosyası KDP Önizleyici'de kaydığı için yayın durmuştu. Tek bir
sebep yoktu; birbirinden bağımsız <b>dört</b> hata üst üste binmişti. Aşağıdaki
teşhis tahmin değil, ölçümdür — hepsi
<code>08_BUILD/audit_cover.py</code> ile yeniden üretilebilir.</p>
{''.join(find_html)}

<h2>Nasıl çözüldü</h2>
<p>{E(audit['fix']['rule'])}</p>
<div class="note">
<p><b>Kritik olan kural şu:</b> görseldeki altın filetolar katlama çizgisi
olarak <i>kullanılamaz</i> — çünkü onlar {audit['artwork']['band_width_frac']*100:.2f}%
genişliğinde, gerçek sırt ise {g.spine_w/g.cover_w*100:.2f}%. Bunun yerine
bandın <b>merkezi</b> sırtın <b>merkezine</b> oturtuldu. Filetolar böylece
sırtın içinde, her iki kattan
<b>{p.rule_inset_in*25.4:.1f} mm</b> içeride kalıyor. Bu, katlama toleransından
etkilenmedikleri ve kasıtlı bir sırt bezemesi gibi okundukları anlamına gelir.</p>
</div>

<h3>Eski dosya / yeni dosya</h3>
<div class="tblwrap"><table class="geo">
<tr><th></th><th>Eski (aşılmış)</th><th>Yeni</th></tr>
<tr><td>Sayfa kutusu</td>
    <td>{audit['old_cover']['page_w_in']} × {audit['old_cover']['page_h_in']} inç</td>
    <td>{g.cover_w:.4f} × {g.cover_h:.4f} inç</td></tr>
<tr><td>KDP'nin uygulayacağı ölçek</td>
    <td>X {audit['findings'][0]['measured']['scale_x']} · Y {audit['findings'][0]['measured']['scale_y']}</td>
    <td>1.0000 · 1.0000</td></tr>
<tr><td>Çözünürlük</td><td>112 PPI</td><td>{S.DPI} PPI</td></tr>
<tr><td>Metin</td><td>piksele gömülü (0 font)</td><td>canlı vektör (3 gömülü font)</td></tr>
<tr><td>Sırt merkezi</td>
    <td>%{audit['artwork']['band_center_frac']*100:.2f} (yanlış)</td>
    <td>%50.00 (tanım gereği)</td></tr>
<tr><td>Sırt genişliği</td><td>tanımsız</td>
    <td>{g.spine_w:.4f} inç = {g.page_count} × {S.PAPER_THICKNESS[g.paper]}</td></tr>
</table></div>

<h2>Doğrulama sonuçları</h2>
<p>Kontroller iki türlüdür. <b>Yapısal</b> olanlar PDF'in kendi nesnelerinden
okunur. <b>Deneysel</b> olanlar PDF'i gerçekten render edip pikselleri ölçer —
eski dosyadaki hatayı ancak bu tür yakalardı, çünkü orada sayılar değil çıktı
yanlıştı.</p>
<div class="tabs">{''.join(tabs)}</div>
{''.join(panes)}

<h2>Yükleme kuralı</h2>
<div class="note warn">
<p><b>Kâğıt seçimi kapak dosyasını belirler.</b> KDP yükleme ekranında
<i>Paper</i> alanında ne seçerseniz, sırt genişliği ona göre hesaplanır:</p>
<ul>
<li><b>Cream</b> seçerseniz →
<code>CODEX_MYTHOLOGICA_COVER_cream_KDP.pdf</code> (sırt {S.geometry('cream').spine_w:.4f} inç)</li>
<li><b>White</b> seçerseniz →
<code>CODEX_MYTHOLOGICA_COVER_white_KDP.pdf</code> (sırt {S.geometry('white').spine_w:.4f} inç)</li>
</ul>
<p>Aradaki fark {abs(S.geometry('cream').spine_w-S.geometry('white').spine_w)*25.4:.1f} mm'dir
ve yanlış eşleşme sırt yazısını doğrudan katlama çizgisine kaydırır.
Bu kitap için <b>krem</b> önerilir: uzun metinde göz daha az yorulur,
maliyet aynıdır.</p>
</div>

<h2>Kalan risk</h2>
<div class="note warn">
<p><b>Ham görselin yerel çözünürlüğü {p.native_ppi} PPI.</b>
{S.DPI} PPI'ya yükseltmek KDP'nin piksel şartını karşılar ve dosya uyarı
almadan geçer; ancak yükseltme <i>detay üretmez</i>. Baskıda mandala
kabartmasının en ince çizgileri bir miktar yumuşak çıkacaktır. Koyu ve
atmosferik bir görsel olduğu için bu kabul edilebilir sınırdadır.</p>
<p>Kesin çözüm: aynı görseli bir yükseltme aracıyla ≥{g.canvas_px[0]} piksel
genişliğe çıkarın, <code>03_COVER/artwork/</code> içine koyun,
<code>cover_spec.py</code> içindeki <code>ART_W/ART_H</code> ve
<code>ART_SPINE_CENTER_FRAC</code> değerlerini
<code>audit_cover.py</code> çıktısıyla güncelleyin, sonra
<code>./08_BUILD/build_cover.sh --all-papers</code> komutunu tekrar çalıştırın.
Tipografi ve geometri kendiliğinden yeniden çözülür.</p>
</div>

<footer>Üretildi: <code>08_BUILD/make_validation_report.py</code> ·
Tüm sayılar <code>08_BUILD/cover_spec.py</code> ve
<code>08_BUILD/typography.py</code> kaynaklıdır ·
Dış bağlantı yoktur, dosya tek başına açılır.</footer>
</div>
<script>
document.querySelectorAll('.tab').forEach(function(b){{
  b.addEventListener('click',function(){{
    document.querySelectorAll('.tab').forEach(function(x){{x.classList.remove('active')}});
    document.querySelectorAll('.pane').forEach(function(x){{x.classList.remove('active')}});
    b.classList.add('active');
    document.getElementById('p-'+b.dataset.t).classList.add('active');
  }});
}});
</script></body></html>"""

    out = os.path.join(ROOT, "06_REPORTS", "COVER_VALIDATION_REPORT.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"  → 06_REPORTS/COVER_VALIDATION_REPORT.html "
          f"({os.path.getsize(out)/1024:.1f} KB)")


if __name__ == "__main__":
    main()
