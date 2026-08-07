#!/usr/bin/env python3
"""
CODEX BESTIARIUM — TASNİF VE ÇAPRAZ REFERANS SENKRONİZASYONU
================================================================================
Faz 2'nin motoru. `research_gen.py` araştırmayı spec.json'a işler; bu betik
TASNİFİ işler:

    01_SOURCE/kin_map.json  →  01_SOURCE/spec.json
                                  · creatures[].crossRefs
                                  · kinFamilies[] (motif · ayrışma · headline · açılış planı)
                                  · classes[]     (targetEntries · targetPages)
                                  · meta.targets  (kilitlenen kapsam)
                               06_REPORTS/crossref-graph.json

NEDEN BU MİMARİ?
    112 maddeye 2–5 KARŞILIKLI çapraz referans, elle tutulduğunda kaçınılmaz
    olarak tek yönlü bağ ve kırık referans üretir. `seed_import.py` ve
    `research_gen.py` için verilen karar burada da geçerlidir: TÜRET, YAZMA.

    Editoryal karar (hangi iki madde birbirine bağlanır ve NEDEN) elle yazılır
    — `kin_map.json` içindeki her bağın bir `note` alanı vardır ve o not
    maddenin 6. bölümüne ("Akrabaları") girecek olan AYRIŞMA cümlesidir.
    Grafiğin kapanışı, simetrisi ve bant denetimi üretilir.

SAYFA BÜTÇESİ — MODEL DEĞİL ÖLÇÜM
    Yol haritası Bölüm 05.3'ün modeli 120 madde için 304 madde sayfası
    veriyordu: madde başına ≈2,53 sayfa. Faz 2'nin PROVA DİZGİSİ o modeli
    doğruladı ve bir şey daha gösterdi (`08_BUILD/entry_page.py`):

        ölçülen içerik yüksekliği        2,558 sayfa/madde  (model 2,53 ✓)
        madde başına GERÇEK maliyet      3 sayfa

    Aradaki 0,44 sayfa, plaka kuralının bedelidir: plaka maddenin ÜST
    YARISINA oturur (STYLE_PLATES § 7.2), dolayısıyla her madde bir sayfanın
    başından başlamak zorundadır ve son sayfası yarım kalır. Sürekli akış
    286 sayfa verirdi ama plakayı sayfa ortasına düşürürdü.

        madde sayfası      112 × 3              = 336
        sınıf açılışları   6 × 2                =  12
        karşılaştırma      8 × 2                =  16
        ön/arka madde + dizin + kaynaklar       =  72
                                                 ────
                                                  436   = TARGET_PAGES

    Telif her üç sürümde de pozitif kalıyor ve sayfa sayıları KDP bandının
    içinde (`editions.verify_royalties`); ciltsizde fark 9,36 $ → 8,76 $.

KULLANIM
    python3 08_BUILD/classify.py            # uygula
    python3 08_BUILD/classify.py --check    # bayat mı? değilse çıkış 1
    python3 08_BUILD/classify.py --report -v
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    CLASS_IDS,
    CONTEXT_DIR,
    CROSSREF_BAND,
    KIN_IDS,
    REPORT_DIR,
    ROOT,
    SOURCE_DIR,
    SPEC_PATH,
    TARGET_CREATURES,
    TARGET_PAGES,
    TARGET_TRADITIONS,
    TARGET_WORDS,
    WORD_BAND,
    WORD_TARGET,
    Result,
    load_spec,
)

KIN_MAP_PATH = os.path.join(SOURCE_DIR, "kin_map.json")
GRAPH_REPORT = os.path.join(REPORT_DIR, "crossref-graph.json")
OPENINGS_DOC = os.path.join(CONTEXT_DIR, "KIN_OPENINGS.md")

# --- sayfa bütçesi (Faz 2 prova dizgisinden ÖLÇÜLDÜ) ----------------------
# `08_BUILD/entry_page.py --proof` ile ölçüldü; oradaki sabitle aynı olmak
# ZORUNDADIR ve `entry_page.py` ayrışmayı kırmızı yakar.
PAGES_PER_ENTRY = 3.0
CLASS_OPENING_PAGES = 2      # sınıf başına
KIN_OPENING_PAGES = 2        # aile başına

LINK_TYPES = {"kin", "function", "pair", "tradition"}


# =============================================================================
# YÜKLEME
# =============================================================================

def load_map(path: str = KIN_MAP_PATH) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def edges(km: dict) -> list[tuple[str, str, str, str]]:
    """(a, b, tip, not) — kaynak dosyadaki sırayla."""
    return [(l["a"], l["b"], l.get("type", ""), l.get("note", "")) for l in km["links"]]


def adjacency(km: dict) -> dict[str, dict[str, dict]]:
    """id → {komşu: {type, note}} — bağ İKİ YÖNLÜ kurulur.

    Karşılıklılık burada ÜRETİLİR, elle yazılmaz: `validate_spec` tek yönlü
    bağı uyarı olarak basıyordu ve o uyarı elle kapatılamayacak kadar çoktur.
    """
    adj: dict[str, dict[str, dict]] = collections.defaultdict(dict)
    for a, b, typ, note in edges(km):
        adj[a][b] = {"type": typ, "note": note}
        adj[b][a] = {"type": typ, "note": note}
    return adj


# =============================================================================
# SAYFA BÜTÇESİ
# =============================================================================

def page_budget(counts: dict[str, int]) -> dict:
    """Sınıf başına sayfa bütçesi. Toplam TARGET_PAGES'i birebir tutar."""
    per_class = {
        cid: round(counts.get(cid, 0) * PAGES_PER_ENTRY) for cid in CLASS_IDS
    }
    entry_pages = sum(per_class.values())
    openings = len(CLASS_IDS) * CLASS_OPENING_PAGES + len(KIN_IDS) * KIN_OPENING_PAGES
    matter = TARGET_PAGES - entry_pages - openings
    return {
        "perClass": per_class,
        "entryPages": entry_pages,
        "openingPages": openings,
        "matterPages": matter,
        "total": entry_pages + openings + matter,
        "pagesPerEntry": PAGES_PER_ENTRY,
    }


