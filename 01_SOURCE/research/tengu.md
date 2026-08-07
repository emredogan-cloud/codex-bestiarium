# Tengu — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `tengu` |
| **Ad** | Tengu |
| **Alternatif yazımlar** | — |
| **Gelenek** | Yamato 神 · Doğu Asya |
| **Sınıf** | III · THE SHAPE-CHANGERS (Şekil Değiştirenler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-012` |
| **Telaffuz (taslak)** | TEN-goo |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Nihon Ryōiki*
- **Yer:** I.2 ve ilgili bölümler

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Michael Dylan Foster, *The Book of Yōkai* (Berkeley: University of California Press, 2015)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Tengu”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `D150` | Transformation: man to bird | ✅ |

**Gerekçe.** D150 ('Transformation: man to bird') doğrulandı ve korundu. Tengu'nun tanımlayıcı özelliği kuş-insan arası biçim ve dönüşümdür.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Yamato; dağlar ve dağ tapınakları
- **İlk kayıt (attested):** *Nihon Ryōiki* (9. yy); Edo dönemi derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Kanatlı
- Erken biçimde çaylak gagalı (karasu-tengu)
- Geç biçimde uzun kırmızı burunlu (daitengu)

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Dağda yaşar; kibirli rahibi ve kendini beğenmiş savaşçıyı cezalandırır. Kimi anlatıda dövüş sanatı öğretir.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** —

## 6. Varyantlar

| Bölge / kaynak | Fark |
|---|---|
| Erken kayıt | Kuş gagalı, kötücül |
| Edo dönemi | Uzun burunlu, kimi zaman öğretici |

**Varyant notu.** Tengu zamanla kötücülden öğreticiye kaydı; madde bu kaymayı gösterecek.

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Kappa** `kappa` | Yamato 神 | `tradition` | Yamato'nun iki dağ/su varlığı: ikisi de sınar, biri dövüş öğretir, öteki güreşe çağırır. |
| **Qílín** `qilin` | Zhōnghuá 龍 | `function` | Qílín adaletsizin üzerine BASMAZ; Tengu kibirliyi cezalandırır. Aynı ahlak, iki ayrı yaptırım. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- —

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

