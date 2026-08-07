#!/usr/bin/env python3
"""
CODEX BESTIARIUM — TEST KURGULARI ÜRETİCİSİ
================================================================================
İki sahte kitap üretir:

    good.json  — bütün kapılardan geçmesi gereken metin
    bad.json   — her kapıya BİLEREK bir kusur yerleştirilmiş metin

`selftest.py` bunları çalıştırır ve şunu kanıtlar: QA betikleri gerçekten
yakalıyor. Metin yokken yeşil kalan bir hat, kusur geldiğinde de yeşil
kalabilir — bu kurgular o riski kapatır.

Metinler İngilizcedir çünkü kitabın dili İngilizcedir. Edebî değerleri yoktur;
yalnızca ölçüm hedefidirler.
"""

from __future__ import annotations

import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "fixtures")

# --- iyi metin için gövde üreteci ----------------------------------------
# Bölüm bantları: opening 25-40 · where 70-110 · looks 110-160 · does 180-260
# why 90-140 · kin 50-80 · sources 30-50
#
# DİKKAT — burada bir ders var. İlk sürüm sabit adımlı bir sayaçla kelime
# seçiyordu; sözlük 31 kelimeydi ve adım 7'ydi. gcd(31,7)=1 olduğu için
# üreteç aynı diziyi tekrarlıyor, iki bölüm aynı 8-gram'ı taşıyordu.
# qa_echo bunu doğru şekilde yakaladı ve KURGU'yu düzelttirdi — betiği
# değil. Test hattının kendisi ilk kusurunu böyle buldu.
#
# Çözüm: geniş sözlük + blok başına ayrı tohumlanmış sözde-rastgele çekim.

FILLER = (
    "grey water stone bank reed mist rope hoof salt iron rain hollow ford "
    "bridle pasture cliff harbour lantern shepherd ferry timber ash pine "
    "furrow gravel shingle boulder eddy current shallow undertow silt "
    "marsh thicket heather bracken quarry cairn hedge byre thatch loom "
    "anvil bellows tallow rushlight kettle trough spindle churn scythe "
    "flint tinder ember hearth chimney rafter lintel threshold latch "
    "meadow orchard vineyard weir sluice millrace culvert causeway "
    "estuary headland skerry reef breaker spindrift kelp barnacle "
    "raven heron curlew plover gannet eider cormorant shearwater "
    "birch alder rowan hazel willow blackthorn juniper bramble "
    "winter thaw sleet hoarfrost drizzle squall gale doldrum "
    "midden furlong league fathom span cubit ell rod "
).split()


def body(n: int, seed: int, lead: str = "") -> str:
    """n kelimelik, bloğa özgü, cümlelere bölünmüş gövde."""
    rng = random.Random(seed)
    out = lead.split()
    while len(out) < n:
        # 14-18 kelimelik cümleler — Bölüm 08.1 ritim bandı
        target = rng.randint(14, 18)
        chunk = [rng.choice(FILLER) for _ in range(min(target, n - len(out)))]
        if not chunk:
            break
        chunk[0] = chunk[0].capitalize()
        chunk[-1] = chunk[-1] + "."
        out.extend(chunk)
    text = " ".join(out[:n])
    if not text.endswith("."):
        text = text.rstrip(".") + "."
    return text


def entry(cid: str, name: str, number: int, klass: str, tradition: str,
          seed: int) -> dict:
    return {
        "id": cid,
        "name": name,
        "number": number,
        "class": klass,
        "tradition": tradition,
        "sections": {
            "opening": body(32, seed, f"The {name} waits where the"),
            "where": body(90, seed + 11),
            "looks": body(135, seed + 23),
            "does": body(220, seed + 37),
            "why": body(115, seed + 53),
            "kin": body(65, seed + 71),
            "sources": body(40, seed + 89),
        },
    }


