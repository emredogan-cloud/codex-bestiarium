#!/usr/bin/env python3
"""
CODEX BESTIARIUM — PLAKA FORMAT DÖNÜŞTÜRÜCÜ
================================================================================
Normalize edilmiş bir plaka (`07_ASSETS/plates/plate-NNN.png`) eklendiği anda
yayın için gereken bütün formatlara dönüştürülür. Elle dönüştürme yapılmaz;
her formatın kendi kısıtı vardır ve o kısıt burada tek yerde tanımlıdır.

ÜRETİLEN FORMATLAR
    baskı   plate-NNN.tif    300 DPI · 1-bit veya 8-bit gri · LZW · gömülü DPI
            İç blok PDF'ine giren dosya. Sıkıştırma kayıpsız olmalı;
            JPEG artefaktı ince tarama çizgilerini yok eder.

    kindle  plate-NNN.png    ≤60 KB · gri · optimize
            Yol haritası Bölüm 06: 120 plaka optimize edilmezse teslim ücreti
            telifi %30 yer. Hedef EPUB ≤7 MB → plaka başına ≤60 KB.

    aplus   plate-NNN.jpg    RGB · kalite 88 · ≤2 MB
            Amazon A+ yalnızca RGB kabul eder; CMYK reddedilir.

    web     plate-NNN.webp   site ve basın kiti için

KULLANIM
    python3 08_BUILD/convert_plates.py                  # eksikleri üret
    python3 08_BUILD/convert_plates.py --force          # hepsini yeniden üret
    python3 08_BUILD/convert_plates.py --formats print,kindle
    python3 08_BUILD/convert_plates.py --check          # bütçeleri denetle
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    ASSET_DIR,
    PLATES_DIR,
    PLATE_EPUB_BUDGET_KB,
    PLATE_SPEC,
    ROOT,
    Result,
    load_spec,
)

FORMATS = {
    "print": {"dir": "plates_print", "ext": ".tif", "budget_kb": None},
    "kindle": {"dir": "plates_kindle", "ext": ".png",
               "budget_kb": PLATE_EPUB_BUDGET_KB},
    "aplus": {"dir": "plates_aplus", "ext": ".jpg", "budget_kb": 2000},
    "web": {"dir": "plates_web", "ext": ".webp", "budget_kb": 300},
}

# Kindle plakası: dosya boyutu bütçesini tutturmak için ölçek düşürülür.
KINDLE_MAX_WIDTH = 900


def _require_pil():
    try:
        from PIL import Image  # noqa: F401
    except ImportError as exc:
        raise SystemExit(
            "HATA: format dönüşümü Pillow gerektirir.\n"
            "      ./08_BUILD/bootstrap.sh çalıştırın.\n"
            f"      ({exc})"
        )


def convert_one(src: str, fmt: str, dst: str) -> int:
    """Bir plakayı bir formata çevirir; üretilen dosyanın boyutunu döner."""
    from PIL import Image

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with Image.open(src) as im:
        dpi = PLATE_SPEC["dpi"]
        if fmt == "print":
            im.convert("L").save(
                dst, "TIFF", compression="tiff_lzw", dpi=(dpi, dpi)
            )
        elif fmt == "kindle":
            g = im.convert("L")
            if g.width > KINDLE_MAX_WIDTH:
                h = round(g.height * KINDLE_MAX_WIDTH / g.width)
                g = g.resize((KINDLE_MAX_WIDTH, h), Image.LANCZOS)
            # Gravür tek renktir; palet 16 tona indirilince dosya küçülür ve
            # tarama çizgileri görünürde bozulmaz.
            g.quantize(colors=16, method=Image.MEDIANCUT).save(
                dst, "PNG", optimize=True
            )
        elif fmt == "aplus":
            im.convert("RGB").save(dst, "JPEG", quality=88, optimize=True,
                                   progressive=True, dpi=(72, 72))
        elif fmt == "web":
            im.convert("L").save(dst, "WEBP", quality=86, method=6)
        else:
            raise ValueError(fmt)
    return os.path.getsize(dst)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--formats", default="print,kindle,aplus,web")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="dönüştürme; yalnızca bütçeleri denetle")
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out",
                    default="06_REPORTS/plate-formats.json")
    args = ap.parse_args()

    wanted = [f.strip() for f in args.formats.split(",") if f.strip()]
    bad = [f for f in wanted if f not in FORMATS]
    if bad:
        print(f"HATA: bilinmeyen format: {bad}", file=sys.stderr)
        return 2

    spec = load_spec()
    plate_ids = sorted(c["plate"] for c in spec["creatures"])
    r = Result("PLAKA FORMAT DÖNÜŞÜMÜ (convert_plates)")

    if not os.path.isdir(PLATES_DIR):
        r.ok("normalize plaka klasörü yok", "illüstrasyon Faz 4'te başlar")
        return r.report(verbose=args.verbose)

    sources = {
        os.path.splitext(f)[0]: os.path.join(PLATES_DIR, f)
        for f in os.listdir(PLATES_DIR)
        if f.lower().endswith(".png")
    }
    present = [p for p in plate_ids if p in sources]

    if not present:
        r.ok("henüz normalize plaka yok",
             f"beklenen {len(plate_ids)} · illüstrasyon Faz 4'te başlar")
        code = r.report(verbose=args.verbose)
        if args.json_out:
            r.to_json(os.path.join(ROOT, args.json_out))
        return code

    if not args.check:
        _require_pil()

    made = 0
    over_budget: list[str] = []
    missing_out: list[str] = []

    for fmt in wanted:
        meta = FORMATS[fmt]
        out_dir = os.path.join(ASSET_DIR, meta["dir"])
        sizes = []
        for pid in present:
            dst = os.path.join(out_dir, pid + meta["ext"])
            if args.check:
                if not os.path.exists(dst):
                    missing_out.append(f"{fmt}/{pid}")
                    continue
            elif args.force or not os.path.exists(dst) or (
                os.path.getmtime(dst) < os.path.getmtime(sources[pid])
            ):
                convert_one(sources[pid], fmt, dst)
                made += 1
            if os.path.exists(dst):
                kb = os.path.getsize(dst) / 1024
                sizes.append(kb)
                if meta["budget_kb"] and kb > meta["budget_kb"]:
                    over_budget.append(f"{fmt}/{pid}: {kb:.0f} KB")

        if sizes:
            r.ok(
                f"format · {fmt}",
                f"{len(sizes)} dosya · ort {sum(sizes) / len(sizes):.0f} KB · "
                f"en büyük {max(sizes):.0f} KB"
                + (f" · bütçe {meta['budget_kb']} KB" if meta["budget_kb"] else ""),
            )

    r.add(not missing_out, "bütün formatlar üretilmiş",
          f"eksik: {missing_out[:12]}")
    r.add(
        not over_budget,
        "dosya boyutu bütçeleri tutuyor",
        "; ".join(over_budget[:12])
        + ("\n         Kindle bütçesi aşılırsa teslim ücreti telifin %30'unu yer."
           if over_budget else ""),
    )

    # EPUB toplam bütçesi
    kindle_dir = os.path.join(ASSET_DIR, FORMATS["kindle"]["dir"])
    if os.path.isdir(kindle_dir):
        total_mb = sum(
            os.path.getsize(os.path.join(kindle_dir, f))
            for f in os.listdir(kindle_dir)
        ) / 1e6
        projected = total_mb * len(plate_ids) / max(1, len(present))
        r.add(
            projected <= 6.0,
            "120 plakanın toplam Kindle ağırlığı ≤6 MB (EPUB bütçesi 7 MB)",
            f"şu an {total_mb:.2f} MB / {len(present)} plaka → "
            f"120 plakada ~{projected:.2f} MB",
        )

    if made:
        print(f"\n{made} dosya üretildi.")

    code = r.report(verbose=args.verbose)
    if args.json_out:
        r.to_json(os.path.join(ROOT, args.json_out))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
