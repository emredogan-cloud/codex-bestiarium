"""
CODEX BESTIARIUM — METİN YARDIMCILARI
================================================================================
Dört QA betiği (qa_length · qa_voice · qa_drift · qa_echo) ortak metin
erişimini buradan alır. Tek yerde tanımlı olması, "kelime" tanımının
betikten betiğe kaymasını engeller — kelime bandı sert bir kısıttır ve
iki farklı sayaç iki farklı gerçek üretir.

MANUSCRIPT ŞEMASI (01_SOURCE/book.json)
---------------------------------------
    {
      "meta":        { ... },
      "frontMatter": { "<key>": {"title": str, "body": str}, ... },
      "classOpenings": { "I": str, ... },
      "kinOpenings":   { "A": str, ... },
      "entries": {
        "<creature-id>": {
          "id": str, "name": str, "class": str, "tradition": str,
          "sections": {
            "opening": str, "where": str, "looks": str, "does": str,
            "why": str, "kin": str, "sources": str
          }
        }, ...
      },
      "backMatter":  { "<key>": {"title": str, "body": str}, ... }
    }

Faz 3 öncesinde bu dosya YOKTUR ve bu bir hata değildir. Bütün QA betikleri
"metin yok" durumunu 0 ile döner; CI yeşil kalır, kapı yükselince kırmızıya
döner.
"""

from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ENTRY_SECTIONS, load_book  # noqa: E402

SECTION_KEYS = [k for k, _, _, _ in ENTRY_SECTIONS]

# Kelime = harf/rakam içeren, boşlukla ayrılmış öbek. Kısa çizgili birleşikler
# (each-uisce) TEK kelimedir; tire ile bölünmüş satır sonu yoktur (JSON kaynağı).
WORD_RE = re.compile(r"[^\W_]+(?:['’-][^\W_]+)*", re.UNICODE)

# Cümle sonu: . ! ? ardından boşluk veya dize sonu. Kısaltmalar (p., c., ed.)
# yanlış bölmeyi tetikler; bilinenler korunur.
#
# PARAGRAF SONU DA BİR CÜMLE SONUDUR. Bu, noktalamayla bitmeyen bir satırın
# — ön/arka maddedeki ara başlıklar böyledir — kendinden sonraki cümleye
# YAPIŞMASINI önler. Yapışsaydı o cümle başlığın kelimeleriyle şişer ve
# `qa_voice`un cümle uzunluğu ölçümü sessizce bozulurdu.
#
# Bu bir kapı gevşetmesi DEĞİL, bir ölçüm düzeltmesidir ve ölçülerek
# doğrulandı: yazılmış 126 blokta cümle sayısı ve kitap ortalaması
# (16,5151) BİREBİR aynı kaldı, çünkü her paragraf zaten noktayla bitiyor.
# Değişen tek şey, noktalamasız satırın artık ayrı sayılması.
ABBREV = {"p", "pp", "c", "ca", "ed", "eds", "vol", "no", "fig", "cf", "trans"}
SENT_RE = re.compile(r"(?<=[.!?])\s+|\n\s*\n")


def words(text: str) -> list[str]:
    return WORD_RE.findall(text or "")


def word_count(text: str) -> int:
    return len(words(text))


def sentences(text: str) -> list[str]:
    raw = SENT_RE.split(text or "")
    out: list[str] = []
    for part in raw:
        part = part.strip()
        if not part:
            continue
        # önceki parça bir kısaltmayla bitiyorsa birleştir
        if out:
            tail = words(out[-1])
            if tail and tail[-1].lower() in ABBREV:
                out[-1] = out[-1] + " " + part
                continue
        out.append(part)
    return out


def normalize(text: str) -> str:
    """Karşılaştırma için: küçük harf, noktalama yok, tek boşluk."""
    return " ".join(w.lower() for w in words(text))


def entry_text(entry: dict) -> str:
    """Bir maddenin yedi bölümünü sırayla birleştirir."""
    sec = entry.get("sections", {})
    return "\n\n".join(sec.get(k, "") for k in SECTION_KEYS if sec.get(k))


def iter_entries(book: dict):
    """(id, kayıt) çiftleri — spec sırasını korumak için numaraya göre."""
    entries = book.get("entries", {}) or {}
    for key in sorted(entries, key=lambda k: entries[k].get("number", 10**6)):
        yield key, entries[key]


def all_prose_blocks(book: dict) -> list[tuple[str, str]]:
    """(etiket, metin) — madde bölümleri + ön/arka madde + açılışlar."""
    blocks: list[tuple[str, str]] = []
    for key, entry in iter_entries(book):
        sec = entry.get("sections", {})
        for skey in SECTION_KEYS:
            if sec.get(skey):
                blocks.append((f"{key}/{skey}", sec[skey]))
    for label, mapping in (
        ("front", book.get("frontMatter", {})),
        ("back", book.get("backMatter", {})),
    ):
        for key, item in (mapping or {}).items():
            body = item.get("body") if isinstance(item, dict) else item
            if body:
                blocks.append((f"{label}/{key}", body))
    for label, mapping in (
        ("classOpening", book.get("classOpenings", {})),
        ("kinOpening", book.get("kinOpenings", {})),
    ):
        for key, body in (mapping or {}).items():
            if body:
                blocks.append((f"{label}/{key}", body))
    return blocks


def require_book(path: str | None = None):
    """Metin varsa döner; yoksa (None, açıklama) döner. Hata DEĞİLDİR."""
    book = load_book(path)
    if book is None:
        return None, (
            "01_SOURCE/book.json yok — yazım Faz 3'te başlar. "
            "Bu bir hata değildir; kapı henüz açılmamıştır."
        )
    if not book.get("entries"):
        return None, "book.json var ama hiç madde içermiyor."
    return book, ""
