"""
A+ üretim ve doğrulama raporu (HTML) — tek dosya, dış bağlantı yok.
Çıktı: 06_REPORTS/APLUS_PRODUCTION_REPORT.html
"""

from __future__ import annotations
import base64
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aplus_spec as A          # noqa: E402
import aplus_copy as CP         # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "03_APLUS")
E = lambda s: html.escape(str(s))   # noqa: E731


def data_uri(path: str) -> str:
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()


def main():
    man = json.load(open(os.path.join(OUT, "spec", "aplus-manifest.json"),
                         encoding="utf-8"))
    val = json.load(open(os.path.join(ROOT, "06_REPORTS",
                                      "aplus-validation.json"),
                         encoding="utf-8"))
    plate = json.load(open(os.path.join(ROOT, "06_REPORTS",
                                        "aplus-plate-analysis.json"),
                           encoding="utf-8"))
    typo = json.load(open(os.path.join(OUT, "spec", "aplus-typography.json"),
                          encoding="utf-8"))
    plate_by = {m["key"]: m for m in plate["modules"]}
    typo_by = {m["key"]: m for m in typo["modules"]}
    checks_by = {}
    for c in val["checks"]:
        checks_by.setdefault(c["module"], []).append(c)

    s = val["summary"]
    ic = {"pass": ("✓", "ok"), "warn": ("!", "wa"), "fail": ("✗", "fa")}

    cards = []
    for rec in man["modules"]:
        key = rec["key"]
        m = A.MODULE_BY_KEY[key]
        pl = plate_by[key]
        tb = typo_by[key]["blocks"]
        img = data_uri(os.path.join(OUT, "exports", f"{key}@1x.jpg"))
        rows = checks_by.get(key, [])
        nfail = sum(1 for r in rows if r["status"] == "fail")

        crop = pl["crop"]
        chk = "".join(
            f'<tr class="{ic[r["status"]][1]}"><td class="s">'
            f'{ic[r["status"]][0]}</td><td>{E(r["name"])}</td>'
            f'<td class="m">{E(r["actual"])}</td></tr>' for r in rows)
        typ = "".join(
            f'<tr><td><code>{E(b["id"])}</code></td><td>{E(b["style"])}</td>'
            f'<td class="m">{E(b["font"])}</td>'
            f'<td class="m">{b["size_pt"]:.1f}</td>'
            f'<td class="m">{b["tracking_em"]:.3f}</td>'
            f'<td class="m">{b["x"]:.0f}, {b["y"]:.0f}</td>'
            f'<td class="m">{b["box_w"]:.0f}</td>'
            f'<td class="m">{len(b["lines"])}</td></tr>' for b in tb)

        cards.append(f"""
<section class="card">
  <div class="chead">
    <h3>{E(m.title)}</h3>
    <span class="tag">{E(A.MODULE_TYPES[m.type]["label"])}</span>
    <span class="tag dim">{rec["size"][0]}×{rec["size"][1]}</span>
    <span class="tag {'good' if nfail == 0 else 'bad'}">
      {len(rows)-nfail}/{len(rows)} kontrol</span>
  </div>
  <p class="purpose">{E(m.purpose)}</p>
  <img src="{img}" alt="{E(rec['alt_text'])}" loading="lazy">
  <div class="grid2">
    <div>
      <h4>Kırpma kararı</h4>
      <table class="kv">
        <tr><td>Kaynak</td><td class="m">{pl["source_size"][0]}×{pl["source_size"][1]} px</td></tr>
        <tr><td>Kırpma penceresi</td><td class="m">{crop["w"]}×{crop["h"]} @ ({crop["x"]},{crop["y"]})</td></tr>
        <tr><td>Yön</td><td class="m">{E(crop["mode"])} · sapma {crop["lost_frac"]*100:.1f}%</td></tr>
        <tr><td>Konu korunumu</td><td class="m">%{crop.get("subject_kept",1)*100:.0f}</td></tr>
        <tr><td>Metin bölgesi</td><td class="m">{E(m.text_side)}</td></tr>
        <tr><td>Yüklenecek</td><td class="m">{E(rec["upload_format"])} ·
            {rec["png1x_bytes"]/1024:.0f} KB</td></tr>
      </table>
      <h4>Alt metin</h4>
      <p class="alt">{E(rec["alt_text"])}</p>
    </div>
    <div>
      <h4>Doğrulama</h4>
      <div class="tw"><table class="chk">{chk}</table></div>
    </div>
  </div>
  <h4>Tipografi belirtimi</h4>
  <div class="tw"><table class="typ">
    <thead><tr><th>id</th><th>stil</th><th>font</th><th>pt</th>
    <th>aralık</th><th>x, y</th><th>sütun</th><th>satır</th></tr></thead>
    <tbody>{typ}</tbody></table></div>
</section>""")

    glob = "".join(
        f'<tr class="{ic[r["status"]][1]}"><td class="s">{ic[r["status"]][0]}'
        f'</td><td>{E(r["name"])}</td><td class="m">{E(r["actual"])}</td>'
        f'<td class="n">{E(r["note"])}</td></tr>'
        for r in checks_by.get("—", []))

    doc = f"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Codex Mythologica — Amazon A+ Üretim Raporu</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#0C0B0A;color:#E6E1D8;
 font:15px/1.65 ui-serif,Georgia,'Times New Roman',serif}}
