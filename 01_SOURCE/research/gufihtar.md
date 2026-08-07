# Gufihtar — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `gufihtar` |
| **Ad** | Gufihtar |
| **Alternatif yazımlar** | Gufittar, Gufihttar |
| **Gelenek** | Sápmi ❄ · Kutup |
| **Sınıf** | III · THE SHAPE-CHANGERS (Şekil Değiştirenler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-106` |
| **Telaffuz (taslak)** | GOO-fih-tar |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `article`

- **Künye:** Emilie Demant Hatt, *By the Fire: Sami Folktales and Legends*, çev. ve yay. haz. Barbara Sjöholm (Minneapolis: University of Minnesota Press, 2019), "Folktales", 58–67
- **Not:** Demant Hatt'ın 1907–16 arası Sámi anlatıcılardan derlediği metinler; birincil derleme.

### Kaynak 2 · `scholarly` · doğrulama `article`

- **Künye:** JoAnn Conrad, "Tracking the Ogre — the Sami Stallo", *Ural-altaische Jahrbücher* 16 (1999–2000), 56–75

### Kaynak 3 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F400` | Spirits and demons (general) | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum F300 öneriyordu ama F300 bu turda erişilen nüshada bağımsız bir tanım taşımıyor — yalnızca 'F300–F399 Fairies and mortals' başlığı var, kodun kendisi tanımsız. Doğrulanmamış kod yazılamaz; doğrulanmış F400 ('Spirits and demons (general)') kullanıldı.

> ⚠ **Tohum kodu değiştirildi.** F300 → F400. F300'ün bağımsız tanımı doğrulanamadı.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Sápmi; sis ve tundra
- **İlk kayıt (attested):** Demant Hatt'ın 1907–16 derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Görünmez veya sisin içinden konuşan

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Yolcuyu görünmez kılar veya yolunu şaşırtır; sisin içinden seslenir.
- **Kayıtlı vaka:** Faz 3'te doğrulanacak.
- **Karşı önlem:** —

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Huldufólk** `huldufolk` | Ísland ❆ | `function` | İkisi de görünmezliği yönetir; Huldufólk kendi görünmezliğini, Gufihtar başkasınınkini. |
| **Masalai** `masalai` | Melanesia ◉ | `function` | İkisi de araziye bağlıdır ve ikisi de yüksek sesle konuşulmayan yerlerdir. |
| **Ulda** `ulda` | Sápmi ❄ | `tradition` | Sápmi'nin iki gizlisi: Ulda yerin altında yaşar, Gufihtar yolcuyu görünmez kılar. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Yalnızca yayımlanmış derleme kullanıldı. Yer-özel anlatı ve tören KULLANILMAZ.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Gufihtar ile Ulda arasındaki sınır kaynaklarda net değil; madde bunu gizlemeyecek.

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

