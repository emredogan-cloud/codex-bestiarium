#!/usr/bin/env python3
"""
CODEX BESTIARIUM — YAZIM TEZGÂHI
================================================================================
Faz 3'ün yazım döngüsünü taşır. Yedi bölümlü madde bir JSON taslağı olarak
yazılır, ÖLÇÜLÜR, bant dışıysa düzeltilir, sonra `book.json`'a işlenir.

    NEDEN AYRI BİR BETİK
    ────────────────────
    `qa_length.py` bir KAPIDIR: kitabın tamamına bakar ve geçti/kaldı der.
    Yazarken gereken şey o değil, bir CETVELDİR: tek maddenin yedi bölümü
    bandın neresinde, kaç kelime eksik, kaç kelime fazla. Kapıyı cetvel
    olarak kullanmak, on madde yazıp sonra hepsini yeniden düzenlemek
    demektir — yol haritasının açıkça yasakladığı şey (Faz 3, Claude notları:
    "Her maddeyi bitirdiğinde qa_length çalıştır. Bant dışıysa HEMEN düzelt").

    Bantlar tek yerden gelir: `bestiarium.ENTRY_SECTIONS`. Bu betikte
    kitaba özgü tek bir sabit yoktur.

TASLAK BİÇİMİ
    {
      "kerberos": {
        "opening": "…", "where": "…", "looks": "…",
        "does": "…", "why": "…", "kin": "…", "sources": "…"
      }
    }

KULLANIM
    python3 08_BUILD/write_entry.py --measure  taslak.json
    python3 08_BUILD/write_entry.py --merge    taslak.json
    python3 08_BUILD/write_entry.py --status
    python3 08_BUILD/write_entry.py --opening class I  --merge acilis.json
    python3 08_BUILD/write_entry.py --matter           --merge matter.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    BOOK_PATH,
    BOOK_TITLE,
    ENTRY_SECTIONS,
    MATTER_KEYS,
    MATTER_PAGES,
    MATTER_SECTIONS,
    matter_group,
    SPEC_PATH,
    WORD_BAND,
    WORD_TARGET,
    load_spec,
)
from textutil import sentences, word_count  # noqa: E402

BANDS = {k: (lo, hi, label) for k, label, lo, hi in ENTRY_SECTIONS}
SECTION_KEYS = [k for k, _, _, _ in ENTRY_SECTIONS]

# CÜMLE UZUNLUĞU HEDEFİ — Faz 3'ün ilk partisinde ölçülerek bulundu.
#
# `qa_voice` KİTAP GENELİ ortalamayı 14–18 bandında ister ve ortalamayı BLOK
# ortalamalarının ortalaması olarak alır; kaynak notu bu hesaba girmez. Yani
# her maddeden altı blok sayılır: açılış + beş bölüm.
#
# Açılış kuralı gereği TEK cümledir ve 25–40 kelimedir, yani o blok tek
# başına ~27 ile hesaba girer ve ortalamayı yukarı çeker. Aritmetik:
#
#     (27 + 5 × X) / 6 = 16   →   X ≈ 13,8
#
# Bu yüzden açılış DIŞINDAKİ blokların cümle ortalaması ~14 olmalıdır. İlk
# partide bu iki kez ıskalandı: 16,1'de kitap 17,9'a çıkıp tavana yapıştı,
# 11,1'de 13,75'e düşüp tabanı deldi. Bandı burada tutmak, kapının kenarında
# yazmaktan iyidir — 45 maddede kenar payı biter.
# Blok başına SERT sınır, qa_voice'un uyarı bandından (11–22) pay bırakarak
# alınmıştır: bunun dışına çıkan blok CI'da uyarı üretir. Partinin genel
# ortalaması ayrıca raporlanır ve asıl nişan odur — 16,0, yani 14–18
# bandının ortası. Kenarda yazmak 45 maddede biten bir paydır.
SENT_TARGET = (11.5, 18.5)
SENT_BOOK_AIM = 16.0


# --- kitap dosyası --------------------------------------------------------

def load_book() -> dict:
    if os.path.exists(BOOK_PATH):
        with open(BOOK_PATH, encoding="utf-8") as fh:
            return json.load(fh)
    return {
        "meta": {
            "title": BOOK_TITLE,
            "language": "en",
            "note": "Manuscript — depo DIŞINDA yaşar (karar A1/D29).",
        },
        "frontMatter": {},
        "classOpenings": {},
        "kinOpenings": {},
        "entries": {},
        "backMatter": {},
    }


def save_book(book: dict) -> None:
    with open(BOOK_PATH, "w", encoding="utf-8") as fh:
        json.dump(book, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


# --- ölçüm ----------------------------------------------------------------

def sentence_avg(body: str) -> float:
    s = sentences(body)
    return (sum(word_count(x) for x in s) / len(s)) if s else 0.0


def measure(sections: dict) -> tuple[list[str], int, bool]:
    """(satırlar, toplam, temiz mi)"""
    lines: list[str] = []
    total = 0
    clean = True
    slo, shi = SENT_TARGET
    for key in SECTION_KEYS:
        lo, hi, label = BANDS[key]
        body = sections.get(key, "") or ""
        n = word_count(body)
        total += n
        if not body.strip():
            lines.append(f"    {key:<9} {'—':>5}          BOŞ · '{label}' yazılmamış")
            clean = False
            continue
        if n < lo:
            mark, note = "EKSİK", f"−{lo - n}"
            clean = False
        elif n > hi:
            mark, note = "FAZLA", f"+{n - hi}"
            clean = False
        else:
            mark, note = "ok", ""

        # Cümle uzunluğu: açılış kural gereği tek cümledir, muaftır.
        # Kaynak notu qa_voice'un ortalamasına girmez, o da muaftır.
        savg = sentence_avg(body)
        if key in ("opening", "sources"):
            snote = f"· cümle {savg:4.1f}"
        elif savg < slo:
            snote = f"· cümle {savg:4.1f} KISA (hedef {slo}–{shi})"
            clean = False
        elif savg > shi:
            snote = f"· cümle {savg:4.1f} UZUN (hedef {slo}–{shi})"
            clean = False
        else:
            snote = f"· cümle {savg:4.1f} ok"
        lines.append(f"    {key:<9} {n:>5}  ({lo}–{hi})  {mark:<5} {note:<5} {snote}")
    lo, hi = WORD_BAND
    if not lo <= total <= hi:
        clean = False
        delta = f"−{lo - total}" if total < lo else f"+{total - hi}"
        lines.append(f"    {'TOPLAM':<9} {total:>5}  ({lo}–{hi})  BANT DIŞI {delta}")
    else:
        lines.append(f"    {'TOPLAM':<9} {total:>5}  ({lo}–{hi})  ok   "
                     f"hedeften {total - WORD_TARGET:+d}")
    return lines, total, clean


def cmd_measure(path: str) -> int:
    with open(path, encoding="utf-8") as fh:
        draft = json.load(fh)
    spec = {c["id"]: c for c in load_spec()["creatures"]}

    bad = 0
    totals = []
    for cid, sections in draft.items():
        rec = spec.get(cid)
        head = f"{cid}" if rec else f"{cid}  ⛔ spec.json'da yok"
        if rec:
            head = f"{rec['name']}  ({cid} · sınıf {rec['class']} · {rec['tradition']})"
        print(f"\n  {head}")
        lines, total, clean = measure(sections)
        print("\n".join(lines))
        totals.append(total)
        if not clean or not rec:
            bad += 1

        unknown = [k for k in sections if k not in SECTION_KEYS]
        if unknown:
            print(f"    ⛔ tanınmayan bölüm: {unknown}")
            bad += 1

    if totals:
        mean = sum(totals) / len(totals)
        drift = abs(mean - WORD_TARGET) / WORD_TARGET
        print(f"\n  parti ortalaması: {mean:.0f}  (hedef {WORD_TARGET} · "
              f"sapma %{drift * 100:.1f})")

        # qa_voice'un göreceği değerin parti içindeki tahmini: kaynak notu
        # dışarıda, açılış içeride, blok ortalamalarının ortalaması.
        avgs = [
            sentence_avg(sections.get(k, ""))
            for sections in draft.values()
            for k in SECTION_KEYS
            if k != "sources" and (sections.get(k) or "").strip()
        ]
        if avgs:
            book_avg = sum(avgs) / len(avgs)
            flag = "ok" if 14.0 <= book_avg <= 18.0 else "BANT DIŞI"
            print(f"  parti cümle ortalaması: {book_avg:.1f}  "
                  f"(qa_voice bandı 14–18 · nişan {SENT_BOOK_AIM}) {flag}")
    print(f"\n  {len(draft) - bad}/{len(draft)} madde bantta\n")
    return 1 if bad else 0


# --- işleme ---------------------------------------------------------------

def cmd_merge(path: str) -> int:
    with open(path, encoding="utf-8") as fh:
        draft = json.load(fh)
    spec_doc = load_spec()
    spec = {c["id"]: c for c in spec_doc["creatures"]}

    for cid, sections in draft.items():
        if cid not in spec:
            print(f"HATA: spec.json'da yok: {cid}", file=sys.stderr)
            return 2
        _, _, clean = measure(sections)
        if not clean:
            print(f"HATA: {cid} bant dışı — önce --measure ile düzeltin",
                  file=sys.stderr)
            return 2

    book = load_book()
    for cid, sections in draft.items():
        rec = spec[cid]
        book["entries"][cid] = {
            "id": cid,
            "number": rec["number"],
            "name": rec["name"],
            "class": rec["class"],
            "tradition": rec["tradition"],
            "kinFamily": rec.get("kinFamily"),
            "plate": rec.get("plate", ""),
            "pronunciation": rec.get("pronunciation", ""),
            "sections": {k: sections.get(k, "").strip() for k in SECTION_KEYS},
        }
        rec["status"] = "written"
    save_book(book)

    with open(SPEC_PATH, "w", encoding="utf-8") as fh:
        json.dump(spec_doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(f"işlendi: {len(draft)} madde → {os.path.relpath(BOOK_PATH)} "
          f"· spec durumu 'written'")
    return cmd_status()


def cmd_merge_openings(kind: str, path: str) -> int:
    """Sınıf veya akraba açılışını book.json'a işler."""
    with open(path, encoding="utf-8") as fh:
        draft = json.load(fh)
    book = load_book()
    field = "classOpenings" if kind == "class" else "kinOpenings"
    for key, body in draft.items():
        book.setdefault(field, {})[key] = body.strip()
        print(f"  {field}[{key}]: {word_count(body)} kelime")
    save_book(book)
    return 0


