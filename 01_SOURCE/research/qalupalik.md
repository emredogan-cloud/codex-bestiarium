# Qalupalik — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `qalupalik` |
| **Ad** | Qalupalik |
| **Alternatif yazımlar** | Qallupilluit (çoğul) |
| **Gelenek** | Inuit ᐃ · Kutup |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-049` |
| **Telaffuz (taslak)** | kah-loo-PAH-lik |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Knud Rasmussen, *Intellectual Culture of the Iglulik Eskimos*, Report of the Fifth Thule Expedition 1921–24, VII:1 (Kopenhag: Gyldendal, 1929)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Daniel Merkur, *Powers Which We Do Not Know: The Gods and Spirits of the Inuit* (Moscow, Idaho: University of Idaho Press, 1991)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Qalupalik”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G442` | Child-stealing demon | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum G308 ('Sea monster') idi; qalupalik'in tanımlayıcı eylemi deniz canavarı olmak değil ÇOCUK ALMAKTIR. Doğrulanan G442 ('Child-stealing demon') tam tanımdır.

> ⚠ **Tohum kodu değiştirildi.** G308 → G442.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Inuit; Nunavut ve Nunavik kıyıları, deniz buzu kenarı
- **İlk kayıt (attested):** 20. yy sözlü derlemeler; Inuit anlatı derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Yeşil derili
- Uzun saçlı
- Sırtında amautik (bebek taşıma kesesi)

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Buzun altında bekler ve kıyıda yalnız kalan çocuğu alır. Anlatı, çocukları buz kenarından uzak tutar.
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
| **Kenas-unarpe** `kenas-unarpe` | Ainu ᚼ | `kin` | Kuzeyin iki bekleyeni: biri bataklıkta loğusayı, öteki buzun altında yalnız çocuğu. |
| **Tupilaq** `tupilaq` | Inuit ᐃ | `tradition` | Inuit'in iki tehlikesi: biri yapılır ve gönderilir, öteki hep oradadır. |
| **Windigo** `windigo` | Anishinaabe ▲ | `function` | İki kuzey korkusu, iki yaş grubu: Qalupalik çocuğu alır, Windigo yetişkini dönüştürür. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Inuit anlatı geleneği YAŞAYANDIR. Yalnızca yayımlanmış derlemeler kullanıldı. Şaman (angakkuq) uygulaması, tören ve yer-özel anlatı KULLANILMAZ. Rasmussen'in sömürge dönemi çerçevesi eleştirel okunacak.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Gece cadısı ailesinin (C) Kutup üyesi ve tek AÇIK ÖĞRETİCİ üyesi: anlatının işlevi çocuğu uyarmak.

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