# =============================================================================
# UYGULAMA
# =============================================================================

def apply(spec: dict, km: dict) -> dict:
    creatures = spec["creatures"]
    adj = adjacency(km)
    counts = collections.Counter(c["class"] for c in creatures)
    budget = page_budget(counts)

    # --- çapraz referanslar ---
    for c in creatures:
        refs = sorted(adj.get(c["id"], {}))
        c["crossRefs"] = refs

    # --- akraba aileleri ---
    members = collections.defaultdict(list)
    for c in creatures:
        if c.get("kinFamily"):
            members[c["kinFamily"]].append(c["id"])
    for fam in spec["kinFamilies"]:
        src = km["families"].get(fam["id"])
        if not src:
            continue
        fam["motif"] = src["motif"]
        fam["motifNote"] = src["motifNote"]
        fam["motifSpread"] = src.get("motifSpread", [])
        fam["divergence"] = src["divergence"]
        fam["headline"] = src["headline"]
        fam["extended"] = sorted(set(members[fam["id"]]) - set(src["headline"]))
        fam["memberCount"] = len(members[fam["id"]])
        fam["opening"] = src["opening"]
        fam["openingPages"] = KIN_OPENING_PAGES

    # --- sınıflar ---
    for klass in spec["classes"]:
        cid = klass["id"]
        # Yol haritası Bölüm 03.1'in 120 maddelik hedefi TARİHSEL KAYIT olarak
        # korunur; yürürlükteki hedef Faz 2'de ölçülen gerçektir.
        klass.setdefault("roadmapTargetEntries", klass.get("targetEntries"))
        klass.setdefault("roadmapTargetPages", klass.get("targetPages"))
        klass["targetEntries"] = counts.get(cid, 0)
        klass["targetPages"] = budget["perClass"][cid]
        klass["openingPages"] = CLASS_OPENING_PAGES
        klass["topics"] = km["classOpenings"][cid]["topics"]

    # --- meta ---
    spec["meta"]["targets"] = {
        "creatures": TARGET_CREATURES,
        "traditions": TARGET_TRADITIONS,
        "pages": TARGET_PAGES,
        "words": TARGET_WORDS,
        "wordsPerEntry": WORD_TARGET,
        "wordBandMin": WORD_BAND[0],
        "wordBandMax": WORD_BAND[1],
        "minSources": 2,
        "scopeFloor": 100,
        "crossRefMin": CROSSREF_BAND[0],
        "crossRefMax": CROSSREF_BAND[1],
    }
    spec["meta"]["scopeLockedAt"] = "phase1"
    spec["meta"]["classificationLockedAt"] = "phase2"
    spec["meta"]["pageBudget"] = budget
    spec["meta"]["generatedBy"] = "08_BUILD/seed_import.py + research_gen.py + classify.py"
    return spec


