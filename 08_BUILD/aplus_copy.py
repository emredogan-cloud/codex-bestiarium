"""
A+ MODÜL METİNLERİ — nihai üretim kopyası.
================================================================================
DİL NOTU
    Kitap İngilizce ve amazon.com'da İngilizce okura satılıyor; dolayısıyla
    MÜŞTERİYE GÖRÜNEN her metin İngilizcedir. Kapakta da aynı ilke uygulandı.
    Raporlar ve kod yorumları Türkçedir.

KAYNAK
    Her cümle ya kitabın kendi metninden damıtıldı ya da üretim raporunun
    onaylanmış konumlandırmasından geldi. Genel pazarlama dili kullanılmadı:
    "bestselling", "must-read", "unlock", "journey", "immerse yourself" gibi
    ifadeler bilinçli olarak yok. Yayıncılık kopyası iddia etmez, gösterir.

UZUNLUK DİSİPLİNİ
    Her metnin karakter bütçesi, o metnin gireceği kutunun ÖLÇÜLEN genişliğine
    göre belirlendi (bkz. aplus_layout.py). Sığmayan metin derlemeyi durdurur;
    sessizce kırpılmaz.
"""

from __future__ import annotations

# =============================================================================
# M1 — BAŞLIK ŞERİDİ  (970 × 300)
# =============================================================================
# Amaç: kapsamı tek bakışta kanıtla. Kaydırmayı durduran modül budur.

M1 = {
    "eyebrow": "CODEX MYTHOLOGICA",
    "headline": ["Nineteen traditions.", "One volume."],
    "subhead": "Seventy-six myths, each told in full.",
}

# =============================================================================
# M2 — BU KİTAP NEDİR / NE DEĞİLDİR / NASIL OKUNUR  (970 × 600, üç panel)
# =============================================================================
# Amaç: yanlış beklentiyle alan okuru elemek. İade oranını düşüren modül budur.
# Kaynak: kitabın kendi Giriş bölümü ("On Reading These Stories").

M2 = {
    "panels": [
        {
            "title": "WHAT THIS BOOK IS",
            "body": "Seventy-six myths from nineteen traditions, each retold "
                    "at full length — the way it would have been told beside "
                    "a fire. Ten to fifteen minutes a story.",
        },
        {
            "title": "WHAT IT IS NOT",
            "body": "Not a reference work. Not a dictionary of gods. Not a "
                    "book of summaries. Nothing here was invented, and "
                    "nothing cruel has been softened.",
        },
        {
            "title": "HOW TO READ IT",
            "body": "Begin anywhere; every story stands alone. Read straight "
                    "through and the rhymes surface — the flood, the "
                    "trickster, the descent, the broken prohibition.",
        },
    ],
}

# =============================================================================
# M3 — KARŞILAŞTIRMA  (970 × 600, üç kaide)
# =============================================================================
# UYUMLULUK NOTU (raporda da işaretlendi):
#   Amazon A+ kuralları RAKİP ÜRÜN karşılaştırmasını yasaklar. Aşağıdaki metin
#   hiçbir marka, yazar veya kitap adı geçirmez; yalnızca KİTAP TÜRLERİNİ
#   tarif eder ve iddiaların hepsi bu kitabın kendi doğrulanabilir nitelikleri
#   üzerinedir. Bu ayrım kasıtlıdır. Yine de yayından önce gözden geçirin.

M3 = {
    "headline": "Where this one sits",
    "columns": [
        {
            "label": "SUMMARY COLLECTIONS",
            "lines": ["One tradition, or two",
                      "A plot in a paragraph",
                      "Read once, then shelved"],
        },
        {
            "label": "CODEX MYTHOLOGICA",
            "lines": ["Nineteen traditions",
                      "Seventy-six full retellings",
                      "329 pages"],
            "emphasis": True,
        },
        {
            "label": "SCHOLARLY EDITIONS",
            "lines": ["Apparatus and footnotes",
                      "Written for specialists",
                      "Consulted, not read"],
        },
    ],
}

