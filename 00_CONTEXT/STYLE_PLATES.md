# STYLE_PLATES — Çizgi dili şartnamesi

> **Projenin tek gerçek başarısızlık modu burada yönetilir.**
>
> 112 plaka tek bir çizgi dilinde durmazsa kitap "derleme" gibi görünür ve
> premium konumlanma çöker. Bu risk **ölçülerek** yönetilir — göz kararıyla
> değil. Bir insan on plakayı kalibre edebilir; yüz on ikisini edemez.

---

## 1. Şartname

Bütün değerler `08_BUILD/bestiarium.py` → `PLATE_SPEC` içindedir.
Bu tablo o sözlüğün insan okunur hâlidir; **ikisi ayrışırsa kod geçerlidir**.

| Parametre | Değer | Tolerans | Ölçen | Kapı |
|---|---|---|---|---|
| Teknik | gravür / hat taraması (line engraving), tek renk | — | — | — |
| Tuval | 1:1,25 dikey · 1800 × 2250 px @ 300 DPI | sabit | `measure_aspect` | ✅ |
| **Tarama darbesi** | darbe ÷ periyot = 0,35–0,65 | bant | `measure_strokes` | ✅ |
| Tarama açısı | 45° birincil · 135° ikincil | ±5° | `measure_hatch` (FFT) | ✅ |
| Tarama sıklığı | cm başına 22–28 çizgi | bant | `measure_hatch` | ✅ |
| En koyu ton | %92 siyah | ±%5 | `measure_ink_range` | ✅ |
| En açık ton | %8 siyah | ±%5 | `measure_ink_range` | ✅ |
| Kapsama | yaratık tuvalin %62–78'i | bant | `measure_coverage` | ✅ |
| Zemin | **boş** — yaratık boşlukta durur, sahne yok | zorunlu | `measure_background` | ✅ |
| Dış hat kalınlığı | 1,4 pt (≈5,8 px @ 300 DPI) | ±%15 | `measure_strokes` | ⚠ ölçülür, **kapı değil** |
| Ölçek işareti | her plakada ince bir insan silueti | zorunlu | insan kontrolü | — |
| Bakış | sola veya izleyiciye | — | insan kontrolü | — |

**Bant dışına çıkan plaka otomatik reddedilir ve yeniden üretilir.**
Bu karar insana bırakılmaz.

---

## 1b. Faz 2 kalibrasyonu — cetvel doğru mu ölçüyor?

> Bu bölüm Faz 2'de eklendi ve bu hattın en önemli bulgusunu taşıyor.

112 plakayı otomatik reddetme yetkisi olan bir ölçüm, hiç sınanmamıştı.
`08_BUILD/tests/plate_fixtures.py` geometrisi **bilinen** gravür plakaları
üretir; `08_BUILD/tests/plate_selftest.py` ölçümü o bilinen değerle
karşılaştırır ve her kurala bir ihlal kurgusu göndererek kapının ısırdığını
kanıtlar. CI'da `plates.yml → calibration` işi olarak koşar.

### İlk çalıştırmada bulunan iki gerçek kusur

**① Açı yanlılığı (√2) — şartnameye tam uyan plakayı reddediyordu.**
Kalınlık, tarama yönüne *dik olmayan* kesitlerden okunuyordu. 45° taramada bir
kesit çizgiyi 45° ile keser ve koşu uzunluğu gerçek kalınlığın **1,41 katı**
çıkar. Şartnamedeki geometriye birebir uyan kurgu plakası bu yüzden
reddediliyordu — yani hat, doğru çizilmiş 112 plakanın tamamını geri
çevirecekti. Ölçüm artık okunan tarama açısına göre düzeltiliyor.

**② Tarama darbesi ile dış hat tek sayıya indirilmişti.**
Şartname hem "cm başına 22–28 çizgi" hem "çizgi kalınlığı 1,4 pt" diyordu.
25 çizgi/cm'de periyot **4,72 piksel**; 1,4 pt ise **5,83 piksel**. Bir
periyoda kendisinden geniş bir darbe sığmaz — iki kural geometrik olarak bir
arada duramıyordu. İkisi ayrıldı: tarama darbesi artık periyoda **oranla**
ölçülür (bandı sıklıktan türer, çelişemez), dış hat ayrı raporlanır.

### Ölçülen doğruluk

Kurgunun gerçek değerleri ile ölçülen değerler (`06_REPORTS/plate-calibration.json`):

