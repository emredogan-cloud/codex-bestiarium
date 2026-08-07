# -*- coding: utf-8 -*-
"""
CODEX MYTHOLOGICA — BASKIYA HAZIR İÇ BLOK  (ciltsiz · ciltli · büyük punto)
================================================================================
Tek motor, üç sürüm. Sayfa ölçüsü, marjlar, punto ve satır aralığı
`editions.py` içinden gelir; bu dosyada sürüme özgü hiçbir sabit yoktur.

    python3 08_BUILD/make_pdf.py --edition paperback
    python3 08_BUILD/make_pdf.py --edition hardcover
    python3 08_BUILD/make_pdf.py --edition largeprint

İKİ GEÇİŞLİ DERLEME
-------------------
Sayfa kromu (üstbilgi + folyo) sayfa AÇILIRKEN çizilir, yani o sayfadaki hiçbir
akış nesnesi henüz çizilmemiştir. Bu yüzden 1. geçiş her hikâyenin/bölümün
hangi sayfada başladığını kaydeder; 2. geçiş doğru üstbilgi ve folyoyu basar.
Ayrıca medeniyet açılışlarının TEK sayfaya (recto) denk gelmesi analitik olarak
çözülür — boş sayfa eklenerek.

FONTLAR
-------
07_ASSETS/fonts/ altındaki değişken fontlardan okunur. (Eskiden /tmp/fonts'a
bakılıyordu; o dizin silindiğinde iç blok DERLENEMEZ hâle gelmişti — kapak
hattı taşınmış ama iç blok unutulmuştu.)
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model
import matter as M
import editions as E
import paths as P

from reportlab.lib.units import inch as IN
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak)
from reportlab.pdfgen.canvas import Canvas

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTS = os.path.join(ROOT, "07_ASSETS", "fonts")

# ── fontlar ──────────────────────────────────────────────────────────
_FONT_FILES = {
    'Gara':   'EBGaramond[wght].ttf',
    'GaraIt': 'EBGaramond-Italic[wght].ttf',
    'Cinzel': 'Cinzel[wght].ttf',
}
for _name, _fn in _FONT_FILES.items():
    _path = os.path.join(FONTS, _fn)
    if not os.path.exists(_path):
        raise SystemExit(
            f"font yok: {_path}\n"
            f"kurulum: ./08_BUILD/bootstrap.sh  (fontları indirir)")
    pdfmetrics.registerFont(TTFont(_name, _path))
pdfmetrics.registerFontFamily('Gara', normal='Gara', bold='Gara',
                              italic='GaraIt', boldItalic='GaraIt')

# reportlab her sayfanın font kaynağını Helvetica ile tohumlar (gömülmeyen
# base-14 yüz). KDP iç bloktaki her fontun gömülü olmasını ister; bu yüzden
# genel varsayılan kendi gömülü fontumuza çevrilir.
from reportlab import rl_config                              # noqa: E402
rl_config.canvas_basefontname = 'Gara'
import reportlab.lib.styles as _rlstyles                      # noqa: E402
_rlstyles._baseFontName = 'Gara'
_rlstyles._baseFontNameB = 'Gara'
_rlstyles._baseFontNameI = 'GaraIt'
_rlstyles._baseFontNameBI = 'GaraIt'

INK = '#111111'


# =============================================================================
# SÜRÜME BAĞLI YERLEŞİM
# =============================================================================

class Layout:
    """Bir sürümün sayfa geometrisi + stil sözlüğü."""

    def __init__(self, ed: E.Edition):
        self.ed = ed
        self.PW, self.PH = ed.trim_w * IN, ed.trim_h * IN
        self.GUTTER = ed.gutter * IN
        self.OUTER = ed.outer * IN
        self.TOPM = ed.top * IN
        self.BOTM = ed.bottom * IN
        self.BODY_PT = ed.body_pt
        self.LEAD_PT = ed.lead_pt
        self.S = self._styles()

    def _styles(self):
        b, l, k = self.BODY_PT, self.LEAD_PT, self.ed.display_scale

        def st(n, **kw):
            return ParagraphStyle(n, **kw)

        return dict(
            body    = st('body', fontName='Gara', fontSize=b, leading=l,
                         alignment=TA_JUSTIFY, textColor=INK,
                         firstLineIndent=16 * k, allowWidows=0, allowOrphans=0,
                         hyphenationLang='en_US'),
            body1   = st('body1', fontName='Gara', fontSize=b, leading=l,
                         alignment=TA_JUSTIFY, textColor=INK, firstLineIndent=0,
                         allowWidows=0, allowOrphans=0, hyphenationLang='en_US'),
            quote   = st('quote', fontName='GaraIt', fontSize=b - 0.4, leading=l,
                         alignment=TA_JUSTIFY, textColor=INK,
                         leftIndent=26 * k, rightIndent=26 * k,
                         spaceBefore=l * .55, spaceAfter=l * .55,
                         allowWidows=0, allowOrphans=0),
            aster   = st('aster', fontName='Gara', fontSize=b, leading=l * 1.6,
                         alignment=TA_CENTER, textColor='#666666',
                         spaceBefore=l * .5, spaceAfter=l * .5),
            ctitle  = st('ctitle', fontName='Cinzel', fontSize=19 * k,
                         leading=24 * k, alignment=TA_CENTER, textColor=INK,
                         spaceAfter=5 * k),
            csub    = st('csub', fontName='GaraIt', fontSize=11.5 * k,
                         leading=15 * k, alignment=TA_CENTER,
                         textColor='#555555', spaceAfter=4 * k),
            civname = st('civname', fontName='Cinzel', fontSize=22 * k,
                         leading=28 * k, alignment=TA_CENTER, textColor=INK,
                         spaceAfter=8 * k),
            civmeta = st('civmeta', fontName='GaraIt', fontSize=11.5 * k,
                         leading=16 * k, alignment=TA_CENTER,
                         textColor='#555555', spaceAfter=14 * k),
            civdesc = st('civdesc', fontName='Gara', fontSize=11.5 * k,
                         leading=17 * k, alignment=TA_CENTER,
                         textColor='#333333', leftIndent=22 * k,
                         rightIndent=22 * k),
            fmtitle = st('fmtitle', fontName='Cinzel', fontSize=17 * k,
                         leading=23 * k, alignment=TA_CENTER, textColor=INK,
                         spaceAfter=18 * k),
            btitle  = st('btitle', fontName='Cinzel', fontSize=30 * k,
                         leading=38 * k, alignment=TA_CENTER, textColor=INK),
            bsub    = st('bsub', fontName='GaraIt', fontSize=13.5 * k,
                         leading=19 * k, alignment=TA_CENTER, textColor='#444444'),
            author  = st('author', fontName='Cinzel', fontSize=14 * k,
                         leading=20 * k, alignment=TA_CENTER, textColor=INK),
            imprint = st('imprint', fontName='Gara', fontSize=10.5 * k,
                         leading=15 * k, alignment=TA_CENTER, textColor='#555555'),
            cright  = st('cright', fontName='Gara', fontSize=8.8 * k,
                         leading=12.6 * k, textColor='#333333', spaceAfter=7 * k),
            ded     = st('ded', fontName='GaraIt', fontSize=12 * k,
                         leading=18 * k, alignment=TA_CENTER, textColor='#333333'),
            toc     = st('toc', fontName='Gara', fontSize=10 * k,
                         leading=14.2 * k, textColor=INK, leftIndent=12 * k,
                         firstLineIndent=-12 * k, spaceAfter=1.2 * k),
            tocciv  = st('tocciv', fontName='Cinzel', fontSize=10 * k,
                         leading=15 * k, textColor=INK,
                         spaceBefore=9 * k, spaceAfter=3 * k),
            ref     = st('ref', fontName='Gara', fontSize=10.4 * k,
                         leading=15 * k, textColor=INK, leftIndent=12 * k,
                         firstLineIndent=-12 * k, spaceAfter=3 * k),
        )


# Aktif yerleşim — configure() ile kurulur. Sayfa kromu ve şablonlar buradan
# okur (reportlab geri çağrıları parametre alamadığı için modül düzeyinde).
L: Layout = None


def configure(edition: str) -> Layout:
    global L
    L = Layout(E.get(edition))
    return L


# =============================================================================
# YERLEŞİM HARİTASI  (1. geçiş doldurur)
# =============================================================================

class Plan:
    def __init__(self):
        self.marks = []       # (page, kind, head, civ)
        self.heads = {}       # page -> (head, civ)
        self.no_head = set()  # açılış sayfaları
        self.front_end = 0    # son numarasız sayfa
        self.body_start = 0   # ilk arap rakamlı sayfa
        self.civ_pages = {}   # civ id -> açıldığı sayfa

    def resolve(self, total):
        self.marks.sort(key=lambda m: m[0])
        head = civ = ''
        for p in range(1, total + 1):
            for mp, kind, h, c in self.marks:
                if mp == p:
                    if h is not None:
                        head = h
                    if c is not None:
                        civ = c
            self.heads[p] = (head, civ)


PLAN = Plan()


class Mark(Spacer):
    """Yüksekliği sıfır olan akış nesnesi; dizgi sırasında sayfasını kaydeder."""

    def __init__(self, kind, head=None, civ=None, no_head=False, cid=None):
        super().__init__(0, 0)
        self.kind, self.head, self.civ, self.nh, self.cid = \
            kind, head, civ, no_head, cid

    def draw(self):
        pg = self.canv.getPageNumber()
        if self.kind == 'civ_open' and self.civ:
            PLAN.civ_pages[self.civ] = pg
        PLAN.marks.append((pg, self.kind, self.head, self.civ))
        if self.nh:
            PLAN.no_head.add(pg)
        if self.kind == 'front_end':
            PLAN.front_end = pg
        if self.kind == 'body_start' and not PLAN.body_start:
            PLAN.body_start = pg


def _roman(n):
    vals = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'),
            (90, 'xc'), (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'),
            (5, 'v'), (4, 'iv'), (1, 'i')]
    out = ''
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


def _chrome(canvas, doc, verso):
    n = canvas.getPageNumber()
    canvas.saveState()
    canvas.setFont('Gara', L.ed.folio_pt)   # asla base-14 yüz seçili kalmasın
    label = None
    if PLAN.body_start and n >= PLAN.body_start:
        label = str(n - PLAN.body_start + 1)
    elif PLAN.front_end and n > PLAN.front_end:
        label = _roman(n - PLAN.front_end)
    if label:
        canvas.setFont('Gara', L.ed.folio_pt)
        canvas.setFillColor('#555555')
        canvas.drawCentredString(L.PW / 2, L.BOTM * 0.52, label)
        if n not in PLAN.no_head:
            head, civ = PLAN.heads.get(n, ('', ''))
            t = civ if verso else head
            if t:
                canvas.setFont('Cinzel', L.ed.head_pt)
                canvas.setFillColor('#777777')
                canvas.drawCentredString(L.PW / 2, L.PH - L.TOPM * 0.60,
                                         t.upper()[:56])
    canvas.restoreState()


class EmbeddedOnlyCanvas(Canvas):
    """reportlab sayfa başlangıcında Helvetica seçer (gömülmeyen base-14).
    KDP iç bloktaki her fontun gömülü olmasını ister — başlangıç fontunu
    gömülü bir yüzle değiştiriyoruz."""

    def __init__(self, *a, **kw):
        kw.setdefault('initialFontName', 'Gara')
        kw.setdefault('initialFontSize', L.BODY_PT if L else 11.2)
        super().__init__(*a, **kw)


def on_recto(c, d): _chrome(c, d, verso=False)
def on_verso(c, d): _chrome(c, d, verso=True)


class Book(BaseDocTemplate):
    def __init__(self, path):
        ed = L.ed
        title = f"{M.TITLE}: {M.SUBTITLE}{ed.title_suffix}"
        super().__init__(path, pagesize=(L.PW, L.PH), title=title,
                         author=M.AUTHOR, subject="World mythology retold",
                         creator=M.IMPRINT)
        w = L.PW - L.GUTTER - L.OUTER
        h = L.PH - L.TOPM - L.BOTM
        fr = Frame(L.GUTTER, L.BOTM, w, h, id='r', leftPadding=0,
                   rightPadding=0, topPadding=0, bottomPadding=0)
        fv = Frame(L.OUTER, L.BOTM, w, h, id='v', leftPadding=0,
                   rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate('recto', [fr], onPage=on_recto),
                               PageTemplate('verso', [fv], onPage=on_verso)])

    def handle_pageBegin(self):
        self._handle_pageBegin()
        # 1. sayfa rectodur; SONRAKİ sayfa pariteyi çevirir
        self._handle_nextPageTemplate(
            'verso' if (self.page + 1) % 2 == 0 else 'recto')


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def opening(text):
    w = text.split(' ')
    lead, rest = ' '.join(w[:3]), ' '.join(w[3:])
    return (f'<font face="Cinzel" size="{L.BODY_PT-1.4:.1f}">'
            f'{esc(lead).upper()}</font> {esc(rest)}')


def story_flow(blanks=frozenset()):
    S = L.S
    B, civs, order, parts = model.load()
    st = []
    add = st.append
    # ── ön madde ──
    add(Spacer(1, 2.5 * IN)); add(Paragraph(esc(M.TITLE), S['btitle']))
    add(PageBreak()); add(PageBreak())
    add(Spacer(1, 1.9 * IN)); add(Paragraph(esc(M.TITLE), S['btitle']))
    add(Spacer(1, 10)); add(Paragraph(esc(M.SUBTITLE), S['bsub']))
    add(Spacer(1, 1.5 * IN)); add(Paragraph(esc(M.AUTHOR), S['author']))
    add(Spacer(1, 1.7 * IN)); add(Paragraph(esc(M.IMPRINT), S['imprint']))
    add(PageBreak())
    add(Spacer(1, 3.1 * IN))
    for _, t in M.COPYRIGHT:
        add(Paragraph(esc(t), S['cright']))
    add(PageBreak())
    add(Spacer(1, 2.6 * IN))
    add(Paragraph(esc(M.DEDICATION[0][1]), S['ded']))
    add(PageBreak()); add(PageBreak())
    add(Paragraph('Contents', S['fmtitle']))
    for p in parts:
        add(Paragraph(esc(p['full'] if p['kind'] == 'civ' else p['title']),
                      S['tocciv'] if p['kind'] == 'civ' else S['toc']))
    add(Mark('front_end')); add(PageBreak())
    # ── giriş + not (roma rakamı) ──
    for _, title, plist in model.front_sections():
        add(Mark('opener', head=title, civ=M.TITLE, no_head=True))
        add(Paragraph(esc(title), S['fmtitle']))
        for i, para in enumerate(plist):
            add(Paragraph(esc(para), S['body1'] if i == 0 else S['body']))
        add(PageBreak())
    # ── gövde (1'den arap rakamı) ──
    first_civ = True
    for p in parts:
        if p['kind'] == 'civ':
            if p['id'] in blanks:
                add(PageBreak())            # recto açılışını zorla
            if first_civ:
                add(Mark('body_start')); first_civ = False
            add(Mark('civ_open', head=p['full'], civ=p['full'], no_head=True))
            add(Spacer(1, 1.55 * IN))
            add(Paragraph(esc(p['full'].replace(' Mythology', '')), S['civname']))
            add(Paragraph(f"{esc(p['name'])} &nbsp;·&nbsp; {esc(p['epoch'])}",
                          S['civmeta']))
            add(Paragraph(esc(p['desc']), S['civdesc']))
            add(PageBreak())
        else:
            add(Mark('opener', head=p['title'], no_head=True))
            add(Spacer(1, 0.42 * IN))
            add(Paragraph(esc(p['title']), S['ctitle']))
            add(Paragraph(esc(p['subtitle']), S['csub']))
            add(Spacer(1, 0.30 * IN))
            first = True
            for kind, text in p['blocks']:
                if kind == 'p':
                    add(Paragraph(opening(text) if first else esc(text),
                                  S['body1'] if first else S['body']))
                    first = False
                elif kind == 'q':
                    add(Paragraph(esc(text), S['quote']))
                else:
                    add(Paragraph('*&nbsp;&nbsp;*&nbsp;&nbsp;*', S['aster']))
            add(PageBreak())
    for tag, title, plist in model.back_sections(civs, order, parts):
        add(Mark('opener', head=title, civ=M.TITLE, no_head=True))
        add(Spacer(1, 0.42 * IN)); add(Paragraph(esc(title), S['fmtitle']))
        for i, para in enumerate(plist):
            sty = S['ref'] if tag == 'Reference' else (
                S['body1'] if i == 0 else S['body'])
            add(Paragraph(esc(para), sty))
        add(PageBreak())
    return st


def build(edition: str = "paperback", out_path: str = None):
    ed = configure(edition).ed
    out = out_path or P.interior_pdf(ed)
    os.makedirs(os.path.dirname(out), exist_ok=True)

    _, civs, order, parts = model.load()
    civ_order = [p['id'] for p in parts if p['kind'] == 'civ']
    name2id = {p['full']: p['id'] for p in parts if p['kind'] == 'civ'}

    import tempfile
    scratch = os.path.join(tempfile.gettempdir(), f'_codex_pass_{ed.slug}.pdf')

    def layout_pass(blanks, path=scratch):
        PLAN.marks.clear(); PLAN.no_head.clear(); PLAN.civ_pages.clear()
        PLAN.front_end = PLAN.body_start = 0
        d = Book(path)
        d.build(story_flow(blanks), canvasmaker=EmbeddedOnlyCanvas)
        return d.page

    # 1. geçiş — doğal konumlar
    layout_pass(frozenset())
    pos = {name2id[n]: pg for n, pg in PLAN.civ_pages.items()}

    # analitik: i. medeniyetten önce eklenen boş sayfa, i.'yi ve sonrasını 1 kaydırır
    blanks, offset = set(), 0
    for cid in civ_order:
        if (pos[cid] + offset) % 2 == 0:        # verso'da açılacaktı
            blanks.add(cid); offset += 1
    blanks = frozenset(blanks)

    # 2. geçiş — boş sayfalarla kromu oturt
    total = layout_pass(blanks)
    PLAN.resolve(total)
    d2 = Book(out)
    d2.build(story_flow(blanks), canvasmaker=EmbeddedOnlyCanvas)
    versos = sorted(n for n, pg in PLAN.civ_pages.items() if pg and pg % 2 == 0)
    try:
        os.remove(scratch)
    except OSError:
        pass
    return out, d2.page, len(blanks), versos


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description="İç blok PDF üretimi")
    E.add_argument(ap)
    ap.add_argument('--out', default=None)
    a = ap.parse_args()

    ed = E.get(a.edition)
    print(f"=== {ed.label} ({ed.slug}) ===")
    print(f"  trim   : {ed.trim_w}x{ed.trim_h} in")
    print(f"  marj   : iç {ed.gutter}\"  dış {ed.outer}\"  "
          f"üst {ed.top}\"  alt {ed.bottom}\"")
    print(f"  gövde  : {ed.body_pt} pt / {ed.lead_pt} pt satır aralığı")
    print(f"  metin  : {ed.text_w:.3f} x {ed.text_h:.3f} in  "
          f"({ed.lines_per_page} satır/sayfa)")

    path, n, nb, versos = build(a.edition, a.out)

    ok, req, slack = ed.gutter_ok(n)
    print()
    print(f"  sayfa       : {n}")
    print(f"  ön madde bitişi: {PLAN.front_end}   gövde başlangıcı: {PLAN.body_start}")
    print(f"  açılışlar   : {len(PLAN.no_head)}   recto için eklenen boş sayfa: {nb}")
    print(f"  verso'da kalan medeniyet açılışı: {versos or 'yok'}")
    print(f"  KDP iç marj : gereken {req:.3f}\"  bizimki {ed.gutter:.3f}\"  "
          f"pay {slack:+.3f}\"  → {'UYGUN' if ok else '⚠ YETERSİZ'}")
    prof = ed.profile
    in_range = prof.min_pages <= n <= prof.max_pages
    print(f"  sayfa sınırı: {prof.min_pages}–{prof.max_pages} "
          f"({prof.label})  → {'UYGUN' if in_range else '⚠ AŞILDI'}")
    print(f"  → {P.rel(path)}  ({os.path.getsize(path)/1e6:.2f} MB)")
    if not (ok and in_range):
        raise SystemExit(1)
