# Curupira — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `curupira` |
| **Ad** | Curupira |
| **Alternatif yazımlar** | Caipora (akraba) |
| **Gelenek** | Tupi-Guarani ❂ · Amazon |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | G · Yaban adamı |
| **Plaka** | `plate-098` |
| **Telaffuz (taslak)** | koo-roo-PEE-rah |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** José de Anchieta, *Cartas, informações, fragmentos históricos e sermões* (16. yy)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Luís da Câmara Cascudo, *Dicionário do folclore brasileiro* (Rio de Janeiro: Instituto Nacional do Livro, 1954)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Curupira”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F567` | Wild man | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum F460 ('Mountain-spirits') idi; doğrulanan F567 ('Wild man') yaban adamı ailesinin (G) tam kodudur ve curupira orman adamıdır, dağ ruhu değil.

> ⚠ **Tohum kodu değiştirildi.** F460 → F567.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Tupi-Guarani; Amazon ve Brezilya ormanları
- **İlk kayıt (attested):** Sömürge dönemi Cizvit kayıtları (16. yy, José de Anchieta); 19.–20. yy derlemeler

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Ayakları TERS dönük
- Kızıl saçlı
- Çocuk boyunda

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Ormanı ve hayvanları korur. Ters ayakları iz bırakır; avcı izi takip eder ve ters yöne gider.
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
| **Basajaun** `basajaun` | Euskal ✜ | `kin` | Curupira avcıyı cezalandırır, Basajaun çobanı korur. Doğanın tarafı, insanın işine göre değişir. |
| **Boitatá** `boitata` | Tupi-Guarani ❂ | `function` | Aynı geleneğin aynı işlevi iki bedende: Curupira izi yanıltır, Boitatá ateşle kovalar. |
| **Migoi** `migoi` | Bod ☷ | `kin` | İkisi de izi yanıltır: biri ters yürüyerek, öteki ters ayakla. Aynı hile, iki ayrı anatomi. |
| **Ông Ba Mươi** `ong-ba-muoi` | Việt ☴ | `function` | İkisi de ormanın efendisidir; Ông Ba Mươi'ye saygı gösterilir, Curupira'dan kaçılır. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Amazon yerli gelenekleri YAŞAYANDIR. Yalnızca yayımlanmış derlemeler kullanıldı; belirli topluluklara ait anlatı, tören ve yer bilgisi KULLANILMAZ. Anchieta'nın misyoner çerçevesi eleştirel okunacak.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Yaban adamı ailesinin (G) Amazon üyesi ve tek CEZALANDIRAN üyesi.
- Ters ayak: Nykur'un ters toynağı ve Ghūl'ün eşek toynağıyla aynı kalıp — ama burada iz YANILTMAK için.

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

