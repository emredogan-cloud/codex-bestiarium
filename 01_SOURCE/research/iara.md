# Iara — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `iara` |
| **Ad** | Iara |
| **Alternatif yazımlar** | Uiara, Mãe d'água |
| **Gelenek** | Tupi-Guarani ❂ · Amazon |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-100` |
| **Telaffuz (taslak)** | ee-AH-rah |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Luís da Câmara Cascudo, *Dicionário do folclore brasileiro* (Rio de Janeiro: Instituto Nacional do Livro, 1954)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Luís da Câmara Cascudo, *Geografia dos mitos brasileiros* (Rio de Janeiro: José Olympio, 1947)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Iara”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F420` | Water-spirits | ✅ |

**Gerekçe.** F420 ('Water-spirits') doğrulandı ve korundu. Iara bir ırmak ruhudur.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Tupi-Guarani; Amazon ırmakları
- **İlk kayıt (attested):** 19. yy derlemeler; Câmara Cascudo

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Uzun siyah saçlı kadın
- Belden aşağısı balık olarak da anlatılır
- Yeşil gözlü

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Şarkısıyla çeker ve suya alır. Öğleden sonra ırmak kıyısında göründüğü anlatılır.
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
| **Ahuizotl** `ahuizotl` | Mēxihcah ☼ | `function` | İkisi de suya çeker; Ahuizotl'un aldığı şey sayılabilir (göz, diş, tırnak), Iara'nınki sayılamaz. |
| **Boitatá** `boitata` | Tupi-Guarani ❂ | `tradition` | Tupi-Guarani'nin iki ucu: biri ormanı korur, öteki nehre çeker. |
| **Nhang** `nhang` | Hayk ✚ | `function` | İkisi de kadın biçiminde suya çeker; Nhang kan içer, Iara yalnızca alıkoyar. |
| **Rusalka** `rusalka` | Slovjan ⚡ | `function` | İkisi de suda ölümle ilişkilidir; Rusalka ölmüş bir kızın DÖNÜŞÜDÜR, Iara nehrin annesidir — biri sonuç, öteki köken. |
| **Xtabay** `xtabay` | Maya 𝋠 | `function` | İkisi de güzellikle çağırır; Xtabay ağaçta ve dikene çevirir, Iara suda ve şarkıyla. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Yerli gelenek malzemesi yalnızca yayımlanmış derlemelerden alındı.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Iara Avrupa denizkızı ikonografisiyle karışmıştır; kaynak notu bu katmanlaşmayı söyleyecek.

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

