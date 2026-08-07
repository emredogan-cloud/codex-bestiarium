# Ḫumbaba — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `humbaba` |
| **Ad** | Ḫumbaba |
| **Alternatif yazımlar** | Huwawa |
| **Gelenek** | Sumer 𒀭 · Yakın Doğu |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | F · Eşik bekçisi |
| **Plaka** | `plate-019` |
| **Telaffuz (taslak)** | hoom-BAH-bah |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** *Gılgamış Destanı*, Standart Babil sürümü
- **Yer:** Tablet V

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Jeremy Black ve Anthony Green, *Gods, Demons and Symbols of Ancient Mesopotamia: An Illustrated Dictionary* (Londra: British Museum Press, 1992)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Humbaba”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F150` | Access to otherworld | ✅ |

**Gerekçe.** F150 ('Access to otherworld') doğrulandı ve korundu. Ḫumbaba sedir ormanının — girilmesi yasak bölgenin — bekçisidir; işlevi eşiği tutmaktır.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Sumer/Akkad; Sedir Ormanı (Lübnan veya Zagros)
- **İlk kayıt (attested):** *Gılgamış Destanı*, Standart Babil sürümü (MÖ ~1200); Sumerce 'Gılgamış ve Huwawa' (MÖ ~2000)

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Yüzü bağırsak kıvrımlarından örülmüş (Eski Babil betimleme tabletleri)
- Sesi tufan
- Yedi 'korkunç ışıltı' (melammu) taşır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Sedir ormanını bekler. Gılgamış ve Enkidu onu öldürür; Enkidu'nun ölümü bu suçun bedeli olarak anlatılır.
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
| **Basiliscus** `basiliscus` | Romana SPQR | `kin` | İkisi de bakışla iş görür; Ḫumbaba'nın yüzü bağırsak kıvrımlarıdır — bakılan da bakan kadar önemlidir. |
| **Golem** `golem` | Talmud ✡ | `kin` | İkisi de korumak için yapılmış ve ikisi de koruduğu şey yüzünden yok olmuştur. |
| **Kérberos** `kerberos` | Hellenic Ω | `kin` | Kérberos kapıyı, Ḫumbaba ormanı bekler; biri görevini sürdürür, öteki görevi yüzünden öldürülür. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Eşik bekçisi ailesinin (F) Yakın Doğu üyesi.
- Yüzün bağırsak kıvrımı olması: kil tabletlerde GERÇEKTEN böyle betimlenir — uydurma değil.

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

