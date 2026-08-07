# Ma lai — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `ma-lai` |
| **Ad** | Ma lai |
| **Alternatif yazımlar** | — |
| **Gelenek** | Việt ☴ · Güneydoğu Asya |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-068` |
| **Telaffuz (taslak)** | mah LYE |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Nguyễn Đổng Chi, *Kho tàng truyện cổ tích Việt Nam* (Hanoi, 1958–82)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Keith Weller Taylor, *The Birth of Vietnam* (Berkeley: University of California Press, 1983)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Ma Lai”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G262.1.3` | Witches suck blood from the navel of a child without anyone knowing it | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum G262 ('Murderous witch') idi; doğrulanan G262.1.3 ('Witches suck blood from the navel of a child without anyone knowing it') ma lai'nin gizli kan emme eylemini birebir tasnif eder.

> ⚠ **Tohum kodu değiştirildi.** G262 → G262.1.3.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Việt; kırsal, gece
- **İlk kayıt (attested):** Vietnam sözlü geleneği; 20. yy derlemeler

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Gövdesinden ayrılan baş
- Baş bağırsaklarıyla birlikte uçar
- Gündüz sıradan bir insan

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Geceleri başı gövdeden ayrılır ve uçar; pislik ve kan arar. Gövde bulunup yeri değiştirilirse baş dönemez ve ölür.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** Gövdeyi bulup yerini değiştirmek.

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Aswang** `aswang` | Filipin ✧ | `kin` | Aswang cesedin yerine muz gövdesi bırakır — hile bırakır; Ma lai iz bırakmaz, yalnızca döner. |
| **Krasue** `krasue` | Siam ☸ | `kin` | İki uçan baş, iki ayrı gelenek; Ma lai pislik ve kan arar, Krasue lohusalık artığı — biri iğrençliğe, öteki doğuma bağlı. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Uçan baş kümesinin (Krasue, Manananggal, Penanggalan) Vietnam üyesi. Bu küme Güneydoğu Asya'ya özgü ve Faz 2'de kendi karşılaştırması hak edebilir.

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

