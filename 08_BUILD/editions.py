"""
CODEX MYTHOLOGICA — SÜRÜM (EDITION) KAYIT DEFTERİ
================================================================================
Bu dosya, çok formatlı üretim hattının TEK doğruluk kaynağıdır.

Bir "sürüm" = bir ürün SKU'su. Her sürüm kendi iç blok tipografisini, kendi
kapak geometrisini ve kendi doğrulama eşiklerini taşır. Hiçbir betikte sürüme
özgü sabit yoktur; hepsi buradan okunur.

    from editions import EDITIONS, get
    ed = get("hardcover")

Yeni bir sürüm eklemek = bu dosyaya bir `Edition` satırı eklemek. Betiklerin
hiçbiri değişmez.

--------------------------------------------------------------------------------
KAYNAKLAR (DOĞRULANMIŞ — Amazon KDP resmî yardım sayfaları, Ağustos 2026)
--------------------------------------------------------------------------------
  * İç marj (gutter) tablosu — "Set Trim Size, Bleed, and Margins" (GVBQ3CMEQW3W2VL6)
        24–150 s : 0.375"     301–500 s : 0.625"     701–828 s : 0.875"
       151–300 s : 0.500"     501–700 s : 0.750"
    Dış/üst/alt asgari: taşmasız 0.25", taşmalı 0.375".
    Tablo ciltsiz için yayımlanmıştır; KDP ciltli için ayrı bir tablo
    yayımlamaz. Bu proje ciltlide de aynı tabloyu kullanır ve üstüne pay bırakır.

  * Ciltli baskı öğeleri — "Hardcover Print Elements" (GKZVNAAFYWVKZWL8)
        2 mm kalınlığında masif karton üzerine sarılmış "case laminate";
        iç kapağa yapıştırılan sarım (wrap); 120 sayfa üstünde başlık bandı.

  * Ciltli sayfa sınırı 75–550, trim seçenekleri — "Print Options" (G201834180)

  * Büyük punto: KDP zorunlu bir standart YAYIMLAMAZ. Yayıncı metadata'da
    kendi beyan eder. Sektör normu 16–18 pt gövde, 1.5–1.8x satır aralığı,
    0.75–1" marj.  → bu proje 16 pt / 1.5x kullanır (Bölüm "largeprint" notu).
"""

from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional


# =============================================================================
# 1. KDP MARJ TABLOSU  (DOĞRULANMIŞ)
# =============================================================================

GUTTER_TABLE = [
    (24, 150, 0.375),
    (151, 300, 0.500),
    (301, 500, 0.625),
    (501, 700, 0.750),
    (701, 828, 0.875),
]

OUTER_MIN_NO_BLEED = 0.25
OUTER_MIN_BLEED = 0.375


def required_gutter(pages: int) -> float:
    """KDP'nin sayfa sayısına göre zorunlu kıldığı asgari iç marj."""
    for lo, hi, g in GUTTER_TABLE:
        if lo <= pages <= hi:
            return g
    if pages < 24:
        raise ValueError(f"{pages} sayfa — KDP asgarisi 24")
    raise ValueError(f"{pages} sayfa — KDP azamisi 828")


# =============================================================================
# 2. CİLTLEME PROFİLLERİ
# =============================================================================

@dataclass(frozen=True)
class BindingProfile:
    """Bir ciltleme türünün kapak geometrisi kuralları. Ölçüler inç."""
    key: str
    label: str
    # Tuvalin kesim kutusunun DIŞINDA kalan pay (dört kenar).
    #   ciltsizde  : taşma (bleed)
    #   ciltlide   : sarım (wrap) — kartonun etrafına dolanıp içeri yapışır
    outer_pad: float
    # Sırt ile ön/arka kapak arasına eklenen menteşe oluğu (her yanda).
    hinge: float
    # Sırt genişliğine eklenen karton payı.
    spine_board: float
    # Kartonun kitap bloğundan taşma payı (kare/square) — yükseklikte TOPLAM.
    board_overhang_h: float
    # Aynısı genişlikte, kenar BAŞINA.
    board_overhang_w: float
    # Canlı içerik yasak bandı, kesim kenarından içeri.
    safe: float
    # Canlı içerik yasak bandı, sırt kenarından içeri (menteşe bölgesi).
    spine_safe: float
    # Sırt METNİNİN sırt kenarlarına asgari uzaklığı.
    spine_text_safe: float
    # Barkod kutusunun kapağın ALTINDAN asgari uzaklığı.
    barcode_bottom_clear: float
    # Barkod kutusunun sırt/menteşeden asgari uzaklığı.
    barcode_spine_clear: float
    # Sayfa sınırları.
    min_pages: int
    max_pages: int
    # Barkod kutusunun tuvaldeki KESİN yeri (x, y, w, h) — inç.
    # None ise aşağıdaki barcode_*_clear paylarından TÜRETİLİR.
    # KDP'nin ciltlide barkodu nereye bastığı türetilebilir bir formülden
    # gelmiyor (kesim altından 0.2583", kesim sağından 0.4459" — hiçbiri
    # yuvarlak sayı değil), bu yüzden şablondan ÖLÇÜLÜR.
    barcode_rect: Optional[tuple] = None
    # Bu profilin sayıları resmî şablondan ÖLÇÜLDÜ mü?
    calibrated: bool = False
    source: str = ""


