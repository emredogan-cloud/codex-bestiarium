# Makara — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `makara` |
| **Ad** | Makara |
| **Alternatif yazımlar** | — |
| **Gelenek** | Bharatiya ॐ · Güney Asya |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-015` |
| **Telaffuz (taslak)** | MAH-kah-rah |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** *Ṛgveda* ve Purāṇa geleneği

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** J. Ph. Vogel, *Indian Serpent-Lore* (Londra: Arthur Probsthain, 1926)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Makara”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B16` | Devastating animals | ✅ |

**Gerekçe.** B16 ('Devastating animals') doğrulandı ve korundu. Makara bir bileşik su canavarıdır; B15 (olağandışı uzuvlar) de aday ama makara'nın işlevi tehlikedir, tuhaflık değil.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Bharat; ırmak ağızları, tapınak eşikleri (makara-toraṇa)
- **İlk kayıt (attested):** Vedik dönemden itibaren; Gupta dönemi tapınak süslemesi (4.–6. yy)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Timsah gövdesi
- Fil hortumu
- Balık kuyruğu

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Suyun eşiğinde durur. Ganga'nın bineği; tapınak kapılarında oyulur — geçişin işareti.
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
| **Chímaira** `chimaira` | Hellenic Ω | `function` | İkisi de bileşiktir; Chímaira'nın parçaları saldırır, Makara'nınki bir eşiği süsler. |
| **Kérberos** `kerberos` | Hellenic Ω | `function` | İkisi de bir kapıya aittir; Kérberos kapıda durur, Makara kapıya OYULUR — bekçi bir imgeye dönüşmüştür. |
| **Nāga** `naga` | Bharatiya ॐ | `tradition` | Bharatiya'nın iki su varlığı: Makara eşiği süsler, Nāga suyun altında yaşar. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Makara bir yaratık olduğu kadar bir MİMARİ öğedir; madde bunu söylemeli.

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

