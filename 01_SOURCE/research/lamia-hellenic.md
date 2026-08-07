# Lámia — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `lamia-hellenic` |
| **Ad** | Lámia |
| **Alternatif yazımlar** | — |
| **Gelenek** | Hellenic Ω · Akdeniz |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | C · Gece cadısı |
| **Plaka** | `plate-003` |
| **Telaffuz (taslak)** | LAH-mee-a |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Diodoros Sikulos, *Bibliotheca historica*
- **Yer:** XX.41

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Sarah Iles Johnston, *Restless Dead: Encounters Between the Living and the Dead in Ancient Greece* (Berkeley: University of California Press, 1999)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Lamia”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G262.0.1` | Lamia. Witch who eats children | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum G264 ('La Belle Dame Sans Merci — witch entices MEN with offers of love') öneriyordu; Lámia erkekleri değil ÇOCUKLARI avlar. Doğrulanan G262.0.1'in tanımı doğrudan 'Lamia. Witch who eats children' — kod ailenin bu üyesinin adını taşıyor.

> ⚠ **Tohum kodu değiştirildi.** G264 → G262.0.1. Ayrıntı: SCOPE_DECISIONS.md § 5①.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Hellas; Libya kökenli anlatılır
- **İlk kayıt (attested):** Duris of Samos (MÖ 3. yy) üzerinden; Diodoros Sikulos XX

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Kadın biçiminde
- Kimi kaynakta yılan gövdeli
- Gözlerini çıkarıp yerine takabildiği anlatılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Çocuklarını kaybettikten sonra başkalarının çocuklarını avlar. Hera'nın cezası olarak anlatılır.
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
| **Lamashtu** `lamashtu` | Sumer 𒀭 | `kin` | Lámia bir cezadır — kaybettiği çocukların yerine başkasını alır; Lamashtu bir iblistir ve kaybetmemiştir. |
| **Strix** `strix` | Romana SPQR | `kin` | Roma, Yunan'ın kraliçesini kuşa çevirir: Lámia bir hikâyedir, strix bir TÜRDÜR ve Ovidius ona tarih verir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Gece cadısı ailesinin (C) çıpası — kodun adı bu maddeden geliyor.
- Kraliçeden canavara dönüşüm: ceza anlatısı, maddenin 5. bölümünün çekirdeği.

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

