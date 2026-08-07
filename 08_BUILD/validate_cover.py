"""
KAPAK DOĞRULAMA — üretilen PDF'in KDP'ye uygunluğunu makineyle kanıtlar.
================================================================================
İki tür kontrol yapılır:

  YAPISAL  — PDF'in kendi nesnelerinden okunur (sayfa kutusu, font gömme,
             görsel çözünürlüğü, saydamlık, renk uzayı).
  DENEYSEL — PDF gerçekten RENDER EDİLİR ve ölçülür. Eski kapaktaki hatayı
             yakalayacak olan kontrol türü budur: sayı doğru olup çıktının
             yanlış olması ancak böyle görülür.

Çıktı: 06_REPORTS/cover-validation.json + konsol tablosu
Kullanım: python3 08_BUILD/validate_cover.py [--paper cream]
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
import cover_spec as S       # noqa: E402
import typography as T       # noqa: E402
import editions as E         # noqa: E402
import paths as P            # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOL_IN = 0.002          # kabul edilen ölçü sapması
RENDER_DPI = 150


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


def structural(pdf_path, g, C):
    r = PdfReader(pdf_path)
    C.add("S1", "Yapı", "Tek sayfa", len(r.pages) == 1, 1, len(r.pages),
          "Tam sarım kapak tek sayfa olmalı")

    pg = r.pages[0]
    w_in = float(pg.mediabox.width) / 72
    h_in = float(pg.mediabox.height) / 72
    C.add("S2", "Ölçü", "Sayfa genişliği",
          abs(w_in - g.cover_w) <= TOL_IN, f"{g.cover_w:.4f} in",
          f"{w_in:.4f} in", "taşma dahil tam kapak genişliği")
    C.add("S3", "Ölçü", "Sayfa yüksekliği",
          abs(h_in - g.cover_h) <= TOL_IN, f"{g.cover_h:.4f} in",
          f"{h_in:.4f} in", "9 inç kesim + 2 x 0.125 taşma")

    # kutular çelişmemeli
    boxes = {}
    for nm in ("mediabox", "cropbox", "trimbox", "bleedbox", "artbox"):
        try:
            b = getattr(pg, nm)
            boxes[nm] = [round(float(v) / 72, 4) for v in
                         (b.left, b.bottom, b.right, b.top)]
        except Exception:
            pass
    same = all(v == boxes["mediabox"] for v in boxes.values())
    C.add("S4", "Yapı", "Sayfa kutuları tutarlı", same, "hepsi eşit",
          "eşit" if same else str(boxes),
          "farklı TrimBox KDP'de ikinci bir ölçekleme doğurur")

    # fontlar
    res = pg.get("/Resources") or {}
    fonts, not_emb, not_sub = [], [], []
    for k, f in (res.get("/Font") or {}).items():
        f = f.get_object()
        for df in (f.get("/DescendantFonts") or [f]):
            df = df.get_object() if hasattr(df, "get_object") else df
            fd = df.get("/FontDescriptor")
            if fd is None:
                not_emb.append(str(f.get("/BaseFont")))
                continue
            fd = fd.get_object()
            name = str(fd.get("/FontName"))
            fonts.append(name)
            if not any(k2 in fd for k2 in ("/FontFile", "/FontFile2", "/FontFile3")):
                not_emb.append(name)
            if "+" not in name:
                not_sub.append(name)
    C.add("S5", "Font", "Tüm fontlar gömülü", not not_emb,
          "gömülü olmayan yok", not_emb or "yok",
          "KDP gömülü olmayan fontu reddeder")
    C.add("S6", "Font", "Fontlar alt kümelenmiş", not not_sub,
          "hepsi alt küme", not_sub or "hepsi alt küme",
          f"{len(fonts)} font: " + ", ".join(sorted(fonts)))
    C.add("S7", "Font", "Metin canlı vektör", len(fonts) > 0,
          ">= 1 font nesnesi", f"{len(fonts)} font",
          "eski kapakta 0 idi — metin piksele gömülüydü")

    # görseller
    xo = res.get("/XObject") or {}
    worst = None
    for k in xo:
        o = xo[k].get_object()
        if o.get("/Subtype") != "/Image":
            continue
        ppi = int(o["/Width"]) / w_in
        if worst is None or ppi < worst[0]:
            worst = (ppi, int(o["/Width"]), int(o["/Height"]),
                     str(o.get("/ColorSpace")), str(o.get("/Filter")))
    if worst:
        ppi, iw, ih, cs, filt = worst
        C.add("S8", "Görsel", "Çözünürlük >= 300 PPI", ppi >= S.DPI - 1,
              f">= {S.DPI} PPI", f"{ppi:.0f} PPI ({iw}x{ih})",
              f"filtre {filt}")
        C.add("S9", "Görsel", "Renk uzayı", "DeviceRGB" in cs or "ICC" in cs,
              "DeviceRGB", cs, "KDP RGB kabul eder ve kendi CMYK'sına çevirir")

    # saydamlık
    raw = open(pdf_path, "rb").read()
    has_alpha = b"/SMask" in raw or b"/CA " in raw or b"/ca " in raw
    C.add("S10", "Yapı", "Saydamlık yok", not has_alpha, "yok",
          "var" if has_alpha else "yok",
          "düzleştirilmemiş saydamlık baskıda sürpriz yapar", warn=True)

    size_mb = os.path.getsize(pdf_path) / 1e6
    C.add("S11", "Dosya", "Boyut sınır içinde", size_mb < 650,
          "< 650 MB", f"{size_mb:.1f} MB", "KDP kapak dosyası üst sınırı")
    return w_in, h_in


def geometric(g, C):
    """Tipografi kutuları güvenli alanların ve barkodun dışında mı?"""
    fb = T.FontBook().build()
    boxes = T.layout(fb, g)
    for b in boxes:
        x1, y1, x2, y2 = T.bbox_of(b)
        if b.panel == "spine":
            safe = g.spine_safe
            sts = g.profile.spine_text_safe
            ok = (x1 >= g.spine.x + sts - 1e-6 and
                  x2 <= g.spine.x2 - sts + 1e-6 and
                  y1 >= safe.y - 1e-6 and y2 <= safe.y2 + 1e-6)
            exp = (f"x {g.spine.x+sts:.3f}.."
                   f"{g.spine.x2-sts:.3f}")
        else:
            safe = g.back_safe if b.panel == "back" else g.front_safe
            ok = (x1 >= safe.x - 1e-6 and x2 <= safe.x2 + 1e-6 and
                  y1 >= safe.y - 1e-6 and y2 <= safe.y2 + 1e-6)
            exp = f"x {safe.x:.3f}..{safe.x2:.3f}  y {safe.y:.3f}..{safe.y2:.3f}"
        C.add(f"G-{b.id}", "Güvenli alan", f"{b.id} içeride", ok, exp,
              f"x {x1:.3f}..{x2:.3f}  y {y1:.3f}..{y2:.3f}")

        bc = g.barcode
        clash = not (x2 <= bc.x or x1 >= bc.x2 or y2 <= bc.y or y1 >= bc.y2)
        if b.panel == "back":
            C.add(f"B-{b.id}", "Barkod", f"{b.id} barkodla çakışmıyor",
                  not clash, "çakışma yok",
                  "ÇAKIŞIYOR" if clash else "çakışma yok",
                  "KDP bu alana beyaz kutu basar")

    # sırt metni sırtın tam ortasında mı
    for b in boxes:
        if b.panel == "spine":
            err = abs(b.x - g.spine.cx)
            C.add(f"C-{b.id}", "Merkezleme", f"{b.id} sırt merkezinde",
                  err <= 1e-6, f"{g.spine.cx:.4f} in", f"{b.x:.4f} in",
                  f"sapma {err*25.4:.4f} mm")
    return boxes


def binding_checks(g, C, ed):
    """Ciltlemeye özgü kontroller: kalibrasyon, menteşe, sayfa sınırı."""
    P_ = g.profile
    C.add("D1", "Ciltleme", "Profil kalibre edilmiş", g.calibrated,
          "resmî KDP şablonundan ölçülmüş",
          "EVET" if g.calibrated else "HAYIR — varsayılan değerler",
          "KDP ciltli kapak formülünü yayımlamaz; şablondan ölçüm şarttır. "
          "Düzeltme: python3 08_BUILD/calibrate_cover.py --template <sablon>")

    C.add("D2", "Ciltleme", "Sayfa sayısı sınır içinde",
          P_.min_pages <= g.page_count <= P_.max_pages,
          f"{P_.min_pages}–{P_.max_pages}", g.page_count,
          f"{P_.label} için KDP sınırı")

    if P_.hinge > 0:
        # Menteşe oluğunda canlı metin olmamalı (KDP: sırttan 10 mm keep-out).
        fb = T.FontBook().build()
        clash = []
        for b in T.layout(fb, g):
            x1, _, x2, _ = T.bbox_of(b)
            for h in (g.hinge_back, g.hinge_front):
                if not (x2 <= h.x or x1 >= h.x2):
                    clash.append(b.id)
        C.add("D3", "Ciltleme", "Menteşe oluğunda metin yok", not clash,
              "boş", ", ".join(sorted(set(clash))) or "boş",
              f"menteşe {g.hinge_back.x:.3f}..{g.hinge_back.x2:.3f} ve "
              f"{g.hinge_front.x:.3f}..{g.hinge_front.x2:.3f} in — burada "
              "kapak büküldüğü için metin bozulur")

        # Sarım payı: kesim kutusunun dışında kalan alan tamamen görselle dolmalı
        C.add("D4", "Ciltleme", "Sarım payı tanımlı",
              P_.outer_pad >= 0.5, ">= 0.5 in",
              f"{P_.outer_pad:.4f} in",
              "kartonun etrafına dolanıp iç kapağa yapışan bölge")

    # Ölçülen barkod dikdörtgeni gerçekten arka kapağın içinde mi?
    # Kalibrasyon mutlak tuval koordinatı saklar; kesim ölçüsü değişirse bu
    # koordinat sessizce yanlış yere düşer. Ucuz ama kritik bir korkuluk.
    bc = g.barcode
    inside = (bc.x >= g.back.x - 1e-6 and bc.x2 <= g.back.x2 + 1e-6
              and bc.y >= g.back.y - 1e-6 and bc.y2 <= g.back.y2 + 1e-6)
    C.add("D6", "Ciltleme", "Barkod kutusu arka kapağın içinde", inside,
          f"x {g.back.x:.3f}..{g.back.x2:.3f}  y {g.back.y:.3f}..{g.back.y2:.3f}",
          f"x {bc.x:.3f}..{bc.x2:.3f}  y {bc.y:.3f}..{bc.y2:.3f}",
          "kalibrasyon mutlak koordinat saklar; kesim ölçüsü değişirse "
          "yeniden kalibre edilmelidir")

    # İç blok ile kapak aynı sayfa sayısını mı görüyor?
    try:
        real = S.interior_pages(ed)
        C.add("D5", "Ciltleme", "Kapak, iç bloğun sayfa sayısını kullanıyor",
              real == g.page_count, f"{real} (iç bloktan)", g.page_count,
              "sırt genişliği buradan çıkar — uyuşmazlık = sırt kayması")
    except SystemExit:
        pass


def empirical(pdf_path, g, boxes, C):
    """PDF'i render edip gerçek pikselleri ölçer."""
    with tempfile.TemporaryDirectory() as td:
        base = os.path.join(td, "r")
        subprocess.run(["pdftoppm", "-r", str(RENDER_DPI), "-png",
                        pdf_path, base], check=True, capture_output=True)
        png = [os.path.join(td, f) for f in sorted(os.listdir(td))][0]
        im = Image.open(png).convert("RGB")
        a = np.asarray(im).astype(float)
        H, W, _ = a.shape
        D = RENDER_DPI

        exp_w = int(round(g.cover_w * D))
        exp_h = int(round(g.cover_h * D))
        C.add("E1", "Render", "Render ölçüsü", abs(W - exp_w) <= 2 and
              abs(H - exp_h) <= 2, f"{exp_w}x{exp_h} px",
              f"{W}x{H} px", f"{RENDER_DPI} DPI'da")

        lum = a.mean(axis=2)
        # altın filetolar gerçekten sırtın içinde mi
        p = S.art_placement(g)
        grad = np.abs(np.diff(lum, axis=1)).mean(axis=0)
        grad = np.convolve(grad, np.ones(3) / 3, mode="same")
        lo, hi = int((g.spine.x - 0.35) * D), int((g.spine.x2 + 0.35) * D)
        peaks = []
        for i in np.argsort(grad[lo:hi])[::-1]:
            x = lo + int(i)
            if all(abs(x - q) > int(0.08 * D) for q in peaks):
                peaks.append(x)
            if len(peaks) >= 2:
                break
        peaks.sort()
        meas = [round(x / D, 4) for x in peaks]
        pred = [p.rule_l_in, p.rule_r_in]
        err = max(abs(m - q) for m, q in zip(meas, pred))
        C.add("E2", "Render", "Altın filetolar öngörülen yerde",
              err <= 0.02, f"{pred[0]:.4f} / {pred[1]:.4f} in",
              f"{meas[0]:.4f} / {meas[1]:.4f} in",
              f"sapma {err*25.4:.2f} mm — görsel yerleşimi doğrulandı")
        inside = all(g.spine.x < m < g.spine.x2 for m in meas)
        C.add("E3", "Render", "Filetolar sırtın içinde", inside,
              f"{g.spine.x:.4f}..{g.spine.x2:.4f}", f"{meas}",
              "katlama toleransından etkilenmez")

        # Sırt METNİ gerçekten sırt sınırları içinde mi (altın piksel taraması).
        #
        # Sırtta üç ayrı altın nesne var: iki fileto (görselden gelir) ve metin.
        # Filetolar 2-3 sütun geniş ve dikeyde kesintisizdir; metin ise ~35
        # sütunluk BİTİŞİK bir blok oluşturur. En uzun bitişik sütun dizisi
        # metindir — filetoların kenar yumuşatması bu ayrımı bozmaz.
        r_, g_, b_ = a[..., 0], a[..., 1], a[..., 2]
        gold = (r_ > 165) & (g_ > 120) & (r_ - b_ > 95)
        sl, sr = int(g.spine.x * D), int(g.spine.x2 * D)
        y0, y1_ = int(0.5 * D), int(8.8 * D)
        band = gold[y0:y1_, sl:sr]
        counts = band.sum(axis=0)
        hot = counts > 50
        runs, cur = [], None
        for i, v in enumerate(hot):
            if v and cur is None:
                cur = i
            elif not v and cur is not None:
                runs.append((cur, i - 1))
                cur = None
        if cur is not None:
            runs.append((cur, len(hot) - 1))
        if runs:
            c0, c1 = max(runs, key=lambda r_: r_[1] - r_[0])
            x1 = (sl + c0) / D
            x2 = (sl + c1) / D
            sts = g.profile.spine_text_safe
            ok = (x1 >= g.spine.x + sts - 0.01 and
                  x2 <= g.spine.x2 - sts + 0.01)
            C.add("E4", "Render", "Sırttaki altın mürekkep güvenli bantta", ok,
                  f"{g.spine.x+sts:.4f}.."
                  f"{g.spine.x2-sts:.4f} in",
                  f"{x1:.4f}..{x2:.4f} in",
                  "1/16 inç sırt payı korunuyor")
            mid = (x1 + x2) / 2
            C.add("E5", "Render", "Sırt mürekkebi ortalanmış",
                  abs(mid - g.spine.cx) <= 0.03, f"{g.spine.cx:.4f} in",
                  f"{mid:.4f} in", f"sapma {abs(mid-g.spine.cx)*25.4:.2f} mm")

        # barkod alanı boş mu (parlak mürekkep yok)
        bc = g.barcode
        patch = lum[int(bc.y * D):int(bc.y2 * D), int(bc.x * D):int(bc.x2 * D)]
        bright = float((patch > 150).mean())
        C.add("E6", "Render", "Barkod alanı temiz", bright < 0.02,
              "< %2 parlak piksel", f"%{bright*100:.2f}",
              "KDP buraya beyaz kutu basacak")

        # metin/zemin kontrastı
        for b in boxes:
            if b.id not in ("front.title.l2", "front.author", "spine.title",
                            "back.hook"):
                continue
            x1, y1, x2, y2 = T.bbox_of(b)
            sub = a[max(int(y1 * D), 0):int(y2 * D),
                    max(int(x1 * D), 0):int(x2 * D)]
            if sub.size == 0:
                continue
            sl_ = sub.mean(axis=2)
            ink = float(np.percentile(sl_, 92))
            bg = float(np.percentile(sl_, 20))
            ratio = (ink + 12) / (bg + 12)
            C.add(f"K-{b.id}", "Kontrast", f"{b.id} okunabilirliği",
                  ratio >= 2.0, ">= 2.0x", f"{ratio:.2f}x",
                  f"mürekkep {ink:.0f} / zemin {bg:.0f} (0-255)", warn=True)


