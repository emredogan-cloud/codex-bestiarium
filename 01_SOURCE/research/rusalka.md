# Rusalka — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `rusalka` |
| **Ad** | Rusalka |
| **Alternatif yazımlar** | — |
| **Gelenek** | Slovjan ⚡ · Kuzey Avrupa |
| **Sınıf** | VI · THE RESTLESS DEAD (Huzursuz Ölüler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-037` |
| **Telaffuz (taslak)** | roo-SAHL-kah |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Dmitrij Zelenin, *Očerki russkoj mifologii: Umeršie neestestvennoju smert'ju i rusalki* (Petrograd, 1916)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Linda J. Ivanits, *Russian Folk Belief* (Armonk: M. E. Sharpe, 1989)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Rusalka”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F420` | Water-spirits | ✅ |

**Gerekçe.** F420 ('Water-spirits') doğrulandı ve korundu. Rusalka bir su ruhudur ve ölünün dönüşü boyutu ikincildir; Slav kaydında su bağı birincildir.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Slovjan; Ukrayna, Rusya, Belarus — ırmak ve ekin tarlaları
- **İlk kayıt (attested):** 19. yy saha derlemeleri; Rusalnaya nedelya (Rusalka Haftası) kayıtları

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Uzun çözük saçlı genç kadın
- Solgun ten
- Çıplak veya beyaz gömlekli

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Rusalka Haftası'nda sudan çıkar ve tarlalarda salınır; ekini sular. Yakaladığını gıdıklayarak veya boğarak öldürür.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** —

## 6. Varyantlar

| Bölge / kaynak | Fark |
|---|---|
| Kuzey Rusya | Çirkin, tehlikeli, yaşlı |
| Ukrayna | Genç, güzel, baştan çıkaran |

**Varyant notu.** Rusalka kuzeyde çirkin ve tehlikeli, güneyde genç ve güzeldir. Aynı ad, iki yüz.

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Iara** `iara` | Tupi-Guarani ❂ | `function` | İkisi de suda ölümle ilişkilidir; Rusalka ölmüş bir kızın DÖNÜŞÜDÜR, Iara nehrin annesidir — biri sonuç, öteki köken. |
| **Näkki** `nakki` | Suomi ᛉ | `function` | İkisi de suyun kenarında görünür; Näkki hep oradaydı, Rusalka önce bir insandı. |
| **Pontianak** `pontianak` | Nusantara ❋ | `function` | İki ölmüş kadının dönüşü: Rusalka ekini sular ve boğar, Pontianak yalnızca yeni doğana yönelir. |
| **Zmey** `zmey` | Slovjan ⚡ | `tradition` | Slovjan'ın iki ucu: biri tarlayı sular, öteki hazineyi bekler. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Hem sular hem boğar: aynı varlık bereket ve ölüm. Maddenin 5. bölümü bu.

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

