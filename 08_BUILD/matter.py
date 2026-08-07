# -*- coding: utf-8 -*-
"""Front and back matter for CODEX MYTHOLOGICA. Original text written for this edition."""

TITLE     = "CODEX MYTHOLOGICA"
SUBTITLE  = "76 Myths from 19 Civilizations"
AUTHOR    = "Emre Doğan"
IMPRINT   = "Vâliçe Press"
YEAR      = "2026"
ISBN_LINE = "ISBN: [assigned by KDP at publication]"

# ─────────────────────────── FRONT MATTER ───────────────────────────

HALF_TITLE = [("h1", TITLE)]

TITLE_PAGE = [
    ("h1", TITLE),
    ("sub", SUBTITLE),
    ("gap", ""),
    ("author", AUTHOR),
    ("gap", ""),
    ("imprint", IMPRINT),
]

COPYRIGHT = [
    ("p", f"{TITLE}: {SUBTITLE}"),
    ("p", f"Copyright © {YEAR} by {AUTHOR}"),
    ("p", "All rights reserved."),
    ("p", "No part of this book may be reproduced, stored in a retrieval system, or transmitted "
          "in any form or by any means — electronic, mechanical, photocopying, recording, or "
          "otherwise — without the prior written permission of the copyright holder, except for "
          "brief quotations embodied in reviews and certain other noncommercial uses permitted "
          "by copyright law."),
    ("p", "The myths retold in this volume are drawn from the traditional oral and literary "
          "inheritance of nineteen cultures. Those traditions belong to no one and to everyone. "
          "The retellings in this book — their language, structure, emphasis, characterisation, "
          "and arrangement — are original work and are protected as such."),
    ("p", "The single quoted line from Hafez in “Jamshid’s Cup” appears in the "
          "translator’s own rendering and is drawn from a work long in the public domain."),
    ("p", f"First edition, {YEAR}"),
    ("p", ISBN_LINE),
    ("p", f"Published by {IMPRINT}"),
    ("p", "Cover art and design by the publisher."),
    ("p", "Set in Garamond and Cinzel."),
]

DEDICATION = [
    ("ded", "For everyone who was told a story before they could read one."),
]

# ─────────────────────────── INTRODUCTION ───────────────────────────

INTRODUCTION_TITLE = "On Reading These Stories"
INTRODUCTION = """Every culture that has ever existed has explained the same four or five things.

Where the world came from. Why we die. What the sun is doing when it is not overhead. Why the crops failed this year and not last year. What is owed to the dead, and by whom, and how soon. These are not sophisticated questions. They are the questions a child asks, and every civilisation has been obliged to answer them, and the answers are what we call mythology.

What is remarkable is not that the answers differ. It is how often they do not.

A god is torn apart and reassembled by a grieving wife in Egypt. A god is torn apart and reassembled by a grieving mother in Greece. In the Andes and in Ireland and on the Japanese archipelago, a hero descends into the land of the dead to fetch back someone he loves, is given a single condition, and breaks it. The rabbit that a Chinese poet sees on the face of the moon is also, independently, sitting on the moon in the reckoning of the Mexica, who never met a Chinese poet. Nobody arranged this. It simply happens, over and over, in cultures separated by oceans and by thousands of years, because the human predicament has a small number of shapes and the imagination keeps finding them.

This book contains seventy-six of those stories, drawn from nineteen traditions.

The selection is deliberately unbalanced in one direction and deliberately balanced in another. It is unbalanced because Greek myth gets more room than Inuit myth, and that is an honest reflection of how much has survived, not a judgement about what deserved to. It is balanced because I have refused to let the book become what most one-volume mythology collections quietly become, which is a Greek book with a Norse appendix. Nineteen traditions are here. Turkic, Inuit, Polynesian, Korean, Mayan, Persian, Slavic, West and Central African, Arabian: these are not filler at the back. They carry some of the strongest stories in the volume. If you read only the Greek chapters you will have read a good book and missed the point of this one.

A word about what these retellings are.

They are not translations. A translation has an original text standing behind it, and for most of what is here there is no original text — there is a tradition, which is a different thing: a body of tellings, variant and contradictory and alive, recorded at different centuries by different hands with different motives. Where a canonical literary source exists — Homer, the Kojiki, the Popol Vuh, the Shahnameh, the Mabinogion, the Epic of Gilgamesh — I have followed its spine and made no attempt to improve on it. Where the tradition is oral, or where the sources disagree, I have chosen the version that seemed to me the most complete rather than the most familiar, and I have said so in the afterword.

What I have not done is invent. There is no episode in this book that I made up. Where I have exercised judgement — and I have, constantly — it is in what to include, what to leave out, where to slow down and where to move quickly, and how a person in that world might actually have spoken. That last is the real work of a retelling. The myths as we have received them are frequently very compressed; a whole marriage can pass in a clause. Opening those clauses out into scenes, while keeping faith with what the tradition actually says happened, is the whole of the craft here.

Some of these stories are cruel. I have not softened them. Medusa is punished for a crime committed against her; Sedna's father cuts her fingers off one joint at a time; Rostam kills his own son on a plain because he would not give his name when the boy asked for it. These are not accidents of an unenlightened past that a modern retelling should quietly correct. They are load-bearing. The tradition is telling us something about power, and about how blame travels downhill, and it has been telling us for three thousand years. To sand that down would be to publish a more comfortable book and a less true one.

You do not need to read this in order.

Each story is complete in itself and can be read in ten or fifteen minutes. They are grouped by civilisation, and the civilisations run roughly by the antiquity of the surviving record, but nothing is lost by opening at random. Some readers will want to go straight to the tradition they grew up inside, to see whether I got it right. That is a fair test and I would encourage it.

If you read the book straight through, though, you will start noticing the rhymes. The flood is everywhere. The trickster who steals a necessary thing from a hoarding sky-god is everywhere — Prometheus with his fennel stalk, Anansi with his four impossible captures, Raven becoming a pine needle to be swallowed and reborn. The descent to the underworld to bargain for a life is everywhere, and it almost never works, and the almost is where the ache lives. The moment when a god or a hero is offered one small prohibition — do not look back, do not open the box, do not light the lamp — is everywhere, and the prohibition is always broken, because a story in which the prohibition is honoured is not a story anyone remembered to write down.

You will also notice where the rhymes stop. The Norse gods know exactly how and when they will die, and they put on their armour and walk out to meet it anyway; nobody else does that. The Egyptian afterlife is not a reward or a punishment but an audit, conducted courteously, with the ledger open. The Mesoamerican sun does not rise because it is the sun's nature to rise. It rises because gods threw themselves into a fire to start it, and it will stop if the debt is not kept up. There is no equivalent anywhere else in this book, and once you have understood it you understand something about the civilisation that believed it which no amount of description of its architecture will give you.

That is the argument of the book, to the extent that a book of stories is allowed one. We are more alike than we are comfortable admitting, and the places where we are genuinely not alike are more interesting than the places where we are.

Nineteen civilisations. Seventy-six myths. One human question, asked in every language that has ever been spoken, and answered — beautifully, and differently, and sometimes almost identically — every time.

Begin anywhere."""

