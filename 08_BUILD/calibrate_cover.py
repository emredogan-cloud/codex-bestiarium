"""
CİLTLİ KAPAK KALİBRASYONU — resmî KDP şablonundan ölçüm
================================================================================
NEDEN GEREKLİ?
--------------
KDP, ciltsiz kapak formülünü yayımlar ama **ciltli kapak formülünü yayımlamaz**;
"cover calculator and template generator" kullanmanızı söyler. Yayımladığı tek
tek ölçüler kendi içinde çelişkilidir ("0.51 inç (15 mm)" — 0.51 in = 12.95 mm)
ve üçüncü taraf kaynaklar üç farklı sarım payı verir (0.51 / 0.591 / 0.625).

Bu yüzden ciltli profil `editions.py` içinde `calibrated=False` işaretlidir ve
kapak `_PROVISIONAL` etiketiyle dışa aktarılır. Bu araç, resmî şablondan ölçüm
alıp `08_BUILD/kdp_calibration.json` yazar; o dosya varken profil `calibrated`
olur ve export adı `_KDP` olarak değişir.

ŞABLON NASIL ALINIR
-------------------
  1. https://kdp.amazon.com/cover-templates
  2. Binding: **Hardcover**  ·  Interior: **Black & white**
     Paper: **Cream**  ·  Trim: **6 x 9 in**  ·  Page count: **329**
  3. "Download template" → ZIP içinden PDF'i alın.
  4. python3 08_BUILD/calibrate_cover.py --template <indirilen>.pdf --spine 0.95

KULLANIM
--------
  # şablon PDF'inden otomatik (en/boy okunur, sırtı siz girersiniz)
  python3 08_BUILD/calibrate_cover.py --template kdp_hardcover_6x9_329.pdf \\
                                      --spine 0.9475

  # ya da doğrudan KDP hesaplayıcının gösterdiği üç sayıyla
  python3 08_BUILD/calibrate_cover.py --width 14.5 --height 10.25 --spine 0.9475

  # kalibrasyonu doğrula (yazmadan karşılaştır)
  python3 08_BUILD/calibrate_cover.py --verify

NE ÖLÇÜLÜR, NE VARSAYILIR
-------------------------
KESİN (şablondan): tam kapak genişliği, tam kapak yüksekliği, sırt genişliği.
Bunlar doğru olduğunda KDP dosyayı ÖLÇEKLEMEZ — kaymanın tek gerçek sebebi
budur.

VARSAYILAN (şablondan okunmaz): sarım payı ile menteşe oluğunun genişliği
arasındaki bölüşüm. Bu bölüşüm görsel olarak ETKİSİZDİR: sarım alanı kartonun
arkasına dolanıp iç kapağa yapıştığından görünmez, menteşe oluğu ise zaten
metinsiz bırakılır. Önemli olan toplamın doğru olmasıdır ve toplam ölçülür.
Menteşeyi ayrıca biliyorsanız `--hinge` ile verin.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editions as E    # noqa: E402
import cover_spec as S  # noqa: E402
import paths as P       # noqa: E402

OUT = S.CALIBRATION_FILE


def measure_barcode(path: str, cover_w: float, dpi: int = 300):
    """Şablondaki SARI barkod kutusunu ölçer → (x, y, w, h) inç.

    KDP'nin ciltlide barkodu nereye bastığı türetilebilir bir formülden gelmiyor
    (kesim altından 0.2583", kesim sağından 0.4459" — hiçbiri yuvarlak sayı
    değil). Şablon bunu sarı bir kutuyla açıkça gösterdiği için ölçülür.
    """
    import subprocess
    import tempfile
    import numpy as np
    from PIL import Image

    png = os.path.splitext(path)[0] + ".png"      # KDP indirmesi PNG de içerir
    src = png if os.path.exists(png) else None
    if src is None:
        tmp = tempfile.mkdtemp()
        base = os.path.join(tmp, "t")
        try:
            subprocess.run(["pdftoppm", "-r", str(dpi), "-png", path, base],
                           check=True, capture_output=True)
        except Exception as exc:
            print(f"  ! barkod ölçülemedi (pdftoppm): {exc}")
            return None
        cand = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
        src = os.path.join(tmp, cand[0]) if cand else None
    if not src:
        return None

    a = np.asarray(Image.open(src).convert("RGB")).astype(int)
    D = a.shape[1] / cover_w                       # px / inç (gerçek ölçekten)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    yellow = (r > 225) & (g > 225) & (b < 130)
    ys = np.where(yellow.sum(axis=1) > 20)[0]
    xs = np.where(yellow.sum(axis=0) > 20)[0]
    if not len(xs) or not len(ys):
        print("  ! şablonda sarı barkod kutusu bulunamadı")
        return None
    x1, x2 = xs[0] / D, (xs[-1] + 1) / D
    y1, y2 = ys[0] / D, (ys[-1] + 1) / D
    w, h = x2 - x1, y2 - y1
    if not (1.8 < w < 2.2 and 1.0 < h < 1.4):
        print(f"  ! ölçülen kutu beklenen 2.0x1.2 inç değil: "
              f"{w:.3f}x{h:.3f} — yok sayıldı")
        return None
    return (round(x1, 4), round(y1, 4), round(w, 4), round(h, 4))


def read_template(path: str) -> tuple:
    """Şablon PDF/PNG'sinden tam kapak ölçüsünü inç olarak okur."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        from pypdf import PdfReader
        pg = PdfReader(path).pages[0]
        w = float(pg.mediabox.width) / 72.0
        h = float(pg.mediabox.height) / 72.0
        return w, h, "PDF MediaBox"
    if ext in (".png", ".jpg", ".jpeg", ".tif", ".tiff"):
        from PIL import Image
        im = Image.open(path)
        dpi = im.info.get("dpi", (300, 300))[0] or 300
        return im.width / dpi, im.height / dpi, f"görsel @ {dpi} DPI"
    raise SystemExit(f"desteklenmeyen şablon biçimi: {ext}  (pdf/png bekleniyor)")


