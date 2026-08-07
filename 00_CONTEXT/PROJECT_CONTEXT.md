# PROJECT CONTEXT — CODEX BESTIARIUM

> **Bu belge, projeyi aylar sonra devralacak kişi (veya ajan) içindir.**
> Hiçbir şeyi hatırladığınız varsayılmaz. Buradaki her sayı ya bir dosyadan
> ölçülmüştür ya da bir kod satırından türetilmiştir; ikisi de gösterilmiştir.
>
> Son güncelleme: **7 Ağustos 2026** — üretim sistemi kuruldu
> Kök dizin: `/home/emre/Downloads/MY-DİGİTAL-BOOK/CODEX_BESTIARIUM`

---

## 1. Bir cümlede durum

Üretim sistemi **kuruldu ve test edildi**. `spec.json`'da 120 tohum kaydı,
on beş doğrulama betiği, CI/CD hattı, 120 plakalık prompt kütüphanesi ve
altı fazlık uygulama yol haritası hazır. **Kitabın tek kelimesi yazılmadı**
ve yazılmayacak — Faz 1 araştırmadır, yazım Faz 3'te başlar ve **kurucu
onayı bekliyor**.

---

## 2. Proje genel görünümü

| | |
|---|---|
| **Ürün** | *Codex Bestiarium: A World Bestiary* — Codex Serisi Cilt II |
| **Yazar / künye** | Emre Doğan · Vâliçe Press |
| **Dil** | Kitabın kendisi **İngilizce**. Bu belgeler ve raporlar Türkçe. |
| **Kapsam** | 120 yaratık · 40 gelenek · 6 sınıf · 8 akraba imge ailesi |
| **Hacim** | ~404 sayfa · ~92.000 kelime · 6 × 9 inç |
| **İllüstrasyon** | 120 çizgi plaka, tek gravür dilinde |
| **Platform** | Amazon KDP — Ciltsiz · Ciltli · Büyük punto · Kindle |
| **Kaynak** | `01_SOURCE/spec.json` — **tek doğruluk kaynağı** |
| **Depo** | `emredogan-cloud/codex-bestiarium` (public) |
| **Takvim** | Eylül 2026 başlangıç → **Mayıs 2027** yayın |
| **İş yükü** | ~436 saat · ayda ~55 saat |

### Editoryal tez

Her kültürde bir su atı vardır. Her kültürde bir gece cadısı, bir eşik
bekçisi, bir fırtına kuşu vardır. Kitap yaratıkları anlatmıyor — **aynı
korkunun kırk ayrı yüzünü** anlatıyor.

Raf, yaratıkları **nereden geldiklerine** göre düzenliyor. Hiç kimse **ne
yaptıklarına** göre düzenlemedi. Coğrafi tasnif bir *katalog* üretir;
işlevsel tasnif bir *tez* üretir — ve tez, kopyalanamayan tek şeydir.

---

## 3. Bu turda ne yapıldı

Talimat açıktı: *"Your first responsibility is to build a production system…
Treat this book like a software product."* Yapılan tam olarak budur.

| # | Teslim | Yol |
|---|---|---|
| 1 | Bölüm 10'daki klasör ağacı | depo kökü |
| 2 | Fontlar ve devralınan 27 betik Mythologica'dan kopyalandı | `07_ASSETS/fonts/` · `08_BUILD/` |
| 3 | **120 tohum kaydı** master yol haritasından *türetildi* | `01_SOURCE/spec.json` |
| 4 | Kitap kayıt defteri — sınıflar, aileler, bantlar, yasak kalıplar | `08_BUILD/bestiarium.py` |
| 5 | Şema doğrulayıcı, dört kapı seviyesiyle | `08_BUILD/validate_spec.py` |
| 6 | Beş metin kalite kapısı | `08_BUILD/qa_*.py` |
| 7 | **Kapıların kendi testi** — kasıtlı kusurlu kurgu ile | `08_BUILD/tests/selftest.py` |
| 8 | Plaka normalizasyonu + tutarlılık ölçümü | `08_BUILD/plates.py` |
| 9 | Plaka format dönüştürücü (baskı · Kindle · A+ · web) | `08_BUILD/convert_plates.py` |
| 10 | Dört dizin üreticisi | `08_BUILD/make_index.py` |
| 11 | **120 plakalık prompt kütüphanesi** | `BESTIARIUM_IMAGE_PROMPTS.html` |
| 12 | Depo/belge/varlık bütünlüğü denetimi | `08_BUILD/validate_structure.py` |
| 13 | Otomatik belge güncelleyici | `08_BUILD/update_docs.py` |
| 14 | CI/CD hattı — dört iş akışı | `.github/workflows/` |
| 15 | **Altı fazlık uygulama yol haritası** | `CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md` |
| 16 | KDP yayın kılavuzu | `BESTIARIUM_KDP_PUBLISHING_GUIDE.md` |

