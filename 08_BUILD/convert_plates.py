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

    web     plate-NNN.webp   1400 px · 16 ton · KAYIPSIZ · ≤300 KB
            Site, basın kiti, Pinterest. Kayıplı sıkıştırma bu çizgi dilinde
            hem bütçeyi üçe katlıyor hem artefakt bırakıyor (Faz 2 ölçümü).

BÜTÇELER PLAKA GELMEDEN ÖLÇÜLÜR
    `--calibrate`, `tests/plate_fixtures.py`'nin kurgusunu dört formata
    çevirir ve gerçek baytı 112 plakaya ekstrapole eder. Belirleyici olan
    konu değil ÇİZGİ DİLİDİR; ince 45° tarama her kodlayıcı için en kötü
    durumdur. Risk 5 böylece Faz 6'da değil Faz 2'de yanıtlanır.

KULLANIM
    python3 08_BUILD/convert_plates.py                  # eksikleri üret
    python3 08_BUILD/convert_plates.py --force          # hepsini yeniden üret
    python3 08_BUILD/convert_plates.py --formats print,kindle
    python3 08_BUILD/convert_plates.py --check          # bütçeleri denetle
    python3 08_BUILD/convert_plates.py --calibrate      # kurguda bütçe ölçümü
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    ASSET_DIR,
    EPUB_BUDGET_MB,
    PLATES_DIR,
    PLATE_EPUB_BUDGET_KB,
    PLATE_SPEC,
    ROOT,
    Result,
    load_spec,
)

# EPUB toplam bütçesi 7 MB; plakalar için hedef 6 MB (metin ve fontlar için
# 1 MB pay bırakılır).
EPUB_TARGET_MB = EPUB_BUDGET_MB - 1.0

FORMATS = {
    "print": {"dir": "plates_print", "ext": ".tif", "budget_kb": None},
    "kindle": {"dir": "plates_kindle", "ext": ".png",
               "budget_kb": PLATE_EPUB_BUDGET_KB},
    "aplus": {"dir": "plates_aplus", "ext": ".jpg", "budget_kb": 2000},
    "web": {"dir": "plates_web", "ext": ".webp", "budget_kb": 300},
}

# Kindle plakası: dosya boyutu bütçesini tutturmak için ölçek düşürülür.
KINDLE_MAX_WIDTH = 900

# Web plakası: Faz 2'de ölçüldü ve KAYIPSIZA çevrildi.
#
# Ham ölçüm (1800 px, kalite 86, kayıplı): 954 KB — bütçenin üç katı.
# İnce 45° tarama, kayıplı kodlayıcı için en kötü durumdur: yüksek frekansı
# kodlamak için bit harcar ve yine de artefakt bırakır. Ölçek düşürmek
# yetmedi (1200 px kalite 80 → 348 KB, hâlâ bütçe dışı).
#
# Çözüm Kindle yolunda zaten vardı: gravür birkaç tonluk bir görüntüdür.
# 16 tona indirilip KAYIPSIZ kaydedildiğinde 1400 pikselde **159 KB** —
# bütçenin yarısı, üstelik artefaktsız. Kayıplı 1400/q80 aynı boyutta
# 474 KB ve daha kötü görünüyordu.
WEB_MAX_WIDTH = 1400
WEB_TONES = 16


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
            # İKİ TON — Faz 5 · karar D49.
            #
            # Faz 2 kalibrasyonu 16 tonu KURGU üzerinde ölçtü ve plaka
            # başına 34 KB verdi. Gerçek set geldiğinde aynı ayar
            # 227 KB üretti (112 plakada 24,8 MB, bütçe 6 MB). Sebep:
            # kurgunun düzenli tramı çok iyi sıkışır, el işi taramanın
            # yüksek frekanslı dokusu sıkışmaz. Kayıpsız PNG o dokuyu
            # olduğu gibi taşımak zorundadır.
            #
            # Ölçülen seçenekler (7 plakalık örnek, ortalama · 112'de):
            #     PNG 900px 16 ton   227 KB · 24,8 MB
            #     PNG 900px  8 ton   162 KB · 17,7 MB
            #     PNG 600px  4 ton    34 KB ·  3,7 MB   (çözünürlük gider)
            #     JPEG 900px k82     178 KB · 19,5 MB
            #     1-bit 900px         39 KB ·  4,3 MB   ✅
            #
            # İki ton hem bütçeyi karşılıyor hem ÇÖZÜNÜRLÜĞÜ KORUYOR, ve
            # gravür için doğru olan da budur: tonu gri seviyeler değil
            # TARAMANIN KENDİSİ taşır. Basılı gravür zaten iki tonludur.
            # Dither KAPALI — dither, taramanın üstüne ikinci bir desen
            # bindirir ve moiré üretir.
            g.convert("1", dither=Image.NONE).save(dst, "PNG", optimize=True)
        elif fmt == "aplus":
            im.convert("RGB").save(dst, "JPEG", quality=88, optimize=True,
                                   progressive=True, dpi=(72, 72))
        elif fmt == "web":
            # İKİ TON + KAYIPSIZ — Faz 5 · karar D49 (Kindle ile aynı gerekçe).
            #
            # D27 kayıpsızı seçti ve o karar doğruydu: kayıplı sıkıştırma bu
            # çizgi dilinde hem daha büyük hem daha kötü. Değişen ton
            # sayısıdır. 16 ton, gerçek el işi taramada 425–552 KB veriyordu
            # (bütçe 300 KB); iki tonda 75 KB'ye iniyor ve 1400 px korunuyor.
            # Tonu tarama taşır, palet değil.
            g = im.convert("L")
            if g.width > WEB_MAX_WIDTH:
                h = round(g.height * WEB_MAX_WIDTH / g.width)
                g = g.resize((WEB_MAX_WIDTH, h), Image.LANCZOS)
            g.convert("1", dither=Image.NONE).convert("L").save(
                dst, "WEBP", lossless=True, method=6
            )
        else:
            raise ValueError(fmt)
    return os.path.getsize(dst)


