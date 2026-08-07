# Àbíkú — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `abiku` |
| **Ad** | Àbíkú |
| **Alternatif yazımlar** | — |
| **Gelenek** | Yorùbá · Ashanti ✺ · Afrika |
| **Sınıf** | VI · THE RESTLESS DEAD (Huzursuz Ölüler) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-041` |
| **Telaffuz (taslak)** | ah-BEE-koo |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Timothy Mobolade, "The Concept of Abiku", *African Arts* 7:1 (1973), 62–64

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** William Bascom, *The Yoruba of Southwestern Nigeria* (New York: Holt, Rinehart and Winston, 1969)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Abiku”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `E220` | Dead relative's malevolent return | ✅ |

**Gerekçe.** TOHUM KODU DOĞRULANDI ve korundu. E220 ('Dead relative's malevolent return') àbíkú'nün aynı aileye tekrar tekrar dönmesini tasnif eder. E324 ('Dead child's friendly return to parents') değerlendirildi ama àbíkú DOSTÇA dönmez.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Yorùbá (Nijerya, Benin)
- **İlk kayıt (attested):** 19.–20. yy saha derlemeleri; Yorùbá adlandırma geleneği kayıtları

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Çocuk biçiminde
- Bedende iz veya yara ile tanınır (önceki ölümden kalan)

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Doğar, ölür ve aynı anneye tekrar döner. Zincir kırılsın diye çocuğa 'kalmasını' isteyen adlar verilir (Málọmọ, Dúrójayé).
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
| **Adze** `adze` | Yorùbá · Ashanti ✺ | `kin` | Aynı gelenekte iki cevap: Adze dışarıdan gelen bir faildir, Àbíkú çocuğun kendisidir. |
| **Bean sídhe** `bean-sidhe` | Ériu ☘ | `function` | İkisi de ölümü ADLA bağlar: Bean sídhe bir aileye, Àbíkú bir anneye — biri haber verir, öteki tekrarlar. |
| **Pontianak** `pontianak` | Nusantara ❋ | `kin` | Àbíkú ölen çocuğun dönüşüdür, Pontianak ölen annenin. Aynı doğum, iki ayrı hayalet. |
| **Strigoi** `strigoi` | Dacia ✠ | `function` | İkisi de aileye geri döner; Strigoi alır, Àbíkú yalnızca gider ve tekrar gelir. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Àbíkú YAŞAYAN bir inanç ve gerçek çocuk ölümleriyle ilgilidir. Madde bir 'yaratık' anlatısı olarak değil, YAS ve adlandırma pratiği olarak yazılacak. Tören ayrıntısı ve koruyucu uygulama aktarılmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Gece cadısı ailesinde (C) ama àbíkú avcı değil KURBAN — Pontianak ile aynı ahlaki konumda. Faz 2'de aile üyeliği gözden geçirilmeli.
- Adların anlamı ('kalma bizi üzme') maddenin 5. bölümünü taşıyacak.

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

