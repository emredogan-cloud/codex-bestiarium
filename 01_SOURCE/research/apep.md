# Apep — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `apep` |
| **Ad** | Apep |
| **Alternatif yazımlar** | Apophis |
| **Gelenek** | Kemet 𓂀 · Akdeniz |
| **Sınıf** | IV · THE WATER-DWELLERS (Su Sakinleri) |
| **Akraba ailesi** | E · Derinlerin yılanı |
| **Plaka** | `plate-005` |
| **Telaffuz (taslak)** | AH-pep |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Apophis Kitabı* (Bremner-Rhind Papirüsü)
- **Yer:** 24.21–26.3

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Erik Hornung, *Conceptions of God in Ancient Egypt: The One and the Many*, çev. John Baines (Ithaca: Cornell University Press, 1982)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Apep”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B11.2.1.1` | Dragon as modified serpent | ✅ |

**Gerekçe.** B11.2.1.1 ('Dragon as modified serpent') doğrulandı ve korundu. Apep bir ejderha değil, kozmik ölçekte bir YILANDIR; Thompson'ın 'değiştirilmiş yılan' alt kodu tam bu ayrımı taşır.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Kemet; güneş teknesinin gece yolculuğu, batı ufku
- **İlk kayıt (attested):** Piramit Metinleri'nden itibaren; Apophis Kitabı (Geç Dönem)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Devasa yılan
- Kıvrımları kum tepesi büyüklüğünde anlatılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Her gece güneş teknesini yutmaya çalışır; her sabah yeniden yenilir. Yenilgisi kalıcı değildir — düzenin her gün YENİDEN kurulması gerekir.
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
| **Ammit** `ammit` | Kemet 𓂀 | `tradition` | Kemet'in iki yutucusu: Apep güneşi, Ammit kalbi hedefler — biri kozmik, öteki kişisel. |
| **Cipactli** `cipactli` | Mēxihcah ☼ | `function` | İkisi de düzenin sürekli yeniden kurulmasını gerektirir: biri beslenerek, öteki yenilerek. |
| **Iku-Turso** `iku-turso` | Suomi ᛉ | `kin` | Apep'in adı her gün anılır ve lanetlenir; Iku-Turso'nun adı uğursuz sayılıp anılmaz. |
| **Jörmungandr** `jormungandr` | Norðr ᚦ | `kin` | Jörmungandr bir kez ve son kez yenilir; Apep her sabah yeniden yenilir. Kıyamet ile döngü arasındaki fark. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Derinlerin yılanı ailesinin (E) Mısır üyesi.
- Ayrışma: Jörmungandr kıyameti BEKLER, Apep her gece YENİLİR — biri bir kez, diğeri sonsuz kez.

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