# =============================================================================
# DOĞRULAMA
# =============================================================================

def verify(spec: dict, km: dict, r: Result) -> None:
    creatures = spec["creatures"]
    ids = {c["id"] for c in creatures}
    lo, hi = CROSSREF_BAND

    # --- kaynak dosyanın kendi tutarlılığı ---
    bad_id = sorted(
        {x for a, b, _, _ in edges(km) for x in (a, b) if x not in ids}
    )
    r.add(not bad_id, "kin_map.json'daki bütün kimlikler spec'te var", f"{bad_id[:10]}")

    self_link = sorted({a for a, b, _, _ in edges(km) if a == b})
    r.add(not self_link, "hiçbir bağ kendine değil", f"{self_link[:10]}")

    seen: set[tuple[str, str]] = set()
    dupes = []
    for a, b, _, _ in edges(km):
        key = tuple(sorted((a, b)))
        if key in seen:
            dupes.append(f"{a}–{b}")
        seen.add(key)
    r.add(not dupes, "tekrarlanan bağ yok", f"{dupes[:10]}")

    bad_type = sorted({t for _, _, t, _ in edges(km) if t not in LINK_TYPES})
    r.add(not bad_type, f"bağ tipleri geçerli ({'|'.join(sorted(LINK_TYPES))})",
          f"{bad_type}")

    no_note = [f"{a}–{b}" for a, b, _, n in edges(km) if not n.strip()]
    r.add(not no_note, "her bağın ayrışma notu var",
          f"{no_note[:10]} — not yoksa bağ süslemedir")

    # --- grafiğin bantları ---
    out_of_band = [
        f"{c['id']} ({len(c['crossRefs'])})"
        for c in creatures
        if not lo <= len(c["crossRefs"]) <= hi
    ]
    r.add(not out_of_band, f"her maddede {lo}–{hi} çapraz referans",
          "; ".join(out_of_band[:12]))

    edge_set = {(c["id"], ref) for c in creatures for ref in c["crossRefs"]}
    one_way = [f"{a}→{b}" for a, b in edge_set if (b, a) not in edge_set]
    r.add(not one_way, "grafik simetrik", f"{one_way[:10]}")

    # --- aile bütünlüğü ---
    members = collections.defaultdict(set)
    for c in creatures:
        if c.get("kinFamily"):
            members[c["kinFamily"]].add(c["id"])
    unlinked = [
        f"{m} ({fam})"
        for fam, ms in members.items()
        for m in ms
        if not (set(next(c for c in creatures if c["id"] == m)["crossRefs"]) & (ms - {m}))
    ]
    r.add(not unlinked, "her aile üyesi en az bir aile kardeşine bağlı",
          f"{unlinked[:10]}")

    cap = km.get("_headlineCap", 9)
    bad_head = []
    for fam in spec["kinFamilies"]:
        head = set(fam.get("headline", []))
        ms = members[fam["id"]]
        if not head <= ms:
            bad_head.append(f"{fam['id']}: {sorted(head - ms)} üye değil")
        if len(head) > cap:
            bad_head.append(f"{fam['id']}: {len(head)} manşet üye > {cap}")
        if not head:
            bad_head.append(f"{fam['id']}: manşet üye yok")
    r.add(not bad_head,
          f"manşet üyeler ailenin içinden ve en çok {cap} kişi",
          "; ".join(bad_head[:8])
          + " — iki sayfalık açılışa daha fazlası sığmaz")

    # --- ayrışma cümlesi süsleme mi ---
    # Ölçüt sert: cümle GERÇEK bir fark söylemeli. En kaba mekanik sınav,
    # cümlenin en az iki geleneği karşı karşıya koymasıdır (';' veya '—').
    weak = [
        fam["id"] for fam in spec["kinFamilies"]
        if fam["divergence"].count(";") + fam["divergence"].count("—") < 1
    ]
    r.add(not weak, "her ailenin ayrışma cümlesi en az iki durumu karşılaştırıyor",
          f"{weak} — 'her kültürde farklı yorumlanır' geçmez")

    # --- sayfa bütçesi ---
    budget = spec["meta"]["pageBudget"]
    r.add(
        budget["total"] == TARGET_PAGES,
        f"sayfa bütçesi toplamı {TARGET_PAGES}",
        f"madde {budget['entryPages']} + açılış {budget['openingPages']} + "
        f"matter {budget['matterPages']} = {budget['total']}",
    )
    r.add(
        budget["matterPages"] > 0,
        "ön/arka madde payı pozitif",
        f"{budget['matterPages']} sayfa",
    )

    counts = collections.Counter(c["class"] for c in creatures)
    drift = [
        f"{k}: {klass['targetEntries']} ≠ {counts.get(k, 0)}"
        for klass in spec["classes"]
        for k in [klass["id"]]
        if klass["targetEntries"] != counts.get(k, 0)
    ]
    r.add(not drift, "sınıf hedefi ölçülen dağılımla birebir", f"{drift}")


