#!/usr/bin/env python3
"""
CODEX BESTIARIUM — İLLÜSTRASYON PROMPT KÜTÜPHANESİ
================================================================================
`BESTIARIUM_IMAGE_PROMPTS.html` dosyasını üretir: 120 plakanın tamamı için
kopyalanabilir prompt, negatif prompt, dosya adı, çıktı yolu, önerilen ölçü,
üretim/üslup/tutarlılık notları.

TASARIM KARARI — PROMPT ELLE YAZILMAZ
    Prompt bir metin değil, bir FONKSİYONDUR:

        prompt = üslup gövdesi (120 plakada AYNI)
               + konu (plakaya özgü)
               + kompozisyon (sınıfa göre)
               + ölçü ve teknik kuyruğu (AYNI)

    Üslup gövdesi tek bir yerde tanımlıdır. Değişirse 120 promptun tamamı
    birlikte değişir. Yol haritası Bölüm 07.3'ün "tek çizgi dili" şartı
    ancak böyle tutulabilir — 120 promptu elle tutarlı yazmak mümkün değildir
    ve projenin tek gerçek başarısızlık modu tam olarak budur.

KULLANIM
    python3 08_BUILD/make_prompts.py
    python3 08_BUILD/make_prompts.py --check     # bayat mı?
"""

from __future__ import annotations

import argparse
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    PLATE_SPEC,
    ROOT,
    SOURCE_DIR,
    load_spec,
)

OUT_PATH = os.path.join(ROOT, "BESTIARIUM_IMAGE_PROMPTS.html")
SUBJECTS_PATH = os.path.join(SOURCE_DIR, "plate_subjects.json")

# =============================================================================
# PROMPT MOTORU
# =============================================================================

# 120 plakada DEĞİŞMEYEN üslup gövdesi. Tek çizgi dilinin kaynağı budur.
STYLE_BODY = (
    "antique line engraving, single-colour black ink on white, "
    "copperplate hatching and cross-hatching, uniform stroke weight, "
    "45-degree primary hatch with 135-degree secondary hatch, "
    "no wash, no grey tone, no shading gradients, "
    "empty white background with no scene, no ground line, no horizon, "
    "no border, no frame, no ornament, "
    "scientific plate from a 19th-century natural history atlas, "
    "full figure, subject isolated in blank space"
)

# Sınıfa göre kompozisyon. Bakış sola veya izleyiciye (Bölüm 07.3).
CLASS_COMPOSITION = {
    "I":   "standing frontal and still, facing the viewer, weight even, "
           "the posture of something that will not move aside",
    "II":  "in three-quarter view turned left, mouth or maw the compositional "
           "centre, body tensed toward the viewer",
    "III": "caught mid-transformation, two forms legible in one silhouette, "
           "turned left",
    "IV":  "emerging, the lower body dissolving into blank space where water "
           "would be, head turned left",
    "V":   "wings fully spread, seen from slightly below, gaze toward the viewer",
    "VI":  "upright and gaunt, facing the viewer, outline broken and unresolved "
           "at the edges",
}

# Her plakada zorunlu: insan siluetiyle ölçek işareti (Bölüm 07.3).
SCALE_CLAUSE = (
    "a small plain human silhouette placed at the lower left as a scale marker, "
    "solid black, no detail, no face"
)

TECH_TAIL = (
    f"vertical composition, aspect ratio 4:5, "
    f"{PLATE_SPEC['target_width_px']} x {PLATE_SPEC['target_height_px']} pixels, "
    f"{PLATE_SPEC['dpi']} DPI, "
    f"subject occupying {int(PLATE_SPEC['coverage'][0] * 100)}-"
    f"{int(PLATE_SPEC['coverage'][1] * 100)} percent of the canvas, "
    "pure white background, maximum ink density 92 percent, "
    "lightest hatching 8 percent"
)

NEGATIVE = (
    "colour, colours, colour wash, watercolour, painting, photograph, "
    "photorealistic, 3d render, digital painting, airbrush, soft shading, "
    "gradient, grey tone, greyscale wash, blur, bokeh, depth of field, "
    "background scenery, landscape, forest, mountains, sky, clouds, water, "
    "ground, shadow, cast shadow, horizon line, "
    "frame, border, cartouche, ornament, banner, scroll, "
    "text, letters, words, caption, signature, watermark, logo, numbers, "
    "cute, chibi, kawaii, cartoon, anime, mascot, friendly, smiling, "
    "heroic pose, dynamic action lines, motion blur, speed lines, "
    "armour with rivets, fantasy game art, concept art sheet, "
    "multiple subjects, duplicate creature, cropped limbs, cut off head, "
    "extra limbs, extra heads beyond those specified, malformed anatomy, "
    "modern clothing, modern objects"
)


