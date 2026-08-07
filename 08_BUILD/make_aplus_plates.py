"""
A+ PLAKALARI — ham görselleri Amazon modül ölçüsüne getirir.
================================================================================
  1. analyze_aplus.solve_crop() ile hesaplanan pencereyi uygular
  2. hedef ölçeğe (@1x ve @2x) LANCZOS ile indirger
  3. plakayı YENİDEN analiz eder → tüm yerleşim koordinatları artık MODÜL
     UZAYINDA ve çözünürlükten bağımsız (oran cinsinden) olur

Çıktı:
  07_ASSETS/aplus_plates/<key>@1x.png   ve  <key>@2x.png
  06_REPORTS/aplus-plate-analysis.json

Kullanım: python3 08_BUILD/make_aplus_plates.py
"""

from __future__ import annotations
import json
import os
import sys

from PIL import Image, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aplus_spec as A          # noqa: E402
import analyze_aplus as AN      # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "07_ASSETS", "aplus_raw")
PLATES = os.path.join(ROOT, "07_ASSETS", "aplus_plates")


def build_plate(m: A.ModuleDef, sharpen: bool = True) -> dict:
    src = os.path.join(RAW, m.source)
    im = Image.open(src)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        flat = Image.new("RGB", im.size, (0, 0, 0))
        flat.paste(im, mask=im.split()[-1])
        im = flat
    else:
        im = im.convert("RGB")

    an = AN.analyze(src, want_panels=(m.text_side == "panels"))
    crop = AN.solve_crop(an, m.ar, m.anchor, m.crop_bias)
    box = (crop["x"], crop["y"], crop["x"] + crop["w"], crop["y"] + crop["h"])
    cut = im.crop(box)

    os.makedirs(PLATES, exist_ok=True)
    out = {}
    for scale in (1, A.RETINA_SCALE):
        w, h = m.w * scale, m.h * scale
        p = cut.resize((w, h), Image.LANCZOS)
        # Büyük bir küçültmeden sonra hafif netleştirme; hale yapmayacak kadar az.
        if sharpen and cut.size[0] > w * 1.25:
            p = p.filter(ImageFilter.UnsharpMask(radius=1.1, percent=42,
                                                 threshold=3))
        f = os.path.join(PLATES, f"{m.key}@{scale}x.png")
        p.save(f, "PNG", optimize=True)
        out[f"@{scale}x"] = {"path": os.path.relpath(f, ROOT),
                             "w": w, "h": h,
                             "bytes": os.path.getsize(f)}

    # Plakayı yeniden analiz et: koordinatlar artık modül uzayında.
    plate2x = os.path.join(PLATES, f"{m.key}@{A.RETINA_SCALE}x.png")
    pan = AN.analyze(plate2x, want_panels=False)

    PW, PH = pan["w"], pan["h"]

    def frac(r):
        return {"x": round(r["x"] / PW, 5), "y": round(r["y"] / PH, 5),
                "w": round(r["w"] / PW, 5), "h": round(r["h"] / PH, 5)}

    def src_to_frac(r):
        """Kaynak uzayındaki kutuyu kırpma penceresinden geçirip plaka oranına
        çevirir. Paneller KAYNAKTA tespit edilir: plakada altın filetolar 2×
        küçüldüğü için incelip eşiğin altında kalıyor."""
        return {"x": round((r["x"] - crop["x"]) / crop["w"], 5),
                "y": round((r["y"] - crop["y"]) / crop["h"], 5),
                "w": round(r["w"] / crop["w"], 5),
                "h": round(r["h"] / crop["h"], 5)}

    return {
        "key": m.key, "source": m.source, "module_type": m.type,
        "target": [m.w, m.h], "files": out,
        "source_size": [an["w"], an["h"]],
        "crop": crop,
        "plate_stats": pan["stats"],
        "subject_frac": frac(pan["subject_box"]) if pan["subject_box"] else None,
        "safe_rects_frac": [frac(r) for r in pan["safe_rects"]],
        "panels_frac": [src_to_frac(p) for p in (an.get("panels") or [])],
        "zone_saliency": pan["zone_saliency"],
    }


def main():
    recs = []
    print("=" * 96)
    print("A+ PLAKALARI")
    print("=" * 96)
    for m in A.MODULES:
        if not os.path.exists(os.path.join(RAW, m.source)):
            print(f"!! kaynak yok: {m.source}")
            continue
        r = build_plate(m)
        recs.append(r)
        f1 = r["files"]["@1x"]
        f2 = r["files"]["@2x"]
        lim = "✓" if f1["bytes"] <= A.MAX_BYTES else "✗ 2MB AŞIMI"
        print(f"\n── {m.key}")
        print(f"   {r['source_size'][0]}×{r['source_size'][1]} "
              f"→ kırp {r['crop']['w']}×{r['crop']['h']} "
              f"@({r['crop']['x']},{r['crop']['y']}) "
              f"→ {f1['w']}×{f1['h']}")
        print(f"   @1x {f1['bytes']/1024:7.0f} KB {lim}   "
              f"@2x {f2['bytes']/1024:7.0f} KB")
        if r["panels_frac"]:
            for i, p in enumerate(r["panels_frac"], 1):
                print(f"   panel {i}: x{p['x']:.3f} y{p['y']:.3f} "
                      f"{p['w']:.3f}×{p['h']:.3f}")
        for i, s in enumerate(r["safe_rects_frac"][:3], 1):
            print(f"   sessiz {i}: x{s['x']:.3f} y{s['y']:.3f} "
                  f"{s['w']:.3f}×{s['h']:.3f}")

    dst = os.path.join(ROOT, "06_REPORTS", "aplus-plate-analysis.json")
    with open(dst, "w", encoding="utf-8") as f:
        json.dump({"modules": recs}, f, ensure_ascii=False, indent=2)
    print(f"\n→ 07_ASSETS/aplus_plates/  ({len(recs)*2} dosya)")
    print(f"→ 06_REPORTS/aplus-plate-analysis.json")


if __name__ == "__main__":
    main()
