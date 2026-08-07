# Ponaturi — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `ponaturi` |
| **Ad** | Ponaturi |
| **Alternatif yazımlar** | — |
| **Gelenek** | Mā'ohi ᴥ · Okyanusya |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-048` |
| **Telaffuz (taslak)** | po-nah-TOO-ree |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** George Grey, *Polynesian Mythology* (Londra: John Murray, 1855)
- **Yer:** Tāwhaki döngüsü

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Margaret Orbell, *The Illustrated Encyclopedia of Māori Myth and Legend* (Christchurch: Canterbury University Press, 1995)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Ponaturi”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G300` | Other ogres | ✅ |

**Gerekçe.** G300 ('Other ogres') doğrulandı ve korundu. Ponaturi belirli bir Thompson alt koduna oturmayan bir deniz halkıdır; doğrulanmamış dar kod yerine doğrulanmış üst kod kullanıldı.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Aotearoa; deniz ve kıyı
- **İlk kayıt (attested):** Grey, *Polynesian Mythology* (1855); Māori sözlü geleneği

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- İnsan benzeri deniz halkı
- Yeşilimsi ten olarak anlatılır
- Gün ışığına dayanamaz

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Gündüz denizde saklanır, geceleri karaya çıkar ve uyur. Anlatıda Tāwhaki, evin kepenklerini açıp gün ışığını içeri alarak onları yok eder.
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
| **Adaro** `adaro` | Melanesia ◉ | `function` | İki deniz halkı: Ponaturi ışıktan ölür, Adaro ışığı silah olarak kullanır. |
| **Moʻo** `moo` | Mā'ohi ᴥ | `tradition` | Maohi'nin iki su varlığı: biri gelir ve tehdittir, öteki kalır ve korur. |
| **Taniwha** `taniwha` | Mā'ohi ᴥ | `function` | Ponaturi denizden karaya çıkar; Taniwha nehir ağzında durur — biri istila, öteki sınır. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

⚠ Māori anlatı geleneği yaşayandır; iwi-özel anlatı ve whakapapa KULLANILMAZ. Yalnızca yayımlanmış derleme kullanıldı.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Gün ışığıyla öldürme: kitaptaki en eski 'vampir mantığı' örneklerinden ve Avrupa dışından.

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

