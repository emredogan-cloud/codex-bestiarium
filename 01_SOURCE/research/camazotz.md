# Camazotz — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `camazotz` |
| **Ad** | Camazotz |
| **Alternatif yazımlar** | Zotz |
| **Gelenek** | Maya 𝋠 · Mezoamerika |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | F · Eşik bekçisi |
| **Plaka** | `plate-034` |
| **Telaffuz (taslak)** | kah-mah-SOTS |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Popol Vuh*
- **Yer:** İkinci Kitap, Xibalba sınavları

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Mary Miller ve Karl Taube, *An Illustrated Dictionary of the Gods and Symbols of Ancient Mexico and the Maya* (Londra: Thames & Hudson, 1993)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Camazotz”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B31.4` | Giant bat | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum B31.1 ('Roc') idi — Camazotz yırtıcı kuş değil YARASADIR. Doğrulanan B31.4'ün tanımı doğrudan 'Giant bat'.

> ⚠ **Tohum kodu değiştirildi.** B31.1 → B31.4. Yarasa kuş değildir.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Maya; Xibalba'nın beşinci evi (Zotzihá, Yarasa Evi)
- **İlk kayıt (attested):** *Popol Vuh* (Quiché Maya, ~1550 yazıya geçirildi)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Dev yarasa
- Kesici burunlu

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Xibalba'nın Yarasa Evi'ni bekler. Popol Vuh'ta Hunahpú'nun başını keser.
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
| **Cipactli** `cipactli` | Mēxihcah ☼ | `tradition` | Mezoamerika'nın iki kozmolojik gövdesi: biri yeryüzünü verir, öteki yeraltını bekler. |
| **Kérberos** `kerberos` | Hellenic Ω | `kin` | İkisi de yeraltının bir odasını tutar; biri köpek, öteki yarasa — hayvan seçimi coğrafyanın seçimidir. |
| **Temes Savsap** `temes-savsap` | Melanesia ◉ | `kin` | Temes Savsap geçişi bilgiye bağlar; Camazotz geçeni keser. Sınav ile infaz. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Eşik bekçisi ailesinin (F) Mezoamerika üyesi. Ayrışma: burada bekçi SINAVIN kendisi — ev bir odadır.

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

