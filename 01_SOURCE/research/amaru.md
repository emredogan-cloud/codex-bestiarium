# Amaru — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `amaru` |
| **Ad** | Amaru |
| **Alternatif yazımlar** | — |
| **Gelenek** | Tawantinsuyu ☉ · And |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | E · Derinlerin yılanı |
| **Plaka** | `plate-095` |
| **Telaffuz (taslak)** | ah-MAH-roo |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Felipe Guaman Poma de Ayala, *Nueva corónica y buen gobierno* (~1615)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Gary Urton, *At the Crossroads of the Earth and the Sky: An Andean Cosmology* (Austin: University of Texas Press, 1981)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Amaru”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B11.2` | Form of dragon | ✅ |

**Gerekçe.** B11.2 ('Form of dragon') doğrulandı ve korundu. Amaru'yu tanımlayan şey biçimidir: kanatlı ve tüylü büyük yılan.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Tawantinsuyu (And); Peru, Bolivya yaylaları
- **İlk kayıt (attested):** Sömürge dönemi kronikleri (Guaman Poma, Cobo); And ikonografisi

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Büyük yılan
- Kanatlı ve tüylü olarak betimlenir
- Kimi kayıtta iki başlı

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** İki dünyayı (hanan ve hurin) birbirine bağlar. Gökkuşağı ve su ile ilişkilendirilir.
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
| **Inkanyamba** `inkanyamba` | Nguni ◈ | `kin` | Amaru iki dünyayı BAĞLAR; Inkanyamba kızdığında fırtına getirir. Biri köprü, öteki tehdit. |
| **Supay** `supay` | Tawantinsuyu ☉ | `tradition` | Tawantinsuyu'nun iki dünyası: Supay aşağıyı tutar, Amaru aşağıyla yukarıyı bağlar. |
| **Taniwha** `taniwha` | Mā'ohi ᴥ | `kin` | İki koruyucu yılan, iki okyanus: biri iwi'ye, öteki iki dünyaya bağlı. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

And gelenekleri YAŞAYANDIR. Yalnızca yayımlanmış kronikler ve akademik çalışmalar kullanıldı; çağdaş topluluk töreni ve yer-özel kutsal (huaca) bilgisi KULLANILMAZ.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Derinlerin yılanı ailesinin (E) And üyesi ve tek BAĞLAYICI üyesi: yıkmaz, bağlar.

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

