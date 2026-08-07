# Kumiho — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `kumiho` |
| **Ad** | Kumiho |
| **Alternatif yazımlar** | — |
| **Gelenek** | Hangug 단 · Doğu Asya |
| **Sınıf** | III · THE SHAPE-CHANGERS (Şekil Değiştirenler) |
| **Akraba ailesi** | B · Tilki kadın |
| **Plaka** | `plate-031` |
| **Telaffuz (taslak)** | KOO-mee-ho |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** *Samguk yusa* (Üç Krallığın Anıları, İlyeon, ~1281)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** James H. Grayson, *Myths and Legends from Korea: An Annotated Compendium of Ancient and Modern Materials* (Richmond: Curzon, 2001)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Kumiho”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `D113.3` | Transformation man to fox | ✅ |
| `G262.5` | Witch takes out man's liver | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum D113.1 ('man to WOLF') idi; kumiho tilkidir. Doğrulanan D113.3 ('Transformation man to fox') doğru koddur. İkinci kod G262.5 ('Witch takes out man's liver') eklendi — kumiho'nun tanımlayıcı eylemi budur ve Thompson'ın tanımı birebir uyuyor.

> ⚠ **Tohum kodu değiştirildi.** D113.1 → D113.3 + G262.5.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Hangug; dağ ve mezarlık
- **İlk kayıt (attested):** *Samguk yusa* (13. yy) ve sonrası; 19.–20. yy sözlü derlemeler

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Dokuz kuyruklu tilki
- Kadın biçimine girdiğinde kuyruk gizlenir
- İnsan olmak için bin yıl beklediği anlatılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** İnsan olmak için karaciğer yer. Kimi anlatıda insan olma sınavını son anda kaybeder.
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
| **Dokkaebi** `dokkaebi` | Hangug 단 | `tradition` | Hangug'un iki karşılaşması: Dokkaebi güreşe çağırır ve sol tarafından yenilir, Kumiho sınar ve sınavı kendi kaybeder. |
| **Húli jīng** `huli-jing` | Zhōnghuá 龍 | `kin` | Húli jīng insandan ömür alır ve kimi anlatıda sadık kalır; kumiho insan OLMAK için karaciğer yer ve sınavı kaybeder. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Tilki kadın ailesinin (B) Kore üyesi. Ayrışma: Húli jīng ÖMÜR toplar, Kumiho KARACİĞER yer — biri soyut, diğeri cerrahi.

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

