# Lamashtu — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `lamashtu` |
| **Ad** | Lamashtu |
| **Alternatif yazımlar** | — |
| **Gelenek** | Sumer 𒀭 · Yakın Doğu |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-021` |
| **Telaffuz (taslak)** | lah-MASH-too |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Lamaštu serisi tabletleri ve muska metinleri (Eski Babil–Yeni Asur)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Jeremy Black ve Anthony Green, *Gods, Demons and Symbols of Ancient Mesopotamia: An Illustrated Dictionary* (Londra: British Museum Press, 1992)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Lamashtu”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G442` | Child-stealing demon | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum G264 ('La Belle Dame Sans Merci') idi — Lamashtu erkekleri baştan çıkarmaz, ÇOCUK ÇALAR. Doğrulanan G442 ('Child-stealing demon') tam tanımdır. G302.9.4 ('Demons injure and strangle little children') da uygundur ve maddede anılacak.

> ⚠ **Tohum kodu değiştirildi.** G264 → G442. Ayrıntı: SCOPE_DECISIONS.md § 5①.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Sumer/Akkad/Asur; doğum odası
- **İlk kayıt (attested):** Eski Babil dönemi muskaları (MÖ ~1800'den itibaren); Lamaštu serisi tabletleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Aslan başlı
- Eşek dişli
- Kuş pençeli
- Göğsünde köpek ve domuz emzirirken betimlenir

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Loğusanın yanına sokulur; çocuğu emzirir gibi yapıp kaçırır. Muskalarla ve Pazuzu figürüyle uzaklaştırılır.
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
| **Lámia** `lamia-hellenic` | Hellenic Ω | `kin` | Lámia bir cezadır — kaybettiği çocukların yerine başkasını alır; Lamashtu bir iblistir ve kaybetmemiştir. |
| **Lilith** `lilith` | Talmud ✡ | `kin` | İkisi de muskayla karşılanır: biri Pazuzu figürüyle, öteki üç melek adıyla. Karşı önlem yazıya geçmiştir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Gece cadısı ailesinin (C) en eski KAYITLI üyesi — muskalar MÖ 2. binyıla iner.
- Pazuzu ile ilişkisi: bir iblisin başka bir iblisle kovulması. Maddenin 5. bölümü.

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

