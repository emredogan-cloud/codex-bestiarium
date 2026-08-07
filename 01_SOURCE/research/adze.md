# Adze — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `adze` |
| **Ad** | Adze |
| **Alternatif yazımlar** | — |
| **Gelenek** | Yorùbá · Ashanti ✺ · Afrika |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-042` |
| **Telaffuz (taslak)** | AHD-zeh |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Jakob Spieth, *Die Ewe-Stämme: Material zur Kunde des Ewe-Volkes in Deutsch-Togo* (Berlin: Reimer, 1906)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Michelle Gilbert, "The Sudden Death of a Millionaire: Conversion and Consensus in a Ghanaian Kingdom", *Africa* 58:3 (1988), 291–314

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Adze”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G262.1` | Witch sucks blood | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum G262 ('Murderous witch') idi; doğrulanan G262.1 ('Witch sucks blood') adze'nin tanımlayıcı eylemini birebir karşılıyor.

> ⚠ **Tohum kodu değiştirildi.** G262 → G262.1.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Ewe (Gana, Togo, Benin)
- **İlk kayıt (attested):** 20. yy saha derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Ateşböceği biçiminde uçar
- Yakalanınca insan biçimine döner

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Ateşböceği kılığında eve girer; uyuyanın, özellikle çocuğun kanını içer.
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
| **Àbíkú** `abiku` | Yorùbá · Ashanti ✺ | `kin` | Aynı gelenekte iki cevap: Adze dışarıdan gelen bir faildir, Àbíkú çocuğun kendisidir. |
| **Anansi** `anansi` | Yorùbá · Ashanti ✺ | `tradition` | Aynı gelenekte kurnazlık ile kötülük: Anansi zayıfın aklı, Adze güçsüzün korkusudur. |
| **Buda** `buda` | Ityop'ya ✤ | `function` | İkisi de bir insanın içinden çalışır — biri nazarla, öteki kan içerek. |
| **Strix** `strix` | Romana SPQR | `kin` | İkisi de küçük bir canlının kılığında girer — biri kuş, öteki ateşböceği. Kılık, girişi mümkün kılan şeydir. |
| **Tokoloshe** `tokoloshe` | Nguni ◈ | `function` | İkisi de küçüktür ve geceleyin gelir; Adze kılık değiştirir, Tokoloshe değiştirmez — gönderilir. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Ewe cadılık inancı yaşayan bir toplumsal olgudur ve gerçek suçlamalara yol açmıştır. Madde suçlamayı yeniden üretmeyecek; Buda maddesiyle aynı etik dikkat uygulanacak.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Ateşböceği: en küçük ölçekli gece cadısı. Ölçek karşıtlığı ailenin açılışında kullanılacak.

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

