#!/usr/bin/env python3
"""
CODEX BESTIARIUM — KIN-IMAGES CHART
================================================================================
Yol haritası Faz 4, çıktı #6: *"Kin-Images Chart taslağı — okur mıknatısı"*
(`03_APLUS/kin-images-chart.pdf`), aynı zamanda A+ içerik modülü **m3**.

    NE İŞE YARAR
    ────────────
    Kitabın tezi tek bir sayfada görülebilir olmalıdır: SEKİZ imge, KIRK
    gelenek, ve her ailenin ayrıştığı yer. Bir okur mıknatısı olarak
    kitaptan bağımsız dolaşır; A+ modülü olarak ürün sayfasında durur.

    TÜRETİLİR, YAZILMAZ
    ───────────────────
    `spec.json` + `kin_map.json`. Aile üyeliği, manşet kadro, motif kodu ve
    AYRIŞMA CÜMLESİ orada kilitlidir (Faz 2). Burada tek bir editoryal
    cümle yoktur; değişecek her şey kaynakta değişir.

    PLAKA YERİ BOŞ BIRAKILIR — VE BU BİR KUSUR DEĞİL
    ────────────────────────────────────────────────
    Ham AI plaka üretimi kurucunun sorumluluğundadır ve Faz 5'ten önce
    tamamlanacaktır (karar D39). Grafik o girdiyi BEKLEYECEK biçimde
    kuruldu: her üye için doğru ölçekte bir çerçeve çizilir ve içine plaka
    kimliği yazılır. Plakalar geldiğinde aynı komut çerçeveleri doldurur;
    yerleşim, ölçek ve sayfa sayısı değişmez.

    Bu, Faz 2'nin `convert_plates --calibrate` kararıyla aynı disiplindir:
    HAT PLAKA GELMEDEN ÖLÇÜLÜR VE SINANIR.

KULLANIM
    python3 08_BUILD/make_kin_chart.py            # PDF üret
    python3 08_BUILD/make_kin_chart.py --check    # üretmeden denetle
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    KIN_IDS,
    PLATES_DIR,
    REPORT_DIR,
    ROOT,
    SOURCE_DIR,
    Result,
    load_spec,
)

OUT_PDF = os.path.join(ROOT, "03_APLUS", "kin-images-chart.pdf")
OUT_JSON = os.path.join(REPORT_DIR, "kin-images-chart.json")
KIN_MAP_PATH = os.path.join(SOURCE_DIR, "kin_map.json")

# Sayfa: A+ modülü ve okur mıknatısı aynı dosyayı paylaşır, bu yüzden
# ekranda okunan bir oran seçildi (US Letter). Kitabın 6×9 trim'i DEĞİL:
# bu artefakt kitabın içine girmez.
PAGE_W, PAGE_H = 612.0, 792.0
MARGIN = 42.0
PLATE_W = 58.0
PLATE_H = PLATE_W * 1.25          # şartname oranı 1:1,25 (PLATE_SPEC)

# Font adları hattın geri kalanıyla AYNI: `make_pdf` içe aktarıldığında
# reportlab'e kaydedilirler. İkinci bir kayıt yolu, ikinci bir gömme
# davranışı demektir (PROJECT_CONTEXT § 8, reportlab tuzağı 3).
FONT_HEAD = "Cinzel"
FONT_BODY = "Gara"


def _require_reportlab():
    try:
        import reportlab  # noqa: F401
    except ImportError:
        raise SystemExit(
            "HATA: Kin-Images Chart şunu gerektirir: reportlab\n"
            "      ./08_BUILD/bootstrap.sh çalıştırın."
        )


def load_map() -> dict:
    with open(KIN_MAP_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def collect(spec: dict, km: dict) -> list[dict]:
    """Aileler → çizilecek satırlar. Editoryal içerik KAYNAKTAN gelir."""
    byid = {c["id"]: c for c in spec["creatures"]}
    trads = {t["id"]: t for t in spec["traditions"]}
    fams = {f["id"]: f for f in spec["kinFamilies"]}

    rows = []
    for fid in KIN_IDS:
        fam = fams[fid]
        src = km["families"][fid]
        headline = [byid[i] for i in src["headline"]]
        rows.append({
            "id": fid,
            # Okur mıknatısı KİTABIN DİLİNDE basılır. `image` alanı Türkçedir
            # ve proje belgelerine aittir; okura giden ad `en`dir.
            "image": fam["en"],
            "motif": fam["motif"],
            "divergence": fam["divergenceEn"],
            "memberCount": fam["memberCount"],
            "extended": [byid[i]["name"] for i in fam.get("extended", [])],
            "headline": [
                {
                    "id": c["id"],
                    "name": c["name"],
                    "tradition": trads[c["tradition"]]["name"],
                    "sigil": trads[c["tradition"]].get("sigil", ""),
                    "class": c["class"],
                    "plate": c.get("plate", ""),
                    "plateFile": os.path.join(PLATES_DIR, f"{c.get('plate','')}.png"),
                }
                for c in headline
            ],
        })
    return rows


def build(rows: list[dict], out_path: str) -> dict:
    _require_reportlab()
    from reportlab.pdfgen import canvas as rl_canvas

    # Fontları KAYDEDEN yer burası değil: `make_pdf` içe aktarıldığında
    # kaydediyor ve gömme davranışı orada sınanmış durumda.
    import make_pdf  # noqa: F401

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    c = rl_canvas.Canvas(out_path, pagesize=(PAGE_W, PAGE_H))
    c.setTitle("Codex Bestiarium — Kin-Images Chart")
    c.setAuthor("Emre Doğan · Vâliçe Press")

    plates_present = 0
    pages = 0
    y = 0.0

    def new_page(first: bool = False) -> float:
        nonlocal pages
        if not first:
            c.showPage()
        pages += 1
        c.setFillColor("#111111")
        c.setFont(FONT_HEAD, 17)
        c.drawString(MARGIN, PAGE_H - MARGIN - 12, "CODEX BESTIARIUM")
        c.setFont(FONT_BODY, 10.5)
        c.drawString(MARGIN, PAGE_H - MARGIN - 28,
                     "The Kin-Images: eight fears, forty traditions, "
                     "one page.")
        c.setStrokeColor("#B08D3F")
        c.setLineWidth(0.6)
        c.line(MARGIN, PAGE_H - MARGIN - 36, PAGE_W - MARGIN,
               PAGE_H - MARGIN - 36)
        return PAGE_H - MARGIN - 58

    y = new_page(first=True)

    for row in rows:
        need = 34 + PLATE_H + 46
        if y - need < MARGIN + 26:
            y = new_page()

        c.setFillColor("#111111")
        c.setFont(FONT_HEAD, 12)
        c.drawString(MARGIN, y, f"{row['id']} · {row['image'].upper()}")
        c.setFont(FONT_BODY, 8.5)
        c.setFillColor("#666666")
        c.drawRightString(PAGE_W - MARGIN, y,
                          f"Thompson {row['motif']} · {row['memberCount']} members")
        y -= 14

        # Plaka şeridi — çerçeveler ŞİMDİ, görseller D39 geldiğinde.
        x = MARGIN
        span = (PAGE_W - 2 * MARGIN)
        step = span / max(len(row["headline"]), 1)
        step = min(step, PLATE_W + 12)
        for m in row["headline"]:
            top = y - PLATE_H
            if os.path.exists(m["plateFile"]):
                c.drawImage(m["plateFile"], x, top, PLATE_W, PLATE_H,
                            preserveAspectRatio=True, anchor="c", mask="auto")
                plates_present += 1
            else:
                c.setStrokeColor("#CCCCCC")
                c.setLineWidth(0.5)
                c.rect(x, top, PLATE_W, PLATE_H)
                c.setFillColor("#AAAAAA")
                c.setFont(FONT_BODY, 6)
                c.drawCentredString(x + PLATE_W / 2, top + PLATE_H / 2 - 2,
                                    m["plate"])
            c.setFillColor("#111111")
            c.setFont(FONT_BODY, 7.5)
            c.drawString(x, top - 9, m["name"][:15])
            c.setFillColor("#777777")
            c.setFont(FONT_BODY, 6.5)
            c.drawString(x, top - 17, f"{m['tradition'][:13]} · {m['class']}")
            x += step
        y -= PLATE_H + 24

        # Ayrışma cümlesi — ailenin TEZİ. kin_map.json'dan, elle yazılmaz.
        c.setFillColor("#333333")
        c.setFont(FONT_BODY, 8.5)
        for line in _wrap(row["divergence"], PAGE_W - 2 * MARGIN, 8.5, c):
            c.drawString(MARGIN, y, line)
            y -= 11
        if row["extended"]:
            c.setFillColor("#888888")
            c.setFont(FONT_BODY, 7.5)
            tail = "also in this family: " + ", ".join(row["extended"])
            for line in _wrap(tail, PAGE_W - 2 * MARGIN, 7.5, c):
                c.drawString(MARGIN, y, line)
                y -= 10
        y -= 14

    c.setFillColor("#999999")
    c.setFont(FONT_BODY, 7)
    c.drawString(MARGIN, MARGIN - 12,
                 "Derived from 01_SOURCE/spec.json and kin_map.json. "
                 "Plate frames are filled when the illustrations arrive.")
    c.showPage()
    c.save()

    return {"pages": pages, "families": len(rows), "platesPresent": plates_present,
            "platesExpected": sum(len(r["headline"]) for r in rows),
            "file": os.path.relpath(out_path, ROOT)}


def _wrap(text: str, width: float, size: float, c) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if c.stringWidth(trial, FONT_BODY, size) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="üretmeden kaynak bütünlüğünü denetle")
    ap.add_argument("--out", default=OUT_PDF)
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    spec = load_spec()
    rows = collect(spec, load_map())

    r = Result("KIN-IMAGES CHART (make_kin_chart)")
    r.add(len(rows) == len(KIN_IDS), f"{len(KIN_IDS)} aile toplandı",
          f"{len(rows)}")
    empty = [x["id"] for x in rows if not x["divergence"].strip()]
    r.add(not empty, "her ailenin ayrışma cümlesi var", f"{empty}")
    thin = [x["id"] for x in rows if not x["headline"]]
    r.add(not thin, "her ailenin manşet kadrosu var", f"{thin}")

    if args.check:
        code = r.report(verbose=args.verbose)
        print("not: --check üretmez; PDF için argümansız çalıştırın.")
        return code

    try:
        _require_reportlab()
    except SystemExit as exc:
        print(exc)
        return 2

    m = build(rows, args.out)
    r.ok("grafik üretildi", f"{m['pages']} sayfa · {m['file']}")
    r.add(
        True,
        "plaka çerçeveleri",
        f"{m['platesPresent']}/{m['platesExpected']} dolu — "
        "kalanı ham AI çıktısı geldiğinde dolar (karar D39)",
    )
    code = r.report(verbose=args.verbose)
    os.makedirs(REPORT_DIR, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(m, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"rapor: {os.path.relpath(OUT_JSON, ROOT)}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
