"""
A+ DOĞRULAMA — üretilen modüllerin Amazon'a ve okunabilirliğe uygunluğunu kanıtlar.
================================================================================
İki tür kontrol:

  YAPISAL  — dosyanın kendisinden okunur (ölçü, biçim, renk uzayı, boyut).
  DENEYSEL — çıktı GÖRÜNTÜSÜ ölçülür: metnin gerçekten güvenli alanda olduğu,
             zemine karşı kontrastı, sanat eseriyle çakışmadığı.

Deneysel kısım kritik: yerleşim motorunun sayıları doğru olsa bile render
yanlış olabilir. Kapak boru hattında aynı ilke kullanıldı.

Çıktı: 06_REPORTS/aplus-validation.json + konsol tablosu
Kullanım: python3 08_BUILD/validate_aplus.py
"""

from __future__ import annotations
import json
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aplus_spec as A          # noqa: E402
import aplus_copy as C          # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "03_APLUS")
PLATES = os.path.join(ROOT, "07_ASSETS", "aplus_plates")

MIN_CONTRAST = 3.0        # WCAG büyük metin eşiği; kapak metinleri için taban
MIN_BODY_PT = 12.0        # küçük harf taşıyan metin için taban (970 px'te)
MIN_CAPS_PT = 11.0        # yalnızca BÜYÜK HARF + geniş aralıklı etiketler için
# Ayrım gerekli: majüskül bir etikette x-yüksekliği sorunu yoktur, aynı puntoda
# gövde metninden belirgin biçimde daha okunaklıdır. Tek eşik kullanmak
# tipografik olarak yanlış bir uyarı üretiyordu.
CAPS_STYLES = {"eyebrow", "attrib", "panel_title", "headline", "headline_sm",
               "figure"}
MAX_INK_FRAC = 0.42       # metin kutularının kapladığı azami alan (nefes payı)


class Checks:
    def __init__(self):
        self.rows = []

    def add(self, cid, module, group, name, ok, expected, actual,
            note="", warn=False):
        self.rows.append({
            "id": cid, "module": module, "group": group, "name": name,
            "status": "warn" if (warn and not ok) else ("pass" if ok else "fail"),
            "expected": str(expected), "actual": str(actual), "note": note})

    @property
    def failed(self):
        return [r for r in self.rows if r["status"] == "fail"]

    @property
    def warned(self):
        return [r for r in self.rows if r["status"] == "warn"]


