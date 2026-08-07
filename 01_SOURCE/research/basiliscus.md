# Basiliscus — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `basiliscus` |
| **Ad** | Basiliscus |
| **Alternatif yazımlar** | Basilisk, Basiliskos |
| **Gelenek** | Romana SPQR · Akdeniz |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | F · Eşik bekçisi |
| **Plaka** | `plate-026` |
| **Telaffuz (taslak)** | bah-si-LIS-kus |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Plinius, *Naturalis Historia*
- **Yer:** VIII.33

### Kaynak 2 · `primary` · doğrulama `canon`

- **Künye:** Lucanus, *Pharsalia*
- **Yer:** IX.724–726

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Basilisk”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B12` | Basilisk. A mythical lizard or serpent whose hissing drives away all other serpents | ✅ |

**Gerekçe.** B12 ('Basilisk. A mythical lizard or serpent whose hissing drives away all other serpents') doğrulandı ve korundu. Kod doğrudan bu maddenin adını taşıyor.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Roma; Kyrene çölü (Plinius'a göre)
- **İlk kayıt (attested):** Plinius, *Naturalis Historia* VIII (MS 77); Lucanus, *Pharsalia* IX

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Küçük — Plinius'a göre on iki parmak uzunluğunda
- Başında taç benzeri beyaz leke
- Dik yürüyen ön gövde

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Bakışı ve soluğu öldürür; geçtiği yeri çöle çevirir. Plinius'ta gelincik onu öldüren tek hayvandır.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** Plinius'ta gelincik (*mustela*); ortaçağda ayna.

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Ḫumbaba** `humbaba` | Sumer 𒀭 | `kin` | İkisi de bakışla iş görür; Ḫumbaba'nın yüzü bağırsak kıvrımlarıdır — bakılan da bakan kadar önemlidir. |
| **Olgoi-Khorkhoi** `olgoi-khorkhoi` | Mongol ⚔ | `function` | Basiliscus bakışla, Olgoi-Khorkhoi dokunuşla öldürür — ikisi de mesafeyi kaldırır. |
| **Qílín** `qilin` | Zhōnghuá 龍 | `kin` | Qílín otu bile ezmez; Basiliscus geçtiği yeri çöle çevirir. Aynı sınıfın iki ucu: dokunmayan ve yok eden. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Eşik bekçisi ailesinde (F) — ama bekçilik etmez, YOL AÇMAZ. Faz 2'de aile üyeliği gözden geçirilmeli.
- Ölçü verilmiş: on iki parmak. Somutluk kuralının Roma kaynaklı örneği.

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

