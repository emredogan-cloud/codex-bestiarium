# Lóng — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `long` |
| **Ad** | Lóng |
| **Alternatif yazımlar** | Lung (Wade-Giles) |
| **Gelenek** | Zhōnghuá 龍 · Doğu Asya |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-028` |
| **Telaffuz (taslak)** | LOONG |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** *Shanhaijing* (Dağlar ve Denizler Kitabı)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Anne Birrell, *Chinese Mythology: An Introduction* (Baltimore: Johns Hopkins University Press, 1993)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Lung”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B11.7` | Dragon as rain-spirit | ✅ |

**Gerekçe.** B11.7 ('Dragon as rain-spirit') doğrulandı ve korundu. Çin ejderhasını Batı ejderhasından ayıran şey tam olarak budur: yağmur ve su denetimi.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Zhōnghuá; ırmaklar, göller, bulutlar
- **İlk kayıt (attested):** *Shanhaijing* (MÖ 4.–1. yy); Han dönemi kayıtları; Wang Chong, *Lunheng* (MS 1. yy)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Kanatsız ama uçan
- Geyik boynuzu, deve başı, tavşan gözü, yılan boynu (Wang Fu'nun dokuz benzerlik listesi)
- Pençesinde inci

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Yağmuru getirir; ırmakları yönetir. Kuraklıkta ejderha kralına yakarılır.
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
| **Húli jīng** `huli-jing` | Zhōnghuá 龍 | `tradition` | Zhōnghuá'nın iki uzun ömürlüsü: Lóng zamanla yükselir, húli jīng zamanla insanlaşır. |
| **Imugi** `imugi` | Hangug 단 | `function` | Lóng olunmuş hâldir, Imugi olunamamış — aynı basamağın iki ucu. |
| **Phaya Nak** `phaya-nak` | Siam ☸ | `function` | İkisi de yağmurun ve ırmağın yöneticisidir; Lóng'a kuraklıkta yakarılır, Phaya Nak yılda bir ateş topu gönderir. |
| **Qílín** `qilin` | Zhōnghuá 龍 | `tradition` | Zhōnghuá'nın iki hayırlı varlığı: biri yağmuru, öteki adaleti haber verir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Batı ejderhasıyla karşıtlık maddenin 5. bölümünün çekirdeği: biri hazine yığar, diğeri yağmur dağıtır.

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

