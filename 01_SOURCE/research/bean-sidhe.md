# Bean sídhe — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `bean-sidhe` |
| **Ad** | Bean sídhe |
| **Alternatif yazımlar** | Banshee, Bean chaointe |
| **Gelenek** | Ériu ☘ · Kuzey Avrupa |
| **Sınıf** | VI · THE RESTLESS DEAD (Huzursuz Ölüler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-017` |
| **Telaffuz (taslak)** | ban SHEE |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Patricia Lysaght, *The Banshee: The Irish Supernatural Death-Messenger* (Dublin: Glendale Press, 1986)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Katharine Briggs, *A Dictionary of Fairies* (Londra: Allen Lane, 1976)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Banshee”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `E402` | Mysterious ghostlike noises heard. Song, animal cries, footsteps, etc. | ✅ |

**Gerekçe.** E402 ('Mysterious ghostlike noises heard. Song, animal cries, footsteps, etc.') doğrulandı ve korundu. Bean sídhe bir görüntü değil bir SEStir; kod tam olarak bunu tasnif eder.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Ériu; belirli ailelere bağlı (Ó Briain, Ó Néill, Ó Conchobhair)
- **İlk kayıt (attested):** 17. yy'dan itibaren yazılı kayıt; 19.–20. yy saha derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Çoğunlukla görülmez, duyulur
- Görüldüğünde saçını tarayan kadın

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Ölümden önce ağıt yakar. Bir aileye bağlıdır ve o ailenin ölümünü haber verir.
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
| **Àbíkú** `abiku` | Yorùbá · Ashanti ✺ | `function` | İkisi de ölümü ADLA bağlar: Bean sídhe bir aileye, Àbíkú bir anneye — biri haber verir, öteki tekrarlar. |
| **Lemures** `lemures` | Romana SPQR | `function` | Bean sídhe'nin sesi duyulur ve hiçbir şey yapılamaz; Lemures'e karşı yapılacak dokuz adımlık bir tören vardır. |
| **Púca** `puca` | Ériu ☘ | `tradition` | İkisi de habercidir; Púca'nın haberi belirsiz, Bean sídhe'ninki kesindir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Huzursuz ölüler sınıfında ama kendisi ölü DEĞİL; haberci. Faz 2'de sınıf gözden geçirilmeli.

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

