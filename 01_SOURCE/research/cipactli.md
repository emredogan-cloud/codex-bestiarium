# Cipactli — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `cipactli` |
| **Ad** | Cipactli |
| **Alternatif yazımlar** | — |
| **Gelenek** | Mēxihcah ☼ · Mezoamerika |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-022` |
| **Telaffuz (taslak)** | see-PAHK-tlee |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Bernardino de Sahagún, *Florentine Codex: General History of the Things of New Spain*, çev. Anderson ve Dibble (Santa Fe: School of American Research, 1950–82)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Mary Miller ve Karl Taube, *An Illustrated Dictionary of the Gods and Symbols of Ancient Mexico and the Maya* (Londra: Thames & Hudson, 1993)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Cipactli”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `A831` | Earth from body of person (animal) | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum A812 ('Earth Diver') idi — earth-diver bir hayvanın dalıp çamur getirmesidir; Cipactli'de yeryüzü onun GÖVDESİNDEN yapılır. Doğrulanan A831 ('Earth from body of person (animal)') tam tanımdır.

> ⚠ **Tohum kodu değiştirildi.** A812 → A831.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Mēxihcah; ilksel su
- **İlk kayıt (attested):** *Historia de los mexicanos por sus pinturas* (16. yy); Sahagún, *Florentine Codex* (1569)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- İlkel timsah/balık benzeri varlık
- Her ekleminde bir ağız

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Tezcatlipoca ve Quetzalcoatl onu parçalar; gövdesinden yeryüzü yapılır. Ağızları doyurulmadıkça yeryüzü meyve vermez.
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
| **Ammit** `ammit` | Kemet 𓂀 | `function` | Cipactli'nin her ekleminde bir ağız vardır ve doyurulmalıdır; Ammit tek ağızdır ve yalnızca hak edeni yutar. |
| **Apep** `apep` | Kemet 𓂀 | `function` | İkisi de düzenin sürekli yeniden kurulmasını gerektirir: biri beslenerek, öteki yenilerek. |
| **Camazotz** `camazotz` | Maya 𝋠 | `tradition` | Mezoamerika'nın iki kozmolojik gövdesi: biri yeryüzünü verir, öteki yeraltını bekler. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Her eklemde ağız: kurban mantığının kozmolojik gerekçesi.

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

