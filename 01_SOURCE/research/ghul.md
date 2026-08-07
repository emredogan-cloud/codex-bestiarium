# Ghūl — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `ghul` |
| **Ad** | Ghūl |
| **Alternatif yazımlar** | Ghoul, Ghūla (dişil) |
| **Gelenek** | ʿArab ☪ · Yakın Doğu |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-055` |
| **Telaffuz (taslak)** | GOOL |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** el-Câhiz, *Kitāb al-Ḥayawān* (Hayvanlar Kitabı, 9. yy)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Amira El-Zein, *Islam, Arabs, and the Intelligent World of the Jinn* (Syracuse: Syracuse University Press, 2009)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Ghul”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G11.2` | Cannibal giant | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum G11 ('Kinds of cannibals') bölüm başlığıydı; doğrulanan G11.2 ('Cannibal giant') ghūl'ün çölde yolcuyu yiyen iri varlık tanımına daha yakın. Not: ghūl aynı zamanda şekil değiştirir; D100 kümesi Faz 2'de ikinci kod olarak değerlendirilecek.

> ⚠ **Tohum kodu değiştirildi.** G11 → G11.2.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** ʿArab; çöl, mezarlık, ıssız yol
- **İlk kayıt (attested):** *Kitāb al-Ḥayawān* (el-Câhiz, 9. yy); *Bin Bir Gece* derlemesi

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Kılık değiştirir
- Ayakları eşek toynağı olarak anlatılır (gizlenemeyen işaret)

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Çölde yolcuyu şaşırtır ve yer. Mezarlıkta ölüyü kazar.
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
| **ʿIfrīt** `ifrit` | ʿArab ☪ | `tradition` | Arap geleneğinde iki ayrı kategori: Ghūl bir yiyici, ʿIfrīt bir cin sınıfı — biri açlık, öteki güç. |
| **Karakoncolos** `karakoncolos` | Türk ☾ | `function` | Karakoncolos soru sorar ve yanlış cevabı cezalandırır; Ghūl soru sormaz, kılık değiştirir. |
| **Pishtaco** `pishtaco` | Tawantinsuyu ☉ | `function` | İkisi de yoldaki yabancıdır; Ghūl kılık değiştirir, Pishtaco zaten yabancı görünür — korku sömürünün suretini alır. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Eşek toynağı: gizlenemeyen işaret. Kitapta tekrar eden bir kalıp (Nykur'un ters toynağı, Curupira'nın ters ayağı).

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

