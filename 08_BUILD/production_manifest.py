#!/usr/bin/env python3
"""
CODEX BESTIARIUM — ÜRETİM MANİFESTOSU (Faz 6)
================================================================================
Hangi yayın dosyası üretildi, kaç sayfa, kaç megabayt — DEPODA duran ölçü.

    NEDEN
    ─────
    `update_docs` Faz 6 ilerlemesini "üretilmiş yayın dosyası ailesi" diye
    sayıyor ve bunu DOSYA SİSTEMİNE bakarak yapıyordu. Üretilen PDF'ler
    `.gitignore`'dadır: yerelde 1/4, temiz klonda 0/4. Belge, üretildiği
    makineye göre değişiyor ve CI her push'ta haklı olarak "bayat" diyordu.

    Bu, projenin üçüncü kez aynı yerden aldığı yaradır:
      D38  manuscript ölçüsü  → `manuscript_metrics.json`
      D51  ön/arka madde      → `matter_measurement.json`
      D55  editör kopyası     → Faz 6 sayımından çıkarıldı
    Kural artık genel: DEPO VARLIĞI DEĞİL, ÖLÇÜSÜNÜ TAŞIR.

    Manifestonun TEK YAZARI bu betiktir. `update_docs` yalnızca okur.

NE İÇERMEZ
    Proza içermez. Yol, sayfa sayısı ve boyut taşır — hepsi ölçüm.

ÇIKIŞ KODLARI
    0  yazıldı / güncel        1  bayat (--check)        2  bağımlılık yok

KULLANIM
    python3 08_BUILD/production_manifest.py
    python3 08_BUILD/production_manifest.py --check
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ROOT  # noqa: E402

MANIFEST = os.path.join(ROOT, "01_SOURCE", "production.json")

# (aile, kök, uzantı, dışlanan alt dizin)
FAMILIES = [
    ("interior", "04_PRINT", ".pdf", {"PROOF", "proofs"}),
    ("cover", "03_COVER", ".pdf", {"artwork", "proofs"}),
    ("ebook", "05_KINDLE", ".epub", set()),
    ("docx", "02_MANUSCRIPT", ".docx", set()),
]


def page_count(path: str) -> int | None:
    """Sayfa sayısı PAGEMAP'ten okunur, PDF'ten değil.

    pypdf isteğe bağlı bir bağımlılıktır; sistem Python'unda yoktur. PDF'ten
    okunsaydı manifesto ÇALIŞTIRAN YORUMLAYICIYA göre değişirdi — venv ile
    sayfa sayılı, sistem Python'uyla sayısız. Bir ölçü dosyasının aracına
    göre değişmesi, düzeltmeye çalıştığımız kusurun ta kendisi olurdu.

    `pagemap.json` dizginin kendi çıktısıdır, depodadır ve deterministiktir.
    """
    pm = os.path.join(os.path.dirname(path), "pagemap.json")
    if not os.path.exists(pm):
        return None
    try:
        with open(pm, encoding="utf-8") as fh:
            return json.load(fh).get("_meta", {}).get("physicalPages")
    except (OSError, ValueError):
        return None


def scan() -> dict:
    from bestiarium import EDITOR_COPY_STEM

    out = {}
    for fam, root, ext, skip in FAMILIES:
        base = os.path.join(ROOT, root)
        items = []
        if os.path.isdir(base):
            for dirpath, dirnames, files in os.walk(base):
                dirnames[:] = [d for d in dirnames if d not in skip]
                for f in sorted(files):
                    if not f.lower().endswith(ext):
                        continue
                    # Editörün ÇALIŞMA kopyası bir yayın dosyası değildir
                    # (D55). Aynı ad tek doğruluk kaynağından gelir.
                    if f.startswith(EDITOR_COPY_STEM):
                        continue
                    full = os.path.join(dirpath, f)
                    rec = {
                        "path": os.path.relpath(full, ROOT),
                        "megabytes": round(os.path.getsize(full) / 1048576, 1),
                    }
                    if ext == ".pdf":
                        n = page_count(full)
                        if n:
                            rec["pages"] = n
                    items.append(rec)
        out[fam] = items
    return out


def payload() -> str:
    data = scan()
    return json.dumps({
        "note": "Üretilen yayın dosyalarının ÖLÇÜSÜ. Proza içermez "
                "(karar A1/D29). Üreten: 08_BUILD/production_manifest.py",
        "families": data,
        "familiesBuilt": sorted(k for k, v in data.items() if v),
        "familyCount": sum(1 for v in data.values() if v),
        "familyTotal": len(FAMILIES),
    }, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    want = payload()
    if args.check:
        # ÜRETİM ÇIKTISI OLMAYAN ORTAMDA DOĞRULANAMAZ. PDF ve EPUB
        # `.gitignore`'dadır; CI koşucusunda hiç bulunmazlar. Manifestoyu
        # boş bir taramayla karşılaştırmak, "dosya yok" ile "manifesto
        # bayat"ı aynı sinyale çevirirdi — çıkış 2 sözleşmesi.
        if not json.loads(want)["familyCount"]:
            print("ATLANDI: üretim çıktısı yok — manifesto doğrulanamaz")
            return 2
        if not os.path.exists(MANIFEST):
            print("BAYAT: 01_SOURCE/production.json yok")
            return 1
        with open(MANIFEST, encoding="utf-8") as fh:
            if fh.read() != want:
                print("BAYAT: 01_SOURCE/production.json — "
                      "python3 08_BUILD/production_manifest.py")
                return 1
        print("TAMAM: üretim manifestosu güncel.")
        return 0

    with open(MANIFEST, "w", encoding="utf-8") as fh:
        fh.write(want)
    data = json.loads(want)
    print("=" * 78)
    print("ÜRETİM MANİFESTOSU")
    print("=" * 78)
    for fam, items in data["families"].items():
        if not items:
            print(f"  {fam:<10} —")
            continue
        for it in items:
            pg = f"{it['pages']} s · " if "pages" in it else ""
            print(f"  {fam:<10} {pg}{it['megabytes']} MB  {it['path']}")
    print(f"\n  {data['familyCount']}/{data['familyTotal']} aile üretildi")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