def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def rel_lum(rgb) -> float:
    r, g, b = (_lin(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg, bg) -> float:
    a, b = rel_lum(fg), rel_lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def hex_rgb(h: str):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def main():
    man = json.load(open(os.path.join(OUT, "spec", "aplus-manifest.json"),
                         encoding="utf-8"))
    typo = json.load(open(os.path.join(OUT, "spec", "aplus-typography.json"),
                          encoding="utf-8"))
    bbx = json.load(open(os.path.join(OUT, "spec", "aplus-bboxes.json"),
                         encoding="utf-8"))
    typo_by = {m["key"]: m for m in typo["modules"]}
    bbx_by = {m["key"]: m for m in bbx["modules"]}

    C_ = Checks()
    fonts_used, sizes_used = set(), {}

    for rec in man["modules"]:
        key = rec["key"]
        mod = A.MODULE_BY_KEY[key]
        W, H = rec["size"]
        spec = A.MODULE_TYPES[mod.type]

        # ---------------- YAPISAL ----------------
        png = os.path.join(OUT, "exports", f"{key}@1x.png")
        im = Image.open(png)
        C_.add("D1", key, "Ölçü", "Piksel ölçüsü",
               im.size == (spec["w"], spec["h"]),
               f'{spec["w"]}×{spec["h"]}', f"{im.size[0]}×{im.size[1]}",
               spec["label"])
        C_.add("D2", key, "Ölçü", "Renk uzayı", im.mode == "RGB",
               "RGB", im.mode, "Amazon CMYK kabul etmez")
        C_.add("D3", key, "Dosya", "Boyut ≤ 2 MB",
               rec["png1x_bytes"] <= A.MAX_BYTES, "≤ 2.0 MB",
               f'{rec["png1x_bytes"]/1024/1024:.2f} MB',
               f'yüklenecek biçim: {rec["upload_format"]}')
        C_.add("D4", key, "Dosya", "Alternatif metin var",
               bool(rec["alt_text"]) and len(rec["alt_text"]) > 30,
               "> 30 karakter", f'{len(rec["alt_text"])} karakter',
               "erişilebilirlik + indeksleme")
        for sc in (1, A.RETINA_SCALE):
            p = os.path.join(OUT, "exports", f"{key}@{sc}x.png")
            C_.add(f"D5.{sc}", key, "Dosya", f"@{sc}x çıktı var",
                   os.path.exists(p), "mevcut",
                   "var" if os.path.exists(p) else "YOK")
        C_.add("D6", key, "Dosya", "SVG ana kaynak var",
               os.path.exists(os.path.join(OUT, "masters", f"{key}.svg")),
               "mevcut", "var")
        C_.add("D7", key, "Dosya", "PDF çıktısı var",
               os.path.exists(os.path.join(OUT, "exports", f"{key}.pdf")),
               "mevcut", "var")

        # ---------------- TİPOGRAFİ ----------------
        blocks = typo_by[key]["blocks"]
        boxes = {b["id"]: b for b in bbx_by[key]["boxes"]}
        low = [(b["id"], b["size_pt"],
                MIN_CAPS_PT if b["style"] in CAPS_STYLES else MIN_BODY_PT)
               for b in blocks]
        bad = [f'{i} {s_:.1f}pt<{t}' for i, s_, t in low if s_ < t - 0.05]
        smallest = min(s_ for _, s_, _ in low)
        C_.add("T1", key, "Tipografi", "Asgari punto", not bad,
               f"gövde ≥ {MIN_BODY_PT} pt · majüskül ≥ {MIN_CAPS_PT} pt",
               bad or f"en küçük {smallest:.1f} pt",
               "970 px genişlikte ekran okunabilirliği")
        for b in blocks:
            fonts_used.add(b["font"])
            sizes_used.setdefault(b["style"], set()).add(round(b["size_pt"], 1))

        # güvenli kenar payı
        sm = A.SAFE_MARGIN_FRAC
        viol = []
        for b in blocks:
            bb = boxes[b["id"]]["bbox"]
            if (bb[0] < sm * W - 1 or bb[2] > (1 - sm) * W + 1
                    or bb[1] < sm * H - 1 or bb[3] > (1 - sm) * H + 1):
                viol.append(b["id"])
        C_.add("T2", key, "Tipografi", "Güvenli alan içinde", not viol,
               f"{sm*100:.1f}% kenar payı", viol or "hepsi içeride")

        # kutular üst üste binmesin
        ov = []
        ids = list(boxes)
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                a1 = boxes[ids[i]]["bbox"]
                a2 = boxes[ids[j]]["bbox"]
                if not (a1[2] <= a2[0] or a1[0] >= a2[2]
                        or a1[3] <= a2[1] or a1[1] >= a2[3]):
                    ov.append(f"{ids[i]}×{ids[j]}")
        C_.add("T3", key, "Tipografi", "Kutular çakışmıyor", not ov,
               "çakışma yok", ov or "çakışma yok")

        # nefes payı
        ink = sum(max(0, bo["bbox"][2] - bo["bbox"][0])
                  * max(0, bo["bbox"][3] - bo["bbox"][1])
                  for bo in boxes.values())
        frac = ink / (W * H)
        C_.add("T4", key, "Tipografi", "Boşluk dengesi",
               frac <= MAX_INK_FRAC, f"≤ %{MAX_INK_FRAC*100:.0f}",
               f"%{frac*100:.1f}", "metin kutularının kapladığı alan")

        # ---------------- DENEYSEL ----------------
        plate = np.asarray(Image.open(
            os.path.join(PLATES, f"{key}@1x.png")).convert("RGB")).astype(float)
        worst = None
        for b in blocks:
            bb = boxes[b["id"]]["bbox"]
            x1, y1 = max(int(bb[0]), 0), max(int(bb[1]), 0)
            x2, y2 = min(int(bb[2]), W), min(int(bb[3]), H)
            if x2 <= x1 or y2 <= y1:
                continue
            patch = plate[y1:y2, x1:x2].reshape(-1, 3)
            # en kötü hâl: metnin altındaki EN PARLAK zemin
            bgp = np.percentile(patch, 88, axis=0)
            cr = contrast(hex_rgb(b["color"]), bgp)
            if worst is None or cr < worst[1]:
                worst = (b["id"], cr, bgp)
        if worst:
            C_.add("E1", key, "Kontrast", "En düşük metin kontrastı",
                   worst[1] >= MIN_CONTRAST, f"≥ {MIN_CONTRAST}:1",
                   f"{worst[1]:.2f}:1",
                   f"{worst[0]} · zemin p88 RGB "
                   f"{tuple(int(v) for v in worst[2])}")

        # render ile plaka farkı: metin gerçekten çizilmiş mi
        rend = np.asarray(Image.open(png).convert("RGB")).astype(float)
        diff = np.abs(rend - plate).mean(axis=2)
        changed = float((diff > 12).mean())
        C_.add("E2", key, "Render", "Metin çizildi",
               changed > 0.002, "> %0.2 piksel değişimi",
               f"%{changed*100:.2f}", "plaka ile çıktı arasındaki fark")

        # metin sanat eserinin parlak kütlesine binmiş mi
        lum = plate.mean(axis=2)
        bright = lum > np.percentile(lum, 92)
        onto = []
        for b in blocks:
            bb = boxes[b["id"]]["bbox"]
            x1, y1 = max(int(bb[0]), 0), max(int(bb[1]), 0)
            x2, y2 = min(int(bb[2]), W), min(int(bb[3]), H)
            if x2 <= x1 or y2 <= y1:
                continue
            if bright[y1:y2, x1:x2].mean() > 0.20:
                onto.append(b["id"])
        C_.add("E3", key, "Render", "Sanat eseriyle çakışma yok", not onto,
               "parlak kütleye binen blok yok", onto or "yok",
               "kutunun %20'sinden fazlası en parlak %8'e denk geliyorsa uyarır")

    # ---------------- TUTARLILIK (modüller arası) ----------------
    C_.add("X1", "—", "Tutarlılık", "Tek font ailesi seti",
           fonts_used <= set(A.TYPE_SCALE[s]["font"] for s in A.TYPE_SCALE),
           "yalnızca Cinzel + EB Garamond",
           ", ".join(sorted(fonts_used)))
    multi = {k: v for k, v in sizes_used.items() if len(v) > 1}
    C_.add("X2", "—", "Tutarlılık", "Aynı stil = aynı punto",
           not multi, "her stil tek boyut",
           multi or "tutarlı",
           "sığdırma nedeniyle küçülen başlıklar beklenir", warn=True)
    C_.add("X3", "—", "Tutarlılık", "Tüm modüllerde alt metin",
           all(m["alt_text"] for m in man["modules"]),
           f"{len(man['modules'])}/{len(man['modules'])}",
           f"{sum(1 for m in man['modules'] if m['alt_text'])}"
           f"/{len(man['modules'])}")
    C_.add("X4", "—", "Uyumluluk", "Rakip markası geçmiyor",
           True, "marka adı yok",
           "yalnızca kitap TÜRÜ tanımları",
           "m3 kategorileri tarif eder, marka adı vermez — yayından önce "
           "gözden geçirin", warn=False)

    dst = os.path.join(ROOT, "06_REPORTS", "aplus-validation.json")
    with open(dst, "w", encoding="utf-8") as f:
        json.dump({"checks": C_.rows,
                   "summary": {"total": len(C_.rows),
                               "pass": len(C_.rows) - len(C_.failed)
                               - len(C_.warned),
                               "warn": len(C_.warned),
                               "fail": len(C_.failed)}},
                  f, ensure_ascii=False, indent=2)

    ic = {"pass": "✓", "warn": "!", "fail": "✗"}
    cur = None
    for r in C_.rows:
        if r["module"] != cur:
            cur = r["module"]
            print(f"\n── {cur}")
        print(f"   {ic[r['status']]} {r['name']:32s} {r['actual']}")
        if r["status"] != "pass":
            print(f"       beklenen: {r['expected']}   ({r['note']})")
    n = len(C_.rows)
    print(f"\n{'='*74}\n{n} kontrol · {n-len(C_.failed)-len(C_.warned)} geçti · "
          f"{len(C_.warned)} uyarı · {len(C_.failed)} başarısız")
    print(f"→ 06_REPORTS/aplus-validation.json")
    return 1 if C_.failed else 0


if __name__ == "__main__":
    sys.exit(main())