def build_prompt(creature: dict, subject: str) -> str:
    comp = CLASS_COMPOSITION.get(creature["class"], CLASS_COMPOSITION["I"])
    return (
        f"{subject}, {comp}. "
        f"{SCALE_CLAUSE}. "
        f"{STYLE_BODY}. "
        f"{TECH_TAIL}."
    )


def generation_notes(creature: dict, spec: dict) -> list[str]:
    trad = next(
        (t for t in spec["traditions"] if t["id"] == creature["tradition"]), {}
    )
    kin = {k["id"]: k for k in spec["kinFamilies"]}
    notes = []
    notes.append(
        f"Gelenek: {trad.get('name', '?')} {trad.get('sigil', '')} · "
        f"{trad.get('regionGroup', '')}"
    )
    if creature.get("kinFamily"):
        fam = kin.get(creature["kinFamily"], {})
        notes.append(
            f"Akraba imge ailesi <b>{creature['kinFamily']} · {fam.get('tr', '')}</b> — "
            f"bu plaka karşılaştırma açılışında ailenin diğer üyeleriyle "
            f"<b>yan yana</b> basılacak. Silüet ölçeği ve bakış yönü aile "
            f"içinde tutarlı olmalı."
        )
    if trad.get("sourceRisk") == "high":
        notes.append(
            "⚠ Bu gelenek İngilizce yayımlanmış kaynak açısından zayıftır. "
            "Plaka üretimi <b>araştırma dosyası tamamlanmadan</b> başlamaz — "
            "aksi hâlde çizim, doğrulanmamış bir tarife dayanır."
        )
    if creature["tradition"] in {
        "inuit", "ainu", "sapmi", "anishinaabe", "ma-ohi", "melanesia",
        "nguni", "tupi-guarani", "yoruba-ashanti", "tawantinsuyu",
        "ityop-ya", "bod", "mongol",
    }:
        notes.append(
            "⚠ Yaşayan gelenek. Tören nesnesi, maske deseni veya klan işareti "
            "<b>çizilmez</b>; yalnızca yayımlanmış ve kısıtlanmamış tarife "
            "dayanılır."
        )
    if not creature.get("sources"):
        notes.append(
            "Kaynak alanı boş — bu plaka <b>tohum tarifiyle</b> üretilecektir. "
            "Faz 1 bittiğinde prompt yeniden üretilmeli."
        )
    return notes


# =============================================================================
# HTML
# =============================================================================

