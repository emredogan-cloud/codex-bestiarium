#!/usr/bin/env python3
"""
CODEX BESTIARIUM — spec.json ŞEMA VE BÜTÜNLÜK DOĞRULAMASI
================================================================================
120 kaydı elle tutarlı tutmak mümkün değildir. Bu betik olmadan Faz 1'e
başlanmaz (yol haritası Bölüm 14).

KAPI SEVİYELERİ
---------------
Kapılar kümülatiftir: her seviye kendinden öncekileri de çalıştırır. CI hangi
fazda olduğumuzu `--gate` ile bilir; kapı yükseldiğinde eski kayıtlar ayakta
kalmak zorundadır — kalite geriye gidemez.

    --gate draft    Faz 0 · yapı, kimlik, tip, tekillik
    --gate phase1   Faz 1 · iki bağımsız kaynak, doğrulanmış motif, kısıt taraması
    --gate phase2   Faz 2 · telaffuz, çapraz referans grafiği, aile üyelikleri
    --gate phase3   Faz 3+ · yazım durumu, araştırma dosyası mevcudiyeti

KULLANIM
    python3 08_BUILD/validate_spec.py
    python3 08_BUILD/validate_spec.py --gate phase1 --verbose
    python3 08_BUILD/validate_spec.py --json 06_REPORTS/spec-validation.json
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    CLASS_COUNT_CEIL,
    CLASS_COUNT_FLOOR,
    CLASS_IDS,
    CROSSREF_BAND,
    KIN_IDS,
    LIVING_TRADITIONS,
    MIN_SOURCES,
    ROOT,
    SPEC_PATH,
    STATUS_ORDER,
    TARGET_CREATURES,
    TARGET_TRADITIONS,
    VERIFY_FLOOR,
    WORD_BAND,
    Result,
    load_spec,
    motif_valid,
    slugify,
)

GATES = ["draft", "phase1", "phase2", "phase3"]

REQUIRED_FIELDS = {
    "id": str,
    "number": int,
    "name": str,
    "pronunciation": str,
    "tradition": str,
    "class": str,
    "motif": list,
    "motifVerified": bool,
    "altNames": list,
    "region": str,
    "attested": str,
    "sources": list,
    "crossRefs": list,
    "plate": str,
    "wordTarget": int,
    "variantNote": str,
    "restrictionScreened": bool,
    "researchFile": str,
    "status": str,
}


# =============================================================================
# SEVİYE 0 — YAPI
# =============================================================================

def check_structure(spec: dict, r: Result) -> None:
    for key in ("meta", "classes", "kinFamilies", "traditions", "creatures"):
        r.add(key in spec, f"üst düzey anahtar var: {key}")

    classes = {c["id"] for c in spec.get("classes", [])}
    r.add(
        classes == set(CLASS_IDS),
        "altı sınıf tanımlı (I–VI)",
        f"bulunan: {sorted(classes)}",
    )

    kin = {k["id"] for k in spec.get("kinFamilies", [])}
    r.add(
        kin == set(KIN_IDS),
        "sekiz akraba imge ailesi tanımlı (A–H)",
        f"bulunan: {sorted(kin)}",
    )

    trads = spec.get("traditions", [])
    r.add(
        len(trads) == TARGET_TRADITIONS,
        f"gelenek sayısı {TARGET_TRADITIONS}",
        f"bulunan: {len(trads)}",
    )

    trad_ids = [t["id"] for t in trads]
    dupes = [i for i, n in collections.Counter(trad_ids).items() if n > 1]
    r.add(not dupes, "gelenek kimlikleri benzersiz", f"kopya: {dupes}")

    inherited = sum(1 for t in trads if t.get("inherited"))
    r.add(
        inherited == 19,
        "Cilt 1'den devralınan gelenek sayısı 19",
        f"bulunan: {inherited} — seri sürekliliği bu sayıya bağlı",
    )


def check_records(spec: dict, r: Result) -> None:
    creatures = spec.get("creatures", [])
    trad_ids = {t["id"] for t in spec.get("traditions", [])}

    r.add(
        len(creatures) == TARGET_CREATURES,
        f"madde sayısı {TARGET_CREATURES}",
        f"bulunan: {len(creatures)}",
    )

    # --- alan ve tip ---
    bad_fields: list[str] = []
    for c in creatures:
        for field, typ in REQUIRED_FIELDS.items():
            if field not in c:
                bad_fields.append(f"{c.get('id', '?')}: eksik alan '{field}'")
            elif not isinstance(c[field], typ):
                bad_fields.append(
                    f"{c.get('id', '?')}: '{field}' {typ.__name__} olmalı, "
                    f"{type(c[field]).__name__} bulundu"
                )
    r.add(not bad_fields, "bütün kayıtlarda zorunlu alanlar ve tipler doğru",
          "\n         ".join(bad_fields[:12]))

    # --- kimlik tekilliği ---
    ids = [c.get("id") for c in creatures]
    dupes = [i for i, n in collections.Counter(ids).items() if n > 1]
    r.add(not dupes, "madde kimlikleri benzersiz", f"kopya: {dupes}")

    # --- kimlik biçimi: slug(name) veya slug(name)-<gelenek> ---
    bad_slug = [
        c["id"]
        for c in creatures
        if c.get("id") not in (slugify(c.get("name", "")),
                               f"{slugify(c.get('name', ''))}-{c.get('tradition')}")
    ]
    r.add(not bad_slug, "kimlikler addan türetilmiş", f"uyumsuz: {bad_slug[:10]}")

    # --- ad tekilliği (aynı ad iki gelenekte olabilir; ikisi de işaretlenmeli) ---
    names = [c.get("name") for c in creatures]
    dupe_names = [n for n, k in collections.Counter(names).items() if k > 1]
    if dupe_names:
        r.warn(
            "aynı ada sahip madde var",
            f"{dupe_names} — dizinde çapraz gönderme zorunlu, kimlik ayrıştırıldı",
        )
    else:
        r.ok("madde adları benzersiz")

    # --- numara ---
    nums = sorted(c.get("number", 0) for c in creatures)
    r.add(
        nums == list(range(1, len(creatures) + 1)),
        "madde numaraları 1..N kesintisiz ve benzersiz",
    )

    # --- sınıf ---
    bad_class = [c["id"] for c in creatures if c.get("class") not in CLASS_IDS]
    r.add(not bad_class, "her madde geçerli bir sınıfta (I–VI)", f"{bad_class[:10]}")

    # --- gelenek ---
    orphan = [c["id"] for c in creatures if c.get("tradition") not in trad_ids]
    r.add(not orphan, "her madde tanımlı bir geleneğe bağlı", f"{orphan[:10]}")

    # --- akraba ailesi ---
    bad_kin = [
        c["id"]
        for c in creatures
        if c.get("kinFamily") is not None and c.get("kinFamily") not in KIN_IDS
    ]
    r.add(not bad_kin, "akraba ailesi değerleri geçerli (A–H veya null)",
          f"{bad_kin[:10]}")

    # --- motif kodu biçimi ---
    bad_motif = [
        f"{c['id']}: {m}"
        for c in creatures
        for m in c.get("motif", [])
        if not motif_valid(m)
    ]
    r.add(not bad_motif, "Thompson motif kodları biçimsel olarak geçerli",
          "; ".join(bad_motif[:10]))

    no_motif = [c["id"] for c in creatures if not c.get("motif")]
    r.add(not no_motif, "her maddede en az bir motif kodu var", f"{no_motif[:10]}")

    # --- plaka ---
    plates = [c.get("plate") for c in creatures]
    dupe_plates = [p for p, n in collections.Counter(plates).items() if n > 1]
    r.add(not dupe_plates, "plaka kimlikleri benzersiz", f"kopya: {dupe_plates}")

    mismatched = [
        c["id"]
        for c in creatures
        if c.get("plate") != f"plate-{c.get('number', 0):03d}"
    ]
    r.add(not mismatched, "plaka kimliği madde numarasıyla eşleşiyor",
          f"{mismatched[:10]}")

    # --- durum ---
    bad_status = [c["id"] for c in creatures if c.get("status") not in STATUS_ORDER]
    r.add(not bad_status, "durum değerleri geçerli", f"{bad_status[:10]}")

    # --- kelime hedefi ---
    lo, hi = WORD_BAND
    bad_target = [
        c["id"] for c in creatures if not lo <= c.get("wordTarget", 0) <= hi
    ]
    r.add(not bad_target, f"kelime hedefleri {lo}–{hi} bandında",
          f"{bad_target[:10]}")


def _dropped_per_tradition(spec: dict) -> dict[str, int]:
    """Kapsam kararıyla DÜŞÜRÜLMÜŞ madde sayısı, gelenek başına.

    Düşen maddenin geleneği tohum tablosunda kalır ama kaydı spec'te yoktur;
    gelenek eşlemesi araştırma verisinden okunur (iş korunmuştur), yoksa
    `scope_amendments.json`'daki `tradition` alanından.
    """
    amend_path = os.path.join(ROOT, "01_SOURCE", "scope_amendments.json")
    if not os.path.exists(amend_path):
        return {}
    with open(amend_path, encoding="utf-8") as fh:
        amendments = json.load(fh).get("amendments", [])
    dropped = [a for a in amendments if a.get("action") == "drop"]
    if not dropped:
        return {}

    trad_of: dict[str, str] = {}
    data_dir = os.path.join(ROOT, "01_SOURCE", "research_data")
    if os.path.isdir(data_dir):
        for fname in sorted(os.listdir(data_dir)):
            if not fname.endswith(".json") or fname.startswith("_"):
                continue
            with open(os.path.join(data_dir, fname), encoding="utf-8") as fh:
                block = json.load(fh)
            tid = block.get("tradition") or os.path.splitext(fname)[0]
            for rec in block.get("creatures", []):
                trad_of[rec["id"]] = tid

    counts: collections.Counter = collections.Counter()
    for a in dropped:
        tid = a.get("tradition") or trad_of.get(a.get("id", ""))
        if tid:
            counts[tid] += 1
    return dict(counts)


def check_distribution(spec: dict, r: Result) -> None:
    """Sınıf dağılımı ve aile üyelikleri — kapsam iddiasının sayısal kanıtı."""
    creatures = spec.get("creatures", [])
    by_class = collections.Counter(c.get("class") for c in creatures)

    out_of_band = {
        k: v
        for k, v in by_class.items()
        if not CLASS_COUNT_FLOOR <= v <= CLASS_COUNT_CEIL
    }
    r.add(
        not out_of_band,
        f"hiçbir sınıf {CLASS_COUNT_FLOOR} altında veya {CLASS_COUNT_CEIL} üstünde",
        f"bant dışı: {out_of_band}",
    )

    # Yol haritası Bölüm 03.1 hedefiyle karşılaştır. Sapma bir HATA değil,
    # Faz 2'nin uzlaştırması gereken bir GERÇEKTİR — ama görünmez olamaz.
    targets = {c["id"]: c.get("targetEntries") for c in spec.get("classes", [])}
    drift = {
        k: (by_class.get(k, 0), targets.get(k))
        for k in CLASS_IDS
        if targets.get(k) is not None and by_class.get(k, 0) != targets[k]
    }
    if drift:
        detail = " · ".join(f"{k}: gerçek {a} ≠ hedef {b}" for k, (a, b) in drift.items())
        r.warn("sınıf dağılımı yol haritası hedefinden sapıyor", detail)
    else:
        r.ok("sınıf dağılımı yol haritası hedefiyle birebir")

    # Gelenek başına madde sayısı. Sapmanın kendisi bir hata değildir — ama
    # AÇIKLANMAMIŞ sapma hatadır. Faz 1'in düşürme kararları
    # `scope_amendments.json`'da kayıtlıdır; oradan açıklanan her eksik madde
    # bir KARARDIR. Açıklanamayan bir sapma sessizce geçmez.
    by_trad = collections.Counter(c.get("tradition") for c in creatures)
    uneven = {k: v for k, v in by_trad.items() if v != 3}
    dropped_by_trad = _dropped_per_tradition(spec)
    unexplained = {
        k: v for k, v in uneven.items()
        if v + dropped_by_trad.get(k, 0) != 3
    }
    if unexplained:
        r.fail(
            "gelenek başına madde sayısındaki sapma açıklanmış",
            f"{unexplained} — eksik madde ya 3'e tamamlanır ya da "
            "scope_amendments.json'da gerekçesiyle kayda geçer",
        )
    elif uneven:
        r.ok(
            "gelenek başına madde sayısı",
            f"{len(uneven)} gelenekte 3'ün altında: {uneven} — "
            f"hepsi kayıtlı kapsam kararlarıyla açıklanıyor",
        )
    else:
        r.ok("her gelenekte tam 3 madde")

    # Aile üyelikleri
    by_kin = collections.Counter(
        c.get("kinFamily") for c in creatures if c.get("kinFamily")
    )
    empty = [k for k in KIN_IDS if by_kin.get(k, 0) < 2]
    r.add(
        not empty,
        "her akraba imge ailesinin en az 2 üyesi var",
        f"yetersiz: {empty} — tek üyeli aile karşılaştırma açılışı taşıyamaz",
    )
    bound = sum(by_kin.values())
    r.ok(
        "aileye bağlı madde sayısı",
        f"{bound}/{len(creatures)} · aile dağılımı: {dict(sorted(by_kin.items()))}",
    )


# =============================================================================
# SEVİYE 1 — ARAŞTIRMA KAPISI
# =============================================================================

def check_phase1(spec: dict, r: Result) -> None:
    creatures = spec.get("creatures", [])
    verified = [c for c in creatures if c.get("status") != "draft"]

    r.add(
        len(verified) >= VERIFY_FLOOR,
        f"doğrulanmış madde sayısı ≥ {VERIFY_FLOOR}",
        f"bulunan: {len(verified)} — altına düşerse kapsam 100'e iner, "
        "uydurmayla doldurulmaz",
    )

    thin = []
    bad_src = []
    for c in verified:
        srcs = c.get("sources", [])
        independent = {
            s.get("ref", "").split(",")[0].strip().lower()
            for s in srcs
            if s.get("type") != "index"
        }
        if len(independent) < MIN_SOURCES:
            thin.append(f"{c['id']} ({len(independent)})")
        for s in srcs:
            if not s.get("ref") or not s.get("type"):
                bad_src.append(c["id"])
    r.add(
        not thin,
        f"her doğrulanmış maddede ≥{MIN_SOURCES} BAĞIMSIZ kaynak "
        "(motif dizini sayılmaz)",
        "; ".join(thin[:12]),
    )
    r.add(not bad_src, "her kaynak künyesinde 'ref' ve 'type' dolu",
          f"{sorted(set(bad_src))[:10]}")

    unverified_motif = [c["id"] for c in verified if not c.get("motifVerified")]
    r.add(
        not unverified_motif,
        "doğrulanmış maddelerin motif kodu Thompson'dan teyit edilmiş",
        f"{unverified_motif[:12]} — tahmin edilen kod doğrulanmış sayılmaz",
    )

    unscreened = [
        c["id"]
        for c in verified
        if c.get("tradition") in LIVING_TRADITIONS and not c.get("restrictionScreened")
    ]
    r.add(
        not unscreened,
        "yaşayan gelenek maddeleri kısıtlılık taramasından geçti",
        f"{unscreened[:12]} — kitabın etik omurgası",
    )

    no_region = [c["id"] for c in verified if not c.get("region", "").strip()]
    r.add(not no_region, "doğrulanmış maddelerde bölge alanı dolu",
          f"{no_region[:10]}")

    no_attest = [c["id"] for c in verified if not c.get("attested", "").strip()]
    r.add(
        not no_attest,
        "doğrulanmış maddelerde ilk kayıt (attested) alanı dolu",
        f"{no_attest[:10]} — 'eski çağlardan beri' yazılmaz, tarih verilir",
    )


# =============================================================================
# SEVİYE 2 — TASNİF VE ÇAPRAZ REFERANS KAPISI
# =============================================================================

def check_phase2(spec: dict, r: Result) -> None:
    creatures = spec.get("creatures", [])
    ids = {c["id"] for c in creatures}
    active = [c for c in creatures if c.get("status") != "draft"]

    no_pron = [c["id"] for c in active if not c.get("pronunciation", "").strip()]
    r.add(
        not no_pron,
        "telaffuz alanları dolu",
        f"{no_pron[:12]} — sesli kitabın en zor kısmı burada çözülür",
    )

    lo, hi = CROSSREF_BAND
    bad_count = [
        f"{c['id']} ({len(c.get('crossRefs', []))})"
        for c in active
        if not lo <= len(c.get("crossRefs", [])) <= hi
    ]
    r.add(not bad_count, f"her maddede {lo}–{hi} çapraz referans",
          "; ".join(bad_count[:12]))

    broken = [
        f"{c['id']} → {ref}"
        for c in creatures
        for ref in c.get("crossRefs", [])
        if ref not in ids
    ]
    r.add(not broken, "çapraz referanslar mevcut maddelere işaret ediyor",
          "; ".join(broken[:12]))

    self_ref = [c["id"] for c in creatures if c["id"] in c.get("crossRefs", [])]
    r.add(not self_ref, "hiçbir madde kendine referans vermiyor", f"{self_ref[:10]}")

    # Karşılıklılık: A → B ise B → A olmalı. Tek yönlü bağ dizinde boşluk üretir.
    edges = {(c["id"], ref) for c in creatures for ref in c.get("crossRefs", [])}
    one_way = [f"{a} → {b}" for a, b in edges if (b, a) not in edges and b in ids]
    if one_way:
        r.warn(
            "tek yönlü çapraz referans var",
            f"{one_way[:12]} — akraba satırı iki taraftan da okunabilmeli",
        )
    else:
        r.ok("çapraz referans grafiği simetrik")

    # Aile içi bağ: aynı ailenin üyeleri birbirini görmeli
    by_kin: dict[str, list[str]] = collections.defaultdict(list)
    for c in creatures:
        if c.get("kinFamily"):
            by_kin[c["kinFamily"]].append(c["id"])
    unlinked = []
    for fam, members in by_kin.items():
        member_set = set(members)
        for m in members:
            rec = next(c for c in creatures if c["id"] == m)
            if rec.get("status") == "draft":
                continue
            if not (set(rec.get("crossRefs", [])) & (member_set - {m})):
                unlinked.append(f"{m} ({fam})")
    r.add(
        not unlinked,
        "her aile üyesi en az bir aile kardeşine bağlı",
        f"{unlinked[:12]} — aile bağı kitabın tezidir, boş kalamaz",
    )


# =============================================================================
# SEVİYE 3 — YAZIM KAPISI
# =============================================================================

def check_phase3(spec: dict, r: Result) -> None:
    creatures = spec.get("creatures", [])
    active = [c for c in creatures if c.get("status") != "draft"]

    missing = [
        c["id"]
        for c in active
        if not os.path.exists(os.path.join(ROOT, c.get("researchFile", "")))
    ]
    r.add(
        not missing,
        "doğrulanmış her maddenin araştırma dosyası var",
        f"{missing[:12]}",
    )

    written = [c for c in creatures if c.get("status") in ("written", "edited", "final")]
    r.ok("yazım ilerlemesi", f"{len(written)}/{len(creatures)} madde yazıldı")

    no_plate_note = [
        c["id"] for c in written if not c.get("plate", "").startswith("plate-")
    ]
    r.add(not no_plate_note, "yazılmış maddelerin plaka kimliği atanmış",
          f"{no_plate_note[:10]}")


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", default=SPEC_PATH)
    ap.add_argument("--gate", choices=GATES, default="draft")
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument(
        "--strict",
        action="store_true",
        help="uyarıları da başarısızlık say",
    )
    args = ap.parse_args()

    if not os.path.exists(args.spec):
        print(f"HATA: spec bulunamadı: {args.spec}", file=sys.stderr)
        return 2
    try:
        spec = load_spec(args.spec)
    except json.JSONDecodeError as exc:
        print(f"HATA: spec.json ayrıştırılamadı: {exc}", file=sys.stderr)
        return 2

    r = Result(f"spec.json DOĞRULAMASI · kapı: {args.gate}")
    check_structure(spec, r)
    check_records(spec, r)
    check_distribution(spec, r)

    level = GATES.index(args.gate)
    if level >= 1:
        check_phase1(spec, r)
    if level >= 2:
        check_phase2(spec, r)
    if level >= 3:
        check_phase3(spec, r)

    code = r.report(verbose=args.verbose)
    if args.json_out:
        r.to_json(args.json_out if os.path.isabs(args.json_out)
                  else os.path.join(ROOT, args.json_out))
    if args.strict and r.warnings:
        return 1
    return code


if __name__ == "__main__":
    raise SystemExit(main())
