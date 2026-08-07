# Each-uisce — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `each-uisce` |
| **Ad** | Each-uisce |
| **Alternatif yazımlar** | Aughisky, Each-uisge |
| **Gelenek** | Ériu ☘ · Kuzey Avrupa |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | A · Su atı |
| **Plaka** | `plate-016` |
| **Telaffuz (taslak)** | AKH-ish-keh |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Thomas Crofton Croker, *Fairy Legends and Traditions of the South of Ireland* (Londra: John Murray, 1825)
- **Yer:** II. cilt

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Katharine Briggs, *A Dictionary of Fairies* (Londra: Allen Lane, 1976)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Each Uisge”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B184.1.3` | Magic horse from water world | ✅ |

**Gerekçe.** B184.1.3 ('Magic horse from water world') doğrulandı ve korundu. Su atı ailesinin (A) çıpa kodu; tanım ailenin tamamını kapsıyor.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Ériu ve Alba; Connacht gölleri, Hebrides deniz gölleri
- **İlk kayıt (attested):** Croker, *Fairy Legends* (1825); 19. yy Highland derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Islak arduvaz renginde at
- Yelesi sürekli damlayan
- Kıyıda uysal duran

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Kıyıda binilmeyi bekler. Binildiğinde suya koşar; İskoçya kaydında biniciyi yer, karaciğerini kıyıya bırakır.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** —

## 6. Varyantlar

| Bölge / kaynak | Fark |
|---|---|
| İskoçya | Biniciyi yer; karaciğeri kıyıya vurur |
| İrlanda | Yalnızca boğar |

**Varyant notu.** İskoçya'da yiyicidir; İrlanda'da yalnızca boğar. Aynı tehlike, iki ahlak.

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Näkki** `nakki` | Suomi ᛉ | `kin` | Ériu'da kıyıda binilmeyi bekler; Suomi'de at, insan veya kadın kılığına girer — biçim sabit değil. |
| **Nykur** `nykur` | Ísland ❆ | `kin` | İskoçya kaydında biniciyi yer ve karaciğerini kıyıya bırakır; İzlanda'da yalnızca göle götürür. |
| **Púca** `puca` | Ériu ☘ | `tradition` | Ériu'da iki at: Púca bindirir ve bırakır, Each-uisce bindirir ve boğar. |
| **Tikbalang** `tikbalang` | Filipin ✧ | `kin` | Ailenin tek karasal üyesi: suya çekmez, yolu daireye çevirir. Su atı sudan çıkınca ne olur — cevabı budur. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Su atı ailesinin (A) çıpası ve kitabın vitrin maddesi.
- Karaciğerin kıyıya vurması: somut, sınanabilir, unutulmaz ayrıntı.

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

