"""
A+ YERLEŞİM MOTORU — her metin kutusunu ölçümle çözer.
================================================================================
Elle konumlandırma YOK. Her koordinat şu üç girdiden türer:

  1. aplus_spec.py        — modül ölçüsü, tipografi ölçeği, güvenli pay
  2. aplus-plate-analysis — baskın konu kutusu, panel dikdörtgenleri, sessiz
                            bölgeler (hepsi ORAN cinsinden, çözünürlükten bağımsız)
  3. typography.FontBook  — fontun kendi hmtx tablosundan gerçek glif genişlikleri

PUNTO BOYUTU İKİ KISITIN KÜÇÜĞÜDÜR:
    (a) modül yüksekliğine oranlı tavan  (hiyerarşiyi korur)
    (b) kutunun genişliğine tam oturan boyut  (taşmayı imkânsız kılar)
Bu yüzden metin hiçbir koşulda kutusundan taşamaz; taşacaksa küçülür, o da
yetmezse derleme HATA verir — sessizce kırpılmaz.

Koordinat sistemi: PUNTO, orijin modülün SOL ÜST köşesi, `y` TABAN ÇİZGİSİ.
@1x'te 1 punto = 1 piksel (PDF sayfası 970×600 punto olarak kurulur).
"""

from __future__ import annotations
import json
import os
import sys
from dataclasses import dataclass, field, asdict
from typing import List, Optional

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aplus_spec as A          # noqa: E402
import aplus_copy as C          # noqa: E402
import typography as T          # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLATES = os.path.join(ROOT, "07_ASSETS", "aplus_plates")
ANALYSIS = os.path.join(ROOT, "06_REPORTS", "aplus-plate-analysis.json")

GUTTER = 0.030        # konu ile metin sütunu arası boşluk (modül genişliğinin oranı)
PANEL_PAD = 0.085     # panel içi kenar payı (panel genişliğinin oranı)
RULE_GAP = 0.55       # altın ayraç çizgisi ile başlık arası (punto boyutunun katı)


# =============================================================================
# blok modeli
# =============================================================================

@dataclass
class Block:
    id: str
    module: str
    style: str
    font: str
    size_pt: float
    tracking_em: float
    leading_pt: float
    color: str
    align: str                 # left | center | right
    x: float                   # çıpa (align'a göre)
    y: float                   # İLK satırın taban çizgisi
    w: float                   # ölçülen mürekkep genişliği (tek satırda)
    cap: float                 # büyük harf yüksekliği
    lines: List[str] = field(default_factory=list)
    box_w: float = 0.0         # tahsis edilen sütun genişliği
    rule: Optional[dict] = None   # {"x1","x2","y"} altın ayraç

    @property
    def height(self) -> float:
        n = max(len(self.lines), 1)
        return (n - 1) * self.leading_pt + self.cap

    def bbox(self) -> tuple:
        top = self.y - self.cap
        bot = self.y + (len(self.lines) - 1) * self.leading_pt if self.lines \
            else self.y
        wid = self.box_w or self.w
        if self.align == "center":
            x1 = self.x - wid / 2
        elif self.align == "right":
            x1 = self.x - wid
        else:
            x1 = self.x
        return (x1, top, x1 + wid, bot)

    def as_dict(self):
        d = asdict(self)
        for k in ("size_pt", "tracking_em", "leading_pt", "x", "y", "w",
                  "cap", "box_w"):
            d[k] = round(d[k], 3)
        d["bbox"] = [round(v, 3) for v in self.bbox()]
        d["height"] = round(self.height, 3)
        return d


class Overflow(RuntimeError):
    pass


# =============================================================================
# tipografi çözücü
# =============================================================================