PAPERBACK_PROFILE = BindingProfile(
    key="paperback",
    label="Ciltsiz (perfect bound)",
    outer_pad=0.125,          # taşma — KDP kapak şablonu üreteci
    hinge=0.0,                # ciltsizde menteşe yok
    spine_board=0.0,
    board_overhang_h=0.0,
    board_overhang_w=0.0,
    safe=0.25,
    spine_safe=0.25,
    spine_text_safe=0.0625,
    barcode_bottom_clear=0.25,
    barcode_spine_clear=0.25,
    min_pages=24,
    max_pages=828,
    calibrated=True,          # 39/39 doğrulama + basılı prova ile teyit edildi
    source="KDP 'Create a Paperback Cover' (G201953020) + 03_COVER doğrulaması",
)

# -----------------------------------------------------------------------------
# ⚠ CİLTLİ PROFİLİ — VARSAYILAN DEĞERLER KALİBRE EDİLMEMİŞTİR
# -----------------------------------------------------------------------------
# KDP, ciltli kapak boyutlarının FORMÜLÜNÜ yayımlamıyor; "cover calculator and
# template generator" kullanılmasını söylüyor. Yayımladığı tek tek ölçüler ise
# kendi içinde çelişkili:
#
#     "extend 0.51" (15 mm) past the edge"   →  0.51 in = 12.95 mm ≠ 15 mm
#
# Üçüncü taraf kaynaklar da üç farklı sarım payı veriyor: 0.51 / 0.591 / 0.625.
# Bu yüzden aşağıdaki değerler VARSAYILANDIR ve KDP'nin resmî şablonundan
# ölçülerek doğrulanmalıdır:
#
#     python3 08_BUILD/calibrate_cover.py --template <indirilen-sablon.png>
#
# Kalibrasyon yapılmadan üretilen ciltli kapak `_PROVISIONAL` etiketiyle
# dışa aktarılır ve doğrulama bunu BLOKE EDİCİ olarak raporlar.
#
# Metrik değerler tercih edildi: KDP'nin ciltli belgesi ölçüleri mm cinsinden
# tutarlı veriyor (15 / 16 / 10 / 19 / 6 mm) ve inç karşılıkları yuvarlanmış.
# -----------------------------------------------------------------------------

MM = 1 / 25.4

HARDCOVER_PROFILE = BindingProfile(
    key="hardcover",
    label="Ciltli (case laminate)",
    outer_pad=round(15 * MM, 4),          # 0.5906" — sarım
    hinge=round(5 * MM, 4),               # 0.1969" — menteşe oluğu, her yanda
    spine_board=0.125,                    # karton payı
    board_overhang_h=round(6 * MM, 4),    # 0.2362" — yükseklikte TOPLAM
    board_overhang_w=0.0,                 # bilinmiyor; kalibrasyon çözer
    safe=round(16 * MM, 4),               # 0.6299" — kitap kenarından
    spine_safe=round(10 * MM, 4),         # 0.3937" — menteşe keep-out
    spine_text_safe=0.0625,
    barcode_bottom_clear=round(19 * MM, 4),   # 0.748"
    barcode_spine_clear=round(6 * MM, 4),     # 0.2362"
    min_pages=75,
    max_pages=550,
    calibrated=False,
    source="KDP 'Create a Hardcover Cover' (GDTKFJPNQCBTMRV6) — kısmî; "
           "formül yayımlanmamış, kalibrasyon gerekir",
)

BINDINGS: Dict[str, BindingProfile] = {
    PAPERBACK_PROFILE.key: PAPERBACK_PROFILE,
    HARDCOVER_PROFILE.key: HARDCOVER_PROFILE,
}


# =============================================================================
# 3. KÂĞIT KALINLIĞI  (DOĞRULANMIŞ — KDP resmî tablosu)
# =============================================================================