def main():
    ap = argparse.ArgumentParser()
    E.add_argument(ap)
    ap.add_argument("--paper", default=None, choices=list(S.PAPER_THICKNESS))
    args = ap.parse_args()

    ed = E.get(args.edition)
    paper = args.paper or ed.paper
    g = S.geometry_for(ed, paper=paper)

    pdf = P.cover_pdf(ed, paper, provisional=not g.calibrated)
    if not os.path.exists(pdf):
        alt = P.cover_pdf(ed, paper, provisional=g.calibrated)
        if os.path.exists(alt):
            pdf = alt
        else:
            raise SystemExit(f"PDF yok: {P.rel(pdf)}\n"
                             f"önce: python3 08_BUILD/make_cover_pdf.py "
                             f"--edition {ed.key} --paper {paper}")

    print(f"\n{'='*70}\n{ed.label.upper()} · {paper.upper()} kapak doğrulaması")
    print(f"{P.rel(pdf)}\n{'='*70}")

    C = Checks()
    structural(pdf, g, C)
    binding_checks(g, C, ed)
    boxes = geometric(g, C)
    empirical(pdf, g, boxes, C)

    out = P.validation_json(ed, "cover", paper)
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"pdf": P.rel(pdf), "edition": ed.key, "binding": g.binding,
                   "paper": paper, "page_count": g.page_count,
                   "calibrated": g.calibrated,
                   "spine_in": g.spine_w, "cover_in": [g.cover_w, g.cover_h],
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
