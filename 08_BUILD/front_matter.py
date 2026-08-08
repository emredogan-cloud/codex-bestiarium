#!/usr/bin/env python3
"""
CODEX BESTIARIUM — YAPISAL ÖN MADDE
================================================================================
Yarım başlık, başlık sayfası, künye, ithaf ve içindekiler başlığı.

    NEDEN BURADA VE NEDEN DEPODA
    ────────────────────────────
    Bu metinler kitabın PROZASI DEĞİLDİR. Manuscript (madde metni, açılışlar,
    giriş, sonsöz) depo dışında yaşar (karar A1/D29). Künye sayfası, telif
    beyanı ve AI beyanı ise ÜRETİM YAPILANDIRMASIDIR: her baskıda birebir
    aynı çıkmak zorundadır, hukuki sonuç doğurur ve gözle yazılırsa bir gün
    birinde eksik kalır.

    Cilt 1'de aynı ayrım aynı biçimde yapılmıştı (`matter.py`).

    AI BEYANI KÜNYE SAYFASINDADIR ve bu bilinçlidir. KDP yükleme formundaki
    kutuyu işaretlemek ayrı bir iştir ve onu da yapmak gerekir; ama okurun
    gördüğü yerde de yazılı olmalıdır. Yol haritası Faz 6 · DoD 6: "AI
    beyanı işaretlendi: metin AI destekli · kapak AI üretimi ·
    illüstrasyonlar AI üretimi."
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bestiarium import (  # noqa: E402
    AUTHOR,
    BOOK_SUBTITLE,
    BOOK_TITLE,
    IMPRINT,
    SERIES,
    TARGET_CREATURES,
    TARGET_TRADITIONS,
    VOLUME,
)

YEAR = "2026"
ISBN_LINE = "ISBN: [KDP tarafından yayında atanır]"

HALF_TITLE = BOOK_TITLE.upper()

TITLE_PAGE = {
    "title": BOOK_TITLE.upper(),
    "subtitle": "A World Bestiary",
    "line": (f"{TARGET_CREATURES} Legendary Creatures "
             f"from {TARGET_TRADITIONS} Traditions"),
    "author": AUTHOR,
    "series": f"{SERIES} · Volume {VOLUME}",
    "imprint": IMPRINT,
}

COPYRIGHT = [
    f"{BOOK_TITLE}: {BOOK_SUBTITLE}",
    f"Copyright © {YEAR} by {AUTHOR}",
    "All rights reserved.",

    "No part of this book may be reproduced, stored in a retrieval system, "
    "or transmitted in any form or by any means — electronic, mechanical, "
    "photocopying, recording, or otherwise — without the prior written "
    "permission of the copyright holder, except for brief quotations "
    "embodied in reviews and certain other noncommercial uses permitted by "
    "copyright law.",

    "The creatures described in this volume are drawn from the traditional "
    "oral and literary inheritance of forty cultures. Those traditions "
    "belong to no one and to everyone. The descriptions, classification, "
    "comparisons, arrangement and language of this book are original work "
    "and are protected as such.",

    "Where a tradition represented here is living, only published and "
    "unrestricted material has been used. Ceremonial knowledge, initiation "
    "material and practitioner procedure are named as withheld and are not "
    "reproduced. Australian Aboriginal traditions are not included, and the "
    "reason is set out in the closing note.",

    "Sources are named at the foot of every entry. Every creature in this "
    "volume is attested in at least two independent published records.",

    "AI disclosure: the text of this book was written with AI assistance "
    "and edited by the author. The cover art and the interior plates were "
    "generated with AI tools and prepared for print by the author.",

    f"First edition, {YEAR}",
    ISBN_LINE,
    f"Published by {IMPRINT}",
    "Set in Cinzel and EB Garamond.",
]

DEDICATION = "For everyone who checked the water before they got in."

# İçindekiler ve gelenek haritası başlıkları — kitapta basılır.
CONTENTS_TITLE = "Contents"
MAP_TITLE = "Forty Traditions"
MAP_NOTE = (
    "The forty traditions represented in this book, grouped by region, with "
    "the number of creatures filed under each. A tradition is named in the "
    "heading of every entry that belongs to it, so a reader who arrives "
    "through a region can start here and follow the names."
)
SOURCES_TITLE = "Sources"
SOURCES_NOTE = (
    "The short citation printed at the foot of each entry, gathered here by "
    "tradition. Full bibliographic detail, the verification level of every "
    "citation, and the reasoning behind every motif code are held in the "
    "project’s public research record."
)
INDEX_TITLES = {
    "traditions": "Index of Traditions",
    "motifs": "Index of Motifs",
    "kin": "The Eight Kin Images",
    "pronunciation": "Pronunciation Guide",
}
INDEX_NOTES = {
    "traditions": "Every tradition in the book, with its creatures and their "
                  "pages.",
    "motifs": "Every Thompson motif code used in this book, with the entries "
              "that carry it. The fastest way to find unexpected neighbours.",
    "kin": "The eight images that recur across unconnected traditions, with "
           "their members and the point on which the traditions disagree.",
    "pronunciation": "An approximation for an English-speaking reader, not a "
                     "phonetic transcription. Alternative spellings are "
                     "cross-referenced.",
}