def solve(width: float, height: float, spine: float, ed, pages: int,
          hinge: float = None) -> dict:
    """Ölçülen üç sayıdan ciltleme profilini çözer."""
    base = E.BINDINGS[ed.binding]
    hinge = base.hinge if hinge is None else hinge

    # Sırt: sayfa bloğu + karton payı. Karton payı ölçümden geri çıkar.
    block = pages * E.PAPER_THICKNESS[ed.paper]
    spine_board = spine - block
    if spine_board < -1e-6:
        raise SystemExit(
            f"ölçülen sırt ({spine:.4f}\") sayfa bloğundan ({block:.4f}\") dar.\n"
            f"Sayfa sayısı veya kâğıt türü yanlış olabilir.")

    # Yükseklik: 2·dış + trim_h + karton_yükseklik_payı
    # Karton payını varsayılanda tutup dış payı ölçümden çözüyoruz.
    overhang_h = base.board_overhang_h
    outer_h = (height - ed.trim_h - overhang_h) / 2.0
    if outer_h <= 0:
        overhang_h = 0.0
        outer_h = (height - ed.trim_h) / 2.0

    # Genişlik: 2·dış + 2·kenar_payı + 2·trim_w + 2·menteşe + sırt
    leftover = width - 2 * ed.trim_w - spine - 2 * hinge
    if leftover < 0:
        raise SystemExit(
            f"ölçülen genişlik ({width:.4f}\") verilen menteşeyle "
            f"({hinge:.4f}\") tutarsız.\n--hinge değerini düşürün.")
    outer_w = leftover / 2.0

    # Dış pay yatay ve dikeyde eşit olmalı; farksa aradaki kadarı kenar payıdır.
    outer = min(outer_w, outer_h)
    overhang_w = outer_w - outer
    overhang_h += 2 * (outer_h - outer)

    return {
        "outer_pad": round(outer, 5),
        "hinge": round(hinge, 5),
        "spine_board": round(spine_board, 5),
        "board_overhang_h": round(overhang_h, 5),
        "board_overhang_w": round(overhang_w, 5),
        "source": f"KDP şablonu · {ed.trim_w:g}x{ed.trim_h:g} in · "
                  f"{pages} sayfa · {ed.paper}",
        "_measured": {"cover_w": round(width, 4), "cover_h": round(height, 4),
                      "spine_w": round(spine, 4), "pages": pages,
                      "paper": ed.paper},
    }


