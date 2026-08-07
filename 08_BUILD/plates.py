#!/usr/bin/env python3
"""
CODEX BESTIARIUM — PLAKA NORMALİZASYONU VE TUTARLILIK ÖLÇÜMÜ
================================================================================
Yol haritası Bölüm 07.3: "projenin en büyük riski".

    120 plaka tek bir çizgi dilinde durmazsa kitap 'derleme' gibi görünür ve
    premium konumlanma çöker. Bu, projenin tek gerçek başarısızlık modudur ve
    ÖLÇÜLEREK yönetilmelidir — göz kararıyla değil.

Bu betik o ölçümü yapar. Yedi kapı, her biri kendi tolerans bandında:

    ① en-boy oranı        1:1,25 dikey             ±0,02
    ② tarama darbesi      darbe/periyot 0,35–0,65  bant
    ③ tarama açısı        45° birincil / 135°      ±5°
    ④ tarama sıklığı      cm başına 22–28 çizgi    bant
    ⑤ mürekkep aralığı    en koyu %92 / en açık %8 ±%5
    ⑥ kapsama             yaratık tuvalin %62–78'i bant
    ⑦ zemin               boş — sahne yok          zorunlu

    (dış hat kalınlığı ÖLÇÜLÜR ama kapı değildir — aşağıya bakın)

Bant dışına çıkan plaka OTOMATİK REDDEDİLİR ve yeniden üretilir. Bu karar
insana bırakılmaz; 112 plakada göz kalibrasyonu kayar.

FAZ 2 KALİBRASYONU — CETVEL DOĞRU MU ÖLÇÜYOR?
    `tests/plate_fixtures.py` geometrisi BİLİNEN plakalar üretir;
    `tests/plate_selftest.py` ölçümü o bilinen değerle karşılaştırır. Bu
    sınav iki gerçek kusur buldu ve ikisi de burada düzeltildi:

    ① **Açı yanlılığı (√2).** Kalınlık, tarama yönüne dik olmayan kesitlerden
      okunuyordu. 45° taramada koşu uzunluğu gerçek kalınlığın 1,41 katıdır;
      ölçüm ŞARTNAMEYE TAM UYAN BİR PLAKAYI reddediyordu. Düzeltildikten
      sonra hata %41 → %0,3.

    ② **İki ayrı kalınlığın tek sayıya indirilmesi.** Şartnamedeki 1,4 pt bir
      DIŞ HAT kalınlığıdır; 22–28 çizgi/cm'lik taramanın periyodu ≈4,7 px ve
      içine 5,8 px sığmaz — şartname kendi kendisiyle çelişiyordu. Tarama
      darbesi artık periyoda ORANLA ölçülür (bant sıklıktan türer) ve dış hat
      ayrı raporlanır.

YÖNTEM NOTLARI
    · Tarama açısı 2B Fourier dönüşümünün güç spektrumundan okunur. Gravür
      taraması spektrumda kaynağın yönüne DİK bir çizgi üretir; ölçülen açı
      90° döndürülerek tarama açısına çevrilir.
    · Tarama darbesi, açıya göre düzeltilmiş koşu uzunluklarının BUDANMIŞ
      ORTALAMASIDIR. Medyan bu ölçekte tam sayıya yapışır (%10 hata);
      budanmış ortalama hem uzun kuyruğa bağışıklıdır hem ara değeri okur.
    · Kapsama, mürekkebin sınırlayıcı kutusunun tuvale oranıdır — mürekkep
      YOĞUNLUĞU değil. İkisi karıştırılırsa koyu bir yaratık "büyük" sanılır.
    · **Dış hat kapı değildir.** Kalibrasyonda 2,9 / 4,2 / 5,83 px konturlu
      kurgular ayırt edilemedi (bkz. `judge`). Ayırt edemeyen bir sayıyla
      plaka reddetmek, ölçüyormuş gibi yapmaktır.

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


MAX_RUN_PX = 60          # bundan uzun koşu dolu alandır, çizgi değil
MIN_ANGLE_FACTOR = 0.2   # taramaya ~11°'den yakın paralel kesit sayılmaz


def _scan_runs(mask) -> list[int]:
    """Bir eksende koyu koşu uzunlukları (piksel)."""
    runs: list[int] = []
    step = max(1, mask.shape[0] // 200)
    for row in mask[::step]:
        n = 0
        for v in row:
            if v:
                n += 1
            elif n:
                if 1 <= n <= MAX_RUN_PX:
                    runs.append(n)
                n = 0
        if 1 <= n <= MAX_RUN_PX:
            runs.append(n)
    return runs


def _angle_factor(angles: list[float], vertical_scan: bool) -> float:
    """Koşu uzunluğunu DİK kalınlığa çeviren çarpan.

    Bir kesit, tarama çizgisini dik kesmez; θ açıyla keser ve koşu uzunluğu
    gerçek kalınlığın 1/sin θ katı olur. 45° taramada bu **√2 ≈ 1,41**
    demektir — yani ölçüm, şartnamedeki kalınlığın %41 üstünü okur ve
    ŞARTNAMEYE TAM UYAN BİR PLAKAYI REDDEDER.

    Bu düzeltme olmadan 112 plakanın tamamı eğri bir cetvelle ölçülürdü.
    """
    import math

    if not angles:
        return 1.0
    best = 0.0
    for a in angles:
        t = math.radians(a)
        f = abs(math.cos(t)) if vertical_scan else abs(math.sin(t))
        best = max(best, f)
    return best if best >= MIN_ANGLE_FACTOR else 1.0


def measure_strokes(gray, angles: list[float], threshold: float = 0.5) -> dict:
    """Tarama darbesi ve dış hat kalınlığı (piksel) — açıya göre düzeltilmiş.

    ÜÇ NOT

    ① **Açı düzeltmesi.** `_angle_factor`'a bakın. Düzeltilmemiş ölçüm 45°
       taramada gerçek kalınlığın √2 katını okur.

    ② **Medyan değil, budanmış ortalama.** Bu ölçekte koşular 3 veya 4
       piksele yuvarlanır; medyan tam sayıya yapışır ve %10'a varan hata
       verir. Medyanın iki katına kadar olan koşuların ORTALAMASI hem uzun
       kuyruğa (dolu alan, kontur) bağışıklıdır hem de ara değeri okur.
       Kurgu üzerinde ölçülen hata: %10 → %0,4.

    ③ **Tarama darbesi ile dış hat AYRI şeylerdir.** Şartnamedeki 1,4 pt bir
       DIŞ HAT kalınlığıdır; 22–28 çizgi/cm'lik bir taramanın periyodu
       ≈4,7 pikseldir ve içine 1,4 pt (5,8 px) sığmaz. İkisini tek sayıya
       indirmek şartnameyi kendi kendisiyle çelişir hâle getirir. Ayrı
       ölçülürler: darbe koşu dağılımının modu, dış hat ise kuyruğun ALT
       kenarıdır (kontur, teğetine göre uzar; en kısa kesişme gerçek
       kalınlıktır).
    """
    import numpy as np

    mask = ink_mask(gray, threshold)
    pools = [
        (np.asarray(_scan_runs(mask), dtype=float), _angle_factor(angles, False)),
        (np.asarray(_scan_runs(mask.T), dtype=float), _angle_factor(angles, True)),
    ]
    corrected = np.concatenate(
        [p * f for p, f in pools if p.size]
    ) if any(p.size for p, _ in pools) else np.array([])

    if corrected.size == 0:
        return {"hatch_px": 0.0, "contour_px": 0.0, "runs": 0,
                "contour_runs": 0, "angle_corrected": bool(angles)}

    med = float(np.median(corrected))
    core = corrected[corrected <= 2.0 * med]
    hatch = float(core.mean()) if core.size else med

    # Dış hat: taramanın iki katından uzun koşular. Kontur teğetine göre
    # uzadığı için kuyruğun ALT kenarı (p10) gerçek kalınlığa en yakın
    # sağlam tahmindir; ortalama veya medyan teğet dağılımını ölçer.
    tail = corrected[corrected > 2.0 * med]
    contour = float(np.percentile(tail, 10)) if tail.size >= 20 else 0.0

    return {
        "hatch_px": hatch,
        "contour_px": contour,
        "runs": int(corrected.size),
        "contour_runs": int(tail.size),
        "angle_corrected": bool(angles),
    }


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
    strokes = measure_strokes(gray, angles)
    h, w = gray.shape

    # Tarama darbesinin periyoda oranı: tonun ölçüsü. 0,5 = yarı yarıya
    # siyah-beyaz. Bant, sıklıktan TÜREDİĞİ için sabit bir pt değeri gibi
    # kendi kendisiyle çelişemez.
    period_px = (dpi / 2.54) / freq_cm if freq_cm > 0 else 0.0
    ratio = strokes["hatch_px"] / period_px if period_px > 0 else 0.0

    return {
        "file": os.path.basename(path),
        "width_px": int(w),
        "height_px": int(h),
        "aspect": round(aspect, 4),
        "hatch_stroke_px": round(strokes["hatch_px"], 2),
        "hatch_stroke_pt": round(px_to_pt(strokes["hatch_px"], dpi), 3),
        "hatch_period_px": round(period_px, 2),
        "hatch_duty": round(ratio, 3),
        "contour_px": round(strokes["contour_px"], 2),
        "contour_pt": round(px_to_pt(strokes["contour_px"], dpi), 3),
        "runs": strokes["runs"],
        "contour_runs": strokes["contour_runs"],
        "angle_corrected": strokes["angle_corrected"],
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

    # ① TARAMA DARBESİ — bandı sıklıktan türer, sabit bir pt değerinden değil.
    # Sabit değer, 22–28 çizgi/cm ile geometrik olarak çelişirdi (periyot
    # ≈4,7 px; içine 1,4 pt = 5,8 px sığmaz).
    dlo, dhi = s["hatch_duty"]
    ok = dlo <= m["hatch_duty"] <= dhi
    out.append((ok, f"tarama darbesi/periyot {dlo:.2f}–{dhi:.2f}",
                f"ölçülen {m['hatch_duty']:.2f} "
                f"({m['hatch_stroke_px']:.2f} px darbe · "
                f"{m['hatch_period_px']:.2f} px periyot · "
                f"{m['hatch_stroke_pt']:.2f} pt)"
                + ("" if m.get("angle_corrected") else
                   " · UYARI: tarama açısı okunamadı, açı düzeltmesi yok")))

    # ② DIŞ HAT — ÖLÇÜLÜR AMA KAPI DEĞİLDİR. Gerekçe, uydurma değil ölçümdür:
    # Faz 2 kalibrasyonunda kontur kalınlığı 2,9 · 4,2 · 5,83 · 7,3 · 8,75 px
    # olan beş kurgu üretildi ve koşu-uzunluğu istatistiklerinin İLK ÜÇÜNÜ
    # AYIRT EDEMEDİĞİ görüldü (p10 üçünde de aynı çıkıyor). Sebep geometrik:
    # 25 çizgi/cm'de tarama periyodu ≈4,7 px, 1,4 pt kontur ise 5,8 px —
    # aynı büyüklük mertebesinde. Birleşen tarama darbeleri kontur
    # kesişmeleriyle karışıyor.
    #
    # Ayırt edemeyen bir sayıyla plaka reddetmek, ölçüyormuş gibi yapmaktır.
    # Sayı raporda kalır (kurucunun göz kontrolü için) ama karar vermez.
    # Gerçek "tek çizgi dili" güvencesi ölçülebilen yedi parametredir.
    lo = s["line_weight_pt"] * (1 - s["line_weight_tol"])
    hi = s["line_weight_pt"] * (1 + s["line_weight_tol"])
    inside = lo <= m["contour_pt"] <= hi
    out.append((
        True,
        "dış hat kalınlığı (ölçüm — kapı DEĞİL)",
        f"ölçülen {m['contour_pt']:.2f} pt "
        f"({m['contour_px']:.1f} px · {m['contour_runs']} kesişme) · "
        f"hedef {s['line_weight_pt']:.2f} pt bandı {lo:.2f}–{hi:.2f} → "
        f"{'içinde' if inside else 'DIŞINDA'} · "
        "tahminci kalibre edilemedi, plaka bu satır yüzünden reddedilmez",
    ))

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
            ("hatch_stroke_pt", "tarama darbesi (pt)"),
            ("hatch_duty", "darbe/periyot"),
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