NOTE_ON_NAMES_TITLE = "A Note on Names"
NOTE_ON_NAMES = """Nineteen traditions means nineteen writing systems, or the absence of one, and no system of transliteration will satisfy everybody.

I have used, throughout, the form most likely to be recognised by a reader in English, and I have been consistent within the book even where scholarship is not. Where a name has a settled English form, that form is used: Odin rather than Óðinn, Krishna rather than Kṛṣṇa, Quetzalcoatl rather than Quetzalcōātl. Where diacritics carry real information and cost the reader nothing, they are kept: Cú Chulainn, Þjálfi, Mictlantecuhtli, Yggdrasil, Sun Wukong.

Nothing in this book depends on pronouncing a name correctly. If you meet a name you cannot say, say it however you like and keep reading; you will be doing exactly what every listener around every fire has done for the whole history of these stories. But for readers who would like a rough guide, a few of the more resistant ones:

Yggdrasil — IG-druh-sil. Cú Chulainn — koo HULL-in. Quetzalcoatl — ket-sal-KWAT-ul. Xibalba — shee-BAL-buh. Nanahuatzin — nah-nah-WAHT-seen. Amaterasu — ah-mah-teh-RAH-soo. Susanoo — soo-sah-NO-oh. Hiranyakashipu — hi-RAN-ya-KASH-i-poo. Ereshkigal — eh-RESH-ki-gal. Utnapishtim — oot-nah-PISH-tim. Sekhmet — SEK-met. Simurgh — see-MORG. Jamshid — jam-SHEED. Sedna — SED-nuh. Mwindo — MWIN-doh. Shahmaran — shah-mah-RAHN. Fionnuala — fin-OO-la. Étaín — AY-deen. Baba Yaga — BAH-buh yuh-GAH. Tamamo-no-Mae — tah-MAH-mo-no-MAH-eh.

One special case. The Egyptian tale of the two brothers gives its elder brother the name Anubis, which is also the name of the jackal-headed god who attends the weighing of the heart three stories earlier. They are not the same figure. Egypt reused its names as freely as any country reuses John, and the text says so where it matters."""

# ─────────────────────────── BACK MATTER ───────────────────────────