class Solver:
    def __init__(self, fb: T.FontBook, mod: A.ModuleDef):
        self.fb, self.m = fb, mod
        self.W, self.H = float(mod.w), float(mod.h)

    def face(self, style):
        return self.fb[A.TYPE_SCALE[style]["font"]]

    def size(self, style: str, text: str = "", box_w: float = 0.0) -> float:
        """(a) yükseklik oranına dayalı tavan ve (b) kutuya sığan boyutun
        küçüğü. text/box_w verilmezse yalnızca (a) uygulanır."""
        sc = A.TYPE_SCALE[style]
        f = self.face(style)
        by_h = sc["cap"] * self.W / f.cap_ratio  # ölçek modül GENİŞLİĞİNE bağlı
        if not text or not box_w:
            return by_h
        by_w = f.size_for_width(text, box_w / 72, sc["track"])
        return min(by_h, by_w)

    def block(self, bid: str, style: str, text, x: float, y: float,
              box_w: float, align: str = "left", color: Optional[str] = None,
              fit: bool = False, size: Optional[float] = None) -> Block:
        sc = A.TYPE_SCALE[style]
        f = self.face(style)
        lines = text if isinstance(text, list) else None

        if size is None:
            if fit:
                probe = max(lines, key=len) if lines else text
                size = self.size(style, probe, box_w)
            else:
                size = self.size(style)
        if lines is None:
            lines = self._wrap(f, text, size, box_w, sc["track"])
            if len(lines) == 1:
                pass
        # taşma kontrolü — sessiz kırpma yok
        for ln in lines:
            wln = f.width(ln, size, sc["track"]) * 72
            if wln > box_w + 0.5:
                raise Overflow(
                    f"{bid}: '{ln[:40]}…' {wln:.1f}pt > sütun {box_w:.1f}pt")

        lead = size * A.leading_for(style)
        widest = max((f.width(ln, size, sc["track"]) * 72 for ln in lines),
                     default=0.0)
        return Block(id=bid, module=self.m.key, style=style,
                     font=sc["font"], size_pt=size, tracking_em=sc["track"],
                     leading_pt=lead, color=color or A.PARCHMENT, align=align,
                     x=x, y=y, w=widest, cap=f.cap_in(size) * 72,
                     lines=lines, box_w=box_w)

    @staticmethod
    def _wrap(face, text: str, size: float, box_w: float, track: float):
        words, out, cur = text.split(), [], ""
        for w in words:
            t = f"{cur} {w}".strip()
            if face.width(t, size, track) * 72 <= box_w or not cur:
                cur = t
            else:
                out.append(cur)
                cur = w
        if cur:
            out.append(cur)
        return out


def stack(solver: Solver, specs, x: float, box_w: float, top: float,
          align: str = "left") -> List[Block]:
    """Blokları dikey olarak yığar. specs: (id, style, text, gap_before, color)

    `gap` MODÜL GENİŞLİĞİNİN oranıdır — bloğun kendi punto boyutunun değil.
    İlk denemede boşluk yeni bloğun punto boyutuyla çarpılıyordu; küçük bir
    künye satırından önceki boşluk da küçülüyor ve alıntıya yapışıyordu.
    Boşluk bir SAYFA ölçüsüdür, bir harf ölçüsü değil."""
    blocks, y = [], top
    for i, (bid, style, text, gap, color) in enumerate(specs):
        y += (gap * solver.W if i else 0)
        b = solver.block(bid, style, text, x, y, box_w,
                         align=align, color=color,
                         fit=style in ("headline", "headline_sm", "figure",
                                       "panel_title", "attrib", "eyebrow"))
        b.y = y + b.cap          # ilk satırın taban çizgisi = üst + cap
        blocks.append(b)
        y = b.y + (len(b.lines) - 1) * b.leading_pt
    return blocks


def column_limit(lum: np.ndarray, side: str, y0: float, y1: float,
                 rise: float = 0.32, win: float = 0.022) -> float:
    """Metin sütununun bitmesi gereken x oranını ÖLÇEREK bulur.

    Baskın-konu kutusuna güvenmek yetmedi: m5'te kutu yalnızca ortadaki
    kitabın parlak çekirdeğini kapsıyordu, kenardaki sayfalar dışarıda kalıyor
    ve alt yazılar kitapların üstüne biniyordu. Burada doğrudan ÇARPIŞMA SINIRI
    aranıyor: metnin geçeceği yatay bandın sütun parlaklığı profilinde,
    zeminden belirgin biçimde yükselen ilk nokta.
    """
    H, W = lum.shape
    band = lum[max(int(y0 * H), 0):min(int(y1 * H), H), :]
    if band.size == 0:
        return 1.0
    prof = band.mean(axis=0)
    k = max(3, int(W * win))
    prof = np.convolve(prof, np.ones(k) / k, mode="same")
    bg = float(np.percentile(prof, 20))
    thr = bg + rise * (float(prof.max()) - bg)
    idx = range(W) if side == "left" else range(W - 1, -1, -1)
    for i in idx:
        if prof[i] > thr:
            return i / W
    return 1.0 if side == "left" else 0.0


