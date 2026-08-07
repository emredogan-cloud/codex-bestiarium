"""
CODEX BESTIARIUM — PROJE KAYIT DEFTERİ
================================================================================
Bütün Bestiarium betikleri sabitlerini buradan alır. `editions.py` bir ÜRÜN
kayıt defteridir (trim, marj, punto); bu dosya bir KİTAP kayıt defteridir
(sınıflar, aileler, kapılar, bantlar, yasak kalıplar).

Kural: hiçbir betikte kitaba özgü sabit yoktur. Değişecek her sayı burada.

    from bestiarium import SPEC, CLASS_IDS, WORD_BAND, load_spec
"""

from __future__ import annotations

import json
import os
import re
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- yollar ---------------------------------------------------------------
SOURCE_DIR = os.path.join(ROOT, "01_SOURCE")
RESEARCH_DIR = os.path.join(SOURCE_DIR, "research")
SPEC_PATH = os.path.join(SOURCE_DIR, "spec.json")
BOOK_PATH = os.path.join(SOURCE_DIR, "book.json")
BOOK_EDITED_PATH = os.path.join(SOURCE_DIR, "book-edited.json")
CONTEXT_DIR = os.path.join(ROOT, "00_CONTEXT")
REPORT_DIR = os.path.join(ROOT, "06_REPORTS")
ASSET_DIR = os.path.join(ROOT, "07_ASSETS")
PLATES_RAW_DIR = os.path.join(ASSET_DIR, "plates_raw")
PLATES_DIR = os.path.join(ASSET_DIR, "plates")
PLATES_PRINT_DIR = os.path.join(ASSET_DIR, "plates_print")
FONT_DIR = os.path.join(ASSET_DIR, "fonts")

BOOK_SLUG = "CODEX_BESTIARIUM"
BOOK_TITLE = "Codex Bestiarium"
BOOK_SUBTITLE = (
    "A World Bestiary: 112 Legendary Creatures from 40 Traditions — "
    "Beasts, Spirits, and Guardians of World Folklore"
)
SERIES = "Codex"
VOLUME = 2
AUTHOR = "Emre Doğan"
IMPRINT = "Vâliçe Press"

# --- kapsam kapıları (yol haritası Bölüm 04 · Bölüm 09 Faz 0) -------------
TARGET_CREATURES = 112   # Faz 1'de kilitlendi (120 aday → 8 düşürüldü)
TARGET_TRADITIONS = 40
SCOPE_FLOOR = 100          # bu sayının altına inilirse kitap yeniden planlanır
VERIFY_FLOOR = 112         # Faz 1 tamamlanma ölçütü
MIN_SOURCES = 2            # iki bağımsız kaynak kuralı
TARGET_PAGES = 380      # Faz 1 kilidi sonrası; dizgi Faz 6'da ölçecek
TARGET_WORDS = 78_400   # 112 × 700

# --- madde bantları (yol haritası Bölüm 05.2) -----------------------------
WORD_TARGET = 700
WORD_BAND = (620, 790)     # sert kısıt; qa_length.py denetler
CROSSREF_BAND = (2, 5)

# Yedi bölümlü madde yapısı. Sıra DEĞİŞMEZ.
ENTRY_SECTIONS = [
    ("opening",   "Açılış cümlesi",              25, 40),
    ("where",     "Nerede anlatılır",            70, 110),
    ("looks",     "Neye benzer",                110, 160),
    ("does",      "Ne yapar",                   180, 260),
    ("why",       "Neden korkulur veya sayılır",  90, 140),
    ("kin",       "Akrabaları",                  50, 80),
    ("sources",   "Kaynak notu",                 30, 50),
]

CLASS_IDS = ["I", "II", "III", "IV", "V", "VI"]
KIN_IDS = ["A", "B", "C", "D", "E", "F", "G", "H"]
STATUS_ORDER = ["draft", "verified", "written", "edited", "final"]

# Sınıf başına madde sayısı için kabul bandı. Yol haritası Bölüm 03.1 hedef
# verir; tohum tablosu ondan sapar (Faz 2 uzlaştırır). Kapı: hiçbir sınıf
# 8'in altına veya 32'nin üstüne çıkamaz.
CLASS_COUNT_FLOOR = 8
CLASS_COUNT_CEIL = 32

# --- Thompson motif kodu --------------------------------------------------
# Motif-Index ana bölümleri. I, O, Y kullanılmaz.
THOMPSON_SECTIONS = set("ABCDEFGHJKLMNPQRSTUVWXZ")
MOTIF_RE = re.compile(r"^[A-Z]\d+(?:\.\d+)*(?:\.\d+)?$")


def motif_valid(code: str) -> bool:
    """Tek bir Thompson kodunun biçimsel geçerliliği (varlığı değil)."""
    code = code.strip()
    if not MOTIF_RE.match(code):
        return False
    return code[0] in THOMPSON_SECTIONS


# --- yaşayan gelenek kapısı (yol haritası Bölüm 08.3) ---------------------
# Bu geleneklerin maddeleri için yalnızca YAYIMLANMIŞ ve KISITLANMAMIŞ
# malzeme kullanılır; kısıtlı olduğu bilinen anlatı anlatılmaz, kısıtlı
# olduğu söylenir.
LIVING_TRADITIONS = {
    "inuit", "ainu", "sapmi", "anishinaabe", "ma-ohi", "maohi",
    "melanesia", "nguni", "tupi-guarani", "yoruba-ashanti",
    "tawantinsuyu", "ityop-ya", "bod", "mongol",
}

