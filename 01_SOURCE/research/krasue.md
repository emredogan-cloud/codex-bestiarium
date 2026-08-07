# Krasue — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `krasue` |
| **Ad** | Krasue |
| **Alternatif yazımlar** | Kasu, Ap (Kamboçya), Phi Krasue |
| **Gelenek** | Siam ☸ · Güneydoğu Asya |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-071` |
| **Telaffuz (taslak)** | krah-SOO-eh |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Phya Anuman Rajadhon, *Essays on Thai Folklore* (Bangkok: Thai Inter-Religious Commission for Development, 1968)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Justin Thomas McDaniel, *The Lovelorn Ghost and the Magical Monk* (New York: Columbia University Press, 2011)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Krasue”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G262.1` | Witch sucks blood | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum G262 ('Murderous witch') idi; doğrulanan G262.1 ('Witch sucks blood') krasue'nin tanımlayıcı eylemini karşılıyor.

> ⚠ **Tohum kodu değiştirildi.** G262 → G262.1.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Siam (Tayland); kırsal, gece
- **İlk kayıt (attested):** Tayland sözlü geleneği; 20. yy derlemeler

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Gövdeden ayrılmış kadın başı
- Baştan sarkan iç organlar (mide, bağırsak, akciğer)
- Geceleri parlar

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Geceleri uçar; doğum yapanın kanını ve lohusalık artıklarını arar. Gövdesi gizli bir yerde bekler.
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
| **Ma lai** `ma-lai` | Việt ☴ | `kin` | İki uçan baş, iki ayrı gelenek; Ma lai pislik ve kan arar, Krasue lohusalık artığı — biri iğrençliğe, öteki doğuma bağlı. |
| **Manananggal** `manananggal` | Filipin ✧ | `kin` | Krasue'nin gövdesi bir yerde bekler, Manananggal'ın alt yarısı; ikisi de gövde bulunursa ölür. |
| **Pontianak** `pontianak` | Nusantara ❋ | `kin` | Pontianak kokusuyla tanınır (çiçek), Krasue görüntüsüyle — geceleri uçan baş ve sarkan organlar. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Krasue, Tayland korku sinemasının merkezî figürü. Tek cümlede ve 'modern' etiketiyle anılacak.

## 10. Yazım notları

- Uçan baş kümesinin (Ma lai, Manananggal, Penanggalan) Tayland üyesi.

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