def calibrate(r: Result) -> dict:
    """Bütçeleri PLAKA GELMEDEN ölçer — kalibrasyon kurgusu üzerinde.

    Yol haritası Faz 2 ve Faz 4 aynı soruyu soruyor: "Kindle bütçesi 112
    plakaya ekstrapole edildiğinde ≤6 MB mı?" O soru, gerçek plaka gelmeden
    de yanıtlanabilir — çünkü belirleyici olan konu değil, ÇİZGİ DİLİDİR:
    ince 45° tarama, her kodlayıcı için en kötü durumdur.

    `tests/plate_fixtures.py`'nin kurgusu tam da o çizgi dilindedir. Dört
    format ondan üretilir, gerçek bayt sayılır ve 112'ye ekstrapole edilir.
    Risk 5 (Kindle dosya boyutu telifi yiyor) böylece Faz 2'de ölçülür,
    Faz 6'da sürprize dönüşmez.
    """
    import tempfile

    _require_pil()
    fixture = os.path.join(
        ROOT, "08_BUILD", "tests", "fixtures", "plates", "good.png"
    )
    if not os.path.exists(fixture):
        sys.path.insert(0, os.path.join(ROOT, "08_BUILD"))
        from tests import plate_fixtures  # noqa: PLC0415

        plate_fixtures.main()

    n_plates = len(load_spec()["creatures"])
    measured: dict[str, float] = {}
    with tempfile.TemporaryDirectory() as tmp:
        for fmt, meta in FORMATS.items():
            dst = os.path.join(tmp, meta["dir"], "plate-000" + meta["ext"])
            kb = convert_one(fixture, fmt, dst) / 1024
            measured[fmt] = kb
            budget = meta["budget_kb"]
            if budget:
                r.add(kb <= budget, f"bütçe · {fmt}",
                      f"kurguda {kb:.0f} KB · bütçe {budget} KB")
            else:
                r.ok(f"bütçe · {fmt}", f"kurguda {kb:.0f} KB · bütçe yok (kayıpsız)")

    epub_mb = measured["kindle"] * n_plates / 1024
    r.add(
        epub_mb <= EPUB_TARGET_MB,
        f"{n_plates} plakalık EPUB projeksiyonu ≤{EPUB_TARGET_MB} MB",
        f"{epub_mb:.2f} MB (plaka başına {measured['kindle']:.0f} KB) — "
        f"Risk 5: Kindle teslim ücreti",
    )
    return {"perPlateKb": {k: round(v, 1) for k, v in measured.items()},
            "plates": n_plates, "epubProjectionMb": round(epub_mb, 2)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--formats", default="print,kindle,aplus,web")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="dönüştürme; yalnızca bütçeleri denetle")
    ap.add_argument("--calibrate", action="store_true",
                    help="kalibrasyon kurgusu üzerinde bütçeleri ölç "
                         "(plaka gelmeden de koşar)")
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out",
                    default="06_REPORTS/plate-formats.json")
    args = ap.parse_args()

    if args.calibrate:
        r = Result("PLAKA FORMAT BÜTÇELERİ · KALİBRASYON (convert_plates)")
        # ÇIKIŞ KODU SÖZLEŞMESİ: 0 geçti · 1 bütçe aşıldı · 2 ATLANDI.
        # `_require_pil()` bir SystemExit(str) fırlatır ve o çıkış kodu 1'dir
        # — yani "Pillow yok" ile "bütçe aşıldı" aynı sinyali veriyordu ve
        # qa_all.sh bunu KIRMIZI sayıyordu. İkisi ayrıldı.
        try:
            _require_pil()
        except SystemExit as exc:
            print(exc)
            return 2
        data = calibrate(r)
        code = r.report(verbose=args.verbose)
        path = os.path.join(ROOT, "06_REPORTS", "plate-format-calibration.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({**data, "passed": len(r.passed),
                       "failed": len(r.failures)}, fh,
                      ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"rapor: 06_REPORTS/plate-format-calibration.json")
        return code

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