Master yol haritası yeni mühendisliği **54 saat** olarak modellemişti;
tamamı bu turda yazıldı ve Faz 1–2 saatlerinden düşüldü.

---

## 4. Klasör yapısı

```
CODEX_BESTIARIUM/
├── 00_CONTEXT/     PROJECT_CONTEXT · BRIEF · STYLE · STYLE_PLATES · SCOPE_DECISIONS
├── 01_SOURCE/
│   ├── spec.json            120 kayıt — TEK DOĞRULUK KAYNAĞI
│   ├── plate_subjects.json  120 İngilizce görsel betimleme
│   ├── indexes.json         üretilmiş dört dizin
│   ├── research/<id>.md     120 araştırma dosyası (Faz 1)
│   └── book.json            yazılmış metin (Faz 3+) — .gitignore'da
├── 02_MANUSCRIPT/  DOCX yedeği
├── 03_COVER/       artwork · PAPERBACK/ HARDCOVER/ LARGEPRINT/
├── 03_APLUS/       5 modül (biri akraba imge tablosu)
├── 04_PRINT/       ★ KDP'ye yüklenecek iç bloklar
├── 05_KINDLE/      reflowable EPUB (≤7 MB)
├── 06_REPORTS/     doğrulama JSON'ları · üretim raporları
├── 07_ASSETS/
│   ├── fonts/               Cinzel + EB Garamond (OFL)
│   ├── plates_raw/          ham AI çıktıları — DEĞİŞTİRİLMEZ
│   ├── plates/              normalize edilmiş 120 plaka
│   └── plates_print · plates_kindle · plates_aplus · plates_web
├── 08_BUILD/       bütün hat
└── 09_ARCHIVE/     aşılmış sürümler
```

---

## 5. `spec.json` — tek doğruluk kaynağı

Dizinler, promptlar, istatistikler, ilerleme ölçümü ve dizgi — hepsi buradan
türer. İki yerde tutulan bir sayı, er geç iki farklı sayı olur.

### Nasıl üretildi

Elle yazılmadı. `08_BUILD/seed_import.py`, master yol haritasının Bölüm 04
tablosunu **ayrıştırır**:

```bash
python3 08_BUILD/seed_import.py \
    --source ../CODEX_MYTHOLOGICA/03_CODEX_BESTIARIUM_MASTER_ROADMAP.html
python3 08_BUILD/seed_import.py --check     # spec kaynakla uyumlu mu?
```

`--check` CI'da her push'ta koşar: `spec.json` kaynağından ayrışırsa derleme
kırmızı yanar.

### Kayıt şeması

```json
{
  "id": "each-uisce",              // dosya adı, çapraz referans anahtarı
  "number": 16,
  "name": "Each-uisce",            // geleneğin kendi yazımı, diakritikler korunur
  "pronunciation": "",             // Faz 2
  "tradition": "eriu",
  "class": "IV",                   // I–VI
  "motif": ["B184.1.3"],           // Thompson kodları
  "motifVerified": false,          // Faz 1 kapısı
  "kinFamily": "A",                // A–H veya null
  "altNames": [],
  "region": "",                    // Faz 1
  "attested": "",                  // Faz 1
  "sources": [],                   // Faz 1: ≥2 BAĞIMSIZ kaynak
  "crossRefs": [],                 // Faz 2: 2–5, karşılıklı
  "plate": "plate-016",
  "wordTarget": 700,
  "variantNote": "",
  "restrictionScreened": false,    // yaşayan gelenek kapısı
  "seedNoteTr": "…",               // tohum tablosunun tek satırlık tanımı
  "researchFile": "01_SOURCE/research/each-uisce.md",
  "status": "draft"                // draft|verified|written|edited|final
}
```

### Ölçülen mevcut durum

| | |
|---|---:|
| Yaratık kaydı | **120** |
| Gelenek | **40** (19'u Cilt 1'den devralındı) |
| Benzersiz Thompson kodu | 70 |
| Aileye bağlı madde | 61/120 |
| Kaynak riski yüksek gelenek | 8 |

---

## 6. ⚠ Devralınan iki tutarsızlık

Bunlar **hata değil**, master yol haritasının iki bölümü arasındaki gerçek
farklardır. `validate_spec.py` ikisini de her koşuda uyarı olarak basar ve
**Faz 2 bunları çözmek zorundadır** — çünkü ikisi de doğrudan sayfa bütçesine,
dolayısıyla baskı maliyetine ve fiyata bağlıdır.

