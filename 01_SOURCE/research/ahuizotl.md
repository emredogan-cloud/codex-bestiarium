# Ahuizotl — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `ahuizotl` |
| **Ad** | Ahuizotl |
| **Alternatif yazımlar** | — |
| **Gelenek** | Mēxihcah ☼ · Mezoamerika |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-023` |
| **Telaffuz (taslak)** | ah-WEE-sotl |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Bernardino de Sahagún, *Florentine Codex*
- **Yer:** XI. kitap (Yeryüzü Şeyleri)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Mary Miller ve Karl Taube, *An Illustrated Dictionary of the Gods and Symbols of Ancient Mexico and the Maya* (Londra: Thames & Hudson, 1993)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Ahuizotl”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B16` | Devastating animals | ✅ |

**Gerekçe.** B16 ('Devastating animals') doğrulandı ve korundu. Ahuizotl suda bekleyen ve öldüren bir hayvandır.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Mēxihcah; göl ve kanal (Tenochtitlan çevresi)
- **İlk kayıt (attested):** Sahagún, *Florentine Codex*, XI. kitap (1569)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Küçük köpek benzeri
- Kuyruğunun ucunda bir EL
- Kaygan siyah tüy

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Kuyruğundaki elle suya çeker. Sahagún'da ceset gözleri, dişleri ve tırnakları alınmış olarak bulunur.
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
| **Iara** `iara` | Tupi-Guarani ❂ | `function` | İkisi de suya çeker; Ahuizotl'un aldığı şey sayılabilir (göz, diş, tırnak), Iara'nınki sayılamaz. |
| **Kappa** `kappa` | Yamato 神 | `function` | İkisi de küçüktür ve gövdenin bir parçasını alır: biri güreşten sonra, öteki gözü ve tırnağı. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Göz, diş, tırnak: alınan üç şey. Somutluk kuralının en iyi örneklerinden.

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

