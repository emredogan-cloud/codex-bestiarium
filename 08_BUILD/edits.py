# -*- coding: utf-8 -*-
"""Editorial fixes for CODEX MYTHOLOGICA. Every change is logged."""
EDITS = [
 # (story_id, before, after, category, rationale)
 ("prometheus",
  "Cook your meat. Soften your iron.",
  "Cook your meat. Harden your spear-points.",
  "Fact — anachronism",
  "Iron-working postdates the fire-gift myth by millennia; fire-hardened spear points are period-correct and keep the imperative rhythm."),

 ("sekhmet",
  "barley beer, eight times distilled",
  "barley beer, eight times brewed",
  "Fact — anachronism",
  "Distillation was unknown in pharaonic Egypt. Egyptian beer was brewed, and strength came from repeated brewing."),

 ("susanoo-orochi",
  "They brewed the rice-spirit eight times distilled,",
  "They brewed the rice-spirit eight times refined,",
  "Fact — anachronism",
  "The Kojiki specifies yashiori no sake, 'eight-fold refined' sake. Sake is brewed, never distilled."),

 ("cu-chulainn",
  "held a magical spear, the Gáe Bolg of his own crafting, and he called out",
  "held one of the three enchanted spears forged by the children of Calatín, and he called out",
  "Fact — mythological error",
  "The Gáe Bolg is Cú Chulainn's own weapon, given him by Scáthach. Lugaid killed him with spears made by Calatín's children."),

 ("princess-bari",
  "She had been gone twenty-one years.",
  "She had been gone twenty-one years: three on the long road west, and eighteen in the keeper's service.",
  "Consistency — arithmetic",
  "Three plus three plus three plus nine is eighteen, not twenty-one. The road accounts for the remainder."),

 ("bran-blessed",
  "there is a saying, much older than the present queen,",
  "there is a saying, much older than the present reign,",
  "Fact — dated reference",
  "The British monarch is no longer a queen; 'reign' is durable and will not date again."),

 ("ocean-of-milk",
  "Then came Kalpavriksha, the wishing-tree, planted itself on the shore.",
  "Then came Kalpavriksha, the wishing-tree, which planted itself on the shore.",
  "Grammar",
  "Missing relative pronoun left the sentence without a finite main verb."),

 ("shiva-tandava",
  "He performs it on a small drum.",
  "He performs it to the beat of a small drum.",
  "Grammar / sense",
  "He dances to the drum; he does not perform on it."),

 ("morrigan",
  "She had, at last, been healed by the only man whose curse would have healed her.",
  "She had, at last, been healed by the only man whose blessing could have healed her.",
  "Sense",
  "It was his three blessings that healed her; 'curse' inverted the meaning."),

 ("simurgh",
  "Many years later, in the matter of Rostam's son Sohrab, Zal would burn a second feather. The Simurgh would come again. She would heal.",
  "Many years later, when Rostam lay wounded after his duel with Esfandiyar, Zal would burn a second feather. The Simurgh would come again. She would heal him, and tell him where his enemy could be struck.",
  "Fact + internal contradiction",
  "In the Shahnameh the second feather is burned for Rostam's wounds after Esfandiyar, not for Sohrab. As written it also contradicted the next story, in which Sohrab dies unsaved."),

 ("jade-emperor",
  "who had hidden in the shoe of the horse",
  "who had coiled herself around the hoof of the horse",
  "Fact — anachronism",
  "Horseshoes are anachronistic here; the traditional tale has the snake wound about the hoof."),

 ("hel",
  "sails north on a ship of her own building. Her ship is called Naglfar, and it is built from the untrimmed nails of dead men,",
  "sails north on the ship her long kingdom has been building all along. The ship is called Naglfar, and it is made from the untrimmed nails of dead men,",
  "Internal contradiction",
  "Paired with the change below, this reconciles Hel's chapter with the Ragnarok chapter, where Loki takes the helm."),

 ("hel",
  "She is the captain of that ship. The dead of her kingdom",
  "Her father takes the helm; the ship, and its long cargo, are hers. The dead of her kingdom",
  "Internal contradiction",
  "'Ragnarok' places Loki at the helm of Naglfar. Ownership stays with Hel; command goes to Loki, and both chapters now agree."),

 ("shiva-tandava",
  "in his hall on Mount Kailash",
  "in his hall on Mount Kailasa",
  "Consistency — spelling",
  "'Ganga' uses Kailasa; one spelling per book."),

 ("maize-people",
  "they became, the priests said, the monkeys you can still see in the high jungle, who remember dimly what it was to be people but cannot quite recover the language.",
  "they became, the priests said, the long-tailed monkeys of the forest canopy, who remember dimly what it was to be people but cannot quite recover the language.",
  "Repetition",
  "The identical clause 'the monkeys you can still see in the high jungle' already appears in 'The Five Suns'. The shared motif is genuine; the shared sentence was not."),

 ("two-brothers",
  "Anubis was the elder. Bata was the younger.",
  "Anubis was the elder. Bata was the younger. (This Anubis is a farmer and a mortal man, not the jackal-headed god who waits at the scales; Egypt reused its names without embarrassment.)",
  "Clarity",
  "Readers meet the god Anubis three stories earlier. Without a word of guidance the same name on a farmer reads as an error."),
]