CSS = """
:root{
  --bg:#0f0e0c; --panel:#171613; --panel-2:#1e1c18; --line:#2e2b25;
  --ink:#e8e0ce; --ink-2:#b9ae95; --ink-3:#8a8171;
  --gold:#c9a227; --gold-lt:#e3c766; --warn:#d08a3e; --ok:#7d9a6a;
  --serif:'EB Garamond',Georgia,'Times New Roman',serif;
  --sans:ui-sans-serif,system-ui,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,'SF Mono',Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:light){
  :root{--bg:#f5f1e8;--panel:#fffdf8;--panel-2:#f0ebdf;--line:#ddd5c4;
        --ink:#241f18;--ink-2:#5a5142;--ink-3:#867c68;--gold:#8a6d10;}
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
     font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--gold-lt)}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px 80px}
header{border-bottom:1px solid var(--line);padding:38px 0 26px;margin-bottom:26px}
.kicker{font-size:11px;letter-spacing:.22em;text-transform:uppercase;
        color:var(--gold);font-weight:600}
h1{font-family:var(--serif);font-size:clamp(30px,5vw,46px);margin:.25em 0 .1em;
   font-weight:500;letter-spacing:.01em}
.sub{color:var(--ink-2);max-width:70ch}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:8px;
      padding:8px 14px;font-size:13px}
.stat b{color:var(--gold-lt);font-family:var(--mono)}
.controls{position:sticky;top:0;z-index:20;background:var(--bg);
          border-bottom:1px solid var(--line);padding:12px 0;margin-bottom:22px;
          display:flex;flex-wrap:wrap;gap:8px;align-items:center}
input[type=search],select{background:var(--panel);color:var(--ink);
  border:1px solid var(--line);border-radius:8px;padding:8px 12px;
  font-family:var(--sans);font-size:14px}
input[type=search]{flex:1;min-width:200px}
.chip{background:var(--panel);border:1px solid var(--line);color:var(--ink-2);
  border-radius:999px;padding:6px 13px;font-size:12.5px;cursor:pointer;
  user-select:none}
.chip[aria-pressed=true]{background:var(--gold);border-color:var(--gold);
  color:#191713;font-weight:600}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;
      margin-bottom:16px;overflow:hidden}
.card summary{cursor:pointer;padding:14px 18px;display:flex;gap:12px;
  align-items:baseline;flex-wrap:wrap;list-style:none}
.card summary::-webkit-details-marker{display:none}
.num{font-family:var(--mono);color:var(--gold);font-size:13px;min-width:3.2em}
.nm{font-family:var(--serif);font-size:20px;font-weight:500}
.meta{color:var(--ink-3);font-size:12.5px;font-family:var(--mono)}
.tag{border:1px solid var(--line);border-radius:5px;padding:1px 7px;
     font-size:11px;color:var(--ink-2);font-family:var(--mono)}
.tag.kin{border-color:var(--gold);color:var(--gold-lt)}
.body{padding:0 18px 18px;border-top:1px solid var(--line)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));
      gap:10px;margin:14px 0}
.f{background:var(--panel-2);border:1px solid var(--line);border-radius:8px;
   padding:9px 12px}
.f .k{font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;
      color:var(--ink-3)}
.f .v{font-family:var(--mono);font-size:12.5px;word-break:break-all;
      color:var(--ink)}
.block{margin-top:14px}
.block h4{margin:0 0 7px;font-size:11px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--gold);font-weight:600;
  display:flex;justify-content:space-between;align-items:center;gap:10px}
pre{margin:0;background:var(--panel-2);border:1px solid var(--line);
    border-radius:8px;padding:12px 14px;font-family:var(--mono);font-size:12.5px;
    line-height:1.65;white-space:pre-wrap;word-break:break-word;
    max-height:none;overflow-x:auto}
pre.neg{color:var(--ink-2)}
button.copy{background:var(--gold);color:#191713;border:0;border-radius:6px;
  padding:5px 13px;font-size:11.5px;font-weight:700;cursor:pointer;
  letter-spacing:.05em;text-transform:uppercase;font-family:var(--sans)}
button.copy:hover{background:var(--gold-lt)}
button.copy.done{background:var(--ok);color:#0f0e0c}
ul.notes{margin:8px 0 0;padding-left:20px;color:var(--ink-2);font-size:13.5px}
ul.notes li{margin:5px 0}
.callout{border-left:3px solid var(--gold);background:var(--panel-2);
  padding:12px 16px;border-radius:0 8px 8px 0;margin:18px 0;font-size:14px}
.callout.warn{border-color:var(--warn)}
h2{font-family:var(--serif);font-weight:500;font-size:26px;
   margin:36px 0 6px;border-bottom:1px solid var(--line);padding-bottom:8px}
table{width:100%;border-collapse:collapse;font-size:13.5px;margin:12px 0}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line)}
th{color:var(--ink-3);font-size:11px;letter-spacing:.1em;text-transform:uppercase;
   font-weight:600}
td.n{text-align:right;font-family:var(--mono)}
.tw{overflow-x:auto}
footer{margin-top:50px;padding-top:20px;border-top:1px solid var(--line);
  color:var(--ink-3);font-size:12.5px}
.hidden{display:none !important}
@media print{.controls,button.copy{display:none}.card{break-inside:avoid}}
"""

