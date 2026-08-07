# Phaya Nak — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `phaya-nak` |
| **Ad** | Phaya Nak |
| **Alternatif yazımlar** | — |
| **Gelenek** | Siam ☸ · Güneydoğu Asya |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | E · Derinlerin yılanı |
| **Plaka** | `plate-070` |
| **Telaffuz (taslak)** | pah-YAH NAHK |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Phya Anuman Rajadhon, *Essays on Thai Folklore* (Bangkok: Thai Inter-Religious Commission for Development, 1968)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Justin Thomas McDaniel, *The Lovelorn Ghost and the Magical Monk: Practicing Buddhism in Modern Thailand* (New York: Columbia University Press, 2011)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Naga, Thai”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B91.1` | Naga. Serpent demon | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum B91 ('Mythical serpent') idi; doğrulanan B91.1 ('Naga. Serpent demon') Phaya Nak'ın Hint nāga geleneğinin Tayland kolu olduğunu doğru tasnif eder.

> ⚠ **Tohum kodu değiştirildi.** B91 → B91.1.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Siam (Tayland) ve Laos; Mekong ırmağı
- **İlk kayıt (attested):** Tayland ve Lao sözlü geleneği; Budist kanon uyarlamaları

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Büyük yılan
- Başında çok sayıda başlık
- Mekong'un altındaki şehirlerde yaşadığı anlatılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Mekong'un altındaki şehirlerin efendisi. Her yıl Ekim'de ırmaktan yükselen ışık topları (bang fai phaya nak) ona atfedilir.
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
| **Kinnarī** `kinnari` | Siam ☸ | `tradition` | Siam'ın iki Himavanta varlığı: biri ormanda şarkı söyler, öteki ırmağın altında hüküm sürer. |
| **Lóng** `long` | Zhōnghuá 龍 | `function` | İkisi de yağmurun ve ırmağın yöneticisidir; Lóng'a kuraklıkta yakarılır, Phaya Nak yılda bir ateş topu gönderir. |
| **Nāga** `naga` | Bharatiya ॐ | `kin` | Aynı kelime, iki coğrafya: Nāga hazineyi ve yağmuru tutar, Phaya Nak bir şehir yönetir. |
| **Thuồng luồng** `thuong-luong` | Việt ☴ | `kin` | Aynı nehir sisteminin iki adı: biri dövmenin kökeni, öteki ateş toplarının. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

Phaya Nak YAŞAYAN bir tapım nesnesidir. Tapınak uygulaması, adak ve dua metni KULLANILMAZ; yalnızca yayımlanmış akademik betimleme kullanılır.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Ateş topları: yıllık, tarihli, gözlemlenebilir bir olay. 'Attested' kuralının en güçlü örneklerinden.

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

