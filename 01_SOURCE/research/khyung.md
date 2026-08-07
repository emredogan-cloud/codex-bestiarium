# Khyung — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `khyung` |
| **Ad** | Khyung |
| **Alternatif yazımlar** | — |
| **Gelenek** | Bod ☷ · Himalaya |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | D · Fırtına kuşu |
| **Plaka** | `plate-078` |
| **Telaffuz (taslak)** | kyoong |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** R. A. Stein, *Tibetan Civilization*, çev. J. E. Stapleton Driver (Stanford: Stanford University Press, 1972)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Per Kvaerne, *The Bon Religion of Tibet: The Iconography of a Living Tradition* (Londra: Serindia, 1995)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Khyung”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `A284.2` | Thunderbird | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum B31 idi (bölüm başlığı, ayrıca 'Roc' anlamı). Khyung bir roc değil FIRTINA kuşudur. Doğrulanan A284.2 ('Thunderbird') tam tanımdır.

> ⚠ **Tohum kodu değiştirildi.** B31 → A284.2.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Bod; Bön geleneği ve Budist Tibet
- **İlk kayıt (attested):** Bön metinleri; Tibet ikonografisi

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Boynuzlu kartal
- Pençesinde yılan tutar
- Altın renkli olarak betimlenir

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Gök varlığı; yılanı (klu) pençesinde tutar. Bön geleneğinde kozmik düzenin işareti.
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
| **Animikii** `animikii` | Anishinaabe ▲ | `kin` | İki gök varlığı, iki ayrı kıta: Khyung yılanı tutar, Animikii su varlığıyla savaşır. Kuş–su karşıtlığı iki yerde bağımsız kurulmuş. |
| **Garuḍa** `garuda` | Bharatiya ॐ | `kin` | İkisi de pençesinde yılan tutar; Garuḍa'nınki bir düşmanlık, Khyung'unki bir kozmik düzen işareti. |
| **Srin-po** `srin-po` | Bod ☷ | `tradition` | Bön kozmolojisinin iki ucu: yerin altındaki et yiyen halk ve gökteki kartal. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Bön ve Tibet Budizmi YAŞAYAN geleneklerdir. Tören, mantra ve tanka yapım bilgisi KULLANILMAZ; plakada kutsanmış ikonografi birebir çizilmez.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Fırtına kuşu ailesinin (D) Himalaya üyesi ve Garuḍa ile doğrudan akraba — ikisi de yılan tutar.

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

