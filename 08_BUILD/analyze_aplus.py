"""
A+ GÖRSEL ANALİZİ — kırpma ve yerleşim kararlarını ölçümle üretir.
================================================================================
Kullanıcıdan hiçbir koordinat istenmez. Her şey pikselden hesaplanır:

  * boyut, en-boy oranı
  * PARLAKLIK / KONTRAST / DOKU YOĞUNLUĞU  (ızgara üzerinde)
  * BELİRGİNLİK (saliency) haritası = ışık × yerel kontrast × doygunluk
      → sanat eserinde konu aydınlatılmış ve altın; zemin koyu ve düz.
  * BASKIN KONU kutusu = belirginlik kütlesinin %85'ini kapsayan en küçük kutu
  * NEGATİF ALAN maskesi = belirginliği ve dokusu düşük hücreler
  * METİN GÜVENLİ DİKDÖRTGENLERİ = negatif alandaki en büyük boş dikdörtgenler
      (histogram tabanlı "largest rectangle in binary matrix" algoritması,
       bulunan her dikdörtgen maskelenip bir sonraki aranır)
  * ÇARPIŞMA BÖLGELERİ = belirginliği yüksek hücreler

Çıktı: 06_REPORTS/aplus-analysis.json + konsol raporu (+ isteğe bağlı görsel)

Kullanım:
    python3 08_BUILD/analyze_aplus.py [--overlay]
"""

from __future__ import annotations
import argparse
import json
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aplus_spec as A  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "07_ASSETS", "aplus_raw")

GRID_W = 128         # analiz ızgarasının yatay hücre sayısı
SUBJECT_PCT = 14     # en parlak %14 hücre → baskın konu adayı
QUIET_SAL_PCT = 46   # belirginlik bu yüzdeliğin altındaysa "sessiz"
QUIET_STD_PCT = 62   # yerel kontrast bu yüzdeliğin altındaysa "düz"
VERY_DARK = 30       # bu parlaklığın altındaki hücre dokusuna bakılmaksızın sessiz


# =============================================================================
# yardımcılar
# =============================================================================

def _load(path: str) -> np.ndarray:
    im = Image.open(path)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        flat = Image.new("RGB", im.size, (0, 0, 0))
        flat.paste(im, mask=im.split()[-1])
        im = flat
    return np.asarray(im.convert("RGB")).astype(np.float64)


def _blockify(a: np.ndarray, gh: int, gw: int) -> np.ndarray:
    """Diziyi gh × gw hücreye böler ve her hücrenin ortalamasını döndürür."""
    H, W = a.shape[:2]
    ys = np.linspace(0, H, gh + 1).astype(int)
    xs = np.linspace(0, W, gw + 1).astype(int)
    out = np.zeros((gh, gw))
    for i in range(gh):
        for j in range(gw):
            blk = a[ys[i]:ys[i + 1], xs[j]:xs[j + 1]]
            out[i, j] = blk.mean() if blk.size else 0.0
    return out


def _grid_std(lum: np.ndarray, gh: int, gw: int) -> np.ndarray:
    H, W = lum.shape
    ys = np.linspace(0, H, gh + 1).astype(int)
    xs = np.linspace(0, W, gw + 1).astype(int)
    out = np.zeros((gh, gw))
    for i in range(gh):
        for j in range(gw):
            blk = lum[ys[i]:ys[i + 1], xs[j]:xs[j + 1]]
            out[i, j] = blk.std() if blk.size else 0.0
    return out


def _norm(a: np.ndarray) -> np.ndarray:
    lo, hi = float(a.min()), float(a.max())
    return (a - lo) / (hi - lo) if hi > lo else np.zeros_like(a)


