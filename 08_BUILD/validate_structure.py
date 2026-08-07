#!/usr/bin/env python3
"""
CODEX BESTIARIUM — DEPO, BELGE VE VARLIK BÜTÜNLÜĞÜ DENETİMİ
================================================================================
CI'ın ana iş atı. Her push'ta çalışır ve kalite düşerse KIRMIZI yanar.

DENETLENEN
    · klasör yapısı           Bölüm 10'daki ağaç eksiksiz mi
    · dosya adlandırma        büyük/küçük harf, boşluk, Türkçe karakter kuralı
    · Markdown başlık hiyerarşisi   H1 tek, atlama yok (H2→H4 yasak)
    · iç bağlantılar          [x](y) hedefleri var mı
    · varlık referansları     görsel ve plaka yolları var mı
    · içindekiler             ROADMAP başlıkları ile faz listesi örtüşüyor mu
    · tekrar eden paragraf    belgeler arası birebir kopya
    · terminoloji             onaylı yazımlar (KDP, EPUB, Thompson, …)
    · tipografi ve noktalama  düz tırnak, üç nokta, çift boşluk
    · boşluk hijyeni          satır sonu boşluğu, sekme, dosya sonu satırı
    · Unicode                 NFC, görünmez karakter, BOM
    · JSON / YAML / HTML      ayrıştırılabilirlik
    · plaka referansları      spec.json ↔ prompts ↔ dosya sistemi
    · KDP uyumluluğu          sayfa/fiyat/anahtar kelime kısıtları

KULLANIM
    python3 08_BUILD/validate_structure.py
    python3 08_BUILD/validate_structure.py --verbose --strict
    python3 08_BUILD/validate_structure.py --json 06_REPORTS/structure.json
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import ROOT, Result, load_spec  # noqa: E402

# --- Bölüm 10'daki ağaç ---------------------------------------------------
REQUIRED_DIRS = [
    "00_CONTEXT", "01_SOURCE", "01_SOURCE/research", "02_MANUSCRIPT",
    "03_COVER", "03_COVER/artwork", "03_APLUS", "04_PRINT", "05_KINDLE",
    "06_REPORTS", "07_ASSETS", "07_ASSETS/fonts", "07_ASSETS/plates_raw",
    "07_ASSETS/plates", "08_BUILD", "09_ARCHIVE",
    ".github", ".github/workflows", ".github/ISSUE_TEMPLATE",
]

REQUIRED_FILES = [
    "README.md", "LICENSE", ".gitignore",
    "CHANGELOG.md", "BOOK_STATS.md", "ROADMAP_PROGRESS.md",
    "CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md",
    "BESTIARIUM_KDP_PUBLISHING_GUIDE.md",
    "BESTIARIUM_IMAGE_PROMPTS.html",
    "00_CONTEXT/PROJECT_CONTEXT.md",
    "00_CONTEXT/STYLE.md",
    "00_CONTEXT/STYLE_PLATES.md",
    "00_CONTEXT/BRIEF.md",
    "01_SOURCE/spec.json",
    "08_BUILD/bestiarium.py",
    "08_BUILD/validate_spec.py",
    "08_BUILD/requirements.txt",
    ".github/PULL_REQUEST_TEMPLATE.md",
]

# Bu klasörlerin içi denetlenmez (üretilmiş veya devralınmış)
SKIP_DIRS = {
    ".git", ".venv", "__pycache__", "node_modules", "09_ARCHIVE",
    "fonts", "plates_raw", "plates", "plates_print", "exports", "proofs",
    "fixtures",
}

TEXT_EXT = {".md", ".py", ".json", ".yml", ".yaml", ".html", ".txt", ".sh",
            ".css", ".js", ".toml", ".cfg"}

# --- terminoloji ----------------------------------------------------------
# (yanlış yazım → doğru yazım). Kitabın ve belgelerin tek sesle konuşması için.
TERMINOLOGY = {
    r"\bKdp\b": "KDP",
    r"\bkdp\b(?![-_/.])": "KDP",
    r"\bePub\b": "EPUB",
    r"\bepub\b(?![-_/.])": "EPUB",
    r"\bE-pub\b": "EPUB",
    r"\bPdf\b": "PDF",
    r"\bDocx\b": "DOCX",
    r"\bThomson\b": "Thompson",
    r"\bmotif index\b": "Motif-Index",
    r"\bBestiarum\b": "Bestiarium",
    r"\bBestiary(?= Codex)\b": "Bestiarium",
    r"\bMythologika\b": "Mythologica",
    r"\bValice\b": "Vâliçe",
    r"\bVarlice\b": "Vâliçe",
    r"\bhard cover\b": "hardcover",
    r"\blarge-print\b": "large print",
    r"\bpaper back\b": "paperback",
}

# --- tipografi ------------------------------------------------------------
TYPO_RULES = [
    (r"[ \t]+$", "satır sonunda boşluk"),
    (r"\t", "sekme karakteri (boşluk kullanın)"),
    (r"\.\.\.", "üç ayrı nokta (… kullanın)"),
    (r"(?<=[a-zA-ZğüşıöçĞÜŞİÖÇ]) {2,}(?=[a-zA-ZğüşıöçĞÜŞİÖÇ])", "çift boşluk"),
    (r"[a-zA-ZğüşıöçĞÜŞİÖÇ] ,", "virgülden önce boşluk"),
]

# DİKKAT — bu tablo görünmez karakterleri ARADIĞI için onları KAÇIŞ DİZİSİYLE
# yazmak zorundadır. Karakteri doğrudan yazmak betiğin kendi kaynağını kirletir
# ve tarama kendini yakalar. (İlk sürümde tam olarak bu oldu.)
INVISIBLE = {
    "\u200b": "ZERO WIDTH SPACE",
    "\u200c": "ZERO WIDTH NON-JOINER",
    "\u200d": "ZERO WIDTH JOINER",
    "\u200e": "LEFT-TO-RIGHT MARK",
    "\u200f": "RIGHT-TO-LEFT MARK",
    "\ufeff": "BYTE ORDER MARK",
    "\u00ad": "SOFT HYPHEN",
    "\u2028": "LINE SEPARATOR",
    "\u2029": "PARAGRAPH SEPARATOR",
}

MD_LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
MD_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
MD_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.M)
FENCE = re.compile(r"^```.*?^```", re.M | re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT)


def walk_files() -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            out.append(os.path.join(dirpath, f))
    return sorted(out)


def read(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def strip_fences(md: str) -> str:
    """Kod bloklarını boş satırlarla değiştirir — SATIR NUMARALARI KORUNUR.

    Blokları silmek satır numaralarını kaydırır ve hata raporu yanlış satırı
    gösterir. Bağlantı taraması satır içi kodu görmeli (bağlantı metni kod
    olabilir), bu yüzden burada yalnızca bloklar maskelenir.
    """
    return FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), md)


def strip_code(md: str) -> str:
    """Bloklar boş satıra, satır içi kod TEK BİR YER TUTUCUYA dönüşür.

    Satır içi kodu silmek, `a `kod` b` ifadesini `a  b` yapar ve tipografi
    taraması bunu "çift boşluk" sanır. Yer tutucu bu yanlış pozitifi kapatır.
    (İlk sürümde tam olarak bu oldu: üretilmiş belgelerde olmayan bir hata
    raporlandı.)
    """
    return INLINE_CODE.sub("x", strip_fences(md))


# =============================================================================
# KONTROLLER
# =============================================================================

def check_tree(r: Result) -> None:
    missing_dirs = [d for d in REQUIRED_DIRS if not os.path.isdir(os.path.join(ROOT, d))]
    r.add(not missing_dirs, "Bölüm 10 klasör ağacı eksiksiz", f"eksik: {missing_dirs}")

    missing_files = [f for f in REQUIRED_FILES if not os.path.isfile(os.path.join(ROOT, f))]
    r.add(not missing_files, "zorunlu dosyalar mevcut", f"eksik: {missing_files}")


def check_naming(files: list[str], r: Result) -> None:
    bad_space = [rel(f) for f in files if " " in os.path.basename(f)]
    r.add(not bad_space, "dosya adlarında boşluk yok", f"{bad_space[:10]}")

    bad_ascii = []
    for f in files:
        name = os.path.basename(f)
        if any(ord(ch) > 127 for ch in name):
            bad_ascii.append(rel(f))
    r.add(
        not bad_ascii,
        "dosya adları ASCII",
        f"{bad_ascii[:10]} — Türkçe karakterli dosya adı Windows/KDP "
        "aktarımında bozulur",
    )

    # Aynı klasörde yalnızca büyük/küçük harfle ayrılan iki dosya
    collisions = []
    by_dir: dict[str, list[str]] = collections.defaultdict(list)
    for f in files:
        by_dir[os.path.dirname(f)].append(os.path.basename(f))
    for d, names in by_dir.items():
        lowered = collections.Counter(n.lower() for n in names)
        for n, c in lowered.items():
            if c > 1:
                collisions.append(f"{rel(d)}/{n}")
    r.add(not collisions, "büyük/küçük harf çakışması yok", f"{collisions[:10]}")

    # Python betikleri snake_case
    bad_py = [
        rel(f) for f in files
        if f.endswith(".py")
        and not re.fullmatch(r"[a-z_][a-z0-9_]*\.py", os.path.basename(f))
    ]
    r.add(not bad_py, "Python betikleri snake_case", f"{bad_py[:10]}")


def check_encoding(files: list[str], r: Result) -> None:
    non_utf8, invisible, no_newline, crlf, not_nfc = [], [], [], [], []
    for f in files:
        if os.path.splitext(f)[1] not in TEXT_EXT:
            continue
        raw = open(f, "rb").read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            non_utf8.append(rel(f))
            continue
        if b"\r\n" in raw:
            crlf.append(rel(f))
        if raw and not raw.endswith(b"\n"):
            no_newline.append(rel(f))
        for ch, name in INVISIBLE.items():
            if ch in text:
                invisible.append(f"{rel(f)}: {name}")
        if text != unicodedata.normalize("NFC", text):
            not_nfc.append(rel(f))

    r.add(not non_utf8, "bütün metin dosyaları UTF-8", f"{non_utf8[:10]}")
    r.add(not crlf, "satır sonları LF (CRLF yok)", f"{crlf[:10]}")
    r.add(not no_newline, "dosyalar satır sonuyla bitiyor", f"{no_newline[:10]}")
    r.add(not invisible, "görünmez/tehlikeli karakter yok", f"{invisible[:10]}")
    r.add(not not_nfc, "metin dosyaları NFC normalize", f"{not_nfc[:10]}")


def check_markdown(files: list[str], r: Result) -> None:
    # GitHub şablonları (PR, issue) BELGE değil FORMDUR: H1 taşımazlar ve
    # taşımamalıdırlar — GitHub başlığı kendi arayüzünden verir.
    mds = [
        f for f in files
        if f.endswith(".md") and ".github" not in rel(f).split(os.sep)
    ]
    r.ok("taranan Markdown dosyası", f"{len(mds)} dosya (.github şablonları hariç)")

    no_h1, multi_h1, skips, empty_head = [], [], [], []
    for f in mds:
        body = strip_code(read(f))
        heads = [(len(h), t) for h, t in MD_HEADING.findall(body)]
        h1s = [t for lvl, t in heads if lvl == 1]
        if not h1s:
            no_h1.append(rel(f))
        elif len(h1s) > 1:
            multi_h1.append(f"{rel(f)} ({len(h1s)})")
        prev = 0
        for lvl, title in heads:
            if not title.strip():
                empty_head.append(rel(f))
            if prev and lvl > prev + 1:
                skips.append(f"{rel(f)}: H{prev} → H{lvl} “{title[:40]}”")
            prev = lvl

    r.add(not no_h1, "her Markdown dosyasında bir H1 var", f"{no_h1[:10]}")
    r.add(not multi_h1, "her Markdown dosyasında yalnızca bir H1", f"{multi_h1[:10]}")
    r.add(not skips, "başlık hiyerarşisinde atlama yok", f"{skips[:10]}")
    r.add(not empty_head, "boş başlık yok", f"{empty_head[:10]}")


def check_links(files: list[str], r: Result) -> None:
    broken, broken_img, empty_text = [], [], []
    for f in files:
        if not f.endswith(".md"):
            continue
        body = strip_fences(read(f))
        base = os.path.dirname(f)

        for text, target in MD_LINK.findall(body):
            if not text.strip():
                empty_text.append(f"{rel(f)} → {target}")
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = os.path.normpath(os.path.join(base, target.split("#")[0]))
            if not os.path.exists(path):
                broken.append(f"{rel(f)} → {target}")

        for alt, target in MD_IMAGE.findall(body):
            if re.match(r"^(https?:|data:)", target):
                continue
            path = os.path.normpath(os.path.join(base, target))
            if not os.path.exists(path):
                broken_img.append(f"{rel(f)} → {target}")

    r.add(not broken, "iç bağlantılar hedeflerine ulaşıyor", "\n         ".join(broken[:12]))
    r.add(not broken_img, "görsel referansları mevcut", "\n         ".join(broken_img[:12]))
    r.add(not empty_text, "bağlantı metni boş değil", f"{empty_text[:10]}")


def check_data_files(files: list[str], r: Result) -> None:
    bad_json, bad_yaml, bad_html = [], [], []
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext == ".json":
            try:
                json.loads(read(f))
            except json.JSONDecodeError as exc:
                bad_json.append(f"{rel(f)}: {exc}")
        elif ext in (".yml", ".yaml"):
            try:
                import yaml

                yaml.safe_load(read(f))
            except ImportError:
                pass
            except Exception as exc:  # noqa: BLE001
                bad_yaml.append(f"{rel(f)}: {exc}")
        elif ext == ".html":
            body = read(f)
            # Kaba ama etkili: açılan/kapanan blok etiketleri dengeli mi
            for tag in ("html", "head", "body", "table", "section", "div"):
                o = len(re.findall(rf"<{tag}\b", body, re.I))
                c = len(re.findall(rf"</{tag}>", body, re.I))
                if o != c:
                    bad_html.append(f"{rel(f)}: <{tag}> {o} açık / {c} kapalı")

    r.add(not bad_json, "bütün JSON dosyaları ayrıştırılabilir",
          "\n         ".join(bad_json[:8]))
    r.add(not bad_yaml, "bütün YAML dosyaları ayrıştırılabilir",
          "\n         ".join(bad_yaml[:8]))
    r.add(not bad_html, "HTML blok etiketleri dengeli",
          "\n         ".join(bad_html[:8]))


def check_typography(files: list[str], r: Result) -> None:
    hits: list[str] = []
    for f in files:
        if not f.endswith(".md"):
            continue
        body = read(f)
        clean = strip_code(body)
        for lineno, line in enumerate(clean.splitlines(), 1):
            # tablo hizalaması ve liste girintisi çift boşluk üretir; onları at
            if line.lstrip().startswith(("|", ">", "-", "*", "+")):
                continue
            # URL'ler kendi sözdizimlerini taşır: GitHub'ın "compare/a...b"
            # biçimindeki üç noktası bir tipografi hatası DEĞİLDİR.
            # SİLMEK yerine MASKELE: silmek satır sonunda boşluk bırakır ve
            # "satır sonunda boşluk" kuralı olmayan bir hatayı raporlar.
            probe = re.sub(r"https?://\S+", "URL", line)
            probe = re.sub(r"\]\([^)\s]+\)", "](URL)", probe)
            for pattern, label in TYPO_RULES:
                if re.search(pattern, probe):
                    hits.append(f"{rel(f)}:{lineno} — {label}")
    r.add(not hits, "tipografi ve boşluk kuralları temiz",
          "\n         ".join(hits[:15]) + (f"\n         toplam {len(hits)}" if hits else ""))


def check_terminology(files: list[str], r: Result) -> None:
    hits: list[str] = []
    for f in files:
        if os.path.splitext(f)[1] not in (".md", ".html"):
            continue
        clean = strip_code(read(f))
        # Amazon anahtar kelime kutuları BİREBİR yüklenir; okurun yazdığı
        # sorguyu taşırlar ve bizim terminolojimize uymak ZORUNDA DEĞİLDİR.
        # "comparative folklore motif index" kutusunu "Motif-Index" yapmak
        # arama eşleşmesini bozar. Blok taramadan muaftır.
        clean = re.sub(
            r"<!-- KEYWORDS -->.*?<!-- /KEYWORDS -->", "", clean, flags=re.S
        )
        for pattern, correct in TERMINOLOGY.items():
            for m in re.finditer(pattern, clean):
                if m.group(0) == correct:
                    continue
                hits.append(f"{rel(f)}: “{m.group(0)}” → “{correct}”")
    r.add(not hits, "terminoloji tutarlı", "\n         ".join(hits[:15]))


GENERATED_MARK = "OTOMATİK ÜRETİLDİ"


def check_duplicate_paragraphs(files: list[str], r: Result) -> None:
    seen: dict[str, list[str]] = collections.defaultdict(list)
    skipped = 0
    for f in files:
        if not f.endswith(".md"):
            continue
        body = read(f)
        # ÜRETİLMİŞ dosyalar atlanır. Ortak şablon bloğu ve aynı kaynağın
        # birden çok maddede künyelenmesi beklenen durumdur — kusur değil.
        # Bu denetim ELLE YAZILMIŞ proza içindeki kopyala-yapıştırı arar.
        if GENERATED_MARK in body:
            skipped += 1
            continue
        clean = strip_code(body)
        for para in clean.split("\n\n"):
            norm = " ".join(para.split()).strip().lower()
            norm = re.sub(r"[^\w\s]", "", norm)
            if len(norm.split()) < 25:
                continue
            if rel(f) not in seen[norm]:
                seen[norm].append(rel(f))
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    r.add(
        not dupes,
        f"belgeler arası birebir kopya paragraf yok ({skipped} üretilmiş dosya atlandı)",
        "\n         ".join(f"{v}: “{k[:70]}…”" for k, v in list(dupes.items())[:8]),
    )


def check_spec_integrity(r: Result) -> None:
    """spec.json ↔ araştırma dosyaları ↔ plakalar ↔ prompt kütüphanesi."""
    spec_path = os.path.join(ROOT, "01_SOURCE", "spec.json")
    if not os.path.exists(spec_path):
        r.fail("spec.json mevcut", "01_SOURCE/spec.json yok")
        return
    spec = load_spec()
    creatures = spec["creatures"]

    # Tekrar eden yaratık adı veya kimliği (kitabın en görünür kusuru)
    names = collections.Counter(c["name"].lower() for c in creatures)
    dupe = [n for n, k in names.items() if k > 1]
    if dupe:
        r.warn(
            "aynı ada sahip yaratık",
            f"{dupe} — kimlik ayrıştırıldı, dizinde çapraz gönderme zorunlu",
        )
    else:
        r.ok("yaratık adları benzersiz")

    # Aynı gelenek + aynı sınıf + aynı motif = muhtemel çift kayıt
    sig = collections.Counter(
        (c["tradition"], c["class"], tuple(sorted(c["motif"]))) for c in creatures
    )
    repeats = [f"{k[0]}/{k[1]}/{k[2]}" for k, v in sig.items() if v > 2]
    r.add(
        not repeats,
        "aynı gelenek+sınıf+motif üçlüsü 2'den fazla tekrar etmiyor",
        f"{repeats[:8]} — aynı mitolojinin aynı figürü iki kez anlatılıyor olabilir",
    )

    # Araştırma dosyaları — mevcut olanların adı kimliğe uymalı
    rdir = os.path.join(ROOT, "01_SOURCE", "research")
    ids = {c["id"] for c in creatures}
    if os.path.isdir(rdir):
        orphan = [
            f for f in os.listdir(rdir)
            if f.endswith(".md") and not f.startswith("_")
            and os.path.splitext(f)[0] not in ids
        ]
        r.add(not orphan, "araştırma dosyaları spec.json kimliklerine karşılık geliyor",
              f"{orphan[:10]}")

    # Plaka dosyaları
    pdir = os.path.join(ROOT, "07_ASSETS", "plates")
    plates = {c["plate"] for c in creatures}
    if os.path.isdir(pdir):
        orphan = [
            f for f in os.listdir(pdir)
            if f.lower().endswith(".png") and os.path.splitext(f)[0] not in plates
        ]
        r.add(not orphan, "plaka dosyaları spec.json plaka kimliklerine uyuyor",
              f"{orphan[:10]}")

    # Prompt kütüphanesi her yaratığı kapsıyor mu
    prompts = os.path.join(ROOT, "BESTIARIUM_IMAGE_PROMPTS.html")
    if os.path.exists(prompts):
        body = read(prompts)
        missing = [c["plate"] for c in creatures if c["plate"] not in body]
        r.add(
            not missing,
            "prompt kütüphanesi 120 plakanın tamamını içeriyor",
            f"eksik: {missing[:10]}",
        )


def check_roadmap_toc(r: Result) -> None:
    """Yol haritasının içindekiler listesi ile gerçek başlıkları örtüşüyor mu."""
    path = os.path.join(ROOT, "CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md")
    if not os.path.exists(path):
        r.fail("uygulama yol haritası mevcut", "dosya yok")
        return
    body = read(path)
    clean = strip_code(body)

    phases = re.findall(r"^##\s+FAZ\s+(\d+)\s*[—·-]\s*(.+)$", clean, re.M)
    r.add(
        4 <= len(phases) <= 6,
        "faz sayısı 4–6 bandında",
        f"bulunan: {len(phases)} — {[p[0] for p in phases]}",
    )

    nums = [int(n) for n, _ in phases]
    r.add(
        nums == list(range(1, len(nums) + 1)),
        "faz numaraları 1..N kesintisiz",
        f"{nums}",
    )

    # Her fazda zorunlu on beş başlık var mı
    required = [
        "Amaç", "Çıktılar", "Araştırma görevleri", "Yazım görevleri",
        "Editoryal görevler", "Dizgi görevleri", "Doğrulama görevleri",
        "Tamamlanma ölçütü", "Definition of Done", "Claude notları",
        "Kurucu notları", "Git etiketi", "Kilometre taşı",
    ]
    sections = re.split(r"^##\s+FAZ\s+", clean, flags=re.M)[1:]
    incomplete = []
    for i, sec in enumerate(sections, 1):
        missing = [h for h in required if h not in sec]
        if missing:
            incomplete.append(f"FAZ {i}: eksik {missing}")
    r.add(not incomplete, "her fazda zorunlu başlıklar var",
          "\n         ".join(incomplete[:6]))

    # İçindekiler bağlantıları gerçek başlıklara gidiyor mu.
    #
    # DİKKAT — Türkçe 'İ' küçültülünce 'i' + U+0307 (birleşen üst nokta) olur.
    # GitHub çıpayı üretirken bu birleşen işareti KORUR. Onu atan bir
    # slugifier, doğru bir bağlantıyı kırık sanır. Birleşen işaretler
    # (U+0300–U+036F) bu yüzden izinli kümededir.
    def anchor(title: str) -> str:
        low = unicodedata.normalize("NFC", title.lower())
        allowed = "[^" + chr(92) + "w" + chr(92) + "u0300-" + chr(92) + "u036f" + chr(92) + "- ]"
        kept = re.sub(allowed, "", low, flags=re.UNICODE)
        return kept.strip().replace(" ", "-")

    anchors = {anchor(t) for _, t in MD_HEADING.findall(clean)}
    dead = []
    for text, target in MD_LINK.findall(clean):
        if target.startswith("#"):
            slug = unicodedata.normalize("NFC", target[1:].lower())
            if slug and slug not in anchors:
                dead.append(f"“{text}” → {target}")
    if dead:
        r.warn("içindekiler çıpaları", f"{dead[:8]}")
    else:
        r.ok("içindekiler çıpaları başlıklara gidiyor")


def check_kdp(r: Result) -> None:
    """KDP'nin sert kısıtları — belgelerde beyan edilen değerler geçerli mi."""
    spec = load_spec()
    t = spec["meta"]["targets"]

    pages = t["pages"]
    r.add(24 <= pages <= 828, "ciltsiz sayfa sayısı KDP bandında (24–828)",
          f"{pages}")
    r.add(75 <= pages <= 550, "ciltli sayfa sayısı KDP bandında (75–550)",
          f"{pages}")

    # Yedi anahtar kelime kutusu ≤ 50 karakter
    kw_path = os.path.join(ROOT, "00_CONTEXT", "BRIEF.md")
    if os.path.exists(kw_path):
        body = read(kw_path)
        block = re.search(r"<!-- KEYWORDS -->(.*?)<!-- /KEYWORDS -->", body, re.S)
        if block:
            kws = [
                line.strip("-*0123456789. `")
                for line in block.group(1).splitlines()
                if line.strip().startswith(("-", "*")) or re.match(r"^\s*\d+\.", line)
            ]
            kws = [k for k in kws if k]
            r.add(len(kws) == 7, "yedi anahtar kelime kutusu dolu", f"bulunan: {len(kws)}")
            too_long = [k for k in kws if len(k) > 50]
            r.add(not too_long, "her anahtar kelime ≤50 karakter",
                  f"{[(k, len(k)) for k in too_long]}")

    # EPUB dosya boyutu bütçesi
    epub_dir = os.path.join(ROOT, "05_KINDLE")
    if os.path.isdir(epub_dir):
        epubs = [f for f in os.listdir(epub_dir) if f.endswith(".epub")]
        over = []
        for f in epubs:
            mb = os.path.getsize(os.path.join(epub_dir, f)) / 1e6
            if mb > 7.0:
                over.append(f"{f}: {mb:.1f} MB")
        r.add(not over, "EPUB dosya boyutu ≤7 MB", f"{over}")


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--strict", action="store_true", help="uyarılar da başarısız")
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    files = walk_files()
    r = Result("DEPO, BELGE VE VARLIK BÜTÜNLÜĞÜ (validate_structure)")

    check_tree(r)
    check_naming(files, r)
    check_encoding(files, r)
    check_markdown(files, r)
    check_links(files, r)
    check_data_files(files, r)
    check_typography(files, r)
    check_terminology(files, r)
    check_duplicate_paragraphs(files, r)
    check_spec_integrity(r)
    check_roadmap_toc(r)
    check_kdp(r)

    code = r.report(verbose=args.verbose)
    if args.json_out:
        r.to_json(os.path.join(ROOT, args.json_out))
    if args.strict and r.warnings:
        return 1
    return code


if __name__ == "__main__":
    raise SystemExit(main())
