#!/usr/bin/env python3
"""
CODEX BESTIARIUM — TOHUM VERİTABANI İÇE AKTARICI
================================================================================
Master yol haritasının (`03_CODEX_BESTIARIUM_MASTER_ROADMAP.html`) Bölüm 04'teki
120 satırlık tohum tablosunu makine okunur `01_SOURCE/spec.json` hâline getirir.

NEDEN BİR BETİK?
    120 kaydı elle yazmak bir transkripsiyon hatası kaynağıdır. Yol haritası
    tek doğruluk kaynağıdır; spec.json ondan TÜRETİLİR. Yol haritası
    güncellenirse bu betik yeniden çalıştırılır ve fark `git diff` ile görünür.

ÖNEMLİ
    Bu betik yalnızca `status: "draft"` kayıt üretir. Hiçbir kayıt Faz 1'deki
    "iki bağımsız kaynak" kapısından geçmeden `verified` olamaz. Betik
    araştırma yapmaz, kaynak uydurmaz, telaffuz doldurmaz.

KULLANIM
    python3 08_BUILD/seed_import.py \
        --source ../CODEX_MYTHOLOGICA/03_CODEX_BESTIARIUM_MASTER_ROADMAP.html
    python3 08_BUILD/seed_import.py --check     # spec.json kaynakla uyumlu mu?
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_PATH = os.path.join(ROOT, "01_SOURCE", "spec.json")
DEFAULT_SOURCE = os.path.normpath(
    os.path.join(
        ROOT, "..", "CODEX_MYTHOLOGICA", "03_CODEX_BESTIARIUM_MASTER_ROADMAP.html"
    )
)

# =============================================================================
# 1. SABİT REFERANS VERİSİ  (yol haritası Bölüm 03)
# =============================================================================

CLASSES = [
    {
        "id": "I",
        "en": "THE GUARDIANS",
        "tr": "Bekçiler",
        "definition": "Eşiği, kapıyı, hazineyi, sınırı tutanlar. Geçişin bedelini alan varlıklar.",
        "thompson": ["B11-B19", "F150", "D1146"],
        "targetEntries": 22,
        "targetPages": 56,
    },
    {
        "id": "II",
        "en": "THE DEVOURERS",
        "tr": "Yutucular",
        "definition": "İnsan yiyenler, çocuk çalanlar, kan içenler. Açlığın kişileşmiş hâli.",
        "thompson": ["G11-G399"],
        "targetEntries": 28,
        "targetPages": 70,
    },
    {
        "id": "III",
        "en": "THE SHAPE-CHANGERS",
        "tr": "Şekil Değiştirenler",
        "definition": "Deri değiştirenler, kılık girenler, kandıranlar. Kimliğin güvenilmezliği.",
        "thompson": ["D100-D199", "D610"],
        "targetEntries": 22,
        "targetPages": 56,
    },
    {
        "id": "IV",
        "en": "THE WATER-DWELLERS",
        "tr": "Su Sakinleri",
        "definition": "Nehirde, gölde, denizde, kuyuda olanlar. Boğulmanın anlatıya dönüşmüş hâli.",
        "thompson": ["B11.2", "B91", "F420"],
        "targetEntries": 24,
        "targetPages": 60,
    },
    {
        "id": "V",
        "en": "SKY AND STORM",
        "tr": "Gök ve Fırtına",
        "definition": "Kanat çırpınca gök gürleyenler. Havanın açıklanması.",
        "thompson": ["A280", "B31", "F960"],
        "targetEntries": 14,
        "targetPages": 36,
    },
    {
        "id": "VI",
        "en": "THE RESTLESS DEAD",
        "tr": "Huzursuz Ölüler",
        "definition": "Gömülmüş ama gitmemiş olanlar. Yasın tamamlanmamış hâli.",
        "thompson": ["E200-E599"],
        "targetEntries": 10,
        "targetPages": 26,
    },
]

KIN_FAMILIES = [
    {
        "id": "A",
        "tr": "Su atı",
        "en": "The Water Horse",
        "motif": "B184.1.3",
        "image": "Suyun kıyısında duran, sırtına bineni suya çeken at",
        "divergence": "İrlanda'da yiyicidir, İzlanda'da boğar, Filipinler'de yolu şaşırtır.",
    },
    {
        "id": "B",
        "tr": "Tilki kadın",
        "en": "The Fox Woman",
        "motif": "D113.1",
        "image": "Kadına dönüşen, ömür veya karaciğer alan tilki",
        "divergence": "Çin'de ölümsüzlük arar, Kore'de karaciğer yer, Japonya'da bazen koruyucudur.",
    },
    {
        "id": "C",
        "tr": "Gece cadısı",
        "en": "The Night Hag",
        "motif": "G264",
        "image": "Loğusayı ve yeni doğanı avlayan dişi varlık",
        "divergence": "Dokuz gelenek, bir korku: doğum ölümlerinin folklora dönüşmesi.",
    },
    {
        "id": "D",
        "tr": "Fırtına kuşu",
        "en": "The Storm Bird",
        "motif": "B31",
        "image": "Kanadı gök gürültüsü, gözü şimşek olan dev kuş",
        "divergence": "Mezopotamya'da hırsız, İran'da bilge, Kuzey Amerika'da savaşçı.",
    },
    {
        "id": "E",
        "tr": "Derinlerin yılanı",
        "en": "The Serpent of the Deep",
        "motif": "B11.2.1.1",
        "image": "Dünyayı çevreleyen veya dibinde yatan yılan",
        "divergence": "Kuzeyde kıyameti getirir, Mısır'da her gece yenilir, And'da iki dünyayı bağlar.",
    },
    {
        "id": "F",
        "tr": "Eşik bekçisi",
        "en": "The Threshold Guardian",
        "motif": "F150",
        "image": "Geçilmesi gereken kapıda duran varlık",
        "divergence": "Bazıları cezalandırır, bazıları yalnızca bakar — ve bakış yeterlidir.",
    },
    {
        "id": "G",
        "tr": "Yaban adamı",
        "en": "The Wild Man",
        "motif": "F460",
        "image": "Ormanda/dağda yaşayan, insana benzeyen ama insan olmayan",
        "divergence": "Baskça'da çobanı korur, Amazon'da avcıyı cezalandırır — doğanın tarafı.",
    },
    {
        "id": "H",
        "tr": "Gizli halk",
        "en": "The Hidden People",
        "motif": "F251",
        "image": "Yanı başımızda ama görünmeyen bir topluluk",
        "divergence": "İzlanda'da hâlâ yol güzergâhı değiştirtir — yaşayan folklor.",
    },
]

# Cilt 1'den (Codex Mythologica) devralınan 19 gelenek. Seri sürekliliği
# buradan gelir: aynı işaret, aynı adlandırma.
INHERITED_TRADITIONS = {
    "Hellenic", "Kemet", "Norðr", "Yamato", "Bharatiya", "Ériu", "Sumer",
    "Mēxihcah", "Romana", "Zhōnghuá", "Hangug", "Maya", "Slovjan",
    "Yorùbá · Ashanti", "Pārs", "Mā'ohi", "Inuit", "Türk", "ʿArab",
}

# Yol haritası Bölüm 04 uyarısı: bu gelenekler İngilizce yayımlanmış kaynak
# açısından zayıftır ve kapsam riskinin merkezindedir. Faz 1 bunlarla başlar.
HARD_TRADITIONS = {
    "Melanesia", "Ainu", "Kartveli", "Hayk", "Sápmi", "Nusantara",
    "Ityop'ya", "Mongol",
}

# =============================================================================
# 2. AYRIŞTIRMA
# =============================================================================

TAG = re.compile(r"<[^>]+>")


def _text(fragment: str) -> str:
    """HTML parçasını düz metne indirger, boşlukları normalize eder."""
    out = html.unescape(TAG.sub(" ", fragment))
    return re.sub(r"\s+", " ", out).strip()


def slugify(name: str) -> str:
    """Diakritikleri düşürüp ASCII kebab-case kimlik üretir."""
    # Türkçe/Skandinav özel harfleri, NFD ayrıştırmasının çözemediği yerler
    swaps = {
        "ð": "d", "Ð": "D", "þ": "th", "Þ": "Th", "ø": "o", "Ø": "O",
        "æ": "ae", "Æ": "Ae", "ı": "i", "İ": "I", "ł": "l", "Ł": "L",
        "ʿ": "", "ʻ": "", "'": "", "'": "", "ḫ": "h", "Ḫ": "H",
    }
    for src, dst in swaps.items():
        name = name.replace(src, dst)
    decomposed = unicodedata.normalize("NFD", name)
    ascii_only = "".join(c for c in decomposed if unicodedata.category(c) != "Mn")
    ascii_only = unicodedata.normalize("NFC", ascii_only).lower()
    ascii_only = re.sub(r"[^a-z0-9]+", "-", ascii_only)
    return ascii_only.strip("-")


def parse_seed_table(source_html: str) -> tuple[list[dict], list[dict]]:
    """Bölüm 04 tablosundan gelenek ve yaratık kayıtlarını çıkarır."""
    start = source_html.find('id="s4"')
    if start < 0:
        raise SystemExit("HATA: Bölüm 04 (id=\"s4\") bulunamadı.")
    tbody_start = source_html.find("<tbody>", start)
    tbody_end = source_html.find("</tbody>", tbody_start)
    if tbody_start < 0 or tbody_end < 0:
        raise SystemExit("HATA: Bölüm 04 tablosunun gövdesi bulunamadı.")
    body = source_html[tbody_start + len("<tbody>") : tbody_end]

    rows = re.findall(r"<tr>(.*?)</tr>", body, flags=re.S)
    traditions: list[dict] = []
    creatures: list[dict] = []
    current: dict | None = None

    for row in rows:
        cells = re.findall(r"<td\b(.*?)>(.*?)</td>", row, flags=re.S)
        if not cells:
            continue

        # rowspan taşıyan ilk hücre yeni bir gelenek açar
        if "rowspan" in cells[0][0]:
            raw = cells[0][1]
            name = _text(raw.split("<br>")[0])
            small = _text(raw.split("<br>")[1]) if "<br>" in raw else ""
            sigil, _, region = small.partition("·")
            current = {
                "id": slugify(name),
                "name": name,
                "sigil": sigil.strip(),
                "regionGroup": region.strip(),
                "inherited": name in INHERITED_TRADITIONS,
                "sourceRisk": "high" if name in HARD_TRADITIONS else "normal",
                "entryCount": 0,
            }
            traditions.append(current)
            cells = cells[1:]

        if current is None or len(cells) < 6:
            continue

        number = int(_text(cells[0][1]))
        creature_name = _text(cells[1][1])
        klass = _text(cells[2][1]).split("·")[0].strip()
        motif = _text(cells[3][1])
        kin = _text(cells[4][1])
        seed_note = _text(cells[5][1])

        creatures.append(
            {
                "number": number,
                "name": creature_name,
                "tradition": current["id"],
                "traditionName": current["name"],
                "class": klass,
                "motifSeed": motif,
                "kinFamily": None if kin in {"—", "-", ""} else kin,
                "seedNoteTr": seed_note,
            }
        )
        current["entryCount"] += 1

    return traditions, creatures


def assign_ids(creatures: list[dict]) -> None:
    """Benzersiz kimlik atar; çakışmayı gelenek adıyla ayırır."""
    counts: dict[str, int] = {}
    for c in creatures:
        counts[slugify(c["name"])] = counts.get(slugify(c["name"]), 0) + 1
    for c in creatures:
        base = slugify(c["name"])
        # Çakışan ad (ör. Hellenic "Lámia" ve Euskal "Lamia") gelenekle ayrılır.
        c["id"] = base if counts[base] == 1 else f"{base}-{c['tradition']}"


# =============================================================================
# 3. KAYIT ÜRETİMİ
# =============================================================================

def build_spec(traditions: list[dict], creatures: list[dict]) -> dict:
    assign_ids(creatures)

    records = []
    for c in creatures:
        records.append(
            {
                "id": c["id"],
                "number": c["number"],
                "name": c["name"],
                "pronunciation": "",          # Faz 2'de doldurulur
                "tradition": c["tradition"],
                "class": c["class"],
                "motif": [c["motifSeed"]],    # Faz 1'de Thompson'dan doğrulanır
                "motifVerified": False,
                "kinFamily": c["kinFamily"],
                "altNames": [],
                "region": "",                 # Faz 1 araştırma çıktısı
                "attested": "",               # Faz 1 araştırma çıktısı
                "sources": [],                # Faz 1: en az 2 bağımsız kaynak
                "crossRefs": [],              # Faz 2: 2–5 akraba çapraz referansı
                "plate": f"plate-{c['number']:03d}",
                "wordTarget": 700,
                "variantNote": "",
                "restrictionScreened": False, # yaşayan gelenek kapısı
                "seedNoteTr": c["seedNoteTr"],
                "researchFile": f"01_SOURCE/research/{c['id']}.md",
                "status": "draft",
            }
        )

    records.sort(key=lambda r: r["number"])

    return {
        "$schema": "./spec.schema.json",
        "meta": {
            "book": "Codex Bestiarium",
            "series": "Codex",
            "volume": 2,
            "language": "en",
            "documentLanguage": "tr",
            "author": "Emre Doğan",
            "imprint": "Vâliçe Press",
            "generatedBy": "08_BUILD/seed_import.py",
            "sourceOfTruth": (
                "CODEX_MYTHOLOGICA/03_CODEX_BESTIARIUM_MASTER_ROADMAP.html § 04"
            ),
            "warning": (
                "Bu bir kanon DEĞİLDİR. Her kayıt Faz 1'deki iki bağımsız kaynak "
                "kapısından geçmeden status 'verified' olamaz."
            ),
            "targets": {
                "creatures": 120,
                "traditions": 40,
                "pages": 404,
                "words": 92000,
                "wordsPerEntry": 700,
                "wordBandMin": 620,
                "wordBandMax": 790,
                "minSources": 2,
                "scopeFloor": 100,
            },
        },
        "classes": CLASSES,
        "kinFamilies": KIN_FAMILIES,
        "traditions": traditions,
        "creatures": records,
    }


# =============================================================================
# 4. GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", default=DEFAULT_SOURCE, help="master roadmap HTML")
    ap.add_argument("--out", default=SPEC_PATH)
    ap.add_argument(
        "--check",
        action="store_true",
        help="yazma; mevcut spec.json kaynakla uyumlu mu diye bak",
    )
    args = ap.parse_args()

    if not os.path.exists(args.source):
        print(f"HATA: kaynak yok: {args.source}", file=sys.stderr)
        return 2

    with open(args.source, encoding="utf-8") as fh:
        source_html = fh.read()

    traditions, creatures = parse_seed_table(source_html)
    spec = build_spec(traditions, creatures)

    print(f"gelenek : {len(traditions)}")
    print(f"yaratık : {len(creatures)}")

    if args.check:
        if not os.path.exists(args.out):
            print("HATA: spec.json yok.", file=sys.stderr)
            return 1
        with open(args.out, encoding="utf-8") as fh:
            existing = json.load(fh)
        # Yalnızca tohumdan türeyen alanları karşılaştır; araştırma çıktısı
        # (kaynak, telaffuz, çapraz referans) elbette farklı olacaktır.
        seed_fields = ("id", "number", "name", "tradition", "class", "kinFamily")
        a = [{k: r[k] for k in seed_fields} for r in spec["creatures"]]
        b = [{k: r.get(k) for k in seed_fields} for r in existing.get("creatures", [])]
        if a != b:
            print("BAŞARISIZ: spec.json tohum tablosuyla uyuşmuyor.", file=sys.stderr)
            for x, y in zip(a, b):
                if x != y:
                    print(f"  kaynak={x}\n  spec  ={y}", file=sys.stderr)
            return 1
        print("TAMAM: spec.json tohum tablosuyla uyumlu.")
        return 0

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"yazıldı : {os.path.relpath(args.out, ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
