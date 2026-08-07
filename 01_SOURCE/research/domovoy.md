# Domovoy — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `domovoy` |
| **Ad** | Domovoy |
| **Alternatif yazımlar** | Domovoi, Domovik |
| **Gelenek** | Slovjan ⚡ · Kuzey Avrupa |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-039` |
| **Telaffuz (taslak)** | do-mo-VOY |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** Aleksandr Afanasyev, *Poetičeskie vozzrenija slavjan na prirodu* (Moskova, 1865–69)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Linda J. Ivanits, *Russian Folk Belief* (Armonk: M. E. Sharpe, 1989)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Domovoi”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F482` | Brownie (nisse) | ✅ |

**Gerekçe.** TOHUM KODU DARALTILDI. Tohum F480 ('House-spirits') bölüm başlığıydı; doğrulanan F482 ('Brownie (nisse)') Domovoy'un tam karşılığı olan ev ruhu tipini tasnif eder.

> ⚠ **Tohum kodu değiştirildi.** F480 → F482.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Slovjan; Rus köy evi, ocak altı
- **İlk kayıt (attested):** 19. yy saha derlemeleri; Zelenin ve Afanasyev

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Küçük, kıllı yaşlı adam
- Ev sahibine benzediği anlatılır
- Ocağın altında veya eşikte yaşar

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Evi ve hayvanları korur. Taşınırken ocaktan kor alınıp yeni eve götürülür — yoksa geride kalır ve ev çöker.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** Taşınırken kor taşımak; ekmek ve tuz bırakmak.

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Dokkaebi** `dokkaebi` | Hangug 단 | `function` | İkisi de eşyaya ve haneye bağlıdır; Domovoy sadıktır, Dokkaebi keyfî. |
| **Huldufólk** `huldufolk` | Ísland ❆ | `function` | Biri evin İÇİNDE saklı, öteki kayanın içinde; ikisi de taşınırken hesaba katılır. |
| **Lemures** `lemures` | Romana SPQR | `function` | İkisi de eve bağlıdır: Domovoy beslenir ve kalır, Lemures yatıştırılır ve gönderilir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Kitaptaki tek KORUYUCU ev ruhu. Bekçiler sınıfının en evcil üyesi.

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

