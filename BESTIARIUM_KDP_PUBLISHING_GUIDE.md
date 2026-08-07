# BESTIARIUM · KDP YAYIN KILAVUZU

> **Bu kitabı daha önce hiç yayımlamadığınız varsayılır.**
> Her ekran, her düğme, her ayar, her yükleme, her uyarı, her onay kutusu ve
> her fiyat alanı burada yazılıdır. Hiçbir adım "bilirsiniz" diye atlanmadı.
>
> Sürüm 1.0 · 7 Ağustos 2026 · Faz 6'da uygulanır
>
> ⚠ **KDP arayüzü değişir.** Bir alan burada yazdığı yerde değilse, adı
> muhtemelen aynıdır — arayın. Değişiklik bulursanız bu belgeyi güncelleyin
> ve `CHANGELOG.md`'ye yazın.

---

## İçindekiler

- [0. Başlamadan — hazırlık listesi](#0-başlamadan--hazırlık-listesi)
- [1. Hesap ve vergi röportajı](#1-hesap-ve-vergi-röportajı)
- [2. Yükleme sırası — neden ciltsizle başlanır](#2-yükleme-sırası--neden-ciltsizle-başlanır)
- [3. Ciltsiz · Ekran 1 — Paperback Details](#3-ciltsiz--ekran-1--paperback-details)
- [4. Ciltsiz · Ekran 2 — Paperback Content](#4-ciltsiz--ekran-2--paperback-content)
- [5. Ciltsiz · Ekran 3 — Paperback Rights & Pricing](#5-ciltsiz--ekran-3--paperback-rights--pricing)
- [6. Ciltli sürüm](#6-ciltli-sürüm)
- [7. Büyük punto sürüm](#7-büyük-punto-sürüm)
- [8. Kindle e-kitap](#8-kindle-e-kitap)
- [9. Prova kopyası](#9-prova-kopyası)
- [10. A+ İçerik](#10-a-i̇çerik)
- [11. Seri sayfası](#11-seri-sayfası)
- [12. Yayın sonrası](#12-yayın-sonrası)
- [13. Uyarılar sözlüğü](#13-uyarılar-sözlüğü)
- [14. Tam kontrol listesi](#14-tam-kontrol-listesi)

---

## 0. Başlamadan — hazırlık listesi

Bu dosyaların **hepsi** hazır olmadan KDP'ye girmeyin. Yarım başlanan bir
yükleme, taslak olarak kalır ve karışıklık üretir.

| # | Dosya | Yol | Nasıl üretilir |
|---|---|---|---|
| 1 | Ciltsiz iç blok PDF | `04_PRINT/PAPERBACK/CODEX_BESTIARIUM_INTERIOR_6x9.pdf` | `./08_BUILD/build_paperback.sh` |
| 2 | Ciltsiz kapak (krem) | `03_COVER/PAPERBACK/exports/..._cream_KDP.pdf` | aynı komut |
| 3 | Ciltsiz kapak (beyaz) | `..._white_KDP.pdf` | `--all-papers` |
| 4 | Ciltli iç blok | `04_PRINT/HARDCOVER/` | `./08_BUILD/build_hardcover.sh` |
| 5 | Ciltli kapak | `03_COVER/HARDCOVER/exports/` | aynı komut |
| 6 | Büyük punto iç blok + kapak | `04_PRINT/LARGEPRINT/` · `03_COVER/LARGEPRINT/exports/` | `./08_BUILD/build_largeprint.sh` |
| 7 | Kindle EPUB | `05_KINDLE/CODEX_BESTIARIUM.epub` | `python3 08_BUILD/make_docx_epub.py` |
| 8 | Kindle kapağı (JPEG) | `05_KINDLE/kindle-cover.jpg` | kapak hattından |
| 9 | A+ modülleri (@1x PNG) | `03_APLUS/exports/` | `./08_BUILD/build_aplus.sh` |
| 10 | Metadata | `00_CONTEXT/BRIEF.md` | elle |

### Son doğrulama

```bash
cd /home/emre/Downloads/MY-DİGİTAL-BOOK/CODEX_BESTIARIUM
./08_BUILD/qa_all.sh                     # bütün kapılar yeşil mi
python3 08_BUILD/validate_interior.py    # üç sürüm
python3 08_BUILD/validate_cover.py       # üç sürüm × iki kâğıt
pdffonts 04_PRINT/PAPERBACK/*.pdf        # DÖRT font görünmeli, hepsi gömülü
```

> **`pdffonts` çıktısında "emb" sütunu her satırda `yes` olmalı.** Tek bir
> `no` varsa KDP dosyayı reddeder. Cilt 1'de bu hata iki kez yaşandı;
> sebebi reportlab'in her Canvas'ı Helvetica ile başlatması ve o fontu
> kullanılmasa bile gömmeden yazmasıydı.

---

## 1. Hesap ve vergi röportajı

> Bu adım tamamlanmadıysa **her şeyden önce gelir**. Vergi röportajı olmadan
> telif ödenmez ve yayımlanan kitap satış yapsa bile para hesabınıza geçmez.

### 1.1 Giriş

1. <https://kdp.amazon.com> → **Sign in**
2. Amazon hesabınızla girin (perakende hesabınızla aynı olabilir).

### 1.2 Account bilgileri

**Your Account** → sol menü.

| Alan | Ne girilecek | Uyarı |
|---|---|---|
| **Author/Publisher Information** | Ad, adres, telefon | Adres **vergi röportajındaki adresle birebir aynı** olmalı |
| **Payment Information** | Banka bilgileri (IBAN, SWIFT) | TR IBAN kabul edilir. Hesap adı, KDP hesap adıyla uyuşmalı |
| **Tax Information** | Vergi röportajı | Aşağıya bakın |

### 1.3 Vergi röportajı (W-8BEN)

**Tax Information** → **Complete Tax Information** düğmesi.

Sırayla sorulacaklar:

| Soru | Yanıt |
|---|---|
| *Are you a U.S. person?* | **No** |
| *Type of beneficial owner* | **Individual** |
| *Country of citizenship* | **Turkey** |
| *Permanent address* | Türkiye adresiniz — **Account'takiyle aynı** |
| *Do you have a U.S. TIN?* | **No** (yoksa) |
| *Do you have a foreign TIN?* | **Yes** → **TC kimlik numaranız** |
| *Claim of tax treaty benefits* | **Yes** |
| *Country* | **Turkey** |
| *Article and paragraph* | **Article 12** (telif — royalties) |
| *Withholding rate* | **10%** |

> ⚠ **En kritik iki nokta:**
> 1. **Anlaşma talebi işaretlenmezse stopaj %30 olur.** Türkiye–ABD
>    anlaşması Madde 12 ile bu oran **%10**'a iner. 9,14 $ birim telifte
>    fark, kitap başına **1,83 $**.
> 2. **Adres uyuşmazlığında %24 yedek stopaj (backup withholding) eklenir.**
>    Account'taki adresle röportajdaki adres harf harf aynı olmalı.

Röportaj bitince **Submit**. Onay genellikle anında, bazen 24 saat.

---

## 2. Yükleme sırası — neden ciltsizle başlanır

**Sıra:** Ciltsiz → Ciltli → Kindle → Büyük punto

Sebebi tek: KDP'de bir formatı **var olan kitabın yanındaki düğmeden**
eklerseniz metadata otomatik kopyalanır ve formatlar ürün sayfasında
birbirine bağlanır. Sıfırdan yeni kitap oluşturursanız iki ayrı ürün olur,
yorumlar bölünür ve "diğer formatlar" kutusu görünmez.

```
Bookshelf
└── Codex Bestiarium (Paperback)     ← ÖNCE BU
    ├── [+ Create Hardcover]          ← sonra bu düğme
    ├── [+ Create Kindle eBook]       ← sonra bu düğme
    └── (Büyük punto AYRI bir kitaptır — § 7)
```

> **Büyük punto neden ayrı?** KDP büyük puntoyu bir "format" olarak tanımaz;
> ayrı bir ciltsiz kitaptır. Alt başlığında **"Large Print Edition"** geçer
> ve aynı seriye eklenerek bağlanır.

---

## 3. Ciltsiz · Ekran 1 — Paperback Details

**Bookshelf** → **+ Create** → **Create Paperback**

### 3.1 Language

| Alan | Değer |
|---|---|
| **Language** | **English** |

> Kitabın dili İngilizcedir. Bu alan yanlış girilirse kategori ve arama
> eşleştirmesi bozulur.

### 3.2 Book Title

| Alan | Değer |
|---|---|
| **Book Title** | `Codex Bestiarium` |
| **Subtitle** | `A World Bestiary: 120 Legendary Creatures from 40 Traditions — Beasts, Spirits, and Guardians of World Folklore` |

> ⚠ **Başlık ve alt başlık yayımlandıktan sonra değiştirilemez** (kapaktaki
> metinle eşleşmesi gerekir). İki kez okuyun.
>
> Alt başlıktaki uzun tire `—` bir U+2014'tür. Kopyalarken düz tireye
> dönüşmediğinden emin olun.

### 3.3 Series

| Alan | Değer |
|---|---|
| **Series** | ☑ *This book is part of a series* |
| **Series name** | `Codex` |
| **Series number** | `2` |

> Seri adı **Cilt 1'dekiyle harf harf aynı** olmalı: `Codex`. Farklıysa iki
> ayrı seri sayfası oluşur ve "sonraki kitap" kartı çalışmaz.

### 3.4 Edition Number

Boş bırakın (ilk baskı).

### 3.5 Author

| Alan | Değer |
|---|---|
| **Primary Author – First name** | `Emre` |
| **Last name** | `Doğan` |

> Türkçe karakter (`ğ`) kabul edilir ve Cilt 1'le aynı yazılmalıdır; farklı
> yazılırsa yazar sayfası ikiye bölünür.

### 3.6 Contributors

Boş. (İllüstratör alanı **doldurulmaz** — illüstrasyonlar AI üretimidir ve
bu, § 4.6'daki AI beyanında bildirilir.)

### 3.7 Description

`00_CONTEXT/BRIEF.md`'den ürün açıklamasını yapıştırın.

- Sınır: **4.000 karakter**
- Basit HTML kabul edilir: `<b>`, `<i>`, `<br>`, `<ul>`, `<li>`, `<h4>`
- İlk **iki satır** kritiktir — mobilde "read more" öncesi görünen kısım

> ⚠ Açıklamada **fiyat, indirim, başka satıcı adı veya kendi sitenize
> bağlantı** geçmemeli; Amazon bunları reddeder.

### 3.8 Publishing Rights

| Seçenek | Değer |
|---|---|
| ◉ **I own the copyright and I hold the necessary publishing rights** | ✅ seçin |
| ○ This is a public domain work | ❌ **seçmeyin** |

> ⚠ **Bu, bu kitap için gerçek bir risk noktasıdır.** Anlatılan folklor
> kamu malıdır; **bu kitabın prozası değildir.** Yanlış seçim e-kitap
> telifini %35'e düşürür. Cilt 1'de bu risk `PROJECT_CONTEXT.md § 13`'te
> kayıtlıdır; künye sayfasındaki özgünlük beyanı ve özgün Giriş/Sonsöz
> bunun savunmasıdır.

### 3.9 Primary Audience

| Alan | Değer |
|---|---|
| **Sexually explicit images or title?** | **No** |
| **Reading age** | Boş bırakın (yetişkin başvuru cildi) |

### 3.10 Categories

**Choose categories** düğmesi → üç kategori seçilir:

1. `Books › Social Science › Folklore & Mythology`
2. `Books › Reference › Mythology & Folk Tales`
3. `Books › Arts & Photography › Fantasy Art & Illustration`

> Üçüncüsü kasıtlıdır: illüstrasyon alıcısını yakalar — rakip serinin
> bulunduğu raf.

### 3.11 Keywords

Yedi kutu, her biri **≤50 karakter**. `00_CONTEXT/BRIEF.md` § 5'ten:

| # | Kutu |
|---|---|
| 1 | `mythical creatures encyclopedia illustrated` |
| 2 | `monsters spirits demons around the world` |
| 3 | `folklore reference book for writers` |
| 4 | `comparative folklore motif index` |
| 5 | `slavic celtic norse japanese creatures` |
| 6 | `line art bestiary gift book hardcover` |
| 7 | `water horse night hag thunderbird lore` |

> ⚠ Başlıkta ve alt başlıkta geçen kelimeler **kasıtlı olarak
> tekrarlanmadı** — tekrar slot israfıdır. Amazon zaten başlığı indeksler.

### 3.12 Publication Date

**Release immediately** seçin (ön sipariş kullanılmıyor).

**Save and Continue** →

---

## 4. Ciltsiz · Ekran 2 — Paperback Content

### 4.1 Print Options

| Alan | Değer | Neden |
|---|---|---|
| **Ink and Paper Type** | **Black & white interior with cream paper** | Uzun metinde göz yorgunluğu düşük; çizgi plakalar krem üzerinde gravür hissi verir |
| **Trim Size** | **6 x 9 in (15.24 x 22.86 cm)** | Cilt 1 ile rafta hizalı; normal trim (0,012 $/sayfa) |
| **Bleed** | **No Bleed** | Metin ve plakalar kesime taşmıyor |
| **Cover Finish** | **Matte** | Koyu kapakta parmak izi göstermez |

> ⚠ **EN KRİTİK KURAL — kâğıt seçimi kapak dosyasını belirler.**
>
> | Seçtiğiniz kâğıt | Yükleyeceğiniz kapak |
> |---|---|
> | Cream | `..._cream_KDP.pdf` |
> | White | `..._white_KDP.pdf` |
>
> Aradaki fark **2,1 mm**'dir ve yanlış eşleşme sırt yazısını doğrudan
> katlama çizgisine kaydırır. Cilt 1'de yayını haftalarca durduran hata
> tam olarak buydu.

### 4.2 ISBN

| Seçenek | Değer |
|---|---|
| ◉ **Get a free KDP ISBN** | ✅ |

**Assign me a free KDP ISBN** → onay kutusunu işaretleyin → **Assign**.

> Kendi ISBN'inizi almanız gerekmez. Ücretsiz KDP ISBN'i yalnızca Amazon
> baskısında geçerlidir; genişletilmiş dağıtım açmadığımız için sorun değil.
>
> ISBN atandıktan sonra **trim size ve kâğıt değiştirilemez**. Bu yüzden
> § 4.1'i önce doğrulayın.

### 4.3 Publication Date

**Release immediately.**

### 4.4 Manuscript

**Upload paperback manuscript** →

```
04_PRINT/PAPERBACK/CODEX_BESTIARIUM_INTERIOR_6x9.pdf
```

Yükleme sonrası KDP dosyayı işler (1–5 dakika). Bekleyin.

**Beklenen sonuç:** *"Upload successful"* ve **hiçbir uyarı yok**.

Uyarı çıkarsa [§ 13](#13-uyarılar-sözlüğü)'e bakın.

### 4.5 Book Cover

| Seçenek | Değer |
|---|---|
| ○ Use Cover Creator | ❌ |
| ◉ **Upload a cover you already have (print-ready PDF)** | ✅ |

→ Kâğıt seçiminize uyan dosyayı yükleyin:

```
03_COVER/PAPERBACK/exports/CODEX_BESTIARIUM_COVER_cream_KDP.pdf
```

### 4.6 AI-Generated Content

**Bu bölüm zorunludur ve dürüst doldurulur.**

| Soru | Yanıt |
|---|---|
| *Did you use AI-based tools in creating text, images, or translations?* | **Yes** |
| *Text* | ☑ **AI-assisted** — AI ile üretilmiş metin insan tarafından düzenlendi |
| *Images* | ☑ **AI-generated** — kapak **ve 120 illüstrasyon plakası** |
| *Translations* | ☐ (yok) |

> ⚠ **"Images" kutusunu mutlaka işaretleyin.** Bu kitapta 120 AI üretimi
> plaka var. Beyan etmemek KDP içerik kurallarının ihlalidir ve hesabın
> askıya alınmasına yol açabilir.
>
> Dürüst beyan aynı zamanda Risk 7'nin (AI illüstrasyon tepkisi) tek gerçek
> azaltıcısıdır. Arka maddedeki illüstrasyon notu süreci anlatır; künye
> sayfası da beyan taşır.

### 4.7 Preview — Print Previewer

**Launch Previewer** düğmesi.

Bakılacaklar, sırayla:

- [ ] **Sırt yazısı** iki katlama çizgisinin **arasında** ve **ortalanmış**
- [ ] Sırt yazısı yukarıdan aşağı okunuyor (ABD/İngiltere standardı)
- [ ] Ön kapakta başlık kesime yakın değil
- [ ] Arka kapakta barkod kutusunun geleceği alan **boş** (alt-sağ köşe)
- [ ] Hiçbir sayfada marj uyarısı yok
- [ ] Plakalar sayfada doğru yerde, kesilmiyor
- [ ] Sayfa numaraları doğru ve tek/çift sayfa doğru tarafta
- [ ] İç marjda metin cilde girmiyor

> **📸 Ekran görüntüsü alın.** Sırtın ortalandığının tek kaydı budur ve
> Cilt 1'de bu kaydın olmaması bir turu kaybettirmişti.

**Approve** → **Save and Continue** →

---

## 5. Ciltsiz · Ekran 3 — Paperback Rights & Pricing

### 5.1 Territories

| Seçenek | Değer |
|---|---|
| ◉ **All territories (worldwide rights)** | ✅ |

### 5.2 Primary Marketplace

**Amazon.com** (ABD) — en büyük pazar.

### 5.3 Pricing

| Alan | Değer |
|---|---|
| **List Price (Amazon.com)** | **`24.99`** USD |

Diğer pazarlar otomatik hesaplanır; dokunmayın.

**Doğrulama tablosu — KDP'nin gösterdiği değerler bunlar olmalı:**

| | Beklenen |
|---|---:|
| Printing cost | ~5,85 $ |
| **Royalty (60% − printing)** | **~9,14 $** |

> ⚠ **Telif 9,14 $ göstermiyorsa bir ayar yanlıştır.** Sayfa sayısını, kâğıt
> tipini ve trim'i kontrol edin. Sapma varsa dosyayı yeniden üretin —
> KDP'de değil, kaynakta düzeltilir.

### 5.4 Expanded Distribution

| Seçenek | Değer |
|---|---|
| ☐ **Expanded Distribution** | ❌ **AÇMAYIN** |

> Genişletilmiş dağıtım telifi %60'tan %40'a düşürür: 24,99 $'da birim
> telif **9,14 $'dan 4,15 $'a** iner. Bir başvuru cildi için kütüphane
> kanalı bu farkı karşılamaz.

### 5.5 Terms & Conditions

☑ *I confirm that I have all rights necessary…* → işaretleyin.

### 5.6 Publish

**Publish Your Paperback Book** düğmesi.

İnceleme **24–72 saat**. E-posta gelir.

---

## 6. Ciltli sürüm

**Bookshelf** → Codex Bestiarium satırının yanındaki **⋯** → **+ Create Hardcover**

Metadata otomatik kopyalanır. Yalnızca şunları değiştirin:

### 6.1 Print Options

| Alan | Değer |
|---|---|
| **Ink and Paper** | Black & white interior with cream paper |
| **Trim Size** | 6 x 9 in |
| **Bleed** | No Bleed |
| **Cover Finish** | **Case Laminate** (ciltlide tek seçenek) |

### 6.2 ISBN

**Ayrı bir ISBN gerekir.** → **Get a free KDP ISBN** → **Assign**.

### 6.3 Dosyalar

```
Manuscript : 04_PRINT/HARDCOVER/CODEX_BESTIARIUM_INTERIOR_6x9.pdf
Cover      : 03_COVER/HARDCOVER/exports/CODEX_BESTIARIUM_COVER_HARDCOVER_cream_KDP.pdf
```

> **İç blok ciltsizle özdeştir** — bilinçli bir karardır. 404 sayfada KDP
> asgari iç marjı 0,625"; bizimki 0,875" — cilt tarafında **0,25" fazlalık**
> zaten var, yani case binding'in daha az açılan yapısı için pay mevcut.
> Gutter'ı büyütmek satır ölçüsünü değiştirir → sayfa sayısı değişir → sırt
> değişir → bütün metin yeniden akar. **Uygunluk kazancı sıfır, risk yüksek.**

### 6.4 Ciltli kapak geometrisi

Ciltli kapak Cilt 1'de KDP'nin **resmî Case Laminate şablonundan kalibre
edildi** ve `08_BUILD/kdp_calibration.json` olarak devralındı.

| Parametre | Varsayılan | **Ölçülen** |
|---|---:|---:|
| Sarım (wrap) | 0,59060" | **0,58927"** |
| Menteşe (hinge) | 0,19690" | 0,19690" |
| **Karton sırt payı** | 0,12500" | **0,18850"** |
| Karton yükseklik payı | 0,23620" | 0,23813" |

> Karton sırt payı **1,61 mm** yanlıştı ve bu, sırt yazısını katlama
> çizgisine itmeye yeterdi. **Yeniden keşfetmeyin.**

### 6.5 Fiyat

| Alan | Değer |
|---|---|
| **List Price** | **`37.99`** USD |

Beklenen: baskı maliyeti ~10,50 $ · **telif ~12,29 $**

### 6.6 Print Previewer

Ciltside ek olarak kontrol edin:

- [ ] Sarım (wrap) alanında kritik bir öğe yok — o kısım iç kapağa yapışır
- [ ] Menteşe bölgesinde metin yok
- [ ] Sırt yazısı 1,0110" genişlikte ortalanmış

**Publish Your Hardcover Book**

---

## 7. Büyük punto sürüm

> **Bu ayrı bir kitaptır.** KDP büyük puntoyu bir format olarak tanımaz.

**Bookshelf** → **+ Create** → **Create Paperback** (sıfırdan)

### 7.1 Farklı alanlar

| Alan | Değer |
|---|---|
| **Book Title** | `Codex Bestiarium` |
| **Subtitle** | `A World Bestiary: 120 Legendary Creatures from 40 Traditions — **Large Print Edition**` |
| **Series** | `Codex` · numara **2** (aynı seriye eklenir) |

### 7.2 Dosyalar ve fiyat

```
Manuscript : 04_PRINT/LARGEPRINT/CODEX_BESTIARIUM_INTERIOR_6x9_LP.pdf
Cover      : 03_COVER/LARGEPRINT/exports/..._cream_KDP.pdf
```

| | Değer |
|---|---|
| Sayfa | **ölçülen** (16 pt gövde → ciltsizin ~1,75 katı) |
| **List Price** | ölçülen sayfa sayısına göre hesaplanır — `editions.py` verir |

> ⚠ **Sayfa sayısı ölçümden gelir, modelden değil.** Cilt 1'de büyük punto
> 540 sayfa modellenmiş, **578** çıkmıştı. Fiyatı `04_PRINT/LARGEPRINT/`
> üretildikten sonra hesaplayın.

### 7.3 Kategoriler

Ciltsizle aynı üç kategori + mümkünse **Large Print** alt rafı.

---

## 8. Kindle e-kitap

**Bookshelf** → Codex Bestiarium (Paperback) → **⋯** → **+ Create Kindle eBook**

### 8.1 Content

| Alan | Değer |
|---|---|
| **Digital Rights Management (DRM)** | **Yes** (önerilir) |
| **Manuscript** | `05_KINDLE/CODEX_BESTIARIUM.epub` |
| **Book Cover** | `05_KINDLE/kindle-cover.jpg` |

> ⚠ **EPUB reflowable olmalı, sabit düzen değil.** Sabit düzen Kindle
> Translate uygunluğunu kalıcı olarak kapatır. `make_docx_epub.py`
> reflowable üretir.
>
> ⚠ **Dosya boyutu ≤7 MB.** 120 plaka optimize edilmezse teslim ücreti
> telifin %30'unu yer. `convert_plates.py` plaka başına ≤60 KB hedefler.

### 8.2 Kindle Previewer

**Launch Previewer** → üç cihazda kontrol:

- [ ] **Kindle e-reader** — plakalar okunabilir mi, ince çizgiler kayboluyor mu
- [ ] **Tablet** — plaka ölçeği doğru mu
- [ ] **Telefon** — içindekiler tablosu çalışıyor mu

- [ ] İçindekiler tablosu (TOC) tıklanabilir ve tam
- [ ] Dört dizin okunabilir (tablo olarak akıyor mu)
- [ ] Madde başlıkları hiyerarşide doğru

### 8.3 Pricing

| Alan | Değer |
|---|---|
| **Royalty Plan** | ◉ **70%** |
| **List Price (Amazon.com)** | **`9.99`** USD |

Beklenen telif: **~5,94 $** (teslim ücreti düşülmüş).

> ⚠ **%70 telif planı 2,99–9,99 $ arasında geçerlidir.** 9,99 $ üst sınırdır;
> bir sent fazlası planı %35'e düşürür.
>
> ⚠ **Teslim ücreti (delivery cost) dosya boyutuyla orantılıdır.** KDP'nin
> gösterdiği telif 5,94 $'ın belirgin altındaysa EPUB çok büyüktür —
> yayımlamayın, plakaları yeniden optimize edin.

### 8.4 KDP Select

| Seçenek | Değer |
|---|---|
| ☐ **Enroll in KDP Select** | ❌ **GİRMEYİN** |

> Başvuru cildi Kindle Unlimited'da zayıftır: 404 sayfalık tam okuma
> ≈ **1,95 $** — ciltsiz telifin beşte biri. Ayrıca KDP Select 90 gün
> münhasırlık ister.

**Publish Your Kindle eBook**

---

## 9. Prova kopyası

> **Fiyatlandırmadan ve reklamdan önce.** Ekran ≠ kâğıt.

**Bookshelf** → kitabın **⋯** → **Order Author Copies**

| Alan | Değer |
|---|---|
| Format | Paperback (ve ayrıca Hardcover) |
| Adet | **1** her formattan |
| Teslimat | Türkiye adresiniz |

Maliyet: baskı maliyeti + kargo. Kâr yok.

> ⚠ **Türkiye'ye kargo 2–3 hafta.** Plana ekleyin.

### Prova kontrol listesi

Kitap elinize geldiğinde:

- [ ] **İç marjda metin cilde giriyor mu** — sayfayı düz açmadan okunabiliyor mu
- [ ] Sayfa numaraları doğru mu
- [ ] Sırt yazısı ortalanmış mı — cetvelle ölçün
- [ ] Kapak koyu tonu baskıda çamurlaşmış mı
- [ ] **Çizgi plakaların ince çizgileri kayboluyor mu** ← *bu kitaba özgü ve en kritik olanı*
- [ ] Plaka kontrastı krem kâğıtta doğru mu
- [ ] Dizin sayfa numaraları gerçekten doğru mu (rastgele 20 madde deneyin)
- [ ] Ciltlide sırt sağlam mı, açıldığında çatlıyor mu

> **İnce çizgi kaybı bu kitabın en büyük baskı riskidir.** Gravür dili
> 1,4 pt çizgilerle çalışır; POD baskıda mürekkep yayılması bunları
> kapatabilir. Kayıp varsa `PLATE_SPEC["line_weight_pt"]` yükseltilir ve
> **120 plaka yeniden normalize edilir** (ham dosyalardan — bu yüzden
> `plates_raw/` asla değiştirilmez).

---

## 10. A+ İçerik

**KDP → Marketing → A+ Content Manager → Create A+ Content**

| Alan | Değer |
|---|---|
| **Content name** | `Codex Bestiarium — Main` |
| **Language** | English |

### Modüller — sırayla ekleyin

| # | Modül tipi | Ölçü | Dosya |
|---|---|---|---|
| 1 | Standard Image & Light Text Overlay | 970×300 | `03_APLUS/exports/m1-header@1x.png` |
| 2 | Standard Image Header with Text | 970×600 | `m2-what-it-is@1x.png` |
| 3 | Standard Image Header with Text | 970×600 | `m3-kin-images@1x.png` |
| 4 | Standard Image Header with Text | 970×600 | `m4-anatomy@1x.png` |
| 5 | Standard Image Header with Text | 970×600 | `m5-interior@1x.png` |

**Amazon sınırları (doğrulanmış):** dosya ≤ **2 MB** · JPEG veya PNG ·
renk uzayı **yalnızca RGB** (CMYK reddedilir) · asgari 72 DPI.

> ⚠ **Yalnızca `@1x.png` yükleyin.** `@2x` yedektir ve 2 MB'ı aşar.

### Her modüle alt metin (alt text) girin

`03_APLUS/aplus-manifest.json` içindeki `ALT_TEXT` değerlerini kullanın.
Erişilebilirlik ve indeksleme kaybı olmasın.

### Uyumluluk

> ⚠ **Amazon rakip ürün karşılaştırmasını yasaklar.** m3 hiçbir marka,
> yazar veya kitap adı geçirmez; yalnızca kendi içeriğimizi gösterir.
> Yayımlamadan önce bir kez daha gözden geçirin.

**Apply to ASINs** → ciltsiz, ciltli ve Kindle ASIN'lerini seçin →
**Submit for approval**

İnceleme genellikle 24 saat, bazen 7 güne kadar.

---

## 11. Seri sayfası

Seri sayfası **otomatik** oluşur; koşul: her formatta **Series** alanı
birebir aynı olmalı (`Codex`, numara `2`).

Kontrol:

- [ ] <https://www.amazon.com/dp/{ASIN}> → ürün sayfasında **"Codex (2 book series)"** kutusu var mı
- [ ] Cilt 1 ve Cilt 2 **aynı** seri sayfasında görünüyor mu
- [ ] Ciltsiz, ciltli ve Kindle aynı ürün sayfasında format sekmesi olarak bağlı mı

Bağlanmamışsa: **KDP Support → "Link my book formats"** talebi açın; ASIN'leri
verin. 2–5 iş günü.

---

## 12. Yayın sonrası

### İlk gün

- [ ] **ASIN'leri kaydedin** (üç format + büyük punto) → `00_CONTEXT/BRIEF.md`
- [ ] `00_CONTEXT/PROJECT_CONTEXT.md` yayın durumuyla güncellendi
- [ ] Ürün sayfasında başlık, alt başlık, açıklama doğru görünüyor mu
- [ ] **İndeksleme testi:** Amazon aramada `codex bestiarium` → kitap çıkıyor mu
- [ ] Yedi anahtar kelimenin her biriyle arama yapın; kaçında ilk 3 sayfadasınız

### İlk hafta

- [ ] A+ İçerik onaylandı ve görünüyor
- [ ] Prova kopyası sipariş edildi
- [ ] `/series/codex` web sayfası güncellendi
- [ ] E-posta listesine duyuru

### Reklam

| Kanal | Bütçe | Hedef |
|---|---|---|
| Sponsored Products (otomatik) | 10–15 $/gün | ACOS ≤ **%27** (başabaşın %75'i) |
| ASIN hedefleme | — | Codex Mythologica'nın sayfası + rakip bestiyer sayfaları |

> **Reklamı Kindle'a verin, ciltsizi organik keşfe bırakın.** E-kitabın
> başabaş ACOS'u iki kat toleranslı.

### ARC ve topluluk

- [ ] StoryOrigin (ücretsiz) + BookSirens (~50–80 $) → hedef **25–50 yorum**
- [ ] Reddit: r/mythology, r/folklore, r/worldbuilding, r/rpg — **önce değer, sonra bağlantı**
- [ ] Mitoloji podcast'lerine inceleme kopyası (kişiselleştirilmiş, toplu değil)
- [ ] Pinterest: plakalardan 30 görsel, her biri gelenek etiketiyle

### Ölçülecek tek şey

> **Cilt 1'in satışındaki değişim.** Seri etkisinin tek gerçek testi budur.
> Bestiarium yayınlandıktan sonra Mythologica'nın haftalık satışı artıyorsa
> seri çalışıyor demektir; artmıyorsa seri sayfası veya çapraz bağlantı
> bozuktur.

### Sesli kitap (Virtual Voice)

Yayından **1 ay sonra** değerlendirin.

Koşullar: Kindle canlı ≥7 gün · içindekiler tablosu · İngilizce ·
<240 bin kelime ✓

> **120 telaffuz alanı zaten `spec.json`'da.** Sesli kitabın en zor kısmı
> önceden çözülmüştür.

---

## 13. Uyarılar sözlüğü

KDP'nin gösterebileceği uyarılar ve **kaynakta** nasıl düzeltilecekleri.
Hiçbiri KDP arayüzünde "yoksayarak" geçilmez.

| Uyarı | Anlamı | Çözüm |
|---|---|---|
| *"Your file contains fonts that are not embedded"* | reportlab Helvetica'yı gömmeden yazdı | `rl_config.canvas_basefontname` kendi fontumuza çevrilmeli. `pdffonts` ile doğrulayın: **dört** font, hepsi `emb=yes` |
| *"Your content extends beyond the printable area"* | İç marj yetersiz veya sayfa kutusu yanlış | `validate_interior.py` çalıştırın; `editions.py`'deki marj sayfa sayısına uygun mu |
| *"Cover file dimensions do not match"* | Kâğıt seçimi ile kapak dosyası uyuşmuyor | Cream seçtiyseniz `_cream_KDP.pdf`. **2,1 mm fark sırt yazısını katlama çizgisine iter** |
| *"Image resolution is below 300 DPI"* | Kapak sanatı düşük çözünürlüklü | Sanat ≥3922 px genişlikte üretilmeli. Cilt 1'de 112 PPI hatası yaşandı — **tekrarlamayın** |
| *"Your book contains blank pages"* | Bölüm başları tek sayfaya zorlanınca boş sayfa oluşur | Normaldir, kabul edin — bölüm hep tek (sağ) sayfada başlamalı |
| *"Page count is outside the allowed range"* | Ciltsiz 24–828, **ciltli 75–550** | Ciltli için sayfa 550'yi aşıyorsa trim veya punto değişmeli |
| *"Spine text may be cut off"* | Sırt genişliği < 0,25" veya metin çok geniş | 404 sayfada sırt ~0,82" — bu uyarı çıkıyorsa sayfa sayısı yanlış girilmiş |
| *"Your eBook file is larger than recommended"* | EPUB > 7 MB | `convert_plates.py --check`; plaka başına ≤60 KB |
| *"This title may be public domain"* | § 3.8'de yanlış seçim veya otomatik inceleme | Künye sayfasındaki özgünlük beyanını ve özgün Giriş/Sonsöz'ü gösterin. **Telifi %35'e düşürür** |
| *"Barcode area is not clear"* | Arka kapak alt-sağ köşesinde öğe var | Kapak hattı iki alt köşeyi de boş bırakır; sanat değiştiyse yeniden üretin |

---

## 14. Tam kontrol listesi

### Hazırlık

- [ ] Vergi röportajı tamamlandı, **stopaj %10** görünüyor
- [ ] Account adresi ile vergi adresi **birebir aynı**
- [ ] Banka bilgileri girildi
- [ ] `./08_BUILD/qa_all.sh` yeşil
- [ ] `pdffonts` üç iç blokta da **dört gömülü font** gösteriyor
- [ ] `validate_cover.py` üç sürüm × iki kâğıt → 0 başarısız

### Ciltsiz

- [ ] Ekran 1 — başlık, alt başlık, seri `Codex` #2, yazar `Emre Doğan`
- [ ] Publishing rights: **I own the copyright** (public domain **değil**)
- [ ] Üç kategori seçildi
- [ ] Yedi anahtar kelime, her biri ≤50 karakter
- [ ] Ekran 2 — 6×9 · No Bleed · **Cream** · Matte
- [ ] Ücretsiz KDP ISBN atandı
- [ ] İç blok yüklendi, **uyarı yok**
- [ ] Kapak: **kâğıt seçimine uyan** dosya
- [ ] **AI beyanı: metin AI-assisted · görseller AI-generated**
- [ ] Print Previewer — sırt ortalanmış, **ekran görüntüsü alındı**
- [ ] Ekran 3 — 24,99 $, **telif 9,14 $ görünüyor**
- [ ] Genişletilmiş dağıtım **kapalı**
- [ ] Yayımlandı

### Ciltli

- [ ] **"+ Create Hardcover" düğmesinden** oluşturuldu (sıfırdan değil)
- [ ] Ayrı ISBN atandı
- [ ] Case Laminate
- [ ] 37,99 $ · **telif 12,29 $**
- [ ] Previewer'da sarım ve menteşe temiz
- [ ] Yayımlandı

### Kindle

- [ ] **"+ Create Kindle eBook" düğmesinden** oluşturuldu
- [ ] EPUB **reflowable** ve **≤7 MB**
- [ ] Previewer'da üç cihaz kontrol edildi, TOC çalışıyor
- [ ] %70 telif planı · 9,99 $ · **telif ~5,94 $**
- [ ] **KDP Select kapalı**
- [ ] Yayımlandı

### Büyük punto

- [ ] Ayrı kitap olarak oluşturuldu
- [ ] Alt başlıkta **"Large Print Edition"**
- [ ] Aynı seriye (`Codex` #2) eklendi
- [ ] Ölçülen sayfa sayısına göre fiyatlandırıldı
- [ ] Yayımlandı

### Yayın sonrası

- [ ] Dört ASIN kaydedildi
- [ ] A+ İçerik gönderildi (5 modül, alt metinlerle)
- [ ] Seri sayfasında Cilt 1 ve Cilt 2 birlikte görünüyor
- [ ] Formatlar aynı ürün sayfasında bağlı
- [ ] **Prova kopyası sipariş edildi**
- [ ] İndeksleme testi geçti
- [ ] Reklam kampanyaları açıldı
- [ ] `PROJECT_CONTEXT.md` ve `CHANGELOG.md` güncellendi
- [ ] `v1.0.0` etiketi atıldı

---

*Vâliçe Press · Codex Bestiarium · KDP Yayın Kılavuzu v1.0 · 7 Ağustos 2026*
