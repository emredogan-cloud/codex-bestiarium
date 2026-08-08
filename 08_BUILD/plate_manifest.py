#!/usr/bin/env python3
"""
CODEX BESTIARIUM — PLAKA MANİFESTOSU VE EŞLEME KAPISI
================================================================================
Yol haritası Faz 5, dizgi görevleri; ve kurucunun Faz 5 emri § 11:

    yaratık → yaratık kimliği → plaka kimliği → ham PNG →
    normalize üretim görüntüsü → dizgideki yeri

    Her yaratık TAM OLARAK bir üretim plakasına eşlenmeli. Kopya eşleme
    yok, eksik eşleme yok, kazara takas yok.

    NEDEN AYRI BİR KAPI
    ───────────────────
    Ham PNG'ler hattın DIŞINDAN gelir ve dosya adları kurucunun
    üretecinden çıkar. `validate_spec` spec'i denetler, `plates.py`
    geometriyi ölçer; ikisi de dosya adının DOĞRU MADDEYE ait olduğunu
    denetlemez. Yanlış eşlenmiş bir plaka bütün kapılardan geçer ve
    kitapta yanlış yaratığın resmi basılır.

    Bu, projenin tek SESSİZ başarısızlık modudur: hiçbir sayı bozulmaz.

    KANONİK AD
    ──────────
    `plate-NNN.png` — üç haneli, sıfır dolgulu. spec.json'daki `plate`
    alanı bu biçimdedir ve dizgi oradan okur. Ham sette sapma varsa
    manifesto onu KAYDEDER ve normalize ederken kanonik ada çevirir;
    ham dosya DEĞİŞTİRİLMEZ (kurucu emri § 5).

KULLANIM
    python3 08_BUILD/plate_manifest.py            # manifesto üret
    python3 08_BUILD/plate_manifest.py --check    # üretmeden denetle
    python3 08_BUILD/plate_manifest.py -v
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    ASSET_DIR,
    PLATES_DIR,
    PLATE_SPEC,
    REPORT_DIR,
    ROOT,
    SOURCE_DIR,
    TARGET_CREATURES,
    Result,
    load_spec,
)

# Kurucu ham seti buraya koydu (Faz 5 emri § 4). Hattın tarihsel yolu
# `plates_raw/`; ikisi de aranır ve hangisinin kullanıldığı raporlanır.
RAW_DIRS = [
    os.path.join(ASSET_DIR, "aplus_raw"),
    os.path.join(ASSET_DIR, "plates_raw"),
]
MANIFEST_PATH = os.path.join(SOURCE_DIR, "plate_manifest.json")
REPORT_PATH = os.path.join(REPORT_DIR, "plate-manifest.json")

# Madde sayfasındaki plaka kutusunun genişliği (inç) — `entry_page.py`
# ile aynı geometriden gelir; çözünürlük şartı buradan türer.
PLATE_BOX_IN = 3.0

CANONICAL = re.compile(r"^plate-(\d{3})$")
LOOSE = re.compile(r"^plate[-_ ]?0*(\d{1,3})$")


def plate_number(stem: str) -> int | None:
    """Dosya kökünden plaka numarası. Kanonik olmayan adları da çözer."""
    m = LOOSE.match(stem.strip().lower())
    return int(m.group(1)) if m else None


def find_raw() -> tuple[str, list[str]]:
    for d in RAW_DIRS:
        if os.path.isdir(d):
            files = sorted(
                f for f in os.listdir(d)
                if f.lower().endswith((".png", ".tif", ".tiff"))
            )
            if files:
                return d, files
    return "", []


def probe(path: str) -> dict:
    """Görüntünün gerçek özellikleri. Pillow yoksa yalnızca dosya ölçüsü."""
    info = {"bytes": os.path.getsize(path)}
    with open(path, "rb") as fh:
        info["sha256"] = hashlib.sha256(fh.read()).hexdigest()
    try:
        from PIL import Image
    except ImportError:
        return info
    try:
        with Image.open(path) as im:
            im.verify()                       # bozuk dosyayı burada yakalar
        with Image.open(path) as im:
            info.update({
                "width": im.width, "height": im.height,
                "mode": im.mode, "format": im.format,
                "aspect": round(im.height / im.width, 4) if im.width else 0,
            })
    except Exception as exc:                  # noqa: BLE001
        info["error"] = f"{type(exc).__name__}: {exc}"
    return info


def build() -> dict:
    spec = load_spec()
    creatures = spec["creatures"]
    raw_dir, files = find_raw()

    # --- spec tarafı: her yaratığın beklediği plaka ---
    want: dict[int, dict] = {}
    dup_plate: list[str] = []
    bad_plate: list[str] = []
    for c in creatures:
        pid = (c.get("plate") or "").strip()
        m = CANONICAL.match(pid)
        if not m:
            bad_plate.append(f"{c['id']}={pid or '(boş)'}")
            continue
        n = int(m.group(1))
        if n in want:
            dup_plate.append(f"{pid}: {want[n]['id']} + {c['id']}")
        want[n] = {"id": c["id"], "name": c["name"], "plate": pid,
                   "number": c["number"], "class": c["class"],
                   "tradition": c["tradition"]}

    # --- ham taraf: dosya → numara ---
    seen: dict[int, list[str]] = {}
    unparsed: list[str] = []
    for f in files:
        n = plate_number(os.path.splitext(f)[0])
        if n is None:
            unparsed.append(f)
            continue
        seen.setdefault(n, []).append(f)

    rows, noncanonical, dup_file = [], [], []
    hashes: dict[str, list[str]] = {}
    for n in sorted(want):
        rec = want[n]
        got = seen.get(n, [])
        if len(got) > 1:
            dup_file.append(f"{rec['plate']}: {', '.join(got)}")
        row = dict(rec)
        if got:
            fn = sorted(got)[0]
            path = os.path.join(raw_dir, fn)
            row["rawFile"] = fn
            row["rawPath"] = os.path.relpath(path, ROOT)
            row.update(probe(path))
            if os.path.splitext(fn)[0] != rec["plate"]:
                noncanonical.append(f"{fn} → {rec['plate']}.png")
                row["renamedFrom"] = fn
            hashes.setdefault(row.get("sha256", ""), []).append(rec["plate"])
        else:
            row["rawFile"] = None
        row["normalized"] = os.path.relpath(
            os.path.join(PLATES_DIR, f"{rec['plate']}.png"), ROOT)
        rows.append(row)

    extra = sorted(seen.keys() - want.keys())
    identical = {h: p for h, p in hashes.items() if len(p) > 1 and h}

    return {
        "note": "Yaratık → plaka → ham PNG → normalize görüntü eşlemesi. "
                "Ham dosyalar DEĞİŞTİRİLMEZ; kanonik ad normalize çıktıda "
                "kullanılır.",
        "rawDir": os.path.relpath(raw_dir, ROOT) if raw_dir else "",
        "rawFiles": len(files),
        "creatures": len(creatures),
        "mapped": sum(1 for r in rows if r["rawFile"]),
        "missing": [r["plate"] for r in rows if not r["rawFile"]],
        "extraPlateNumbers": extra,
        "unparsedFiles": unparsed,
        "nonCanonicalNames": noncanonical,
        "duplicateFilesForPlate": dup_file,
        "duplicatePlateInSpec": dup_plate,
        "malformedPlateField": bad_plate,
        "identicalImages": identical,
        "entries": rows,
    }


def verify(doc: dict, r: Result) -> None:
    n = doc["creatures"]
    r.add(n == TARGET_CREATURES, f"{TARGET_CREATURES} yaratık kaydı",
          f"{n}")
    r.add(bool(doc["rawDir"]), "ham plaka dizini bulundu",
          doc["rawDir"] or "aranan: " + ", ".join(
              os.path.relpath(d, ROOT) for d in RAW_DIRS))
    r.add(not doc["malformedPlateField"], "her maddenin plaka kimliği kanonik",
          f"{doc['malformedPlateField'][:8]}")
    r.add(not doc["duplicatePlateInSpec"], "hiçbir plaka iki maddeye atanmamış",
          f"{doc['duplicatePlateInSpec'][:8]}")
    r.add(doc["mapped"] == n, f"{n} maddenin {n}'i ham dosyaya eşleşti",
          f"eşleşen {doc['mapped']} · eksik {doc['missing'][:8]}")
    r.add(not doc["duplicateFilesForPlate"],
          "bir plaka numarasına birden çok dosya düşmüyor",
          f"{doc['duplicateFilesForPlate'][:8]}")
    r.add(not doc["unparsedFiles"], "her ham dosya adı bir plaka numarası veriyor",
          f"{doc['unparsedFiles'][:8]}")
    r.add(not doc["extraPlateNumbers"], "fazladan plaka numarası yok",
          f"{doc['extraPlateNumbers'][:8]}")

    broken = [e["plate"] for e in doc["entries"] if e.get("error")]
    r.add(not broken, "her ham görüntü açılabiliyor", f"{broken[:8]}")

    # AYNI GÖRÜNTÜ İKİ MADDEDE — sessiz başarısızlığın en olası biçimi.
    r.add(not doc["identicalImages"],
          "iki madde aynı görüntüyü paylaşmıyor",
          f"{list(doc['identicalImages'].values())[:5]}")

    sized = [e for e in doc["entries"] if e.get("width")]
    if sized:
        tol = PLATE_SPEC["aspect_tol"]
        want_a = PLATE_SPEC["aspect"]
        off = [f"{e['plate']} ({e['aspect']})" for e in sized
               if abs(e["aspect"] - want_a) > tol]
        r.add(not off, f"en/boy oranı 1:{want_a} ±{tol}",
              f"{off[:8]} — ölçülen {len(sized)} plaka")
        # ÇÖZÜNÜRLÜK, YERLEŞTİĞİ BOYUTTAN ÖLÇÜLÜR — tuval hedefinden değil.
        #
        # `target_width_px` (1800) bir ÜRETİM yönergesidir: prompt kütüphanesi
        # onu görsel üretecine yazar ve iki kat pay bırakır. Baskı şartı
        # değildir. Baskı şartı KDP'nin tabanıdır: yerleştiği ölçüde ≥300 DPI.
        #
        # Madde sayfasında plaka kutusu 3,0 inç geniştir (`entry_page.py`).
        # Gelen set 1122 px → 1122/3,0 = 374 DPI, yani tabanın üstünde.
        # Ham dosyayı 1800 px olmadığı için reddetmek, gerçek kısıtı değil
        # bir üretim notunu kapı sanmak olurdu.
        dpi_min = 300.0
        box_in = PLATE_BOX_IN
        low = [
            f"{e['plate']} ({e['width']}px → {e['width'] / box_in:.0f} DPI)"
            for e in sized if e["width"] / box_in < dpi_min
        ]
        got = min(e["width"] for e in sized) / box_in
        r.add(not low,
              f"yerleştiği ölçüde ≥{dpi_min:.0f} DPI (plaka kutusu {box_in} inç)",
              f"{low[:8]}" if low else
              f"en düşük {got:.0f} DPI · üretim hedefi "
              f"{PLATE_SPEC['target_width_px']} px bir prompt yönergesidir, "
              "baskı şartı değil")
        modes = sorted({e["mode"] for e in sized})
        r.ok("renk kipi", f"{modes} · {len(sized)} plaka ölçüldü")
    else:
        r.warn("görüntü ölçümü atlandı", "pillow yok — ./08_BUILD/bootstrap.sh")

    if doc["nonCanonicalNames"]:
        r.warn("kanonik olmayan ham dosya adı",
               f"{doc['nonCanonicalNames']} — ham dosya DEĞİŞTİRİLMEZ; "
               "normalize çıktı kanonik adı kullanır")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="yazma; manifesto bayatsa çıkış 1")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    doc = build()

    # HAM PLAKA DİZİNİ YOKSA BU BİR KALİTE DÜŞÜŞÜ DEĞİLDİR.
    #
    # Görüntüler `.gitignore` § ③ gereği depoda değildir; CI koşucusunda
    # hiç bulunmazlar. Manifesto ise DEPODADIR (D38/D51 sözleşmesi) ve
    # asıl sözleşme odur: hangi maddenin hangi plakaya ait olduğu.
    # Ham dizinin yokluğunda yapılabilecek denetim manifestonun KENDİ
    # tutarlılığıdır; dosya eşleşmesi yapılamaz ve yapılamadığı söylenir.
    #
    # Bu bir gevşetme DEĞİLDİR: plakaların bulunduğu her makinede — yerel
    # ve `plates.yml` iş akışı — tam eşleşme yine koşar ve yine ısırır.
    # Ayrım, projenin baştan beri kullandığı çıkış kodu sözleşmesidir:
    #   0 geçti · 1 kalite düştü · 2 isteğe bağlı girdi yok, ATLANDI
    # Faz 5'te `release` iş akışı bu yüzden kırmızı yandı: adım "eksik
    # girdi"yi "kusur" ile aynı sinyale çeviriyordu.
    if not doc["rawDir"]:
        print("=" * 78)
        print("PLAKA MANİFESTOSU VE EŞLEME (plate_manifest)")
        print("=" * 78)
        print("\nATLANDI: ham plaka dizini yok — aranan: "
              + ", ".join(os.path.relpath(d, ROOT) for d in RAW_DIRS))
        print("         Görüntüler depoda değildir (.gitignore § ③).")
        if not os.path.exists(MANIFEST_PATH):
            print("\n[FAIL] manifesto da yok — eşleme sözleşmesi kayıp")
            return 1
        with open(MANIFEST_PATH, encoding="utf-8") as fh:
            stored = json.load(fh)
        n = len([e for e in stored.get("entries", []) if e.get("rawFile")])
        ok = (stored.get("creatures") == TARGET_CREATURES
              and n == TARGET_CREATURES
              and not stored.get("duplicatePlateInSpec")
              and not stored.get("malformedPlateField"))
        print(f"         Depodaki manifesto: {stored.get('creatures')} "
              f"yaratık · {n} eşleme")
        if not ok:
            print("\n[FAIL] depodaki manifesto kendi içinde tutarsız")
            return 1
        print("[  ok ] depodaki manifesto tutarlı — dosya eşleşmesi "
              "yapılamadı")
        return 2

    r = Result("PLAKA MANİFESTOSU VE EŞLEME (plate_manifest)")
    verify(doc, r)

    # Manifesto DEPOYA girer: eşleme bir ölçüm değil, bir SÖZLEŞMEDİR.
    # Görüntüler depoda değildir (.gitignore § ③) ama hangi görüntünün
    # hangi maddeye ait olduğu depoda durmak zorundadır.
    want_text = json.dumps(doc, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        code = r.report(verbose=args.verbose)
        if not os.path.exists(MANIFEST_PATH):
            print(f"BAYAT: {os.path.relpath(MANIFEST_PATH, ROOT)} yok")
            print("Düzeltmek için: python3 08_BUILD/plate_manifest.py")
            return 1
        with open(MANIFEST_PATH, encoding="utf-8") as fh:
            if fh.read() != want_text:
                print(f"BAYAT: {os.path.relpath(MANIFEST_PATH, ROOT)}")
                print("Düzeltmek için: python3 08_BUILD/plate_manifest.py")
                return 1
        return code

    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        fh.write(want_text)
    os.makedirs(REPORT_DIR, exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        json.dump({"title": r.title, "passed": len(r.passed),
                   "failed": len(r.failures), "warnings": len(r.warnings),
                   "checks": r.checks}, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    code = r.report(verbose=args.verbose)
    print(f"yazıldı: {os.path.relpath(MANIFEST_PATH, ROOT)}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