def largest_rect(mask: np.ndarray):
    """İkili matriste en büyük dolu (True) dikdörtgen — O(satır × sütun).
    Döndürür: (alan, üst, sol, alt_dışlayan, sağ_dışlayan)"""
    gh, gw = mask.shape
    heights = np.zeros(gw, dtype=int)
    best = (0, 0, 0, 0, 0)
    for i in range(gh):
        heights = np.where(mask[i], heights + 1, 0)
        stack = []          # (başlangıç sütunu, yükseklik)
        for j in range(gw + 1):
            h = heights[j] if j < gw else 0
            start = j
            while stack and stack[-1][1] >= h:
                s, hh = stack.pop()
                area = hh * (j - s)
                if area > best[0]:
                    best = (area, i - hh + 1, s, i + 1, j)
                start = s
            stack.append((start, h))
    return best


def majority(mask: np.ndarray, passes: int = 2) -> np.ndarray:
    """3×3 çoğunluk süzgeci. Tek tük sapan hücreler koca bir sessiz bölgeyi
    ikiye bölmesin diye — açgözlü dikdörtgen arayışının asıl kırılma noktası
    buydu."""
    m = mask.astype(np.int8)
    for _ in range(passes):
        p = np.pad(m, 1, mode="edge")
        s = sum(p[i:i + m.shape[0], j:j + m.shape[1]]
                for i in range(3) for j in range(3))
        m = (s >= 5).astype(np.int8)
    return m.astype(bool)


def label(mask: np.ndarray) -> tuple:
    """4-komşuluk bağlantılı bileşen etiketleme (union-find)."""
    gh, gw = mask.shape
    par = {}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            par[rb] = ra

    lab = np.zeros((gh, gw), dtype=int)
    nxt = 1
    for i in range(gh):
        for j in range(gw):
            if not mask[i, j]:
                continue
            up = lab[i - 1, j] if i > 0 else 0
            lf = lab[i, j - 1] if j > 0 else 0
            if up and lf:
                lab[i, j] = min(up, lf)
                union(min(up, lf), max(up, lf))
            elif up or lf:
                lab[i, j] = up or lf
            else:
                lab[i, j] = nxt
                par[nxt] = nxt
                nxt += 1
    for i in range(gh):
        for j in range(gw):
            if lab[i, j]:
                lab[i, j] = find(lab[i, j])
    ids = [v for v in np.unique(lab) if v]
    return lab, ids


