"""
CODEX MYTHOLOGICA — DOSYA YOLLARI
================================================================================
Bütün betikler çıktı yollarını buradan alır. Tek bir yerde tanımlı olması,
klasör yapısının değişmesi hâlinde 12 betiği tek tek düzenleme ihtiyacını
ortadan kaldırır.

KLASÖR YAPISI
-------------
    03_COVER/
      artwork/                     PAYLAŞILAN kaynak sanat (metinsiz)
      <SÜRÜM>/plates/              tuvale oturtulmuş 300 DPI plaka
      <SÜRÜM>/typography/          çözülmüş metin kutuları (json + md)
      <SÜRÜM>/templates/           düzenlenebilir SVG ana kaynak + kılavuz
      <SÜRÜM>/exports/             ★ KDP'YE YÜKLENECEK kapak PDF'i
      <SÜRÜM>/proofs/              kılavuz çizgili kontrol kopyası
    04_PRINT/
      <SÜRÜM>/                     ★ KDP'YE YÜKLENECEK iç blok PDF'i
    06_REPORTS/
      <SÜRÜM>/                     doğrulama json + HTML rapor
      *.html                       sürümler arası paylaşılan raporlar
    07_ASSETS/
      fonts/                       PAYLAŞILAN — her sürüm aynı yüzleri kullanır

Sürüm klasörü adı = Edition.slug  (PAPERBACK · HARDCOVER · LARGEPRINT)
"""

from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "08_BUILD")

# --- paylaşılan ---
ART_SRC_DIR = os.path.join(ROOT, "03_COVER", "artwork")
FONT_DIR = os.path.join(ROOT, "07_ASSETS", "fonts")
REPORT_DIR = os.path.join(ROOT, "06_REPORTS")
SOURCE_DIR = os.path.join(ROOT, "01_SOURCE")

BOOK_SLUG = "CODEX_MYTHOLOGICA"


def _mk(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path


def cover_dir(ed, sub: str = "") -> str:
    """03_COVER/<SÜRÜM>/<sub>"""
    p = os.path.join(ROOT, "03_COVER", ed.slug, sub) if sub \
        else os.path.join(ROOT, "03_COVER", ed.slug)
    return _mk(p)


def print_dir(ed) -> str:
    """04_PRINT/<SÜRÜM>"""
    return _mk(os.path.join(ROOT, "04_PRINT", ed.slug))


def report_dir(ed=None) -> str:
    """06_REPORTS[/<SÜRÜM>]"""
    return _mk(os.path.join(REPORT_DIR, ed.slug) if ed else REPORT_DIR)


# ---------------------------------------------------------------- dosya adları

def interior_pdf(ed) -> str:
    return os.path.join(print_dir(ed),
                        f"{BOOK_SLUG}_INTERIOR_{ed.slug}.pdf")


def cover_pdf(ed, paper: str, provisional: bool = False) -> str:
    tag = "PROVISIONAL" if provisional else "KDP"
    return os.path.join(cover_dir(ed, "exports"),
                        f"{BOOK_SLUG}_COVER_{ed.slug}_{paper}_{tag}.pdf")


def cover_proof_pdf(ed, paper: str) -> str:
    return os.path.join(cover_dir(ed, "proofs"),
                        f"{BOOK_SLUG}_COVER_{ed.slug}_{paper}_PROOF.pdf")


def cover_plate(ed, paper: str, dpi: int = 300) -> str:
    return os.path.join(cover_dir(ed, "plates"),
                        f"cover-plate-{paper}-{dpi}dpi.png")


def typography_spec(ed, paper: str, ext: str = "json") -> str:
    return os.path.join(cover_dir(ed, "typography"),
                        f"typography-spec-{paper}.{ext}")


def validation_json(ed, kind: str, paper: str = None) -> str:
    """kind: cover | interior"""
    name = f"{kind}-validation" + (f"-{paper}" if paper else "") + ".json"
    return os.path.join(report_dir(ed), name)


def edition_report_html(ed) -> str:
    return os.path.join(report_dir(ed), f"{ed.slug}_PRODUCTION_REPORT.html")


def build_log(ed) -> str:
    return os.path.join(report_dir(ed), "build.log")


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, BUILD)
    import editions as E

    print(f"ROOT = {ROOT}\n")
    for k in E.ORDER:
        ed = E.get(k)
        print(f"── {ed.label} ({ed.slug})")
        print(f"   iç blok   : {rel(interior_pdf(ed))}")
        print(f"   kapak     : {rel(cover_pdf(ed, ed.paper))}")
        print(f"   prova     : {rel(cover_proof_pdf(ed, ed.paper))}")
        print(f"   plaka     : {rel(cover_plate(ed, ed.paper))}")
        print(f"   tipografi : {rel(typography_spec(ed, ed.paper))}")
        print(f"   rapor     : {rel(edition_report_html(ed))}")
        print()