def cmd_merge_matter(path: str) -> int:
    """Ön/arka madde bölümlerini book.json'a işler.

    Anahtar ve başlık `bestiarium.MATTER_SECTIONS`'tan gelir; taslak yalnızca
    GÖVDEYİ verir. Başlığı taslağa yazdırmak, tek doğruluk kaynağının yanına
    ikinci bir kopya koymaktır — bir gün ikisi ayrışır ve kimse fark etmez.

    Bu komut SAYFA ölçmez, kelime sayar. Sayfanın tek doğru ölçüsü gerçek
    dizgidir ve o `matter_page.py`'dedir; burada verilen sayı bir cetveldir.
    """
    with open(path, encoding="utf-8") as fh:
        draft = json.load(fh)

    unknown = [k for k in draft if k not in MATTER_KEYS]
    if unknown:
        print(f"HATA: tanınmayan bölüm: {', '.join(unknown)}")
        print(f"      geçerli anahtarlar: {', '.join(MATTER_KEYS)}")
        return 1

    titles = {k: t for _, k, t, _ in MATTER_SECTIONS}
    book = load_book()
    for key, body in draft.items():
        group = matter_group(key)
        book.setdefault(group, {})[key] = {
            "title": titles[key],
            "body": body.strip(),
        }
        n = word_count(body)
        savg = sentence_avg(body)
        print(f"  {group}[{key}]: {n} kelime · ort cümle {savg:.1f} "
              f"· slot {MATTER_PAGES[key]} sayfa")
    save_book(book)
    print("\n  SAYFA ÖLÇÜMÜ:  python3 08_BUILD/matter_page.py --measure")
    return 0


