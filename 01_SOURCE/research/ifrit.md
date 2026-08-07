# ʿIfrīt — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `ifrit` |
| **Ad** | ʿIfrīt |
| **Alternatif yazımlar** | Afrit, Efreet |
| **Gelenek** | ʿArab ☪ · Yakın Doğu |
| **Sınıf** | III · THE SHAPE-CHANGERS (Şekil Değiştirenler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-056` |
| **Telaffuz (taslak)** | if-REET |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Kur'an*
- **Yer:** 27:39 (Neml suresi)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Amira El-Zein, *Islam, Arabs, and the Intelligent World of the Jinn* (Syracuse: Syracuse University Press, 2009)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Ifrit”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G307` | Jinn | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum F402 ('Evil spirits') idi; doğrulanan G307 ('Jinn') ʿifrīt'in cinlerin bir SINIFI olduğunu doğru şekilde tasnif eder — genel 'kötü ruh' değil.

> ⚠ **Tohum kodu değiştirildi.** F402 → G307.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** ʿArab; İslam öncesi ve sonrası Arap dünyası
- **İlk kayıt (attested):** Kur'an 27:39; *Bin Bir Gece*; el-Câhiz

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Ateşten yaratılmış
- Cinlerin güçlü ve dik başlı sınıfı
- Kanatlı olarak da betimlenir

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Cinlerin en güçlü sınıfı. Kur'an'da Süleyman'ın huzurunda Belkıs'ın tahtını getirmeyi öneren varlıktır.
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
| **Ghūl** `ghul` | ʿArab ☪ | `tradition` | Arap geleneğinde iki ayrı kategori: Ghūl bir yiyici, ʿIfrīt bir cin sınıfı — biri açlık, öteki güç. |
| **Perī** `peri` | Pārs 𐎩 | `function` | İkisi de ateşten yaratılmıştır; Perī kararsızdır, ʿIfrīt dik başlı — aynı madde, iki mizaç. |
| **Rukh** `rukh` | ʿArab ☪ | `tradition` | Arap anlatısının iki ölçeği: biri tahtı taşır, öteki gemiyi batırır. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

ʿIfrīt YAŞAYAN bir dinî geleneğin parçasıdır. Kur'an atfı bir metin atfıdır; teolojik yorum yapılmaz, muska ve dua metni aktarılmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Perī ile ortak kod (G307): iki komşu gelenek aynı ateş-varlığı kümesinde.

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

