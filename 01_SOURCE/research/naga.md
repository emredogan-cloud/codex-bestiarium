# Nāga — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `naga` |
| **Ad** | Nāga |
| **Alternatif yazımlar** | — |
| **Gelenek** | Bharatiya ॐ · Güney Asya |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | E · Derinlerin yılanı |
| **Plaka** | `plate-014` |
| **Telaffuz (taslak)** | NAH-gah |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Mahabharata*
- **Yer:** I (Ādi Parva), Astika Parva

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** J. Ph. Vogel, *Indian Serpent-Lore, or The Nāgas in Hindu Legend and Art* (Londra: Arthur Probsthain, 1926)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Naga”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B91.1` | Naga. Serpent demon | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum B91 ('Mythical serpent') idi; doğrulanan B91.1'in tanımı doğrudan 'Naga. Serpent demon' — kod bu maddenin adını taşıyor.

> ⚠ **Tohum kodu değiştirildi.** B91 → B91.1 (daha dar ve adı taşıyan kod).

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Bharat; su altı şehirleri (Pātāla), göl ve ırmaklar
- **İlk kayıt (attested):** *Mahabharata*; *Atharvaveda*; Buddhist Pali kanonu

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Yılan biçiminde; kimi zaman insan üst gövdeli
- Başında çok sayıda başlık (çoğunlukla yedi)
- Boynunda mücevher

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Suyun altındaki şehirlerde yaşar; hazineyi ve yağmuru tutar. Garuḍa'nın avıdır.
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
| **Imugi** `imugi` | Hangug 단 | `kin` | Nāga zaten bir halktır; Imugi tek başına ve bekleyendir. Biri düzen, öteki eşik. |
| **Makara** `makara` | Bharatiya ॐ | `tradition` | Bharatiya'nın iki su varlığı: Makara eşiği süsler, Nāga suyun altında yaşar. |
| **Phaya Nak** `phaya-nak` | Siam ☸ | `kin` | Aynı kelime, iki coğrafya: Nāga hazineyi ve yağmuru tutar, Phaya Nak bir şehir yönetir. |
| **Şahmeran** `sahmeran` | Türk ☾ | `function` | İkisi de yılanların yönetimidir; Şahmeran bilgiyi taşır ve o bilgi yüzünden ölür, Nāga hazineyi taşır. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Derinlerin yılanı ailesinin (E) Güney Asya üyesi ve tek TOPLUM kuran üyesi.

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

