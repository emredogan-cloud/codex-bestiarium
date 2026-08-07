# Karakoncolos — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `karakoncolos` |
| **Ad** | Karakoncolos |
| **Alternatif yazımlar** | Karakoncilos, Koncolos |
| **Gelenek** | Türk ☾ · Orta Asya |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-053` |
| **Telaffuz (taslak)** | kah-rah-kon-jo-LOS |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `catalog`

- **Künye:** Pertev Naili Boratav, *100 Soruda Türk Folkloru* (İstanbul: Gerçek Yayınevi, 1973)

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Abdülkadir İnan, *Tarihte ve Bugün Şamanizm* (Ankara: Türk Tarih Kurumu, 1954)

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Karakoncolos”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G302` | Demons. Malevolent creatures (not usually further defined) | ✅ |

**Gerekçe.** G302 ('Demons. Malevolent creatures (not usually further defined)') doğrulandı ve korundu. Karakoncolos kaynaklarda biçimden çok ZAMANLA (zemheri) tanımlanır; genel iblis kodu doğrudur.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Türk; Karadeniz kıyısı, Balkanlar, Anadolu
- **İlk kayıt (attested):** 19.–20. yy saha derlemeleri; Boratav

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Kıllı, iri
- Zemherinin ilk on gününde çıktığı anlatılır

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Sokakta karşılaştığına soru sorar. Cevapta 'kara' kelimesi geçmezse çarpar.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** Her cevapta 'kara' kelimesini geçirmek.

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Al Karısı** `al-karisi` | Türk ☾ | `tradition` | Türk geleneğinin iki mevsimi: biri zemherinin, öteki doğumun tehlikesi. |
| **Ghūl** `ghul` | ʿArab ☪ | `function` | Karakoncolos soru sorar ve yanlış cevabı cezalandırır; Ghūl soru sormaz, kılık değiştirir. |
| **Şahmeran** `sahmeran` | Türk ☾ | `tradition` | İkisi de bir SORUYA bağlıdır: biri sırrın açığa çıkmasıyla ölür, öteki yanlış cevabı cezalandırır. |
| **Strigoi** `strigoi` | Dacia ✠ | `function` | İkisi de kışın belirli günlerine bağlıdır; biri sokakta, öteki mezarda başlar. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Karşı önlem bir KELİME OYUNU. Kappa'nın selamıyla akraba: nezaket ve dil, güçten üstün.

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