### ① Sınıf dağılımı

| Sınıf | Bölüm 03.1 hedefi | Bölüm 04 tohum tablosu | Sapma |
|---|---:|---:|---:|
| I · Bekçiler | 22 | **19** | −3 |
| II · Yutucular | 28 | **29** | +1 |
| III · Şekil Değiştirenler | 22 | **20** | −2 |
| IV · Su Sakinleri | 24 | **25** | +1 |
| V · Gök ve Fırtına | 14 | **17** | +3 |
| VI · Huzursuz Ölüler | 10 | **10** | — |
| | 120 | 120 | |

Toplam tutuyor, dağılım tutmuyor. Sınıf başına sayfa hedefi (Bölüm 05.3)
**hedef sayılara** göre hesaplanmış; tohum dağılımıyla kullanılırsa sayfa
bütçesi kayar.

### ② Akraba aile üyelikleri

Bölüm 03.2 tablosu 55 maddenin bir aileye bağlı olduğunu söylüyor; tohum
tablosunun `Aile` sütunu **61** diyor. Fark üç ailede toplanıyor:

| Aile | Bölüm 03.2 | Tohum tablosu |
|---|---:|---:|
| C · Gece cadısı | 9 | **14** |
| D · Fırtına kuşu | 8 | **9** |
| E · Derinlerin yılanı | 9 | **15** |

Bölüm 03.2 muhtemelen *manşet üyeleri* listeliyor; tohum tablosu daha geniş
bir üyelik tanımlıyor. Faz 2 hangisinin karşılaştırma açılışlarına gireceğine
karar verir — iki sayfalık bir açılışa 15 üye sığmaz.

---

## 7. Kalite kapıları — mimari

Merkezde tek bir fikir var: **kalite ölçülür, göz kararıyla kabul edilmez.**

### Kapı seviyeleri kümülatiftir

```
draft  →  phase1  →  phase2  →  phase3
```

Aktif seviye depo kökündeki **`.gate`** dosyasındadır. Bir kapı açıldıktan
sonra kapanamaz: sonraki her push açılmış bütün kapılardan geçmek zorundadır.
**Kalite geriye gidemez.**

### Metin kapıları metin yokken yeşil kalır

`qa_*.py` betikleri `book.json` yokken **0 döner**. Bu kasıtlıdır: henüz
açılmamış bir kapı yüzünden CI kırmızı yanmaz. Ama metin geldiğinde otomatik
devreye girerler.

### Kapıların kendi testi — en önemli test

```bash
python3 08_BUILD/tests/selftest.py
```

İki kurgu kitap: biri temiz, biri **her kapıya kasıtlı bir kusur**
yerleştirilmiş. Temiz olan geçmeli, kusurlu olan yakalanmalıdır.

> **Metin yokken yeşil kalan bir hat, kusur geldiğinde de yeşil kalabilir.**
> Bu test o riski kapatır ve CI'da her push'ta koşar.

Bu test ilk çalıştırmasında gerçek bir kusur buldu: kurgu üreteci sabit
adımlı bir sayaç kullandığı için (31 kelimelik sözlük, 7 adım, gcd=1) kendi
kendini tekrarlıyordu ve `qa_echo` haklı olarak alarm verdi. Düzeltilen betik
değil, **kurgu** oldu.

---

## 8. Devralınan hat — Codex Mythologica'dan

Cilt 1'in hattı **kitaba özgü değildir**. `editions.py` bir sürüm kayıt
defteri, `paths.py` bir yol tablosudur; ikisi de olduğu gibi çalışır.

### Cilt 1'den devralınan üç ders

Bunlar tekrar keşfedilmez:

1. **Tek ve aynı ölçek çarpanı.** Kapak görseli X ve Y'de aynı katsayıyla
   ölçeklenir. Farklı katsayı = kayma. (Cilt 1'de %3,03 anizotropi ciltsiz
   yayınını durdurmuştu.)
2. **Sırt merkezi = tuval merkezi.** Her zaman. Görseldeki dekoratif bandın
   *merkezi* buraya oturur; filetolar katlama çizgisi olarak kullanılamaz.
3. **Metin canlı vektör, sayfa kutusu tam ölçü.** O zaman KDP hiç ölçeklemez.

### Ciltli kalibrasyonu hazır

KDP ciltli kapak formülünü yayımlamaz. Cilt 1'de resmî Case Laminate
şablonundan ölçüldü ve `08_BUILD/kdp_calibration.json` olarak devralındı.
Kritik bulgu: **karton sırt payı 0,125" değil 0,1885"** — 1,61 mm'lik bu
hata sırt yazısını katlama çizgisine itmeye yeter.

