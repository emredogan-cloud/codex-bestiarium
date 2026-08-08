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

# Şema kapılarının kusur kurguları — `make_fixtures.py` üretir.
# Her seviyeye TAM BİR kusur konur ve o seviyenin onu yakalaması beklenir.
GATE_FIXTURES = ["draft", "phase1", "phase2", "phase3"]


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

    # Aktif kapı GEÇMELİ
    gate_file = os.path.join(ROOT, ".gate")
    level = "draft"
    if os.path.exists(gate_file):
        with open(gate_file, encoding="utf-8") as fh:
            level = fh.read().strip() or "draft"

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

    # ŞEMA KAPILARININ ISIRDIĞININ KANITI
    # ------------------------------------------------------------------
    # Eskiden burada "bir üst kapı henüz kapalı olmalı" sınanıyordu. O
    # varsayım her faz kapanışında kendini yanlışlar: kapı açıldığı anda
    # test, ortada kusur yokken kırmızıya döner. Metin kapılarında olduğu
    # gibi doğru yöntem KUSUR YERLEŞTİRMEKTİR — her kapı seviyesi için
    # gerçek spec'ten türetilmiş, tam bir kusur taşıyan bir kurgu.
    for gate in GATE_FIXTURES:
        fixture = os.path.join(FIXTURES, f"spec_bad_{gate}.json")
        if not os.path.exists(fixture):
            print(f"[FAIL] spec kurgusu yok: tests/fixtures/spec_bad_{gate}.json "
                  "— python3 08_BUILD/tests/make_fixtures.py")
            failures += 1
            continue
        proc = subprocess.run(
            [PY, os.path.join(BUILD, "validate_spec.py"),
             "--gate", gate, "--spec", fixture],
            capture_output=True, text=True, cwd=ROOT,
        )
        ok = proc.returncode == 1
        print(f"[{'  ok ' if ok else 'FAIL'}] validate_spec.py     "
              f"kusurlu spec, kapı '{gate}' → yakalamalı "
              f"(beklenen çıkış 1, alınan {proc.returncode})")
        if not ok:
            failures += 1
            if args.verbose:
                print("         " + "\n         ".join(
                    proc.stdout.strip().splitlines()[-10:]))

    # CÜMLE BÖLÜCÜNÜN GERİLEME TESTİ
    # ------------------------------------------------------------------
    # `textutil.sentences` paragraf sonunu da cümle sonu sayar. Bu, ön/arka
    # maddedeki noktalamasız ara başlığın kendinden sonraki cümleye
    # yapışmasını önler; yapışırsa `qa_voice`un cümle uzunluğu ölçümü
    # SESSİZCE bozulur — kapı kırmızı yanmaz, yanlış ölçer.
    sys.path.insert(0, BUILD)
    from textutil import sentences as _sent  # noqa: E402

    sent_cases = [
        ("Noktalamasız ara başlık ayrı sayılır",
         "A Book Filed by Function\n\nIt waits at the ford. The rider gets on.",
         3),
        ("Noktayla biten paragraf iki kez bölünmez",
         "It waits at the ford.\n\nThe rider gets on.", 2),
        ("Kısaltma cümleyi bölmez",
         "Croker, Fairy Legends, vol. II; Rose (2000).", 1),
    ]
    for label, text, want in sent_cases:
        got = len(_sent(text))
        ok = got == want
        if not ok:
            failures += 1
        print(f"[{'  ok ' if ok else 'FAIL'}] textutil.sentences   {label} "
              f"(beklenen {want}, alınan {got})")

    print("-" * 78)
    if failures:
        print(f"BAŞARISIZ: {failures} kontrol beklendiği gibi davranmadı.")
        return 1
    print("TAMAM: bütün kalite kapıları beklendiği gibi davranıyor.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
