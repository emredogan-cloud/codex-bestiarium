"""
CODEX MYTHOLOGICA — kapak tipografi sistemi.
================================================================================
Hiçbir konum elle ayarlanmaz. Her metin kutusu:

    * bir HEDEF GENİŞLİĞE göre çözülür (punto boyutu hesaplanır, tahmin edilmez)
    * geometriden gelen bir çıpaya göre hizalanır
    * inç cinsinden kesin bir dikdörtgen döndürür

Böylece sayfa sayısı, kâğıt türü veya kesim ölçüsü değişirse tipografi
kendiliğinden yeniden çözülür — yeniden konumlandırma gerekmez.

Ölçüm motoru fontun kendi hmtx/cmap tablolarını okur; yani punto boyutları
gerçek glif genişliklerinden türetilir.
"""

from __future__ import annotations
import os
import sys
from dataclasses import dataclass, field, asdict
from typing import List, Optional

from fontTools.ttLib import TTFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cover_spec as S  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(ROOT, "07_ASSETS", "fonts")

PT = 72.0  # punto / inç

# =============================================================================
# METİN İÇERİĞİ  (onaylanmış — 06_REPORTS üretim raporu Bölüm 07'den)
# =============================================================================

TITLE_L1 = "CODEX"
TITLE_L2 = "MYTHOLOGICA"
SUBTITLE = "76 Myths from 19 Civilizations"
AUTHOR = "EMRE DOĞAN"
IMPRINT = "VÂLİÇE PRESS"

SPINE_TITLE = "CODEX MYTHOLOGICA"
SPINE_ORNAMENT = "*"
SPINE_AUTHOR = "EMRE DOĞAN"

BACK_HOOK = ("Nineteen civilizations. Seventy-six myths. "
             "One human question, asked in every language ever spoken.")

BACK_BODY = ("A god is torn apart and reassembled by a grieving wife in Egypt "
             "— and by a grieving mother in Greece. A hero descends into the "
             "land of the dead to bring back someone he loves, is given one "
             "condition, and breaks it, in Japan and in Ireland and in "
             "Mesopotamia. The rabbit a Chinese poet sees on the face of the "
             "moon is also, independently, sitting on the moon in the "
             "reckoning of the Mexica, who never met a Chinese poet.")

BACK_TAGLINE = "76 myths · 19 civilizations"


# =============================================================================
# FONT ÖLÇÜM MOTORU
# =============================================================================

@dataclass
class Face:
    key: str
    path: str
    weight: int
    _tt: TTFont = field(repr=False, default=None)
    _cmap: dict = field(repr=False, default=None)
    _hmtx: dict = field(repr=False, default=None)
    upem: int = 1000
    cap_ratio: float = 0.70
    asc_ratio: float = 0.80

    def load(self):
        self._tt = TTFont(self.path, lazy=False)
        self._cmap = self._tt.getBestCmap()
        self._hmtx = self._tt["hmtx"].metrics
        self.upem = self._tt["head"].unitsPerEm
        os2 = self._tt["OS/2"]
        cap = getattr(os2, "sCapHeight", None) or int(0.70 * self.upem)
        self.cap_ratio = cap / self.upem
        self.asc_ratio = self._tt["hhea"].ascent / self.upem
        return self

    def missing(self, text: str) -> str:
        return "".join(sorted({c for c in text if ord(c) not in self._cmap}))

    def advance_em(self, text: str) -> float:
        """Metnin em cinsinden genişliği (harf aralığı hariç)."""
        tot = 0
        for ch in text:
            gn = self._cmap.get(ord(ch))
            if gn is None:
                gn = self._cmap.get(ord("?"))
            tot += self._hmtx[gn][0]
        return tot / self.upem

    def width(self, text: str, size_pt: float, tracking_em: float = 0.0) -> float:
        """Çizilen genişlik, İNÇ. Son harften sonraki aralık sayılmaz."""
        n = max(len(text) - 1, 0)
        return (self.advance_em(text) + tracking_em * n) * size_pt / PT

    def size_for_width(self, text: str, target_in: float,
                       tracking_em: float = 0.0) -> float:
        """Hedef genişliği tam tutturan punto boyutu."""
        n = max(len(text) - 1, 0)
        em = self.advance_em(text) + tracking_em * n
        return target_in * PT / em

    def cap_in(self, size_pt: float) -> float:
        return self.cap_ratio * size_pt / PT