# =============================================================================
# RAPOR
# =============================================================================

def graph_report(spec: dict, km: dict) -> dict:
    creatures = spec["creatures"]
    by_id = {c["id"]: c for c in creatures}
    adj = adjacency(km)
    types = collections.Counter(t for _, _, t, _ in edges(km))
    degrees = collections.Counter(len(c["crossRefs"]) for c in creatures)
    return {
        "edges": len(km["links"]),
        "nodes": len(creatures),
        "byType": dict(sorted(types.items())),
        "degreeDistribution": {str(k): v for k, v in sorted(degrees.items())},
        "meanDegree": round(sum(len(c["crossRefs"]) for c in creatures) / len(creatures), 2),
        "links": [
            {
                "a": a, "b": b, "type": t, "note": n,
                "classA": by_id[a]["class"], "classB": by_id[b]["class"],
                "familyA": by_id[a].get("kinFamily"),
                "familyB": by_id[b].get("kinFamily"),
            }
            for a, b, t, n in edges(km)
        ],
        "adjacency": {k: sorted(v) for k, v in sorted(adj.items())},
    }


def render_openings(spec: dict, km: dict) -> str:
    """`00_CONTEXT/KIN_OPENINGS.md` — sekiz açılışın içerik planı.

    Metin Faz 5'te yazılır; bu belge NE yazılacağını kilitler. Üretilmiştir,
    çünkü plaka kimlikleri ve üye listeleri spec'ten okunur — elle yazılırsa
    ilk kapsam değişikliğinde ayrışır.
    """
    by_id = {c["id"]: c for c in spec["creatures"]}
    trads = {t["id"]: t for t in spec["traditions"]}
    classes = {c["id"]: c for c in spec["classes"]}
    budget = spec["meta"]["pageBudget"]

    L: list[str] = []
    A = L.append
    A("# KIN_OPENINGS — karşılaştırma ve sınıf açılışlarının içerik planı")
    A("")
    A("<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/classify.py · ELLE DÜZENLEMEYİN")
    A("     Kaynak: 01_SOURCE/kin_map.json -->")
    A("")
    A("> **Bu belge metin değildir; metnin ŞARTNAMESİDİR.**")
    A("> Sekiz karşılaştırma açılışı kitabın satın alma sebebidir ve metinleri")
    A("> Faz 3–5'te yazılır. Burada ne söyleyecekleri, hangi üyeleri yan yana")
    A("> koyacakları ve hangi plakaları taşıyacakları **Faz 2'de kilitlenir**.")
    A("")
    A(f"Toplam açılış bütçesi: {len(KIN_IDS)} × {KIN_OPENING_PAGES} = "
      f"{len(KIN_IDS) * KIN_OPENING_PAGES} sayfa (karşılaştırma) + "
      f"{len(CLASS_IDS)} × {CLASS_OPENING_PAGES} = "
      f"{len(CLASS_IDS) * CLASS_OPENING_PAGES} sayfa (sınıf) = "
      f"{budget['openingPages']} sayfa.")
    A("")
    A("---")
    A("")

    A("## 0. Manşet üye kuralı")
    A("")
    A(f"İki sayfalık bir açılışa en çok **{km.get('_headlineCap', 9)} üye** sığar.")
    A("Ailelerin üyeliği bundan geniş olabilir ve üçünde öyledir. Bu yüzden")
    A("üyelik iki katmanlıdır:")
    A("")
    A("| Katman | Nerede görünür |")
    A("|---|---|")
    A("| **manşet** | Karşılaştırma açılışının tablosunda ve plaka dizisinde |")
    A("| **uzun kuyruk** | Akraba imge tablosunda (dizin), kendi maddesinde ve "
      "Kin-Images Chart'ta |")
    A("")
    A("İkisi de tam üyedir; fark yalnızca **iki sayfaya ne sığdığıdır**.")
    A("")
    A("| Aile | Üye | Manşet | Uzun kuyruk | Motif çıpası |")
    A("|---|---:|---:|---:|---|")
    for fam in spec["kinFamilies"]:
        A(f"| **{fam['id']}** · {fam['tr']} | {fam['memberCount']} | "
          f"{len(fam['headline'])} | {len(fam['extended'])} | `{fam['motif']}` |")
    A("")
    A("---")
    A("")

    A("## 1. Karşılaştırma açılışları")
    A("")
    for fam in spec["kinFamilies"]:
        op = fam["opening"]
        A(f"### {fam['id']} · {fam['tr']} — *{op['title']}*")
        A("")
        A(f"**Ortak imge.** {fam['image']}")
        A("")
        A(f"**Motif çıpası.** `{fam['motif']}` — {fam['motifNote']}")
        if fam.get("motifSpread"):
            A("")
            A("**Üyelerin dağıldığı diğer kodlar.** "
              + " · ".join(f"`{m}`" for m in fam["motifSpread"]))
        A("")
        A(f"**Tez.** {op['thesis']}")
        A("")
        A(f"**Harita.** {op['map']}")
        A("")
        A("**Manşet üyeler ve plakaları.**")
        A("")
        A("| # | Üye | Gelenek | Sınıf | Plaka |")
        A("|---:|---|---|---|---|")
        for i, mid in enumerate(fam["headline"], 1):
            rec = by_id[mid]
            t = trads.get(rec["tradition"], {})
            A(f"| {i} | **{rec['name']}** | {t.get('name', '?')} "
              f"{t.get('sigil', '')} | {rec['class']} | `{rec['plate']}` |")
        A("")
        A("**Karşılaştırma tablosunun sütunları.**")
        A("")
        for col in op["table"]:
            A(f"- {col}")
        A("")
        A(f"**Ayrışma cümlesi.** {fam['divergence']}")
        A("")
        A(f"**Kapanış.** {op['closing']}")
        if op.get("longTail"):
            A("")
            A(f"**Uzun kuyruk.** {op['longTail']}")
        if op.get("note"):
            A("")
            A(f"> {op['note']}")
        A("")

    A("---")
    A("")
    A("## 2. Sınıf açılışları")
    A("")
    A("Her sınıf açılışı **2 sayfadır** ve metni Faz 3–5'te, o sınıfın")
    A("maddeleriyle birlikte yazılır. Konu başlıkları burada kilitlidir.")
    A("")
    for klass in spec["classes"]:
        A(f"### {klass['id']} · {klass['en']} — {klass['tr']}")
        A("")
        A(f"> {klass['definition']}")
        A("")
        A(f"**Bütçe.** {klass['targetEntries']} madde · "
          f"{klass['targetPages']} sayfa + {klass['openingPages']} sayfa açılış")
        A("")
        for topic in klass["topics"]:
            A(f"- {topic}")
        A("")

    A("---")
    A("")
    A("*Bu dosya `08_BUILD/classify.py` tarafından `01_SOURCE/kin_map.json`'dan")
    A("üretilir. CI her push'ta `--check` ile bayatlığını denetler.*")
    return "\n".join(L) + "\n"


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="yazma; bayatsa çıkış 1")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(KIN_MAP_PATH):
        print(f"HATA: {os.path.relpath(KIN_MAP_PATH, ROOT)} yok.", file=sys.stderr)
        return 2

    km = load_map()
    spec = apply(load_spec(), km)

    r = Result("TASNİF VE ÇAPRAZ REFERANS (classify)")
    verify(spec, km, r)

    want_spec = json.dumps(spec, ensure_ascii=False, indent=2) + "\n"
    want_graph = json.dumps(graph_report(spec, km), ensure_ascii=False, indent=2) + "\n"
    want_doc = render_openings(spec, km)

    if args.check:
        # `06_REPORTS/*.json` .gitignore'dadır ve olmalıdır: rapor bir ÇIKTIDIR,
        # kaynak değil. Bayatlık denetimi yalnızca DEPODAKİ türetilmiş
        # dosyalara uygulanır — CI'da olmayan bir raporu "bayat" saymak,
        # gerçek bir kalite düşüşü olmadan derlemeyi kırmızıya çevirir.
        stale = []
        for path, want in ((SPEC_PATH, want_spec), (OPENINGS_DOC, want_doc)):
            if not os.path.exists(path):
                stale.append(f"{os.path.relpath(path, ROOT)} (yok)")
                continue
            with open(path, encoding="utf-8") as fh:
                if fh.read() != want:
                    stale.append(os.path.relpath(path, ROOT))
        code = r.report(verbose=args.verbose)
        if stale:
            print("BAYAT: " + ", ".join(stale))
            print("Düzeltmek için: python3 08_BUILD/classify.py")
            return 1
        if code == 0:
            print("TAMAM: tasnif ve çapraz referanslar güncel.")
            if not os.path.exists(GRAPH_REPORT):
                print(f"not: {os.path.relpath(GRAPH_REPORT, ROOT)} yok "
                      "(.gitignore § rapor) — üretmek için: classify.py")
        return code

    with open(SPEC_PATH, "w", encoding="utf-8") as fh:
        fh.write(want_spec)
    os.makedirs(REPORT_DIR, exist_ok=True)
    with open(GRAPH_REPORT, "w", encoding="utf-8") as fh:
        fh.write(want_graph)
    with open(OPENINGS_DOC, "w", encoding="utf-8") as fh:
        fh.write(want_doc)
    print(f"yazıldı: {os.path.relpath(SPEC_PATH, ROOT)}")
    print(f"yazıldı: {os.path.relpath(GRAPH_REPORT, ROOT)}")
    print(f"yazıldı: {os.path.relpath(OPENINGS_DOC, ROOT)}")

    if args.report or args.verbose:
        b = spec["meta"]["pageBudget"]
        print(f"\nsayfa bütçesi: madde {b['entryPages']} · açılış "
              f"{b['openingPages']} · matter {b['matterPages']} = {b['total']}")
        for klass in spec["classes"]:
            print(f"  {klass['id']:<4} {klass['targetEntries']:>3} madde · "
                  f"{klass['targetPages']:>3} sayfa "
                  f"(yol haritası: {klass['roadmapTargetEntries']} / "
                  f"{klass['roadmapTargetPages']})")
        for fam in spec["kinFamilies"]:
            print(f"  {fam['id']} · {fam['memberCount']:>2} üye · "
                  f"{len(fam['headline'])} manşet · "
                  f"{len(fam['extended'])} uzun kuyruk · {fam['motif']}")

    return r.report(verbose=args.verbose)


if __name__ == "__main__":
    raise SystemExit(main())
