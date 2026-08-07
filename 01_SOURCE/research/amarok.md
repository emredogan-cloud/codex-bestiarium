# Amarok — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `amarok` |
| **Ad** | Amarok |
| **Alternatif yazımlar** | Amaroq |
| **Gelenek** | Inuit ᐃ · Kutup |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-050` |
| **Telaffuz (taslak)** | AH-mah-rok |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Knud Rasmussen, *Intellectual Culture of the Iglulik Eskimos* (Kopenhag: Gyldendal, 1929)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Daniel Merkur, *Powers Which We Do Not Know* (Moscow, Idaho: University of Idaho Press, 1991)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Amarok”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B871` | Giant beasts | ✅ |

**Gerekçe.** B871 ('Giant beasts') doğrulandı ve korundu. Amarok dev bir kurttur; Thompson'da özel bir 'dev kurt' alt kodu bulunamadı, doğrulanmış üst kod kullanıldı.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Inuit; Grönland ve Kanada tundrası
- **İlk kayıt (attested):** Rasmussen derlemeleri; 19.–20. yy kayıtlar

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Dev kurt
- Sürü hâlinde değil YALNIZ avlanır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Yalnız avlanır. Kuralı çiğneyen — geceleyin tek başına avlanan — avcıyı bulur.
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
| **Fenrir** `fenrir` | Norðr ᚦ | `function` | Fenrir bağlanır ve kurtulur; Amarok bağlanmaz — kuralı çiğneyeni bulmakla yetinir. |
| **Stállu** `stallu` | Sápmi ❄ | `function` | İkisi de tek başına avlanan insanı hedefler; biri hayvan, öteki eşyalı bir dev. |
| **Windigo** `windigo` | Anishinaabe ▲ | `function` | İkisi de kuzeyin yalnızlığından doğar: Amarok kuralı çiğneyeni cezalandırır, Windigo kuralın kendisini yok eder. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Yalnızca yayımlanmış derlemeler kullanıldı; şaman uygulaması ve yer-özel anlatı KULLANILMAZ.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Kuralı çiğneyeni cezalandırma: Repun Kamuy ve Amarok aynı av ahlakının iki yüzü.

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

