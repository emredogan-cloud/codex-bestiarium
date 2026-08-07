# Sīmurgh — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `simurgh` |
| **Ad** | Sīmurgh |
| **Alternatif yazımlar** | Simorgh, Senmurv, Saēna |
| **Gelenek** | Pārs 𐎩 · Yakın Doğu |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | D · Fırtına kuşu |
| **Plaka** | `plate-043` |
| **Telaffuz (taslak)** | see-MOORG |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Firdevsî, *Şahnâme*
- **Yer:** Zal ve Rüstem bölümleri

### Kaynak 2 · `primary` · doğrulama `canon`

- **Künye:** *Avesta*
- **Yer:** Yašt 14

### Kaynak 3 · `scholarly` · doğrulama `catalog`

- **Künye:** Arthur Christensen, *Les Kayanides* (Kopenhag: Høst, 1931)

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B31.5` | Simorg: giant bird | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum B31 idi (bölüm başlığı). Doğrulanan B31.5'in tanımı doğrudan 'Simorg: giant bird' — kod bu maddenin adını taşıyor.

> ⚠ **Tohum kodu değiştirildi.** B31 → B31.5. Ayrıntı: SCOPE_DECISIONS.md § 5②.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Pārs; Elburz dağı (Alborz)
- **İlk kayıt (attested):** *Avesta* (Yašt 14, saēna kuşu); Firdevsî, *Şahnâme* (1010)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Devasa kuş; kanat açıklığı bulutu kaplar
- Tüyü şifa verir
- Köpek başlı olarak da betimlenir (erken kayıt)

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Zal'ı Elburz'da büyütür. Tüyü yakıldığında gelir; Rüstem'in doğumunda ve Isfendiyar'la savaşında yol gösterir.
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
| **Anzû** `anzu` | Sumer 𒀭 | `kin` | Anzû kader tabletlerini ÇALAR; Sīmurgh bir çocuğu büyütür ve yol gösterir. Aynı kanat, hırsız ve bilge. |
| **Bennu** `bennu` | Kemet 𓂀 | `kin` | Bennu zamanın başlangıcını işaretler, Sīmurgh bir ömrü taşır — biri kozmik takvim, öteki kişisel kader. |
| **Garuḍa** `garuda` | Bharatiya ॐ | `kin` | Sīmurgh çağrılır (tüy yakılır), Garuḍa binilir. Biri danışman, öteki taşıt. |
| **Perī** `peri` | Pārs 𐎩 | `tradition` | Pars'ın iki yardımcısı: biri kararsız, öteki güvenilir — kitabın ikisini de aynı geleneğe borçlu olması tesadüf değil. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Fırtına kuşu ailesinin (D) tek BİLGE üyesi ve kapak adayı.

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

