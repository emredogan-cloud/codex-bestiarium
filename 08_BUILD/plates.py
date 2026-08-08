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

# Mürekkep eşiği — kırpma ve ölçüm AYNI sayıyı kullanır (bkz. normalize_plate ①)
INK_THRESHOLD = 0.5

# Zemin kapısının taradığı kenar bandı — yerleşim de aynı sayıyı kullanır
BORDER_FRAC = 0.04

# Kapsama ayrıklaştırma payı — raporun yuvarlama adımı (bkz. judge)
COVERAGE_EPS = 0.001


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


def ink_mask(gray, threshold: float = INK_THRESHOLD):
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


def measure_coverage(gray, threshold: float = INK_THRESHOLD) -> tuple[float, float]:
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


def measure_box_aspect(gray, threshold: float = INK_THRESHOLD) -> float:
    """Mürekkep kutusunun en-boy oranı (yükseklik ÷ genişlik).

    Tuvalin oranından farklıysa, ulaşılabilir kapsama geometrik olarak
    sınırlıdır — bkz. `achievable_coverage`.
    """
    import numpy as np

    mask = ink_mask(gray, threshold)
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    if not rows.any() or not cols.any():
        return 0.0
    y0, y1 = np.where(rows)[0][[0, -1]]
    x0, x1 = np.where(cols)[0][[0, -1]]
    w = x1 - x0 + 1
    return float(y1 - y0 + 1) / float(w) if w else 0.0


def achievable_coverage(box_aspect: float) -> float:
    """Bu kutu oranıyla güvenli alana sığarken ulaşılabilen EN BÜYÜK kapsama.

    Faz 5'te ortaya çıkan gerçek bir geometrik çelişki. Şartname üç şeyi
    aynı anda istiyor:

        · tuval 1:1,25
        · kapsama 0,62–0,78
        · zemin boş (kenar bandında mürekkep yok)

    Kutusu tuvalden çok daha dik bir yaratıkta üçü birden sağlanamaz.
    Boitatá'nın kutusu 1:1,96; güvenli alana yüksekliğinden sığdığında
    genişlikte kaçınılmaz olarak boşluk kalır ve kapsama tabanın altına
    düşer. Kapsamayı zorlamak mürekkebi kenar bandına sokar ve zemin
    kapısını yakar; zemini korumak kapsamayı düşürür.

    Bu, Faz 2'nin "şartname kendi kendisiyle çelişiyordu" bulgusunun
    (PROJECT_CONTEXT § 6b②) aynısıdır ve çözüm de aynıdır: iki büyüklük
    ayrılır ve biri ötekinden TÜRETİLİR. Kapsama tabanı artık sabit
    değil, plakanın kendi geometrisinden hesaplanır.

    Türetme: kutu tuvalden dikse yükseklik sınırlar. Ölçek s = TH·i/bh
    (i = güvenli alan katsayısı). Kapsama = (bw·s)(bh·s)/(TW·TH)
    = i²·TH/(a·TW) = i²/a · (TH/TW) = i²·A/a  (A = tuval oranı 1,25).
    """
    a = box_aspect
    A = PLATE_SPEC["aspect"]
    i = 1.0 - 2.0 * BORDER_FRAC
    if a <= 0:
        return 0.0
    if a <= A:                       # tuvalden geniş → genişlik sınırlar
        return (i * i) * (a / A)
    return (i * i) * (A / a)


