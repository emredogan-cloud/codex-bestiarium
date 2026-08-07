# -*- coding: utf-8 -*-
"""Canonical book model + typographic normalisation shared by all output builders."""
import json, re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matter as M

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
# Kanonik metin 01_SOURCE altında yaşar. (Eskiden 08_BUILD içinde aranıyordu;
# dosyalar 01_SOURCE'a taşındığında model.py güncellenmemişti ve iç blok
# DERLENEMEZ hâle gelmişti — kapak hattı taşınmış, metin hattı unutulmuştu.)
SOURCE = os.path.join(ROOT, '01_SOURCE')
BOOK_JSON = os.path.join(SOURCE, 'book-edited.json')
if not os.path.exists(BOOK_JSON):                      # düzenlenmemiş yedek
    BOOK_JSON = os.path.join(SOURCE, 'book.json')

# ── typographic normalisation ────────────────────────────────────────
_APOS_AFTER = re.compile(r"(?<=[A-Za-zÀ-ÿ0-9])'")          # Zeus's, don't, o'clock

def _pair(t: str, straight: str, open_c: str, close_c: str) -> str:
    """Alternate open/close across a paragraph.

    A state machine, not a look-behind heuristic: it is the only thing that gets
    interrupted dialogue right — `“…But —” and he stepped back “— I am leaving.”`
    Each paragraph starts outside a quotation, which is correct for this book
    (no speech runs across a paragraph break).
    """
    out, inside = [], False
    for ch in t:
        if ch == straight:
            out.append(close_c if inside else open_c)
            inside = not inside
        else:
            out.append(ch)
    return ''.join(out)

def smarten(t: str) -> str:
    """Straight quotes -> typographic quotes. Order matters."""
    if not t:
        return t
    t = t.replace('...', '…')                      # ellipsis
    t = re.sub(r'(?<=\w)--(?=\w)', '—', t)         # stray double hyphen
    t = _APOS_AFTER.sub('', t)               # park apostrophes
    t = _pair(t, '"', '“', '”')          # doubles
    t = _pair(t, "'", '‘', '’')          # any true single quotes
    t = t.replace('', '’')              # restore apostrophes
    # interrupted speech: set quote tight against the dash — “…But —” he said “— I go.”
    t = t.replace('\u2014 \u201d', '\u2014\u201d').replace('\u201c \u2014', '\u201c\u2014')
    t = t.replace('\u2013 \u201d', '\u2013\u201d').replace('\u201c \u2013', '\u201c\u2013')
    t = re.sub(r'[ \t]{2,}', ' ', t)
    return t.strip()

# ── model ────────────────────────────────────────────────────────────
def load():
    if not os.path.exists(BOOK_JSON):
        raise SystemExit(
            f"kanonik metin yok: {BOOK_JSON}\n"
            f"01_SOURCE/book-edited.json bulunmalı (extract.js + edits.py çıktısı).")
    B = json.load(open(BOOK_JSON, encoding='utf-8'))
    civs = {c['id']: c for c in B['civs']}
    order = [c['id'] for c in B['civs']]
    parts = []
    seen = set()
    for s in B['stories']:
        cid = s['civilization']
        if cid not in seen:
            seen.add(cid)
            c = civs[cid]
            parts.append({'kind': 'civ', 'id': cid, 'full': c['full'], 'name': c['name'],
                          'epoch': c['epoch'], 'desc': smarten(c['description'])})
        blocks = []
        for item in s['content']:
            if isinstance(item, str):
                blocks.append(('p', smarten(item)))
            elif item.get('style') == 'quote':
                blocks.append(('q', smarten(item.get('text', ''))))
            elif item.get('style') == 'hr':
                blocks.append(('hr', ''))
        parts.append({'kind': 'story', 'id': s['id'], 'civ': cid,
                      'title': smarten(s['title']), 'subtitle': smarten(s.get('subtitle') or ''),
                      'themes': s.get('themes', []), 'blocks': blocks})
    return B, civs, order, parts

def story_count(parts):
    return sum(1 for p in parts if p['kind'] == 'story')

def word_count(parts):
    n = 0
    for p in parts:
        if p['kind'] == 'story':
            for k, t in p['blocks']:
                if k in ('p', 'q'):
                    n += len(t.split())
    return n

# ── front / back matter as renderable block lists ────────────────────
def paras(txt):
    return [x.strip() for x in txt.strip().split('\n\n') if x.strip()]

def front_sections():
    return [
        ('Introduction', M.INTRODUCTION_TITLE, [smarten(p) for p in paras(M.INTRODUCTION)]),
        ('Note',         M.NOTE_ON_NAMES_TITLE, [smarten(p) for p in paras(M.NOTE_ON_NAMES)]),
    ]

def back_sections(civs, order, parts):
    counts = {}
    for p in parts:
        if p['kind'] == 'story':
            counts[p['civ']] = counts.get(p['civ'], 0) + 1
    civ_lines = [f"{civs[c]['full']} — {civs[c]['name']}, {civs[c]['epoch']} — "
                 f"{counts.get(c,0)} {'story' if counts.get(c,0)==1 else 'stories'}"
                 for c in order]
    return [
        ('Afterword', M.AFTERWORD_TITLE,             [smarten(p) for p in paras(M.AFTERWORD)]),
        ('Reference', M.CIVILIZATION_NOTE_TITLE,     civ_lines),
        ('Author',    M.ABOUT_AUTHOR_TITLE,          [smarten(p) for p in paras(M.ABOUT_AUTHOR)]),
        ('CTA',       M.REVIEW_CTA_TITLE,            [smarten(p) for p in paras(M.REVIEW_CTA)]),
        ('Colophon',  M.COLOPHON_TITLE,              [smarten(p) for p in paras(M.COLOPHON)]),
    ]