JS = """
const q=document.getElementById('q'),
      selClass=document.getElementById('fclass'),
      selKin=document.getElementById('fkin'),
      selRisk=document.getElementById('frisk'),
      cards=[...document.querySelectorAll('.card')],
      count=document.getElementById('count');

function apply(){
  const t=(q.value||'').toLowerCase().trim();
  const c=selClass.value,k=selKin.value,rk=selRisk.value;
  let n=0;
  for(const el of cards){
    const hay=el.dataset.search;
    let ok = (!t || hay.includes(t))
          && (!c || el.dataset.class===c)
          && (!k || el.dataset.kin===k)
          && (!rk || el.dataset.risk===rk);
    el.classList.toggle('hidden',!ok);
    if(ok) n++;
  }
  count.textContent=n;
}
[q,selClass,selKin,selRisk].forEach(el=>el.addEventListener('input',apply));

document.addEventListener('click',async e=>{
  const b=e.target.closest('button.copy'); if(!b) return;
  const src=document.getElementById(b.dataset.target);
  const text=src.textContent;
  try{ await navigator.clipboard.writeText(text); }
  catch(_){
    const ta=document.createElement('textarea');
    ta.value=text; document.body.appendChild(ta); ta.select();
    document.execCommand('copy'); ta.remove();
  }
  const old=b.textContent; b.textContent='kopyalandı ✓'; b.classList.add('done');
  setTimeout(()=>{b.textContent=old;b.classList.remove('done');},1400);
});

document.getElementById('expand').addEventListener('click',()=>{
  const any=cards.some(c=>!c.open&&!c.classList.contains('hidden'));
  cards.forEach(c=>{if(!c.classList.contains('hidden'))c.open=any;});
});
apply();
"""


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def render(spec: dict, subjects: dict) -> str:
    creatures = spec["creatures"]
    trads = {t["id"]: t for t in spec["traditions"]}
    classes = {c["id"]: c for c in spec["classes"]}
    kin = {k["id"]: k for k in spec["kinFamilies"]}

    P = []
    A = P.append
    A("<title>Codex Bestiarium · İllüstrasyon Prompt Kütüphanesi</title>")
    A(f"<style>{CSS}</style>")
    A('<div class="wrap">')

    # --- başlık ---
    A("<header>")
    A('<div class="kicker">Vâliçe Press · Codex Serisi Cilt II</div>')
    A("<h1>İllüstrasyon Prompt Kütüphanesi</h1>")
    A('<p class="sub">120 plakanın tamamı. Her prompt <b>üretilmiştir</b>, elle '
      "yazılmamıştır: değişmeyen bir üslup gövdesi + plakaya özgü konu + "
      "sınıfa göre kompozisyon + teknik kuyruk. Üslup gövdesi tek bir yerde "
      "durur; değişirse 120 promptun tamamı birlikte değişir. Yol haritası "
      "Bölüm 07.3'ün <b>tek çizgi dili</b> şartı ancak böyle tutulabilir.</p>")
    A('<div class="stats">')
    A(f'<div class="stat">Plaka <b>{len(creatures)}</b></div>')
    A(f'<div class="stat">Gelenek <b>{len(trads)}</b></div>')
    A(f'<div class="stat">Sınıf <b>{len(classes)}</b></div>')
    A(f'<div class="stat">Akraba ailesi <b>{len(kin)}</b></div>')
    A(f'<div class="stat">Tuval <b>{PLATE_SPEC["target_width_px"]}×'
      f'{PLATE_SPEC["target_height_px"]}</b></div>')
    A(f'<div class="stat">Çözünürlük <b>{PLATE_SPEC["dpi"]} DPI</b></div>')
    A("</div></header>")

    # --- üretim protokolü ---
    A("<h2>Üretim protokolü</h2>")
    A('<div class="callout"><b>Pilot set kilidi.</b> Önce yalnızca on plaka '
      "üretilir (altı sınıftan örnek). <code>plates.py --pilot</code> ölçer. "
      "Ölçülen dağılım tolerans bandında değilse üslup gövdesi düzeltilir ve "
      "pilot yeniden üretilir. <b>Pilot onaylanmadan diğer 110'a geçilmez.</b>"
      "</div>")
    A('<div class="callout warn"><b>Ölçüm göz kararının yerine geçer.</b> '
      "Ham çıktı <code>07_ASSETS/plates_raw/</code> içine <b>değiştirilmeden</b> "
      "konur. <code>plates.py --normalize</code> kırpar, seviyeler, hedef "
      "tuvale oturtur ve beş parametreyi ölçer: çizgi kalınlığı, tarama açısı, "
      "tarama sıklığı, mürekkep aralığı, kapsama. <b>Bant dışına çıkan plaka "
      "otomatik reddedilir</b> — bu karar insana bırakılmaz, çünkü 120 plakada "
      "göz kalibrasyonu kayar.</div>")

    A("<div class='tw'><table><thead><tr><th>Adım</th><th>Komut / eylem</th>"
      "<th>Çıktı</th></tr></thead><tbody>")
    for step, cmd, out in [
        ("1 · Prompt", "Bu sayfadan <b>Prompt kopyala</b>",
         "görsel modeline girdi"),
        ("2 · Ham çıktı", "PNG'yi <code>07_ASSETS/plates_raw/plate-NNN.png</code> "
         "olarak kaydet", "ham dosya — <b>asla değiştirilmez</b>"),
        ("3 · Normalize", "<code>python3 08_BUILD/plates.py --normalize</code>",
         "<code>07_ASSETS/plates/plate-NNN.png</code>"),
        ("4 · Ölçüm", "<code>python3 08_BUILD/plates.py --measure -v</code>",
         "<code>06_REPORTS/plate-consistency.json</code>"),
        ("5 · İnsan geçişi", "vektör araçta temizlik (~25 dk/plaka)",
         "kopuk çizgi, anatomi, parazit leke"),
        ("6 · Yayın formatları",
         "<code>python3 08_BUILD/convert_plates.py</code>",
         "baskı TIFF · Kindle PNG (≤60 KB) · A+ JPEG"),
    ]:
        A(f"<tr><td>{step}</td><td>{cmd}</td><td>{out}</td></tr>")
    A("</tbody></table></div>")

    # --- şartname ---
    A("<h2>Çizgi dili şartnamesi</h2>")
    A("<div class='tw'><table><thead><tr><th>Parametre</th><th>Değer</th>"
      "<th>Tolerans</th></tr></thead><tbody>")
    s = PLATE_SPEC
    for label, value, tol in [
        ("Teknik", "gravür / hat taraması, tek renk", "—"),
        ("Tuval", f"1:{s['aspect']} dikey · "
                  f"{s['target_width_px']}×{s['target_height_px']} px", "sabit"),
        ("Ana çizgi kalınlığı", f"{s['line_weight_pt']} pt "
         f"(~{s['line_weight_pt'] * s['dpi'] / 72:.1f} px @ {s['dpi']} DPI)",
         f"±%{int(s['line_weight_tol'] * 100)}"),
        ("Tarama açısı", f"{s['hatch_primary_deg']:.0f}° birincil · "
         f"{s['hatch_secondary_deg']:.0f}° ikincil",
         f"±{s['hatch_angle_tol_deg']:.0f}°"),
        ("Tarama sıklığı",
         f"cm başına {s['hatch_lines_per_cm'][0]}–{s['hatch_lines_per_cm'][1]} çizgi",
         "bant"),
        ("Zemin", "boş — yaratık boşlukta durur, sahne yok", "zorunlu"),
        ("Kontrast", f"en koyu %{int(s['ink_darkest'] * 100)} – "
         f"en açık %{int(s['ink_lightest'] * 100)} siyah",
         f"±%{int(s['ink_tol'] * 100)}"),
        ("Kompozisyon", f"yaratık tuvalin %{int(s['coverage'][0] * 100)}–"
         f"%{int(s['coverage'][1] * 100)}'ini kaplar; bakış sola veya izleyiciye",
         "bant"),
        ("Ölçek işareti", "her plakada ince bir insan siluetiyle ölçek", "zorunlu"),
    ]:
        A(f"<tr><td>{label}</td><td>{value}</td><td>{tol}</td></tr>")
    A("</tbody></table></div>")

    # --- ortak negatif prompt ---
    A("<h2>Ortak negatif prompt</h2>")
    A("<p class='sub'>120 plakada aynıdır. Her kartta ayrıca kopyalanabilir.</p>")
    A('<div class="block"><h4>Negative prompt'
      '<button class="copy" data-target="neg-global">Kopyala</button></h4>'
      f'<pre class="neg" id="neg-global">{esc(NEGATIVE)}</pre></div>')

    # --- denetimler ---
    A("<h2>120 plaka</h2>")
    A('<div class="controls">')
    A('<input type="search" id="q" placeholder="ara: ad, gelenek, motif, plaka…" '
      'aria-label="ara">')
    A('<select id="fclass" aria-label="sınıf"><option value="">Bütün sınıflar</option>')
    for cid in ["I", "II", "III", "IV", "V", "VI"]:
        c = classes[cid]
        A(f'<option value="{cid}">{cid} · {esc(c["tr"])}</option>')
    A("</select>")
    A('<select id="fkin" aria-label="aile"><option value="">Bütün aileler</option>')
    for kid in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        A(f'<option value="{kid}">{kid} · {esc(kin[kid]["tr"])}</option>')
    A('<option value="-">aileye bağlı değil</option></select>')
    A('<select id="frisk" aria-label="risk"><option value="">Bütün gelenekler</option>'
      '<option value="high">yalnızca kaynak riski yüksek</option></select>')
    A('<span class="chip" id="expand" role="button" tabindex="0" '
      'aria-pressed="false">Hepsini aç / kapa</span>')
    A('<span class="meta"><span id="count">0</span> plaka</span>')
    A("</div>")

    # --- kartlar ---
    for c in creatures:
        cid = c["id"]
        subj = subjects.get(cid, {}).get("subject", "")
        prompt = build_prompt(c, subj) if subj else ""
        trad = trads.get(c["tradition"], {})
        klass = classes.get(c["class"], {})
        fam = kin.get(c["kinFamily"], {}) if c.get("kinFamily") else {}
        pid = c["plate"]
        search = " ".join([
            c["name"], cid, pid, trad.get("name", ""), klass.get("tr", ""),
            klass.get("en", ""), " ".join(c["motif"]), c.get("seedNoteTr", ""),
            subj,
        ]).lower()

        A(f'<details class="card" data-class="{c["class"]}" '
          f'data-kin="{c.get("kinFamily") or "-"}" '
          f'data-risk="{trad.get("sourceRisk", "normal")}" '
          f'data-search="{esc(search)}" id="{esc(pid)}">')
        A("<summary>")
        A(f'<span class="num">{c["number"]:03d}</span>')
        A(f'<span class="nm">{esc(c["name"])}</span>')
        A(f'<span class="tag">{c["class"]} · {esc(klass.get("tr", ""))}</span>')
        A(f'<span class="tag">{esc(trad.get("name", ""))} '
          f'{esc(trad.get("sigil", ""))}</span>')
        A(f'<span class="tag">{esc(" · ".join(c["motif"]))}</span>')
        if fam:
            A(f'<span class="tag kin">{c["kinFamily"]} · {esc(fam.get("tr", ""))}</span>')
        A(f'<span class="meta">{esc(pid)}</span>')
        A("</summary>")

        A('<div class="body">')
        A(f'<p class="sub" style="margin:12px 0 0">{esc(c.get("seedNoteTr", ""))}</p>')

        A('<div class="grid">')
        for k, v in [
            ("Yaratık", c["name"]),
            ("Bölüm", f'{c["class"]} · {klass.get("en", "")}'),
            ("Gelenek", f'{trad.get("name", "")} {trad.get("sigil", "")}'),
            ("Plaka kimliği", pid),
            ("Dosya adı", f"{pid}.png"),
            ("Ham çıktı yolu", f"07_ASSETS/plates_raw/{pid}.png"),
            ("PNG çıktı yolu", f"07_ASSETS/plates/{pid}.png"),
            ("Baskı çıktısı", f"07_ASSETS/plates_print/{pid}.tif"),
            ("Önerilen ölçü",
             f'{PLATE_SPEC["target_width_px"]}×{PLATE_SPEC["target_height_px"]} px '
             f'@ {PLATE_SPEC["dpi"]} DPI'),
            ("Kindle bütçesi", "≤60 KB"),
            ("Motif kodu", " · ".join(c["motif"])),
            ("Araştırma dosyası", c["researchFile"]),
        ]:
            A(f'<div class="f"><div class="k">{esc(k)}</div>'
              f'<div class="v">{esc(v)}</div></div>')
        A("</div>")

        if prompt:
            A(f'<div class="block"><h4>Prompt'
              f'<button class="copy" data-target="p-{esc(pid)}">Prompt kopyala</button>'
              f'</h4><pre id="p-{esc(pid)}">{esc(prompt)}</pre></div>')
        A(f'<div class="block"><h4>Negatif prompt'
          f'<button class="copy" data-target="n-{esc(pid)}">Negatif kopyala</button>'
          f'</h4><pre class="neg" id="n-{esc(pid)}">{esc(NEGATIVE)}</pre></div>')

        A('<div class="block"><h4>Üretim notları</h4><ul class="notes">')
        for note in generation_notes(c, spec):
            A(f"<li>{note}</li>")
        A("</ul></div>")

        A('<div class="block"><h4>Üslup notları</h4><ul class="notes">')
        A(f"<li>Kompozisyon (sınıf {c['class']}): "
          f"{esc(CLASS_COMPOSITION.get(c['class'], ''))}</li>")
        A("<li>Zemin <b>boş</b>. Sahne, zemin çizgisi, ufuk, çerçeve ve süs "
          "yasaktır — yaratık boşlukta durur.</li>")
        A("<li>Ölçek işareti zorunludur: sol altta düz siyah insan silueti, "
          "yüzsüz ve detaysız.</li>")
        A("<li>Tek renk siyah mürekkep. Gri ton, yıkama veya degrade yok; "
          "tonlama yalnızca tarama sıklığıyla yapılır.</li>")
        A("</ul></div>")

        A('<div class="block"><h4>Tutarlılık notları</h4><ul class="notes">')
        if fam:
            sibs = [
                x["name"] for x in creatures
                if x.get("kinFamily") == c["kinFamily"] and x["id"] != cid
            ]
            A(f"<li><b>Aile {c['kinFamily']} · {esc(fam.get('tr', ''))}</b> — "
              f"karşılaştırma açılışında yan yana basılacaklar: "
              f"{esc(', '.join(sibs))}. Silüet ölçeği ve bakış yönü aile "
              f"içinde <b>aynı</b> olmalı.</li>")
        A(f"<li>Çizgi kalınlığı {PLATE_SPEC['line_weight_pt']} pt "
          f"±%{int(PLATE_SPEC['line_weight_tol'] * 100)} — "
          f"<code>plates.py</code> ölçer, bant dışı plaka reddedilir.</li>")
        A(f"<li>Kapsama %{int(PLATE_SPEC['coverage'][0] * 100)}–"
          f"%{int(PLATE_SPEC['coverage'][1] * 100)}. Daha küçük yaratık sayfada "
          f"kaybolur, daha büyüğü madde başlığı bloğunu ezer.</li>")
        A("<li>Pilot setle üretim setinin ölçülen dağılımları örtüşmelidir; "
          "örtüşmüyorsa üslup gövdesi kaymıştır.</li>")
        A("</ul></div>")

        A("</div></details>")

    A("<footer>")
    A("<p>Bu sayfa <code>08_BUILD/make_prompts.py</code> tarafından "
      "<code>01_SOURCE/spec.json</code> ve "
      "<code>01_SOURCE/plate_subjects.json</code>'dan üretilir. "
      "<b>Elle düzenlemeyin</b> — bir sonraki üretimde kaybolur. "
      "Prompt değişecekse <code>make_prompts.py</code> içindeki "
      "<code>STYLE_BODY</code>, <code>CLASS_COMPOSITION</code> veya "
      "<code>NEGATIVE</code> düzenlenir ve betik yeniden çalıştırılır.</p>")
    A("<p>AI görsel beyanı KDP yükleme ekranında işaretlenir. Künyede ve "
      "illüstrasyon notunda süreç açıkça anlatılır.</p>")
    A("</footer></div>")
    A(f"<script>{JS}</script>")
    return "\n".join(P) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    spec = load_spec()
    with open(SUBJECTS_PATH, encoding="utf-8") as fh:
        subjects = json.load(fh)["subjects"]

    missing = [c["id"] for c in spec["creatures"] if c["id"] not in subjects]
    if missing:
        print(f"HATA: plaka konusu eksik: {missing[:10]}", file=sys.stderr)
        return 2

    content = render(spec, subjects)

    if args.check:
        if not os.path.exists(OUT_PATH):
            print("BAYAT: BESTIARIUM_IMAGE_PROMPTS.html yok")
            return 1
        with open(OUT_PATH, encoding="utf-8") as fh:
            if fh.read() != content:
                print("BAYAT: BESTIARIUM_IMAGE_PROMPTS.html güncel değil")
                print("Düzeltmek için: python3 08_BUILD/make_prompts.py")
                return 1
        print("TAMAM: prompt kütüphanesi güncel.")
        return 0

    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"yazıldı: {os.path.relpath(OUT_PATH, ROOT)} · "
          f"{len(spec['creatures'])} plaka")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