| Parametre | Gerçek | Ölçülen | Hata | İzin |
|---|---:|---:|---:|---:|
| En-boy oranı | 1,250 | 1,250 | %0,0 | %1 |
| Tarama darbesi (px) | 2,362 | 2,370 | **%0,3** | %5 |
| Tarama sıklığı (çizgi/cm) | 25,0 | 25,0 | %0,0 | %5 |
| Kapsama | 0,706 | 0,711 | %0,8 | %5 |
| En koyu ton | 0,920 | 0,894 | 0,026 | 0,05 |
| En açık ton | 0,080 | 0,110 | 0,030 | 0,05 |
| Tarama açısı | 45°/135° | 45° | oturuyor | ±5° |

Düzeltmeden önce tarama darbesi hatası **%41**'di.

### Dış hat neden kapı değil

Kontur kalınlığı **2,9 · 4,2 · 5,83 · 7,3 · 8,75 px** olan beş kurgu üretildi
ve koşu-uzunluğu istatistiklerinin **ilk üçünü ayırt edemediği** ölçüldü
(üçünde de aynı yüzdelik çıkıyor). Sebep geometrik: 25 çizgi/cm'de periyot
≈4,7 px, 1,4 pt kontur ise 5,8 px — aynı büyüklük mertebesinde, ve birleşen
tarama darbeleri kontur kesişmeleriyle karışıyor.

**Ayırt edemeyen bir sayıyla plaka reddetmek, ölçüyormuş gibi yapmaktır.**
Dış hat kalınlığı raporda kalır (kurucunun göz kontrolü için) ama karar
vermez. Gerçek "tek çizgi dili" güvencesi, doğruluğu yukarıda ölçülmüş yedi
parametredir. Pilot set geldiğinde tahminci gerçek plakalarda yeniden
değerlendirilecek (Faz 3 açık kalemi).

### Format bütçeleri de kurguda ölçüldü

`convert_plates.py --calibrate` aynı kurguyu dört formata çevirir ve gerçek
baytı 112 plakaya ekstrapole eder. Belirleyici olan konu değil çizgi dilidir;
ince 45° tarama her kodlayıcı için en kötü durumdur.

| Format | Plaka başına | Bütçe | Durum |
|---|---:|---:|---|
| Baskı (TIFF LZW) | 237 KB | — | kayıpsız |
| Kindle (PNG, 16 ton, 900 px) | 34 KB | 60 KB | ✅ |
| A+ (JPEG q88) | 1235 KB | 2000 KB | ✅ |
| Web (WebP, 16 ton, **kayıpsız**, 1400 px) | 159 KB | 300 KB | ✅ |

**112 plakalık EPUB projeksiyonu: 3,74 MB** (hedef ≤6 MB) — Risk 5 Faz 6'da
değil Faz 2'de yanıtlandı.

> Web formatı bu ölçümde değişti. Kayıplı WebP (1800 px, kalite 86) **954 KB**
> veriyordu — bütçenin üç katı — ve ölçek düşürmek yetmedi. Çözüm Kindle
> yolunda zaten vardı: gravür birkaç tonluk bir görüntüdür. 16 tona indirilip
> **kayıpsız** kaydedilince 1400 pikselde 159 KB'ye iniyor; aynı boyuttaki
> kayıplı sürüm 474 KB ve artefaktlı.

---

## 2. Ölçüm yöntemi — üç not

### ① Tarama açısı Fourier'den okunur

Gravür taraması güç spektrumunda, kaynağın yönüne **dik** bir doğru üretir.
`measure_hatch` bu doğrunun açısını bulur ve 90° döndürerek tarama açısına
çevirir.

İki tuzak, ikisi de kodda kapatıldı:
- **Dikdörtgen tuval** spektrumu yönsel olarak çarpıtır → kare pencere alınır.
- **Kenar sızıntısı** spektrumda yalancı 0°/90° tepesi üretir → Hann penceresi
  uygulanır.

### ② Kalınlık açıya göre düzeltilir ve budanmış ortalamayla okunur

İki ayrı düzeltme, ikisi de Faz 2 kalibrasyonunun bulgusu:

- **Açı düzeltmesi.** Koşu uzunluğu, kesit yönüyle çizgi yönü arasındaki
  açının sinüsüne bölünmüş kalınlıktır. 45° taramada düzeltmesiz ölçüm √2
  yanlıdır (bkz. § 1b①).
- **Budanmış ortalama.** Bu ölçekte koşular 3 veya 4 piksele yuvarlanır ve
  medyan tam sayıya yapışır (%10 hata). Medyanın iki katına kadar olan
  koşuların ortalaması hem uzun kuyruğa (dolu alan, kontur) bağışıklıdır hem
  ara değeri okur: hata %10 → %0,3.

### ③ Kapsama, yoğunluk değildir

**Kapsama** = mürekkebin sınırlayıcı kutusu ÷ tuval.
**Yoğunluk** = koyu piksel ÷ toplam piksel.

