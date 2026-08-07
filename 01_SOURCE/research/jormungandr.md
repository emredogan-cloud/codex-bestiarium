# Jörmungandr — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `jormungandr` |
| **Ad** | Jörmungandr |
| **Alternatif yazımlar** | Miðgarðsormr |
| **Gelenek** | Norðr ᚦ · Kuzey Avrupa |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | E · Derinlerin yılanı |
| **Plaka** | `plate-008` |
| **Telaffuz (taslak)** | YUR-mun-gand-r |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Snorri Sturluson, *Gylfaginning*
- **Yer:** 34, 48

### Kaynak 2 · `primary` · doğrulama `canon`

- **Künye:** *Hymiskviða*
- **Yer:** 21–24

### Kaynak 3 · `scholarly` · doğrulama `catalog`

- **Künye:** John Lindow, *Norse Mythology* (Oxford: Oxford University Press, 2001)

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B11.2.1.1` | Dragon as modified serpent | ✅ |

**Gerekçe.** B11.2.1.1 ('Dragon as modified serpent') doğrulandı ve korundu. Miðgarðsormr bir ejderha değil, dünyayı çevreleyen YILANDIR.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Norðr; Miðgarðr'ı çevreleyen dış deniz
- **İlk kayıt (attested):** *Gylfaginning* (~1220); *Hymiskviða*; Gosforth ve Altuna taş kabartmaları (10.–11. yy)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Dünyayı çevreleyecek uzunlukta deniz yılanı
- Kendi kuyruğunu ısırır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Denizin dibinde yatar. Þórr onu iki kez karşılar: Hymir'in teknesinde oltayla, Ragnarök'te ölümüne.
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
| **Apep** `apep` | Kemet 𓂀 | `kin` | Jörmungandr bir kez ve son kez yenilir; Apep her sabah yeniden yenilir. Kıyamet ile döngü arasındaki fark. |
| **Fenrir** `fenrir` | Norðr ᚦ | `pair` | Kardeşler ve Ragnarök'ün iki ayrı ucu: biri Óðinn'i yutar, öteki Þórr'u zehirler. |
| **Iku-Turso** `iku-turso` | Suomi ᛉ | `kin` | İkisi de kuzey denizinin dibinde; biri yemin ettirilip gönderilir, öteki orada bekler. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Derinlerin yılanı ailesinin (E) çıpası.

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