def verify(ed, pages: int) -> int:
    """Mevcut kalibrasyonu ölçülen değerlerle karşılaştırır."""
    cal = S.load_calibration().get(ed.binding)
    if not cal:
        print(f"kalibrasyon yok: {P.rel(OUT)}")
        print("→ ciltli kapak PROVISIONAL olarak üretiliyor.")
        return 1
    m = cal.get("_measured", {})
    g = S.geometry_for(ed, pages=pages)
    rows = [("tam kapak genişliği", m.get("cover_w"), g.cover_w),
            ("tam kapak yüksekliği", m.get("cover_h"), g.cover_h),
            ("sırt genişliği", m.get("spine_w"), g.spine_w)]
    br = cal.get("barcode_rect")
    if br:
        rows += [("barkod sol kenarı", br[0], g.barcode.x),
                 ("barkod üst kenarı", br[1], g.barcode.y)]
    bad = 0
    print(f"kaynak: {cal.get('source','?')}\n")
    print(f"  {'ölçüt':26s} {'şablon':>12s} {'motor':>12s}  {'fark':>10s}")
    print("  " + "-" * 64)
    for name, want, got in rows:
        if want is None:
            continue
        d = got - want
        ok = abs(d) <= 0.002
        bad += 0 if ok else 1
        print(f"  {name:26s} {want:12.4f} {got:12.4f}  "
              f"{d*25.4:+9.3f}mm  {'OK' if ok else 'SAPMA'}")
    if m.get("pages") and m["pages"] != pages:
        print(f"\n  ⚠ kalibrasyon {m['pages']} sayfa içindi, şimdiki {pages}.")
        print("    Sayfa sayısı değiştiyse yeni şablonla yeniden kalibre edin.")
        bad += 1
    print()
    print("SONUÇ:", "KALİBRASYON TUTARLI" if bad == 0 else f"{bad} SAPMA")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(
        description="Ciltli kapak profilini resmî KDP şablonundan kalibre eder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("ŞABLON NASIL ALINIR")[1])
    E.add_argument(ap)
    ap.add_argument("--template", help="KDP şablonu (PDF veya PNG)")
    ap.add_argument("--width", type=float, help="tam kapak genişliği, inç")
    ap.add_argument("--height", type=float, help="tam kapak yüksekliği, inç")
    ap.add_argument("--spine", type=float, help="sırt genişliği, inç")
    ap.add_argument("--hinge", type=float, default=None,
                    help="menteşe oluğu genişliği, inç (biliniyorsa)")
    ap.add_argument("--pages", type=int, default=None)
    ap.add_argument("--verify", action="store_true",
                    help="yazmadan mevcut kalibrasyonu doğrula")
    ap.add_argument("--reset", action="store_true",
                    help="kalibrasyonu sil (varsayılanlara dön)")
    a = ap.parse_args()

    ed = E.get(a.edition if a.edition != "paperback" else "hardcover")
    pages = a.pages or S.interior_pages(ed)

    if a.reset:
        if os.path.exists(OUT):
            os.remove(OUT)
            print(f"silindi: {P.rel(OUT)}")
        else:
            print("zaten kalibrasyon yok")
        return 0

    if a.verify:
        return verify(ed, pages)

    if a.template:
        w, h, how = read_template(a.template)
        print(f"şablon okundu ({how}): {w:.4f} x {h:.4f} inç")
    else:
        w, h = a.width, a.height
        how = "elle girilen ölçü"
    if not (w and h and a.spine):
        raise SystemExit(
            "eksik ölçü.\n"
            "  --template <dosya> --spine <inç>\n"
            "veya\n"
            "  --width <inç> --height <inç> --spine <inç>\n\n"
            "Üç sayı da KDP'nin kapak hesaplayıcısında görünür:\n"
            "  https://kdp.amazon.com/cover-templates")

    prof = solve(w, h, a.spine, ed, pages, a.hinge)

    if a.template:
        bc = measure_barcode(a.template, w)
        if bc:
            prof["barcode_rect"] = list(bc)
            print(f"\nbarkod kutusu ölçüldü: x {bc[0]:.4f}..{bc[0]+bc[2]:.4f}  "
                  f"y {bc[1]:.4f}..{bc[1]+bc[3]:.4f}  "
                  f"({bc[2]:.3f} × {bc[3]:.3f} inç)")
    data = S.load_calibration()
    data[ed.binding] = prof
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nçözülen profil ({ed.profile.label}):")
    for k in ("outer_pad", "hinge", "spine_board",
              "board_overhang_h", "board_overhang_w"):
        base = getattr(E.BINDINGS[ed.binding], k)
        print(f"  {k:20s} {prof[k]:9.5f} in   (varsayılan {base:.5f}, "
              f"fark {(prof[k]-base)*25.4:+.2f} mm)")
    print(f"\n→ {P.rel(OUT)}")

    g = S.geometry_for(ed, pages=pages)
    print(f"\nkalibre edilmiş geometri:")
    print(f"  tam kapak : {g.cover_w:.4f} x {g.cover_h:.4f} in  "
          f"(şablon {w:.4f} x {h:.4f})")
    print(f"  sırt      : {g.spine_w:.4f} in  (şablon {a.spine:.4f})")
    print(f"  kalibre   : {g.calibrated}")
    print("\nşimdi: ./08_BUILD/build_hardcover.sh")
    return 0


if __name__ == "__main__":
    sys.exit(main())
