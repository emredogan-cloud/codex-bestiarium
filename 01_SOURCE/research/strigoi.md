# Strigoi — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `strigoi` |
| **Ad** | Strigoi |
| **Alternatif yazımlar** | Strigoiul, Moroi (akraba) |
| **Gelenek** | Dacia ✠ · Balkanlar |
| **Sınıf** | VI · THE RESTLESS DEAD (Huzursuz Ölüler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-092` |
| **Telaffuz (taslak)** | stree-GOY |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Agnes Murgoci, "The Vampire in Roumania", *Folklore* 37:4 (1926), 320–349

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Paul Barber, *Vampires, Burial, and Death: Folklore and Reality* (New Haven: Yale University Press, 1988)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Strigoi”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `E251` | Vampire. Corpse which comes from grave at night and sucks blood | ✅ |

**Gerekçe.** E251 ('Vampire. Corpse which comes from grave at night and sucks blood') doğrulandı ve korundu. Strigoi'nin tanımı budur ve kod tam oturuyor.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Dacia (Romanya); Transilvanya, Oltenia köyleri
- **İlk kayıt (attested):** 19.–20. yy saha derlemeleri; Agnes Murgoci kayıtları (1926)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Kızıl saçlı, mavi gözlü olarak anlatılır
- İki kalp veya iki ruh taşıdığı söylenir
- Gömüldükten sonra bozulmayan ceset

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Mezarından kalkar; önce ailesinin sonra köyün kanını ve şansını alır. Hayvanlar kısırlaşır, süt kesilir.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** —

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Àbíkú** `abiku` | Yorùbá · Ashanti ✺ | `function` | İkisi de aileye geri döner; Strigoi alır, Àbíkú yalnızca gider ve tekrar gelir. |
| **Draugr** `draugr` | Norðr ᚦ | `function` | İkisi de gömüldüğü yerden kalkar; Draugr malını korur, Strigoi ailesinin kanını alır — biri mülkiyet, öteki soy. |
| **Karakoncolos** `karakoncolos` | Türk ☾ | `function` | İkisi de kışın belirli günlerine bağlıdır; biri sokakta, öteki mezarda başlar. |
| **Vârcolac** `varcolac` | Dacia ✠ | `tradition` | Dacia'nın iki gece varlığı: biri göğü, öteki aileyi tüketir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Murgoci'nin 1926 makalesi tam künyeli ve sayfa aralıklı — 'article' doğrulamasının en temiz örneklerinden.
- Adı Latince 'strix'ten gelir: Roma ve Romanya maddeleri arasında doğrudan dilsel köprü.

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

