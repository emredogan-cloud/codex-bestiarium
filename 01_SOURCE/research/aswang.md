# Aswang — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `aswang` |
| **Ad** | Aswang |
| **Alternatif yazımlar** | Asuang |
| **Gelenek** | Filipin ✧ · Güneydoğu Asya |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-073` |
| **Telaffuz (taslak)** | AHS-wahng |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Maximo D. Ramos, *The Creatures of Midnight: Faded Deities of Luzon, the Visayas and Mindanao* (Quezon City: Island Publishers, 1967)

### Kaynak 2 · `scholarly` · doğrulama `article`

- **Künye:** Frank Lynch, "An mga asuwang: A Bicol Belief", *Philippine Social Sciences and Humanities Review* 14:4 (1949), 401–427

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Aswang”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G262.1` | Witch sucks blood | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum G262 ('Murderous witch') idi; doğrulanan G262.1 ('Witch sucks blood') aswang'ın tanımlayıcı eylemini karşılıyor. Not: 'aswang' Filipinler'de bir KATEGORİ adıdır ve alt türleri kapsar.

> ⚠ **Tohum kodu değiştirildi.** G262 → G262.1.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Filipinler; Batı Visayas (özellikle Capiz, Antique, Iloilo)
- **İlk kayıt (attested):** İspanyol sömürge dönemi kayıtları (17. yy); 20. yy saha derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Gündüz sıradan bir komşu
- Gece uzun dilli veya kanatlı
- Gözbebekleri ters yansıtır (tanıma işareti)

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Gündüz komşu, gece yiyicidir. Ölüyü ve doğmamışı arar; cesedin yerine muz gövdesinden yapılmış bir kopya bırakır.
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
| **Ma lai** `ma-lai` | Việt ☴ | `kin` | Aswang cesedin yerine muz gövdesi bırakır — hile bırakır; Ma lai iz bırakmaz, yalnızca döner. |
| **Manananggal** `manananggal` | Filipin ✧ | `kin` | Aynı gelenekte iki katman: Aswang bir kategori (gündüz komşu), Manananggal onun en somut biçimi. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

⚠ Aswang suçlaması Filipinler'de GERÇEK insanlara — özellikle Capiz sakinlerine — yöneltilmiş ve damgalama üretmiştir. Madde suçlamayı yeniden üretmeyecek; Buda ve Adze maddeleriyle aynı etik dikkat uygulanacak.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Aswang bir tür değil bir KATEGORİ; madde bunu ilk cümlede söylemeli.

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

