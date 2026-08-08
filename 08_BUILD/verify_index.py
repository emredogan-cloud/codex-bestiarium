#!/usr/bin/env python3
"""
CODEX BESTIARIUM — DİZİN SAYFA NUMARASI DOĞRULAMASI (Faz 6)
================================================================================
Dizindeki sayfa numarası, o maddenin BASILI PDF'te gerçekten bulunduğu
sayfayı mı gösteriyor?

    NEDEN
    ─────
    Yol haritası: *"Dizin sayfa numaralarını `pagemap.json`'dan oku. Elle
    girme — Cilt 1'de sırt kaymasının kaynağı tam olarak buydu."* Ve
    editoryal görev: *"Dizin sayfa numaralarının gerçekten doğru olduğu
    GÖZLE doğrulanır (rastgele 20 madde)."*

    Gözle yirmi madde bakmak bir örneklemedir. Bu betik AYNI DOĞRULAMAYI
    yüz on iki maddenin tamamında yapar ve gözle bakılacak yirmi maddeyi
    de ayrıca listeler — biri diğerinin yerine geçmez, ikisi birlikte
    çalışır.

    ZİNCİR ÜÇ HALKALI ve her halka ayrı ayrı bozulabilir:
        dizgi → pagemap.json → indexes.json → basılı dizin sayfası
    Betik zincirin İKİ UCUNU karşılaştırır: dizinde yazan numarayı alır,
    PDF'in o sayfasındaki METNİ çıkarır ve yaratığın adını orada arar.
    Aradaki halkaların hepsi doğruysa ad oradadır.

ÇIKIŞ KODLARI
    0  hepsi doğru      1  eşleşmeyen var      2  PDF veya araç yok

KULLANIM
    python3 08_BUILD/verify_index.py
    python3 08_BUILD/verify_index.py --sample 20      # gözle bakılacaklar
"""

from __future__ import annotations

import argparse
import json
import os
import random
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ROOT, load_spec  # noqa: E402

PDF = os.path.join(ROOT, "04_PRINT", "PAPERBACK",
                   "CODEX_BESTIARIUM_INTERIOR_PAPERBACK.pdf")
PAGEMAP = os.path.join(ROOT, "04_PRINT", "PAPERBACK", "pagemap.json")
INDEXES = os.path.join(ROOT, "01_SOURCE", "indexes.json")
REPORT = os.path.join(ROOT, "06_REPORTS", "index-verification.json")


def page_text(pdf: str, physical: int) -> str:
    out = subprocess.run(
        ["pdftotext", "-f", str(physical), "-l", str(physical), pdf, "-"],
        capture_output=True, text=True)
    return out.stdout


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sample", type=int, default=20)
    ap.add_argument("--seed", type=int, default=112)
    args = ap.parse_args()

    for p in (PDF, PAGEMAP, INDEXES):
        if not os.path.exists(p):
            print(f"ATLANDI: {os.path.relpath(p, ROOT)} yok — önce "
                  f"08_BUILD/make_book.py")
            return 2
    if subprocess.run(["which", "pdftotext"],
                      capture_output=True).returncode != 0:
        print("ATLANDI: pdftotext yok (poppler-utils)")
        return 2

    with open(PAGEMAP, encoding="utf-8") as fh:
        pm = json.load(fh)
    with open(INDEXES, encoding="utf-8") as fh:
        idx = json.load(fh)
    spec = load_spec()
    by_id = {c["id"]: c for c in spec["creatures"]}

    body_start = pm["_meta"]["bodyStartsAtPhysical"]

    # Dizinde yazan numarayı topla — kaynağı `indexes.json`, pagemap değil.
    # İkisi ayrışmışsa yakalanması gereken tam olarak budur.
    printed: dict[str, str] = {}
    for row in idx["traditions"]:
        for e in row["entries"]:
            printed[e["id"]] = e["page"]

    checks, bad = [], []
    for cid, page in sorted(printed.items()):
        rec = by_id.get(cid)
        if rec is None or not str(page).isdigit():
            bad.append((cid, page, "dizinde sayfa numarası yok"))
            continue
        physical = int(page) + body_start - 1
        text = page_text(PDF, physical)
        ok = rec["name"] in text
        checks.append((cid, page, physical, ok))
        if not ok:
            bad.append((cid, page, f"fiziksel {physical}. sayfada "
                                   f"“{rec['name']}” bulunamadı"))

    print("=" * 78)
    print("DİZİN SAYFA NUMARASI DOĞRULAMASI")
    print("=" * 78)
    print(f"  denetlenen madde : {len(checks)}")
    print(f"  gövde başlangıcı : fiziksel {body_start}. sayfa")

    rnd = random.Random(args.seed)
    sample = rnd.sample(checks, min(args.sample, len(checks)))
    print(f"\n▸ gözle bakılacak {len(sample)} madde "
          f"(tohum {args.seed} — tekrarlanabilir)")
    for cid, page, phys, ok in sorted(sample, key=lambda x: int(x[1])):
        print(f"  {'ok' if ok else 'HATA':>4}  {by_id[cid]['name']:<22} "
              f"dizin s.{page:<4} → PDF fiziksel s.{phys}")

    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as fh:
        json.dump({"checked": len(checks), "failed": len(bad),
                   "bodyStartsAtPhysical": body_start,
                   "sample": [{"id": c, "indexPage": p,
                               "physicalPage": ph, "ok": o}
                              for c, p, ph, o in sample],
                   "failures": [{"id": c, "page": p, "why": w}
                                for c, p, w in bad]},
                  fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    if bad:
        print(f"\n[FAIL] {len(bad)} madde eşleşmedi:")
        for cid, page, why in bad[:12]:
            print(f"         {cid} (dizin s.{page}) — {why}")
        return 1
    print(f"\n[  ok ] {len(checks)}/{len(checks)} madde: dizindeki numara "
          f"basılı sayfayla eşleşiyor")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