### reportlab'in üç gizli tuzağı

1. `canvas.setCharSpace` **yoktur**; harf aralığı metin nesnesinde ayarlanır
   ve sıfır olsa bile **her seferinde** çağrılmalıdır (grafik durumunda taşınır).
2. reportlab her Canvas'ı **Helvetica** ile başlatır ve bu font hiç
   kullanılmasa bile **gömülmeden** yazılır. KDP gömülü olmayan fontu reddeder.
3. `instantiateVariableFont(..., updateFontNames=False)` çağrılırsa sabit
   örnekler aynı iç adı taşır ve reportlab onları **tek fonta indirger**.
   Doğrulama: `pdffonts` çıktısında **dört** ayrı font görünmeli.

---

## 9. Komutlar

```bash
cd /home/emre/Downloads/MY-DİGİTAL-BOOK/CODEX_BESTIARIUM

# kurulum (yalnızca üretim için gerekir)
./08_BUILD/bootstrap.sh

# bütün kalite kapıları — CI'ın çalıştırdığının birebir aynısı
./08_BUILD/qa_all.sh
./08_BUILD/qa_all.sh phase1        # kapıyı yükselterek
./08_BUILD/qa_all.sh --fix         # üretilen belgeleri tazeleyerek

# tek tek
python3 08_BUILD/seed_import.py --check
python3 08_BUILD/validate_spec.py --gate draft -v
python3 08_BUILD/validate_structure.py -v
python3 08_BUILD/tests/selftest.py
python3 08_BUILD/qa_length.py --sections -v
python3 08_BUILD/plates.py --pilot -v
python3 08_BUILD/convert_plates.py
python3 08_BUILD/make_index.py
python3 08_BUILD/make_prompts.py
python3 08_BUILD/update_docs.py
```

### Bağımlılıklar

Kalite kapılarının **hiçbiri** üçüncü taraf pakete ihtiyaç duymaz — hepsi
standart kütüphaneyle koşar. CI'ın ana doğrulama işi bu yüzden saniyeler
sürer ve hiçbir kuruluma bağlı değildir.

Üretim (plaka, dizgi, kapak, EPUB) için: pillow, numpy, reportlab, fonttools,
pypdf, python-docx, ebooklib, pyyaml + sistem aracı olarak `poppler-utils`.

> **Debian/Ubuntu notu:** PEP 668 yüzünden `pip install` doğrudan çalışmaz.
> `bootstrap.sh` bir venv kurar (`08_BUILD/.venv`).

> **Bellek notu:** bu iş istasyonunda 16 GB RAM var ve OOM geçmişi mevcut.
> Ciltli kapak derlemesi ~13,6 MP görüntüyle çalışır; aynı anda ağır başka
> iş çalıştırmayın.

---

## 10. Bilinen sorunlar ve açık kararlar

| # | Konu | Durum |
|---|---|---|
| 1 | Sınıf dağılımı tutarsızlığı (§ 6①) | Faz 2 çözecek |
| 2 | Akraba aile üyelik tutarsızlığı (§ 6②) | Faz 2 çözecek |
| 3 | **Herkese açık depoda proza** | Faz 3 öncesi karar — [yol haritası § A1](../CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md#a1--depo-herkese-açık-manuscript-ne-olacak) |
| 4 | Kapsam 120/40 mı 100/35 mi | Faz 1'in 3. haftasında ölçülecek |
| 5 | Vektör temizlik dışarıya verilecek mi | Faz 2'de pilot süresi ölçülünce |
| 6 | `STYLE.md` ses kalibrasyon örnekleri boş | Faz 1'de Cilt 1'den kopyalanacak |
| 7 | Kindle Translate uygunluğu belirsiz | 120 plaka kapıyı kapatabilir; **finansal modele dahil edilmedi** |
| 8 | Kamu malı yanlış sınıflandırma riski | Cilt 1'den devralındı; künyede özgünlük beyanı + özgün Giriş/Sonsöz savunma olarak yazılacak |

---

## 11. Sıradaki adım

**Kurucu onayı bekleniyor.** Faz 1 ve Faz 2 tamamen planlandı; talimat gereği
bir oturumda ikiden fazla faz yürütülmez ve **yazım Faz 3'te başlar**.

Onay geldiğinde:

```
"Melanezya, Ainu ve Kartveli geleneklerinden dokuz yaratık için iki
 bağımsız kaynak bul, Thompson motif kodlarını doğrula ve
 01_SOURCE/research/<id>.md dosyalarını yaz. Proza yazma."
```
