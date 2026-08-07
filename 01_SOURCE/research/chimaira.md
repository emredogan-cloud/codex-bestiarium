# Chímaira — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `chimaira` |
| **Ad** | Chímaira |
| **Alternatif yazımlar** | Chimera, Chimaera |
| **Gelenek** | Hellenic Ω · Akdeniz |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-002` |
| **Telaffuz (taslak)** | KHEE-my-ra |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Homeros, *İlyada*
- **Yer:** VI.179–183

### Kaynak 2 · `primary` · doğrulama `canon`

- **Künye:** Hesiodos, *Theogonia*
- **Yer:** 319–325

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Chimaera”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B15` | Animals with unusual limbs or members | ✅ |

**Gerekçe.** B15 ('Animals with unusual limbs or members') doğrulandı ve korundu. Khimaira'yı tanımlayan şey tam olarak uzuv birleşimidir: aslan, keçi ve yılan tek gövdede.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Likya (Anadolu güneybatısı)
- **İlk kayıt (attested):** Homeros, *İlyada* VI (MÖ ~750); Hesiodos, *Theogonia*

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Önü aslan, ortası keçi, arkası yılan (Homeros)
- Ateş soluyan
- Sırtından keçi başı çıkan

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Likya'yı yakar; Bellerophontes tarafından Pegasos'un sırtından öldürülür.
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
| **Ammit** `ammit` | Kemet 𓂀 | `function` | İki bileşik gövde: Chímaira üç hayvanı yan yana taşır, Ammit üçünü tek işlevde birleştirir — yutma. |
| **Herensuge** `herensuge` | Euskal ✜ | `function` | İkisi de bir kahraman anlatısının hedefi; biri kanattan öldürülür, öteki azizle. |
| **Makara** `makara` | Bharatiya ॐ | `function` | İkisi de bileşiktir; Chímaira'nın parçaları saldırır, Makara'nınki bir eşiği süsler. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- 'Chimera' modern anlamda 'melez/hayal' demektir; bu anlam maddede kullanılmayacak.

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

