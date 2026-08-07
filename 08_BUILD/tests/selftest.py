#!/usr/bin/env python3
"""
CODEX BESTIARIUM — KALİTE KAPILARININ KENDİ TESTİ
================================================================================
Bu, hattın en önemli testidir. Kanıtladığı şey:

    QA betikleri gerçekten yakalıyor.

Metin yokken yeşil kalan bir hat, kusurlu metin geldiğinde de yeşil kalabilir.
Bu test o riski kapatır: iki kurgu kitap çalıştırılır ve şu beklenir —

    good.json  → bütün betikler 0 döner
    bad.json   → hedeflenen betikler 1 döner (yakalamazsa TEST BAŞARISIZ)

CI bunu her push'ta çalıştırır. Bir QA betiği bozulursa (ör. bir regex
yanlış düzenlenirse) burası kırmızıya döner — sessizce kör kalmaz.

KULLANIM
    python3 08_BUILD/tests/selftest.py
    python3 08_BUILD/tests/selftest.py --verbose
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
ROOT = os.path.dirname(BUILD)
FIXTURES = os.path.join(HERE, "fixtures")

PY = sys.executable

# (betik, iyi metinde beklenen, kötü metinde beklenen)
#   0 = geçmeli   1 = başarısız olmalı
CASES = [
    ("qa_length.py",      ["--sections"], 0, 1),
    ("qa_voice.py",       [],             0, 1),
    ("qa_echo.py",        [],             0, 1),
    ("qa_diacritics.py",  [],             0, 1),
    # qa_drift yalnızca 10 maddede eğim ölçer; kurguda kasıtlı sürüklenme
    # yoktur, iki metinde de geçmesi beklenir. Buradaki testi "çöküyor mu"dur.
    ("qa_drift.py",       [],             0, 0),
]


def run(script: str, extra: list[str], book: str) -> tuple[int, str]:
    cmd = [PY, os.path.join(BUILD, script), "--book", book, *extra]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    # kurguları her seferinde yeniden üret — kayma olmasın
    gen = subprocess.run(
        [PY, os.path.join(HERE, "make_fixtures.py")],
        capture_output=True, text=True,
    )
    if gen.returncode != 0:
        print(gen.stdout + gen.stderr, file=sys.stderr)
        print("HATA: kurgular üretilemedi.", file=sys.stderr)
        return 2

    good = os.path.join(FIXTURES, "good.json")
    bad = os.path.join(FIXTURES, "bad.json")

    print("=" * 78)
    print("KALİTE KAPILARININ KENDİ TESTİ")
    print("=" * 78)

    failures = 0
    for script, extra, want_good, want_bad in CASES:
        for label, book, want in (("iyi", good, want_good), ("kötü", bad, want_bad)):
            code, out = run(script, extra, book)
            ok = code == want
            mark = "  ok " if ok else "FAIL"
            verb = "geçmeli" if want == 0 else "yakalamalı"
            print(f"[{mark}] {script:<20} {label:<5} metin → {verb} "
                  f"(beklenen çıkış {want}, alınan {code})")
            if not ok:
                failures += 1
                print("         " + "\n         ".join(out.strip().splitlines()[-25:]))
            elif args.verbose:
                print("         " + "\n         ".join(out.strip().splitlines()[-14:]))

    # spec.json doğrulaması draft kapısında geçmeli
    proc = subprocess.run(
        [PY, os.path.join(BUILD, "validate_spec.py"), "--gate", "draft"],
        capture_output=True, text=True, cwd=ROOT,
    )
    ok = proc.returncode == 0
    print(f"[{'  ok ' if ok else 'FAIL'}] validate_spec.py     draft kapısı → geçmeli "
          f"(alınan {proc.returncode})")
    if not ok:
        failures += 1
        print(proc.stdout)

    # Kapıların GERÇEKTEN ısırdığını kanıtlamak için, AÇILMAMIŞ bir sonraki
    # kapıya bakılır. Sabit bir faza bakmak yanlıştır: o faz bitince test
    # kendi kendini yanlışlar. Aktif seviye `.gate`ten okunur; bir üstü
    # kapalı olmalıdır.
    gate_file = os.path.join(ROOT, ".gate")
    level = "draft"
    if os.path.exists(gate_file):
        with open(gate_file, encoding="utf-8") as fh:
            level = fh.read().strip() or "draft"
    order = ["draft", "phase1", "phase2", "phase3"]
    nxt = order[min(order.index(level) + 1, len(order) - 1)] if level in order else "phase1"

    # Aktif kapı GEÇMELİ
    proc = subprocess.run(
        [PY, os.path.join(BUILD, "validate_spec.py"), "--gate", level],
        capture_output=True, text=True, cwd=ROOT,
    )
    ok = proc.returncode == 0
    print(f"[{'  ok ' if ok else 'FAIL'}] validate_spec.py     aktif kapı "
          f"'{level}' → geçmeli (alınan {proc.returncode})")
    if not ok:
        failures += 1
        print(proc.stdout[-1500:])

    # BİR ÜSTÜ kapalı olmalı — kapıların ısırdığının kanıtı
    if nxt != level:
        proc = subprocess.run(
            [PY, os.path.join(BUILD, "validate_spec.py"), "--gate", nxt],
            capture_output=True, text=True, cwd=ROOT,
        )
        ok = proc.returncode == 1
        print(f"[{'  ok ' if ok else 'FAIL'}] validate_spec.py     sonraki kapı "
              f"'{nxt}' → henüz KAPALI olmalı (alınan {proc.returncode})")
        if not ok:
            failures += 1

    print("-" * 78)
    if failures:
        print(f"BAŞARISIZ: {failures} kontrol beklendiği gibi davranmadı.")
        return 1
    print("TAMAM: bütün kalite kapıları beklendiği gibi davranıyor.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
