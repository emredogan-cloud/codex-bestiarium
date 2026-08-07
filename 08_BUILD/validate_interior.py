"""
İÇ BLOK DOĞRULAMA — üretilen iç blok PDF'inin KDP'ye uygunluğunu kanıtlar.
================================================================================
İki tür kontrol yapılır:

  YAPISAL  — PDF'in kendi nesnelerinden okunur: sayfa ölçüsü, sayfa sayısı,
             font gömme ve alt kümeleme, saydamlık, görsel, metadata.
  DENEYSEL — Sayfalar GERÇEKTEN RENDER EDİLİR ve mürekkep sınırları ölçülür.
             Marj hatası "sayı doğru, çıktı yanlış" türündendir ve ancak
             render ölçülerek yakalanır — kapak tarafında öğrenilen ders.

Kullanım:
    python3 08_BUILD/validate_interior.py --edition hardcover
    python3 08_BUILD/validate_interior.py --edition largeprint --sample 40

Çıktı: 06_REPORTS/<SÜRÜM>/interior-validation.json + konsol tablosu
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image
from pypdf import PdfReader

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editions as E   # noqa: E402
import paths as P      # noqa: E402
import matter as M     # noqa: E402

ROOT = P.ROOT
PT = 72.0
TOL_IN = 0.003          # kabul edilen ölçü sapması
RENDER_DPI = 150
INK_THRESHOLD = 205     # bu değerin altındaki gri = mürekkep
KDP_EDGE_MIN = 0.25     # taşmasız kitapta kesim kenarına asgari uzaklık


class Checks:
    def __init__(self):
        self.rows = []

    def add(self, cid, group, name, ok, expected, actual, note="", warn=False):
        self.rows.append({
            "id": cid, "group": group, "name": name,
            "status": "warn" if (warn and not ok) else ("pass" if ok else "fail"),
            "expected": str(expected), "actual": str(actual), "note": note})

    @property
    def failed(self):
        return [r for r in self.rows if r["status"] == "fail"]

    @property
    def warned(self):
        return [r for r in self.rows if r["status"] == "warn"]


# =============================================================================
# YAPISAL
# =============================================================================

def structural(pdf_path, ed, C):
    r = PdfReader(pdf_path)
    n = len(r.pages)

    prof = ed.profile
    C.add("S1", "Yapı", "Sayfa sayısı ciltleme sınırında",
          prof.min_pages <= n <= prof.max_pages,
          f"{prof.min_pages}–{prof.max_pages}", n,
          f"{prof.label} için KDP sınırı")

    # KDP çift sayfa istemez ama tek sayfalı bir blok basılırken sona boş
    # sayfa eklenir; bunu bilerek üretmek daha temizdir.
    C.add("S2", "Yapı", "Sayfa sayısı çift", n % 2 == 0, "çift", n,
          "tek sayılı blokta matbaa sona boş sayfa ekler", warn=True)

    pg = r.pages[0]
    w_in = float(pg.mediabox.width) / PT
    h_in = float(pg.mediabox.height) / PT
    C.add("S3", "Ölçü", "Sayfa genişliği (trim)",
          abs(w_in - ed.trim_w) <= TOL_IN, f"{ed.trim_w:.4f} in",
          f"{w_in:.4f} in", "taşma yok — kesim ölçüsünde")
    C.add("S4", "Ölçü", "Sayfa yüksekliği (trim)",
          abs(h_in - ed.trim_h) <= TOL_IN, f"{ed.trim_h:.4f} in",
          f"{h_in:.4f} in")

    # bütün sayfalar aynı ölçüde mi
    sizes = {(round(float(p.mediabox.width), 2),
              round(float(p.mediabox.height), 2)) for p in r.pages}
    C.add("S5", "Ölçü", "Bütün sayfalar aynı ölçüde", len(sizes) == 1,
          "1 farklı ölçü", f"{len(sizes)} farklı ölçü: {sorted(sizes)[:3]}",
          "karışık ölçü KDP'de reddedilir")

    # sayfa kutuları tutarlı mı
    inconsistent = []
    for i, p in enumerate(r.pages[:8]):
        boxes = {}
        for nm in ("mediabox", "cropbox", "trimbox", "bleedbox", "artbox"):
            try:
                b = getattr(p, nm)
                boxes[nm] = [round(float(v) / PT, 3)
                             for v in (b.left, b.bottom, b.right, b.top)]
            except Exception:
                pass
        if len({tuple(v) for v in boxes.values()}) > 1:
            inconsistent.append(i + 1)
    C.add("S6", "Yapı", "Sayfa kutuları tutarlı", not inconsistent,
          "hepsi eşit", inconsistent or "eşit",
          "farklı TrimBox ikinci bir ölçekleme doğurur")

    # fontlar — bütün sayfalar taranır
    fonts, not_emb, not_sub = set(), set(), set()
    for p in r.pages:
        res = p.get("/Resources") or {}
        for _k, f in (res.get("/Font") or {}).items():
            f = f.get_object()
            for df in (f.get("/DescendantFonts") or [f]):
                df = df.get_object() if hasattr(df, "get_object") else df
                fd = df.get("/FontDescriptor")
                if fd is None:
                    not_emb.add(str(f.get("/BaseFont")))
                    continue
                fd = fd.get_object()
                name = str(fd.get("/FontName"))
                fonts.add(name)
                if not any(k2 in fd for k2 in
                           ("/FontFile", "/FontFile2", "/FontFile3")):
                    not_emb.add(name)
                if "+" not in name:
                    not_sub.add(name)
    C.add("S7", "Font", "Tüm fontlar gömülü", not not_emb,
          "gömülü olmayan yok", sorted(not_emb) or "yok",
          "KDP gömülü olmayan fontu reddeder — reportlab varsayılanı "
          "Helvetica'dır ve gömülmez")
    C.add("S8", "Font", "Fontlar alt kümelenmiş", not not_sub,
          "hepsi alt küme", sorted(not_sub) or "hepsi alt küme",
          f"{len(fonts)} font: " + ", ".join(sorted(fonts)))
    C.add("S9", "Font", "Beklenen font sayısı", len(fonts) == 3,
          "3 (Cinzel, EBGaramond, EBGaramond-Italic)", len(fonts),
          "fazlası sızmış bir yüz demektir")

    # saydamlık / görsel
    raw = open(pdf_path, "rb").read()
    has_alpha = b"/SMask" in raw
    C.add("S10", "Yapı", "Saydamlık yok", not has_alpha, "yok",
          "var" if has_alpha else "yok",
          "düzleştirilmemiş saydamlık baskıda sürpriz yapar")

    imgs = 0
    for p in r.pages:
        xo = (p.get("/Resources") or {}).get("/XObject") or {}
        for k in xo:
            if xo[k].get_object().get("/Subtype") == "/Image":
                imgs += 1
    C.add("S11", "Görsel", "Görsel yok (saf metin bloğu)", imgs == 0,
          "0 görsel", imgs,
          "görsel eklenirse >= 300 PPI kontrolü gerekir")

    # metadata
    md = r.metadata or {}
    title = str(md.get("/Title") or "")
    author = str(md.get("/Author") or "")
    C.add("S12", "Metadata", "Başlık dolu",
          M.TITLE.lower() in title.lower(), f"…{M.TITLE}…", title or "(boş)")
    C.add("S13", "Metadata", "Yazar dolu", bool(author.strip()),
          M.AUTHOR, author or "(boş)")
    if ed.title_suffix:
        C.add("S14", "Metadata", "Sürüm eki başlıkta",
              ed.title_suffix.strip() in title, ed.title_suffix.strip(),
              title, "büyük punto ayrı bir üründür; başlıkta görünmeli")

    size_mb = os.path.getsize(pdf_path) / 1e6
    C.add("S15", "Dosya", "Boyut sınır içinde", size_mb < 650,
          "< 650 MB", f"{size_mb:.2f} MB", "KDP iç blok üst sınırı")
    return n, w_in, h_in


# =============================================================================
# MARJ TABLOSU
# =============================================================================

def margin_policy(ed, pages, C):
    ok, req, slack = ed.gutter_ok(pages)
    C.add("M1", "Marj", "İç marj (gutter) KDP tablosuna uygun", ok,
          f">= {req:.3f} in ({pages} sayfa)", f"{ed.gutter:.3f} in",
          f"pay {slack:+.3f} in — KDP tablosu sayfa sayısına bağlıdır")
    for name, val in (("dış", ed.outer), ("üst", ed.top), ("alt", ed.bottom)):
        C.add(f"M-{name}", "Marj", f"{name.capitalize()} marj asgariyi geçiyor",
              val >= E.OUTER_MIN_NO_BLEED,
              f">= {E.OUTER_MIN_NO_BLEED} in", f"{val:.3f} in",
              "taşmasız kitapta KDP asgarisi")
    # büyük puntoda erişilebilirlik eşiği
    if ed.key == "largeprint":
        C.add("M2", "Marj", "Gövde punto büyük punto eşiğinde",
              ed.body_pt >= 16, ">= 16 pt", f"{ed.body_pt:g} pt",
              "KDP zorunlu standart yayımlamaz; sektör normu 16–18 pt")
        ratio = ed.lead_pt / ed.body_pt
        C.add("M3", "Marj", "Satır aralığı >= 1.5x", ratio >= 1.5 - 1e-9,
              ">= 1.5x", f"{ratio:.2f}x",
              "büyük punto okurunda satır takibi için")


# =============================================================================
# DENEYSEL — render edip mürekkebi ölç
# =============================================================================

def _ink_bbox(arr):
    """Mürekkep sınırlarını (l, t, r, b) piksel olarak döndürür; yoksa None."""
    mask = arr < INK_THRESHOLD
    cols = np.where(mask.any(axis=0))[0]
    rows = np.where(mask.any(axis=1))[0]
    if not len(cols) or not len(rows):
        return None
    return int(cols[0]), int(rows[0]), int(cols[-1]), int(rows[-1])


def empirical(pdf_path, ed, pages, C, sample=24):
    """Sayfaları render eder, gerçek mürekkep sınırlarını ölçer."""
    # Örneklem: baştan, ortadan, sondan + rastgele olmayan düzenli aralık.
    idx = sorted({1, 2, 3, pages // 2, pages // 2 + 1, pages - 1, pages}
                 | {1 + round(i * (pages - 1) / max(sample - 1, 1))
                    for i in range(sample)})
    idx = [i for i in idx if 1 <= i <= pages]

    D = RENDER_DPI
    exp_w, exp_h = ed.trim_w * D, ed.trim_h * D

    worst_edge = (99.0, None)      # (inç, sayfa)
    worst_gutter = (99.0, None)
    bad_size, blank, folio_missing = [], [], []
    head_seen = 0

    with tempfile.TemporaryDirectory() as td:
        for pno in idx:
            base = os.path.join(td, f"p{pno}")
            subprocess.run(["pdftoppm", "-r", str(D), "-gray",
                            "-f", str(pno), "-l", str(pno), "-png",
                            pdf_path, base], check=True, capture_output=True)
            files = [f for f in os.listdir(td) if f.startswith(f"p{pno}-")
                     or f == f"p{pno}.png"]
            if not files:
                continue
            im = Image.open(os.path.join(td, files[0])).convert("L")
            a = np.asarray(im).astype(float)
            H, W = a.shape
            if abs(W - exp_w) > 3 or abs(H - exp_h) > 3:
                bad_size.append(pno)

            bb = _ink_bbox(a)
            if bb is None:
                blank.append(pno)
                continue
            l, t, r, b = bb
            left_in, right_in = l / D, (W - 1 - r) / D
            top_in, bot_in = t / D, (H - 1 - b) / D

            edge = min(left_in, right_in, top_in, bot_in)
            if edge < worst_edge[0]:
                worst_edge = (edge, pno)

            # cilt tarafı: tek sayfa (recto) solda, çift sayfa (verso) sağda
            gutter_in = left_in if pno % 2 == 1 else right_in
            if gutter_in < worst_gutter[0]:
                worst_gutter = (gutter_in, pno)

            # folyo: sayfanın alt %12'sinde mürekkep var mı
            strip = a[int(H * 0.88):, :]
            if (strip < INK_THRESHOLD).sum() > 8:
                pass
            else:
                folio_missing.append(pno)
            # üstbilgi: üst %7
            if (a[:int(H * 0.07), :] < INK_THRESHOLD).sum() > 8:
                head_seen += 1

    C.add("E1", "Render", "Render ölçüsü doğru", not bad_size,
          f"{exp_w:.0f}x{exp_h:.0f} px", bad_size or "hepsi doğru",
          f"{D} DPI'da")

    C.add("E2", "Render", "Mürekkep kesim kenarından uzak",
          worst_edge[0] >= KDP_EDGE_MIN - 0.02,
          f">= {KDP_EDGE_MIN} in", f"{worst_edge[0]:.3f} in "
          f"(sayfa {worst_edge[1]})",
          "taşmasız kitapta KDP asgarisi; folyo ve üstbilgi dahil ölçüldü")

    C.add("E3", "Render", "Cilt tarafı marjı korunuyor",
          worst_gutter[0] >= ed.gutter - 0.05,
          f">= {ed.gutter:.3f} in", f"{worst_gutter[0]:.3f} in "
          f"(sayfa {worst_gutter[1]})",
          "tek sayfa solda, çift sayfa sağda ölçülür — recto/verso "
          "şablonlarının doğru sırayla uygulandığını kanıtlar")

    C.add("E4", "Render", "Boş sayfa sayısı makul", len(blank) <= 14,
          "<= 14 örneklemde", f"{len(blank)} boş: {blank[:8]}",
          "medeniyet açılışlarını recto'ya itmek için bilinçli eklenenler",
          warn=True)

    checked = len(idx) - len(blank)
    C.add("E5", "Render", "Folyo (sayfa numarası) basılıyor",
          len(folio_missing) <= len(blank) + 12,
          "numaralı sayfalarda var",
          f"{len(folio_missing)}/{len(idx)} sayfada alt bant boş",
          "ön maddede ve açılışlarda folyo bilinçli olarak yoktur", warn=True)

    C.add("E6", "Render", "Üstbilgi basılıyor", head_seen > 0,
          "> 0 sayfa", f"{head_seen}/{checked} sayfada üst bantta mürekkep",
          "koşan başlık — açılış sayfalarında bilinçli olarak yoktur")
    return idx


# =============================================================================
# MAIN
# =============================================================================

def main():
    ap = argparse.ArgumentParser(description="İç blok doğrulama")
    E.add_argument(ap)
    ap.add_argument("--sample", type=int, default=24,
                    help="render edilip ölçülecek sayfa sayısı")
    ap.add_argument("--pdf", default=None)
    a = ap.parse_args()

    ed = E.get(a.edition)
    pdf = a.pdf or P.interior_pdf(ed)
    if not os.path.exists(pdf):
        raise SystemExit(f"PDF yok: {P.rel(pdf)}\n"
                         f"önce: python3 08_BUILD/make_pdf.py --edition {ed.key}")

    print(f"\n{'='*70}\n{ed.label.upper()} · iç blok doğrulaması")
    print(f"{P.rel(pdf)}\n{'='*70}")

    C = Checks()
    pages, w_in, h_in = structural(pdf, ed, C)
    margin_policy(ed, pages, C)
    sampled = empirical(pdf, ed, pages, C, sample=a.sample)

    out = P.validation_json(ed, "interior")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"pdf": P.rel(pdf), "edition": ed.key,
                   "binding": ed.binding, "pages": pages,
                   "trim_in": [round(w_in, 4), round(h_in, 4)],
                   "body_pt": ed.body_pt, "lead_pt": ed.lead_pt,
                   "gutter_in": ed.gutter, "outer_in": ed.outer,
                   "sampled_pages": sampled,
                   "checks": C.rows,
                   "summary": {"total": len(C.rows),
                               "pass": len(C.rows) - len(C.failed) - len(C.warned),
                               "warn": len(C.warned), "fail": len(C.failed)}},
                  f, ensure_ascii=False, indent=2)

    ic = {"pass": "✓", "warn": "!", "fail": "✗"}
    grp = None
    for r in C.rows:
        if r["group"] != grp:
            grp = r["group"]
            print(f"\n── {grp} " + "─" * (62 - len(grp)))
        print(f" {ic[r['status']]} {r['name']:44s} {r['actual']}")
        if r["status"] != "pass":
            print(f"     beklenen: {r['expected']}   ({r['note']})")
    n = len(C.rows)
    print(f"\n{'='*70}\n{n} kontrol · "
          f"{n-len(C.failed)-len(C.warned)} geçti · "
          f"{len(C.warned)} uyarı · {len(C.failed)} başarısız")
    print(f"→ {P.rel(out)}")
    return 1 if C.failed else 0


if __name__ == "__main__":
    sys.exit(main())
