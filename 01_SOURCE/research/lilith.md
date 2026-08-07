# Lilith — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `lilith` |
| **Ad** | Lilith |
| **Alternatif yazımlar** | — |
| **Gelenek** | Talmud ✡ · Yakın Doğu |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-086` |
| **Telaffuz (taslak)** | LIL-ith |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Babil Talmudu, *Şabbat*
- **Yer:** 151b

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Rebecca Lesses, "Exe(o)rcising Power: Women as Sorceresses, Exorcists, and Demonesses in Babylonian Jewish Society of Late Antiquity", *Journal of the American Academy of Religion* 69:2 (2001), 343–375

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Lilith”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G442` | Child-stealing demon | ✅ |
| `G302.9.4` | Demons injure and strangle little children | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum G264 ('La Belle Dame Sans Merci') idi — Lilith'in Talmud ve muska geleneğindeki işlevi erkek baştan çıkarmak değil YENİ DOĞANA yönelmektir. Doğrulanan G442 ('Child-stealing demon') ana kod; G302.9.4 ('Demons injure and strangle little children') ikinci kod.

> ⚠ **Tohum kodu değiştirildi.** G264 → G442 + G302.9.4.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Talmud geleneği; Mezopotamya ve Akdeniz Yahudiliği
- **İlk kayıt (attested):** *Şabbat* 151b; *Eruvin* 100b; Alfabe of Ben Sira (8.–10. yy); Aramice büyü kâseleri (5.–7. yy)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Uzun saçlı kadın
- Kanatlı olarak betimlenir
- Büyü kâselerinde bağlanmış hâlde resmedilir

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Yeni doğana yönelir. Doğum odasına Senoy, Sansenoy ve Semangelof adlarını taşıyan muska asılır.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** Üç meleğin adını taşıyan muska.

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Al Karısı** `al-karisi` | Türk ☾ | `kin` | Lilith yeni doğana yönelir; Al Karısı loğusanın ciğerini alır — hedef çocuktan anneye kayar. |
| **Lamashtu** `lamashtu` | Sumer 𒀭 | `kin` | İkisi de muskayla karşılanır: biri Pazuzu figürüyle, öteki üç melek adıyla. Karşı önlem yazıya geçmiştir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

Yahudi muska geleneği yaşayan bir uygulamadır. Muska METNİ aktarılmaz; yalnızca varlığı ve işlevi anlatılır.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Gece cadısı ailesinin (C) en çok yeniden yorumlanmış üyesi. Modern feminist okuma TEK CÜMLEDE ve 'modern' etiketiyle anılacak — kitabın konusu geç antik kayıt.

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