İkisi karıştırılırsa koyu bir yaratık "büyük" sanılır. Şartnamedeki %62–78
**kapsamadır**; yoğunluk yalnızca raporlanır.

---

## 3. Üretim protokolü

```
① Prompt      BESTIARIUM_IMAGE_PROMPTS.html → "Prompt kopyala"
② Ham çıktı   07_ASSETS/plates_raw/plate-NNN.png   ← ASLA DEĞİŞTİRİLMEZ
③ Normalize   python3 08_BUILD/plates.py --normalize
④ Ölçüm       python3 08_BUILD/plates.py --measure -v
⑤ İnsan       vektör araçta temizlik (~25 dk/plaka)
⑥ Formatlar   python3 08_BUILD/convert_plates.py
```

### Ham dosya neden değiştirilmez

Normalizasyon geri döndürülemez (kırpma, seviye gerdirme). Şartname
değiştiğinde — ve değişecektir — bütün plakalar **ham dosyadan** yeniden
üretilir. Ham dosya kaybolursa 112 plaka yeniden çizilir.

---

## 4. Pilot set kilidi

**On plaka onaylanmadan diğer 102'ye geçilmez.**

Pilot, altı sınıfın tamamından örnek taşır (`plates.py` → `PILOT_IDS`):

| Plaka | Yaratık | Sınıf | Neden pilotta |
|---|---|---|---|
| `plate-001` | Kérberos | I · Bekçiler | Çok başlı, simetrik, frontal duruş |
| `plate-003` | Lámia | II · Yutucular | İnsan-hayvan geçişi, yüz ifadesi |
| `plate-031` | Kumiho | III · Şekil Değiştirenler | Dokuz kuyruk — tarama yoğunluğu sınavı |
| `plate-016` | Each-uisce | IV · Su Sakinleri | Gövdenin boşlukta erimesi |
| `plate-043` | Sīmurgh | V · Gök ve Fırtına | Açık kanat — en geniş kompozisyon |
| `plate-009` | Draugr | VI · Huzursuz Ölüler | Kırık dış hat, çözülmemiş kenar |
| `plate-074` | Manananggal | II | Ayrılmış gövde — anatomik zorluk |
| `plate-102` | Animikii | V | Aile D tutarlılığı (Sīmurgh ile karşılaştırma) |
| `plate-107` | Huldufólk | I | Aile H — topluluk kompozisyonu |
| `plate-098` | Curupira | I | Aile G — insan siluetine en yakın |

> Plaka numaraları Faz 1'in kapsam kilidinden sonra yeniden verildi
> (120 → 112). Bu tablo `plates.py` → `PILOT_IDS`'ten türetilerek tazelendi;
> ikisi ayrışırsa **kod geçerlidir**.

### Onay ölçütü

1. `plates.py --pilot -v` → **tolerans dışı plaka sıfır**
2. On plaka **yan yana** dizilir ve gözle bakılır: aynı elden çıkmış görünüyor
   mu? Ölçüm geçiyor ama göz "hayır" diyorsa **tolerans bandı dardır, ölçüm
   eksiktir** — banda yeni bir parametre eklenir.
3. Ölçülen dağılım (ortalama + standart sapma) bu belgeye yazılır ve üretim
   setinin karşılaştırma tabanı olur.

---

## 5. Ölçülen dağılım

> **Durum: hat hazır, ham plaka bekleniyor.**
>
> Faz 2'nin plaka işi ikiye ayrılıyordu: **hattı kurup kalibre etmek** ve
> **on ham plakayı üretip ölçmek**. Birincisi tamamlandı ve § 1b'de
> ölçümleriyle duruyor — cetvel sınandı, iki kusuru bulundu, düzeltildi ve
> doğruluğu sayıyla kayda geçti. İkincisi **ham AI çıktısı gerektirir**:
> `BESTIARIUM_IMAGE_PROMPTS.html` → görsel üreteç → `07_ASSETS/plates_raw/`.
> Bu, hattın dışındaki tek girdidir ve kurucudan gelir.
>
> Ham plakalar geldiğinde tek komut yeter:
>
> ```bash
> python3 08_BUILD/plates.py --normalize --pilot
> python3 08_BUILD/plates.py --pilot -v
> python3 08_BUILD/convert_plates.py
> ```
>
> Sonra aşağıdaki tablo `06_REPORTS/plate-consistency.json`'dan doldurulur ve
> üretim setinin (102 plaka) karşılaştırma tabanı olur; örtüşmüyorsa üslup
> gövdesi kaymıştır.

| Parametre | Ortalama | Std sapma | Aralık |
|---|---|---|---|
| Tarama darbesi (pt) | — | — | — |
| Darbe / periyot | — | — | — |
| Tarama sıklığı (çizgi/cm) | — | — | — |
| Kapsama | — | — | — |
| En koyu ton | — | — | — |

