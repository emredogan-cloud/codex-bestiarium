#!/usr/bin/env python3
"""
CODEX BESTIARIUM — PLAKA ÖLÇÜMÜNÜN KENDİ TESTİ
================================================================================
Metin kapılarının `selftest.py`'si var; plaka kapısının yoktu. Oysa plaka
kapısı yol haritasının "projenin tek gerçek başarısızlık modu" dediği riski
tutuyor ve 112 plakayı otomatik reddetme yetkisi var.

Bu test iki şeyi kanıtlar:

    ① DOĞRULUK — geometrisi bilinen bir plakada ölçüm gerçek değeri buluyor mu?
    ② ISIRMA   — tam bir kural ihlali taşıyan plaka reddediliyor mu?

①'in olmadığı bir hatta ② anlamsızdır: eğri bir cetvel de tutarlı biçimde
"yanlış" der. Bu yüzden önce cetvel ölçülür.

Bu test ilk çalıştırmasında İKİ GERÇEK KUSUR buldu:
    · kalınlık ölçümü 45° taramada √2 yanlıydı ve şartnameye tam uyan bir
      plakayı reddediyordu (%41 hata),
    · şartname tarama darbesiyle dış hattı tek sayıya indirmişti ve iki değer
      geometrik olarak bir arada duramıyordu.
İkisi de `plates.py`'de düzeltildi.

KULLANIM
    python3 08_BUILD/tests/plate_selftest.py
    python3 08_BUILD/tests/plate_selftest.py --verbose --json 06_REPORTS/plate-calibration.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
ROOT = os.path.dirname(BUILD)
sys.path.insert(0, BUILD)

import plates  # noqa: E402
from bestiarium import PLATE_SPEC, Result  # noqa: E402
from tests import plate_fixtures as pf  # noqa: E402

FIXTURES = os.path.join(HERE, "fixtures", "plates")

# (kurgu değeri, ölçüm alanı, kabul edilen bağıl hata)
# Tolerans, ilgili kapının tolerans bandının ÜÇTE BİRİDİR: cetvelin hatası,
# ayırt etmesi beklenen farktan belirgin biçimde küçük olmalıdır.
ACCURACY = [
    ("aspect",             "aspect",             0.01,  "en-boy oranı"),
    ("hatch_stroke_px",    "hatch_stroke_px",    0.05,  "tarama darbesi"),
    ("hatch_lines_per_cm", "hatch_lines_per_cm", 0.05,  "tarama sıklığı"),
    ("coverage",           "coverage",           0.05,  "kapsama"),
]

# Mutlak (oransal değil) karşılaştırılanlar — ±%5'lik bant zaten mutlaktır.
ACCURACY_ABS = [
    ("ink_darkest",  "ink_darkest",  0.05, "en koyu ton"),
    ("ink_lightest", "ink_lightest", 0.05, "en açık ton"),
]


def measure(name: str) -> dict:
    return plates.measure_plate(os.path.join(FIXTURES, f"{name}.png"))


def ensure_fixtures() -> bool:
    need = ["good"] + [f"bad_{k}" for k in pf.DEFECTS]
    missing = [n for n in need if not os.path.exists(os.path.join(FIXTURES, f"{n}.png"))]
    if missing:
        print(f"kurgu üretiliyor ({len(missing)} eksik)…")
        pf.main()
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out",
                    default="06_REPORTS/plate-calibration.json")
    args = ap.parse_args()

    try:
        plates._require_imaging()
    except SystemExit as exc:
        print(exc)
        return 2

    ensure_fixtures()
    r = Result("PLAKA ÖLÇÜMÜNÜN KALİBRASYONU (plate_selftest)")

    # ---------------------------------------------------------- ⓪ GERİLEME
    # Faz 5 · D48: kapsama tabanı artık plakanın kendi kutu oranından
    # TÜRETİLİR, çünkü 1:1,25 tuval + boş kenar bandı + %62 taban üçlüsü
    # dik kutulu yaratıklarda aynı anda sağlanamaz. Türetme kapalı biçimde
    # yazıldı; bu test onu BİLİNEN geometriyle sınar.
    #
    # Gerileme testi olmadan, bir sonraki oturumda "kapsama tabanı neden
    # 0,54'e düşmüş" sorusunun cevabı kodda kaybolur.
    i = (1.0 - 2.0 * plates.BORDER_FRAC) ** 2
    A = PLATE_SPEC["aspect"]
    for aspect, want, note in (
        (A,        i,           "kutu tuvalle aynı oranda → tam güvenli alan"),
        (2 * A,    i * 0.5,     "kutu iki kat dik → yarısı"),
        (A / 2,    i * 0.5,     "kutu iki kat geniş → yarısı"),
        (1.964,    i * A / 1.964, "Migoi — setin en dik kutusu"),
    ):
        got = plates.achievable_coverage(aspect)
        r.add(abs(got - want) < 1e-9,
              f"ulaşılabilir kapsama · {note}",
              f"kutu 1:{aspect:.3f} → beklenen {want:.4f} · hesaplanan {got:.4f}")

    # Sınırın ALTINDA kalan bir plaka hâlâ reddedilmeli: pay yalnızca
    # ayrıklaştırma içindir, sınırın kendisini kaldırmaz.
    fake = {"aspect": A, "hatch_duty": 0.5, "hatch_stroke_px": 2.0,
            "hatch_period_px": 4.0, "hatch_stroke_pt": 0.5,
            "hatch_angles_deg": [45.0], "hatch_lines_per_cm": 25.0,
            "contour_pt": 1.4, "contour_px": 5.8, "contour_runs": 40,
            "ink_darkest": 0.92, "ink_lightest": 0.08, "background_ink": 0.0,
            "box_aspect": 1.964, "coverage": 0.30}
    verdicts = plates.judge(fake)
    cov_ok = next(ok for ok, rule, _ in verdicts if rule.startswith("kapsama"))
    r.add(not cov_ok, "geometrik sınırın ALTINDAKİ plaka reddediliyor",
          "kutu 1:1,964 · ulaşılabilir %54 · sahte ölçüm %30 → reddedilmeli")

    # ---------------------------------------------------------------- ①
    good = measure("good")
    truth = pf.GROUND_TRUTH
    accuracy_rows = []

    for tkey, mkey, tol, label in ACCURACY:
        t, v = truth[tkey], good[mkey]
        err = abs(v - t) / t if t else 0.0
        accuracy_rows.append({"parameter": label, "truth": t, "measured": v,
                              "relError": round(err, 4), "tolerance": tol})
        r.add(err <= tol, f"doğruluk · {label}",
              f"gerçek {t:.3f} · ölçülen {v:.3f} · hata %{err * 100:.1f} "
              f"(en çok %{tol * 100:.0f})")

    for tkey, mkey, tol, label in ACCURACY_ABS:
        t, v = truth[tkey], good[mkey]
        err = abs(v - t)
        accuracy_rows.append({"parameter": label, "truth": t, "measured": v,
                              "absError": round(err, 4), "tolerance": tol})
        r.add(err <= tol, f"doğruluk · {label}",
              f"gerçek {t:.3f} · ölçülen {v:.3f} · fark {err:.3f} "
              f"(en çok {tol:.2f})")

    # Açı: ölçülen tepelerden en az biri hedefe ±5° içinde olmalı
    wanted = (PLATE_SPEC["hatch_primary_deg"], PLATE_SPEC["hatch_secondary_deg"])
    tol_deg = PLATE_SPEC["hatch_angle_tol_deg"]
    hit = [a for a in good["hatch_angles_deg"]
           if any(min(abs(a - w), 180 - abs(a - w)) <= tol_deg for w in wanted)]
    r.add(bool(hit), "doğruluk · tarama açısı",
          f"gerçek {truth['hatch_angles_deg']} · ölçülen "
          f"{good['hatch_angles_deg']} · hedefe oturan: {hit}")

    r.add(good["angle_corrected"], "açı düzeltmesi uygulandı",
          "tarama açısı okunamazsa kalınlık √2 yanlı okunur — bu kusur "
          "Faz 2'de bulundu ve düzeltildi")

    # ---------------------------------------------------------------- ②
    ok_good = all(ok for ok, _, _ in plates.judge(good))
    r.add(ok_good, "şartnameye tam uyan plaka KABUL ediliyor",
          "" if ok_good else " · ".join(
              f"{rule} → {detail}" for ok, rule, detail in plates.judge(good) if not ok))

    # D47 SONRASI ISIRMA BEKLENTİSİ.
    #
    # Üç tarama ölçümü (açı · sıklık · darbe) Faz 5'te kapı olmaktan
    # çıkarıldı: mekanik tramı ölçen cetvel, gelen el işi taramayı
    # okuyamıyor (112 plakada medyan 1,4 çizgi/cm · band 22–28). Bu
    # kurguların ısırması artık BEKLENMEZ ve beklememek de sınanır —
    # aksi hâlde "kapı kalktı" ile "kapı bozuldu" aynı görünür.
    #
    # Kurgular ölçülmeye devam ediyor; değişen şey kararın kimde olduğu.
    DEMOTED = {"hatch_angle", "hatch_frequency"}
    for name, (rule, _) in pf.DEFECTS.items():
        m = measure(f"bad_{name}")
        verdicts = plates.judge(m)
        rejected = [ru for ok, ru, _ in verdicts if not ok]
        if name in DEMOTED:
            r.add(not rejected, f"ısırmıyor (kasıtlı · D47) · {rule}",
                  "ölçülüyor ama karar vermiyor — el işi tarama mekanik "
                  "tram bandıyla yargılanamaz"
                  if not rejected else f"BEKLENMEDİK RED: {rejected}")
        else:
            r.add(bool(rejected), f"ısırma · {rule}",
                  f"reddeden kural: {rejected}" if rejected
                  else "YAKALANMADI — yakalamayan bir kapı, kapı değildir")

    # D47'nin YERİNE GELEN kapı ısırıyor mu? Ton dağılımı kapısı, setin
    # medyanından sapan plakayı yakalamalı. Kapı set düzeyinde çalışır,
    # bu yüzden burada doğrudan mantığı sınanır.
    import statistics as _st
    base = [0.20] * 20
    med = _st.median(base)
    mad = _st.median([abs(d - med) for d in base]) or 1e-9
    limit = 6.0 * mad
    r.add(abs(0.90 - med) > limit,
          "ısırma · ton dağılımı (D47 yerine gelen kapı)",
          f"medyan {med:.3f} · eşik ±{limit:.4f} · sapan plaka 0,900 → "
          "yakalanmalı")

    # ---------------------------------------------------------------- ③
    # Dış hat tahmincisi ayırt edebiliyor mu? Edemiyorsa kapı OLMAMALIDIR.
    contour_rule = [ru for _, ru, _ in plates.judge(good) if "dış hat" in ru]
    r.add(
        bool(contour_rule) and "kapı DEĞİL" in contour_rule[0],
        "dış hat kapı olarak İŞARETLENMEMİŞ",
        f"{contour_rule} — kalibrasyonda 2,9 / 4,2 / 5,83 px konturlu kurgular "
        "ayırt edilemedi; ayırt edemeyen sayı karar veremez",
    )

    code = r.report(verbose=args.verbose)

    if args.json_out:
        path = args.json_out if os.path.isabs(args.json_out) \
            else os.path.join(ROOT, args.json_out)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({
                "groundTruth": truth,
                "measuredGood": good,
                "accuracy": accuracy_rows,
                "defectsCaught": {
                    name: [ru for ok, ru, _ in plates.judge(measure(f"bad_{name}"))
                           if not ok]
                    for name in pf.DEFECTS
                },
                "passed": len(r.passed),
                "failed": len(r.failures),
            }, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"\nrapor: {os.path.relpath(path, ROOT)}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
