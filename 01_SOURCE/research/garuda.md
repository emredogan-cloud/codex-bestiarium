# Garuḍa — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `garuda` |
| **Ad** | Garuḍa |
| **Alternatif yazımlar** | — |
| **Gelenek** | Bharatiya ॐ · Güney Asya |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | D · Fırtına kuşu |
| **Plaka** | `plate-013` |
| **Telaffuz (taslak)** | gah-ROO-da |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Mahabharata*
- **Yer:** I (Ādi Parva), Astika Parva, 14–34

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Wendy Doniger O'Flaherty, *Hindu Myths: A Sourcebook* (Harmondsworth: Penguin, 1975)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Garuda”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B56` | Garuda-bird. Lower part man, upper part bird | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum B31 idi; doğrulama B31'in bölüm başlığı (Giant birds), B31.1'in ise 'Roc' olduğunu gösterdi. Garuḍa'nın KENDİ kodu var: B56 'Garuda-bird. Lower part man, upper part bird'.

> ⚠ **Tohum kodu değiştirildi.** B31 → B56. Ayrıntı: SCOPE_DECISIONS.md § 5②.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Bharat; Vişnu tapımı, Güneydoğu Asya'ya yayılmış
- **İlk kayıt (attested):** *Mahabharata* (MÖ 4. yy – MS 4. yy), Astika Parva

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Alt gövdesi insan, üst gövdesi kuş (Thompson'ın tanımı)
- Altın renkli
- Kanat çırpışı fırtına

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Yılanların (nāga) ezelî düşmanı. Annesini kölelikten kurtarmak için amrita'yı çalar; Vişnu'nun bineği olur.
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
| **Khyung** `khyung` | Bod ☷ | `kin` | İkisi de pençesinde yılan tutar; Garuḍa'nınki bir düşmanlık, Khyung'unki bir kozmik düzen işareti. |
| **Kinnarī** `kinnari` | Siam ☸ | `function` | İki kuş-insan: Garuḍa avlar, Kinnarī avlanır. |
| **Sīmurgh** `simurgh` | Pārs 𐎩 | `kin` | Sīmurgh çağrılır (tüy yakılır), Garuḍa binilir. Biri danışman, öteki taşıt. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Fırtına kuşu ailesinin (D) Güney Asya üyesi. Ayrışma: Garuḍa'nın düşmanlığı KİŞİSELdir — annesinin esareti.

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

