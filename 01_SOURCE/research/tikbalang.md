# Tikbalang — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `tikbalang` |
| **Ad** | Tikbalang |
| **Alternatif yazımlar** | — |
| **Gelenek** | Filipin ✧ · Güneydoğu Asya |
| **Sınıf** | III · THE SHAPE-CHANGERS (Şekil Değiştirenler) |
| **Akraba ailesi** | A · Su atı |
| **Plaka** | `plate-075` |
| **Telaffuz (taslak)** | tik-bah-LAHNG |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Maximo D. Ramos, *The Creatures of Midnight* (Quezon City: Island Publishers, 1967)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Maximo D. Ramos, *Philippine Demonological Legends and Their Cultural Bearings* (Quezon City: Phoenix, 1971)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Tikbalang”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `B184.1` | Magic horse | ✅ |

**Gerekçe.** TOHUM KODU DOĞRULANDI ve korundu. B184.1 ('Magic horse') tikbalang'ı tasnif eder. Su atı ailesinin (A) çıpası B184.1.3 ('Magic horse from water world') ama tikbalang SUYA bağlı değildir — bu ayrım maddede söylenecek ve Faz 2'de aile üyeliği gözden geçirilecek.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Filipinler; Luzon, ıssız yol ve bambu korulukları
- **İlk kayıt (attested):** İspanyol sömürge dönemi kayıtları; Ramos derlemeleri

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- At başlı, insan gövdeli
- Aşırı uzun bacaklar — oturduğunda dizleri başını aşar
- Ensesinde üç altın kıl

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Yolcuyu daireler çizdirerek kaybettirir. Gömleğini ters giymek yolu geri açar; ensesindeki üç altın kıl koparılırsa hizmet eder.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** Gömleği ters giymek.

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Each-uisce** `each-uisce` | Ériu ☘ | `kin` | Ailenin tek karasal üyesi: suya çekmez, yolu daireye çevirir. Su atı sudan çıkınca ne olur — cevabı budur. |
| **Nykur** `nykur` | Ísland ❆ | `kin` | İkisinin de ayağı yanlıştır — Nykur'un toynağı ters, Tikbalang'ın bacağı orantısız uzun. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- ⚠ Su atı ailesinde (A) ama SUYA bağlı değil. Faz 2'de üyelik kararı verilmeli — aile 'su atı' ise tikbalang dışarıda kalabilir.

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