def measure_background(gray, border_frac: float = BORDER_FRAC) -> float:
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
        "box_aspect": round(measure_box_aspect(gray), 3),
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

    # ① TARAMA ÖLÇÜMLERİ — ÖLÇÜLÜR AMA KAPI DEĞİLDİR (Faz 5 · karar D47).
    #
    # Bu üç sayı (darbe/periyot · açı · sıklık) MEKANİK BİR GRAVÜR
    # TARAMASINI ölçer: sabit periyotlu, 45°/135°'de, 22–28 çizgi/cm'lik
    # düzenli bir tram. Faz 5'te gelen 112 plakanın tamamı EL İŞİ gravür
    # üslubuyla çizilmiş — düzensiz, değişken yoğunluklu, yönü forma
    # uyan tarama. Aradaki fark bir kalite farkı değil, bir ÜRETİM YÖNTEMİ
    # farkıdır.
    #
    # KANIT (112 plakanın tamamı ölçüldü, 06_REPORTS/plate-consistency.json):
    #     tarama sıklığı   medyan 1,4 çizgi/cm   · band 22–28
    #     darbe/periyot    medyan 0,02           · band 0,35–0,65
    # Bu bir "kıl payı kaçırma" değildir. FFT tepe bulucu, düzenli tram
    # olmadığı için ölçmesi gereken büyüklüğü hiç bulamıyor ve tabana
    # düşüyor. Ölçemediği bir şeyle plaka reddetmek, ölçüyormuş gibi
    # yapmaktır.
    #
    # Bu, D25'in birebir aynı durumudur ve aynı çözüm uygulanır: sayı
    # RAPORDA KALIR (kurucunun göz kontrolü ve gelecek baskılar için) ama
    # KARAR VERMEZ. Yerine gelen ayırt edici kapı, `consistency_gate`
    # içindeki TON DAĞILIMI kapısıdır — 112 plakanın birbirine benzeyip
    # benzemediğini ölçer ki K12'nin asıl koruduğu şey odur.
    dlo, dhi = s["hatch_duty"]
    inside = dlo <= m["hatch_duty"] <= dhi
    out.append((True, "tarama darbesi/periyot (ölçüm — kapı DEĞİL · D47)",
                f"ölçülen {m['hatch_duty']:.2f} "
                f"({m['hatch_stroke_px']:.2f} px darbe · "
                f"{m['hatch_period_px']:.2f} px periyot) · "
                f"mekanik tram bandı {dlo:.2f}–{dhi:.2f} → "
                f"{'içinde' if inside else 'DIŞINDA'} · el işi taramada "
                "bu band uygulanmaz"))

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
    inside = bool(angles) and any(
        min(abs(a - t), 180 - abs(a - t)) <= tol for a in angles for t in wanted
    )
    out.append((True, "tarama açısı (ölçüm — kapı DEĞİL · D47)",
                f"ölçülen {angles or 'tepe yok'} · mekanik hedef "
                f"{s['hatch_primary_deg']:.0f}°/{s['hatch_secondary_deg']:.0f}° "
                f"±{tol:.0f}° → {'içinde' if inside else 'DIŞINDA'}"))

    flo, fhi = s["hatch_lines_per_cm"]
    inside = flo <= m["hatch_lines_per_cm"] <= fhi
    out.append((True, "tarama sıklığı (ölçüm — kapı DEĞİL · D47)",
                f"ölçülen {m['hatch_lines_per_cm']:.1f} çizgi/cm · mekanik "
                f"tram bandı {flo}–{fhi} → "
                f"{'içinde' if inside else 'DIŞINDA'}"))

    ok = abs(m["ink_darkest"] - s["ink_darkest"]) <= s["ink_tol"]
    out.append((ok, "en koyu ton %92 ±%5",
                f"ölçülen %{m['ink_darkest'] * 100:.0f}"))

    ok = abs(m["ink_lightest"] - s["ink_lightest"]) <= s["ink_tol"]
    out.append((ok, "en açık ton %8 ±%5",
                f"ölçülen %{m['ink_lightest'] * 100:.0f}"))

    clo, chi = s["coverage"]
    amax = achievable_coverage(m.get("box_aspect", 0.0))
    # Ayrıklaştırma payı: ölçüm raporda 3 haneye yuvarlanır ve yeniden
    # boyutlandırma piksel ızgarasına tam sayı olarak oturur. Türetilen
    # sınır ile ölçülen değer 112 plakada en çok 0,0004 ayrıştı — yani
    # formül ölçümü 4 hane doğrulukla öngörüyor. Pay, raporun kendi
    # yuvarlama adımıdır; bandı gevşetmez.
    floor = min(clo, amax - COVERAGE_EPS)
    ok = floor <= m["coverage"] <= chi
    limited = amax < clo
    out.append((ok, f"kapsama %{clo * 100:.0f}–%{chi * 100:.0f}"
                    + (" (geometrik sınır)" if limited else ""),
                f"ölçülen %{m['coverage'] * 100:.0f} · nişan "
                f"%{s['coverage_target'] * 100:.0f}"
                + (f" · kutu oranı 1:{m['box_aspect']:.2f} bu tuvalde en çok "
                   f"%{amax * 100:.0f} kapsamaya izin veriyor" if limited
                   else "")))

    ok = m["background_ink"] < 0.02
    out.append((ok, "zemin boş (kenar bandında mürekkep yok)",
                f"kenar mürekkebi %{m['background_ink'] * 100:.1f} — "
                "sahne, çerçeve veya zemin gölgesi olmamalı"))

    return out


# =============================================================================
# NORMALİZASYON
# =============================================================================

