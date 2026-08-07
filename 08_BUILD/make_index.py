#!/usr/bin/env python3
"""
CODEX BESTIARIUM — DÖRT DİZİN ÜRETİCİSİ
================================================================================
Yol haritası Bölüm 05.3 · Bölüm 10: dizinler kitabın rafta kalma süresini
belirleyen şeydir ve **elle yazılamazlar**.

    gelenek dizini        8 sayfa
    motif dizini          4 sayfa
    akraba imge tablosu   4 sayfa
    telaffuz rehberi      6 sayfa
                         ── 22 sayfa

Dördü de `spec.json`'dan üretilir. Sayfa numaraları **dizgiden okunur**
(`04_PRINT/<SÜRÜM>/pagemap.json`); elle girilmez. Sayfa haritası yoksa dizin
yine üretilir ama numara yerine `—` konur ve bu bir kapı ihlali olarak
raporlanır (Faz 6 kapısı: "dizin sayfa numaraları gerçek dizgiyle eşleşiyor mu").

Çıktı: `01_SOURCE/indexes.json` (dizgi motorunun okuduğu) +
       `06_REPORTS/INDEXES_PREVIEW.md` (insan gözüyle kontrol için)

KULLANIM
    python3 08_BUILD/make_index.py
    python3 08_BUILD/make_index.py --pagemap 04_PRINT/PAPERBACK/pagemap.json
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ROOT, SOURCE_DIR, Result, load_spec  # noqa: E402

OUT_JSON = os.path.join(SOURCE_DIR, "indexes.json")
OUT_MD = os.path.join(ROOT, "06_REPORTS", "INDEXES_PREVIEW.md")


def sortkey(s: str) -> tuple:
    """Diakritikten bağımsız alfabetik sıralama; diakritik ikincil anahtardır."""
    flat = "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    ).lower()
    return (flat, s.lower())


def load_pagemap(path: str | None) -> dict:
    if not path:
        return {}
    full = path if os.path.isabs(path) else os.path.join(ROOT, path)
    if not os.path.exists(full):
        return {}
    with open(full, encoding="utf-8") as fh:
        return json.load(fh)


def page_of(pagemap: dict, key: str) -> str:
    p = pagemap.get(key)
    return str(p) if p else "—"


# =============================================================================
# DİZİNLER
# =============================================================================

def index_traditions(spec: dict, pm: dict) -> list[dict]:
    """40 gelenek dizini — gelenek → maddeleri, sayfa numarasıyla."""
    by_trad = collections.defaultdict(list)
    for c in spec["creatures"]:
        by_trad[c["tradition"]].append(c)
    out = []
    for t in sorted(spec["traditions"], key=lambda t: sortkey(t["name"])):
        entries = sorted(by_trad.get(t["id"], []), key=lambda c: sortkey(c["name"]))
        out.append({
            "tradition": t["name"],
            "sigil": t["sigil"],
            "regionGroup": t["regionGroup"],
            "inherited": t.get("inherited", False),
            "entries": [
                {"name": c["name"], "id": c["id"], "class": c["class"],
                 "page": page_of(pm, c["id"])}
                for c in entries
            ],
        })
    return out


def index_motifs(spec: dict, pm: dict) -> list[dict]:
    """Motif dizini — Thompson kodu → maddeler. Kodlar hiyerarşik sıralanır."""
    by_motif = collections.defaultdict(list)
    for c in spec["creatures"]:
        for m in c["motif"]:
            by_motif[m].append(c)

    def mkey(code: str) -> tuple:
        letter = code[0]
        nums = tuple(int(n) for n in code[1:].split(".") if n.isdigit())
        return (letter, nums)

    return [
        {
            "motif": m,
            "section": m[0],
            "entries": [
                {"name": c["name"], "id": c["id"], "tradition": c["tradition"],
                 "page": page_of(pm, c["id"])}
                for c in sorted(by_motif[m], key=lambda c: sortkey(c["name"]))
            ],
        }
        for m in sorted(by_motif, key=mkey)
    ]


def index_kin(spec: dict, pm: dict) -> list[dict]:
    """Akraba imge tablosu — kitabın tezinin dizin hâli."""
    by_kin = collections.defaultdict(list)
    for c in spec["creatures"]:
        if c.get("kinFamily"):
            by_kin[c["kinFamily"]].append(c)
    trads = {t["id"]: t for t in spec["traditions"]}
    out = []
    for fam in spec["kinFamilies"]:
        members = sorted(by_kin.get(fam["id"], []), key=lambda c: c["number"])
        out.append({
            "family": fam["id"],
            "tr": fam["tr"],
            "en": fam["en"],
            "motif": fam["motif"],
            "image": fam["image"],
            "divergence": fam["divergence"],
            "members": [
                {
                    "name": c["name"], "id": c["id"],
                    "tradition": trads.get(c["tradition"], {}).get("name", ""),
                    "sigil": trads.get(c["tradition"], {}).get("sigil", ""),
                    "page": page_of(pm, c["id"]),
                }
                for c in members
            ],
        })
    return out


def index_pronunciation(spec: dict, pm: dict) -> list[dict]:
    """Telaffuz rehberi — alfabetik, alternatif yazımlardan çapraz gönderme."""
    rows = []
    for c in sorted(spec["creatures"], key=lambda c: sortkey(c["name"])):
        rows.append({
            "name": c["name"],
            "id": c["id"],
            "pronunciation": c.get("pronunciation") or "—",
            "page": page_of(pm, c["id"]),
            "type": "entry",
        })
        for alt in c.get("altNames") or []:
            rows.append({
                "name": alt,
                "id": c["id"],
                "seeAlso": c["name"],
                "pronunciation": "",
                "page": page_of(pm, c["id"]),
                "type": "crossref",
            })
    return sorted(rows, key=lambda r: sortkey(r["name"]))


# =============================================================================
# ÖNİZLEME
# =============================================================================

def render_md(idx: dict, spec: dict) -> str:
    L = []
    A = L.append
    A("# Dizin önizlemesi — Codex Bestiarium")
    A("")
    A("<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/make_index.py · ELLE DÜZENLEMEYİN -->")
    A("")
    A("Dört dizin `01_SOURCE/spec.json`'dan üretilir. Sayfa numaraları dizgiden")
    A("okunur; `—` görüyorsanız o sürüm henüz dizilmemiştir.")
    A("")

    A("## 1. Gelenek dizini")
    A("")
    A("| Gelenek | İşaret | Bölge | Cilt 1 | Maddeler |")
    A("|---|---|---|---|---|")
    for t in idx["traditions"]:
        ent = " · ".join(
            f"{e['name']} ({e['page']})" for e in t["entries"]
        )
        A(f"| {t['tradition']} | {t['sigil']} | {t['regionGroup']} | "
          f"{'✓' if t['inherited'] else '—'} | {ent} |")
    A("")

    A("## 2. Motif dizini")
    A("")
    A("| Motif | Bölüm | Maddeler |")
    A("|---|---|---|")
    for m in idx["motifs"]:
        ent = " · ".join(f"{e['name']} ({e['page']})" for e in m["entries"])
        A(f"| `{m['motif']}` | {m['section']} | {ent} |")
    A("")

    A("## 3. Akraba imge tablosu")
    A("")
    for fam in idx["kin"]:
        A(f"### {fam['family']} · {fam['tr']} — *{fam['en']}* · `{fam['motif']}`")
        A("")
        A(f"> {fam['image']}")
        A("")
        A("| Üye | Gelenek | Sayfa |")
        A("|---|---|---:|")
        for m in fam["members"]:
            A(f"| {m['name']} | {m['tradition']} {m['sigil']} | {m['page']} |")
        A("")
        A(f"**Ayrışma noktası.** {fam['divergence']}")
        A("")

    A("## 4. Telaffuz rehberi")
    A("")
    A("| Ad | Telaffuz | Sayfa |")
    A("|---|---|---:|")
    for row in idx["pronunciation"]:
        if row["type"] == "crossref":
            A(f"| {row['name']} | *bkz.* {row['seeAlso']} | {row['page']} |")
        else:
            A(f"| **{row['name']}** | {row['pronunciation']} | {row['page']} |")
    A("")
    return "\n".join(L) + "\n"


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pagemap", default="04_PRINT/PAPERBACK/pagemap.json")
    ap.add_argument(
        "--gate",
        choices=["draft", "phase2", "phase6"],
        default="draft",
        help="draft: eksik telaffuz/sayfa uyarıdır · "
             "phase2: telaffuz zorunlu · phase6: sayfa numarası da zorunlu",
    )
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    spec = load_spec()
    pm = load_pagemap(args.pagemap)

    idx = {
        "traditions": index_traditions(spec, pm),
        "motifs": index_motifs(spec, pm),
        "kin": index_kin(spec, pm),
        "pronunciation": index_pronunciation(spec, pm),
    }

    r = Result("DİZİN ÜRETİMİ (make_index)")
    r.ok("gelenek dizini", f"{len(idx['traditions'])} gelenek")
    r.ok("motif dizini", f"{len(idx['motifs'])} benzersiz Thompson kodu")
    r.ok("akraba imge tablosu",
         f"{len(idx['kin'])} aile · "
         f"{sum(len(f['members']) for f in idx['kin'])} üye")
    r.ok("telaffuz rehberi", f"{len(idx['pronunciation'])} satır")

    # Kapılar kümülatiftir: eksik telaffuz Faz 2'den ÖNCE bir uyarı, sonra
    # bir hatadır. Henüz açılmamış bir kapı yüzünden CI kırmızı yanmaz —
    # ama kapı açılınca affetmez.
    missing_pron = [
        row["name"] for row in idx["pronunciation"]
        if row["type"] == "entry" and row["pronunciation"] == "—"
    ]
    pron_detail = (
        f"{len(missing_pron)} eksik: {missing_pron[:10]} — Faz 2 kapısı"
    )
    if missing_pron and args.gate == "draft":
        r.warn("her maddede telaffuz var", pron_detail)
    else:
        r.add(not missing_pron, "her maddede telaffuz var", pron_detail)

    if not pm:
        detail = (
            f"{args.pagemap} bulunamadı — dizin numarasız üretildi. "
            "Faz 6 kapısı: dizin sayfa numaraları gerçek dizgiyle eşleşmeli."
        )
        if args.gate == "phase6":
            r.fail("sayfa haritası mevcut", detail)
        else:
            r.warn("sayfa haritası yok", detail)
    else:
        no_page = [
            c["id"] for c in spec["creatures"] if c["id"] not in pm
        ]
        r.add(not no_page, "her maddenin sayfa numarası var", f"{no_page[:10]}")

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(idx, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write(render_md(idx, spec))

    print(f"yazıldı: {os.path.relpath(OUT_JSON, ROOT)}")
    print(f"yazıldı: {os.path.relpath(OUT_MD, ROOT)}")
    return r.report(verbose=args.verbose)


if __name__ == "__main__":
    raise SystemExit(main())
