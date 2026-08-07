# Rukh — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `rukh` |
| **Ad** | Rukh |
| **Alternatif yazımlar** | Roc, Rukhkh |
| **Gelenek** | ʿArab ☪ · Yakın Doğu |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | D · Fırtına kuşu |
| **Plaka** | `plate-057` |
| **Telaffuz (taslak)** | ROOK |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Bin Bir Gece* (Alf layla wa-layla)
- **Yer:** Sindbad'ın İkinci Yolculuğu

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Robert Irwin, *The Arabian Nights: A Companion* (Londra: Allen Lane, 1994)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Roc”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B31.1` | Roc | ✅ |

**Gerekçe.** TOHUM KODU DOĞRULANDI ve korundu. Doğrulanan B31.1'in tanımı 'Roc. A giant bird which carries off men in its claws' — kod bu maddenin adını taşıyor. NOT: önceki turda B31'in 'Roc' olduğu sanılmıştı; tam nüsha ayrıştırması B31'in bölüm başlığı, B31.1'in Roc olduğunu gösterdi. Tohum tablosu BAŞTAN DOĞRUYDU.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** ʿArab; Hint Okyanusu, Madagaskar anlatıları
- **İlk kayıt (attested):** *Bin Bir Gece* (Sindbad'ın ikinci ve beşinci yolculuğu); İbn Battûta (14. yy)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Devasa kuş
- Fili pençesiyle kaldırır
- Yumurtası bir kubbe büyüklüğünde

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Sindbad yumurtasına bağlanarak adadan kurtulur; sonra Rukh gemiyi kayayla batırır.
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
| **Anzû** `anzu` | Sumer 𒀭 | `kin` | Rukh bir gezi anlatısına girer (Sindbad), Anzû bir devlet anlatısına — biri denizde, öteki tapınakta. |
| **ʿIfrīt** `ifrit` | ʿArab ☪ | `tradition` | Arap anlatısının iki ölçeği: biri tahtı taşır, öteki gemiyi batırır. |
| **Ziz** `ziz` | Talmud ✡ | `kin` | Thompson ikisini yan yana kodlar (B31.1 · B31.1.0.1): Rukh gemiyi batırır, Ziz yalnızca büyüktür. Ölçek ile tehlike aynı şey değildir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Fırtına kuşu ailesinin (D) tek TAŞIYICI üyesi: fırtına getirmez, YÜK kaldırır.

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