PAPER_THICKNESS = {
    "white": 0.002252,     # siyah mürekkep + beyaz kâğıt
    "cream": 0.0025,       # siyah mürekkep + krem kâğıt
    "color": 0.002347,     # renkli mürekkep + beyaz kâğıt
}


# =============================================================================
# 4. SÜRÜMLER
# =============================================================================

@dataclass(frozen=True)
class Edition:
    key: str
    label: str
    binding: str              # BINDINGS anahtarı
    trim_w: float
    trim_h: float
    paper: str                # varsayılan kâğıt
    papers: List[str]         # bu sürüm için üretilecek kâğıt varyantları

    # --- iç blok tipografisi ---
    body_pt: float
    lead_pt: float
    gutter: float
    outer: float
    top: float
    bottom: float
    display_scale: float      # başlık/ara başlık ölçek çarpanı
    folio_pt: float
    head_pt: float

    # --- ürün ---
    price_usd: float
    title_suffix: str = ""    # KDP başlığına eklenecek ek
    kdp_notes: str = ""

    # --- üretim ---
    slug: str = ""
    interior_dir: str = ""
    cover_dir: str = ""

    def __post_init__(self):
        object.__setattr__(self, "slug", self.slug or self.key.upper())
        object.__setattr__(self, "interior_dir",
                           self.interior_dir or f"04_PRINT/{self.slug}")
        object.__setattr__(self, "cover_dir",
                           self.cover_dir or f"03_COVER/{self.slug}")

    # ---- türetilmiş ----
    @property
    def profile(self) -> BindingProfile:
        return BINDINGS[self.binding]

    @property
    def text_w(self) -> float:
        return self.trim_w - self.gutter - self.outer

    @property
    def text_h(self) -> float:
        return self.trim_h - self.top - self.bottom

    @property
    def lines_per_page(self) -> int:
        return int((self.text_h * 72) // self.lead_pt)

    def gutter_ok(self, pages: int) -> tuple:
        """(uygun_mu, gereken, pay)"""
        req = required_gutter(pages)
        return self.gutter >= req, req, round(self.gutter - req, 4)

    def as_dict(self) -> dict:
        d = asdict(self)
        d["profile"] = asdict(self.profile)
        d["text_w"] = round(self.text_w, 4)
        d["text_h"] = round(self.text_h, 4)
        d["lines_per_page"] = self.lines_per_page
        return d


# -----------------------------------------------------------------------------
# Ölçülen taban: ciltsiz sürüm 329 sayfa
# (04_PRINT/PAPERBACK/CODEX_MYTHOLOGICA_INTERIOR_PAPERBACK.pdf).
# Aşağıdaki üç sürüm bu tabandan türetilir. Ciltsiz satırındaki her sayı,
# YAYIMLANMIŞ kitaptaki değerdir — değiştirilmemelidir.
# -----------------------------------------------------------------------------

PAPERBACK = Edition(
    key="paperback",
    label="Ciltsiz",
    binding="paperback",
    trim_w=6.0, trim_h=9.0,
    paper="cream", papers=["cream", "white"],
    body_pt=11.2, lead_pt=15.6,
    gutter=0.875, outer=0.625, top=0.75, bottom=0.75,
    display_scale=1.0, folio_pt=9.2, head_pt=7.6,
    price_usd=18.99,
    kdp_notes="Yayında. 329 sayfa. Bu sürümün hiçbir parametresi değiştirilmez.",
    slug="PAPERBACK",
)

# CİLTLİ: iç blok ciltsizle AYNIDIR ve bu bilinçli bir karardır.
#   * 329 sayfa → KDP asgari iç marjı 0.625"; bizimki 0.875" — 0.25" pay var,
#     yani ciltli cildin daha az açılan yapısı için hazır fazlalık mevcut.
#   * Gutter'ı büyütmek satır ölçüsünü değiştirir → sayfa sayısı değişir →
#     sırt değişir → metin yeniden akar. Uygunluk kazancı SIFIR, risk YÜKSEK.
#   * Sonuç: tek metin bloğu, iki ürün. Ciltli yalnızca KAPAKTA farklıdır.
HARDCOVER = Edition(
    key="hardcover",
    label="Ciltli",
    binding="hardcover",
    trim_w=6.0, trim_h=9.0,
    paper="cream", papers=["cream", "white"],
    body_pt=11.2, lead_pt=15.6,
    gutter=0.875, outer=0.625, top=0.75, bottom=0.75,
    display_scale=1.0, folio_pt=9.2, head_pt=7.6,
    price_usd=32.99,
    kdp_notes="İç blok ciltsizle özdeştir (bilinçli). 75–550 sayfa sınırı: 329 ✓",
    slug="HARDCOVER",
)

# BÜYÜK PUNTO: 16 pt gövde, 1.5x satır aralığı (24 pt).
#   * Dış marj 0.625" → 0.50"e indirildi: büyük puntoda satır ölçüsü kritik,
#     KDP asgarisi 0.25" olduğu için hâlâ iki kat pay var.
#   * Sayfa sayısı ~2x artar → 501–700 bandı → asgari iç marj 0.75";
#     bizimki 0.875" — pay korunur.
#   * Görüntü stilleri 1.28x ölçeklenir ki başlık/gövde hiyerarşisi korunsun.
LARGEPRINT = Edition(
    key="largeprint",
    label="Büyük Punto",
    binding="paperback",
    trim_w=6.0, trim_h=9.0,
    paper="cream", papers=["cream"],
    body_pt=16.0, lead_pt=24.0,
    gutter=0.875, outer=0.500, top=0.70, bottom=0.70,
    display_scale=1.28, folio_pt=13.0, head_pt=10.5,
    price_usd=27.99,
    title_suffix=" (Large Print Edition)",
    kdp_notes="Ayrı ASIN. Başlıkta 'Large Print' geçmeli — arama niyeti farklı.",
    slug="LARGEPRINT",
)

EDITIONS: Dict[str, Edition] = {e.key: e for e in (PAPERBACK, HARDCOVER, LARGEPRINT)}
ORDER = ["paperback", "hardcover", "largeprint"]


def get(key: str) -> Edition:
    if key not in EDITIONS:
        raise SystemExit(f"bilinmeyen sürüm: {key!r}\n"
                         f"seçenekler: {', '.join(ORDER)}")
    return EDITIONS[key]


def add_argument(ap, required: bool = False):
    """Her betiğin aynı --edition bayrağını kullanması için tek yer."""
    ap.add_argument("--edition", "-e", default=None if required else "paperback",
                    choices=ORDER, required=required,
                    help="üretilecek sürüm (varsayılan: paperback)")
    return ap


# =============================================================================
# 5. RAPOR
# =============================================================================

def table(pages_by_edition: Optional[Dict[str, int]] = None) -> str:
    pages_by_edition = pages_by_edition or {}
    L = []
    L.append(f"{'sürüm':12s} {'ciltleme':11s} {'trim':9s} {'gövde':>10s} "
             f"{'iç marj':>8s} {'dış':>6s} {'metin':>12s} {'satır/s':>8s}")
    L.append("-" * 84)
    for k in ORDER:
        e = EDITIONS[k]
        L.append(f"{e.label:12s} {e.profile.label[:11]:11s} "
                 f"{e.trim_w:g}x{e.trim_h:g}in "
                 f"{e.body_pt:5.1f}/{e.lead_pt:<4.1f} "
                 f"{e.gutter:8.3f} {e.outer:6.3f} "
                 f"{e.text_w:5.3f}x{e.text_h:<5.3f} {e.lines_per_page:8d}")
        p = pages_by_edition.get(k)
        if p:
            ok, req, slack = e.gutter_ok(p)
            L.append(f"{'':12s} → {p} sayfa · KDP asgari iç marj {req:.3f}\" · "
                     f"pay {slack:+.3f}\" · {'UYGUN' if ok else 'YETERSİZ'}")
    return "\n".join(L)


if __name__ == "__main__":
    import json
    import argparse

    ap = argparse.ArgumentParser(description="Sürüm kayıt defteri")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.json:
        print(json.dumps({k: EDITIONS[k].as_dict() for k in ORDER},
                         ensure_ascii=False, indent=2))
    else:
        print("CODEX MYTHOLOGICA — sürüm kayıt defteri\n")
        print(table({"paperback": 329, "hardcover": 329}))
        print()
        print("KDP iç marj tablosu (DOĞRULANMIŞ):")
        for lo, hi, g in GUTTER_TABLE:
            print(f"  {lo:3d}–{hi:3d} sayfa → {g:.3f}\"")
        print()
        for k in ORDER:
            e = EDITIONS[k]
            p = e.profile
            print(f"{e.label}: {p.label}  · sayfa {p.min_pages}–{p.max_pages}"
                  f"  · dış pay {p.outer_pad:.4f}\"  · menteşe {p.hinge:.4f}\""
                  f"  · {'KALİBRE' if p.calibrated else '⚠ KALİBRE DEĞİL'}")