class FontBook:
    """Değişken fontlardan sabit örnekler üretir ve ölçüm sağlar."""

    SPECS = {
        "cinzel-500": ("Cinzel[wght].ttf", 500),
        "cinzel-400": ("Cinzel[wght].ttf", 400),
        "garamond-400": ("EBGaramond[wght].ttf", 400),
        "garamond-italic-400": ("EBGaramond-Italic[wght].ttf", 400),
    }

    def __init__(self, static_dir: Optional[str] = None):
        self.static_dir = static_dir or os.path.join(FONT_DIR, "static")
        os.makedirs(self.static_dir, exist_ok=True)
        self.faces = {}

    def build(self) -> "FontBook":
        from fontTools.varLib import instancer
        for key, (fn, wght) in self.SPECS.items():
            src = os.path.join(FONT_DIR, fn)
            if not os.path.exists(src):
                raise SystemExit(f"font yok: {src}\n"
                                 f"07_ASSETS/fonts/README.md içindeki indirme "
                                 f"komutunu çalıştırın.")
            out = os.path.join(self.static_dir, f"{key}.ttf")
            if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
                tt = TTFont(src)
                if "fvar" in tt:
                    instancer.instantiateVariableFont(
                        tt, {"wght": wght}, inplace=True, updateFontNames=False)
                # Her sabit örneğe BENZERSİZ bir iç ad verilir.
                # Aksi hâlde cinzel-400 ve cinzel-500 dosyalarının ikisi de
                # "Cinzel Regular" adını taşır; reportlab bunları tek fonta
                # indirger ve 500 ağırlığı PDF'e HİÇ gömülmez — başlık sessizce
                # 400 ile basılır. Belirtim ile çıktı arasındaki bu sessiz
                # uyuşmazlığı önlemek için ad tablosu açıkça yeniden yazılır.
                uniq = key.replace("-", "").title().replace("_", "")
                nm = tt["name"]
                for nid, val in ((1, uniq), (4, uniq), (6, uniq),
                                 (3, f"{uniq};codexmythologica")):
                    nm.setName(val, nid, 3, 1, 0x409)
                    nm.setName(val, nid, 1, 0, 0)
                tt["OS/2"].usWeightClass = wght
                tt.save(out)
                tt.close()
            self.faces[key] = Face(key, out, wght).load()
        return self

    def __getitem__(self, k) -> Face:
        return self.faces[k]

    def check_glyphs(self) -> List[str]:
        problems = []
        for key, texts in [
            ("cinzel-500", [TITLE_L1, TITLE_L2]),
            ("cinzel-400", [AUTHOR, SPINE_TITLE, SPINE_AUTHOR,
                            SPINE_ORNAMENT, IMPRINT]),
            ("garamond-400", [BACK_HOOK, BACK_BODY]),
            ("garamond-italic-400", [SUBTITLE, BACK_TAGLINE]),
        ]:
            for t in texts:
                m = self.faces[key].missing(t)
                if m:
                    problems.append(f"{key}: eksik glif {m!r} ({t[:36]}…)")
        return problems


# =============================================================================
# YERLEŞİM PARAMETRELERİ  (tek ayar noktası — tüm koordinatlar bunlardan türer)
# =============================================================================

# ═════════════════════════════════════════════════════════════════════════
# ÖNEMLİ: BÜTÜN DİKEY ÇIPALAR ARTIK **KESİM KUTUSUNUN ÜSTÜNDEN** ÖLÇÜLÜR
# ═════════════════════════════════════════════════════════════════════════
# Eskiden tuvalin üstünden ölçülüyordu. Ciltside tuval, sarım (0.5906") ve
# karton payı yüzünden kesim kutusundan çok daha büyük; tuval-göreli çıpalar
# ciltlide metni sayfanın ortasına kaydırırdı.
#
# Kesim-göreli değere geçiş = eski değer − ciltsiz taşması (0.125").
#   TITLE_CAP_TOP        0.950 → 0.825
#   AUTHOR_BASELINE      8.470 → 8.345
#   SPINE_TITLE_TOP      0.950 → 0.825
#   SPINE_AUTHOR_BOTTOM  8.450 → 8.325
#   BACK_TOP             2.350 → 2.225
#   BACK_IMPRINT_BASELINE 7.250 → 7.125
# Ciltsizde sonuç BİREBİR aynıdır (g.trim.y = 0.125); regresyon testi kanıtlar.

