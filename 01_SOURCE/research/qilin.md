# Qílín — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `qilin` |
| **Ad** | Qílín |
| **Alternatif yazımlar** | Kirin, Ki-lin |
| **Gelenek** | Zhōnghuá 龍 · Doğu Asya |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | F · Eşik bekçisi |
| **Plaka** | `plate-029` |
| **Telaffuz (taslak)** | CHEE-lin |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** *Chunqiu* (Bahar ve Güz Yıllıkları), Ai Gong 14. yıl

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Anne Birrell, *Chinese Mythology* (Baltimore: Johns Hopkins University Press, 1993)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Ki-lin”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B19` | Other mythical beasts | ✅ |

**Gerekçe.** B19 ('Other mythical beasts') doğrulandı ve korundu. Qílín bir bileşik hayvandır ve Thompson'ın daha dar bir alt kodu bu maddeye uymuyor; doğrulanmamış dar kod yerine doğrulanmış üst kod kullanıldı.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Zhōnghuá; iyi hükümdarın çağı
- **İlk kayıt (attested):** *Chunqiu* (MÖ 5. yy) ve Zuo şerhi; Han dönemi kayıtları

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Geyik gövdesi, öküz kuyruğu, at toynağı
- Tek boynuz (etle kaplı)
- Pullu deri

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Adaletsizin üzerine basmaz; otu bile ezmez. Bilge bir hükümdarın doğuşunu veya gelişini haber verir.
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
| **Basiliscus** `basiliscus` | Romana SPQR | `kin` | Qílín otu bile ezmez; Basiliscus geçtiği yeri çöle çevirir. Aynı sınıfın iki ucu: dokunmayan ve yok eden. |
| **Lóng** `long` | Zhōnghuá 龍 | `tradition` | Zhōnghuá'nın iki hayırlı varlığı: biri yağmuru, öteki adaleti haber verir. |
| **Tengu** `tengu` | Yamato 神 | `function` | Qílín adaletsizin üzerine BASMAZ; Tengu kibirliyi cezalandırır. Aynı ahlak, iki ayrı yaptırım. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Eşik bekçisi ailesinin (F) en tuhaf üyesi: engellemez, YARGILAR. Ayrışma noktası bu.

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

