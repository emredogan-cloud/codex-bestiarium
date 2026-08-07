# Animikii — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `animikii` |
| **Ad** | Animikii |
| **Alternatif yazımlar** | Animikii-binesi, Thunderbird |
| **Gelenek** | Anishinaabe ▲ · Kuzey Amerika |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | D · Fırtına kuşu |
| **Plaka** | `plate-102` |
| **Telaffuz (taslak)** | ah-nee-MEE-kee |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** *The Jesuit Relations and Allied Documents* (Cleveland: Burrows, 1896–1901)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Christopher Vecsey, *Traditional Ojibwa Religion and Its Historical Changes* (Philadelphia: American Philosophical Society, 1983)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Thunderbird”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `A284.2` | Thunderbird | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum B31.1 ('Roc') idi — animikii yük taşıyan dev kuş değil GÖK GÜRÜLTÜSÜ kuşudur. Doğrulanan A284.2 ('Thunderbird') tam tanımdır.

> ⚠ **Tohum kodu değiştirildi.** B31.1 → A284.2.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Anishinaabe; Yukarı Göller bölgesi
- **İlk kayıt (attested):** Cizvit Relations (17. yy); 19.–20. yy derlemeler

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Dev kuş
- Kanat çırpışı gök gürültüsü
- Gözlerinden şimşek

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Gök gürültüsünü getirir. Su varlıklarının — özellikle Mishipeshu'nun — ezelî karşıtı.
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
| **Impundulu** `impundulu` | Nguni ◈ | `kin` | Animikii gök gürültüsünü GETİRİR; Impundulu şimşeği ÇAĞIRIR ve bir insana bağlıdır — biri hava, öteki sahiplik. |
| **Khyung** `khyung` | Bod ☷ | `kin` | İki gök varlığı, iki ayrı kıta: Khyung yılanı tutar, Animikii su varlığıyla savaşır. Kuş–su karşıtlığı iki yerde bağımsız kurulmuş. |
| **Mishipeshu** `mishipeshu` | Anishinaabe ▲ | `pair` | Ezelî karşıtlar: biri suyun altında bakırı korur, öteki gökten gürler. Kitabın tek doğrudan düşman çifti. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

⚠ Anishinaabe gelenekleri yaşayandır. Midewiwin bilgisi, tören ve klan (doodem) işareti KULLANILMAZ; plakada klan işareti çizilmez.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Fırtına kuşu ailesinin (D) Kuzey Amerika üyesi. Ayrışma: tek KARŞITI olan üye — düşmanı adı konmuş.

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