def cmd_status() -> int:
    spec_doc = load_spec()
    creatures = spec_doc["creatures"]
    book = load_book()
    written = set(book.get("entries", {}))

    print()
    for cls in ("I", "II", "III", "IV", "V", "VI"):
        items = [c for c in creatures if c["class"] == cls]
        if not items:
            continue
        done = sum(1 for c in items if c["id"] in written)
        bar = "█" * round(16 * done / len(items))
        print(f"  sınıf {cls:<4} {bar:<16} {done:>3}/{len(items)}")

    total_words = sum(
        word_count(e["sections"].get(k, ""))
        for e in book.get("entries", {}).values()
        for k in SECTION_KEYS
    )
    co = len(book.get("classOpenings", {}))
    ko = len(book.get("kinOpenings", {}))
    print(f"\n  yazılmış madde : {len(written)}/{len(creatures)}")
    print(f"  madde metni    : {total_words:,} kelime".replace(",", "."))
    print(f"  sınıf açılışı  : {co}/6   ·  akraba açılışı: {ko}/8")
    written_matter = sum(
        1 for _, key, _, _ in MATTER_SECTIONS
        if ((book.get(matter_group(key)) or {}).get(key) or {}).get("body")
    )
    print(f"  ön/arka madde  : {written_matter}/{len(MATTER_SECTIONS)}\n")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--measure", metavar="TASLAK")
    ap.add_argument("--merge", metavar="TASLAK")
    ap.add_argument("--opening", choices=["class", "kin"],
                    help="--merge'ü açılış metni olarak işler")
    ap.add_argument("--matter", action="store_true",
                    help="--merge'ü ön/arka madde olarak işler")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    if args.measure:
        return cmd_measure(args.measure)
    if args.merge:
        if args.opening:
            return cmd_merge_openings(args.opening, args.merge)
        if args.matter:
            return cmd_merge_matter(args.merge)
        return cmd_merge(args.merge)
    if args.status:
        return cmd_status()
    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
