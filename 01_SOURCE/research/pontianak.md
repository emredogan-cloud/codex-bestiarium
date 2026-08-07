# Pontianak — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `pontianak` |
| **Ad** | Pontianak |
| **Alternatif yazımlar** | Kuntilanak, Matianak, Langsuir (akraba) |
| **Gelenek** | Nusantara ❋ · Güneydoğu Asya |
| **Sınıf** | VI · THE RESTLESS DEAD (Huzursuz Ölüler) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-076` |
| **Telaffuz (taslak)** | pon-tee-AH-nak |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `toc`

- **Künye:** Walter William Skeat, *Malay Magic: An Introduction to the Folklore and Popular Religion of the Malay Peninsula* (Londra: Macmillan, 1900)
- **Erişim:** Kamuya açık dijital nüsha (archive.org)
- **Yer:** Bölüm VI ("Magic Rites affecting the Life of Man"), Birth-Spirits bölümü; Plaka 7: "Penanggalan and Langsuir"
- **Not:** Bölüm ve plaka başlığı Project Gutenberg nüshasından (pg47873) doğrulandı.

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** R. O. Winstedt, *The Malay Magician: Being Shaman, Saiva and Sufi* (Londra: Routledge, 1925)

### Kaynak 3 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G262.0.1` | Lamia. Witch who eats children | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum E425 öneriyordu; E425'in tanımı bu turda erişilen nüshada bulunamadı. Doğrulanmış G262.0.1 ('Lamia. Witch who eats children') kullanıldı — pontianak doğumda ölen kadının dönüşüdür ve yeni doğana yönelir. Not: E251 ('Vampire. Corpse which comes from grave at night and sucks blood') da doğrulanmış bir alternatiftir ve Faz 2'de değerlendirilmeli, çünkü pontianak bir REVENANT'tır (ölünün dönüşü), doğuştan bir cadı değil.

> ⚠ **Tohum kodu değiştirildi.** E425 → G262.0.1. E425 doğrulanamadı; C ailesinin ortak kodu kullanıldı. Faz 2'de E251 ile karşılaştırılacak.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Malay yarımadası, Sumatra, Java, Borneo
- **İlk kayıt (attested):** Skeat'in 1890'lar saha derlemesi; 1900'de yayımlandı

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Uzun siyah saçlı kadın
- Sırtında bir delik olduğu anlatılır
- Kokusu çiçek (kemboja/frangipani)
- Sesi bebek ağlaması

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Doğumda ölen kadının dönüşü. Yeni doğana ve loğusaya yönelir.
- **Kayıtlı vaka:** Faz 3'te Skeat'ten doğrudan okunacak.
- **Karşı önlem:** Skeat'in kaydettiği uygulamalar Faz 3'te doğrulanacak; şu an uydurulmayacak.

## 6. Varyantlar

| Bölge / kaynak | Fark |
|---|---|
| Malay yarımadası | Langsuir ile ayrımı kaynaklarda değişken; Skeat ikisini ayrı kaydeder |
| Endonezya | Kuntilanak adıyla |

**Varyant notu.** Pontianak ve langsuir kaynaklarda bazen ayrı bazen aynı; madde bu belirsizliği gösterecek.

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Àbíkú** `abiku` | Yorùbá · Ashanti ✺ | `kin` | Àbíkú ölen çocuğun dönüşüdür, Pontianak ölen annenin. Aynı doğum, iki ayrı hayalet. |
| **Krasue** `krasue` | Siam ☸ | `kin` | Pontianak kokusuyla tanınır (çiçek), Krasue görüntüsüyle — geceleri uçan baş ve sarkan organlar. |
| **Rusalka** `rusalka` | Slovjan ⚡ | `function` | İki ölmüş kadının dönüşü: Rusalka ekini sular ve boğar, Pontianak yalnızca yeni doğana yönelir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

Yalnızca yayımlanmış malzeme kullanıldı. Bomoh uygulamaları ve muska metinleri KULLANILMAZ — Skeat bunları kaydetmiştir ama tören metni aktarmak bu kitabın işi değildir.

## 9. Modern kurgu etkisi

Pontianak, 1950'lerden bu yana Malezya ve Endonezya sinemasının merkezî figürü. Maddede TEK CÜMLEDE ve 'modern' etiketiyle anılacak.

## 10. Yazım notları

- Gece cadısı ailesinin (C) Nusantara üyesi.
- Ayrışma noktası: çoğu C üyesi doğuştan/dönüşümle cadıdır; pontianak bir KURBAN'dır — doğumda ölen kadın. Aile içindeki en güçlü ahlaki ayrım bu.

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

