# Iku-Turso — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `iku-turso` |
| **Ad** | Iku-Turso |
| **Alternatif yazımlar** | Turisas, Tursas |
| **Gelenek** | Suomi ᛉ · Kuzey Avrupa |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | E · Derinlerin yılanı |
| **Plaka** | `plate-058` |
| **Telaffuz (taslak)** | EE-koo TOOR-so |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Kalevala*
- **Yer:** runo 42

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Anna-Leena Siikala, *Mythic Images and Shamanism: A Perspective on Kalevala Poetry* (Helsinki: Academia Scientiarum Fennica, 2002)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Iku-Turso”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B11.2` | Form of dragon | ✅ |

**Gerekçe.** B11.2 ('Form of dragon') doğrulandı ve korundu. Iku-Turso'nun kaynaklarda tanımlanan yanı biçimi ve denizden çıkışıdır.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Suomi; deniz dibi
- **İlk kayıt (attested):** *Kalevala* (Lönnrot, 1849); Suomen Kansan Vanhat Runot derlemesi

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Deniz dibinden çıkan varlık
- Bin boynuzlu olarak anılır
- Biçimi kaynaklarda belirsiz bırakılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Denizin dibinden çıkar. Kalevala'da Väinämöinen onu yakalar ve bir daha çıkmayacağına yemin ettirir.
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
| **Ajatar** `ajatar` | Suomi ᛉ | `tradition` | Suomi'nin iki eski varlığı: biri ormanda hastalık yayar, öteki denizin dibinde bekler. |
| **Apep** `apep` | Kemet 𓂀 | `kin` | Apep'in adı her gün anılır ve lanetlenir; Iku-Turso'nun adı uğursuz sayılıp anılmaz. |
| **Jörmungandr** `jormungandr` | Norðr ᚦ | `kin` | İkisi de kuzey denizinin dibinde; biri yemin ettirilip gönderilir, öteki orada bekler. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Adı bile uğursuz sayılır: kaynaklarda biçimi kasten belirsiz. Bu BELİRSİZLİK maddenin konusu olacak.

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