AFTERWORD_TITLE = "Afterword: On Sources and Liberties"
AFTERWORD = """A reader is entitled to know where a book like this comes from.

For the traditions with a surviving literary spine, I have followed it. The Greek stories rest on Hesiod, Homer, the Homeric Hymns, Apollodorus and Ovid, with Ovid supplying the shape of Arachne and of Medusa's punishment. The Norse chapters follow the Poetic Edda and Snorri Sturluson's Prose Edda. The Japanese follow the Kojiki and Nihon Shoki, except Urashima Tarō and Tamamo-no-Mae, which come down through later collections. The Hindu chapters draw on the Mahabharata, the Ramayana, the Bhagavata Purana and the Vishnu Purana. The Mesopotamian follow the Standard Babylonian Epic of Gilgamesh and the Sumerian Descent of Inanna. The Mayan follow the Popol Vuh. The Persian follow Ferdowsi's Shahnameh. The Welsh follow the Mabinogion; the Irish, the Ulster Cycle and the Mythological Cycle. The Arabian draw on the Thousand and One Nights and on Nizami's Layla and Majnun.

For the traditions carried orally — Inuit, Polynesian, West and Central African, Turkic, and much of the Slavic and Korean material — there is no single authoritative text, and anyone who tells you otherwise is selling something. In those chapters I have worked from the ethnographic collections and from the versions that have circulated most widely, and I have chosen, where versions conflict, the one with the most internal coherence rather than the one with the earliest date.

Where I have taken liberties, they are these.

I have given people dialogue. Almost none of the sources do, or they do it so sparely that a scene is reported rather than shown. When Zeus and Prometheus speak to each other on the mountain, the exchange is mine; the positions they take are the tradition's.

I have chosen among variants without cluttering the page. Medusa has at least three incompatible origins in the ancient sources; I have told Ovid's, because it is the one that makes her a person. Theseus abandons Ariadne on Naxos for four different reasons depending on who is telling it; I have laid the reasons side by side and declined to choose, because the sources decline to choose. The Morrigan is one goddess or three depending on the manuscript, and I have said so in the text rather than pretending to a certainty nobody has.

I have compressed. The Mwindo epic takes Nyanga performers several days. The Journey to the West is a hundred chapters. The Shahnameh is longer than the Iliad and the Odyssey combined. What is here is a chapter, and a chapter is a doorway, not a house. If a story in this book makes you want the whole thing, the whole thing exists, and it is better than my summary of it.

I have not corrected the ethics. This bears repeating because it is the decision most likely to be mistaken for carelessness. Athena punishes a victim. Aoife curses four children out of ordinary jealousy. Sedna's father saves himself by drowning his daughter. A goddess is required to be stripped at seven gates because that is what the lower country charges everyone. The traditions knew these were monstrous — that is why the stories survived; nobody memorises a story about a fair world — and they left the monstrousness in for us to look at. So have I.

One last thing. There is a temptation, in a book that puts nineteen mythologies between the same two covers, to flatten them into a single system: to imply that every flood is the same flood and every trickster the same trickster and that we are all, underneath, telling one story. We are not. The similarities in this book are real and I have pointed at some of them. But the Aztec sun that must be fed, the Norse gods who walk knowingly into their own extinction, the Egyptian heart weighed honestly against a feather, the Yoruba smith who cleared the road and had to come back and demand his own credit — these are not local dialects of a universal myth. They are different answers, arrived at by different people, to a question we have all been asked. The differences are the reason to read nineteen of them instead of one.

I hope you find, somewhere in here, the story you did not know you had been missing."""

CIVILIZATION_NOTE_TITLE = "The Nineteen Traditions"

ABOUT_AUTHOR_TITLE = "About the Author"
ABOUT_AUTHOR = """%s writes about the stories that cultures tell themselves in order to keep going.

Trained as a software engineer, he came to mythology the way most people do — through a single story that would not leave him alone — and stayed for the pattern underneath. He reads in several languages, badly, and is grateful daily to the translators and ethnographers whose patient work made a book like this possible for someone who is neither.

He lives in Turkey.""" % AUTHOR

REVIEW_CTA_TITLE = "If You Enjoyed This Book"
REVIEW_CTA = """Independent books live or die on word of mouth. There is no publicity department behind this one.

If any of these stories stayed with you, the single most useful thing you can do is leave an honest review wherever you bought the book. It takes two minutes. It is read by the next person deciding whether to spend an evening with the Hero Twins or with Sedna at the bottom of the sea, and it matters far more than anything I could say about my own work.

If you found an error — a name misspelled, a variant I should have followed, a tradition I have misrepresented — I would genuinely like to know. Corrections are incorporated into later printings, and the reader who catches one is doing the book a service.

Thank you for reading."""

COLOPHON_TITLE = "Colophon"
COLOPHON = """The body text of this book is set in Garamond, a face descended from the sixteenth-century romans of Claude Garamond, chosen for its long history in the printing of classical texts and its comfort at length. Chapter titles and the civilisation openers are set in Cinzel, whose letterforms derive from Roman inscriptional capitals.

Ornamental breaks within stories are marked with three centred asterisks. Each story opens on a fresh page; each civilisation opens on a right-hand page.

The interior was typeset for a 6 × 9 inch trim with a gutter allowance appropriate to its extent."""
