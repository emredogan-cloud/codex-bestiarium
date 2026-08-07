#!/usr/bin/env python3
"""
CODEX BESTIARIUM — PLAKA NORMALİZASYONU VE TUTARLILIK ÖLÇÜMÜ
================================================================================
Yol haritası Bölüm 07.3: "projenin en büyük riski".

    120 plaka tek bir çizgi dilinde durmazsa kitap 'derleme' gibi görünür ve
    premium konumlanma çöker. Bu, projenin tek gerçek başarısızlık modudur ve
    ÖLÇÜLEREK yönetilmelidir — göz kararıyla değil.

Bu betik o ölçümü yapar. Beş parametre, her biri kendi tolerans bandında:

    ① en-boy oranı        1:1,25 dikey            ±0,02
    ② çizgi kalınlığı     1,4 pt (300 DPI ~5,8 px) ±%15
    ③ tarama açısı        45° birincil / 135°      ±5°
    ④ tarama sıklığı      cm başına 22–28 çizgi    bant
    ⑤ mürekkep aralığı    en koyu %92 / en açık %8 ±%5
    ⑥ kapsama             yaratık tuvalin %62–78'i bant
    ⑦ zemin               boş — sahne yok          zorunlu

Bant dışına çıkan plaka OTOMATİK REDDEDİLİR ve yeniden üretilir. Bu karar
insana bırakılmaz; 120 plakada göz kalibrasyonu kayar.

YÖNTEM NOTLARI
    · Tarama açısı 2B Fourier dönüşümünün güç spektrumundan okunur. Gravür
      taraması spektrumda kaynağın yönüne DİK bir çizgi üretir; ölçülen açı
      90° döndürülerek tarama açısına çevrilir.
    · Çizgi kalınlığı, tarama yönüne dik atılan kesitlerdeki koyu koşu
      uzunluklarının medyanıdır. Ortalama değil medyan: tek bir dolu alan
      ortalamayı bozar, medyanı bozmaz.
    · Kapsama, mürekkebin sınırlayıcı kutusunun tuvale oranıdır — mürekkep
      YOĞUNLUĞU değil. İkisi karıştırılırsa koyu bir yaratık "büyük" sanılır.

KULLANIM
    python3 08_BUILD/plates.py --measure          # yalnızca ölç ve raporla
    python3 08_BUILD/plates.py --normalize        # kırp + seviyele + boyutlandır
    python3 08_BUILD/plates.py --pilot            # yalnızca pilot seti
    python3 08_BUILD/plates.py --json 06_REPORTS/plate-consistency.json
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    PLATES_DIR,
    PLATES_RAW_DIR,
    PLATE_SPEC,
    REPORT_DIR,
    ROOT,
    Result,
    load_spec,
)

# Pilot set — altı sınıftan on plaka. Onaylanmadan diğer 110'a geçilmez.
PILOT_IDS = [
    "kerberos", "lamia-hellenic", "kumiho", "each-uisce", "simurgh",
    "draugr", "manananggal", "animikii", "huldufolk", "curupira",
]

PT_PER_INCH = 72.0


def _require_imaging():
    try:
        import numpy as np  # noqa: F401
        from PIL import Image  # noqa: F401
    except ImportError as exc:
        raise SystemExit(
            "HATA: plaka ölçümü Pillow ve numpy gerektirir.\n"
            "      ./08_BUILD/bootstrap.sh  çalıştırın.\n"
            f"      ({exc})"
        )


# =============================================================================
# ÖLÇÜM
# =============================================================================

def load_gray(path: str):
    import numpy as np
    from PIL import Image

    with Image.open(path) as im:
        im = im.convert("L")
        return np.asarray(im, dtype=np.float64) / 255.0


def ink_mask(gray, threshold: float = 0.5):
    """Mürekkep = eşiğin altındaki piksel (0 siyah, 1 beyaz)."""
    return gray < threshold


def measure_aspect(gray) -> float:
    h, w = gray.shape
    return h / w if w else 0.0


def measure_ink_range(gray) -> tuple[float, float]:
    """(en koyu, en açık) — %1 ve %99 yüzdelik, aykırı pikselden bağımsız.
    Siyahlık oranı olarak döner: 0 = beyaz, 1 = tam siyah."""
    import numpy as np

    flat = gray.ravel()
    darkest = 1.0 - float(np.percentile(flat, 1))
    lightest_ink = 1.0 - float(np.percentile(flat[flat < 0.98], 99)) \
        if np.any(flat < 0.98) else 0.0
    return darkest, lightest_ink


def measure_coverage(gray, threshold: float = 0.5) -> tuple[float, float]:
    """(kapsama, mürekkep yoğunluğu).

    kapsama  = mürekkebin sınırlayıcı kutusu ÷ tuval
    yoğunluk = koyu piksel ÷ toplam piksel
    """
    import numpy as np

    mask = ink_mask(gray, threshold)
    density = float(mask.mean())
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    if not rows.any() or not cols.any():
        return 0.0, density
    y0, y1 = np.where(rows)[0][[0, -1]]
    x0, x1 = np.where(cols)[0][[0, -1]]
    bbox = (y1 - y0 + 1) * (x1 - x0 + 1)
    return float(bbox) / gray.size, density


def measure_background(gray, border_frac: float = 0.04) -> float:
    """Kenar bandındaki mürekkep oranı. Zemin boşsa ~0 olmalı.
    Sahne (manzara, çerçeve, zemin gölgesi) buradan yakalanır."""
    import numpy as np

    h, w = gray.shape
    b = max(1, int(min(h, w) * border_frac))
    border = np.concatenate([
        gray[:b, :].ravel(), gray[-b:, :].ravel(),
        gray[:, :b].ravel(), gray[:, -b:].ravel(),
    ])
    return float((border < 0.5).mean())


def measure_hatch(gray) -> tuple[list[float], float]:
    """(baskın tarama açıları °, cm başına çizgi).

    Güç spektrumunun tepe noktalarından okunur. Gravür taraması spektrumda
    kaynağa DİK bir doğru üretir; 90° eklenerek düzeltilir.
    """
    import numpy as np

    # Kare pencere: dikdörtgen tuval spektrumu yönsel olarak çarpıtır.
    h, w = gray.shape
    n = min(h, w)
    y0 = (h - n) // 2
    x0 = (w - n) // 2
    patch = gray[y0 : y0 + n, x0 : x0 + n]

    # Hann penceresi — kenar sızıntısı spektrumda 0°/90° yalancı tepe üretir.
    win = np.outer(np.hanning(n), np.hanning(n))
    spec = np.abs(np.fft.fftshift(np.fft.fft2((1.0 - patch) * win))) ** 2

    c = n // 2
    yy, xx = np.mgrid[0:n, 0:n]
    dy = yy - c
    dx = xx - c
    radius = np.sqrt(dy * dy + dx * dx)

    # DC ve çok düşük frekansları (kompozisyon) ve Nyquist yakınını (gürültü) at
    lo = max(3.0, n * 0.01)
    hi = n * 0.45
    band = (radius >= lo) & (radius <= hi)
    if not band.any():
        return [], 0.0

    angles = (np.degrees(np.arctan2(dy, dx)) + 180.0) % 180.0
    power = spec.copy()
    power[~band] = 0.0

    # 1° kovalarda açısal histogram
    hist = np.zeros(180)
    idx = angles.astype(int) % 180
    np.add.at(hist, idx.ravel(), power.ravel())
    if hist.max() <= 0:
        return [], 0.0
    hist /= hist.max()

    # Tepe seçimi: komşularından yüksek ve tabanın 2 katı üstünde
    baseline = float(np.median(hist))
    peaks = []
    for a in range(180):
        v = hist[a]
        if v < max(0.25, baseline * 2.0):
            continue
        if v >= hist[(a - 1) % 180] and v >= hist[(a + 1) % 180]:
            peaks.append((v, a))
    peaks.sort(reverse=True)

    # Spektrum yönü → tarama yönü: 90° döndür
    hatch_angles = sorted({(a + 90) % 180 for _, a in peaks[:4]})

    # Sıklık: en güçlü açının radyal profilindeki tepe
    freq_cm = 0.0
    if peaks:
        best_angle = peaks[0][1]
        sel = (np.abs(angles - best_angle) < 3.0) & band
        if sel.any():
            r_int = radius[sel].astype(int)
            p = power[sel]
            prof = np.zeros(int(radius.max()) + 1)
            np.add.at(prof, r_int, p)
            if prof.size and prof.max() > 0:
                peak_r = int(np.argmax(prof))
                # peak_r cycles per n px  →  cycles/px  →  cycles/cm @ DPI
                cycles_per_px = peak_r / float(n)
                dpi = PLATE_SPEC["dpi"]
                freq_cm = cycles_per_px * dpi / 2.54
    return hatch_angles, freq_cm


def measure_line_weight(gray, threshold: float = 0.5) -> float:
    """Koyu koşu uzunluklarının medyanı (piksel).

    Yatay ve dikey kesitler alınır; ikisinin birleşiminin medyanı, tarama
    yönünden bağımsız bir kalınlık tahmini verir.
    """
    import numpy as np

    mask = ink_mask(gray, threshold)
    runs: list[int] = []

    def scan(arr2d):
        step = max(1, arr2d.shape[0] // 200)
        for row in arr2d[::step]:
            n = 0
            for v in row:
                if v:
                    n += 1
                elif n:
                    # Çok uzun koşular dolu alandır, çizgi değil
                    if 1 <= n <= 60:
                        runs.append(n)
                    n = 0
            if 1 <= n <= 60:
                runs.append(n)

    scan(mask)
    scan(mask.T)
    if not runs:
        return 0.0
    return float(np.median(runs))


def px_to_pt(px: float, dpi: int) -> float:
    return px * PT_PER_INCH / dpi


def measure_plate(path: str) -> dict:
    gray = load_gray(path)
    dpi = PLATE_SPEC["dpi"]
    aspect = measure_aspect(gray)
    darkest, lightest = measure_ink_range(gray)
    coverage, density = measure_coverage(gray)
    background = measure_background(gray)
    angles, freq_cm = measure_hatch(gray)
    weight_px = measure_line_weight(gray)
    h, w = gray.shape
    return {
        "file": os.path.basename(path),
        "width_px": int(w),
        "height_px": int(h),
        "aspect": round(aspect, 4),
        "line_weight_px": round(weight_px, 2),
        "line_weight_pt": round(px_to_pt(weight_px, dpi), 3),
        "hatch_angles_deg": [round(a, 1) for a in angles],
        "hatch_lines_per_cm": round(freq_cm, 1),
        "ink_darkest": round(darkest, 3),
        "ink_lightest": round(lightest, 3),
        "coverage": round(coverage, 3),
        "ink_density": round(density, 3),
        "background_ink": round(background, 4),
    }


# =============================================================================
# TOLERANS DEĞERLENDİRMESİ
# =============================================================================

def judge(m: dict) -> list[tuple[bool, str, str]]:
    """[(geçti, kural, ayrıntı)] — bant dışı tek kural plakayı reddeder."""
    s = PLATE_SPEC
    out: list[tuple[bool, str, str]] = []

    ok = abs(m["aspect"] - s["aspect"]) <= s["aspect_tol"]
    out.append((ok, "en-boy oranı 1:1,25",
                f"ölçülen {m['aspect']:.3f} · hedef {s['aspect']:.2f} "
                f"±{s['aspect_tol']}"))

    lo = s["line_weight_pt"] * (1 - s["line_weight_tol"])
    hi = s["line_weight_pt"] * (1 + s["line_weight_tol"])
    ok = lo <= m["line_weight_pt"] <= hi
    out.append((ok, "çizgi kalınlığı 1,4 pt ±%15",
                f"ölçülen {m['line_weight_pt']:.2f} pt "
                f"({m['line_weight_px']:.1f} px) · bant {lo:.2f}–{hi:.2f}"))

    angles = m["hatch_angles_deg"]
    tol = s["hatch_angle_tol_deg"]
    wanted = (s["hatch_primary_deg"], s["hatch_secondary_deg"])
    ok = bool(angles) and any(
        min(abs(a - t), 180 - abs(a - t)) <= tol for a in angles for t in wanted
    )
    out.append((ok, "tarama açısı 45°/135° ±5°",
                f"ölçülen {angles or 'tepe yok'}"))

    flo, fhi = s["hatch_lines_per_cm"]
    ok = flo <= m["hatch_lines_per_cm"] <= fhi
    out.append((ok, f"tarama sıklığı {flo}–{fhi} çizgi/cm",
                f"ölçülen {m['hatch_lines_per_cm']:.1f}"))

    ok = abs(m["ink_darkest"] - s["ink_darkest"]) <= s["ink_tol"]
    out.append((ok, "en koyu ton %92 ±%5",
                f"ölçülen %{m['ink_darkest'] * 100:.0f}"))

    ok = abs(m["ink_lightest"] - s["ink_lightest"]) <= s["ink_tol"]
    out.append((ok, "en açık ton %8 ±%5",
                f"ölçülen %{m['ink_lightest'] * 100:.0f}"))

    clo, chi = s["coverage"]
    ok = clo <= m["coverage"] <= chi
    out.append((ok, f"kapsama %{clo * 100:.0f}–%{chi * 100:.0f}",
                f"ölçülen %{m['coverage'] * 100:.0f}"))

    ok = m["background_ink"] < 0.02
    out.append((ok, "zemin boş (kenar bandında mürekkep yok)",
                f"kenar mürekkebi %{m['background_ink'] * 100:.1f} — "
                "sahne, çerçeve veya zemin gölgesi olmamalı"))

    return out


# =============================================================================
# NORMALİZASYON
# =============================================================================

def normalize_plate(src: str, dst: str) -> dict:
    """Kırp → seviyele → hedef tuvale oturt. Ham dosya DEĞİŞTİRİLMEZ."""
    import numpy as np
    from PIL import Image

    with Image.open(src) as im:
        im = im.convert("L")
        arr = np.asarray(im, dtype=np.float64) / 255.0

        # ① kırpma: mürekkebin sınırlayıcı kutusu + %4 pay
        mask = arr < 0.85
        if mask.any():
            rows = np.where(np.any(mask, axis=1))[0]
            cols = np.where(np.any(mask, axis=0))[0]
            pad_y = int((rows[-1] - rows[0]) * 0.04)
            pad_x = int((cols[-1] - cols[0]) * 0.04)
            y0 = max(0, rows[0] - pad_y)
            y1 = min(arr.shape[0], rows[-1] + pad_y + 1)
            x0 = max(0, cols[0] - pad_x)
            x1 = min(arr.shape[1], cols[-1] + pad_x + 1)
            arr = arr[y0:y1, x0:x1]

        # ② seviye düzeltme: %1–%99 yüzdeliği tam siyah–tam beyaza ger
        lo = float(np.percentile(arr, 1))
        hi = float(np.percentile(arr, 99))
        if hi - lo > 1e-6:
            arr = np.clip((arr - lo) / (hi - lo), 0.0, 1.0)
        # şartnamedeki mürekkep aralığına indir (%92 koyu, %8 açık)
        d = PLATE_SPEC["ink_darkest"]
        l = PLATE_SPEC["ink_lightest"]
        arr = arr * ((1 - l) - (1 - d)) + (1 - d)

        out = Image.fromarray((arr * 255).astype("uint8"), mode="L")

        # ③ hedef tuval: 1:1,25 dikey, beyaz dolgu, ortalanmış
        tw = PLATE_SPEC["target_width_px"]
        th = PLATE_SPEC["target_height_px"]
        scale = min(tw / out.width, th / out.height)
        new = (max(1, int(out.width * scale)), max(1, int(out.height * scale)))
        out = out.resize(new, Image.LANCZOS)
        canvas = Image.new("L", (tw, th), 255)
        canvas.paste(out, ((tw - new[0]) // 2, (th - new[1]) // 2))

        os.makedirs(os.path.dirname(dst), exist_ok=True)
        canvas.save(dst, "PNG", optimize=True, dpi=(PLATE_SPEC["dpi"],) * 2)

    return {"src": os.path.basename(src), "dst": os.path.basename(dst)}


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--measure", action="store_true", default=True)
    ap.add_argument("--normalize", action="store_true",
                    help="plates_raw/ → plates/ normalizasyonu")
    ap.add_argument("--pilot", action="store_true",
                    help="yalnızca 10 plakalık pilot seti")
    ap.add_argument("--dir", default=None, help="ölçülecek klasör")
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out",
                    default="06_REPORTS/plate-consistency.json")
    args = ap.parse_args()

    spec = load_spec()
    by_plate = {c["plate"]: c for c in spec["creatures"]}
    wanted = {c["plate"] for c in spec["creatures"]
              if not args.pilot or c["id"] in PILOT_IDS}

    r = Result("PLAKA TUTARLILIK RAPORU (plates.py)"
               + (" · PİLOT SET" if args.pilot else ""))

    src_dir = args.dir or (PLATES_RAW_DIR if args.normalize else PLATES_DIR)
    if not os.path.isdir(src_dir):
        r.ok("plaka klasörü yok", f"{os.path.relpath(src_dir, ROOT)} — "
             "illüstrasyon Faz 4'te başlar")
        return r.report(verbose=args.verbose)

    files = sorted(
        f for f in os.listdir(src_dir)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".tif", ".tiff"))
    )
    present = {os.path.splitext(f)[0]: os.path.join(src_dir, f) for f in files}
    found = {k: v for k, v in present.items() if k in wanted}

    if not found:
        r.ok(
            "henüz plaka yok",
            f"{os.path.relpath(src_dir, ROOT)} boş · beklenen {len(wanted)} plaka "
            "· illüstrasyon Faz 4'te başlar",
        )
        code = r.report(verbose=args.verbose)
        if args.json_out:
            r.to_json(os.path.join(ROOT, args.json_out))
        return code

    _require_imaging()

    if args.normalize:
        for plate_id, path in sorted(found.items()):
            dst = os.path.join(PLATES_DIR, f"{plate_id}.png")
            normalize_plate(path, dst)
            print(f"normalize: {plate_id}")
        src_dir = PLATES_DIR
        found = {
            k: os.path.join(PLATES_DIR, f"{k}.png")
            for k in found
            if os.path.exists(os.path.join(PLATES_DIR, f"{k}.png"))
        }

    measurements = []
    rejected = []
    for plate_id, path in sorted(found.items()):
        m = measure_plate(path)
        m["plate"] = plate_id
        m["creature"] = by_plate.get(plate_id, {}).get("name", "?")
        verdicts = judge(m)
        m["checks"] = [
            {"ok": ok, "rule": rule, "detail": detail} for ok, rule, detail in verdicts
        ]
        m["accepted"] = all(ok for ok, _, _ in verdicts)
        measurements.append(m)
        if not m["accepted"]:
            bad = [f"{rule} → {detail}" for ok, rule, detail in verdicts if not ok]
            rejected.append(f"{plate_id} ({m['creature']}): " + " · ".join(bad))

    r.add(
        not rejected,
        "tolerans dışı plaka yok",
        "\n         ".join(rejected[:10])
        + (f"\n         toplam {len(rejected)} reddedilen plaka" if rejected else ""),
    )

    missing = sorted(wanted - set(found))
    r.ok(
        "plaka sayımı",
        f"{len(found)}/{len(wanted)} mevcut"
        + (f" · eksik: {missing[:8]}{'…' if len(missing) > 8 else ''}"
           if missing else ""),
    )

    # Dağılım — pilot setle üretim setinin örtüşmesi Faz 4 kapısıdır
    if len(measurements) >= 3:
        import statistics as st

        for field, label in (
            ("line_weight_pt", "çizgi kalınlığı (pt)"),
            ("hatch_lines_per_cm", "tarama sıklığı (çizgi/cm)"),
            ("coverage", "kapsama"),
            ("ink_darkest", "en koyu ton"),
        ):
            vals = [m[field] for m in measurements]
            r.ok(
                f"dağılım · {label}",
                f"ort {st.mean(vals):.3f} · std {st.pstdev(vals):.3f} · "
                f"aralık {min(vals):.3f}–{max(vals):.3f}",
            )

    code = r.report(verbose=args.verbose)
    if args.json_out:
        path = os.path.join(ROOT, args.json_out)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(
                {
                    "spec": PLATE_SPEC,
                    "measured": len(measurements),
                    "accepted": sum(1 for m in measurements if m["accepted"]),
                    "rejected": len(rejected),
                    "plates": measurements,
                },
                fh, ensure_ascii=False, indent=2,
            )
            fh.write("\n")
        print(f"\nrapor: {args.json_out}")
    _ = REPORT_DIR
    return code


if __name__ == "__main__":
    raise SystemExit(main())
