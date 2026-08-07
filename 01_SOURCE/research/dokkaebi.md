# Dokkaebi — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `dokkaebi` |
| **Ad** | Dokkaebi |
| **Alternatif yazımlar** | Tokkaebi |
| **Gelenek** | Hangug 단 · Doğu Asya |
| **Sınıf** | III · THE SHAPE-CHANGERS (Şekil Değiştirenler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-033` |
| **Telaffuz (taslak)** | TOK-kay-bee |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** James H. Grayson, *Myths and Legends from Korea* (Richmond: Curzon, 2001)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Choi In-hak, *A Type Index of Korean Folktales* (Seul: Myong Ji University Press, 1979)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Tokkebi”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F400` | Spirits and demons (general) | ✅ |

**Gerekçe.** F400 ('Spirits and demons (general)') doğrulandı ve korundu. Dokkaebi belirli bir biçime veya araziye bağlı değil; eski bir NESNEDEN doğar.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Hangug; kırsal, terk edilmiş eşya
- **İlk kayıt (attested):** Choson dönemi kayıtları; 20. yy saha derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Elinde dövülmüş demir sopa (bangmangi)
- Kan bulaşmış eski süpürge veya çamaşır tokacından doğduğu anlatılır
- Tek bacaklı olarak da anlatılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Güreşe çağırır — sol tarafından yakalanırsa yenilir. Sevdiğine zenginlik, sevmediğine bela verir.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** Güreşte sol tarafından yakalamak.

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Anansi** `anansi` | Yorùbá · Ashanti ✺ | `function` | İki hilekâr: Anansi pazarlıkla kazanır, Dokkaebi güreşle kaybeder. |
| **Domovoy** `domovoy` | Slovjan ⚡ | `function` | İkisi de eşyaya ve haneye bağlıdır; Domovoy sadıktır, Dokkaebi keyfî. |
| **Kumiho** `kumiho` | Hangug 단 | `tradition` | Hangug'un iki karşılaşması: Dokkaebi güreşe çağırır ve sol tarafından yenilir, Kumiho sınar ve sınavı kendi kaybeder. |
| **Púca** `puca` | Ériu ☘ | `function` | İki keyfî varlık: ikisi de sevdiğine yardım, sevmediğine bela verir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Nesneden doğma: bu kitapta başka örneği yok.

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

