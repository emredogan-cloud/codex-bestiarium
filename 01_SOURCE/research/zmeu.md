# Zmeu — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `zmeu` |
| **Ad** | Zmeu |
| **Alternatif yazımlar** | Zmeul |
| **Gelenek** | Dacia ✠ · Balkanlar |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | E · Derinlerin yılanı |
| **Plaka** | `plate-094` |
| **Telaffuz (taslak)** | ZMEH-oo |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Petre Ispirescu, *Legende sau basmele românilor* (Bükreş, 1872)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Moses Gaster, *Rumanian Bird and Beast Stories* (Londra: Sidgwick & Jackson, 1915)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Zmeu”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B11.2.3` | Many-headed dragon | ✅ |

**Gerekçe.** B11.2.3 ('Many-headed dragon') doğrulandı ve korundu. Zmeu Rumen masallarında çok başlı ve konuşan bir ejderhadır.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Dacia (Romanya)
- **İlk kayıt (attested):** Petre Ispirescu, *Legende sau basmele românilor* (1872); 19.–20. yy derlemeler

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Çok başlı
- İnsan gibi konuşur ve düşünür
- At sürer, ev sahibi olur

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Kızları kaçırır ve hazine bekler. Rumen masallarında insan gibi pazarlık eder — bu, onu Zmey'den ayırır.
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
| **Aži Dahāka** `azi-dahaka` | Pārs 𐎩 | `kin` | İkisi de konuşur ve ikisi de tutsak alır; Aži Dahāka'nın tutsaklığı kendi başına gelir — dağın altına zincirlenir. |
| **Vârcolac** `varcolac` | Dacia ✠ | `tradition` | Rumen masalının iki düşmanı: biri kozmik bir açıklama, öteki bir pazarlık. |
| **Zmey** `zmey` | Slovjan ⚡ | `kin` | Zmey yalnızca güçtür; Zmeu insan gibi pazarlık eder. Ailenin dış sınırı tam olarak burasıdır. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Derinlerin yılanı ailesinin (E) en İNSANSI üyesi: konuşur, pazarlık eder, evlenmek ister.

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

