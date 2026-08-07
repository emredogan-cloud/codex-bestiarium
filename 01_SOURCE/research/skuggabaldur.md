# Skuggabaldur — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `skuggabaldur` |
| **Ad** | Skuggabaldur |
| **Alternatif yazımlar** | Skoffín (akraba) |
| **Gelenek** | Ísland ❆ · Kuzey Avrupa |
| **Sınıf** | III · THE SHAPE-CHANGERS (Şekil Değiştirenler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-109` |
| **Telaffuz (taslak)** | SKOOG-gah-bald-oor |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Jón Árnason, *Íslenzkar þjóðsögur og æfintýri* (Leipzig: J. C. Hinrichs, 1862–64)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Jacqueline Simpson, *Icelandic Folktales and Legends* (Berkeley: University of California Press, 1972)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Skuggabaldur”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B14` | Other hybrid animals | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum B871 ('Giant beasts') idi — skuggabaldur dev değil MELEZDİR. Doğrulanan B14 ('Other hybrid animals') tam tanımdır.

> ⚠ **Tohum kodu değiştirildi.** B871 → B14.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Ísland; kırsal, koyun otlakları
- **İlk kayıt (attested):** Jón Árnason, *Íslenzkar þjóðsögur* (1862–64)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Kedi ile tilkinin yavrusu
- Kurşun işlemez

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Koyun sürüsüne saldırır. Öldürüldüğünde son sözünü söylediği ve öldüreni lanetlediği anlatılır.
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
| **Buda** `buda` | Ityop'ya ✤ | `function` | İkisi de sürüye zarar verir ve ikisi de melez sayılır; biri insanla hayvan, öteki iki hayvan arasında. |
| **Huldufólk** `huldufolk` | Ísland ❆ | `tradition` | Ísland'ın iki ucu: biri kayanın içindeki komşu, öteki kurşun işlemeyen melez. |
| **Nykur** `nykur` | Ísland ❆ | `tradition` | İzlanda'nın iki tehlikeli hayvanı: biri sürüye, öteki biniciye. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Melezlik: Chímaira ve Makara ile karşılaştırılabilir ama burada melez GERÇEK hayvanlardan.

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

