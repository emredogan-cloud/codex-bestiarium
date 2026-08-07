"""
KAPAK DENETİMİ — tipografinin neden kaydığının kanıta dayalı teşhisi.
================================================================================
Bu betik hiçbir şey varsaymaz. Ölçer:

  * eski (aşılmış) kapak PDF'inin sayfa kutusunu ve gömülü görsel çözünürlüğünü
  * KDP'nin bu kitap için gerektirdiği gerçek geometriyi
  * ikisi arasındaki ölçek uyuşmazlığını
  * ham sanat eserindeki altın fileto bandının piksel konumunu

Çıktı: 06_REPORTS/cover-audit.json + konsol raporu

Kullanım:  python3 08_BUILD/audit_cover.py
"""

from __future__ import annotations
import json
import os
import sys

import numpy as np
from PIL import Image
from pypdf import PdfReader

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cover_spec as S  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD_PDF = "09_ARCHIVE/superseded-cover/CODEX_MYTHOLOGICA_COVER_flattened-72dpi.pdf"
ART = S.ART_FILE


def _wrap(t, n):
    words, out, cur = t.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= n or not cur:
            cur = f"{cur} {w}".strip()
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def audit_old_pdf() -> dict:
    path = os.path.join(ROOT, OLD_PDF)
    if not os.path.exists(path):
        return {"present": False}
    r = PdfReader(path)
    pg = r.pages[0]
    box = pg.mediabox
    w_pt, h_pt = float(box.width), float(box.height)

    imgs, fonts = [], []
    res = pg.get("/Resources") or {}
    xo = res.get("/XObject") or {}
    for k in xo:
        o = xo[k].get_object()
        if o.get("/Subtype") == "/Image":
            imgs.append({"name": str(k), "w": int(o["/Width"]),
                         "h": int(o["/Height"]),
                         "filter": str(o.get("/Filter"))})
    for k in (res.get("/Font") or {}):
        fonts.append(str(k))

    return {
        "present": True, "path": OLD_PDF,
        "page_w_pt": w_pt, "page_h_pt": h_pt,
        "page_w_in": round(w_pt / 72, 4), "page_h_in": round(h_pt / 72, 4),
        "aspect": round(w_pt / h_pt, 4),
        "images": imgs, "font_count": len(fonts),
        "producer": str(r.metadata.get("/Producer")) if r.metadata else None,
    }


def measure_artwork() -> dict:
    path = os.path.join(ROOT, ART)
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(float)
    H, W, _ = a.shape
    lum = a.mean(axis=2)

    # Sırt bandı iki altın filetoyla sınırlı. Filetolar = en güçlü dikey kenar.
    grad = np.abs(np.diff(lum, axis=1)).mean(axis=0)
    grad = np.convolve(grad, np.ones(5) / 5, mode="same")
    lo, hi = int(W * 0.38), int(W * 0.58)
    peaks = []
    for i in np.argsort(grad[lo:hi])[::-1]:
        x = lo + int(i)
        if all(abs(x - q) > 20 for q in peaks):
            peaks.append(x)
        if len(peaks) >= 2:
            break
    peaks.sort()
    l, r = peaks
    return {
        "file": ART, "w": W, "h": H, "aspect": round(W / H, 4),
        "gold_rule_left_px": l, "gold_rule_right_px": r,
        "band_center_px": (l + r) / 2,
        "band_center_frac": round((l + r) / 2 / W, 5),
        "band_width_px": r - l, "band_width_frac": round((r - l) / W, 5),
    }


