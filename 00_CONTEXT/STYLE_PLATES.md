# STYLE_PLATES — Çizgi dili şartnamesi

> **Projenin tek gerçek başarısızlık modu burada yönetilir.**
>
> 120 plaka tek bir çizgi dilinde durmazsa kitap "derleme" gibi görünür ve
> premium konumlanma çöker. Bu risk **ölçülerek** yönetilir — göz kararıyla
> değil. Bir insan on plakayı kalibre edebilir; yüz yirmisini edemez.

---

## 1. Şartname

Bütün değerler `08_BUILD/bestiarium.py` → `PLATE_SPEC` içindedir.
Bu tablo o sözlüğün insan okunur hâlidir; **ikisi ayrışırsa kod geçerlidir**.

| Parametre | Değer | Tolerans | Ölçen |
|---|---|---|---|
| Teknik | gravür / hat taraması (line engraving), tek renk | — | — |
| Tuval | 1:1,25 dikey · 1800 × 2250 px @ 300 DPI | sabit | `measure_aspect` |
| Ana çizgi kalınlığı | 1,4 pt (≈5,8 px @ 300 DPI) | ±%15 | `measure_line_weight` |
| Tarama açısı | 45° birincil · 135° ikincil | ±5° | `measure_hatch` (FFT) |
| Tarama sıklığı | cm başına 22–28 çizgi | bant | `measure_hatch` |
| En koyu ton | %92 siyah | ±%5 | `measure_ink_range` |
| En açık ton | %8 siyah | ±%5 | `measure_ink_range` |
| Kapsama | yaratık tuvalin %62–78'i | bant | `measure_coverage` |
| Zemin | **boş** — yaratık boşlukta durur, sahne yok | zorunlu | `measure_background` |
| Ölçek işareti | her plakada ince bir insan silueti | zorunlu | insan kontrolü |
| Bakış | sola veya izleyiciye | — | insan kontrolü |

**Bant dışına çıkan plaka otomatik reddedilir ve yeniden üretilir.**
Bu karar insana bırakılmaz.

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

### ② Çizgi kalınlığı medyandır, ortalama değil

Koyu koşu uzunlukları ölçülür ve **medyanı** alınır. Ortalama alınırsa tek bir
dolu alan (ör. bir gözün siyahı) ölçümü bozar; medyan bozulmaz. 60 pikselden
uzun koşular "dolu alan" sayılıp elenir.

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
üretilir. Ham dosya kaybolursa 120 plaka yeniden çizilir.

---

## 4. Pilot set kilidi

**On plaka onaylanmadan diğer 110'a geçilmez.**

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
| `plate-110` | Animikii | V | Aile D tutarlılığı (Sīmurgh ile karşılaştırma) |
| `plate-115` | Huldufólk | I | Aile H — topluluk kompozisyonu |
| `plate-106` | Curupira | I | Aile G — insan siluetine en yakın |

### Onay ölçütü

1. `plates.py --pilot -v` → **tolerans dışı plaka sıfır**
2. On plaka **yan yana** dizilir ve gözle bakılır: aynı elden çıkmış görünüyor
   mu? Ölçüm geçiyor ama göz "hayır" diyorsa **tolerans bandı dardır, ölçüm
   eksiktir** — banda yeni bir parametre eklenir.
3. Ölçülen dağılım (ortalama + standart sapma) bu belgeye yazılır ve üretim
   setinin karşılaştırma tabanı olur.

---

## 5. Ölçülen dağılım

> **Faz 2 görevi.** Pilot set onaylandığında `06_REPORTS/plate-consistency.json`
> çıktısındaki dağılım buraya yazılır. Üretim setinin (110 plaka) dağılımı
> bununla **örtüşmek zorundadır**; örtüşmüyorsa üslup gövdesi kaymıştır.

| Parametre | Ortalama | Std sapma | Aralık |
|---|---|---|---|
| Çizgi kalınlığı (pt) | — | — | — |
| Tarama sıklığı (çizgi/cm) | — | — | — |
| Kapsama | — | — | — |
| En koyu ton | — | — | — |

---

## 6. Prompt üretimi

Prompt **elle yazılmaz**. Bir fonksiyondur:

```
prompt = üslup gövdesi (120 plakada AYNI)
       + konu (plakaya özgü)
       + kompozisyon (sınıfa göre)
       + teknik kuyruk (AYNI)
```

Üslup gövdesi `08_BUILD/make_prompts.py` → `STYLE_BODY` içinde **tek bir
yerde** durur. Değişirse 120 promptun tamamı birlikte değişir. "Tek çizgi
dili" şartı ancak böyle tutulabilir; 120 promptu elle tutarlı yazmak mümkün
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

1. **Tutarlılık.** 120 farklı sahne, 120 farklı üslup demektir. Boşluk tek
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
| Kindle | `plate-NNN.png` | **≤60 KB**, 16 ton, ≤900 px | 120 plaka optimize edilmezse teslim ücreti telifin %30'unu yer |
| A+ | `plate-NNN.jpg` | RGB, ≤2 MB | Amazon CMYK reddeder |
| Web | `plate-NNN.webp` | ≤300 KB | Site, basın kiti, Pinterest |

EPUB toplam bütçesi **7 MB**; hedef 120 plakada ≤6 MB.
`convert_plates.py --check` mevcut plakalardan 120'ye ekstrapole eder ve
bütçe aşılacaksa **şimdiden** uyarır.

---

## 9. AI beyanı

İllüstrasyonlar AI ile üretilir ve insan eliyle vektör temizliğinden geçer.
Bu, üç yerde **açıkça** beyan edilir:

1. KDP yükleme ekranındaki AI içerik beyanı (zorunlu)
2. Kitabın künye sayfası
3. Arka maddedeki illüstrasyon notu — sürecin kendisi anlatılır

Dürüst beyan, Risk 7'nin (AI illüstrasyon tepkisi) tek gerçek azaltıcısıdır.
