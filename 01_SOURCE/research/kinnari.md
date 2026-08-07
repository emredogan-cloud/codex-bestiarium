# Kinnarī — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `kinnari` |
| **Ad** | Kinnarī |
| **Alternatif yazımlar** | Kinnara (eril), Kinnaree |
| **Gelenek** | Siam ☸ · Güneydoğu Asya |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-072` |
| **Telaffuz (taslak)** | kin-nah-REE |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `catalog`

- **Künye:** *Paññāsa Jātaka*, Sudhana-Manoharā anlatısı

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Phya Anuman Rajadhon, *Essays on Thai Folklore* (Bangkok, 1968)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Kinnara”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B52` | Harpy. Bird with arms and breasts of woman | ✅ |

**Gerekçe.** B52 ('Harpy. Bird with arms and breasts of woman') doğrulandı ve korundu. Thompson'ın kaynakçasında Budist gelenek doğrudan anılır; kinnarī bu tipin Güneydoğu Asya üyesidir.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Siam ve Güneydoğu Asya; Himavanta ormanı (mitik)
- **İlk kayıt (attested):** Pali Jātaka geleneği; *Traibhumikatha* (14. yy Tayland kozmolojisi)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Belden yukarısı kadın, aşağısı kuş
- Süslü kanatlar ve kuyruk

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Himavanta ormanında yaşar ve şarkı söyler. Manohara Jātaka'sında bir kinnarī avlanır ve bir prensle evlenir.
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
| **Bennu** `bennu` | Kemet 𓂀 | `function` | İkisi de bir düzenin işaretidir ve ikisi de saldırmaz — kitabın en zararsız iki maddesi. |
| **Garuḍa** `garuda` | Bharatiya ॐ | `function` | İki kuş-insan: Garuḍa avlar, Kinnarī avlanır. |
| **Perī** `peri` | Pārs 𐎩 | `function` | İki yarı-varlık: Perī insanın aklını alır, Kinnarī yalnızca şarkı söyler. |
| **Phaya Nak** `phaya-nak` | Siam ☸ | `tradition` | Siam'ın iki Himavanta varlığı: biri ormanda şarkı söyler, öteki ırmağın altında hüküm sürer. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Harpy koduyla paylaşım tuhaf ve öğretici: Yunan harpyia yırtıcı, kinnarī şarkıcı. Aynı biçim, karşıt ahlak.

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

