# Zmey — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `zmey` |
| **Ad** | Zmey |
| **Alternatif yazımlar** | Zmey Gorynych, Zmaj |
| **Gelenek** | Slovjan ⚡ · Kuzey Avrupa |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | E · Derinlerin yılanı |
| **Plaka** | `plate-038` |
| **Telaffuz (taslak)** | zmay |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Aleksandr Afanasyev, *Narodnye russkie skazki* (Moskova, 1855–63)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Linda J. Ivanits, *Russian Folk Belief* (Armonk: M. E. Sharpe, 1989)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Zmey”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B11.2.3` | Many-headed dragon | ✅ |

**Gerekçe.** B11.2.3 ('Many-headed dragon') doğrulandı ve korundu. Zmey'in tanımlayıcı özelliği çok başlılık ve kesilen başın yerine yenisinin çıkmasıdır.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Slovjan; Rusya, Ukrayna, Balkanlar
- **İlk kayıt (attested):** Rus bylina geleneği (Dobrynya Nikitich); Afanasyev derlemesi (1855–63)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Üç, altı, dokuz veya on iki başlı
- Ateş soluyan
- Kanatlı

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Kızları kaçırır ve hazine bekler. Kesilen her başın yerine yenisi çıkar — ateşle dağlanmadıkça.
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
| **Herensuge** `herensuge` | Euskal ✜ | `function` | İki çok başlı ejderha, iki ayrı son: biri azizle, öteki ateşle dağlanarak. |
| **Rusalka** `rusalka` | Slovjan ⚡ | `tradition` | Slovjan'ın iki ucu: biri tarlayı sular, öteki hazineyi bekler. |
| **Vishap** `vishap` | Hayk ✚ | `kin` | Vishap taş dikitlerle işaretlenir — yeri bellidir; Zmey'in yeri yoktur, kesilen başı yerine yenisi çıkar. |
| **Yamata-no-Orochi** `yamata-no-orochi` | Yamato 神 | `kin` | İki çok başlı: Orochi sarhoş edilip parçalanır, Zmey'in başı ateşle dağlanmadıkça geri çıkar. |
| **Zmeu** `zmeu` | Dacia ✠ | `kin` | Zmey yalnızca güçtür; Zmeu insan gibi pazarlık eder. Ailenin dış sınırı tam olarak burasıdır. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Derinlerin yılanı ailesinin (E) Slav üyesi. Ayrışma: Zmey ÇOĞALAN tek yaratık.

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

