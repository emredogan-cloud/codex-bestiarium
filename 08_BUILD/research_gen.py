#!/usr/bin/env python3
"""
CODEX BESTIARIUM — ARAŞTIRMA DOSYASI ÜRETİCİSİ VE SENKRONİZASYONU
================================================================================
Araştırma, gelenek başına bir JSON dosyasında yazılır:

    01_SOURCE/research_data/<tradition>.json

Bu betik ondan iki şey üretir:

    01_SOURCE/research/<id>.md   insan okunur araştırma dosyası
    01_SOURCE/spec.json          sources · region · attested · motifVerified
                                 · restrictionScreened · altNames · pronunciation
                                 · variantNote · status

NEDEN BU MİMARİ?
    Yol haritası 120 araştırma dosyası istiyor ve her birinin aynı yapıyı
    taşımasını şart koşuyor (DoD #2). 120 markdown dosyasını elle tutarlı
    tutmak, 120 spec kaydını elle tutarlı tutmakla aynı sorundur — ve
    `seed_import.py` için verilen karar burada da geçerlidir: TÜRET, YAZMA.

    Araştırmanın kendisi (künyeler, alıntılar, kararlar) elle yazılır;
    biçim üretilir.

KAPI
    Her kayıt `00_CONTEXT/SOURCING_STANDARD.md`'deki ölçütten geçmeden
    `status: "verified"` alamaz:
      · ≥2 index-olmayan kaynak
      · en az biri primary veya scholarly
      · en az birinin doğrulaması fulltext, toc, canon veya article
      · motifNote dolu
      · yaşayan gelenekse restriction alanı dolu

KULLANIM
    python3 08_BUILD/research_gen.py              # üret + spec'i senkronla
    python3 08_BUILD/research_gen.py --check      # bayat mı? değilse çıkış 1
    python3 08_BUILD/research_gen.py --report     # kapsam özeti
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    LIVING_TRADITIONS,
    RESEARCH_DIR,
    ROOT,
    SOURCE_DIR,
    SPEC_PATH,
    Result,
    load_spec,
    motif_valid,
)

DATA_DIR = os.path.join(SOURCE_DIR, "research_data")

SOURCE_TYPES = {"primary", "scholarly", "reference", "index"}
INDEPENDENT_TYPES = {"primary", "scholarly", "reference"}
STRONG_TYPES = {"primary", "scholarly"}
VERIFICATION_LEVELS = {"fulltext", "toc", "canon", "article", "sv", "catalog", "secondary"}
# Güç ölçütü "okudum mu" değil, "okur gidip KESİN bir yere bakabilir mi"dir.
STRONG_VERIFICATION = {"fulltext", "toc", "canon", "article", "sv"}

GENERATED = (
    "<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py\n"
    "     Kaynak: 01_SOURCE/research_data/<gelenek>.json\n"
    "     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->"
)


# =============================================================================
# YÜKLEME
# =============================================================================

def load_data() -> dict:
    """Bütün gelenek dosyalarını tek sözlükte toplar: id → kayıt."""
    out: dict[str, dict] = {}
    for path in sorted(glob.glob(os.path.join(DATA_DIR, "*.json"))):
        if os.path.basename(path).startswith("_"):
            continue
        with open(path, encoding="utf-8") as fh:
            block = json.load(fh)
        for rec in block.get("creatures", []):
            rec["_file"] = os.path.basename(path)
            out[rec["id"]] = rec
    return out


# =============================================================================
# KAPI
# =============================================================================

def gate(rec: dict, tradition: str) -> list[str]:
    """Bu kaydın `verified` olmasını engelleyen sebepler. Boşsa geçer."""
    problems: list[str] = []
    srcs = rec.get("sources", [])

    for s in srcs:
        # `sv` (sub verbo) yalnızca ALFABETİK başvuru cildi için geçerlidir.
        # Bir monografiye `sv` yazmak, olmayan bir kesinlik iddia etmektir.
        if s.get("verification") == "sv" and s.get("type") != "reference":
            problems.append(
                f"`sv` yalnızca `reference` katmanında kullanılabilir; "
                f"burada tip `{s.get('type')}`")
        if s.get("type") not in SOURCE_TYPES:
            problems.append(f"geçersiz kaynak tipi: {s.get('type')!r}")
        if s.get("verification") not in VERIFICATION_LEVELS:
            problems.append(
                f"geçersiz doğrulama seviyesi: {s.get('verification')!r}"
            )
        if not s.get("ref", "").strip():
            problems.append("künyesi boş kaynak")

    independent = [s for s in srcs if s.get("type") in INDEPENDENT_TYPES]
    if len(independent) < 2:
        problems.append(
            f"{len(independent)} bağımsız kaynak (≥2 gerekir; motif dizini sayılmaz)"
        )
    if not any(s.get("type") in STRONG_TYPES for s in independent):
        problems.append(
            "hiçbir kaynak primary/scholarly değil — yalnızca başvuru cildi yetmez"
        )
    if not any(s.get("verification") in STRONG_VERIFICATION for s in independent):
        problems.append(
            "hiçbir bağımsız kaynağın doğrulaması kesin-yer düzeyinde değil (fulltext/toc/canon/article/sv)"
        )

    if not rec.get("motifNote", "").strip():
        problems.append("motifNote boş — kodun neden uyduğu yazılmalı")
    # İKİ KAPI AYNI ŞEYİ SÖYLEMELİ. validate_spec --gate phase1 "doğrulanmış
    # maddenin motif kodu da doğrulanmış olmalı" der; bu kapı onu söylemiyordu
    # ve ikisi ayrıştı (aralez, nhang). Sıkı olan doğrudur: motifi
    # doğrulanmamış bir madde 'verified' olamaz.
    if not rec.get("motifVerified"):
        problems.append("motif kodu doğrulanmadı — madde 'verified' olamaz")
    for m in rec.get("motif", []):
        if not motif_valid(m):
            problems.append(f"geçersiz motif kodu: {m}")
    if not rec.get("motif"):
        problems.append("motif kodu yok")

    if not rec.get("region", "").strip():
        problems.append("region boş")
    if not rec.get("attested", "").strip():
        problems.append("attested boş")

    if tradition in LIVING_TRADITIONS and not rec.get("restriction", "").strip():
        problems.append("yaşayan gelenek — restriction alanı boş")

    return problems


# =============================================================================
# MARKDOWN ÜRETİMİ
# =============================================================================

def load_kin_notes() -> dict[tuple[str, str], dict]:
    """(a, b) → bağ kaydı. Faz 2'nin çapraz referans notları.

    Not kaynağı `01_SOURCE/kin_map.json`'dur ve `classify.py` onu spec'e
    işler; buradaki iş yalnızca notu araştırma dosyasında GÖSTERMEKTİR.
    """
    path = os.path.join(SOURCE_DIR, "kin_map.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        km = json.load(fh)
    out: dict[tuple[str, str], dict] = {}
    for l in km.get("links", []):
        out[(l["a"], l["b"])] = l
        out[(l["b"], l["a"])] = l
    return out


def render_md(rec: dict, spec_rec: dict, spec: dict,
              kin_notes: dict | None = None) -> str:
    trads = {t["id"]: t for t in spec["traditions"]}
    classes = {c["id"]: c for c in spec["classes"]}
    kin = {k["id"]: k for k in spec["kinFamilies"]}
    by_id = {c["id"]: c for c in spec["creatures"]}
    kin_notes = kin_notes if kin_notes is not None else {}

    trad = trads.get(spec_rec["tradition"], {})
    klass = classes.get(spec_rec["class"], {})
    fam = kin.get(spec_rec.get("kinFamily")) if spec_rec.get("kinFamily") else None

    L: list[str] = []
    A = L.append

    A(f"# {rec['name']} — araştırma dosyası")
    A("")
    A(GENERATED)
    A("")

    A("| Alan | Değer |")
    A("|---|---|")
    A(f"| **id** | `{rec['id']}` |")
    A(f"| **Ad** | {rec['name']} |")
    alt = rec.get("altNames") or []
    A(f"| **Alternatif yazımlar** | {', '.join(alt) if alt else '—'} |")
    A(f"| **Gelenek** | {trad.get('name', '?')} {trad.get('sigil', '')} · "
      f"{trad.get('regionGroup', '')} |")
    A(f"| **Sınıf** | {spec_rec['class']} · {klass.get('en', '')} "
      f"({klass.get('tr', '')}) |")
    kin_cell = f"{spec_rec['kinFamily']} · {fam['tr']}" if fam else "—"
    A(f"| **Akraba ailesi** | {kin_cell} |")
    A(f"| **Plaka** | `{spec_rec['plate']}` |")
    A(f"| **Telaffuz (taslak)** | {rec.get('pronunciation', '—') or '—'} |")
    A(f"| **Durum** | `{rec.get('status', 'draft')}` |")
    A("")

    A("## 1. Kaynaklar")
    A("")
    A("> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)")
    A("> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin")
    A("> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.")
    A("")
    for i, s in enumerate(rec.get("sources", []), 1):
        A(f"### Kaynak {i} · `{s['type']}` · doğrulama `{s['verification']}`")
        A("")
        A(f"- **Künye:** {s['ref']}")
        if s.get("access"):
            A(f"- **Erişim:** {s['access']}")
        if s.get("locus"):
            A(f"- **Yer:** {s['locus']}")
        if s.get("note"):
            A(f"- **Not:** {s['note']}")
        if s.get("quote"):
            A("- **İlgili alıntı:**")
            A("")
            for line in s["quote"].split("\n"):
                A(f"  > {line}")
        A("")

    A("## 2. Motif kodu")
    A("")
    A("| Kod | Thompson tanımı | Doğrulandı |")
    A("|---|---|---|")
    for m in rec.get("motif", []):
        A(f"| `{m}` | {rec.get('motifDefs', {}).get(m, '—')} | "
          f"{'✅' if rec.get('motifVerified') else '⬜'} |")
    A("")
    A(f"**Gerekçe.** {rec.get('motifNote', '—')}")
    A("")
    if rec.get("motifChanged"):
        A(f"> ⚠ **Tohum kodu değiştirildi.** {rec['motifChanged']}")
        A("")

    A("## 3. Coğrafya ve ilk kayıt")
    A("")
    A(f"- **Bölge:** {rec.get('region', '—')}")
    A(f"- **İlk kayıt (attested):** {rec.get('attested', '—')}")
    if rec.get("spread"):
        A(f"- **Yayılım:** {rec['spread']}")
    A("")

    A("## 4. Fiziksel tarif")
    A("")
    A("> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü")
    A("> hem de plaka promptunu besler.")
    A("")
    for item in rec.get("appearance", []):
        A(f"- {item}")
    if not rec.get("appearance"):
        A("- —")
    A("")

    A("## 5. Davranış ve kayıtlı vaka")
    A("")
    A(f"- **Ne yapar:** {rec.get('behaviour', '—')}")
    A(f"- **Kayıtlı vaka:** {rec.get('incident', '—')}")
    A(f"- **Karşı önlem:** {rec.get('counter', '—')}")
    A("")

    A("## 6. Varyantlar")
    A("")
    variants = rec.get("variants", [])
    if variants:
        A("| Bölge / kaynak | Fark |")
        A("|---|---|")
        for v in variants:
            A(f"| {v['where']} | {v['what']} |")
    else:
        A("*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*")
    A("")
    if rec.get("variantNote"):
        A(f"**Varyant notu.** {rec['variantNote']}")
        A("")

    A("## 7. Akrabalar")
    A("")
    A("> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·")
    A("> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.")
    A("> Bu tablo maddenin 6. bölümünün (\"Akrabaları\") ham malzemesidir.")
    A("")
    refs = spec_rec.get("crossRefs") or []
    if refs:
        A("| Madde | Gelenek | Bağ | Ayrışma noktası |")
        A("|---|---|---|---|")
        for rid in refs:
            other = by_id.get(rid, {})
            otrad = trads.get(other.get("tradition", ""), {})
            link = kin_notes.get((spec_rec["id"], rid), {})
            A(f"| **{other.get('name', rid)}** `{rid}` | "
              f"{otrad.get('name', '?')} {otrad.get('sigil', '')} | "
              f"`{link.get('type', '—')}` | {link.get('note', '—')} |")
    else:
        A("*Faz 2'de doldurulacak.*")
    A("")

    A("## 8. Kısıtlılık taraması")
    A("")
    if spec_rec["tradition"] in LIVING_TRADITIONS:
        A("> **Yaşayan gelenek — bu tarama zorunludur.**")
        A("")
        A(f"{rec.get('restriction', '—')}")
    else:
        A("Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.")
        if rec.get("restriction"):
            A("")
            A(rec["restriction"])
    A("")

    A("## 9. Modern kurgu etkisi")
    A("")
    A(rec.get("modern", "*Kaydedilmedi.*"))
    A("")

    A("## 10. Yazım notları")
    A("")
    for note in rec.get("writingNotes", []):
        A(f"- {note}")
    if not rec.get("writingNotes"):
        A("- —")
    A("")

    A("## Kontrol listesi")
    A("")
    problems = gate(rec, spec_rec["tradition"])
    checks = [
        ("En az iki bağımsız kaynak, tam künyeyle",
         len([s for s in rec.get("sources", []) if s["type"] in INDEPENDENT_TYPES]) >= 2),
        ("En az biri primary/scholarly",
         any(s["type"] in STRONG_TYPES for s in rec.get("sources", []))),
        ("En az biri kesin-yer doğrulamalı (fulltext/toc/canon/article)",
         any(s["verification"] in STRONG_VERIFICATION for s in rec.get("sources", []))),
        ("Motif kodu doğrulandı ve gerekçelendirildi",
         bool(rec.get("motifVerified")) and bool(rec.get("motifNote"))),
        ("Bölge somut, ilk kayıt tarihli",
         bool(rec.get("region")) and bool(rec.get("attested"))),
        ("Fiziksel tarif kaynağa dayanıyor", bool(rec.get("appearance"))),
        ("Kısıtlılık taraması yapıldı (yaşayan gelenekse)",
         spec_rec["tradition"] not in LIVING_TRADITIONS or bool(rec.get("restriction"))),
        ("Telaffuz taslağı yazıldı", bool(rec.get("pronunciation"))),
        ("Bu dosyada proza cümlesi yok", True),
    ]
    for label, ok in checks:
        A(f"- [{'x' if ok else ' '}] {label}")
    A("")
    if problems:
        A("> ⛔ **Kapı açık değil:**")
        for p in problems:
            A(f"> - {p}")
        A("")

    return "\n".join(L) + "\n"


# =============================================================================
# SPEC SENKRONİZASYONU
# =============================================================================

def sync_spec(data: dict, spec: dict) -> tuple[dict, list[str]]:
    changes: list[str] = []
    for c in spec["creatures"]:
        rec = data.get(c["id"])
        if not rec:
            continue
        problems = gate(rec, c["tradition"])
        research_ok = not problems and rec.get("status") != "dropped"

        # Araştırma hattı ARAŞTIRMA durumunun sahibidir, YAZIM durumunun
        # değil. Faz 3'te bulundu: bu satır `verified` yazdığı için, yazılmış
        # bir maddeyi `written` işaretlemek `--check`'i bayat gösteriyordu ve
        # `qa_all.sh --fix` durumu sessizce `verified`'a geri alıyordu — yani
        # tamamlanmış yazım işi her tazeleme koşusunda kayboluyordu.
        #
        # Kural: araştırma kapısı DÜŞERSE durum draft'a iner (kalite geriye
        # gidemez, araştırması bozulan madde yazılmış sayılamaz). Araştırma
        # geçerliyse, `written`/`edited`/`final` KORUNUR.
        cur = c.get("status", "draft")
        if not research_ok:
            new_status = "draft"
        elif cur in ("written", "edited", "final"):
            new_status = cur
        else:
            new_status = "verified"

        updates = {
            "pronunciation": rec.get("pronunciation", ""),
            "motif": rec.get("motif", c["motif"]),
            "motifVerified": bool(rec.get("motifVerified")) and not problems,
            "altNames": rec.get("altNames", []),
            "region": rec.get("region", ""),
            "attested": rec.get("attested", ""),
            "sources": [
                {k: v for k, v in s.items() if k in ("ref", "type", "verification", "locus")}
                for s in rec.get("sources", [])
            ],
            "variantNote": rec.get("variantNote", ""),
            # Kodun NEDEN seçildiği ve tohumdan neyin değiştiği kaydın
            # parçasıdır: kitabın 7. bölümü bunu basıyor ("tohum kodu
            # A812 yanlıştı"). Spec bunu taşımazsa `factcheck.py` o
            # cümleyi "kayıtta olmayan kod" diye itiraz eder ve haklıdır —
            # kayıt gerçekten taşımıyordur.
            "motifNote": rec.get("motifNote", ""),
            "motifChanged": rec.get("motifChanged", ""),
            "restrictionScreened": bool(rec.get("restriction", "").strip()),
            "status": new_status,
        }
        for k, v in updates.items():
            if c.get(k) != v:
                changes.append(f"{c['id']}.{k}")
                c[k] = v
    return spec, changes


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    spec = load_spec()
    data = load_data()
    by_id = {c["id"]: c for c in spec["creatures"]}

    # DÜŞÜRÜLEN maddeler: araştırma verisi KORUNUR (yapılan iş ve düşürme
    # gerekçesi kayıt altında kalmalı) ama spec'e girmez. Bunları hata saymak
    # yanlış olur — düşürme bir KARARDIR, bir tutarsızlık değil.
    dropped = set()
    amend_path = os.path.join(SOURCE_DIR, "scope_amendments.json")
    if os.path.exists(amend_path):
        with open(amend_path, encoding="utf-8") as fh:
            dropped = {
                a["id"] for a in json.load(fh).get("amendments", [])
                if a.get("action") == "drop"
            }
    skipped = sorted(k for k in data if k in dropped)
    for k in skipped:
        data.pop(k)
    if skipped:
        print(f"atlandı  : {len(skipped)} düşürülmüş madde ({', '.join(skipped[:5])}"
              f"{'…' if len(skipped) > 5 else ''}) — kararlar scope_amendments.json'da")

    unknown = [k for k in data if k not in by_id]
    if unknown:
        print(f"HATA: spec.json'da olmayan kimlik: {unknown}", file=sys.stderr)
        return 2

    # --- markdown üret ---
    os.makedirs(RESEARCH_DIR, exist_ok=True)
    kin_notes = load_kin_notes()
    stale: list[str] = []
    for cid, rec in data.items():
        content = render_md(rec, by_id[cid], spec, kin_notes)
        path = os.path.join(RESEARCH_DIR, f"{cid}.md")
        if args.check:
            if not os.path.exists(path):
                stale.append(f"{cid}.md (yok)")
            else:
                with open(path, encoding="utf-8") as fh:
                    if fh.read() != content:
                        stale.append(f"{cid}.md")
        else:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)

    # --- spec senkronla ---
    spec, changes = sync_spec(data, spec)
    if args.check:
        with open(SPEC_PATH, encoding="utf-8") as fh:
            current = fh.read()
        want = json.dumps(spec, ensure_ascii=False, indent=2) + "\n"
        if current != want:
            stale.append("spec.json")
        if stale:
            print("BAYAT: " + ", ".join(stale[:12]))
            print("Düzeltmek için: python3 08_BUILD/research_gen.py")
            return 1
        print("TAMAM: araştırma dosyaları ve spec.json güncel.")
        return 0

    with open(SPEC_PATH, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(f"üretildi : {len(data)} araştırma dosyası")
    if changes:
        print(f"spec     : {len(changes)} alan güncellendi")

    # --- rapor ---
    if args.report or args.verbose:
        r = Result("ARAŞTIRMA KAPSAMI (research_gen)")
        verified = [c for c in spec["creatures"] if c["status"] == "verified"]
        r.ok("doğrulanmış madde", f"{len(verified)}/{len(spec['creatures'])}")

        blocked = []
        for cid, rec in sorted(data.items()):
            problems = gate(rec, by_id[cid]["tradition"])
            if problems:
                blocked.append(f"{cid}: {'; '.join(problems)}")
        r.add(not blocked, "kapıdan geçmeyen kayıt yok",
              "\n         ".join(blocked[:15]))

        by_trad = collections.Counter(
            by_id[cid]["tradition"] for cid in data
        )
        done_trads = [t for t, n in by_trad.items() if n == 3]
        r.ok("tamamlanmış gelenek", f"{len(done_trads)}/40")

        src_types = collections.Counter(
            s["type"] for rec in data.values() for s in rec.get("sources", [])
        )
        r.ok("kaynak dağılımı", str(dict(src_types)))
        ver_levels = collections.Counter(
            s["verification"] for rec in data.values() for s in rec.get("sources", [])
        )
        r.ok("doğrulama dağılımı", str(dict(ver_levels)))
        r.report(verbose=args.verbose)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
