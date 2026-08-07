# Pishtaco — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `pishtaco` |
| **Ad** | Pishtaco |
| **Alternatif yazımlar** | Nakaq, Kharisiri |
| **Gelenek** | Tawantinsuyu ☉ · And |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-096` |
| **Telaffuz (taslak)** | peesh-TAH-ko |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `article`

- **Künye:** Mary Weismantel, "Cities of Women", *American Ethnologist* 24:4 (1997)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Mary Weismantel, *Cholas and Pishtacos: Stories of Race and Sex in the Andes* (Chicago: University of Chicago Press, 2001)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Pishtaco”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G11.2` | Cannibal giant | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum G11 ('Kinds of cannibals') bölüm başlığıydı; doğrulanan G11.2 ('Cannibal giant') pishtaco'nun insanı avlayan yabancı figürünü tasnif eder. Not: pishtaco eti değil YAĞI alır; Thompson'da tam karşılık bulunamadı ve bu maddede belirtilecek.

> ⚠ **Tohum kodu değiştirildi.** G11 → G11.2.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Tawantinsuyu (And); Peru ve Bolivya kırsalı
- **İlk kayıt (attested):** Sömürge döneminden itibaren; 20. yy saha derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Yabancı — sömürge döneminde İspanyol, sonra beyaz adam, mühendis veya doktor olarak
- Uzun bıçak taşır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Yolcuyu yakalar ve yağını çıkarır. Yağın çan yapımında, ilaçta veya makine yağı olarak kullanıldığı anlatılır.
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
| **Ghūl** `ghul` | ʿArab ☪ | `function` | İkisi de yoldaki yabancıdır; Ghūl kılık değiştirir, Pishtaco zaten yabancı görünür — korku sömürünün suretini alır. |
| **Supay** `supay` | Tawantinsuyu ☉ | `tradition` | Tawantinsuyu'nun iki sömürü anlatısı: biri bedeni, öteki madeni alır. |
| **Windigo** `windigo` | Anishinaabe ▲ | `function` | İkisi de ekonomik bir korkuyu bedenleştirir: biri yağı çıkarır, öteki asla doymaz. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Pishtaco anlatısı YAŞAYANDIR ve gerçek şiddet olaylarıyla (yabancıların linç edilmesi dahil) ilişkilidir. Madde bunu bir 'yaratık' olarak değil, sömürünün aldığı BİÇİM olarak anlatacak.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Sömürünün suretini almış korku: kitabın en politik maddesi. Weismantel'in çözümlemesi 5. bölümü taşıyacak.

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

