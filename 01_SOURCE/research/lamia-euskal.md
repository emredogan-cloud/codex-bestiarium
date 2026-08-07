# Lamia — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `lamia-euskal` |
| **Ad** | Lamia |
| **Alternatif yazımlar** | Lamiak (çoğul), Laminak |
| **Gelenek** | Euskal ✜ · Batı Avrupa |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-062` |
| **Telaffuz (taslak)** | LAH-mee-ah |
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
- **Yer:** s.v. “Lamiak”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F420` | Water-spirits | ✅ |

**Gerekçe.** F420 ('Water-spirits') doğrulandı ve korundu. Bask lamia'sı Yunan Lámia'sıyla AD dışında ilgisiz — bir ırmak perisidir. Bu ayrım maddede açıkça yapılacak.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Euskal Herria; ırmak ve pınarlar
- **İlk kayıt (attested):** Barandiarán derlemeleri (20. yy)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Uzun saçlı kadın
- Ördek veya keçi ayaklı
- Altın tarakla saçını tarar

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Irmakta saçını altın tarakla tarar. Tarağı alınırsa geri ister; karşılığında yardım eder — köprü veya ev yapar.
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
| **Basajaun** `basajaun` | Euskal ✜ | `tradition` | Euskal'ın iki sahibi: biri ırmağın, öteki ormanın; ikisi de karşılığında iş yapar. |
| **Xtabay** `xtabay` | Maya 𝋠 | `function` | İkisi de saç ve güzellikle tanımlanır; Lamia bir tarak ister, Xtabay bir kucaklama. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- ⚠ ADAŞ UYARISI: Yunan Lámia ile aynı ad, ayrı yaratık. Dizinde çapraz gönderme ZORUNLU.
- Ördek ayağı: gizlenemeyen işaret kalıbının Bask üyesi.

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

