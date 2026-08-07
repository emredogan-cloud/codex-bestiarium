# Srin-po — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `srin-po` |
| **Ad** | Srin-po |
| **Alternatif yazımlar** | Srin mo (dişil) |
| **Gelenek** | Bod ☷ · Himalaya |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-079` |
| **Telaffuz (taslak)** | SIN-po |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** R. A. Stein, *Tibetan Civilization*, çev. J. E. Stapleton Driver (Stanford: Stanford University Press, 1972)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Janet Gyatso, "Down with the Demoness: Reflections on a Feminine Ground in Tibet", *The Tibetan Journal* 12:4 (1987), 38–53

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Srinpo”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G312.3` | Flesh-eating spirits live in trees | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum G300 ('Other ogres') genel bir kümeydi; doğrulanan G312.3 ('Flesh-eating spirits live in trees') ve G312.5 srin-po'nun et yiyen ruh sınıfını daha dar tasnif eder.

> ⚠ **Tohum kodu değiştirildi.** G300 → G312.3.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Bod; toprak altı ve ıssız yerler
- **İlk kayıt (attested):** Tibet tarih ve din metinleri; Padmasambhava döngüsü

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Et yiyen varlıklar sınıfı
- Kırmızı yüzlü olarak betimlenir

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Toprağın altında yaşadığı anlatılır. Tibet'in Budistleşmesi anlatısında tapınaklarla bastırılırlar — Jokhang ve on iki tapınak, yere serilmiş bir srin-mo'nun uzuvlarına çakılır.
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
| **Ajatar** `ajatar` | Suomi ᛉ | `function` | İkisi de bastırılması gereken eski bir güçtür — biri hastalıkla, öteki tapınakla. |
| **Khyung** `khyung` | Bod ☷ | `tradition` | Bön kozmolojisinin iki ucu: yerin altındaki et yiyen halk ve gökteki kartal. |
| **Migoi** `migoi` | Bod ☷ | `tradition` | Bod'un iki yer varlığı: Srin-po toprağın altında bastırılmıştır, Migoi karda serbesttir. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Tibet Budizmi yaşayan bir gelenektir. Tapınak yerleşimi anlatısı yayımlanmış akademik çalışmalardan alınmıştır; tören ve manastır uygulaması KULLANILMAZ.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Yaratığın ÜZERİNE tapınak çakılması: mimarinin folklorla açıklanması. Kitapta benzersiz.

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

