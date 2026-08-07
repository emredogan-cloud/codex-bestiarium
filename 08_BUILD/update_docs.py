#!/usr/bin/env python3
"""
CODEX BESTIARIUM — OTOMATİK BELGE GÜNCELLEYİCİ
================================================================================
`BOOK_STATS.md` ve `ROADMAP_PROGRESS.md` ELLE YAZILMAZ. İkisi de spec.json,
book.json, dosya sistemi ve git geçmişinden TÜRETİLİR.

Neden? Çünkü "her faz sonunda güncelle, asla unutma" bir disiplin talebidir ve
disiplin unutulur. Mekanizma unutmaz:

    python3 08_BUILD/update_docs.py            # yeniden üret
    python3 08_BUILD/update_docs.py --check    # güncel mi? değilse çıkış 1

CI `--check` çalıştırır. Belgeler bayatsa derleme KIRMIZI yanar. Böylece
belgeyi güncellemek bir hatırlama işi olmaktan çıkıp bir kapı olur.

`CHANGELOG.md` ve `PROJECT_CONTEXT.md` elle yazılır (editoryal karar içerirler)
ama bu betik ikisinin de tarih damgasını ve faz satırını denetler.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    PLATES_DIR,
    RESEARCH_DIR,
    ROOT,
    SCOPE_FLOOR,
    STATUS_ORDER,
    TARGET_CREATURES,
    TARGET_PAGES,
    TARGET_TRADITIONS,
    TARGET_WORDS,
    VERIFY_FLOOR,
    WORD_BAND,
    load_book,
    load_spec,
)
from textutil import iter_entries, word_count  # noqa: E402

STATS_PATH = os.path.join(ROOT, "BOOK_STATS.md")
PROGRESS_PATH = os.path.join(ROOT, "ROADMAP_PROGRESS.md")

GENERATED = (
    "<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/update_docs.py · ELLE DÜZENLEMEYİN -->"
)

# Uygulama yol haritasındaki altı faz. Tek doğruluk kaynağı roadmap'tir;
# burası yalnızca ilerleme ölçümü için gereken makine okunur özettir.
PHASES = [
    {
        "n": 1, "tag": "v0.1.0",
        "title": "Altyapı, Araştırma ve Kapsam Kilidi",
        "gate": "phase1",
        "milestone": "Faz 1 · Temel",
    },
    {
        "n": 2, "tag": "v0.2.0",
        "title": "Tasnif, Veri Modeli ve Pilot Plaka Seti",
        "gate": "phase2",
        "milestone": "Faz 2 · Veri",
    },
    {
        "n": 3, "tag": "v0.3.0",
        "title": "Çekirdek Yazım · Bekçiler ve Yutucular",
        "gate": "phase3",
        "milestone": "Faz 3 · Çekirdek",
    },
    {
        "n": 4, "tag": "v0.4.0",
        "title": "Genişleme · Şekil Değiştirenler ve Su Sakinleri",
        "gate": "phase3",
        "milestone": "Faz 4 · Genişleme",
    },
    {
        "n": 5, "tag": "v0.5.0",
        "title": "Tamamlama, İllüstrasyon ve Editoryal İnceleme",
        "gate": "phase3",
        "milestone": "Faz 5 · Tamamlama",
    },
    {
        "n": 6, "tag": "v1.0.0",
        "title": "Üretim, KDP ve Lansman",
        "gate": "phase3",
        "milestone": "Faz 6 · Üretim",
    },
]

# Faz başına yazılacak madde aralığı (sınıf sırasına göre)
PHASE_CLASSES = {3: ["I", "II"], 4: ["III", "IV"], 5: ["V", "VI"]}


def today() -> str:
    return dt.date.today().isoformat()


def git(*args: str) -> str:
    try:
        return subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception:  # noqa: BLE001
        return ""


def bar(done: int, total: int, width: int = 24) -> str:
    if total <= 0:
        return "·" * width
    filled = round(width * done / total)
    return "█" * filled + "░" * (width - filled)


# =============================================================================
# ÖLÇÜM
# =============================================================================

def gather() -> dict:
    spec = load_spec()
    creatures = spec["creatures"]
    book = load_book()

    by_status = collections.Counter(c["status"] for c in creatures)
    by_class = collections.Counter(c["class"] for c in creatures)
    by_kin = collections.Counter(c["kinFamily"] for c in creatures if c["kinFamily"])
    by_region = collections.Counter(
        t["regionGroup"] for t in spec["traditions"]
    )

    verified = sum(by_status[s] for s in STATUS_ORDER[1:])
    written = sum(by_status[s] for s in ("written", "edited", "final"))

    research_files = 0
    if os.path.isdir(RESEARCH_DIR):
        research_files = len(
            [f for f in os.listdir(RESEARCH_DIR)
             if f.endswith(".md") and not f.startswith("_")]
        )

    plates = 0
    if os.path.isdir(PLATES_DIR):
        plates = len([f for f in os.listdir(PLATES_DIR) if f.lower().endswith(".png")])

    sourced = sum(
        1 for c in creatures
        if len({s.get("ref", "").split(",")[0].strip().lower()
                for s in c.get("sources", []) if s.get("type") != "index"}) >= 2
    )
    motif_ok = sum(1 for c in creatures if c.get("motifVerified"))
    pron_ok = sum(1 for c in creatures if (c.get("pronunciation") or "").strip())
    xref_ok = sum(1 for c in creatures if len(c.get("crossRefs") or []) >= 2)
    screened = sum(1 for c in creatures if c.get("restrictionScreened"))

    words_total = 0
    entry_words: list[int] = []
    if book:
        for _, entry in iter_entries(book):
            n = sum(word_count(v) for v in (entry.get("sections") or {}).values())
            entry_words.append(n)
            words_total += n
        for group in ("frontMatter", "backMatter"):
            for item in (book.get(group) or {}).values():
                body = item.get("body") if isinstance(item, dict) else item
                words_total += word_count(body or "")
        for group in ("classOpenings", "kinOpenings"):
            for body in (book.get(group) or {}).values():
                words_total += word_count(body or "")

    return {
        "spec": spec,
        "creatures": creatures,
        "by_status": by_status,
        "by_class": by_class,
        "by_kin": by_kin,
        "by_region": by_region,
        "verified": verified,
        "written": written,
        "research_files": research_files,
        "plates": plates,
        "sourced": sourced,
        "motif_ok": motif_ok,
        "pron_ok": pron_ok,
        "xref_ok": xref_ok,
        "screened": screened,
        "words_total": words_total,
        "entry_words": entry_words,
        "commits": git("rev-list", "--count", "HEAD") or "0",
        "tag": git("describe", "--tags", "--abbrev=0") or "—",
        "branch": git("rev-parse", "--abbrev-ref", "HEAD") or "—",
    }


# =============================================================================
# BOOK_STATS.md
# =============================================================================

def render_stats(d: dict) -> str:
    spec = d["spec"]
    classes = {c["id"]: c for c in spec["classes"]}
    kin = {k["id"]: k for k in spec["kinFamilies"]}
    n = len(d["creatures"])

    est_words = d["words_total"] or 0
    est_pages = round(est_words / 260) if est_words else 0

    L = []
    A = L.append
    A("# BOOK STATS — Codex Bestiarium")
    A("")
    A(GENERATED)
    A("")
    A(f"> Son ölçüm: **{today()}** · dal `{d['branch']}` · "
      f"son etiket `{d['tag']}` · {d['commits']} commit")
    A("")
    A("Buradaki her sayı bir dosyadan ölçülmüştür. Hiçbiri elle girilmez ve")
    A("hiçbiri tahmin değildir. Ölçülemeyen alan **—** ile gösterilir.")
    A("")

    A("## 1. Tek bakışta")
    A("")
    A("| Ölçü | Şu an | Hedef | İlerleme |")
    A("|---|---:|---:|---|")
    rows = [
        ("Yaratık kaydı", n, TARGET_CREATURES),
        ("Gelenek", len(spec["traditions"]), TARGET_TRADITIONS),
        ("Araştırma dosyası", d["research_files"], TARGET_CREATURES),
        ("İki bağımsız kaynaklı madde", d["sourced"], TARGET_CREATURES),
        ("Doğrulanmış motif kodu", d["motif_ok"], TARGET_CREATURES),
        ("Telaffuz alanı dolu", d["pron_ok"], TARGET_CREATURES),
        ("Çapraz referansı olan madde", d["xref_ok"], TARGET_CREATURES),
        ("Kısıtlılık taraması yapılmış", d["screened"], TARGET_CREATURES),
        ("Yazılmış madde", d["written"], TARGET_CREATURES),
        ("Normalize plaka", d["plates"], TARGET_CREATURES),
    ]
    for label, cur, target in rows:
        A(f"| {label} | {cur} | {target} | `{bar(cur, target)}` "
          f"%{100 * cur / target:.0f} |")
    A(f"| Kelime (yazılmış) | {est_words:,} | {TARGET_WORDS:,} | "
      f"`{bar(est_words, TARGET_WORDS)}` %{100 * est_words / TARGET_WORDS:.0f} |")
    A(f"| Tahmini sayfa | {est_pages or '—'} | {TARGET_PAGES} | "
      f"`{bar(est_pages, TARGET_PAGES)}` %{100 * est_pages / TARGET_PAGES:.0f} |")
    A("")
    A(f"Sayfa tahmini **260 kelime/sayfa** ile hesaplanır (Codex Mythologica'nın")
    A("ölçülen 6×9 · 11,2/15,6 pt dizgi yoğunluğu). Gerçek değer dizgi")
    A("çalıştırılınca `04_PRINT/` çıktısından okunur — model değil ölçüm geçerlidir.")
    A("")

    A("## 2. Kapsam kapıları")
    A("")
    A("| Kapı | Eşik | Şu an | Durum |")
    A("|---|---:|---:|---|")
    gates = [
        ("Faz 1 tamamlanma — doğrulanmış madde", VERIFY_FLOOR, d["verified"]),
        ("Kapsam tabanı — altına inilirse kitap yeniden planlanır",
         SCOPE_FLOOR, n),
    ]
    for label, thr, cur in gates:
        state = "✅ açık" if cur >= thr else "⛔ kapalı"
        A(f"| {label} | {thr} | {cur} | {state} |")
    A("")

    A("## 3. Durum dağılımı")
    A("")
    A("| Durum | Madde | Pay |")
    A("|---|---:|---:|")
    for s in STATUS_ORDER:
        c = d["by_status"].get(s, 0)
        A(f"| `{s}` | {c} | %{100 * c / n:.0f} |")
    A("")

    A("## 4. Sınıf dağılımı")
    A("")
    A("Yürürlükteki hedef **Faz 2'de ölçülen gerçektir**; yol haritası Bölüm")
    A("03.1'in sayıları 120 maddelik kapsam için hesaplanmıştı ve tarihsel")
    A("kayıt olarak korunur (bkz. `CHANGELOG.md` · karar D21).")
    A("")
    A("| # | Sınıf | Madde | Hedef | Sapma | Sayfa | Yol haritası (120) |")
    A("|---|---|---:|---:|---:|---:|---:|")
    for cid in ["I", "II", "III", "IV", "V", "VI"]:
        cur = d["by_class"].get(cid, 0)
        meta = classes.get(cid, {})
        tgt = meta.get("targetEntries", 0)
        delta = cur - tgt
        mark = "—" if delta == 0 else f"{delta:+d}"
        rm_e = meta.get("roadmapTargetEntries", "—")
        rm_p = meta.get("roadmapTargetPages", "—")
        A(f"| {cid} | {meta.get('en', '?')} · {meta.get('tr', '')} | {cur} | "
          f"{tgt} | {mark} | {meta.get('targetPages', '—')} | {rm_e} / {rm_p} s |")
    A("")

    budget = spec.get("meta", {}).get("pageBudget")
    if budget:
        A("### Sayfa bütçesi")
        A("")
        A(f"Madde başına **{budget['pagesPerEntry']} sayfa** "
          "(yol haritası Bölüm 05.3'ün 304/120 ≈ 2,53 modelinden, kilitlenen")
        A("112 maddelik kapsama göre yeniden dağıtıldı).")
        A("")
        A("| Kalem | Sayfa |")
        A("|---|---:|")
        A(f"| Maddeler ({n} × {budget['pagesPerEntry']}) | {budget['entryPages']} |")
        A(f"| Sınıf ve karşılaştırma açılışları | {budget['openingPages']} |")
        A(f"| Ön/arka madde · dizinler · kaynaklar | {budget['matterPages']} |")
        A(f"| **Toplam** | **{budget['total']}** |")
        A("")

    A("## 5. Akraba imge aileleri")
    A("")
    A("**Manşet** üyeler iki sayfalık karşılaştırma açılışına girer; **uzun")
    A("kuyruk** üyeleri akraba imge tablosunda ve kendi maddesinde durur.")
    A("İkisi de tam üyedir (bkz. `00_CONTEXT/KIN_OPENINGS.md`).")
    A("")
    A("| Aile | İmge | Motif | Üye | Manşet | Uzun kuyruk |")
    A("|---|---|---|---:|---:|---:|")
    for kid in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        meta = kin.get(kid, {})
        cnt = d["by_kin"].get(kid, 0)
        head = len(meta.get("headline") or [])
        tail = len(meta.get("extended") or [])
        A(f"| **{kid}** · {meta.get('tr', '')} | {meta.get('en', '')} | "
          f"`{meta.get('motif', '')}` | {cnt} | {head} | {tail} |")
    bound = sum(d["by_kin"].values())
    A("")
    A(f"Aileye bağlı madde: **{bound}/{n}** · bağımsız madde: {n - bound}")
    A("")

    A("## 5b. Çapraz referans grafiği")
    A("")
    xrefs = [len(c.get("crossRefs") or []) for c in d["creatures"]]
    edges = sum(xrefs) // 2
    A("| Ölçü | Değer |")
    A("|---|---:|")
    A(f"| Bağ (karşılıklı) | {edges} |")
    A(f"| Madde başına ortalama | {sum(xrefs) / n:.2f} |")
    A(f"| En az / en çok | {min(xrefs)} / {max(xrefs)} |")
    lo_x, hi_x = spec.get("meta", {}).get("targets", {}).get("crossRefMin", 2), \
        spec.get("meta", {}).get("targets", {}).get("crossRefMax", 5)
    A(f"| Bantta ({lo_x}–{hi_x}) | "
      f"{sum(1 for x in xrefs if lo_x <= x <= hi_x)}/{n} |")
    A("")

    A("## 6. Bölge dağılımı")
    A("")
    A("| Bölge grubu | Gelenek |")
    A("|---|---:|")
    for region, cnt in sorted(d["by_region"].items(), key=lambda kv: -kv[1]):
        A(f"| {region} | {cnt} |")
    A("")

    if d["entry_words"]:
        lo, hi = WORD_BAND
        ew = d["entry_words"]
        in_band = sum(1 for w in ew if lo <= w <= hi)
        A("## 7. Madde uzunluğu")
        A("")
        A(f"| Ölçü | Değer |")
        A("|---|---:|")
        A(f"| Yazılmış madde | {len(ew)} |")
        A(f"| Ortalama | {sum(ew) / len(ew):.0f} kelime |")
        A(f"| En kısa | {min(ew)} |")
        A(f"| En uzun | {max(ew)} |")
        A(f"| Bantta ({lo}–{hi}) | {in_band}/{len(ew)} |")
        A("")

    A("---")
    A("")
    A("*Bu dosya `08_BUILD/update_docs.py` tarafından üretilir. CI her push'ta")
    A("`--check` ile bayatlığını denetler; bayatsa derleme kırmızı yanar.*")
    return "\n".join(L) + "\n"


# =============================================================================
# ROADMAP_PROGRESS.md
# =============================================================================

def phase_progress(d: dict, phase: dict) -> tuple[int, int, str]:
    """(tamamlanan, toplam, ölçüt) — faz başına ilerleme."""
    creatures = d["creatures"]
    n = phase["n"]
    if n == 1:
        return d["sourced"], TARGET_CREATURES, "iki bağımsız kaynaklı madde"
    if n == 2:
        # Faz 2'nin ölçütü telaffuz DEĞİLDİR — telaffuz Faz 1'de toplandı.
        # Fazı bitiren şey tasniftir: madde bir sınıfa, bir aileye ve
        # karşılıklı bir çapraz referans grafiğine oturmuş olmalı.
        done = sum(
            1 for c in creatures
            if (c.get("pronunciation") or "").strip()
            and len(c.get("crossRefs") or []) >= 2
        )
        return done, TARGET_CREATURES, "telaffuz + karşılıklı çapraz referans"
    if n in PHASE_CLASSES:
        wanted = [c for c in creatures if c["class"] in PHASE_CLASSES[n]]
        done = sum(1 for c in wanted if c["status"] in ("written", "edited", "final"))
        classes = " + ".join(PHASE_CLASSES[n])
        return done, len(wanted), f"sınıf {classes} maddeleri yazıldı"
    # Faz 6 — üretim
    formats = 0
    checks = [
        ("04_PRINT", ".pdf"), ("05_KINDLE", ".epub"),
        ("02_MANUSCRIPT", ".docx"), ("03_COVER", ".pdf"),
    ]
    for folder, ext in checks:
        p = os.path.join(ROOT, folder)
        if os.path.isdir(p):
            for _, _, fs in os.walk(p):
                if any(f.lower().endswith(ext) for f in fs):
                    formats += 1
                    break
    return formats, len(checks), "üretilmiş yayın dosyası ailesi"


def render_progress(d: dict) -> str:
    L = []
    A = L.append
    A("# ROADMAP PROGRESS — Codex Bestiarium")
    A("")
    A(GENERATED)
    A("")
    A(f"> Son ölçüm: **{today()}** · dal `{d['branch']}` · son etiket `{d['tag']}`")
    A("")
    A("Kaynak: [`CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md`]"
      "(CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md)")
    A("")

    A("## Faz durumu")
    A("")
    A("| Faz | Başlık | İlerleme | Ölçüt | Etiket | Kilometre taşı |")
    A("|---:|---|---|---|---|---|")
    for p in PHASES:
        done, total, metric = phase_progress(d, p)
        pct = 100 * done / total if total else 0
        A(f"| **{p['n']}** | {p['title']} | `{bar(done, total, 16)}` "
          f"{done}/{total} (%{pct:.0f}) | {metric} | `{p['tag']}` | "
          f"{p['milestone']} |")
    A("")

    A("## Kalite kapıları — şu anki durum")
    A("")
    A("| Kapı | Komut | Ne zaman açılır |")
    A("|---|---|---|")
    A("| Şema | `validate_spec.py --gate draft` | her zaman |")
    A("| Araştırma | `validate_spec.py --gate phase1` | Faz 1 sonunda |")
    A("| Tasnif | `validate_spec.py --gate phase2` | Faz 2 sonunda |")
    A("| Çapraz referans | `classify.py --check` | her push |")
    A("| Yazım | `validate_spec.py --gate phase3` | Faz 3'ten itibaren |")
    A("| Kelime bandı | `qa_length.py --sections` | metin geldiğinde |")
    A("| Ses | `qa_voice.py` | metin geldiğinde |")
    A("| Sürüklenme | `qa_drift.py` | haftalık, Faz 3'ten itibaren |")
    A("| Tekrar | `qa_echo.py` | metin geldiğinde |")
    A("| Diakritik | `qa_diacritics.py` | her zaman |")
    A("| Plaka | `plates.py --measure` | plaka geldiğinde |")
    A("| Yapı | `validate_structure.py` | her push |")
    A("")

    A("## Sonraki eylem")
    A("")
    if d["sourced"] < VERIFY_FLOOR:
        A(f"**Faz 1 · Araştırma.** {d['sourced']}/{TARGET_CREATURES} maddede iki")
        A(f"bağımsız kaynak var. Kapı {VERIFY_FLOOR}'de açılıyor.")
        A("")
        A("Sıra yol haritasının emrettiği gibi **en zor sekiz gelenekten**")
        A("başlar — kapsamı bunlar belirler:")
        A("")
        spec = d["spec"]
        hard = [t for t in spec["traditions"] if t.get("sourceRisk") == "high"]
        by_trad = collections.defaultdict(list)
        for c in d["creatures"]:
            by_trad[c["tradition"]].append(c)
        for t in hard:
            items = by_trad.get(t["id"], [])
            done = sum(1 for c in items if c["status"] != "draft")
            names = ", ".join(c["name"] for c in items)
            A(f"- **{t['name']}** {t['sigil']} — {done}/{len(items)} · {names}")
    elif d["written"] < TARGET_CREATURES:
        A(f"**Yazım.** {d['written']}/{TARGET_CREATURES} madde yazıldı.")
        A("Tek seferde en fazla üç madde — daha fazlası üslup sürüklenmesi üretir.")
    else:
        A("**Üretim.** Bütün maddeler yazıldı; dizgi ve KDP fazına geçilebilir.")
    A("")

    A("---")
    A("")
    A("*Bu dosya `08_BUILD/update_docs.py` tarafından üretilir.*")
    return "\n".join(L) + "\n"


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="yazma; bayatsa çıkış 1")
    args = ap.parse_args()

    d = gather()
    outputs = [(STATS_PATH, render_stats(d)), (PROGRESS_PATH, render_progress(d))]

    if args.check:
        stale = []
        for path, content in outputs:
            if not os.path.exists(path):
                stale.append(f"{os.path.relpath(path, ROOT)} (yok)")
                continue
            with open(path, encoding="utf-8") as fh:
                current = fh.read()
            # Tarih satırı her gün değişir; onu karşılaştırmadan çıkar.
            def strip_date(t: str) -> str:
                return "\n".join(
                    l for l in t.splitlines() if not l.startswith("> Son ölçüm:")
                )
            if strip_date(current) != strip_date(content):
                stale.append(os.path.relpath(path, ROOT))
        if stale:
            print("BAYAT BELGE:", ", ".join(stale))
            print("Düzeltmek için: python3 08_BUILD/update_docs.py")
            return 1
        print("TAMAM: üretilen belgeler güncel.")
        return 0

    for path, content in outputs:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"yazıldı: {os.path.relpath(path, ROOT)}")
    _ = json
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
