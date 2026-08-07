"""
CODEX MYTHOLOGICA — Amazon A+ İçerik modülleri: geometri ve sabitler.
================================================================================
Kapak boru hattındaki `cover_spec.py` ile aynı felsefe: TEK doğruluk kaynağı.
Hiçbir koordinat elle yazılmaz.

Kaynaklar (DOĞRULANMIŞ — Amazon A+ modül belgeleri, 2026):
  * Standard Image Header with Text ............ 970 × 600 px
  * Standard Image & Light/Dark Text Overlay ... 970 × 300 px
  * Standard Three Images & Text ............... 300 × 300 px
  * Standard Company Logo ...................... 600 × 180 px
  * Azami dosya boyutu ......................... 2 MB  (standart katman)
  * Biçim ...................................... JPEG veya PNG
  * Renk uzayı ................................. YALNIZCA RGB (CMYK kabul edilmez)
  * Asgari çözünürlük .......................... 72 DPI

TASARIM KARARI — @1x ve @2x
    Amazon yukarıdaki ölçüleri GÖRÜNTÜLEME ölçüsü olarak tanımlar. Tam ölçüde
    yüklemek her zaman kabul edilir; iki katı yüklemek retina ekranlarda daha
    net görünür ama Amazon'un ölçekleme davranışı belgelenmemiştir.
    Bu yüzden İKİSİ de üretilir: @1x kanonik (yüklenecek olan), @2x yedek.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional

# =============================================================================
# 1. AMAZON MODÜL TİPLERİ
# =============================================================================

MODULE_TYPES = {
    "image_header_text": {
        "label": "Standard Image Header with Text",
        "w": 970, "h": 600,
        "note": "Sayfanın en üstünde tam genişlik başlık görseli.",
    },
    "image_text_overlay": {
        "label": "Standard Image & Light Text Overlay",
        "w": 970, "h": 300,
        "note": "Tam genişlik şerit. Kısa ve çarpıcı olmalı.",
    },
    "three_images_text": {
        "label": "Standard Three Images & Text",
        "w": 300, "h": 300,
        "note": "Üç sütun; her sütunun kendi başlığı ve gövdesi var.",
    },
    "company_logo": {
        "label": "Standard Company Logo",
        "w": 600, "h": 180,
        "note": "Künye / yayınevi logosu.",
    },
}

MAX_BYTES = 2 * 1024 * 1024      # 2 MB, standart A+ katmanı
ACCEPTED_FORMATS = ("JPEG", "PNG")
COLOR_SPACE = "RGB"
RETINA_SCALE = 2

# Görsel içi güvenli kenar payı: modül genişliğinin oranı olarak.
# Amazon kırpmaz, ama ürün sayfası dar ekranlarda modülü yeniden ölçekler;
# kenara yapışan tipografi sıkışık görünür.
SAFE_MARGIN_FRAC = 0.045

# =============================================================================
# 2. MODÜL TANIMLARI
# =============================================================================
# `source`   : 07_ASSETS/aplus_raw/ içindeki dosya
# `type`     : yukarıdaki MODULE_TYPES anahtarı
# `anchor`   : kırpma sırasında korunacak taraf — otomatik analiz bunu doğrular
#              ama sanat yönü kararı olduğu için açıkça yazılır.
# `text_side`: tipografinin yerleşeceği taraf (analiz bunu ölçerek DOĞRULAR;
#              uyuşmazlık olursa derleme uyarı verir)


@dataclass(frozen=True)
class ModuleDef:
    key: str
    source: str
    type: str
    title: str
    purpose: str
    anchor: str            # yatay kırpmada korunacak taraf
    text_side: str         # "left" | "right" | "panels" | "columns" | "rows"
    order: int
    crop_bias: str = "center"   # dikey kırpmada: "center" | "subject"
    # NEDEN "center" varsayılan:
    #   module-1'de belirginlik kütlesi mandalanın parlak çekirdeğine kayıyor;
    #   konuya göre ortalanan kırpma halkanın ALT madalyonlarını kesiyordu.
    #   Görsel karşılaştırma (üst / orta / alt) ortadakini net kazanan yaptı.

    @property
    def w(self) -> int: return MODULE_TYPES[self.type]["w"]

    @property
    def h(self) -> int: return MODULE_TYPES[self.type]["h"]

    @property
    def ar(self) -> float: return self.w / self.h


MODULES = [
    ModuleDef(
        key="m1-header", source="module-1.png", type="image_text_overlay",
        title="Başlık şeridi",
        purpose="Kapsamı bir bakışta kanıtla: on dokuz gelenek, tek cilt.",
        anchor="right", text_side="left", order=1),
    ModuleDef(
        key="m2-what-it-is", source="module-2.png", type="image_header_text",
        title="Bu kitap nedir / ne değildir / nasıl okunur",
        purpose="Referans kitabı sanıp alan okuru elemek — iade oranını düşürür.",
        anchor="left", text_side="panels", order=2),
    ModuleDef(
        key="m3-comparison", source="module-3.png", type="image_header_text",
        title="Karşılaştırma",
        purpose="Fry/Gaiman okuyan okura 'ek olarak neden bu' cevabını ver.",
        anchor="center", text_side="columns", order=3),
    ModuleDef(
        key="m4-quotation", source="module-4.png", type="image_header_text",
        title="Metinden bir bölüm",
        purpose="Üslup örneği — edebî kurguda satın alma kararını ses verir.",
        anchor="right", text_side="left", order=4),
    ModuleDef(
        key="m5-interior", source="bonus-module.png", type="image_header_text",
        title="İç sayfalar",
        purpose="Dizgi kalitesini göster; koleksiyonluk algısını pekiştir.",
        anchor="center", text_side="rows", order=5),
]

MODULE_BY_KEY = {m.key: m for m in MODULES}

# =============================================================================
# 3. RENK PALETİ  (kapaktan devralınır — tek görsel dil)
# =============================================================================

GOLD = "#C9A227"
GOLD_LIGHT = "#E3C766"
PARCHMENT = "#E8E0CE"
DIM = "#B9AE95"
RULE = "#8A7327"          # ince ayraç çizgileri
SHADOW = "#000000"

# =============================================================================
# 4. TİPOGRAFİ ÖLÇEĞİ
# =============================================================================
# Kapakla aynı iki yüz: Cinzel (majüskül başlık) + EB Garamond (gövde).
#
# Punto boyutları modülün GENİŞLİĞİNİN oranı olarak tanımlanır.
#
# NEDEN GENİŞLİK, YÜKSEKLİK DEĞİL:
#   Bütün A+ modülleri 970 px genişliktedir ama yükseklik 300 ile 600 arasında
#   değişir. Ölçek yüksekliğe bağlanınca aynı "gövde metni" şerit modülde 12 px,
#   uzun modülde 24 px oluyordu — aynı sayfada iki farklı tipografik ses.
#   Genişliğe bağlanınca bütün modüller tek bir ölçeği paylaşır.
#
# Değerler 970 px genişlikte EKRANDA okunacak metne göre kalibre edildi.

TYPE_SCALE = {
    # ad                  genişlik oranı   font              harf aralığı
    "eyebrow":      dict(cap=0.0092, font="cinzel-400",          track=0.240),
    "headline":     dict(cap=0.0320, font="cinzel-500",          track=0.045),
    "headline_sm":  dict(cap=0.0216, font="cinzel-500",          track=0.050),
    "subhead":      dict(cap=0.0140, font="garamond-italic-400", track=0.000),
    "panel_title":  dict(cap=0.0110, font="cinzel-400",          track=0.130),
    "body":         dict(cap=0.0108, font="garamond-400",        track=0.000),
    "body_sm":      dict(cap=0.0093, font="garamond-400",        track=0.000),
    "caption":      dict(cap=0.0098, font="garamond-italic-400", track=0.000),
    "figure":       dict(cap=0.0300, font="cinzel-500",          track=0.020),
    "quote":        dict(cap=0.0182, font="garamond-italic-400", track=0.000),
    "attrib":       dict(cap=0.0092, font="cinzel-400",          track=0.180),
}

# Satır aralığı = punto boyutunun katı
LEADING = {
    "headline": 1.20, "headline_sm": 1.22, "subhead": 1.34,
    "panel_title": 1.30, "body": 1.46, "body_sm": 1.48,
    "caption": 1.40, "quote": 1.52, "eyebrow": 1.30,
    "figure": 1.10, "attrib": 1.30,
}


def leading_for(style: str) -> float:
    return LEADING.get(style, 1.40)


def dump() -> dict:
    return {
        "module_types": MODULE_TYPES,
        "limits": {"max_bytes": MAX_BYTES, "formats": list(ACCEPTED_FORMATS),
                   "color_space": COLOR_SPACE, "retina_scale": RETINA_SCALE,
                   "safe_margin_frac": SAFE_MARGIN_FRAC},
        "modules": [asdict(m) | {"w": m.w, "h": m.h, "ar": round(m.ar, 4)}
                    for m in MODULES],
        "type_scale": TYPE_SCALE, "leading": LEADING,
        "colors": {"gold": GOLD, "gold_light": GOLD_LIGHT,
                   "parchment": PARCHMENT, "dim": DIM, "rule": RULE},
    }


if __name__ == "__main__":
    print(f"{'anahtar':16s} {'kaynak':18s} {'modül tipi':34s} "
          f"{'ölçü':12s} {'AR':>7s}  metin")
    print("-" * 104)
    for m in MODULES:
        t = MODULE_TYPES[m.type]
        print(f"{m.key:16s} {m.source:18s} {t['label']:34s} "
              f"{t['w']}x{t['h']:<7d} {m.ar:7.4f}  {m.text_side}")
    print(f"\nAzami dosya: {MAX_BYTES/1024/1024:.0f} MB · biçim "
          f"{'/'.join(ACCEPTED_FORMATS)} · renk {COLOR_SPACE} · "
          f"retina @{RETINA_SCALE}x")
