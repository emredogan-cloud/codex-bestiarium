# Way — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `way` |
| **Ad** | Way |
| **Alternatif yazımlar** | — |
| **Gelenek** | Maya 𝋠 · Mezoamerika |
| **Sınıf** | III · THE SHAPE-CHANGERS (Şekil Değiştirenler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-036` |
| **Telaffuz (taslak)** | WHY |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Klasik Maya seramik yazıtları (MS 600–900), 'way' glifi

### Kaynak 2 · `scholarly` · doğrulama `article`

- **Künye:** Stephen Houston ve David Stuart, "The Way Glyph: Evidence for Co-essences among the Classic Maya", *Research Reports on Ancient Maya Writing* 30 (Washington: Center for Maya Research, 1989)
- **Yer:** Rapor no. 30
- **Not:** Numaralı dizi yayını (Research Reports on Ancient Maya Writing 30); yer kesin ve kalıcı.

### Kaynak 3 · `scholarly` · doğrulama `catalog`

- **Künye:** Mary Miller ve Karl Taube, *An Illustrated Dictionary of the Gods and Symbols of Ancient Mexico and the Maya* (Londra: Thames & Hudson, 1993)

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `E715` | Separable soul kept in animal | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum D110 idi — ama way bir DÖNÜŞÜM değil, ayrılabilir bir ruhtur. Doğrulanan E715 ('Separable soul kept in animal') doğru koddur.

> ⚠ **Tohum kodu değiştirildi.** D110 → E715. Way dönüşmez; AYRILIR.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Maya; Yucatán, Chiapas, Guatemala yaylaları
- **İlk kayıt (attested):** Klasik dönem seramik yazıtları (MS 600–900); modern etnografi

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Her insanın hayvan eşlikçisi
- Uykuda serbest kalır
- Klasik dönem vazolarında adlandırılmış olarak resmedilir

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Uykuda bedenden ayrılır. Way'e verilen zarar sahibine de gelir.
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
| **Nahual** `nahual` | Mēxihcah ☼ | `kin` | Nahual dönüşümü SEÇER (büyücüdür), Way herkeste vardır ve uykuda serbest kalır. |
| **Tupilaq** `tupilaq` | Inuit ᐃ | `function` | Way'e verilen zarar sahibine geçer; Tupilaq zarar veremezse yapanına döner. İkisi de bir bağın bedelidir. |
| **Xtabay** `xtabay` | Maya 𝋠 | `tradition` | Maya'nın iki ruhu: biri her insanın içinde, öteki ağacın altında bekler. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

Maya toplulukları yaşayan geleneklerdir. Yalnızca yayımlanmış akademik betimleme kullanıldı; çağdaş topluluklara ait tören ve uygulayıcı bilgisi KULLANILMAZ.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Nahual ile ayrışma: Nahual dönüşür, Way ayrılır.

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