def detect_panels(a: np.ndarray, side: str = "right",
                  span: float = 0.42) -> list:
    """Sanat eserinin KENDİ çizdiği altın çerçeveli panelleri bulur.

    module-2'de üç panel zaten çizilmiş durumda; genel "sessiz bölge" arayışı
    bunları tek bir koyu kütle sanıp birleştiriyor. Panelleri ayıran şey altın
    filetolardır — o hâlde filetoları arayalım: altın maskesini satırlara ve
    sütunlara izdüşürüp tepe noktalarını panel sınırı olarak alırız."""
    H, W, _ = a.shape
    x0 = int(W * (1 - span)) if side == "right" else 0
    x1 = W if side == "right" else int(W * span)
    sub = a[:, x0:x1]
    r, g, b = sub[..., 0], sub[..., 1], sub[..., 2]
    gold = (r > 62) & (r - b > 22) & (g > b)

    rows = gold.mean(axis=1)
    cols = gold.mean(axis=0)

    def peaks(sig, min_frac_, min_gap):
        thr = max(min_frac_, float(np.percentile(sig, 96)) * 0.45)
        idx = np.where(sig >= thr)[0]
        if not len(idx):
            return []
        groups, cur = [], [idx[0]]
        for v in idx[1:]:
            if v - cur[-1] <= min_gap:
                cur.append(v)
            else:
                groups.append(cur)
                cur = [v]
        groups.append(cur)
        return [int(np.mean(gp)) for gp in groups]

    hbounds = peaks(rows, 0.30, max(3, H // 120))
    vbounds = peaks(cols, 0.30, max(3, (x1 - x0) // 120))
    if len(hbounds) < 4 or len(vbounds) < 2:
        return []

    left = x0 + vbounds[0]
    right = x0 + vbounds[-1]
    panels = []
    for i in range(len(hbounds) - 1):
        top, bot = hbounds[i], hbounds[i + 1]
        if bot - top < H * 0.10:      # ince aralıkları at, panelleri tut
            continue
        panels.append({"x": int(left), "y": int(top),
                       "w": int(right - left), "h": int(bot - top)})
    return panels


def find_safe_rects(mask: np.ndarray, n: int = 4, min_frac: float = 0.010):
    """Sessiz bölgeleri BAĞLANTILI BİLEŞEN olarak ayırır ve her bileşenin içine
    sığan en büyük dikdörtgeni bulur.

    Açgözlü küresel arama yerine bu yöntem gerekiyor: module-2'de sanat eserinin
    kendi üç paneli üç ayrı bileşendir; küresel arama bunları parçalıyordu."""
    m = majority(mask)
    lab, ids = label(m)
    total = m.size
    out = []
    for cid in ids:
        comp = lab == cid
        if comp.sum() / total < min_frac * 0.6:
            continue
        area, r0, c0, r1, c1 = largest_rect(comp)
        if area / total < min_frac:
            continue
        out.append({"r0": int(r0), "c0": int(c0), "r1": int(r1), "c1": int(c1),
                    "cells": int(area)})
    out.sort(key=lambda r: -r["cells"])
    return out[:n]


# =============================================================================
# tek görselin analizi
# =============================================================================

def analyze(path: str, grid_w: int = GRID_W,
            want_panels: bool = False) -> dict:
    a = _load(path)
    H, W, _ = a.shape
    lum = a.mean(axis=2)

    gw = grid_w
    gh = max(4, int(round(grid_w * H / W)))

    # --- temel istatistikler ---
    mx = a.max(axis=2)
    mn = a.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0.0)
    gx = np.abs(np.diff(lum, axis=1, prepend=lum[:, :1]))
    gy = np.abs(np.diff(lum, axis=0, prepend=lum[:1, :]))
    grad = gx + gy

    g_lum = _blockify(lum, gh, gw)
    g_sat = _blockify(sat, gh, gw)
    g_grad = _blockify(grad, gh, gw)
    g_std = _grid_std(lum, gh, gw)

    # --- belirginlik: ışık × yerel kontrast × doygunluk ---
    sal = (_norm(g_lum) ** 1.15) * (0.55 + 0.45 * _norm(g_std)) \
        * (0.65 + 0.35 * _norm(g_sat))
    sal = _norm(sal)

    # --- baskın konu kutusu ---
    # Belirginlik kütlesinin %85'ini almak diffüz görsellerde tüm kareyi
    # kapsıyordu. Bunun yerine yüksek eşik + EN BÜYÜK BAĞLANTILI BİLEŞEN:
    # "asıl konu" tek bir aydınlatılmış kütledir, dağınık parıltılar değil.
    hot = majority(sal >= np.percentile(sal, 100 - SUBJECT_PCT), passes=1)
    subj = None
    if hot.any():
        lab_h, ids_h = label(hot)
        big = max(ids_h, key=lambda c: int((lab_h == c).sum()))
        ys, xs = np.where(lab_h == big)
        subj = {"r0": int(ys.min()), "c0": int(xs.min()),
                "r1": int(ys.max()) + 1, "c1": int(xs.max()) + 1}

    # --- negatif alan: belirginlik düşük VE (doku düşük VEYA hücre çok koyu) ---
    # "Çok koyu" istisnası şart: m4'ün sol üstünde duvar dokusu var ama zemin
    # o kadar karanlık ki üstüne yazılan açık renk metin sorunsuz okunuyor.
    quiet = (sal < np.percentile(sal, QUIET_SAL_PCT)) & (
        (g_std < np.percentile(g_std, QUIET_STD_PCT)) | (g_lum < VERY_DARK))
    rects = find_safe_rects(quiet, n=5)
    # Panel dedektörü yalnızca sanat eserinde gerçekten çizili panel varsa
    # çalıştırılır; aksi hâlde rastgele altın parıltıları panel sanır.
    panels = detect_panels(a, side="right") if want_panels else []

    def to_px(r):
        return {
            "x": round(r["c0"] / gw * W), "y": round(r["r0"] / gh * H),
            "w": round((r["c1"] - r["c0"]) / gw * W),
            "h": round((r["r1"] - r["r0"]) / gh * H),
            "x_frac": round(r["c0"] / gw, 4), "y_frac": round(r["r0"] / gh, 4),
            "w_frac": round((r["c1"] - r["c0"]) / gw, 4),
            "h_frac": round((r["r1"] - r["r0"]) / gh, 4),
        }

    # --- yarım / üçte bir bölge özetleri (metin hangi tarafa gider) ---
    half = gw // 2
    third = gw // 3
    zones = {
        "left_half": float(sal[:, :half].mean()),
        "right_half": float(sal[:, half:].mean()),
        "left_third": float(sal[:, :third].mean()),
        "mid_third": float(sal[:, third:2 * third].mean()),
        "right_third": float(sal[:, 2 * third:].mean()),
        "top_third": float(sal[:gh // 3].mean()),
        "bottom_third": float(sal[2 * gh // 3:].mean()),
    }

    return {
        "file": os.path.basename(path),
        "w": W, "h": H, "aspect": round(W / H, 4),
        "grid": [gh, gw],
        "stats": {
            "brightness_mean": round(float(lum.mean()), 2),
            "brightness_p95": round(float(np.percentile(lum, 95)), 2),
            "contrast_std": round(float(lum.std()), 2),
            "texture_density": round(float(grad.mean()), 3),
            "saturation_mean": round(float(sat.mean()), 4),
            "dark_frac": round(float((lum < 40).mean()), 4),
        },
        "subject_box": to_px(subj) if subj else None,
        "safe_rects": [to_px(r) for r in rects],
        "panels": panels,
        "zone_saliency": {k: round(v, 4) for k, v in zones.items()},
        "collision_frac": round(float(hot.mean()), 4),
        "_grids": {"sal": sal.tolist(), "quiet": quiet.astype(int).tolist()},
    }


# =============================================================================
# kırpma çözümü
# =============================================================================

def solve_crop(an: dict, target_ar: float, anchor: str,
               bias: str = "center") -> dict:
    """Hedef en-boy oranına ulaşmak için kırpma penceresi hesaplar.
    Baskın konuyu ve metin alanını korumaya çalışır."""
    W, H, ar = an["w"], an["h"], an["aspect"]
    subj = an["subject_box"]

    if abs(ar - target_ar) < 1e-6:
        return {"x": 0, "y": 0, "w": W, "h": H, "mode": "none",
                "lost_frac": 0.0}

    if ar > target_ar:
        # görsel fazla geniş → yatay kırp
        nw, nh = int(round(H * target_ar)), H
        if anchor == "left":
            x = 0
        elif anchor == "right":
            x = W - nw
        else:
            # konu merkezini koru, sınırlara sıkıştır
            cx = (subj["x"] + subj["w"] / 2) if subj else W / 2
            x = int(round(cx - nw / 2))
        x = max(0, min(W - nw, x))
        y, mode = 0, "horizontal"
    else:
        # görsel fazla uzun → dikey kırp
        nw, nh = W, int(round(W / target_ar))
        if bias == "subject" and subj:
            cy = subj["y"] + subj["h"] / 2
        else:
            cy = H / 2
        y = int(round(cy - nh / 2))
        y = max(0, min(H - nh, y))
        x, mode = 0, "vertical"

    lost = 1 - (nw * nh) / (W * H)
    keep = 1.0
    if subj:
        ix = max(0, min(x + nw, subj["x"] + subj["w"]) - max(x, subj["x"]))
        iy = max(0, min(y + nh, subj["y"] + subj["h"]) - max(y, subj["y"]))
        keep = (ix * iy) / max(subj["w"] * subj["h"], 1)

    return {"x": x, "y": y, "w": nw, "h": nh, "mode": mode,
            "lost_frac": round(lost, 4), "subject_kept": round(keep, 4)}


# =============================================================================
# ana akış
# =============================================================================

def main(overlay: bool = False):
    if not os.path.isdir(RAW):
        raise SystemExit(f"kaynak klasör yok: {RAW}")

    out = {"source_dir": os.path.relpath(RAW, ROOT), "modules": []}
    print("=" * 100)
    print("A+ GÖRSEL ANALİZİ")
    print("=" * 100)

    for m in A.MODULES:
        p = os.path.join(RAW, m.source)
        if not os.path.exists(p):
            print(f"\n!! kaynak yok: {m.source}")
            continue
        an = analyze(p, want_panels=(m.text_side == "panels"))
        crop = solve_crop(an, m.ar, m.anchor, m.crop_bias)
        z = an["zone_saliency"]
        measured_side = "left" if z["left_half"] < z["right_half"] else "right"

        rec = {"key": m.key, "module_type": m.type,
               "target": [m.w, m.h], "target_ar": round(m.ar, 4),
               "analysis": {k: v for k, v in an.items() if k != "_grids"},
               "crop": crop, "measured_quiet_side": measured_side,
               "declared_text_side": m.text_side}
        out["modules"].append(rec)

        s = an["stats"]
        print(f"\n── {m.key}  ({m.source})")
        print(f"   {an['w']}×{an['h']} px  AR {an['aspect']}  →  hedef "
              f"{m.w}×{m.h} (AR {m.ar:.4f})")
        print(f"   parlaklık {s['brightness_mean']:.1f} · kontrast "
              f"{s['contrast_std']:.1f} · doku {s['texture_density']:.2f} · "
              f"koyu alan %{s['dark_frac']*100:.0f}")
        if an["subject_box"]:
            b = an["subject_box"]
            print(f"   baskın konu: x {b['x']}..{b['x']+b['w']} "
                  f"y {b['y']}..{b['y']+b['h']}  "
                  f"(%{b['x_frac']*100:.0f}–%{(b['x_frac']+b['w_frac'])*100:.0f} "
                  f"yatay)")
        print(f"   sessiz taraf: {measured_side}  (sol {z['left_half']:.3f} / "
              f"sağ {z['right_half']:.3f})  · beyan: {m.text_side}")
        print(f"   kırpma: {crop['mode']} → x{crop['x']} y{crop['y']} "
              f"{crop['w']}×{crop['h']}  kayıp %{crop['lost_frac']*100:.1f}"
              + (f"  konu korunumu %{crop['subject_kept']*100:.0f}"
                 if "subject_kept" in crop else ""))
        for i, q in enumerate(an.get("panels") or [], 1):
            print(f"   panel {i}: {q['w']}×{q['h']} px @ ({q['x']},{q['y']})")
        for i, r in enumerate(an["safe_rects"][:3], 1):
            print(f"   güvenli alan {i}: {r['w']}×{r['h']} px @ "
                  f"({r['x']},{r['y']})  = %{r['w_frac']*100:.0f}×"
                  f"%{r['h_frac']*100:.0f}")

        if overlay:
            _overlay(p, an, crop, m.key)

    dst = os.path.join(ROOT, "06_REPORTS", "aplus-analysis.json")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\n→ 06_REPORTS/aplus-analysis.json")


def _overlay(path, an, crop, key):
    from PIL import ImageDraw
    im = Image.open(path).convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    if an["subject_box"]:
        b = an["subject_box"]
        d.rectangle([b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]],
                    outline=(228, 87, 46, 255), width=6)
    for i, r in enumerate(an["safe_rects"][:3]):
        c = [(61, 190, 123, 255), (91, 141, 239, 255), (232, 182, 39, 255)][i]
        d.rectangle([r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"]],
                    outline=c, width=5)
    d.rectangle([crop["x"], crop["y"], crop["x"] + crop["w"],
                 crop["y"] + crop["h"]], outline=(255, 255, 255, 220), width=4)
    o = os.path.join(ROOT, "09_ARCHIVE", "aplus-analysis-overlays")
    os.makedirs(o, exist_ok=True)
    im.save(os.path.join(o, f"{key}.jpg"), quality=86)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--overlay", action="store_true",
                    help="analiz kutularını görselin üstüne çizip kaydet")
    main(**vars(ap.parse_args()))
