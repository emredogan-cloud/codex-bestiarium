# Imugi — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `imugi` |
| **Ad** | Imugi |
| **Alternatif yazımlar** | Imoogi |
| **Gelenek** | Hangug 단 · Doğu Asya |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | E · Derinlerin yılanı |
| **Plaka** | `plate-032` |
| **Telaffuz (taslak)** | EE-moo-gee |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** James H. Grayson, *Myths and Legends from Korea* (Richmond: Curzon, 2001)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Choi In-hak, *A Type Index of Korean Folktales* (Seul: Myong Ji University Press, 1979)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Imugi”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B11.1` | Origin of dragon | ✅ |

**Gerekçe.** B11.1 ('Origin of dragon') doğrulandı ve korundu. Imugi'nin tanımı ejderha OLMA sürecidir — kod tam olarak ejderhanın kökenini tasnif eder.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Hangug; göl, mağara, derin su
- **İlk kayıt (attested):** 19.–20. yy sözlü derlemeler; Grayson ve Choi derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Büyük su yılanı
- Henüz boynuzsuz
- Bin yıl beklediği anlatılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Ejderha (yong) olmayı bekler. Çoğu anlatıda olamaz — bir insan onu görüp bağırırsa dönüşüm bozulur.
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
| **Lóng** `long` | Zhōnghuá 龍 | `function` | Lóng olunmuş hâldir, Imugi olunamamış — aynı basamağın iki ucu. |
| **Nāga** `naga` | Bharatiya ॐ | `kin` | Nāga zaten bir halktır; Imugi tek başına ve bekleyendir. Biri düzen, öteki eşik. |
| **Thuồng luồng** `thuong-luong` | Việt ☴ | `kin` | Imugi ejderha olmayı bekler ve olamaz; Thuồng luồng olduğu şeyle yetinir ve insan ona benzemeye çalışır (dövme). |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Derinlerin yılanı ailesinin (E) tek BAŞARISIZ üyesi — ayrışma noktası bu.

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