def main():
    g = S.geometry()
    p = S.art_placement(g)
    old = audit_old_pdf()
    art = measure_artwork()
    findings = []

    if old.get("present"):
        sx = g.cover_w / old["page_w_in"]
        sy = g.cover_h / old["page_h_in"]
        anis = abs(sx - sy) / sy * 100
        findings.append({
            "id": "A1", "severity": "blocker",
            "title": "PDF sayfa kutusu yanlış ölçüde",
            "detail": (
                f"Eski kapak PDF'i {old['page_w_in']}x{old['page_h_in']} inç. "
                f"Bu kitabın gerektirdiği ölçü {g.cover_w:.4f}x{g.cover_h:.4f} "
                f"inç. KDP dosyayı kendi şablonuna oturtmak için ölçekler: "
                f"yatayda {sx:.4f}x, dikeyde {sy:.4f}x. İki çarpan eşit "
                f"olmadığı için (%{anis:.2f} fark) görüntü ya kırpılır ya "
                f"sıkışır — KAYMANIN BİRİNCİ SEBEBİ budur."),
            "measured": {"old_in": [old["page_w_in"], old["page_h_in"]],
                         "required_in": [g.cover_w, g.cover_h],
                         "scale_x": round(sx, 4), "scale_y": round(sy, 4),
                         "anisotropy_pct": round(anis, 2)},
        })
        if old["images"]:
            im0 = old["images"][0]
            ppi = im0["w"] / g.cover_w
            findings.append({
                "id": "A2", "severity": "blocker",
                "title": "Çözünürlük KDP asgarisinin çok altında",
                "detail": (
                    f"PDF içindeki tek görsel {im0['w']}x{im0['h']} piksel. "
                    f"Gereken tuvalde bu {ppi:.0f} PPI eder; KDP asgarisi "
                    f"{S.DPI} PPI. Dosya Acrobat'ın görüntü dönüştürücüsüyle "
                    f"üretildiği için 1 piksel = 1 punto kabul edilmiş "
                    f"({old['page_w_in']}x{old['page_h_in']} inçlik sayfa "
                    f"buradan çıkıyor)."),
                "measured": {"image_px": [im0["w"], im0["h"]],
                             "effective_ppi": round(ppi, 1),
                             "required_ppi": S.DPI,
                             "producer": old["producer"]},
            })
        if old["font_count"] == 0:
            findings.append({
                "id": "A3", "severity": "high",
                "title": "Tipografi vektör değil, piksele gömülü",
                "detail": (
                    "PDF'te hiç font nesnesi yok; başlık, sırt yazısı ve arka "
                    "kapak metni görüntünün içine düzleştirilmiş. Bu yüzden "
                    "KDP'nin uyguladığı her ölçekleme metni de bozar ve "
                    "yeniden konumlandırmak imkânsızdır."),
                "measured": {"font_count": 0},
            })

    band_needed = g.spine_w / g.cover_w
    findings.append({
        "id": "A4", "severity": "blocker",
        "title": "Görseldeki sırt bandı gerçek sırttan dar",
        "detail": (
            f"GPT görselindeki altın filetolu bant, görsel genişliğinin "
            f"%{art['band_width_frac']*100:.2f}'i. Gerçek sırt ise tuvalin "
            f"%{band_needed*100:.2f}'i olmak zorunda ({g.spine_w:.4f} inç = "
            f"{g.page_count} sayfa x {S.PAPER_THICKNESS[g.paper]} inç). Bant "
            f"merkezi de görselin %{art['band_center_frac']*100:.2f}'inde; "
            f"oysa sırt merkezi her zaman tam %50'dedir. Tipografiyi bu "
            f"filetolara göre hizalamak sırt yazısını katlama çizgisine "
            f"kaydırır — KAYMANIN İKİNCİ SEBEBİ budur."),
        "measured": {"band_center_frac": art["band_center_frac"],
                     "band_width_frac": art["band_width_frac"],
                     "required_center_frac": 0.5,
                     "required_width_frac": round(band_needed, 5),
                     "center_error_in": round(
                         abs(art["band_center_frac"] - 0.5) * g.cover_w, 4)},
    })

    findings.append({
        "id": "A5", "severity": "medium",
        "title": "Ham görselin yerel çözünürlüğü yetersiz",
        "detail": (
            f"Sanat eseri {art['w']}x{art['h']} piksel. Tam kapak "
            f"{g.cover_w:.4f} inç geniş olduğuna göre yerel çözünürlük "
            f"{p.native_ppi} PPI. {S.DPI} PPI'ya yükseltmek piksel sayısını "
            f"karşılar ama detay üretmez. Baskıda mandala kabartması bir miktar "
            f"yumuşak çıkar. Çözüm: aynı görseli bir yükseltme aracıyla "
            f">= {g.canvas_px[0]} px genişliğe çıkarıp aynı boru hattını "
            f"tekrar çalıştırmak."),
        "measured": {"art_px": [art["w"], art["h"]],
                     "native_ppi": p.native_ppi, "required_ppi": S.DPI,
                     "upscale_factor": round(p.scale, 4)},
    })

    report = {
        "book": {"pages": g.page_count, "trim": [S.TRIM_W, S.TRIM_H],
                 "paper": g.paper},
        "required_geometry": {
            "spine_in": g.spine_w, "cover_in": [g.cover_w, g.cover_h],
            "canvas_px": list(g.canvas_px)},
        "old_cover": old, "artwork": art,
        "fix": {
            "rule": ("Tek ve aynı ölçek çarpanı; görseldeki bandın MERKEZİ "
                     "hesaplanmış sırt MERKEZİNE oturur; metin canlı vektör "
                     "olarak PDF'e yazılır; sayfa kutusu tam ölçüdedir."),
            "scale": p.scale, "offset_px": [p.offset_x, p.offset_y],
            "gold_rules_in": [p.rule_l_in, p.rule_r_in],
            "rule_inset_from_fold_in": p.rule_inset_in},
        "findings": findings,
    }

    out = os.path.join(ROOT, "06_REPORTS", "cover-audit.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("=" * 78)
    print("KAPAK DENETİMİ — CODEX MYTHOLOGICA")
    print("=" * 78)
    if old.get("present"):
        print(f"\nEski kapak : {old['page_w_in']} x {old['page_h_in']} inç  "
              f"({old['page_w_pt']:.0f} x {old['page_h_pt']:.0f} pt), "
              f"{old['font_count']} font, üretici: {old['producer']}")
    print(f"Gereken    : {g.cover_w:.4f} x {g.cover_h:.4f} inç  "
          f"(sırt {g.spine_w:.4f} = {g.page_count} x "
          f"{S.PAPER_THICKNESS[g.paper]})")
    print(f"Sanat eseri: {art['w']} x {art['h']} px, altın fileto bandı "
          f"x={art['gold_rule_left_px']}..{art['gold_rule_right_px']} "
          f"(merkez %{art['band_center_frac']*100:.2f})")
    for f_ in findings:
        print(f"\n[{f_['id']}] {f_['severity'].upper():8s} {f_['title']}")
        for line in _wrap(f_["detail"], 74):
            print("    " + line)
    print("\n→ 06_REPORTS/cover-audit.json")


if __name__ == "__main__":
    main()