GOOD_ENTRIES = [
    ("kerberos", "Kérberos", 1, "I", "hellenic"),
    ("chimaira", "Chímaira", 2, "II", "hellenic"),
    ("lamia-hellenic", "Lámia", 3, "II", "hellenic"),
    ("ammit", "Ammit", 4, "II", "kemet"),
    ("apep", "Apep", 5, "IV", "kemet"),
    ("bennu", "Bennu", 6, "V", "kemet"),
    ("fenrir", "Fenrir", 7, "II", "nordr"),
    ("jormungandr", "Jörmungandr", 8, "IV", "nordr"),
    ("draugr", "Draugr", 9, "VI", "nordr"),
    ("each-uisce", "Each-uisce", 16, "IV", "eriu"),
]


def make_good() -> dict:
    entries = {}
    for i, (cid, name, num, klass, trad) in enumerate(GOOD_ENTRIES):
        entries[cid] = entry(cid, name, num, klass, trad, seed=i * 101 + 5)
    return {
        "meta": {"fixture": "good", "language": "en"},
        "frontMatter": {
            "introduction": {
                "title": "Forty Faces of One Fear",
                "body": body(160, 909, "Every tradition keeps a horse at the"),
            }
        },
        "classOpenings": {"I": body(120, 313), "II": body(120, 419)},
        "kinOpenings": {"A": body(140, 523)},
        "entries": entries,
        "backMatter": {
            "afterword": {
                "title": "Afterword",
                "body": body(150, 631, "What is left out of this volume"),
            }
        },
    }


def make_bad() -> dict:
    """Her kapıya tam bir kusur. Yorumlar hangi betiğin yakalaması
    gerektiğini söyler."""
    book = make_good()
    book["meta"]["fixture"] = "bad"
    e = book["entries"]

    # qa_length — bant altı (620'nin altı)
    e["kerberos"]["sections"]["does"] = body(40, 7)

    # qa_length — bant üstü (790'ın üstü)
    e["chimaira"]["sections"]["does"] = body(520, 9)

    # qa_length — boş bölüm
    e["ammit"]["sections"]["why"] = ""

    # qa_voice — yasak belirsizlik kalıbı
    e["apep"]["sections"]["where"] = (
        "It is said that the serpent rises each night beneath the western "
        "horizon. " + body(80, 13)
    )

    # qa_voice — oyun terminolojisi
    e["bennu"]["sections"]["does"] = (
        "The bird has no known weakness to fire and a high challenge rating. "
        + body(190, 17)
    )

    # qa_voice — ünlem + ölçülemez üstünlük
    e["fenrir"]["sections"]["why"] = (
        "This is the most terrifying wolf in the north! " + body(100, 19)
    )

    # qa_voice — sevimlileştirme + etiketsiz modern kurgu
    e["draugr"]["sections"]["why"] = (
        "Deep down it is a misunderstood creature, familiar to readers of "
        "Tolkien. " + body(100, 23)
    )

    # qa_echo — iki madde arasında birebir 8+ kelimelik öbek
    echo = ("the grey mare stands at the ford and waits for a rider to mount "
            "her. ")
    e["jormungandr"]["sections"]["looks"] = echo + body(120, 29)
    e["each-uisce"]["sections"]["looks"] = echo + body(120, 31)

    # qa_echo — tekrar eden açılış cümlesi
    same_open = "The creature waits where the water turns dark and slow."
    e["lamia-hellenic"]["sections"]["opening"] = same_open
    e["ammit"]["sections"]["opening"] = same_open

    # qa_diacritics — diakritik düşürülmüş ad
    e["kerberos"]["sections"]["kin"] = (
        "Compare Kerberos and Chimaira, whose names lose their marks here. "
        + body(50, 37)
    )

    # qa_diacritics — görünmez karakter + düz tırnak
    e["apep"]["sections"]["looks"] = (
        'A serpent "the colour of wet slate", its\u200b coil always dripping. '
        + body(110, 41)
    )

    return book


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    for name, data in (("good", make_good()), ("bad", make_bad())):
        path = os.path.join(OUT, f"{name}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"yazıldı: {os.path.relpath(path, HERE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
