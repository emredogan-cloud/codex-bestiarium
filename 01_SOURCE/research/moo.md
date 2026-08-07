# Moʻo — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `moo` |
| **Ad** | Moʻo |
| **Alternatif yazımlar** | Mo'o |
| **Gelenek** | Mā'ohi ᴥ · Okyanusya |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-047` |
| **Telaffuz (taslak)** | MO-oh |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Abraham Fornander, *Fornander Collection of Hawaiian Antiquities and Folk-Lore* (Honolulu: Bishop Museum Press, 1916–20)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Martha Beckwith, *Hawaiian Mythology* (New Haven: Yale University Press, 1940)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Moo”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B91` | Mythical serpent | ✅ |

**Gerekçe.** B91 ('Mythical serpent') doğrulandı ve korundu. Moʻo büyük bir kertenkele/sürüngen ruhtur; B91.1 ('Naga') Hint bağlamına özgü olduğu için üst kod kullanıldı.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Hawaiʻi; tatlı su gölcükleri (loko), balık havuzları
- **İlk kayıt (attested):** 19. yy Hawaii derlemeleri (Fornander, Kamakau)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Büyük siyah kertenkele
- Kimi anlatıda kadın biçiminde

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Gölcükleri ve balık havuzlarını bekler. Suyun ve soy bağının koruyucusu; sularının rengi onun varlığını gösterir.
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
| **Adaro** `adaro` | Melanesia ◉ | `function` | İki Pasifik su varlığı: Adaro açık denizde vurur, Moʻo gölcüğü bekler. |
| **Ponaturi** `ponaturi` | Mā'ohi ᴥ | `tradition` | Maohi'nin iki su varlığı: biri gelir ve tehdittir, öteki kalır ve korur. |
| **Repun Kamuy** `repun-kamuy` | Ainu ᚼ | `function` | İkisi de suyun ve soyun sahibidir; Repun Kamuy av bağışlar, Moʻo yalnızca korur. |
| **Taniwha** `taniwha` | Mā'ohi ᴥ | `function` | İki Pasifik koruyucusu: Moʻo suyun rengiyle bilinir, Taniwha kabile ilişkisiyle. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

⚠ Hawaii geleneği YAŞAYANDIR. Belirli bir moʻo'nun adı, yeri ve ona bağlı ʻohana (aile) bağı KULLANILMAZ. Yalnızca yayımlanmış derleme ve akademik betimleme kullanılır; mele (şarkı) ve pule (dua) aktarılmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Su ve soy bağı: moʻo bir yer koruyucusu olduğu kadar bir SOY işaretidir.

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

