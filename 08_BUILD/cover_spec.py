"""
CODEX MYTHOLOGICA — KAPAK GEOMETRİSİ  (ciltsiz · ciltli · büyük punto)
================================================================================
Bu dosya, kapak boru hattının TEK doğruluk kaynağıdır.
Hiçbir koordinat elle yazılmaz; hepsi buradan türetilir.

Ölçü birimi: inç. PDF'e yazarken 72 ile çarpılıp punto'ya çevrilir.

--------------------------------------------------------------------------------
TEK MOTOR, İKİ CİLTLEME
--------------------------------------------------------------------------------
Ciltsiz ve ciltli kapak AYNI formülden çıkar; fark yalnızca `BindingProfile`
sayılarındadır (editions.py). Bu sayede:

    ciltsiz : dış pay = taşma 0.125"        · menteşe yok   · sırt = s×t
    ciltli  : dış pay = sarım  0.5906"      · menteşe var   · sırt = s×t + karton

    tuval genişliği = 2·dış + 2·kenar_payı + 2·trim + 2·menteşe + sırt
    tuval yüksekliği = 2·dış + trim + karton_yükseklik_payı

Ciltsizde menteşe ve karton payları sıfırdır; formül eski davranışa BİREBİR
indirgenir (regression testiyle kanıtlanır: `python3 cover_spec.py --selftest`).

--------------------------------------------------------------------------------
⚠ CİLTLİ KALİBRASYONU
--------------------------------------------------------------------------------
KDP ciltli kapak formülünü yayımlamaz. Varsayılan sayılar editions.py içinde
gerekçeleriyle durur ve `calibrated=False` işaretlidir. Resmî şablondan ölçüm:

    python3 08_BUILD/calibrate_cover.py --template <sablon.png> --pages 329

Kalibrasyon 08_BUILD/kdp_calibration.json dosyasına yazılır ve buradaki
varsayılanları EZER.

--------------------------------------------------------------------------------
KAYNAKLAR (DOĞRULANMIŞ — Amazon KDP resmî yardım sayfaları)
--------------------------------------------------------------------------------
  * Kâğıt kalınlığı, sırt, taşma : "Create a Paperback Cover" (G201953020)
  * Ciltli sarım/menteşe/güvenli : "Create a Hardcover Cover" (GDTKFJPNQCBTMRV6)
  * Barkod 2 x 1.2 inç           : "Barcodes" (G5HDYGP4BXLX4RUW)
  * Çözünürlük >= 300 DPI        : KDP kapak yönergeleri
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass, asdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editions as E  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALIBRATION_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "kdp_calibration.json")

# =============================================================================
# 1. KİTABIN ÖLÇÜLEN GERÇEKLERİ  (varsayım değil — dosyadan okundu)
# =============================================================================

# `pdfinfo 04_PRINT/PAPERBACK/..._INTERIOR.pdf` çıktısıyla doğrulandı.
PAGE_COUNT = 329
TRIM_W = 6.0
TRIM_H = 9.0
PAPER = "cream"
BINDING = "paperback"

# =============================================================================
# 2. KDP SABİTLERİ  (geriye dönük uyumluluk için modül düzeyinde de durur)
# =============================================================================

PAPER_THICKNESS = E.PAPER_THICKNESS

BLEED = E.PAPERBACK_PROFILE.outer_pad          # 0.125
SAFE = E.PAPERBACK_PROFILE.safe                # 0.25
SPINE_TEXT_SAFE = E.PAPERBACK_PROFILE.spine_text_safe

BARCODE_W = 2.0
BARCODE_H = 1.2
BARCODE_CLEAR = 0.25

MIN_SPINE_TEXT_PAGES = 79   # KDP sırta metin için asgari sayfa sayısı
DPI = 300


# =============================================================================
# 3. KALİBRASYON
# =============================================================================

def load_calibration() -> dict:
    """Resmî KDP şablonundan ölçülmüş düzeltmeleri okur (varsa)."""
    if not os.path.exists(CALIBRATION_FILE):
        return {}
    try:
        with open(CALIBRATION_FILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:            # bozuk dosya sessizce yutulmaz
        raise SystemExit(f"kalibrasyon dosyası okunamadı: {CALIBRATION_FILE}\n{exc}")


def binding_profile(binding: str) -> E.BindingProfile:
    """Profili döndürür; kalibrasyon dosyası varsa üzerine uygular."""
    base = E.BINDINGS[binding]
    cal = load_calibration().get(binding)
    if not cal:
        return base
    fields = {k: v for k, v in cal.items()
              if k in base.__dataclass_fields__ and k not in ("key", "label")}
    if isinstance(fields.get("barcode_rect"), list):
        fields["barcode_rect"] = tuple(fields["barcode_rect"])
    fields["calibrated"] = True
    fields.setdefault("source", cal.get("source", "kdp_calibration.json"))
    return E.BindingProfile(**{**asdict(base), **fields})


# =============================================================================
# 4. TÜRETİLMİŞ GEOMETRİ
# =============================================================================

def _r(x: float, n: int = 4) -> float:
    return round(x + 0.0, n)


@dataclass(frozen=True)
class Rect:
    """Sol-üst köşe (x, y) + genişlik/yükseklik. Origin = tuvalin sol ÜST köşesi."""
    x: float
    y: float
    w: float
    h: float

    @property
    def x2(self) -> float: return self.x + self.w
    @property
    def y2(self) -> float: return self.y + self.h
    @property
    def cx(self) -> float: return self.x + self.w / 2
    @property
    def cy(self) -> float: return self.y + self.h / 2

    def inset(self, d: float) -> "Rect":
        return Rect(self.x + d, self.y + d, self.w - 2 * d, self.h - 2 * d)

    def as_dict(self):
        return {k: _r(v) for k, v in asdict(self).items()}


@dataclass(frozen=True)
class CoverGeometry:
    binding: str
    paper: str
    page_count: int
    trim_w: float
    trim_h: float
    spine_w: float
    cover_w: float
    cover_h: float
    canvas_px: tuple
    back: Rect            # arka kapak — kesim ölçüsünde
    spine: Rect           # sırt — kesim ölçüsünde
    front: Rect           # ön kapak — kesim ölçüsünde
    hinge_back: Rect      # menteşe oluğu (ciltside genişliği > 0)
    hinge_front: Rect
    back_safe: Rect
    front_safe: Rect
    spine_safe: Rect
    barcode: Rect
    barcode_mirror: Rect
    trim: Rect            # kitap bloğunun tuvaldeki dikdörtgeni
    profile: E.BindingProfile
    calibrated: bool

    @property
    def is_hardcover(self) -> bool:
        return self.binding == "hardcover"


def geometry(paper: str = PAPER, pages: int = PAGE_COUNT,
             trim_w: float = TRIM_W, trim_h: float = TRIM_H,
             dpi: int = DPI, binding: str = BINDING) -> CoverGeometry:
    """Tüm kapak geometrisini ciltleme + sayfa sayısı + kâğıttan hesaplar."""
    if paper not in E.PAPER_THICKNESS:
        raise ValueError(f"bilinmeyen kâğıt: {paper}")
    if binding not in E.BINDINGS:
        raise ValueError(f"bilinmeyen ciltleme: {binding}")

    P = binding_profile(binding)
    if not (P.min_pages <= pages <= P.max_pages):
        raise SystemExit(
            f"{P.label}: {pages} sayfa, KDP sınırı {P.min_pages}–{P.max_pages}.\n"
            f"Bu ciltleme bu kalınlıkta üretilemez.")

    # --- sırt ---
    spine_w = pages * E.PAPER_THICKNESS[paper] + P.spine_board

    # --- tuval ---
    cover_w = (2 * P.outer_pad + 2 * P.board_overhang_w
               + 2 * trim_w + 2 * P.hinge + spine_w)
    cover_h = 2 * P.outer_pad + trim_h + P.board_overhang_h

    # --- paneller (soldan sağa) ---
    bx = P.outer_pad + P.board_overhang_w
    by = P.outer_pad + P.board_overhang_h / 2

    back = Rect(bx, by, trim_w, trim_h)
    hinge_back = Rect(back.x2, by, P.hinge, trim_h)
    spine = Rect(hinge_back.x2, by, spine_w, trim_h)
    hinge_front = Rect(spine.x2, by, P.hinge, trim_h)
    front = Rect(hinge_front.x2, by, trim_w, trim_h)
    trim = Rect(back.x, by, front.x2 - back.x, trim_h)

    # --- güvenli alanlar ---
    # Dış üç kenar profilin `safe` payı kadar içeride; sırta bakan kenar ise
    # `spine_safe` kadar SIRTIN kenarından içeride. Ciltsizde ikisi de 0.25
    # olduğu için formül eski davranışa birebir indirgenir.
    back_safe = Rect(back.x + P.safe, back.y + P.safe,
                     (spine.x - P.spine_safe) - (back.x + P.safe),
                     trim_h - 2 * P.safe)
    front_safe = Rect(spine.x2 + P.spine_safe, front.y + P.safe,
                      (front.x2 - P.safe) - (spine.x2 + P.spine_safe),
                      trim_h - 2 * P.safe)
    spine_safe = Rect(spine.x + P.spine_text_safe, spine.y + P.safe,
                      spine.w - 2 * P.spine_text_safe, spine.h - 2 * P.safe)

    # --- barkod ---
    # KDP kutuyu arka kapağın alt-sağ köşesine basar; oraya hiçbir şey konmamalı.
    # Ciltside konum türetilebilir bir formülden gelmiyor; kalibrasyon dosyası
    # şablondan ÖLÇÜLMÜŞ dikdörtgeni taşıyorsa o kullanılır.
    if P.barcode_rect:
        bx_, by_, bw_, bh_ = P.barcode_rect
        barcode = Rect(bx_, by_, bw_, bh_)
    else:
        barcode = Rect(spine.x - P.barcode_spine_clear - BARCODE_W,
                       back.y2 - P.barcode_bottom_clear - BARCODE_H,
                       BARCODE_W, BARCODE_H)
    # İhtiyaten alt-SOL köşe de boş bırakılır (KDP yerleşim algoritması
    # belgelenmemiş; iki köşeyi de boş tutmak sıfır maliyetli).
    # Ayna kutu, ölçülen/türetilen kutunun arka kapak merkezine göre yansımasıdır.
    barcode_mirror = Rect(2 * back.cx - barcode.x2, barcode.y,
                          barcode.w, barcode.h)

    return CoverGeometry(
        binding=binding, paper=paper, page_count=pages,
        trim_w=trim_w, trim_h=trim_h,
        spine_w=_r(spine_w), cover_w=_r(cover_w), cover_h=_r(cover_h),
        canvas_px=(int(round(cover_w * dpi)), int(round(cover_h * dpi))),
        back=back, spine=spine, front=front,
        hinge_back=hinge_back, hinge_front=hinge_front,
        back_safe=back_safe, front_safe=front_safe, spine_safe=spine_safe,
        barcode=barcode, barcode_mirror=barcode_mirror, trim=trim,
        profile=P, calibrated=P.calibrated,
    )


def interior_pages(edition) -> int:
    """Bu sürümün ÜRETİLMİŞ iç bloğundaki sayfa sayısını okur.

    Sırt genişliği sayfa sayısından çıkar. Sayfa sayısını elle yazmak veya bir
    sürümden diğerine taşımak, bu projenin daha önce yaşadığı sırt kayması
    hatasının tam olarak kaynağıdır. Bu yüzden kapak, SARDIĞI DOSYADAN okur —
    başka hiçbir yerden.
    """
    import paths as P
    from pypdf import PdfReader
    pdf = P.interior_pdf(edition)
    if not os.path.exists(pdf):
        raise SystemExit(
            f"iç blok yok: {P.rel(pdf)}\n"
            f"kapak, sardığı iç bloktan sayfa sayısını okur.\n"
            f"önce: python3 08_BUILD/make_pdf.py --edition {edition.key}")
    return len(PdfReader(pdf).pages)


def geometry_for(edition, paper: str = None, pages: int = None,
                 dpi: int = DPI) -> CoverGeometry:
    """editions.Edition nesnesinden doğrudan geometri.

    `pages` verilmezse sürümün üretilmiş iç bloğundan OKUNUR.
    """
    return geometry(paper=paper or edition.paper,
                    pages=pages if pages is not None else interior_pages(edition),
                    trim_w=edition.trim_w, trim_h=edition.trim_h,
                    dpi=dpi, binding=edition.binding)


# =============================================================================
# 5. GÖRSELİN TUVALE YERLEŞİMİ
# =============================================================================
#
# Sanat eseri DEĞİŞTİRİLMEZ. Yalnızca ÖLÇEKLENİR ve KONUMLANIR.
#
# GPT Image çıktısında sırt, iki altın filetoyla çerçevelenmiş dar bir bant
# olarak çizilmiş. Bant piksel analiziyle ölçüldü (audit_cover.py):
#   sol fileto x=683 px · sağ fileto x=733 px · bant merkezi x=708 px
#
# Bant gerçek sırttan DAHA DAR; filetolar katlama çizgisi olarak KULLANILAMAZ.
# Kural: bandın MERKEZİ sırtın MERKEZİNE oturur, ölçek iki eksende AYNIDIR.

ART_FILE = "03_COVER/artwork/paperback-artwork-textless.png"
ART_W, ART_H = 1472, 1069
ART_SPINE_CENTER_FRAC = 708 / 1472
ART_RULE_L_FRAC = 683 / 1472
ART_RULE_R_FRAC = 733 / 1472


@dataclass(frozen=True)
class ArtPlacement:
    scale: float
    offset_x: float
    offset_y: float
    scaled_w: float
    scaled_h: float
    crop_left: float
    crop_right: float
    crop_top: float
    crop_bottom: float
    rule_l_in: float
    rule_r_in: float
    rule_inset_in: float
    native_ppi: float


def art_placement(g: CoverGeometry, dpi: int = DPI) -> ArtPlacement:
    """Görseli, sırt bandı sırtla hizalanacak ve tuval tamamen dolacak
    şekilde ölçekler. Ölçek her iki eksende eşittir — KAYMANIN kökü buydu."""
    CW, CH = g.canvas_px
    # Sırt merkezi = TUVAL merkezi. Her iki ciltlemede de tuval simetriktir
    # (sol ve sağ paneller aynı genişlikte), bu yüzden CW/2 sırt merkezidir.
    # YUVARLANMIŞ piksel genişliği kullanılır: yayımlanmış ciltsiz kapak bu
    # değerle üretildi ve baskı provasından geçti. Geometrik merkez (spine.cx)
    # yarım pikselden küçük bir farkla ayrışır; regresyonu bozmamak için
    # piksel merkezi korunur.
    assert abs((g.spine.cx * dpi) - CW / 2.0) < 1.0, "tuval simetrik değil"
    cx = CW / 2.0
    a_cx = ART_SPINE_CENTER_FRAC * ART_W

    # Üç kısıt: (1) tuvali dikey kapla, (2) solu kapla, (3) sağı kapla
    s_h = CH / ART_H
    s_left = cx / a_cx
    s_right = (CW - cx) / (ART_W - a_cx)
    scale = max(s_h, s_left, s_right)

    off_x = cx - a_cx * scale
    sw, sh = ART_W * scale, ART_H * scale
    off_y = (CH - sh) / 2.0

    rl = (off_x + ART_RULE_L_FRAC * ART_W * scale) / dpi
    rr = (off_x + ART_RULE_R_FRAC * ART_W * scale) / dpi

    return ArtPlacement(
        scale=_r(scale, 6), offset_x=_r(off_x, 2), offset_y=_r(off_y, 2),
        scaled_w=_r(sw, 2), scaled_h=_r(sh, 2),
        crop_left=_r(-off_x, 2), crop_right=_r(sw + off_x - CW, 2),
        crop_top=_r(-off_y, 2), crop_bottom=_r(sh + off_y - CH, 2),
        rule_l_in=_r(rl), rule_r_in=_r(rr),
        rule_inset_in=_r(rl - g.spine.x),
        native_ppi=_r(ART_W / g.cover_w, 1),
    )


# =============================================================================
# 6. RENKLER  (mevcut sanat yönünden örneklendi — yeniden tasarım yok)
# =============================================================================

GOLD = "#C9A227"
GOLD_LIGHT = "#E3C766"
PARCHMENT = "#E8E0CE"
DIM = "#B9AE95"


# =============================================================================
# 7. DÖKÜM + KENDİ KENDİNİ TEST
# =============================================================================

def dump(path: str = None, binding: str = BINDING, paper: str = PAPER,
         pages: int = PAGE_COUNT) -> dict:
    g = geometry(paper=paper, pages=pages, binding=binding)
    p = art_placement(g)
    d = {
        "book": {"page_count": pages, "trim_w": TRIM_W, "trim_h": TRIM_H,
                 "paper": paper, "binding": binding,
                 "paper_thickness_in_per_page": E.PAPER_THICKNESS[paper]},
        "binding_profile": asdict(g.profile),
        "calibrated": g.calibrated,
        "kdp_constants": {"barcode_w": BARCODE_W, "barcode_h": BARCODE_H,
                          "dpi": DPI},
        "geometry": {
            "spine_w": g.spine_w, "cover_w": g.cover_w, "cover_h": g.cover_h,
            "canvas_px": list(g.canvas_px),
            "back": g.back.as_dict(), "spine": g.spine.as_dict(),
            "front": g.front.as_dict(), "trim": g.trim.as_dict(),
            "hinge_back": g.hinge_back.as_dict(),
            "hinge_front": g.hinge_front.as_dict(),
            "back_safe": g.back_safe.as_dict(),
            "front_safe": g.front_safe.as_dict(),
            "spine_safe": g.spine_safe.as_dict(),
            "barcode": g.barcode.as_dict(),
            "barcode_mirror": g.barcode_mirror.as_dict(),
        },
        "art_placement": asdict(p),
        "colors": {"gold": GOLD, "gold_light": GOLD_LIGHT,
                   "parchment": PARCHMENT, "dim": DIM},
    }
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
    return d


# Yayımlanmış ciltsiz kapağın ÖLÇÜLEN değerleri. Bu sayılar 39/39 doğrulamadan
# ve basılı provadan geçti; motor genelleştirilirken DEĞİŞMEMELİDİR.
_PAPERBACK_GOLDEN = {
    "cream": dict(spine_w=0.8225, cover_w=13.0725, cover_h=9.25,
                  canvas=(3922, 2775), spine_x=6.125, spine_x2=6.9475,
                  front_x=6.9475, art_scale=2.769774,
                  rule_l=6.3059, rule_r=6.7675),
    # NOT: krem satırındaki değerler PROJECT_CONTEXT.md'de belgelenmiş,
    # basılı provadan geçmiş ölçümlerdir. Beyaz satırı aynı formülden türer;
    # krem satırının birebir tutması formülün doğruluğunu kanıtlar.
    "white": dict(spine_w=0.7409, cover_w=12.9909, cover_h=9.25,
                  canvas=(3897, 2775), spine_x=6.125, spine_x2=6.8659,
                  front_x=6.8659, art_scale=2.752119,
                  rule_l=6.2657, rule_r=6.7243),
}


def selftest() -> int:
    """Ciltsiz geometrisinin yayımlanmış değerlerle birebir aynı kaldığını
    kanıtlar. Motor genelleştirildikten sonra en kritik kontrol budur."""
    bad = 0
    for paper, want in _PAPERBACK_GOLDEN.items():
        g = geometry(paper=paper, binding="paperback")
        p = art_placement(g)
        checks = [
            ("sırt", g.spine_w, want["spine_w"], 1e-4),
            ("tuval G", g.cover_w, want["cover_w"], 1e-4),
            ("tuval Y", g.cover_h, want["cover_h"], 1e-4),
            ("sırt x", g.spine.x, want["spine_x"], 1e-4),
            ("sırt x2", g.spine.x2, want["spine_x2"], 1e-4),
            ("ön x", g.front.x, want["front_x"], 1e-4),
            ("ölçek", p.scale, want["art_scale"], 1e-5),
            ("fileto L", p.rule_l_in, want["rule_l"], 1e-3),
            ("fileto R", p.rule_r_in, want["rule_r"], 1e-3),
        ]
        for name, got, exp, tol in checks:
            ok = abs(got - exp) <= tol
            if not ok:
                bad += 1
            print(f"  [{'OK ' if ok else 'HATA'}] {paper:6s} {name:9s} "
                  f"beklenen {exp:<12} gelen {got}")
        ok_px = tuple(g.canvas_px) == want["canvas"]
        if not ok_px:
            bad += 1
        print(f"  [{'OK ' if ok_px else 'HATA'}] {paper:6s} {'tuval px':9s} "
              f"beklenen {want['canvas']} gelen {tuple(g.canvas_px)}")
    # ciltside menteşe ve karton payları sıfırdan büyük olmalı
    h = geometry(binding="hardcover")
    for name, val in [("menteşe", h.hinge_back.w), ("karton sırt payı",
                      h.spine_w - PAGE_COUNT * E.PAPER_THICKNESS[PAPER])]:
        ok = val > 0
        if not ok:
            bad += 1
        print(f"  [{'OK ' if ok else 'HATA'}] ciltli {name:9s} = {val:.4f} in")
    print()
    print("SONUÇ:", "TÜM KONTROLLER GEÇTİ" if bad == 0 else f"{bad} HATA")
    return bad


def _print(g: CoverGeometry, p: ArtPlacement):
    P = g.profile
    print(f"Ciltleme     : {P.label}"
          f"{'' if g.calibrated else '   ⚠ KALİBRE EDİLMEMİŞ'}")
    print(f"Kâğıt        : {g.paper}  ({E.PAPER_THICKNESS[g.paper]} inç/sayfa)")
    print(f"Sayfa        : {g.page_count}   (sınır {P.min_pages}–{P.max_pages})")
    print(f"Sırt         : {g.spine_w:.4f} inç  ({g.spine_w*25.4:.2f} mm)"
          + (f"   = {g.page_count}×{E.PAPER_THICKNESS[g.paper]} + karton {P.spine_board}"
             if P.spine_board else ""))
    print(f"Tam kapak    : {g.cover_w:.4f} x {g.cover_h:.4f} inç")
    print(f"             = {g.cover_w*25.4:.2f} x {g.cover_h*25.4:.2f} mm")
    print(f"{DPI} DPI tuval: {g.canvas_px[0]} x {g.canvas_px[1]} px")
    print()
    panels = [("Arka", g.back), ("Menteşe", g.hinge_back), ("Sırt", g.spine),
              ("Menteşe", g.hinge_front), ("Ön", g.front), ("Barkod", g.barcode)]
    for name, r in panels:
        if r.w <= 0:
            continue
        print(f"  {name:8s} x={r.x:8.4f}..{r.x2:8.4f}  y={r.y:6.4f}..{r.y2:6.4f}"
              f"   ({r.x/g.cover_w*100:6.2f}% .. {r.x2/g.cover_w*100:6.2f}%)")
    print()
    print(f"Görsel ölçek : {p.scale:.6f}x   (yerel {p.native_ppi} PPI)")
    print(f"Kırpma       : sol {p.crop_left:.0f} sağ {p.crop_right:.0f} "
          f"üst {p.crop_top:.0f} alt {p.crop_bottom:.0f} px")
    print(f"Altın fileto : {p.rule_l_in:.4f} ve {p.rule_r_in:.4f} inç")
    print(f"             → sırt kenarından {p.rule_inset_in:.4f} inç "
          f"({p.rule_inset_in*25.4:.2f} mm) içeride")


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Kapak geometrisi")
    E.add_argument(ap)
    ap.add_argument("--paper", default=None, choices=list(E.PAPER_THICKNESS))
    ap.add_argument("--pages", type=int, default=None)
    ap.add_argument("--selftest", action="store_true",
                    help="ciltsiz geometrisinin değişmediğini kanıtla")
    ap.add_argument("--all-editions", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        print("REGRESYON — yayımlanmış ciltsiz kapağın değerleri\n")
        raise SystemExit(1 if selftest() else 0)

    keys = E.ORDER if a.all_editions else [a.edition]
    for k in keys:
        ed = E.get(k)
        paper = a.paper or ed.paper
        print(f"\n{'='*72}\n{ed.label.upper()}  ({k})\n{'='*72}")
        try:
            # --pages verilmezse sayfa sayısı ÜRETİLMİŞ İÇ BLOKTAN okunur.
            # Sabit bir varsayılan kullanmak, büyük punto gibi sayfa sayısı
            # farklı sürümlerde günlüğe yanlış sırt yazdırıyordu.
            g = geometry_for(ed, paper=paper, pages=a.pages)
            src = "elle verildi" if a.pages else "iç bloktan okundu"
            print(f"(sayfa sayısı {src})")
            _print(g, art_placement(g))
        except SystemExit as exc:
            print(f"  ÜRETİLEMEZ: {exc}")