# --- ÖN KAPAK ---
# Bu oranlar ONAYLANMIŞ kapaktan ölçülerek alındı (bkz. 06_REPORTS/
# cover-audit.json ve PROJECT_CONTEXT.md "Tipografi kararları"). Sanat yönü
# korunuyor; yalnızca matematiksel olarak yeniden kuruluyor.
TITLE_WIDTH_RATIO = 0.780     # başlık genişliği / ön kapak kesim genişliği
TITLE_TRACKING = 0.080        # em
TITLE_CAP_TOP = 0.825         # ilk satırın büyük harf üstü, KESİM üstünden inç
TITLE_LEADING_RATIO = 1.124   # satır aralığı / punto boyutu
SUBTITLE_WIDTH_RATIO = 0.740  # alt başlık genişliği / başlık genişliği
SUBTITLE_GAP = 0.240          # başlık son satırının taban çizgisinden inç
AUTHOR_CAP_RATIO = 0.660      # yazar büyük harf yüksekliği / başlığınki
AUTHOR_TRACKING = 0.320       # geniş harf aralığı — klasik kapak yazar satırı
AUTHOR_BASELINE = 8.345       # KESİM üstünden inç (ölçülen onaylı konum)

# --- SIRT ---
# Sırtta üç blok var: başlık (üstte), süs (ortada), yazar (altta). Üçünün
# toplam uzunluğu kullanılabilir yüksekliği aşmamalı — bu yüzden boyutlar
# başlığınkinden bağımsız, sırt genişliğine göre ölçeklenir.
SPINE_CAP_RATIO = 0.280       # sırt metni büyük harf yüksekliği / sırt genişliği
SPINE_TRACKING = 0.060
SPINE_AUTHOR_TRACKING = 0.140  # ön kapaktan dar: sırtta yer kısıtlı
SPINE_TITLE_TOP = 0.825       # sırt başlığının başlangıcı, KESİM üstünden inç
SPINE_AUTHOR_BOTTOM = 8.325   # sırt yazarının bitişi, KESİM üstünden inç
SPINE_MIN_GAP = 0.400         # başlık/süs/yazar arası asgari boşluk
SPINE_CAP_MAX = 0.360         # sırt harf yüksekliği tavanı, inç — kalın sırtta
                              # oran tek başına absürt büyük punto üretiyor

# --- ARKA KAPAK ---
BACK_COL_WIDTH = 4.600        # metin sütunu genişliği, inç
BACK_TOP = 2.225              # ilk satırın taban çizgisi, KESİM üstünden inç
BACK_HOOK_SIZE = 16.5         # punto
BACK_HOOK_LEAD = 22.5
BACK_BODY_SIZE = 13.5
BACK_BODY_LEAD = 18.6
BACK_GAP_HOOK_BODY = 0.320    # inç
BACK_GAP_BODY_TAG = 0.360
BACK_TAG_SIZE = 13.5
BACK_IMPRINT_SIZE = 9.0
BACK_IMPRINT_TRACKING = 0.180
BACK_IMPRINT_BASELINE = 7.125  # barkod bandının üstünde kalır (KESİM göreli)


# =============================================================================
# METİN KUTUSU
# =============================================================================

@dataclass
class TextBox:
    id: str
    panel: str            # back | spine | front
    text: str
    font: str
    size_pt: float
    tracking_em: float
    leading_pt: float
    color: str
    align: str            # left | center | right
    rotation: int         # 0 | -90 (sırt: yukarıdan aşağı okunur)
    x: float              # çizim çıpası (inç, tuval sol-üst orijin)
    y: float              # TABAN ÇİZGİSİ (inç)
    w: float              # ölçülen mürekkep genişliği (inç)
    h: float              # büyük harf yüksekliği ya da satır bloğu yüksekliği
    lines: List[str] = field(default_factory=list)

    def as_dict(self):
        d = asdict(self)
        for k in ("size_pt", "tracking_em", "leading_pt", "x", "y", "w", "h"):
            d[k] = round(d[k], 4)
        return d


