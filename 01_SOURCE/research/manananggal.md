# Manananggal — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `manananggal` |
| **Ad** | Manananggal |
| **Alternatif yazımlar** | Mananangal |
| **Gelenek** | Filipin ✧ · Güneydoğu Asya |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-074` |
| **Telaffuz (taslak)** | mah-nah-nahng-GAHL |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Maximo D. Ramos, *The Creatures of Midnight* (Quezon City: Island Publishers, 1967)

### Kaynak 2 · `scholarly` · doğrulama `article`

- **Künye:** Frank Lynch, "An mga asuwang: A Bicol Belief", *Philippine Social Sciences and Humanities Review* 14:4 (1949), 401–427

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Manananggal”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G262.1` | Witch sucks blood | ✅ |

**Gerekçe.** TOHUM KODU DOĞRULANDI ve korundu. G262.1 ('Witch sucks blood') manananggal'ın eylemini karşılıyor. Adı Tagalogca 'tanggal' (ayrılmak) kökünden gelir ve gövdenin ikiye ayrılması tanımlayıcıdır.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Filipinler; Visayas ve Luzon
- **İlk kayıt (attested):** İspanyol sömürge dönemi kayıtları; Ramos derlemeleri (20. yy)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Belden ayrılan üst gövde
- Yarasa kanatları
- Uzun hortum benzeri dil

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Geceleri belinden ayrılır ve uçar; gebe kadınların ceninlerini hortumuyla emer. Alt gövdesi gizli bir yerde bekler.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** Alt gövdeye tuz veya kül dökmek — üst gövde geri dönemez.

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Aswang** `aswang` | Filipin ✧ | `kin` | Aynı gelenekte iki katman: Aswang bir kategori (gündüz komşu), Manananggal onun en somut biçimi. |
| **Krasue** `krasue` | Siam ☸ | `kin` | Krasue'nin gövdesi bir yerde bekler, Manananggal'ın alt yarısı; ikisi de gövde bulunursa ölür. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

Aswang kategorisiyle aynı etik dikkat: suçlama yeniden üretilmeyecek.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Gece cadısı ailesinin (C) en anatomik üyesi: ayrılma noktası GÖRÜNÜR.

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