# =============================================================================
# M4 — METİNDEN BİR BÖLÜM  (970 × 600)
# =============================================================================
# Amaç: üslup örneği. Edebî kurguda satın alma kararını SES verir.
# Kaynak: "Prometheus the Firebringer", kitabın 1. bölümü — birebir alıntı.

M4 = {
    "eyebrow": "FROM THE OPENING CHAPTER",
    "quote": "Prometheus loved them. He could not have told you why. "
             "Perhaps it was that they were the only creatures who looked up.",
    "attrib": "PROMETHEUS THE FIREBRINGER",
    "note": "Seventy-five more, from Sedna to Sun Wukong.",
}

# =============================================================================
# M5 — İÇ SAYFALAR  (970 × 600)
# =============================================================================
# Amaç: dizgi kalitesini göster; koleksiyonluk algısını pekiştir.
# İddiaların hepsi ölçülebilir ve doğrudur (bkz. 04_PRINT interior PDF).

M5 = {
    "eyebrow": "INSIDE THE BOOK",
    "captions": [
        "Nineteen civilisations, each opening on its own page.",
        "EB Garamond, set 11.2 on 15.6 — built for long reading.",
        "329 pages. No footnotes, no apparatus, nothing between you "
        "and the story.",
    ],
}

# =============================================================================
# ERİŞİLEBİLİRLİK — Amazon alt metin alanları
# =============================================================================
# Amazon her A+ görseli için alternatif metin ister. Boş bırakmak hem
# erişilebilirlik hem indeksleme kaybıdır. Anahtar kelimeler doğal biçimde
# geçirildi; anahtar kelime yığma yapılmadı.

ALT_TEXT = {
    "m1-header": "Codex Mythologica — an illuminated mythological calendar "
                 "wheel ringed by nineteen civilisation medallions.",
    "m2-what-it-is": "An open illustrated volume of world mythology on a "
                     "scholar's desk beside a candle, compass and wax seal.",
    "m3-comparison": "Three museum plinths in a dark gallery; the Codex "
                     "Mythologica stands lit at the centre.",
    "m4-quotation": "An open book of myths beside a bronze zodiac disc, a "
                    "candle and a quill on a carved stone ledge.",
    "m5-interior": "Three interior spreads from Codex Mythologica showing "
                   "civilisation opening pages and engraved plates.",
}

# =============================================================================
# YAZAR BİYOGRAFİSİ  (Author Central — A+ değil, ama aynı yerde durması iyi)
# =============================================================================

AUTHOR_BIO = (
    "Emre Doğan writes about the stories that cultures tell themselves in "
    "order to keep going. Trained as a software engineer, he came to "
    "mythology the way most people do — through a single story that would "
    "not leave him alone — and stayed for the pattern underneath. "
    "CODEX MYTHOLOGICA, his first book, gathers seventy-six myths from "
    "nineteen traditions and retells each one in full. He lives in Turkey."
)

MODULE_COPY = {
    "m1-header": M1, "m2-what-it-is": M2, "m3-comparison": M3,
    "m4-quotation": M4, "m5-interior": M5,
}


def word_count(o) -> int:
    if isinstance(o, str):
        return len(o.split())
    if isinstance(o, list):
        return sum(word_count(x) for x in o)
    if isinstance(o, dict):
        return sum(word_count(v) for k, v in o.items()
                   if k not in ("emphasis",))
    return 0


if __name__ == "__main__":
    for k, v in MODULE_COPY.items():
        print(f"\n═══ {k}  ({word_count(v)} kelime)")
        for kk, vv in v.items():
            if isinstance(vv, list) and vv and isinstance(vv[0], dict):
                for p in vv:
                    ttl = p.get("title") or p.get("label")
                    txt = p.get("body") or " · ".join(p.get("lines", []))
                    print(f"   {ttl}")
                    print(f"      {txt}  [{len(txt)} kr]")
            elif isinstance(vv, list):
                for x in vv:
                    print(f"   {kk}: {x}  [{len(x)} kr]")
            else:
                print(f"   {kk}: {vv}  [{len(str(vv))} kr]")
    print(f"\nalt metinler: {len(ALT_TEXT)} · yazar biyografisi "
          f"{word_count(AUTHOR_BIO)} kelime")
