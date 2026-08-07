#!/usr/bin/env python3
"""
CODEX BESTIARIUM — PLAKA KURGULARI ÜRETİCİSİ (ÖLÇÜM KALİBRASYONU)
================================================================================
`plates.py` yedi parametre ölçer ve bant dışına çıkan plakayı OTOMATİK reddeder.
Yol haritası bunu "projenin tek gerçek başarısızlık modu" sayar. Ama bir soru
hiç sorulmamıştı:

    ÖLÇEN ALET DOĞRU MU ÖLÇÜYOR?

112 plaka eğri bir cetvelle ölçülürse, ölçüm disiplininin tamamı bir gösteriye
dönüşür. Bu dosya o cetveli sınar: geometrisi BİLİNEN sentetik gravür plakaları
üretir ve `plate_selftest.py` ölçülen değerin gerçek değeri bulup bulmadığına
bakar.

    good.png            bütün bantlarda — geçmeli
    bad_<kural>.png     tam bir kural ihlali — YAKALANMALI

Bu plakalar KİTABA GİRMEZ. Yaratık değil, ölçüm hedefidirler; `07_ASSETS`
altına değil `08_BUILD/tests/fixtures/plates/` altına yazılırlar.

KULLANIM
    python3 08_BUILD/tests/plate_fixtures.py
"""

from __future__ import annotations

import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
sys.path.insert(0, BUILD)

from bestiarium import PLATE_SPEC  # noqa: E402

OUT = os.path.join(HERE, "fixtures", "plates")

# --- kurgunun GERÇEK değerleri ------------------------------------------
# Ölçümün bulması gereken sayılar bunlardır. Şartnameden türetilirler ki
# şartname değişince kurgu da değişsin.
DPI = PLATE_SPEC["dpi"]
W = PLATE_SPEC["target_width_px"]
H = PLATE_SPEC["target_height_px"]

HATCH_LINES_PER_CM = 25.0                      # 22–28 bandının ortası
HATCH_PERIOD_PX = (DPI / 2.54) / HATCH_LINES_PER_CM   # ≈ 4,72 px
HATCH_STROKE_PX = HATCH_PERIOD_PX * 0.5        # yarı yarıya siyah-beyaz
CONTOUR_STROKE_PX = PLATE_SPEC["line_weight_pt"] * DPI / 72.0  # 1,4 pt ≈ 5,83 px

INK_DARK = 1.0 - PLATE_SPEC["ink_darkest"]     # 0,08 → en koyu piksel değeri
INK_LIGHT = 1.0 - PLATE_SPEC["ink_lightest"]   # 0,92 → en açık mürekkep

# Figürün sınırlayıcı kutusu tuvalin %70,6'sı (kapsama bandı %62–78)
FIG_FRAC = 0.84

GROUND_TRUTH = {
    "aspect": H / W,
    "hatch_lines_per_cm": HATCH_LINES_PER_CM,
    "hatch_stroke_px": HATCH_STROKE_PX,
    "hatch_stroke_pt": HATCH_STROKE_PX * 72.0 / DPI,
    "contour_stroke_px": CONTOUR_STROKE_PX,
    "contour_stroke_pt": PLATE_SPEC["line_weight_pt"],
    "hatch_angles_deg": [45.0, 135.0],
    "ink_darkest": PLATE_SPEC["ink_darkest"],
    "ink_lightest": PLATE_SPEC["ink_lightest"],
    "coverage": FIG_FRAC * FIG_FRAC,
    "background_ink": 0.0,
}


def _require():
    try:
        import numpy  # noqa: F401
        from PIL import Image  # noqa: F401
    except ImportError as exc:  # pragma: no cover
        raise SystemExit(
            "HATA: plaka kurguları Pillow ve numpy gerektirir.\n"
            "      ./08_BUILD/bootstrap.sh çalıştırın.\n"
            f"      ({exc})"
        )


# =============================================================================
# ÜRETİM
# =============================================================================