def _wrap(face: Face, text: str, size_pt: float, max_in: float,
          tracking_em: float = 0.0) -> List[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if face.width(trial, size_pt, tracking_em) <= max_in or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def layout(fb: FontBook, g: S.CoverGeometry = None) -> List[TextBox]:
    """Tüm metin kutularını hesaplar. Sıra = çizim sırası."""
    g = g or S.geometry()
    boxes: List[TextBox] = []

    cin5, cin4 = fb["cinzel-500"], fb["cinzel-400"]
    gar, gari = fb["garamond-400"], fb["garamond-italic-400"]

    # Bütün dikey çıpalar kesim kutusunun üstünden ölçülür.
    T0 = g.trim.y          # ciltsiz: 0.125  ·  ciltli: 0.7087

    # ---------------- ÖN KAPAK ----------------
    fcx = g.front.cx
    title_w = TITLE_WIDTH_RATIO * g.front.w
    t_size = cin5.size_for_width(TITLE_L2, title_w, TITLE_TRACKING)
    t_cap = cin5.cap_in(t_size)
    lead_in = TITLE_LEADING_RATIO * t_size / PT

    y1 = T0 + TITLE_CAP_TOP + t_cap            # 1. satır taban çizgisi
    y2 = y1 + lead_in                          # 2. satır taban çizgisi
    for i, (txt, yy) in enumerate([(TITLE_L1, y1), (TITLE_L2, y2)], 1):
        w = cin5.width(txt, t_size, TITLE_TRACKING)
        boxes.append(TextBox(
            id=f"front.title.l{i}", panel="front", text=txt, font="cinzel-500",
            size_pt=t_size, tracking_em=TITLE_TRACKING,
            leading_pt=lead_in * PT, color=S.GOLD, align="center", rotation=0,
            x=fcx, y=yy, w=w, h=t_cap))

    sub_w = SUBTITLE_WIDTH_RATIO * title_w
    s_size = gari.size_for_width(SUBTITLE, sub_w)
    boxes.append(TextBox(
        id="front.subtitle", panel="front", text=SUBTITLE,
        font="garamond-italic-400", size_pt=s_size, tracking_em=0.0,
        leading_pt=s_size * 1.2, color="#EDE6D6", align="center", rotation=0,
        x=fcx, y=y2 + SUBTITLE_GAP + gari.cap_in(s_size),
        w=gari.width(SUBTITLE, s_size), h=gari.cap_in(s_size)))

    # Yazar satırı GENİŞLİKLE değil, BÜYÜK HARF YÜKSEKLİĞİYLE ölçeklenir:
    # başlıkla arasındaki hiyerarşi kesim ölçüsü değişse bile korunsun diye.
    a_size = AUTHOR_CAP_RATIO * t_cap / cin4.cap_ratio * PT
    boxes.append(TextBox(
        id="front.author", panel="front", text=AUTHOR, font="cinzel-400",
        size_pt=a_size, tracking_em=AUTHOR_TRACKING, leading_pt=a_size * 1.2,
        color=S.GOLD_LIGHT, align="center", rotation=0,
        x=fcx, y=T0 + AUTHOR_BASELINE,
        w=cin4.width(AUTHOR, a_size, AUTHOR_TRACKING), h=cin4.cap_in(a_size)))

    # ---------------- SIRT ----------------
    # Döndürülmüş metinde "büyük harf yüksekliği" sırt ENİNDE yer kaplar; metnin
    # UZUNLUĞU ise sırt boyunda. Bu yüzden punto iki kısıtın küçüğüdür:
    #   (a) sırt genişliğine oranlı tavan (tipografik hiyerarşi)
    #   (b) başlık + yazar + boşlukların sırt boyuna sığdığı en büyük punto
    # Tek başına (a) kullanılırsa kalın sırtlarda metin sırttan taşar; bu,
    # 800 sayfalık bir cildi derlerken sessizce bozulan tek yerdi.
    spine_top = T0 + SPINE_TITLE_TOP
    spine_bot = T0 + SPINE_AUTHOR_BOTTOM
    avail = spine_bot - spine_top

    sp_cap = min(SPINE_CAP_RATIO * g.spine_w, SPINE_CAP_MAX)
    sp_size = sp_cap / cin4.cap_ratio * PT

    # (b): genişlikler punto ile doğrusal ölçeklendiği için tek adımda çözülür.
    unit = (cin4.width(SPINE_TITLE, sp_size, SPINE_TRACKING)
            + cin4.width(SPINE_AUTHOR, sp_size * 0.86, SPINE_AUTHOR_TRACKING)) / sp_size
    fit_size = (avail - 2 * SPINE_MIN_GAP) / unit if unit > 0 else sp_size
    if fit_size < sp_size:
        sp_size = fit_size
        sp_cap = cin4.cap_in(sp_size)

    if sp_size <= 4.0:
        raise SystemExit(
            f"Sırt yerleşimi çözülemedi: kullanılabilir boy {avail:.3f} inç, "
            f"gereken punto {sp_size:.2f} pt (<4 pt).\n"
            f"SPINE_TITLE metnini kısaltın veya SPINE_MIN_GAP değerini düşürün.")

    spx = g.spine.cx                       # sırt merkezine ortalanır
    st_w = cin4.width(SPINE_TITLE, sp_size, SPINE_TRACKING)
    boxes.append(TextBox(
        id="spine.title", panel="spine", text=SPINE_TITLE, font="cinzel-400",
        size_pt=sp_size, tracking_em=SPINE_TRACKING, leading_pt=sp_size * 1.2,
        color=S.GOLD, align="left", rotation=-90,
        x=spx, y=spine_top, w=st_w, h=sp_cap))

    sa_size = sp_size * 0.86
    sa_w = cin4.width(SPINE_AUTHOR, sa_size, SPINE_AUTHOR_TRACKING)
    boxes.append(TextBox(
        id="spine.author", panel="spine", text=SPINE_AUTHOR, font="cinzel-400",
        size_pt=sa_size, tracking_em=SPINE_AUTHOR_TRACKING,
        leading_pt=sa_size * 1.2,
        color=S.GOLD_LIGHT, align="left", rotation=-90,
        x=spx, y=spine_bot - sa_w, w=sa_w,
        h=cin4.cap_in(sa_size)))

    # Sırt sıkışırsa sessizce üst üste binmesin — derlemeyi durdur.
    slack = (spine_bot - sa_w) - (spine_top + st_w)
    if slack < 2 * SPINE_MIN_GAP - 1e-6:   # uyarlama tam sınıra oturabilir
        raise SystemExit(
            f"Sırt yerleşimi sıkışık: başlık {st_w:.3f} + yazar {sa_w:.3f} inç, "
            f"kalan boşluk {slack:.3f} inç < {2*SPINE_MIN_GAP} inç.\n"
            f"SPINE_CAP_RATIO ({SPINE_CAP_RATIO}) veya "
            f"SPINE_AUTHOR_TRACKING ({SPINE_AUTHOR_TRACKING}) değerini düşürün.")

    orn_size = sp_size * 0.92
    orn_w = cin4.width(SPINE_ORNAMENT, orn_size)
    orn_y = (spine_top + st_w + (spine_bot - sa_w)) / 2 - orn_w / 2
    boxes.append(TextBox(
        id="spine.ornament", panel="spine", text=SPINE_ORNAMENT,
        font="cinzel-400", size_pt=orn_size, tracking_em=0.0,
        leading_pt=orn_size, color=S.GOLD, align="left", rotation=-90,
        x=spx, y=orn_y, w=orn_w, h=cin4.cap_in(orn_size)))

    # ---------------- ARKA KAPAK ----------------
    # Sütun, arka kapağın GÜVENLİ ALANINA ortalanır. Ciltsizde güvenli alan
    # simetrik olduğu için bu, panelin merkezine ortalamakla aynı sonucu verir;
    # ciltlide ise menteşe keep-out'u yüzünden alan asimetriktir ve sütunun
    # menteşeye kaymasını bu engeller.
    col_x = g.back_safe.cx - BACK_COL_WIDTH / 2
    y = T0 + BACK_TOP

    hook_lines = _wrap(gar, BACK_HOOK, BACK_HOOK_SIZE, BACK_COL_WIDTH)
    boxes.append(TextBox(
        id="back.hook", panel="back", text=BACK_HOOK, font="garamond-400",
        size_pt=BACK_HOOK_SIZE, tracking_em=0.0, leading_pt=BACK_HOOK_LEAD,
        color=S.PARCHMENT, align="left", rotation=0, x=col_x, y=y,
        w=BACK_COL_WIDTH, h=(len(hook_lines) - 1) * BACK_HOOK_LEAD / PT
        + gar.cap_in(BACK_HOOK_SIZE), lines=hook_lines))
    y += (len(hook_lines) - 1) * BACK_HOOK_LEAD / PT + BACK_GAP_HOOK_BODY

    body_lines = _wrap(gar, BACK_BODY, BACK_BODY_SIZE, BACK_COL_WIDTH)
    boxes.append(TextBox(
        id="back.body", panel="back", text=BACK_BODY, font="garamond-400",
        size_pt=BACK_BODY_SIZE, tracking_em=0.0, leading_pt=BACK_BODY_LEAD,
        color=S.PARCHMENT, align="left", rotation=0, x=col_x, y=y,
        w=BACK_COL_WIDTH, h=(len(body_lines) - 1) * BACK_BODY_LEAD / PT
        + gar.cap_in(BACK_BODY_SIZE), lines=body_lines))
    y += (len(body_lines) - 1) * BACK_BODY_LEAD / PT + BACK_GAP_BODY_TAG

    boxes.append(TextBox(
        id="back.tagline", panel="back", text=BACK_TAGLINE,
        font="garamond-italic-400", size_pt=BACK_TAG_SIZE, tracking_em=0.0,
        leading_pt=BACK_TAG_SIZE * 1.2, color=S.GOLD, align="left", rotation=0,
        x=col_x, y=y, w=gari.width(BACK_TAGLINE, BACK_TAG_SIZE),
        h=gari.cap_in(BACK_TAG_SIZE)))

    boxes.append(TextBox(
        id="back.imprint", panel="back", text=IMPRINT, font="cinzel-400",
        size_pt=BACK_IMPRINT_SIZE, tracking_em=BACK_IMPRINT_TRACKING,
        leading_pt=BACK_IMPRINT_SIZE * 1.2, color=S.DIM, align="left",
        rotation=0, x=col_x, y=T0 + BACK_IMPRINT_BASELINE,
        w=cin4.width(IMPRINT, BACK_IMPRINT_SIZE, BACK_IMPRINT_TRACKING),
        h=cin4.cap_in(BACK_IMPRINT_SIZE)))

    return boxes


def bbox_of(b: TextBox) -> tuple:
    """Kutunun mürekkep sınırlarını (x1, y1, x2, y2) inç olarak döndürür."""
    if b.rotation == -90:
        # metin yukarıdan aşağı akar; genişlik dikeyde, harf yüksekliği yatayda
        return (b.x - b.h / 2, b.y, b.x + b.h / 2, b.y + b.w)
    if b.lines:
        top = b.y - b.h + (len(b.lines) - 1) * b.leading_pt / PT
        top = b.y - (b.h - (len(b.lines) - 1) * b.leading_pt / PT)
        bottom = b.y + (len(b.lines) - 1) * b.leading_pt / PT
        return (b.x, top, b.x + b.w, bottom)
    if b.align == "center":
        return (b.x - b.w / 2, b.y - b.h, b.x + b.w / 2, b.y)
    return (b.x, b.y - b.h, b.x + b.w, b.y)


def dump(paper: str = S.PAPER, edition: str = "paperback") -> dict:
    """Tipografi sistemini 03_COVER/<SÜRÜM>/typography/ altına yazar."""
    import json
    import editions as E
    import paths as P
    ed = E.get(edition)
    fb = FontBook().build()
    g = S.geometry_for(ed, paper=paper)
    boxes = layout(fb, g)
    out_dir = P.cover_dir(ed, "typography")

    recs = []
    for b in boxes:
        x1, y1, x2, y2 = bbox_of(b)
        d = b.as_dict()
        d["bbox_in"] = [round(v, 4) for v in (x1, y1, x2, y2)]
        d["cap_height_in"] = round(b.h, 4)
        d["baseline_from_top_in"] = round(b.y, 4)
        recs.append(d)

    spec = {
        "edition": edition, "binding": g.binding, "calibrated": g.calibrated,
        "paper": paper, "page_count": g.page_count,
        "cover_in": [g.cover_w, g.cover_h], "spine_in": g.spine_w,
        "origin": "tuvalin sol ÜST köşesi; y = TABAN ÇİZGİSİ; birim inç",
        "parameters": {
            "TITLE_WIDTH_RATIO": TITLE_WIDTH_RATIO,
            "TITLE_TRACKING": TITLE_TRACKING,
            "TITLE_CAP_TOP": TITLE_CAP_TOP,
            "TITLE_LEADING_RATIO": TITLE_LEADING_RATIO,
            "SUBTITLE_WIDTH_RATIO": SUBTITLE_WIDTH_RATIO,
            "SUBTITLE_GAP": SUBTITLE_GAP,
            "AUTHOR_CAP_RATIO": AUTHOR_CAP_RATIO,
            "AUTHOR_TRACKING": AUTHOR_TRACKING,
            "AUTHOR_BASELINE": AUTHOR_BASELINE,
            "SPINE_CAP_RATIO": SPINE_CAP_RATIO,
            "SPINE_TRACKING": SPINE_TRACKING,
            "BACK_COL_WIDTH": BACK_COL_WIDTH,
        },
        "boxes": recs,
    }
    with open(os.path.join(out_dir, f"typography-spec-{paper}.json"),
              "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)

    md = [f"# Tipografi sistemi — {ed.label} · {paper} kâğıt, "
          f"{g.page_count} sayfa", "",
          f"Tuval **{g.cover_w:.4f} × {g.cover_h:.4f} inç**, "
          f"sırt **{g.spine_w:.4f} inç**.", "",
          "Orijin tuvalin **sol üst** köşesi. `y` sütunu **taban çizgisidir** "
          "(kutunun üstü değil). Tüm değerler inç.", "",
          "| id | panel | font | pt | harf aralığı | satır aralığı | x | y "
          "(taban) | genişlik | büyük harf y. | hiza | döndürme |",
          "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|"]
    for b in boxes:
        md.append(f"| `{b.id}` | {b.panel} | {b.font} | {b.size_pt:.2f} | "
                  f"{b.tracking_em:.3f} em | {b.leading_pt:.2f} pt | "
                  f"{b.x:.4f} | {b.y:.4f} | {b.w:.4f} | {b.h:.4f} | "
                  f"{b.align} | {b.rotation}° |")
    md += ["", "## Metin içeriği", ""]
    for b in boxes:
        md.append(f"- **`{b.id}`** — {b.text}")
    with open(os.path.join(out_dir, f"typography-spec-{paper}.md"),
              "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(f"  → {P.rel(os.path.join(out_dir, f'typography-spec-{paper}.json'))}")
    print(f"  → {P.rel(os.path.join(out_dir, f'typography-spec-{paper}.md'))}")
    return spec


if __name__ == "__main__":
    import argparse
    import editions as E
    ap = argparse.ArgumentParser()
    E.add_argument(ap)
    ap.add_argument("--paper", default=None, choices=list(S.PAPER_THICKNESS))
    ap.add_argument("--all-papers", action="store_true")
    args = ap.parse_args()
    ed = E.get(args.edition)

    fb = FontBook().build()
    probs = fb.check_glyphs()
    if probs:
        print("!! EKSİK GLİF:")
        for p in probs:
            print("   ", p)
        raise SystemExit(1)

    for paper in (ed.papers if args.all_papers else [args.paper or ed.paper]):
        g = S.geometry_for(ed, paper=paper)
        print(f"\n=== {ed.slug} · {paper.upper()} — kapak {g.cover_w:.4f} x "
              f"{g.cover_h:.4f} inç · sırt {g.spine_w:.4f} ===")
        hdr = (f"{'id':22s} {'font':20s} {'pt':>7s} {'trk':>6s} "
               f"{'x':>8s} {'y':>7s} {'w':>7s} {'cap':>6s}  hiza/döndürme")
        print(hdr)
        print("-" * len(hdr))
        for b in layout(fb, g):
            print(f"{b.id:22s} {b.font:20s} {b.size_pt:7.2f} "
                  f"{b.tracking_em:6.3f} {b.x:8.4f} {b.y:7.4f} {b.w:7.4f} "
                  f"{b.h:6.4f}  {b.align}/{b.rotation}")
        dump(paper, edition=args.edition)
