# Bennu — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `bennu` |
| **Ad** | Bennu |
| **Alternatif yazımlar** | — |
| **Gelenek** | Kemet 𓂀 · Akdeniz |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | D · Fırtına kuşu |
| **Plaka** | `plate-006` |
| **Telaffuz (taslak)** | BEN-noo |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Herodotos, *Historiai*
- **Yer:** II.73

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Rudolf Anthes, "Mythology in Ancient Egypt", *Mythologies of the Ancient World* içinde, yay. haz. S. N. Kramer (New York: Doubleday, 1961)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Bennu”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B32` | Phoenix. Renews its youth at advanced age | ✅ |

**Gerekçe.** B32 ('Phoenix. Renews its youth at advanced age') doğrulandı ve korundu. Yunan phoinix'inin Mısır karşılığı olarak zaten bu kod altında tasniflenir.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Kemet; Heliopolis (Iunu) tapınağı, benben taşı
- **İlk kayıt (attested):** Piramit Metinleri (MÖ ~2400); Herodotos II.73

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Balıkçıl (heron) biçiminde
- İki uzun tüy taşıyan başlık
- Kendi külünden doğduğu anlatılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Zamanın başlangıcını işaretler; ilk tepe üzerine konar. Yeniden doğuş döngüsünün ölçüsüdür.
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
| **Kinnarī** `kinnari` | Siam ☸ | `function` | İkisi de bir düzenin işaretidir ve ikisi de saldırmaz — kitabın en zararsız iki maddesi. |
| **Sīmurgh** `simurgh` | Pārs 𐎩 | `kin` | Bennu zamanın başlangıcını işaretler, Sīmurgh bir ömrü taşır — biri kozmik takvim, öteki kişisel kader. |
| **Ziz** `ziz` | Talmud ✡ | `kin` | İkisi de kozmolojiyi doldurmak için var: Bennu ilk tepeye konar, Ziz üçlünün gök ayağıdır. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Fırtına kuşu ailesinin (D) Mısır üyesi ama fırtına değil ZAMAN kuşu; ayrışma noktası bu.

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