def render(
    width: int = W,
    height: int = H,
    period: float = HATCH_PERIOD_PX,
    stroke: float = HATCH_STROKE_PX,
    contour: float = CONTOUR_STROKE_PX,
    angle_deg: float = 45.0,
    cross_angle_deg: float = 135.0,
    fig_frac: float = FIG_FRAC,
    dark: float = INK_DARK,
    light: float = INK_LIGHT,
    background_noise: float = 0.0,
):
    """Bilinen geometride bir gravür plakası.

    Figür bir elipstir; içi `angle_deg` yönünde taranır ve alt yarısında
    `cross_angle_deg` ile çapraz taranır. Ton, figürün üstünden altına doğru
    en koyudan en açığa geçer — böylece mürekkep aralığı ölçülebilir olur.
    Dış hat ayrı ve daha kalın bir konturdur.
    """
    import numpy as np

    img = np.ones((height, width), dtype=np.float64)

    yy, xx = np.mgrid[0:height, 0:width]
    cy, cx = height / 2.0, width / 2.0
    ry, rx = height * fig_frac / 2.0, width * fig_frac / 2.0
    rho = np.sqrt(((yy - cy) / ry) ** 2 + ((xx - cx) / rx) ** 2)
    inside = rho <= 1.0

    def hatch_mask(theta_deg: float) -> "np.ndarray":
        """Verilen açıda, `period` aralıklı, `stroke` kalınlıkta çizgiler."""
        t = math.radians(theta_deg)
        # Çizgi yönü (cos t, sin t); ona DİK eksende mesafe periyodu belirler.
        d = xx * math.sin(t) - yy * math.cos(t)
        phase = np.mod(d, period)
        return phase < stroke

    # Ton geçişi: üstte en koyu, altta en açık
    t = np.clip((yy - (cy - ry)) / (2 * ry), 0.0, 1.0)
    tone = dark + (light - dark) * t

    primary = hatch_mask(angle_deg) & inside
    img[primary] = tone[primary]

    lower = inside & (yy > cy)
    cross = hatch_mask(cross_angle_deg) & lower
    img[cross] = np.minimum(img[cross], tone[cross])

    # Dış hat: elipsin kabuğu, kontur kalınlığında, en koyu tonda
    shell_half = contour / 2.0
    # rho birimini piksele çevir: |∇rho| ≈ 1/r yönüne göre; en kaba ve yeterli
    # yaklaşım ortalama yarıçapı kullanmaktır.
    r_mean = (ry + rx) / 2.0
    shell = np.abs(rho - 1.0) * r_mean <= shell_half
    img[shell] = dark

    if background_noise > 0:
        band = int(min(height, width) * 0.02)
        img[:band, :] = dark
        img[-band:, :] = dark

    return img


def save(arr, path: str) -> None:
    import numpy as np
    from PIL import Image

    os.makedirs(os.path.dirname(path), exist_ok=True)
    Image.fromarray((np.clip(arr, 0, 1) * 255).astype("uint8"), mode="L").save(
        path, "PNG", optimize=True, dpi=(DPI, DPI)
    )


# =============================================================================
# KUSURLU KURGULAR — her biri TAM BİR kuralı ihlal eder
# =============================================================================

DEFECTS = {
    "aspect": (
        "en-boy oranı 1:1,25",
        dict(width=W, height=int(W * 1.10)),
    ),
    "hatch_angle": (
        "tarama açısı 45°/135° ±5°",
        dict(angle_deg=15.0, cross_angle_deg=105.0),
    ),
    "hatch_frequency": (
        "tarama sıklığı 22–28 çizgi/cm",
        dict(period=HATCH_PERIOD_PX * 2.2, stroke=HATCH_STROKE_PX * 2.2),
    ),
    "ink_darkest": (
        "en koyu ton %92 ±%5",
        dict(dark=0.35, light=INK_LIGHT),
    ),
    "coverage": (
        "kapsama %62–78",
        dict(fig_frac=0.45),
    ),
    "background": (
        "zemin boş",
        dict(background_noise=1.0),
    ),
}


def main() -> int:
    _require()
    save(render(), os.path.join(OUT, "good.png"))
    print("yazıldı: tests/fixtures/plates/good.png — bütün bantlarda")
    for name, (rule, kwargs) in DEFECTS.items():
        save(render(**kwargs), os.path.join(OUT, f"bad_{name}.png"))
        print(f"yazıldı: tests/fixtures/plates/bad_{name}.png — ihlal: {rule}")

    print("\nkurgunun gerçek değerleri:")
    for k, v in GROUND_TRUTH.items():
        print(f"  {k:<22} {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