.wrap{{max-width:1180px;margin:0 auto;padding:40px 22px 90px}}
h1{{font-size:clamp(26px,4vw,40px);margin:0 0 6px;color:#EFE9DD;line-height:1.15}}
.sub{{color:#9C948A;margin:0 0 30px}}
h2{{font-size:22px;margin:52px 0 14px;color:#C9A227;
 border-bottom:1px solid #2A2724;padding-bottom:8px;font-weight:600}}
h3{{font-size:19px;margin:0;color:#EFE9DD}}
h4{{font-size:12px;letter-spacing:.09em;text-transform:uppercase;
 color:#9C948A;margin:20px 0 8px;font-weight:600}}
code{{font:12.5px ui-monospace,Menlo,monospace;background:#1A1815;
 padding:1px 5px;border-radius:3px;color:#D9C98A}}
.hero{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
 gap:12px;margin:24px 0}}
.stat{{background:#141210;border:1px solid #2A2724;border-radius:10px;padding:14px 16px}}
.stat .v{{font-size:26px;font-weight:600;color:#C9A227;line-height:1.1}}
.stat .k{{font-size:12px;color:#9C948A;margin-top:4px;letter-spacing:.03em}}
.card{{background:#141210;border:1px solid #2A2724;border-radius:12px;
 padding:20px 22px 24px;margin:0 0 26px}}
.chead{{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin-bottom:6px}}
.tag{{font-size:11px;letter-spacing:.06em;padding:3px 9px;border-radius:99px;
 background:#241F1B;color:#D9C98A}}
.tag.dim{{color:#9C948A}}
.tag.good{{background:#16301F;color:#8FD4A8}}
.tag.bad{{background:#3A1A12;color:#F3A88C}}
.purpose{{color:#9C948A;margin:0 0 14px;font-size:14px}}
.card img{{width:100%;height:auto;display:block;border-radius:8px;
 border:1px solid #2A2724;margin:0 0 6px}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
@media(max-width:820px){{.grid2{{grid-template-columns:1fr}}}}
.tw{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
td,th{{padding:5px 8px;text-align:left;border-bottom:1px solid #201D1A;
 vertical-align:top}}
th{{color:#9C948A;font-size:11px;letter-spacing:.05em;text-transform:uppercase}}
.m{{font:12px ui-monospace,Menlo,monospace;color:#D9C98A;white-space:nowrap}}
.n{{color:#8B8680;font-size:12px}}
.s{{width:22px;text-align:center;font-weight:700}}
.ok .s{{color:#5FBF87}} .wa .s{{color:#E8B627}} .fa .s{{color:#E4572E}}
.fa{{background:#1E1310}}
.kv td:first-child{{color:#9C948A;width:44%}}
.alt{{color:#B9B2A8;font-size:13.5px;margin:0;font-style:italic}}
.note{{background:#141210;border:1px solid #2A2724;border-radius:10px;
 padding:16px 18px;margin:18px 0}}
.note.warn{{border-color:#5A4415;background:#191510}}
.note b{{color:#C9A227}}
ul{{margin:0 0 12px;padding-left:20px}} li{{margin:5px 0;color:#B9B2A8}}
ol{{padding-left:20px}} ol li{{margin:7px 0;color:#B9B2A8}}
footer{{margin-top:56px;padding-top:20px;border-top:1px solid #2A2724;
 color:#6B6560;font-size:12.5px}}
@media (prefers-color-scheme:light){{
 body{{background:#FBF9F5;color:#221F1B}}
 .card,.stat,.note{{background:#FFF;border-color:#E3DED4}}
 h1,h3{{color:#171512}} .sub,.purpose,.n,li,.alt{{color:#6B655C}}
 .fa{{background:#FDF0EC}} code,.m{{color:#7A5E10}}
 code{{background:#F3EFE6}}
}}
</style></head><body><div class="wrap">

<h1>Amazon A+ İçerik — üretim raporu</h1>
<p class="sub">CODEX MYTHOLOGICA · {len(man["modules"])} modül ·
tipografi tamamen kodla çözüldü, elle konumlandırma yok</p>

<div class="hero">
 <div class="stat"><div class="v">{s["pass"]}/{s["total"]}</div>
  <div class="k">DOĞRULAMA KONTROLÜ</div></div>
 <div class="stat"><div class="v">{s["fail"]}</div><div class="k">BAŞARISIZ</div></div>
 <div class="stat"><div class="v">{len(man["modules"])}</div>
  <div class="k">MODÜL</div></div>
 <div class="stat"><div class="v">4</div><div class="k">ÇIKTI BİÇİMİ</div></div>
</div>

<h2>Yöntem</h2>
<p>Sanat eserlerine dokunulmadı. Yapılan iş yalnızca üretim mühendisliğidir ve
kapak boru hattıyla aynı ilkeleri izler:</p>
<ol>
<li><b>Otomatik analiz.</b> Her görselin belirginlik haritası, baskın konu
kutusu, negatif alanları ve doku yoğunluğu ölçülür. Kullanıcıdan hiçbir
koordinat istenmez.</li>
<li><b>Konu koruyan kırpma.</b> Hedef en-boy oranına ulaşmak için gereken
pencere hesaplanır; ölçek X ve Y'de daima eşittir.</li>
<li><b>Sığdırarak çözülen tipografi.</b> Punto boyutu iki kısıtın küçüğüdür:
modül genişliğine oranlı tavan ve kutuya tam oturan boyut. Metin taşarsa
sessizce kırpılmaz — derleme durur.</li>
<li><b>Çarpışma sınırı ölçümü.</b> Metin sütununun nerede biteceği, sanat
eserinin sütun parlaklık profilinde zeminden yükselen ilk noktadan bulunur.</li>
<li><b>Tek render, üç biçim.</b> Tipografi bir kez vektör olarak çizilir;
PNG'ler o PDF'ten rasterlenir. Biçimler arası kayma imkânsızdır.</li>
</ol>

<div class="note"><p><b>Sanat eserinin kendi yapısı kullanıldı.</b>
module-2'de üç altın çerçeveli panel zaten çizilmişti: filetolar tespit edilip
metin tam onların içine yerleştirildi. module-3'te üç kaide ve module-5'te üç
kitap açılımı ayırıcı tespitiyle hücrelere bölündü. Tipografi sanat eserinin
üstüne konmadı; <i>onun mimarisine</i> oturtuldu.</p></div>

<h2>Modüller</h2>
{''.join(cards)}

<h2>Modüller arası tutarlılık</h2>
<div class="tw"><table class="chk">{glob}</table></div>

<h2>Yükleme sırası</h2>
<p>Amazon KDP → Marketing → A+ Content Manager → Create A+ Content.
Modülleri bu sırayla ekleyin; her birine kendi alt metnini girin.</p>
<div class="tw"><table>
<thead><tr><th>#</th><th>Modül tipi</th><th>Dosya</th><th>Ölçü</th>
<th>Boyut</th></tr></thead><tbody>
{''.join(f'<tr><td>{i}</td><td>{E(A.MODULE_TYPES[A.MODULE_BY_KEY[r["key"]].type]["label"])}</td>'
         f'<td><code>{E(os.path.basename(r["upload_file"]))}</code></td>'
         f'<td class="m">{r["size"][0]}×{r["size"][1]}</td>'
         f'<td class="m">{r["png1x_bytes"]/1024:.0f} KB</td></tr>'
         for i, r in enumerate(man["modules"], 1))}
</tbody></table></div>

<div class="note warn">
<p><b>Yayından önce gözden geçirin.</b> Amazon A+ kuralları rakip ürün
karşılaştırmasını yasaklar. Üçüncü modül hiçbir marka, yazar veya kitap adı
geçirmez; yalnızca <i>kitap türlerini</i> tarif eder ve bu kitaba dair bütün
iddialar doğrulanabilirdir (19 gelenek, 76 anlatı, 329 sayfa). Bu ayrım
kasıtlıdır, ancak nihai karar sizindir — metni yumuşatmak isterseniz
<code>08_BUILD/aplus_copy.py</code> içindeki <code>M3</code> sözlüğünü
düzenleyip boru hattını yeniden çalıştırmanız yeterli.</p>
</div>

<div class="note">
<p><b>@2x dosyaları neden var?</b> Amazon modül ölçülerini <i>görüntüleme</i>
ölçüsü olarak tanımlar. @1x kanoniktir ve yüklenecek olandır; @2x retina
ekranlar için yedektir ve 2 MB sınırını aştığı için doğrudan yüklenmemelidir.
JPEG sürümleri de üretildi: PNG bir modülde sınırı aşarsa
<code>aplus-manifest.json</code> otomatik olarak JPEG'i işaret eder.</p>
</div>

<footer>Üretildi: <code>08_BUILD/make_aplus_report.py</code> ·
Bütün sayılar <code>aplus_spec.py</code>, <code>aplus_layout.py</code> ve
<code>validate_aplus.py</code> kaynaklıdır · Dış bağlantı yoktur.</footer>
</div></body></html>"""

    dst = os.path.join(ROOT, "06_REPORTS", "APLUS_PRODUCTION_REPORT.html")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"  → 06_REPORTS/APLUS_PRODUCTION_REPORT.html "
          f"({os.path.getsize(dst)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