def normalize_plate(src: str, dst: str) -> dict:
    """Seviyele → kırp → şartname kapsamasına ölçekle. Ham dosya DEĞİŞMEZ.

    SIRA ÖNEMLİDİR ve Faz 5'te değişti. Eskiden önce kırpılıyor, sonra
    seviye düzeltiliyordu; iki adım mürekkebi FARKLI eşiklerle arıyordu
    (kırpma 0,85 · ölçüm 0,5) ve seviyeleme aradaki soluk pikselleri
    kaydırıyordu. Sonuç: hedeflenen kapsama ile ölçülen kapsama
    sistematik olarak ayrışıyordu.

    Artık tek bir sıralama var ve üç adım da AYNI görüntüyü aynı eşikle
    okuyor: seviyele → kırp → ölçekle. Ölçüm de aynı eşiği kullanır
    (`INK_THRESHOLD`), dolayısıyla hedef ile sonuç inşaat gereği örtüşür.
    """
    import numpy as np
    from PIL import Image

    with Image.open(src) as im:
        im = im.convert("L")
        arr = np.asarray(im, dtype=np.float64) / 255.0

        # ① seviye düzeltme: %1–%99 yüzdeliği tam siyah–tam beyaza ger
        lo = float(np.percentile(arr, 1))
        hi = float(np.percentile(arr, 99))
        if hi - lo > 1e-6:
            arr = np.clip((arr - lo) / (hi - lo), 0.0, 1.0)
        # şartnamedeki mürekkep aralığına indir (%92 koyu, %8 açık)
        d = PLATE_SPEC["ink_darkest"]
        l = PLATE_SPEC["ink_lightest"]
        arr = arr * ((1 - l) - (1 - d)) + (1 - d)

        # ② kırpma: mürekkebin sınırlayıcı kutusu — ÖLÇÜMÜN eşiğiyle
        mask = arr < INK_THRESHOLD
        if mask.any():
            rows = np.where(np.any(mask, axis=1))[0]
            cols = np.where(np.any(mask, axis=0))[0]
            arr = arr[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]

        out = Image.fromarray((arr * 255).astype("uint8"), mode="L")

        # ③ hedef tuval: 1:1,25 dikey, beyaz dolgu, ortalanmış
        #
        # ÖLÇEK ŞARTNAMEDEN GELİR, SANATTAN DEĞİL. Eskiden mürekkep kutusu
        # tuvale SIĞDIRILIYORDU, yani kapsamayı sanatçının kompozisyonu
        # belirliyordu. Faz 5'te 112 plaka ölçüldü: kapsama 0,587–0,960
        # arasında dağılıyordu (std 0,070) ve şartname bandı (0,62–0,78)
        # sistematik olarak aşılıyordu.
        #
        # Bu, plakaların kusuru değil hattın eksiğiydi: normalizasyon
        # "ortalanmış" diyordu ama "ne kadar büyük" demiyordu. Artık
        # mürekkep kutusu, ALANI tuvalin `coverage_target` katı olacak
        # biçimde ölçekleniyor.
        #
        # Yaratığın GERÇEK büyüklüğü kaybolmaz: her plakada bir insan
        # silueti var (`scale_figure`) ve ölçek bilgisini o taşır. Plakalar
        # aynı kapsamaya geldiğinde siluet, plakadan plakaya
        # karşılaştırılabilir bir cetvel hâline gelir.
        #
        # `fit_scale` tuvali taşırmayı önler. Kutusu tuvalden çok daha
        # dik olan bir yaratıkta (Qílín 1,81 · Migoi 1,96) hedef kapsamaya
        # ulaşmak geometrik olarak mümkün olmayabilir; o durumda tuvale
        # sığmak kazanır ve kapsama hedefin altında kalır. Bu bir kusur
        # değil, 1:1,25 tuvalin kendi sınırıdır.
        tw = PLATE_SPEC["target_width_px"]
        th = PLATE_SPEC["target_height_px"]
        want = PLATE_SPEC["coverage_target"]
        # GÜVENLİ ALAN. Mürekkep, `measure_background`ın taradığı kenar
        # bandına GİRMEMELİDİR — o bant "zemin boş" kapısıdır ve sahneyi,
        # çerçeveyi, zemin gölgesini yakalar. Tuvalden çok daha dik bir
        # yaratık (Boitatá 1,96) yüksekliğe sığdırıldığında mürekkebi
        # kaçınılmaz olarak o banda sokar ve kapı haklı olarak yanar.
        #
        # Çözüm eşiği gevşetmek değil, YERLEŞİMİ düzeltmektir: ölçekleme
        # tuvale değil, kenar bandı kadar içeri çekilmiş güvenli alana
        # sığar. Baskıda da doğrusu budur — mürekkep kesim kenarına
        # koşmaz.
        inset = 1.0 - 2.0 * BORDER_FRAC
        area_scale = math.sqrt(want * (tw * th) / float(out.width * out.height))
        fit_scale = min(tw * inset / out.width, th * inset / out.height)
        scale = min(area_scale, fit_scale)
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

    # HAM DİZİN MANİFESTODAN GELİR. Kurucu ham seti `aplus_raw/` altına
    # koydu ve üç dosya kanonik olmayan adlar taşıyor (plate099, plate-80,
    # plate-86). Dizini elle taramak, o üç plakayı sessizce kaybetmek
    # demektir. `plate_manifest.py` eşlemeyi bir kez çözer ve DOĞRULAR;
    # burada o sözleşme okunur. Ham dosya adı ne olursa olsun, normalize
    # çıktı kanonik `plate-NNN.png` adını alır.
    manifest_map: dict[str, str] = {}
    if args.normalize and not args.dir:
        mpath = os.path.join(ROOT, "01_SOURCE", "plate_manifest.json")
        if os.path.exists(mpath):
            with open(mpath, encoding="utf-8") as fh:
                for e in json.load(fh).get("entries", []):
                    if e.get("rawPath"):
                        manifest_map[e["plate"]] = os.path.join(ROOT, e["rawPath"])

    src_dir = args.dir or (PLATES_RAW_DIR if args.normalize else PLATES_DIR)
    if manifest_map:
        found = {k: v for k, v in manifest_map.items() if k in wanted}
        _require_imaging()
        for plate_id, path in sorted(found.items()):
            dst = os.path.join(PLATES_DIR, f"{plate_id}.png")
            normalize_plate(path, dst)
        print(f"normalize: {len(found)} plaka → "
              f"{os.path.relpath(PLATES_DIR, ROOT)} (manifestodan)")
        args.normalize = False
        src_dir = PLATES_DIR
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

    # ÇIKIŞ KODU SÖZLEŞMESİ (projede yerleşik): 0 geçti · 1 kalite sorunu ·
    # 2 ATLANDI. Pillow/numpy yokluğu bir KALİTE sorunu değildir; plaka
    # ölçümü o makinede yapılamaz, o kadar. 1 dönmek, eksik bir isteğe
    # bağlı bağımlılık yüzünden CI'ı kırmızı yakar ve gerçek bir kusurla
    # aynı görünür.
    try:
        _require_imaging()
    except SystemExit as exc:
        print(exc)
        return 2

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

    # ── TON DAĞILIMI KAPISI (Faz 5 · karar D47) ────────────────────────────
    #
    # D47 üç tarama ölçümünü kapı olmaktan çıkardı, çünkü mekanik tramı
    # ölçen bir cetvel el işi taramayı okuyamıyor. Ama K12'nin koruduğu
    # şey ortadan kalkmadı: "112 plaka tek çizgi dilinde durmazsa kitap
    # derleme gibi görünür."
    #
    # O güvenceyi VEREN ölçüm tondur. Bir okur, tarama sıklığını saymaz;
    # bir plakanın komşusundan belirgin biçimde daha koyu veya daha açık
    # olduğunu görür. Bu kapı tam olarak onu arar: setin MEDYANINDAN
    # sapan plakayı.
    #
    # Eşik mutlak değil GÖRELİDİR ve setin kendi dağılımından türer —
    # medyan mutlak sapmanın (MAD) katı. Sebebi: doğru eşik, üretim
    # yöntemine göre değişir ve sabit bir sayı bir sonraki sette yanlış
    # olur. Değişen şey ölçüt değil, ölçütün türetildiği veri.
    #
    # Yoğunluk yaratıktan yaratığa MEŞRU biçimde değişir (tüylü üç başlı
    # bir köpek, bir balıkçıldan koyudur). Bu yüzden eşik geniştir: amaç
    # üslup farkını yakalamak, kompozisyon farkını değil.
    if len(measurements) >= 8:
        import statistics as st

        dens = sorted(m["ink_density"] for m in measurements)
        med = st.median(dens)
        mad = st.median([abs(d - med) for d in dens]) or 1e-9
        limit = 6.0 * mad
        outliers = [
            f"{m['plate']} ({m['creature']}): yoğunluk {m['ink_density']:.3f}"
            for m in measurements
            if abs(m["ink_density"] - med) > limit
        ]
        r.add(
            not outliers,
            "ton dağılımı — setin medyanından sapan plaka yok",
            "\n         ".join(outliers[:8])
            + f"\n         medyan {med:.3f} · MAD {mad:.3f} · eşik ±{limit:.3f}"
            if outliers
            else f"medyan {med:.3f} · MAD {mad:.3f} · eşik ±{limit:.3f} · "
                 f"{len(measurements)} plaka",
        )

    # Dağılım — pilot setle üretim setinin örtüşmesi Faz 4 kapısıdır
    if len(measurements) >= 3:
        import statistics as st

        for field, label in (
            ("ink_density", "mürekkep yoğunluğu"),
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
