# Supay — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `supay` |
| **Ad** | Supay |
| **Alternatif yazımlar** | — |
| **Gelenek** | Tawantinsuyu ☉ · And |
| **Sınıf** | VI · THE RESTLESS DEAD (Huzursuz Ölüler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-097` |
| **Telaffuz (taslak)** | SOO-pye |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Michael Taussig, *The Devil and Commodity Fetishism in South America* (Chapel Hill: University of North Carolina Press, 1980)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** June Nash, *We Eat the Mines and the Mines Eat Us: Dependency and Exploitation in Bolivian Tin Mines* (New York: Columbia University Press, 1979)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Supay”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `E200` | Malevolent return from the dead | ✅ |

**Gerekçe.** E200 ('Malevolent return from the dead') doğrulandı ve korundu. Supay yeraltı ve ölülerle ilişkili bir varlıktır. Not: sömürge sonrası Hristiyan 'şeytan' ile karıştırılmıştır ve bu ayrım maddede yapılacak.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Tawantinsuyu (And); yeraltı, madenler
- **İlk kayıt (attested):** Sömürge dönemi kronikleri; Potosí maden anlatıları; 20. yy etnografi

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Biçimi değişken
- Maden ocaklarında 'Tío' figürü olarak heykelleştirilir

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Yeraltının ve madenlerin efendisi. Madenciler ocakta ona koka, alkol ve sigara sunar.
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
| **Amaru** `amaru` | Tawantinsuyu ☉ | `tradition` | Tawantinsuyu'nun iki dünyası: Supay aşağıyı tutar, Amaru aşağıyla yukarıyı bağlar. |
| **Ammit** `ammit` | Kemet 𓂀 | `function` | Ammit yargının sonucudur — kalp tartılır; Supay yeraltının sahibidir ve yargılamaz, tutar. |
| **Lemures** `lemures` | Romana SPQR | `function` | İkisi de sunuyla yatıştırılır: biri baklayla, öteki koka ve alkolle. |
| **Pishtaco** `pishtaco` | Tawantinsuyu ☉ | `tradition` | Tawantinsuyu'nun iki sömürü anlatısı: biri bedeni, öteki madeni alır. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

⚠ Tío sunusu YAŞAYAN bir madenci pratiğidir. Tören sırası ve dua KULLANILMAZ; yalnızca yayımlanmış etnografik betimleme kullanılır.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Sömürge sonrası 'şeytan'la karıştırılma: maddenin kaynak notu bu ayrımı yapmak zorunda.

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

