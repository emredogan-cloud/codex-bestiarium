# Anzû — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `anzu` |
| **Ad** | Anzû |
| **Alternatif yazımlar** | Imdugud, Zû |
| **Gelenek** | Sumer 𒀭 · Yakın Doğu |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | D · Fırtına kuşu |
| **Plaka** | `plate-020` |
| **Telaffuz (taslak)** | AN-zoo |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Anzû Destanı*
- **Yer:** Tablet I–III

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Jeremy Black ve Anthony Green, *Gods, Demons and Symbols of Ancient Mesopotamia: An Illustrated Dictionary* (Londra: British Museum Press, 1992)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Anzu”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B31.1` | Roc | ✅ |

**Gerekçe.** TOHUM KODU DÜZELTİLDİ. Tohum B31 idi; B31 bölüm başlığıdır (Giant birds). Doğrulanan B31.1 ('Roc. A giant bird which carries off men in its claws') Anzû'nun dev yırtıcı kuş biçimini tasnif eder.

> ⚠ **Tohum kodu değiştirildi.** B31 → B31.1 (B31 bölüm başlığıdır).

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Sumer/Akkad; Ekur tapınağı ve dağlar
- **İlk kayıt (attested):** *Anzû Destanı* (Eski Babil ve Standart Babil sürümleri); Sumerce Lugalbanda döngüsü

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Aslan başlı dev kuş
- Kartal gövdeli

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Kader Tabletleri'ni Enlil'den çalar; Ninurta onu yener. Hırsızlık kozmik düzeni askıya alır.
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
| **Rukh** `rukh` | ʿArab ☪ | `kin` | Rukh bir gezi anlatısına girer (Sindbad), Anzû bir devlet anlatısına — biri denizde, öteki tapınakta. |
| **Sīmurgh** `simurgh` | Pārs 𐎩 | `kin` | Anzû kader tabletlerini ÇALAR; Sīmurgh bir çocuğu büyütür ve yol gösterir. Aynı kanat, hırsız ve bilge. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Fırtına kuşu ailesinin (D) Mezopotamya üyesi ve tek HIRSIZ üyesi.

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

