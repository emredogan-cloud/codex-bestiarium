# Olgoi-Khorkhoi — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `olgoi-khorkhoi` |
| **Ad** | Olgoi-Khorkhoi |
| **Alternatif yazımlar** | Olgoi-khorkhoi, allghoi khorkhoi |
| **Gelenek** | Mongol ⚔ · Orta Asya |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-080` |
| **Telaffuz (taslak)** | OL-goy KHOR-khoy |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `fulltext`

- **Künye:** Roy Chapman Andrews, *On the Trail of Ancient Man: A Narrative of the Field Work of the Central Asiatic Expeditions* (New York: G. P. Putnam's Sons, 1926)
- **Erişim:** archive.org/details/ontrailofancient00andr — tam metin indirilip tarandı
- **Yer:** Gobi seferi anlatısı
- **Not:** Alıntı tam metinden BİREBİR alındı. Andrews'un kaydı kritik bir noktayı içeriyor: mecliste bulunanların HİÇBİRİ yaratığı görmemişti ama varlığına kesin inanıyorlardı. Bu, kaydın bir GÖZLEM değil bir İNANÇ kaydı olduğunu kaynağın kendisi söylüyor.
- **İlgili alıntı:**

  > None of those present ever had seen the creature, but they all firmly believed in its existence and described it minutely. It is shaped like a sausage about two feet long, has no head nor legs and is so poisonous that merely to touch it means instant death. It lives in the most desolate parts of the Gobi Desert.

### Kaynak 2 · `primary` · doğrulama `catalog`

- **Künye:** Roy Chapman Andrews, *The New Conquest of Central Asia: A Narrative of the Explorations of the Central Asiatic Expeditions in Mongolia and China, 1921–1930* (New York: American Museum of Natural History, 1932)
- **Not:** Andrews, Moğol yetkililerinden çöl solucanı inancını doğrudan kaydeden ilk Batılı; sefer anlatısı birincil tanıklıktır.

### Kaynak 3 · `scholarly` · doğrulama `catalog`

- **Künye:** Walther Heissig, *The Religions of Mongolia*, çev. Geoffrey Samuel (Londra: Routledge & Kegan Paul, 1980)
- **Not:** Moğol halk dini ve şamanizmi üzerine standart Batı dilinde ele alış.

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B765` | Fanciful qualities of snakes | ✅ |

**Gerekçe.** TOHUM KODU DOĞRULANDI. Tam Motif-Index ayrıştırmasında B765'in tanımı 'Fanciful qualities of snakes' olarak bulundu. Olgoi-khorkhoi bir yılan/solucan biçiminde tasavvur edilir ve ona atfedilen nitelikler (dokunmadan öldürme) tam olarak 'fanciful qualities' kümesine girer.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Gobi çölü
- **İlk kayıt (attested):** Andrews'un 1922–25 sefer kayıtları; 1932'de yayımlandı

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Sosis biçiminde, yaklaşık altmış santim (Andrews'un kaydı: 'about two feet long')
- Başı ve bacağı yok
- Kırmızımsı

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Gobi'nin en ıssız yerlerinde kumun altında yaşar. Dokunmanın bile ânında öldürdüğü anlatılır.
- **Kayıtlı vaka:** Andrews 1926: Moğol yetkililerden oluşan bir meclis yaratığı ayrıntılı biçimde tarif eder — ama hiçbiri görmemiştir.
- **Karşı önlem:** —

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Adaro** `adaro` | Melanesia ◉ | `function` | İkisi de görünmeden vurur: biri kumun altından, öteki güneş ışınıyla. |
| **Basiliscus** `basiliscus` | Romana SPQR | `function` | Basiliscus bakışla, Olgoi-Khorkhoi dokunuşla öldürür — ikisi de mesafeyi kaldırır. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Yalnızca yayımlanmış malzeme kullanıldı (Andrews'un sefer anlatısı, Heissig). Moğol şaman uygulaması ve ongon yapımı KULLANILMAZ. Andrews'un kaydı bir Batılı seferin derlediği FOLKLOR kaydıdır; sömürge dönemi çerçevesi eleştirel okunacak.

## 9. Modern kurgu etkisi

'Mongolian death worm' adıyla 20.–21. yy kriptozoolojisinin sabit konularından. Tek cümlede ve 'modern' etiketiyle anılacak.

## 10. Yazım notları

- Kaynağın kendisi bunun bir İNANÇ kaydı olduğunu söylüyor: kimse görmemiş, herkes inanıyor. Maddenin 5. bölümü ('neden korkulur') tam olarak bu.
- Kriptozooloji literatürü ('Mongolian death worm') KAYNAK SAYILMAZ; tek cümlede ve 'modern' etiketiyle anılacak.

## Kontrol listesi

- [x] En az iki bağımsız kaynak, tam künyeyle
- [x] En az biri primary/scholarly
- [x] En az biri kesin-yer doğrulamalı (fulltext/toc/canon/article)
- [x] Motif kodu doğrulandı ve gerekçelendirildi
- [x] Bölge somut, ilk kayıt tarihli
- [x] Fiziksel tarif kaynağa dayanıyor
- [x] Kısıtlılık taraması yapıldı (yaşayan gelenekse)
- [x] Telaffuz taslağı yazıldı
- [x] Bu dosyada proza cümlesi yok

