# Devi — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `devi` |
| **Ad** | Devi |
| **Alternatif yazımlar** | Dev, Devebi (çoğul) |
| **Gelenek** | Kartveli ✛ · Kafkasya |
| **Sınıf** | II · THE DEVOURERS (Yutucular) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-084` |
| **Telaffuz (taslak)** | DEH-vee |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `fulltext`

- **Künye:** Marjory Wardrop (çev.), *Georgian Folk Tales* (Londra: David Nutt, 1894)
- **Erişim:** gutenberg.org/files/44536 — tam metin indirilip tarandı
- **Yer:** “Ghvthisavari” ve devi anlatıları
- **Not:** Tam metinde 'devi' 113 kez geçiyor. Çok başlılık (üç, beş, dokuz, on baş) ve kardeş devler doğrudan doğrulandı.
- **İlgili alıntı:**

  > The three-headed devi came home… Then the nine-headed devi went… The ten-headed devi was now the only one left.

### Kaynak 2 · `primary` · doğrulama `catalog`

- **Künye:** Elene B. Virsaladze, *Georgian Folk Traditions and Legends*, çev. D. G. Hunt (Moskova: Nauka, 1973)
- **Not:** Gürcü folklorunun standart derlemesi; Virsaladze (1911–1977) alanın kurucu saha araştırmacısı.

### Kaynak 3 · `scholarly` · doğrulama `catalog`

- **Künye:** Mikheil Chikovani, *Kartuli polk'lori* (Gürcü folkloru) (Tiflis: Sakhelgami, 1946)

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `G100` | Giant ogre. Polyphemus | ✅ |

**Gerekçe.** G100 ('Giant ogre. Polyphemus') doğrulandı ve korundu. Gürcü devi mağarada yaşayan, kardeşleriyle birlikte bulunan dev-yamyamdır; Thompson'ın Polyphemus tipi tam oturur. Ad İran 'div'inden ödünçtür ve bu bağ maddede belirtilecek.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Gürcistan dağları; mağara anlatıları
- **İlk kayıt (attested):** 19.–20. yy derlemeleri; Chikovani ve Virsaladze

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Çok başlı — anlatıya göre üç, beş, dokuz veya on baş
- Dev boyutlu
- Mağarada, kardeşleriyle birlikte

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Mağarasında hazine ve tutsak tutar. Wardrop derlemesinde kardeşler sırayla gelir ve sırayla yenilir — sayı arttıkça tehlike artar.
- **Kayıtlı vaka:** Wardrop 1894, 'Ghvthisavari': üç, beş, dokuz ve on başlı kardeşler sırayla gönderilir.
- **Karşı önlem:** Anlatılarda kurnazlıkla yenilir — güçle değil.

## 6. Varyantlar

| Bölge / kaynak | Fark |
|---|---|
| İran etkisi | Ad ve figür Farsça 'div' ile akraba |

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Herensuge** `herensuge` | Euskal ✜ | `function` | İkisi de çok başlıdır ve baş sayısı tehlikenin ölçüsüdür. |
| **Nhang** `nhang` | Hayk ✚ | `tradition` | Kafkasya'nın iki yüzü: mağarada bekleyen güç ve ırmakta biçim değiştiren aldatma. |
| **Stállu** `stallu` | Sápmi ❄ | `function` | İki hantal dev: Devi sayıca artar, Stállu eşya biriktirir; ikisi de kurnazlıkla yenilir. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Kardeşlerin sırayla gelmesi: anlatı yapısı sayıyla gerilim kuruyor.
- Kartveli geleneğinin TEK doğrulanmış maddesi — Ochokochi ve Kaji erişilebilir kaynakta bulunamadı.

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