**Kalibrasyon kurgusunun değerleri** (üretim setinin beklendiği yer —
`06_REPORTS/plate-calibration.json`):

| Parametre | Kurguda ölçülen |
|---|---:|
| Tarama darbesi | 0,57 pt (2,37 px) |
| Darbe / periyot | 0,50 |
| Tarama sıklığı | 25,0 çizgi/cm |
| Kapsama | %71,1 |
| En koyu ton | %89,4 |

---

## 6. Prompt üretimi

Prompt **elle yazılmaz**. Bir fonksiyondur:

```
prompt = üslup gövdesi (112 plakada AYNI)
       + konu (plakaya özgü)
       + kompozisyon (sınıfa göre)
       + teknik kuyruk (AYNI)
```

Üslup gövdesi `08_BUILD/make_prompts.py` → `STYLE_BODY` içinde **tek bir
yerde** durur. Değişirse 112 promptun tamamı birlikte değişir. "Tek çizgi
dili" şartı ancak böyle tutulabilir; 112 promptu elle tutarlı yazmak mümkün
değildir.

### Sınıfa göre kompozisyon

| Sınıf | Kompozisyon |
|---|---|
| I · Bekçiler | Frontal, hareketsiz, izleyiciye bakan — kenara çekilmeyecek bir şeyin duruşu |
| II · Yutucular | Sola dönük dörtte üç, ağız kompozisyonun merkezi |
| III · Şekil Değiştirenler | Dönüşümün ortasında, tek siluette iki biçim okunur |
| IV · Su Sakinleri | Yükselen, alt gövde suyun olacağı boşlukta eriyen |
| V · Gök ve Fırtına | Kanatlar tam açık, hafif alttan görünüş |
| VI · Huzursuz Ölüler | Dik ve zayıf, kenarlarda çözülmemiş dış hat |

### Ölçek işareti

Her plakada sol altta düz siyah bir insan silueti — yüzsüz, detaysız.
Okur ölçeği bir cümleden değil **bir bakıştan** almalıdır.

---

## 7. Zemin neden boş

Sahne, zemin çizgisi, ufuk, çerçeve ve süs **yasaktır**. Üç sebep:

1. **Tutarlılık.** 112 farklı sahne, 112 farklı üslup demektir. Boşluk tek
   ortak paydadır.
2. **Sayfa yerleşimi.** Plaka madde sayfasının üst yarısına oturur; alt yarı
   metindir. Sahne, metin sütununu görsel olarak yarıştırır.
3. **Başvuru cildi olmak.** Bu bir sanat kitabı değil, bir atlastır. 19. yüzyıl
   doğa tarihi plakaları da boşluktadır ve sebebi aynıdır.

`measure_background` kenar bandındaki mürekkep oranını ölçer; %2'yi geçen
plaka reddedilir.

---

## 8. Yayın formatları

`convert_plates.py` her normalize plakadan dört format üretir:

| Format | Dosya | Kısıt | Neden |
|---|---|---|---|
| Baskı | `plate-NNN.tif` | 300 DPI, LZW, kayıpsız | JPEG artefaktı ince tarama çizgilerini yok eder |
| Kindle | `plate-NNN.png` | **≤60 KB**, 16 ton, ≤900 px | 112 plaka optimize edilmezse teslim ücreti telifin %30'unu yer |
| A+ | `plate-NNN.jpg` | RGB, ≤2 MB | Amazon CMYK reddeder |
| Web | `plate-NNN.webp` | ≤300 KB · 16 ton · **kayıpsız** · ≤1400 px | Site, basın kiti, Pinterest. Kayıplı sıkıştırma bu çizgi dilinde bütçeyi üçe katlar (§ 1b) |

EPUB toplam bütçesi **7 MB**; hedef 112 plakada ≤6 MB.
`convert_plates.py --check` mevcut plakalardan 112'ye ekstrapole eder;
`--calibrate` ise plaka gelmeden kalibrasyon kurgusundan ekstrapole eder.
**Faz 2 ölçümü: 3,74 MB** — bütçenin içinde (§ 1b).

---

## 9. AI beyanı

İllüstrasyonlar AI ile üretilir ve insan eliyle vektör temizliğinden geçer.
Bu, üç yerde **açıkça** beyan edilir:

1. KDP yükleme ekranındaki AI içerik beyanı (zorunlu)
2. Kitabın künye sayfası
3. Arka maddedeki illüstrasyon notu — sürecin kendisi anlatılır

Dürüst beyan, Risk 7'nin (AI illüstrasyon tepkisi) tek gerçek azaltıcısıdır.
