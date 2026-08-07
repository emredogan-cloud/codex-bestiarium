# Draugr — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `draugr` |
| **Ad** | Draugr |
| **Alternatif yazımlar** | Draugar (çoğul), Haugbúi |
| **Gelenek** | Norðr ᚦ · Kuzey Avrupa |
| **Sınıf** | VI · THE RESTLESS DEAD (Huzursuz Ölüler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-009` |
| **Telaffuz (taslak)** | DROU-gr |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Grettis saga Ásmundarsonar*
- **Yer:** 32–35 (Glámr bölümü)

### Kaynak 2 · `primary` · doğrulama `canon`

- **Künye:** *Eyrbyggja saga*
- **Yer:** 51–55 (Fróðá harikaları)

### Kaynak 3 · `scholarly` · doğrulama `catalog`

- **Künye:** Hilda Roderick Ellis Davidson, *The Road to Hel: A Study of the Conception of the Dead in Old Norse Literature* (Cambridge: Cambridge University Press, 1943)

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `E422` | The living corpse. Revenant is not a specter but has the attributes of a living person | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum E230 ('Return from dead to inflict punishment') idi; draugr ceza için dönmez, HİÇ GİTMEZ. Doğrulanan E422 ('The living corpse. Revenant is not a specter but has the attributes of a living person') draugr'ın tanımıdır: hayalet değil, ağırlaşmış ve güçlenmiş bir CESET.

> ⚠ **Tohum kodu değiştirildi.** E230 → E422. Draugr bir hayalet değil, yürüyen bir cesettir.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Norðr; İzlanda ve Norveç saga coğrafyası, höyük mezarlar
- **İlk kayıt (attested):** *Grettis saga* (14. yy, olaylar 11. yy); *Eyrbyggja saga* (13. yy)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Şişmiş ve ağırlaşmış ceset
- Ölü mavisi veya kara ten (*hel-blár*)
- İnsanüstü ağırlık ve güç

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Höyüğünde yatar ve malını bekler. Grettis saga'da Glámr, öldürüldükten sonra çiftliği basar; Grettir onunla güreşir.
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
| **Fenrir** `fenrir` | Norðr ᚦ | `tradition` | Norðr'un iki bekleyeni: biri zinciri, öteki höyüğü bekler. |
| **Lemures** `lemures` | Romana SPQR | `function` | Draugr güreşle yenilir, Lemures törenle gönderilir. Güç ile ritüel. |
| **Strigoi** `strigoi` | Dacia ✠ | `function` | İkisi de gömüldüğü yerden kalkar; Draugr malını korur, Strigoi ailesinin kanını alır — biri mülkiyet, öteki soy. |
| **Windigo** `windigo` | Anishinaabe ▲ | `function` | İkisi de büyüyen bir gövdedir: Draugr şişer ve ağırlaşır, Windigo yedikçe boy atar. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Huzursuz ölüler sınıfının çıpası: draugr FİZİKSELDİR ve bu onu Lemures'ten ayırır.

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

