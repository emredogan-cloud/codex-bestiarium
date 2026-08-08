#!/usr/bin/env python3
"""
CODEX BESTIARIUM — BASKIYA HAZIR İÇ BLOK
================================================================================
Kitabın TAMAMINI dizer ve gerçek sayfa haritasını yayar.

    NEDEN YENİ BİR BETİK
    ────────────────────
    `make_pdf.py` Cilt 1'den devralındı ve CODEX MYTHOLOGICA üretir: on dokuz
    uygarlığın yetmiş altı miti, anlatı bölümleriyle. Bestiarium'un yapısı
    başkadır — altı sınıf, yedi bölümlü madde, her maddenin üstünde bir
    plaka, sekiz karşılaştırma açılışı, dört dizin. Devralınan betiği
    "uyarlamak" iki kitabın yapısını tek dosyada tutmak olurdu ve ikisi de
    bozulurdu.

    DEVRALINAN ŞEY YERLEŞİM MOTORUDUR, KİTAP DEĞİL. `make_pdf`ten alınanlar:
    `Layout` (sürüm geometrisi ve stiller), `PLAN`/`Mark` (dizgi sırasında
    sayfa kaydı), `_chrome` (üst bilgi ve folyo), `EmbeddedOnlyCanvas` (KDP
    gömülü font kuralı). Bunlar iki kitapta da aynıdır ve tekrar yazmak
    aptallık olurdu.

İKİ GEÇİŞ — VE NEDEN İKİ GEÇİŞ ŞART
    Dizin sayfa numaraları ve akraba satırındaki çapraz referans sayfaları
    ancak kitap dizildikten SONRA bilinir. Ama dizinin kendisi de sayfa
    tutar. Klasik özyineleme.

    Çözüm sıra ile: dizinler ve kaynaklar kitabın SONUNDADIR, yani onların
    uzunluğu kendinden ÖNCEKİ hiçbir sayfayı kaydırmaz.
      1. geçiş  → dizin gövdesi olmadan diz, madde sayfalarını kaydet
      dizinler  → `make_index --pagemap` gerçek numaralarla üretir
      2. geçiş  → dizinlerle birlikte diz
      DOĞRULAMA → iki geçişin madde sayfaları BİREBİR aynı olmalı
    Son satır bir sınamadır: aynı değilse varsayım çökmüştür ve betik
    kırmızı yanar. Sessizce yanlış numara basmaz.

    Çapraz referans sayfaları için 1. geçişte `(p. 000)` yer tutucusu
    konur; 2. geçişte gerçek numara aynı genişlikte yerine geçer. Her madde
    üç sayfaya kuruluyor ve ölçülen içeriği ~2,13 sayfa — yani sayfa başına
    ~0,87 sayfalık pay var. Birkaç karakterlik fark bir maddeyi dördüncü
    sayfaya taşıyamaz; doğrulama adımı bunu zaten kanıtlıyor.

ÇIKTILAR
    04_PRINT/<SÜRÜM>/CODEX_BESTIARIUM_INTERIOR_<SÜRÜM>.pdf
    04_PRINT/<SÜRÜM>/pagemap.json          ← depoda kalır, proza içermez

ÇIKIŞ KODLARI
    0  üretildi        1  üretim kusuru        2  bağımlılık veya metin yok

KULLANIM
    python3 08_BUILD/make_book.py                       # ciltsiz
    python3 08_BUILD/make_book.py --edition hardcover
    python3 08_BUILD/make_book.py --all
    python3 08_BUILD/make_book.py --no-plates           # plakasız prova
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import front_matter as FM  # noqa: E402
from bestiarium import (  # noqa: E402
    AUTHOR,
    region_en,
    BOOK_SUBTITLE,
    BOOK_TITLE,
    CLASS_IDS,
    ENTRY_SECTIONS,
    IMPRINT,
    KIN_IDS,
    MATTER_SECTIONS,
    ROOT,
    SERIES,
    VOLUME,
    load_book,
    load_spec,
    matter_group,
)

PRINT_DIR = os.path.join(ROOT, "04_PRINT")
PLATE_INT_DIR = os.path.join(ROOT, "07_ASSETS", "plates_interior")
PLATE_PRINT_DIR = os.path.join(ROOT, "07_ASSETS", "plates_print")
PLATE_DIR = os.path.join(ROOT, "07_ASSETS", "plates")
INDEX_PATH = os.path.join(ROOT, "01_SOURCE", "indexes.json")

# Sürüm kimlikleri `editions.py`den gelir; burada UYDURULMAZ. İlk yazımda
# "large-print" yazılmıştı ve kayıt defterinde "largeprint" geçiyor —
# `--all` sessizce iki sürüm üretip üçüncüde düştü.
EDITION_DIRS = {
    "paperback": "PAPERBACK",
    "hardcover": "HARDCOVER",
    "largeprint": "LARGEPRINT",
}

# Çapraz referans yer tutucusu. Genişliği gerçek numarayla aynı olsun diye
# üç haneli: kitap 436 sayfa, yani numaraların çoğu üç hanelidir.
XREF_PLACEHOLDER = "000"


def _require():
    missing = []
    for mod, why in (("reportlab", "dizgi"), ("pypdf", "sayfa sayımı")):
        try:
            __import__(mod)
        except ImportError:
            missing.append(f"{mod} ({why})")
    if missing:
        print("ATLANDI: iç blok dizgisi şunları gerektirir: "
              + ", ".join(missing))
        print("         ./08_BUILD/bootstrap.sh çalıştırın.")
        raise SystemExit(2)


# =============================================================================
# PLAKA
# =============================================================================

def plate_path(plate_id: str) -> str | None:
    """İç blok plakası (450 DPI gri ton PNG); yoksa normalize master.

    SIRA ÖLÇÜLEREK SEÇİLDİ. Önce TIFF deneniyordu ve kitap 220 MB çıkıyordu
    — plaka başına ~2 MB. Aynı görüntü PNG olarak gömüldüğünde plaka başına
    ~230 KB, kitap ~35 MB. Sebep reportlab'in TIFF'i ham RGB'ye açıp öyle
    gömmesi; PNG kendi sıkıştırmasıyla geçiyor.

    Kalite kaybı YOKTUR ve bu ölçüldü: iki dosya da 1800×2250 gri ton, aynı
    normalize çıktının iki kabı. Kutuda 600 DPI — KDP'nin 300 tabanının iki
    katı. Baskı gri ton kalır: plakaların %26'sı ara tondur ve iki tona
    indirmek o bilgiyi yok ederdi (iki ton kararı D49 Kindle içindi).
    """
    for d, ext in ((PLATE_INT_DIR, ".png"), (PLATE_DIR, ".png"),
                   (PLATE_PRINT_DIR, ".tif")):
        p = os.path.join(d, plate_id + ext)
        if os.path.exists(p):
            return p
    return None


def plate_flowable(rec, w, h, use_plates: bool):
    """Gerçek plaka varsa görüntü, yoksa ölçülü çerçeve.

    Çerçeve bir yedek değil bir SİNYALDİR: plakasız üretilen bir prova,
    plakalı olduğunu iddia etmemelidir.
    """
    from reportlab.platypus import Image as RLImage
    from reportlab.platypus.flowables import Flowable

    path = plate_path(rec.get("plate", "")) if use_plates else None
    if path:
        img = RLImage(path, width=w, height=h)
        img.hAlign = "CENTER"
        return img

    class PlateFrame(Flowable):
        def __init__(self):
            super().__init__()
            self.width, self.height = w, h

        def draw(self):
            c = self.canv
            c.saveState()
            c.setStrokeColor("#BBBBBB")
            c.setLineWidth(0.4)
            c.setDash(3, 3)
            c.rect(0, 0, self.width, self.height)
            c.setDash()
            c.setFillColor("#999999")
            c.setFont("Cinzel", 7.5)
            c.drawCentredString(self.width / 2, self.height / 2,
                                rec.get("plate", "").upper())
            c.restoreState()

    return PlateFrame()


# =============================================================================
# AKIŞLAR
# =============================================================================

def book_flow(book, spec, L, S, MP, pages: dict, use_plates: bool,
              indexes: dict | None):
    """Kitabın tamamının akış nesneleri.

    `pages` boşsa 1. geçiştir: çapraz referanslar yer tutucu alır ve dizin
    gövdesi basılmaz. Doluysa 2. geçiştir.
    """
    from reportlab.lib.units import inch as IN
    from reportlab.platypus import (KeepTogether, PageBreak, Paragraph,
                                    Spacer, Table, TableStyle)

    import entry_page as EP

    F = []
    A = F.append
    k = L.ed.display_scale
    text_w = L.ed.text_w * 72.0

    trads = {t["id"]: t for t in spec["traditions"]}
    classes = {c["id"]: c for c in spec["classes"]}
    kinfam = {f["id"]: f for f in spec["kinFamilies"]}
    by_id = {c["id"]: c for c in spec["creatures"]}
    creatures = sorted(spec["creatures"], key=lambda c: c.get("number", 0))

    def page_ref(cid: str) -> str:
        if not pages:
            return XREF_PLACEHOLDER
        return str(pages.get(cid, XREF_PLACEHOLDER))

    # ── yarım başlık ────────────────────────────────────────────────────
    A(Spacer(1, 2.6 * IN))
    A(Paragraph(EP.tracked(FM.HALF_TITLE, 0.10, 17 * k), S["fmhalf"]))
    A(PageBreak())
    A(PageBreak())

    # ── başlık sayfası ──────────────────────────────────────────────────
    tp = FM.TITLE_PAGE
    A(Spacer(1, 1.55 * IN))
    A(Paragraph(EP.tracked(tp["title"], 0.09, 27 * k), S["btitle"]))
    A(Spacer(1, 16 * k))
    A(Paragraph(tp["subtitle"], S["bsub"]))
    A(Paragraph(tp["line"], S["bline"]))
    A(Spacer(1, 1.35 * IN))
    A(Paragraph(EP.tracked(tp["author"].upper(), 0.22, 12.5 * k), S["author"]))
    A(Spacer(1, 1.5 * IN))
    A(Paragraph(tp["series"], S["bline"]))
    A(Spacer(1, 8 * k))
    A(Paragraph(EP.tracked(tp["imprint"].upper(), 0.18, 9 * k), S["imprint"]))
    A(PageBreak())

    # ── künye ───────────────────────────────────────────────────────────
    A(Spacer(1, 1.7 * IN))
    for line in FM.COPYRIGHT:
        A(Paragraph(MP.esc(line), S["copy"]))
    A(PageBreak())

    # ── ithaf ───────────────────────────────────────────────────────────
    A(Spacer(1, 2.9 * IN))
    A(Paragraph(MP.esc(FM.DEDICATION), S["ded"]))
    A(PageBreak())
    A(PageBreak())

    # ── içindekiler ─────────────────────────────────────────────────────
    A(MP.Mark("front", head=FM.CONTENTS_TITLE, civ=BOOK_TITLE, no_head=True))
    A(Paragraph(EP.tracked(FM.CONTENTS_TITLE.upper(), 0.07, 17 * k),
                S["fmtitle"]))
    rows = []
    for _group, key, title, _p in MATTER_SECTIONS:
        if key in ("about-author", "series", "review-call", "colophon"):
            continue
        rows.append((title, page_ref("matter/" + key)))
    for cid in CLASS_IDS:
        kl = classes[cid]
        n = sum(1 for c in creatures if c["class"] == cid)
        rows.append((f"{cid} · {kl['en']}  ({n})", page_ref("class/" + cid)))
    for key in ("traditions", "motifs", "kin", "pronunciation"):
        rows.append((FM.INDEX_TITLES[key], page_ref("index/" + key)))
    rows.append((FM.SOURCES_TITLE, page_ref("sources")))
    for label, pg in rows:
        A(Paragraph(f"{MP.esc(label)}<font color='#FFFFFF'>.</font>"
                    f"&nbsp;&nbsp;<font color='#777777'>{pg}</font>",
                    S["toc"]))
    A(PageBreak())

    # ── kırk gelenek haritası (çift sayfa) ──────────────────────────────
    A(MP.Mark("front", head=FM.MAP_TITLE, civ=BOOK_TITLE, no_head=True))
    A(Paragraph(EP.tracked(FM.MAP_TITLE.upper(), 0.07, 17 * k), S["fmtitle"]))
    A(Paragraph(MP.esc(FM.MAP_NOTE), S["fmnote"]))
    A(Spacer(1, 10 * k))
    ordered = sorted(spec["traditions"],
                     key=lambda t: (region_en(t["regionGroup"]), t["name"]))
    data, region = [], None
    for t in ordered:
        if t.get("regionGroup") != region:
            region = t.get("regionGroup")
            data.append([Paragraph(f"<b>{MP.esc(region_en(region))}</b>",
                                   S["maphead"]),
                         Paragraph("", S["mapnum"])])
        n = sum(1 for c in creatures if c["tradition"] == t["id"])
        data.append([Paragraph(MP.esc(t["name"]), S["maprow"]),
                     Paragraph(str(n), S["mapnum"])])
    tbl = Table(data, colWidths=[text_w * 0.80, text_w * 0.20])
    tbl.setStyle(TableStyle([
        # FONT AÇIKÇA VERİLİR. reportlab'in hücre varsayılanı Helvetica'dır
        # ve GÖMÜLMEZ; boş bir hücre bile onu PDF'in font kaynağına sokar.
        # KDP gömülü olmayan font kabul etmez. Tek boş hücre yüzünden 435
        # sayfanın tamamında Helvetica göründü — `pdffonts` yakaladı.
        ("FONTNAME", (0, 0), (-1, -1), "Gara"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1.2 * k),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2 * k),
    ]))
    A(tbl)
    A(PageBreak())
    A(MP.Mark("front_end"))

    # ── giriş ve "bu kitap nasıl okunur" ────────────────────────────────
    import matter_page as MPG
    first_body = True
    for group, key, title, _p in MATTER_SECTIONS:
        if group != "front":
            continue
        item = (book.get(matter_group(key)) or {}).get(key) or {}
        if not item.get("body"):
            continue
        if first_body:
            A(MP.Mark("body_start"))
            first_body = False
        A(MP.Mark("matter", head=title, civ=BOOK_TITLE, no_head=True,
                  cid="matter/" + key))
        A(MP.Mark("pin", head=None, civ=None))
        A(_PinMatter("matter/" + key, MP))
        for fl in MPG.matter_flow(title, item["body"], L, S):
            A(fl)
        A(PageBreak())

    # ── altı sınıf ──────────────────────────────────────────────────────
    kin_home = {}
    for fid in KIN_IDS:
        members = [c for c in creatures if c.get("kinFamily") == fid]
        if not members:
            continue
        counts = {}
        for m in members:
            counts[m["class"]] = counts.get(m["class"], 0) + 1
        kin_home.setdefault(max(counts, key=counts.get), []).append(fid)

    for cid in CLASS_IDS:
        kl = classes[cid]
        members = [c for c in creatures if c["class"] == cid]
        head = f"{cid} · {kl['en']}"

        A(MP.Mark("class", head=head, civ=kl["en"], no_head=True,
                  cid="class/" + cid))
        A(_PinMatter("class/" + cid, MP))
        A(Spacer(1, 1.0 * IN))
        A(Paragraph(EP.tracked(f"CLASS {cid}", 0.22, 10 * k), S["classnum"]))
        A(Paragraph(EP.tracked(kl["en"].upper(), 0.08, 23 * k), S["classname"]))
        A(Paragraph(f"{len(members)} creatures", S["classmeta"]))
        A(PageBreak())
        body = (book.get("classOpenings") or {}).get(cid, "")
        if body:
            for i, para in enumerate(
                    [p.strip() for p in body.split("\n\n") if p.strip()]):
                A(Paragraph(MP.esc(para), S["body1"] if i == 0 else S["body"]))
        A(PageBreak())

        for fid in kin_home.get(cid, []):
            fam = kinfam[fid]
            fmem = [c for c in creatures if c.get("kinFamily") == fid]
            A(MP.Mark("kin", head=fam["en"], civ=kl["en"], no_head=True,
                      cid="kin/" + fid))
            A(_PinMatter("kin/" + fid, MP))
            A(Spacer(1, 0.75 * IN))
            A(Paragraph(EP.tracked("KIN IMAGE", 0.22, 9 * k), S["classnum"]))
            A(Paragraph(EP.tracked(fam["en"].upper(), 0.07, 19 * k),
                        S["classname"]))
            A(Paragraph(f"{len(fmem)} creatures · "
                        f"{len({m['tradition'] for m in fmem})} traditions · "
                        f"{fam.get('motif','')}", S["classmeta"]))
            A(Spacer(1, 14 * k))
            names = " · ".join(
                f"{m['name']} <font color='#777777'>{page_ref(m['id'])}</font>"
                for m in fmem)
            A(Paragraph(names, S["kinlist"]))
            A(PageBreak())
            kbody = (book.get("kinOpenings") or {}).get(fid, "")
            if kbody:
                for i, para in enumerate(
                        [p.strip() for p in kbody.split("\n\n") if p.strip()]):
                    A(Paragraph(MP.esc(para),
                                S["body1"] if i == 0 else S["body"]))
            A(PageBreak())

        for rec in members:
            entry = (book.get("entries") or {}).get(rec["id"])
            if not entry:
                continue
            A(MP.Mark("entry", head=rec["name"], civ=kl["en"],
                      cid=rec["id"]))
            A(_PinMatter(rec["id"], MP))
            for fl in entry_flow_book(rec, spec, entry["sections"], L, S,
                                      use_plates, page_ref, by_id, trads,
                                      classes, kinfam, MP):
                A(fl)
            A(PageBreak())

    # ── sonsöz ve arka madde ────────────────────────────────────────────
    for group, key, title, _p in MATTER_SECTIONS:
        if group != "back":
            continue
        item = (book.get(matter_group(key)) or {}).get(key) or {}
        if not item.get("body"):
            continue
        A(MP.Mark("matter", head=title, civ=BOOK_TITLE, no_head=True,
                  cid="matter/" + key))
        A(_PinMatter("matter/" + key, MP))
        for fl in MPG.matter_flow(title, item["body"], L, S):
            A(fl)
        A(PageBreak())

    # ── dizinler ────────────────────────────────────────────────────────
    for key in ("traditions", "motifs", "kin", "pronunciation"):
        A(MP.Mark("index", head=FM.INDEX_TITLES[key], civ=BOOK_TITLE,
                  no_head=True, cid="index/" + key))
        A(_PinMatter("index/" + key, MP))
        A(Spacer(1, 0.55 * IN))
        A(Paragraph(EP.tracked(FM.INDEX_TITLES[key].upper(), 0.07, 16 * k),
                    S["fmtitle"]))
        A(Paragraph(MP.esc(FM.INDEX_NOTES[key]), S["fmnote"]))
        A(Spacer(1, 8 * k))
        if indexes:
            for fl in index_flow(key, indexes, S, MP, text_w, k):
                A(fl)
        A(PageBreak())

    # ── kaynaklar ───────────────────────────────────────────────────────
    A(MP.Mark("sources", head=FM.SOURCES_TITLE, civ=BOOK_TITLE,
              no_head=True, cid="sources"))
    A(_PinMatter("sources", MP))
    A(Spacer(1, 0.55 * IN))
    A(Paragraph(EP.tracked(FM.SOURCES_TITLE.upper(), 0.07, 16 * k),
                S["fmtitle"]))
    A(Paragraph(MP.esc(FM.SOURCES_NOTE), S["fmnote"]))
    A(Spacer(1, 8 * k))
    for t in sorted(spec["traditions"], key=lambda x: x["name"]):
        mem = [c for c in creatures if c["tradition"] == t["id"]]
        if not mem:
            continue
        A(Paragraph(EP.display_safe(MP.esc(t["name"])), S["srchead"]))
        for rec in mem:
            entry = (book.get("entries") or {}).get(rec["id"])
            note = (entry.get("sections") or {}).get("sources", "") if entry \
                else ""
            if not note:
                continue
            A(Paragraph(f"<b>{MP.esc(rec['name'])}</b> — {MP.esc(note)}",
                        S["srcrow"]))
    return F


def _PinMatter(cid, MP):
    """Sayfa haritasına bir kimlik çakan sıfır yükseklikli nesne."""
    return MP.Mark("pin", head=None, civ=None, cid=cid)


def entry_flow_book(rec, spec, sections, L, S, use_plates, page_ref, by_id,
                    trads, classes, kinfam, MP):
    """Bir maddenin akışı — `entry_page.entry_flow`un ÜRETİM sürümü.

    Ölçüm sürümünden iki farkı var ve ikisi de üretime özgüdür:
    gerçek plaka görüntüsü, ve akraba satırındaki sayfa numaraları.
    """
    from reportlab.platypus import Paragraph, Spacer
    from reportlab.platypus.flowables import Flowable

    import entry_page as EP

    s = EP.ENTRY_SPEC
    k = L.ed.display_scale
    pw, ph = EP.plate_box(L)

    class GoldRule(Flowable):
        def __init__(self, w):
            super().__init__()
            self.width, self.height = w, s["kin_rule_pt"] + 4 * k

        def draw(self):
            c = self.canv
            c.saveState()
            c.setStrokeColor(s["kin_rule_color"])
            c.setLineWidth(s["kin_rule_pt"])
            c.line(0, 2 * k, self.width, 2 * k)
            c.restoreState()

    flow = [plate_flowable(rec, pw, ph, use_plates),
            Spacer(1, s["plate_gap_pt"] * k)]
    flow.append(Paragraph(
        EP.tracked(rec["name"], s["title_tracking_em"], s["title_pt"] * k),
        S["title"]))

    trad = trads.get(rec["tradition"], {})
    klass = classes.get(rec["class"], {})
    # GELENEK SİGİLİ BASILMAZ. Kırk sigilin otuz yedisinin ne EB Garamond'da
    # ne Cinzel'de glifi var (ölçüldü); hiyeroglif, çivi yazısı, Maya
    # rakamı, runa ve hangul'u tek metin fontuyla dizmek mümkün değil.
    # Basılmayan bir işaret, tutarsız bir işaret sisteminden iyidir.
    #
    # Yerine AKRABA AİLESİ harfi kondu — "bu kitap nasıl okunur" bölümünün
    # "madde başlığının yanında aileyi gösteren bir işaret" sözünü tutan,
    # ve her yerde dizilebilen işaret budur.
    meta = (f"{trad.get('name', '?')} &nbsp;·&nbsp; "
            f"{rec['class']} · {klass.get('en', '')}")
    fam0 = kinfam.get(rec.get("kinFamily"))
    if fam0:
        meta += f" &nbsp;·&nbsp; {fam0['id']} · {fam0['en']}"
    meta += f" &nbsp;·&nbsp; {' '.join(rec['motif'])}"
    if rec.get("pronunciation"):
        meta += f" &nbsp;·&nbsp; [{rec['pronunciation']}]"
    flow.append(Paragraph(meta, S["meta"]))

    for key, _label, _lo, _hi in ENTRY_SECTIONS:
        text = sections.get(key, "")
        if not text:
            continue
        text = MP.esc(text)
        if key == "opening":
            flow.append(Paragraph(text, S["opening"]))
        elif key == "kin":
            flow.append(GoldRule(L.ed.text_w * 72.0))
            fam = kinfam.get(rec.get("kinFamily"))
            lead = f"<b>{fam['en']}</b> — " if fam else ""
            refs = ", ".join(
                f"{by_id[r]['name']} <font color='#777777'>p.&nbsp;"
                f"{page_ref(r)}</font>"
                for r in rec.get("crossRefs", []) if r in by_id)
            flow.append(Paragraph(f"{lead}{text} <i>See also:</i> {refs}.",
                                  S["kin"]))
        elif key == "sources":
            flow.append(Paragraph(text, S["sources"]))
        else:
            flow.append(Paragraph(text, S["body1"] if key == "where"
                                  else S["body"]))
    return flow


def index_flow(key, indexes, S, MP, text_w, k):
    from reportlab.platypus import Paragraph

    from entry_page import display_safe as _safe

    out = []
    if key == "traditions":
        for row in indexes["traditions"]:
            out.append(Paragraph(_safe(MP.esc(row["tradition"])),
                                 S["idxhead"]))
            out.append(Paragraph(", ".join(
                f"{MP.esc(e['name'])} <font color='#777777'>{e['page']}</font>"
                for e in row["entries"]), S["idxrow"]))
    elif key == "motifs":
        for row in indexes["motifs"]:
            out.append(Paragraph(
                f"<b>{row['motif']}</b> &nbsp; " + ", ".join(
                    f"{MP.esc(e['name'])} "
                    f"<font color='#777777'>{e['page']}</font>"
                    for e in row["entries"]), S["idxrow"]))
    elif key == "kin":
        for row in indexes["kin"]:
            out.append(Paragraph(
                _safe(f"{row['family']} · {MP.esc(row['en'])}"),
                S["idxhead"]))
            out.append(Paragraph(MP.esc(row.get("divergenceEn")
                                        or row.get("divergence", "")),
                                 S["idxnote"]))
            out.append(Paragraph(", ".join(
                f"{MP.esc(e['name'])} <font color='#777777'>{e['page']}</font>"
                for e in row.get("members", [])), S["idxrow"]))
    else:
        for row in indexes["pronunciation"]:
            if row.get("type") == "crossref":
                out.append(Paragraph(
                    f"{MP.esc(row['name'])} <i>see</i> "
                    f"{MP.esc(row.get('seeAlso',''))}", S["idxrow"]))
            else:
                out.append(Paragraph(
                    f"{MP.esc(row['name'])} &nbsp;<font color='#555555'>"
                    f"[{MP.esc(row.get('pronunciation',''))}]</font> "
                    f"<font color='#777777'>{row.get('page','—')}</font>",
                    S["idxrow"]))
    return out


# =============================================================================
# STİLLER
# =============================================================================

def styles(L, MP):
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
    from reportlab.lib.styles import ParagraphStyle as PS

    import matter_page as MPG

    k = L.ed.display_scale
    b, lead = L.BODY_PT, L.LEAD_PT
    S = dict(MPG.matter_styles(L))
    S.update(MP.L.S if False else {})
    S.update(
        body=L.S["body"], body1=L.S["body1"],
        fmhalf=PS("fmhalf", fontName="Cinzel", fontSize=17 * k,
                  leading=24 * k, alignment=TA_CENTER, textColor="#111111"),
        btitle=PS("btitle2", fontName="Cinzel", fontSize=27 * k,
                  leading=34 * k, alignment=TA_CENTER, textColor="#111111"),
        bsub=PS("bsub2", fontName="GaraIt", fontSize=13 * k, leading=18 * k,
                alignment=TA_CENTER, textColor="#444444"),
        bline=PS("bline", fontName="Gara", fontSize=10.5 * k, leading=15 * k,
                 alignment=TA_CENTER, textColor="#555555"),
        author=PS("author2", fontName="Cinzel", fontSize=12.5 * k,
                  leading=18 * k, alignment=TA_CENTER, textColor="#111111"),
        imprint=PS("imprint2", fontName="Cinzel", fontSize=9 * k,
                   leading=13 * k, alignment=TA_CENTER, textColor="#555555"),
        copy=PS("copy", fontName="Gara", fontSize=8.2 * k, leading=11.6 * k,
                alignment=TA_LEFT, textColor="#333333", spaceAfter=5.5 * k),
        ded=PS("ded", fontName="GaraIt", fontSize=11.5 * k, leading=17 * k,
               alignment=TA_CENTER, textColor="#333333"),
        fmtitle=PS("fmtitle2", fontName="Cinzel", fontSize=16 * k,
                   leading=22 * k, alignment=TA_CENTER, textColor="#111111",
                   spaceAfter=14 * k),
        fmnote=PS("fmnote", fontName="GaraIt", fontSize=9.5 * k,
                  leading=14 * k, alignment=TA_JUSTIFY, textColor="#555555"),
        toc=PS("toc", fontName="Gara", fontSize=10.2 * k, leading=17 * k,
               alignment=TA_LEFT, textColor="#222222"),
        maphead=PS("maphead", fontName="Cinzel", fontSize=9 * k,
                   leading=15 * k, textColor="#8A6E2F", spaceBefore=7 * k),
        maprow=PS("maprow", fontName="Gara", fontSize=10 * k, leading=13.5 * k,
                  textColor="#222222"),
        mapnum=PS("mapnum", fontName="Gara", fontSize=10 * k, leading=13.5 * k,
                  alignment=TA_CENTER, textColor="#777777"),
        classnum=PS("classnum", fontName="Cinzel", fontSize=10 * k,
                    leading=16 * k, alignment=TA_CENTER, textColor="#8A6E2F"),
        classname=PS("classname", fontName="Cinzel", fontSize=23 * k,
                     leading=30 * k, alignment=TA_CENTER, textColor="#111111",
                     spaceBefore=6 * k),
        classmeta=PS("classmeta", fontName="GaraIt", fontSize=10.5 * k,
                     leading=15 * k, alignment=TA_CENTER, textColor="#555555",
                     spaceBefore=8 * k),
        kinlist=PS("kinlist", fontName="Gara", fontSize=10 * k,
                   leading=16 * k, alignment=TA_CENTER, textColor="#333333"),
        idxhead=PS("idxhead", fontName="Cinzel", fontSize=9.5 * k,
                   leading=14 * k, textColor="#8A6E2F", spaceBefore=8 * k,
                   spaceAfter=2 * k),
        idxrow=PS("idxrow", fontName="Gara", fontSize=8.8 * k,
                  leading=12.2 * k, alignment=TA_LEFT, textColor="#222222",
                  spaceAfter=2.5 * k),
        idxnote=PS("idxnote", fontName="GaraIt", fontSize=8.5 * k,
                   leading=12 * k, textColor="#666666", spaceAfter=2 * k),
        srchead=PS("srchead", fontName="Cinzel", fontSize=9.5 * k,
                   leading=14 * k, textColor="#8A6E2F", spaceBefore=9 * k,
                   spaceAfter=2 * k),
        srcrow=PS("srcrow", fontName="Gara", fontSize=8.6 * k,
                  leading=12 * k, alignment=TA_JUSTIFY, textColor="#333333",
                  spaceAfter=3 * k),
    )
    S["opening"] = PS("opening2", fontName="GaraIt", fontSize=b, leading=lead,
                      alignment=TA_JUSTIFY, textColor="#111111",
                      firstLineIndent=0, spaceAfter=lead * 0.35)
    for key in ("title", "meta", "kin", "sources"):
        S[key] = None
    import entry_page as EP
    ES = EP.entry_styles(L)
    for key in ("title", "meta", "kin", "sources"):
        S[key] = ES[key]
    return S


# =============================================================================
# ÜRETİM
# =============================================================================

class BestiariumBook:
    """`make_pdf.Book`un Bestiarium metadatasıyla eşdeğeri."""

    @staticmethod
    def make(MP, L, path):
        from reportlab.lib.units import inch as IN
        from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate

        ed = L.ed
        doc = BaseDocTemplate(
            path, pagesize=(L.PW, L.PH),
            title=f"{BOOK_TITLE}: {BOOK_SUBTITLE}{ed.title_suffix}",
            author=AUTHOR,
            subject=f"World folklore reference · {SERIES} volume {VOLUME}",
            creator=IMPRINT,
        )
        w = L.PW - L.GUTTER - L.OUTER
        h = L.PH - L.TOPM - L.BOTM
        fr = Frame(L.GUTTER, L.BOTM, w, h, id="r", leftPadding=0,
                   rightPadding=0, topPadding=0, bottomPadding=0)
        fv = Frame(L.OUTER, L.BOTM, w, h, id="v", leftPadding=0,
                   rightPadding=0, topPadding=0, bottomPadding=0)
        doc.addPageTemplates([
            PageTemplate("recto", [fr], onPage=MP.on_recto),
            PageTemplate("verso", [fv], onPage=MP.on_verso)])

        def handle_pageBegin(self=doc):
            BaseDocTemplate._handle_pageBegin(self)
            self._handle_nextPageTemplate(
                "verso" if (self.page + 1) % 2 == 0 else "recto")

        doc.handle_pageBegin = handle_pageBegin
        _ = IN
        return doc


def typeset(edition: str, out_path: str, pages: dict, use_plates: bool,
            indexes: dict | None) -> tuple[int, dict]:
    """Tek geçiş. (toplam sayfa, sayfa haritası) döner."""
    import make_pdf as MP
    import reportlab.rl_config as rl_config

    # ASCII85 KAPALI. reportlab görüntü akışını varsayılan olarak ASCII85 ile
    # kodlar ve ikili veriyi %25 şişirir. PDF ikili akış taşıyabilir; bu
    # kodlama yalnızca 7-bit aktarım gerektiren ortamlar içindi. Kayıpsız,
    # bedava kazanç.
    rl_config.useA85 = 0

    # SAYFA AKIŞI SIKIŞTIRILIR. reportlab'in varsayılanı KAPALIDIR ve
    # sıkıştırmasız çıktı 231 MB oluyordu; aynı plakalar sıkıştırmayla
    # ~25 MB. KDP'nin 650 MB sınırının altında olmak yeterli değil: 231 MB
    # bir dosya yüklenemez, incelenemez ve prova döngüsünü saatlere yayar.
    #
    # Bu bir kalite düşüşü DEĞİLDİR: Flate kayıpsızdır. Plakalar 1800 px
    # (kutuda 600 DPI) gri tonda kalır — ölçüldü, plakaların %26'sı ara
    # tondur ve iki tona indirmek o bilgiyi yok ederdi. İki ton kararı
    # (D49) Kindle ve web içindi, baskı için değil.
    rl_config.pageCompression = 1

    L = MP.configure(edition)
    S = styles(L, MP)

    book = load_book()
    spec = load_spec()

    MP.PLAN.__init__()
    MP.PLAN.pins = {}

    orig_draw = MP.Mark.draw

    def draw(self):
        orig_draw(self)
        if getattr(self, "cid", None):
            MP.PLAN.pins.setdefault(self.cid, self.canv.getPageNumber())

    MP.Mark.draw = draw
    try:
        doc = BestiariumBook.make(MP, L, out_path)
        flow = book_flow(book, spec, L, S, MP, pages, use_plates, indexes)
        doc.build(flow, canvasmaker=MP.EmbeddedOnlyCanvas)
    finally:
        MP.Mark.draw = orig_draw

    from pypdf import PdfReader
    total = len(PdfReader(out_path).pages)

    front_end = MP.PLAN.front_end
    body_start = MP.PLAN.body_start or 1
    pagemap = {}
    for cid, phys in MP.PLAN.pins.items():
        pagemap[cid] = phys - body_start + 1 if phys >= body_start else phys
    pagemap["_meta"] = {
        "edition": edition,
        "physicalPages": total,
        "frontMatterPages": front_end,
        "bodyStartsAtPhysical": body_start,
        "note": "Sayfa numaraları BASILAN numaralardır (arap rakamları "
                "gövde başında 1'den başlar). Üreten: 08_BUILD/make_book.py",
    }
    return total, pagemap


def build(edition: str, use_plates: bool = True, verbose: bool = True) -> int:
    _require()
    book = load_book()
    if book is None or not book.get("entries"):
        print("ATLANDI: metin yok — iç blok dizgisi yazımdan sonradır.")
        return 2

    sub = EDITION_DIRS[edition]
    out_dir = os.path.join(PRINT_DIR, sub)
    os.makedirs(out_dir, exist_ok=True)
    pdf = os.path.join(out_dir, f"CODEX_BESTIARIUM_INTERIOR_{sub}.pdf")
    pm_path = os.path.join(out_dir, "pagemap.json")

    if verbose:
        print("=" * 78)
        print(f"İÇ BLOK DİZGİSİ — {edition}")
        print("=" * 78)

    # 1. geçiş — dizin gövdesi yok, çapraz referanslar yer tutucu
    total1, pm1 = typeset(edition, pdf, {}, use_plates, None)
    if verbose:
        print(f"  1. geçiş : {total1} sayfa (dizin gövdesi yok)")

    # dizinler gerçek numaralarla üretilir
    with open(pm_path, "w", encoding="utf-8") as fh:
        json.dump(pm1, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    rc = os.system(
        f'cd "{ROOT}" && python3 08_BUILD/make_index.py '
        f'--pagemap "{os.path.relpath(pm_path, ROOT)}" '
        f'--gate phase6 >/dev/null 2>&1')
    if rc != 0 and verbose:
        print("  [uyarı] make_index phase6 kapısı geçmedi — dizinler yine de "
              "üretildi; ayrıntı için betiği tek başına koşun")
    indexes = {}
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, encoding="utf-8") as fh:
            indexes = json.load(fh)

    # 2. geçiş — dizinlerle, çapraz referanslar gerçek numarayla
    total2, pm2 = typeset(edition, pdf, pm1, use_plates, indexes)
    if verbose:
        print(f"  2. geçiş : {total2} sayfa (dizinlerle)")

    # DOĞRULAMA: dizinlerden ÖNCEKİ hiçbir sayfa kaymamalı
    moved = [k for k in pm1
             if not k.startswith(("index/", "sources", "_"))
             and pm1[k] != pm2.get(k)]
    if moved:
        print(f"\n[FAIL] iki geçiş arasında {len(moved)} sayfa kaydı: "
              f"{moved[:6]}")
        print("       Dizin gövdesi kendinden önceki sayfaları kaydırdı. "
              "Varsayım çöktü; numaralar güvenilmez.")
        return 1

    with open(pm_path, "w", encoding="utf-8") as fh:
        json.dump(pm2, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    if verbose:
        creatures = sum(1 for k in pm2 if not k.startswith(
            ("class/", "kin/", "matter/", "index/", "sources", "_")))
        print(f"\n  [  ok ] madde sayfası kaymadı — iki geçiş birebir")
        print(f"  sayfa haritası: {creatures} madde + sınıf/aile/matter/dizin")
        print(f"\n  yazıldı: {os.path.relpath(pdf, ROOT)}")
        print(f"  yazıldı: {os.path.relpath(pm_path, ROOT)}")
        print(f"\n  TOPLAM SAYFA: {total2}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--edition", default="paperback",
                    choices=sorted(EDITION_DIRS))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--no-plates", action="store_true")
    args = ap.parse_args()

    eds = sorted(EDITION_DIRS) if args.all else [args.edition]
    worst = 0
    for ed in eds:
        rc = build(ed, use_plates=not args.no_plates)
        worst = max(worst, rc)
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
