# Basajaun — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `basajaun` |
| **Ad** | Basajaun |
| **Alternatif yazımlar** | Basojaun |
| **Gelenek** | Euskal ✜ · Batı Avrupa |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | G · Yaban adamı |
| **Plaka** | `plate-061` |
| **Telaffuz (taslak)** | bah-sah-HOWN |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** José Miguel de Barandiarán, *Diccionario ilustrado de mitología vasca* (Bilbao: La Gran Enciclopedia Vasca, 1972)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Julio Caro Baroja, *Los vascos* (Madrid: Istmo, 1971)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Basajaun”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F567` | Wild man | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum F460 ('Mountain-spirits') idi; doğrulanan F567 ('Wild man') yaban adamı ailesinin (G) tam kodudur.

> ⚠ **Tohum kodu değiştirildi.** F460 → F567.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Euskal Herria; Pirene ormanları
- **İlk kayıt (attested):** José Miguel de Barandiarán derlemeleri (20. yy); 19. yy kayıtlar

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- İri, kıllı, insan benzeri
- Uzun saçlı
- Tek ayağı yuvarlak olarak da anlatılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Ormanın efendisi. Fırtına yaklaşınca ıslık çalar ve çobanı uyarır; sürüyü kurttan korur. Barandiarán'da tarım ve demirciliği insana öğreten de odur.
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
| **Curupira** `curupira` | Tupi-Guarani ❂ | `kin` | Curupira avcıyı cezalandırır, Basajaun çobanı korur. Doğanın tarafı, insanın işine göre değişir. |
| **Herensuge** `herensuge` | Euskal ✜ | `tradition` | Euskal'ın iki dağ varlığı: biri kurban ister, öteki sürüyü korur. |
| **Lamia** `lamia-euskal` | Euskal ✜ | `tradition` | Euskal'ın iki sahibi: biri ırmağın, öteki ormanın; ikisi de karşılığında iş yapar. |
| **Migoi** `migoi` | Bod ☷ | `kin` | Basajaun ıslıkla haber verir — sesiyle bilinir; Migoi görülmemek için geri geri yürür — iziyle. |
| **Stállu** `stallu` | Sápmi ❄ | `kin` | Stállu insanı avlar ve kurnazlıkla yenilir; Basajaun insana demirciliği öğretir. Ailenin ahlaki uçları. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Yaban adamı ailesinin (G) tek KORUYUCU üyesi. Ayrışma noktası ailenin açılışını taşıyacak: Basajaun uyarır, Curupira cezalandırır.

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