# --- ses kuralları (yol haritası Bölüm 08.1) ------------------------------
# qa_voice.py bunları arar. Hepsi İNGİLİZCE metinde aranır — kitabın dili
# İngilizcedir; bu belgeler Türkçedir.
FORBIDDEN_PHRASES = [
    "it is said", "it is said that", "legend has it", "legend says",
    "according to legend", "some say", "it was believed", "some believe",
    "as the story goes", "folklore tells us", "many believe",
    "it is thought", "rumour has it", "rumor has it", "reputedly",
    "supposedly", "allegedly",
]

# Oyun terminolojisi — bu kitapta yasak (Bölüm 08.1)
FORBIDDEN_GAME_TERMS = [
    "hit points", "stat block", "saving throw", "damage type",
    "resistance to", "weakness to", "challenge rating", "ability score",
    "level up", "loot", "spawn", "boss fight", "player character",
]

# Ölçülemez üstünlük iddiaları
FORBIDDEN_SUPERLATIVES = [
    "the most terrifying", "the most famous", "the scariest",
    "the most feared", "the deadliest", "the most powerful",
    "the best known", "the most horrifying",
]

# Sevimlileştirme
FORBIDDEN_SOFTENERS = [
    "actually quite", "just a lonely", "misunderstood creature",
    "not really evil", "deep down", "at heart it is",
]

# Modern kurgu kaynak sayılmaz (Bölüm 08.3). Geçiyorsa "modern" etiketiyle
# tek cümlede olmalı; qa_voice.py bağlam kontrolü yapar.
MODERN_FICTION_MARKERS = [
    "tolkien", "dungeons & dragons", "dungeons and dragons", "d&d",
    "pokemon", "pokémon", "final fantasy", "the witcher", "world of warcraft",
    "harry potter", "marvel", "netflix",
]

# Ünlem işareti tüm kitapta sıfır olmalı.
MAX_EXCLAMATIONS = 0

# --- plaka şartnamesi (yol haritası Bölüm 07.3) ---------------------------
PLATE_SPEC = {
    "aspect": 1.25,               # 1:1,25 dikey
    "aspect_tol": 0.02,
    "line_weight_pt": 1.4,        # ana çizgi kalınlığı
    "line_weight_tol": 0.15,      # ±%15
    "hatch_primary_deg": 45.0,
    "hatch_secondary_deg": 135.0,
    "hatch_angle_tol_deg": 5.0,
    "hatch_lines_per_cm": (22, 28),
    "ink_darkest": 0.92,          # en koyu %92 siyah
    "ink_lightest": 0.08,         # en açık %8
    "ink_tol": 0.05,
    "coverage": (0.62, 0.78),     # yaratık tuvalin %62–78'i
    "background": "empty",        # zemin boş — sahne yok
    "scale_figure": True,         # her plakada insan siluetiyle ölçek
    "dpi": 300,
    "target_width_px": 1800,
    "target_height_px": 2250,
}

# Kindle dosya boyutu bütçesi (Bölüm 06)
EPUB_BUDGET_MB = 7.0
PLATE_EPUB_BUDGET_KB = 60


# --- yükleyiciler ---------------------------------------------------------

def load_spec(path: str = SPEC_PATH) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_book(path: str | None = None) -> dict | None:
    """Yazılmış metin. Faz 3 öncesinde yoktur ve bu bir hata değildir."""
    for candidate in ([path] if path else [BOOK_EDITED_PATH, BOOK_PATH]):
        if candidate and os.path.exists(candidate):
            with open(candidate, encoding="utf-8") as fh:
                return json.load(fh)
    return None


def slugify(name: str) -> str:
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
    return re.sub(r"[^a-z0-9]+", "-", ascii_only).strip("-")


# --- rapor yardımcıları ---------------------------------------------------

class Result:
    """Basit kontrol toplayıcı. Her betik aynı çıktı biçimini kullanır."""

    def __init__(self, title: str) -> None:
        self.title = title
        self.checks: list[dict] = []

    def add(self, ok: bool, name: str, detail: str = "", warn: bool = False) -> bool:
        self.checks.append(
            {"ok": bool(ok), "name": name, "detail": detail, "warn": warn}
        )
        return bool(ok)

    def ok(self, name: str, detail: str = "") -> None:
        self.add(True, name, detail)

    def fail(self, name: str, detail: str = "") -> None:
        self.add(False, name, detail)

    def warn(self, name: str, detail: str = "") -> None:
        self.add(False, name, detail, warn=True)

    @property
    def failures(self) -> list[dict]:
        return [c for c in self.checks if not c["ok"] and not c["warn"]]

    @property
    def warnings(self) -> list[dict]:
        return [c for c in self.checks if not c["ok"] and c["warn"]]

    @property
    def passed(self) -> list[dict]:
        return [c for c in self.checks if c["ok"]]

    def report(self, verbose: bool = False) -> int:
        print(f"\n{'=' * 78}\n{self.title}\n{'=' * 78}")
        for c in self.checks:
            if c["ok"] and not verbose:
                continue
            mark = "  ok " if c["ok"] else ("WARN" if c["warn"] else "FAIL")
            line = f"[{mark}] {c['name']}"
            if c["detail"]:
                line += f"\n         {c['detail']}"
            print(line)
        n = len(self.checks)
        print(
            f"\n{len(self.passed)}/{n} geçti · "
            f"{len(self.failures)} başarısız · {len(self.warnings)} uyarı"
        )
        return 1 if self.failures else 0

    def to_json(self, path: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(
                {
                    "title": self.title,
                    "passed": len(self.passed),
                    "failed": len(self.failures),
                    "warnings": len(self.warnings),
                    "checks": self.checks,
                },
                fh,
                ensure_ascii=False,
                indent=2,
            )
            fh.write("\n")
