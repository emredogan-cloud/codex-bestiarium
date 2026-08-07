# Masalai — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `masalai` |
| **Ad** | Masalai |
| **Alternatif yazımlar** | masalai ples |
| **Gelenek** | Melanesia ◉ · Okyanusya |
| **Sınıf** | III · THE SHAPE-CHANGERS (Şekil Değiştirenler) |
| **Akraba ailesi** | — |
| **Plaka** | `plate-111` |
| **Telaffuz (taslak)** | mah-sah-LYE |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `article`

- **Künye:** Margaret Mead, "The Sepik as a Culture Area: Comment", *Anthropological Quarterly* 51:1 (1978), 69–75
- **Erişim:** JSTOR 3317126 · DOI 10.2307/3317126
- **Not:** Mead'in masalai tanımı bu makaleden gelir ve alanın standart tanımıdır: belirli bir doğal işaretle ayrılmış yerleri mekân tutan, sınırlı yetki alanı olan doğaüstü varlıklar.

### Kaynak 2 · `scholarly` · doğrulama `article`

- **Künye:** Andrew Lattas, "Sexuality and Cargo Cults: The Politics of Gender and Procreation in West New Britain", *Cultural Anthropology* 6:2 (1991), 230–256
- **Erişim:** JSTOR 656416 · DOI 10.1525/can.1991.6.2.02a00070

### Kaynak 3 · `primary` · doğrulama `catalog`

- **Künye:** Thomas H. Slone, *One Thousand One Papua New Guinean Nights: Folktales from Wantok Newspaper*, Cilt 1 (Oakland: Masalai Press, 2001)
- **Erişim:** ISBN 978-0-9714127-0-5
- **Not:** Wantok gazetesinde Tok Pisin olarak yayımlanmış halk anlatılarının derlemesi — yayımlanmış ve kısıtlanmamış birincil malzeme.

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F460` | Mountain-spirits | ✅ |

**Gerekçe.** Tohum kodu F400 ('Spirits and demons (general)') idi; F460 ('Mountain-spirits') ile DEĞİŞTİRİLDİ. Gerekçe: masalai'nin tanımlayıcı özelliği genel bir cin olması değil, BELİRLİ BİR YERİ tutmasıdır (su birikintisi, şelale, kaya, ırmak dönemeci). Thompson'ın yer-ruhu kümesi bu işlevi F400'ün genel başlığından daha doğru yakalar. F441 ('Vegetation-spirits') de değerlendirildi ama masalai yalnızca bitkiye değil araziye bağlıdır.

> ⚠ **Tohum kodu değiştirildi.** F400 → F460. Tohum tablosu genel 'ruhlar ve cinler' kodunu önermişti; masalai bir YER ruhudur ve kodu bunu söylemeli.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Papua Yeni Gine geneli; Sepik, Batı Yeni Britanya ve Fore bölgelerinde ayrıntılı kayıt
- **İlk kayıt (attested):** Mead'in Sepik saha çalışmasından; tanım 1978'de yayımlandı. Slone'un derlediği Wantok anlatıları 1970'lerden itibaren
- **Yayılım:** Tok Pisin'de ülke çapında ortak terim; her bölge kendi masalai yerlerini tanır

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Sabit bir biçimi yok; yılan, timsah veya başka hayvan kılığında görünür
- Tuhaf renk, iki baş gibi olağandışı işaretler taşır
- Bir yere bağlıdır: su birikintisi, şelale, ırmak dönemeci, uçurum, bataklık

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Kendi arazisinde sınırlı bir yetki kullanır. Fore anlatılarında 'ples masalai' (masalai yeri) sayılan noktalarda yüksek sesle konuşulmaz ve oradaki bitkilere dokunulmaz.
- **Kayıtlı vaka:** Faz 3'te Slone'un derlemesinden tarihli bir anlatı seçilecek.
- **Karşı önlem:** Masalai yerinde sessiz kalmak; oradaki bitkilere ve taşlara dokunmamak.

## 6. Varyantlar

| Bölge / kaynak | Fark |
|---|---|
| Sepik (Mead) | Soy çizgilerine, moietylere ve köylere bağlı olabilir |
| Fore | 'Ples masalai' kutsal yer olarak işaretlenir; konuşma ve dokunma yasağı |

**Varyant notu.** Masalai bir TÜR değil bir KATEGORİDİR; her yerin kendi masalai'si vardır. Madde bunu gizlemeyecek.

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Adaro** `adaro` | Melanesia ◉ | `tradition` | Melanezya'da kara ve deniz: Masalai yerinde kalır, Adaro açıkta vurur. |
| **Boitatá** `boitata` | Tupi-Guarani ❂ | `function` | İkisi de toprağın kendisini savunur; Masalai bir yere bağlıdır, Boitatá gezer. |
| **Gufihtar** `gufihtar` | Sápmi ❄ | `function` | İkisi de araziye bağlıdır ve ikisi de yüksek sesle konuşulmayan yerlerdir. |
| **Temes Savsap** `temes-savsap` | Melanesia ◉ | `tradition` | Melanezya'nın iki sınırı: biri arazinin, öteki ölümün. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Yalnızca yayımlanmış malzeme kullanıldı: Mead ve Lattas'ın hakemli makaleleri, Slone'un gazetede yayımlanmış anlatı derlemesi. Belirli bir topluluğun kendi masalai yerinin adı, konumu veya ona bağlı tören ANLATILMAZ — bunlar yer-özel ve topluluğa aittir. Plakada gerçek bir yer veya klan işareti çizilmez.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Masalai bir tür değil bir kategori — madde bunu ilk cümlede söylemeli, yoksa okur yanılır.
- Tok Pisin terimi olduğu ve ülke çapında ortak olduğu belirtilmeli.

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

