# Impundulu — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `impundulu` |
| **Ad** | Impundulu |
| **Alternatif yazımlar** | — |
| **Gelenek** | Nguni ◈ · Afrika |
| **Sınıf** | V · SKY AND STORM (Gök ve Fırtına) |
| **Akraba ailesi** | D · Fırtına kuşu |
| **Plaka** | `plate-090` |
| **Telaffuz (taslak)** | im-poon-DOO-loo |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** W. D. Hammond-Tooke, *Bhaca Society: A People of the Transkeian Uplands, South Africa* (Kapstadt: Oxford University Press, 1962)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Axel-Ivar Berglund, *Zulu Thought-Patterns and Symbolism* (Londra: Hurst, 1976)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Impundulu”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `A284.2` | Thunderbird | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum B31.1 ('Roc') idi — impundulu yük taşıyan dev kuş değil ŞİMŞEK kuşudur. Doğrulanan A284.2 ('Thunderbird') tam tanımdır.

> ⚠ **Tohum kodu değiştirildi.** B31.1 → A284.2.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Nguni (Xhosa, Zulu); Güney Afrika
- **İlk kayıt (attested):** 19.–20. yy saha derlemeleri; Hammond-Tooke

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Beyaz ve siyah kuş
- İnsan boyunda anlatılır
- Şimşek çaktığında indiği söylenir

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Şimşeği çağırır. Bir büyücüye bağlıdır ve kan ister; beslenmezse sahibine döner.
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
| **Animikii** `animikii` | Anishinaabe ▲ | `kin` | Animikii gök gürültüsünü GETİRİR; Impundulu şimşeği ÇAĞIRIR ve bir insana bağlıdır — biri hava, öteki sahiplik. |
| **Tokoloshe** `tokoloshe` | Nguni ◈ | `tradition` | Nguni'nin iki gönderilmişi: ikisi de bir büyücüye bağlıdır, biri yerde biri gökte. |
| **Ziz** `ziz` | Talmud ✡ | `kin` | Impundulu kan ister ve beslenmezse sahibine döner; Ziz kimseden bir şey istemez — gölgesi güneşi kapatır, o kadar. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Büyücülük suçlamalarıyla ilişkilidir; Tokoloshe maddesiyle aynı etik dikkat uygulanacak.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Fırtına kuşu ailesinin (D) Afrika üyesi ve tek SAHİPLİ üyesi: bir kişiye bağlı.

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