def recentre(blocks: List[Block], top: float, bottom: float,
             optical: float = 0.045):
    """Blok grubunu dikeyde ortalar; optik olarak biraz yukarı çeker."""
    if not blocks:
        return
    t = min(b.bbox()[1] for b in blocks)
    bo = max(b.bbox()[3] for b in blocks)
    h = bo - t
    want = top + (bottom - top - h) / 2 - (bottom - top) * optical
    d = want - t
    for b in blocks:
        b.y += d
        if b.rule:
            b.rule["y"] += d


# =============================================================================
# yapı tespiti (hücreler)
# =============================================================================

def _plate(key: str) -> np.ndarray:
    p = os.path.join(PLATES, f"{key}@1x.png")
    return np.asarray(Image.open(p).convert("RGB")).astype(float).mean(axis=2)


def detect_cells(profile: np.ndarray, bright_gap: bool, n: int = 3,
                 tol: float = 0.35):
    """Ayırıcıları bulup profili n hücreye böler.
    Hücreler eşitten %35'ten fazla saparsa EŞİT BÖLMEYE düşer — sanat eserinin
    aydınlatması yanıltıcı olabiliyor (m5'te alt sayfa koyu olduğu için
    ayırıcı sanılıyordu)."""
    L = len(profile)
    k = max(3, int(L * 0.012))
    s = np.convolve(profile, np.ones(k) / k, mode="same")
    sig = s if bright_gap else -s
    lo, hi = int(L * 0.12), int(L * 0.88)
    win = sig[lo:hi]
    on = win > np.percentile(win, 72)
    runs, cur = [], None
    for i, v in enumerate(on):
        if v and cur is None:
            cur = i
        elif not v and cur is not None:
            if i - cur >= L * 0.02:
                runs.append((cur + lo, i + lo))
            cur = None
    if cur is not None:
        runs.append((cur + lo, hi))
    runs = sorted(runs, key=lambda t: -(t[1] - t[0]))[:n - 1]
    runs.sort()

    if len(runs) == n - 1:
        edges = [0] + [(a + b) // 2 for a, b in runs] + [L]
        sizes = [edges[i + 1] - edges[i] for i in range(n)]
        if max(sizes) / min(sizes) <= 1 + tol * 2:
            return [(edges[i] / L, edges[i + 1] / L) for i in range(n)], "tespit"
    step = 1.0 / n
    return [(i * step, (i + 1) * step) for i in range(n)], "eşit bölme"


# =============================================================================
# modül yerleşimleri
# =============================================================================

def detect_plinths(lum: np.ndarray, cells, H: int,
                   y0: float = 0.70, y1: float = 0.84):
    """Her hücrenin içinde kaidenin gövdesini bulur.

    Kaide yüzü çevresinden KOYUdur (ışık üstten geliyor). Hücre başına
    kısıtlanmış arama, üçünü de güvenilir biçimde bulur — küresel arama
    ortadaki spot ışıklı kaideyi kaçırıyordu."""
    Hp, W = lum.shape
    band = lum[int(Hp * y0):int(Hp * y1)].mean(axis=0)
    out = []
    for (c0, c1) in cells:
        a, b = int(c0 * W), int(c1 * W)
        seg = band[a:b]
        if seg.size < 8:
            out.append((c0, c1))
            continue
        thr = np.percentile(seg, 50)
        on = seg < thr
        runs, cur = [], None
        for i, v in enumerate(on):
            if v and cur is None:
                cur = i
            elif not v and cur is not None:
                runs.append((cur, i))
                cur = None
        if cur is not None:
            runs.append((cur, len(on)))
        if not runs:
            out.append((c0, c1))
            continue
        r = max(runs, key=lambda t: t[1] - t[0])
        # Bulunan koyu koşu hücrenin en az %40'ı değilse kaide değil, gölgedir:
        # hücrenin orta %62'sine düş.
        if (r[1] - r[0]) < 0.40 * seg.size:
            pad = 0.19 * (c1 - c0)
            out.append((c0 + pad, c1 - pad))
        else:
            out.append(((a + r[0]) / W, (a + r[1]) / W))
    return out


def _load_analysis():
    with open(ANALYSIS, encoding="utf-8") as f:
        return {m["key"]: m for m in json.load(f)["modules"]}


def layout_module(fb: T.FontBook, m: A.ModuleDef, an: dict) -> List[Block]:
    s = Solver(fb, m)
    W, H = s.W, s.H
    sm = A.SAFE_MARGIN_FRAC
    cp = C.MODULE_COPY[m.key]
    blocks: List[Block] = []

    # ---------------------------------------------------------------- LEFT
    if m.text_side == "left":
        lum = _plate(m.key)
        edge = column_limit(lum, "left", 0.12, 0.88)
        x0 = sm * W
        box_w = max((edge - GUTTER) * W - x0, W * 0.22)

        if m.key == "m1-header":
            specs = [("eyebrow", "eyebrow", cp["eyebrow"], 0.000, A.DIM),
                     ("headline", "headline", cp["headline"], 0.022, A.GOLD),
                     ("subhead", "subhead", cp["subhead"], 0.028, A.PARCHMENT)]
        else:
            specs = [("eyebrow", "eyebrow", cp["eyebrow"], 0.000, A.DIM),
                     ("quote", "quote", cp["quote"], 0.022, A.PARCHMENT),
                     ("attrib", "attrib", cp["attrib"], 0.034, A.GOLD),
                     ("note", "caption", cp["note"], 0.016, A.DIM)]
        blocks = stack(s, specs, x0, box_w, sm * H)
        recentre(blocks, sm * H, (1 - sm) * H)

    # -------------------------------------------------------------- PANELS
    elif m.text_side == "panels":
        panels = an["panels_frac"]
        if len(panels) != len(cp["panels"]):
            raise Overflow(f"{m.key}: {len(panels)} panel bulundu, "
                           f"{len(cp['panels'])} metin var")
        for i, (p, txt) in enumerate(zip(panels, cp["panels"]), 1):
            px, py = p["x"] * W, p["y"] * H
            pw, ph = p["w"] * W, p["h"] * H
            pad = PANEL_PAD * pw
            # Metin kutusu İKİ kısıtın kesişiminde olmalı:
            #   (1) panelin içinde — sanat eserinin çizdiği çerçeve
            #   (2) modülün güvenli alanında — panelin sağ kenarı güvenli paydan
            #       daha dışarıda başlıyor, kırpma sonrası üst panelin y'si de
            #       negatife düşüyor
            tx = max(px + pad, sm * W)
            tx2 = min(px + pw - pad, (1 - sm) * W)
            top = max(py + pad, sm * H)
            bot = min(py + ph - pad, (1 - sm) * H)
            grp = stack(s, [
                (f"p{i}.title", "panel_title", txt["title"], 0.0, A.GOLD),
                (f"p{i}.body", "body_sm", txt["body"], 0.016, A.PARCHMENT),
            ], tx, tx2 - tx, top)
            if grp[0].bbox()[1] < top - 0.5 or grp[-1].bbox()[3] > bot + 0.5:
                recentre(grp, top, bot, optical=0.0)
            else:
                recentre(grp, top, bot, optical=0.02)
            # başlığın altına altın ayraç
            t0 = grp[0]
            grp[0].rule = {"x1": tx, "x2": tx2,
                           "y": t0.y + t0.cap * RULE_GAP}
            blocks += grp

    # ------------------------------------------------------------- COLUMNS
    elif m.text_side == "columns":
        lum = _plate(m.key)
        prof = lum[int(H * 0.66):int(H * 0.88)].mean(axis=0)
        cells, how = detect_cells(prof, bright_gap=True, n=3)
        m3 = cp
        head = s.block("headline", "headline_sm", m3["headline"], W / 2,
                       0, W * 0.52, align="center", color=A.GOLD, fit=True)
        head.y = sm * H + head.cap
        blocks.append(head)
        # Etiketler KAİDE yüzüne oturmalı, hücrenin tamamına değil: hücre
        # duvarı da kapsıyor ve etiket kaidenin dışına taşıyordu.
        plinths = detect_plinths(lum, cells, H)
        for i, (cell, col, pl) in enumerate(zip(cells, m3["columns"], plinths), 1):
            cx = (pl[0] + pl[1]) / 2 * W
            # Kaide MERKEZİ hizalamayı belirler; genişlik biraz taşabilir —
            # koyu duvara birkaç piksel taşmak sorun değil, hücrenin tamamına
            # yayılmak sorundu.
            cw = min((pl[1] - pl[0]) * 1.02, (cell[1] - cell[0]) * 0.88) * W
            emph = col.get("emphasis")
            grp = stack(s, [
                (f"c{i}.label", "panel_title", col["label"], 0.0,
                 A.GOLD if emph else A.DIM),
                (f"c{i}.lines", "body_sm", col["lines"], 0.014,
                 A.PARCHMENT if emph else A.DIM),
            ], cx, cw, H * 0.716, align="center")
            grp[0].rule = {"x1": cx - cw * 0.30, "x2": cx + cw * 0.30,
                           "y": grp[0].y - grp[0].cap * 1.55}
            blocks += grp
        blocks[0].__dict__["_cells_how"] = how

    # ---------------------------------------------------------------- ROWS
    elif m.text_side == "rows":
        lum = _plate(m.key)
        prof = lum[:, int(W * 0.28):int(W * 0.72)].mean(axis=1)
        cells, how = detect_cells(prof, bright_gap=False, n=3)
        x0 = sm * W
        # Her satırın sütun sınırı AYRI ölçülür: kitap sayfaları farklı
        # satırlarda farklı x'te başlıyor.
        eb_edge = column_limit(lum, "left", 0.0, cells[0][0] + 0.02)
        box_eb = max((eb_edge - GUTTER) * W - x0, W * 0.16)
        eb = s.block("eyebrow", "eyebrow", cp["eyebrow"], x0, 0, box_eb,
                     color=A.DIM, fit=True)
        eb.y = sm * H + eb.cap
        blocks.append(eb)
        for i, (cell, cap_txt) in enumerate(zip(cells, cp["captions"]), 1):
            top, bot = cell[0] * H, cell[1] * H
            edge = column_limit(lum, "left", cell[0], cell[1])
            bw = max((edge - GUTTER) * W - x0, W * 0.16)
            grp = stack(s, [(f"r{i}.caption", "caption", cap_txt, 0.0,
                             A.PARCHMENT)], x0, bw, top)
            recentre(grp, top, bot, optical=0.0)
            g = grp[0]
            g.rule = {"x1": x0, "x2": x0 + bw * 0.32,
                      "y": g.bbox()[1] - g.cap * 0.95}
            blocks += grp
        blocks[0].__dict__["_cells_how"] = how

    return blocks


def build(fb: Optional[T.FontBook] = None) -> dict:
    fb = fb or T.FontBook().build()
    ana = _load_analysis()
    out = {"modules": []}
    for m in A.MODULES:
        if m.key not in ana:
            continue
        blocks = layout_module(fb, m, ana[m.key])
        # çarpışma kontrolü: metin baskın konunun üstüne binmesin
        subj = ana[m.key].get("subject_frac")
        clashes = []
        if subj and m.text_side in ("left", "rows"):
            sx1, sy1 = subj["x"] * m.w, subj["y"] * m.h
            sx2 = sx1 + subj["w"] * m.w
            sy2 = sy1 + subj["h"] * m.h
            for b in blocks:
                x1, y1, x2, y2 = b.bbox()
                if not (x2 <= sx1 or x1 >= sx2 or y2 <= sy1 or y1 >= sy2):
                    clashes.append(b.id)
        out["modules"].append({
            "key": m.key, "type": m.type, "w": m.w, "h": m.h,
            "alt_text": C.ALT_TEXT[m.key],
            "blocks": [b.as_dict() for b in blocks],
            "collisions": clashes,
        })
    return out


if __name__ == "__main__":
    d = build()
    for mod in d["modules"]:
        print(f"\n═══ {mod['key']}  {mod['w']}×{mod['h']}"
              + ("  ⚠ ÇAKIŞMA: " + ", ".join(mod["collisions"])
                 if mod["collisions"] else ""))
        print(f"   {'id':16s} {'stil':12s} {'font':22s} {'pt':>6s} "
              f"{'x':>7s} {'y':>7s} {'genişlik':>9s} satır")
        for b in mod["blocks"]:
            print(f"   {b['id']:16s} {b['style']:12s} {b['font']:22s} "
                  f"{b['size_pt']:6.2f} {b['x']:7.1f} {b['y']:7.1f} "
                  f"{b['box_w']:9.1f} {len(b['lines'])}")
    os.makedirs(os.path.join(ROOT, "03_APLUS", "spec"), exist_ok=True)
    p = os.path.join(ROOT, "03_APLUS", "spec", "aplus-layout.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"\n→ 03_APLUS/spec/aplus-layout.json")
