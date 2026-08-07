# CHANGELOG — Codex Bestiarium

Bu dosya **elle yazılır** çünkü editoryal karar içerir. `BOOK_STATS.md` ve
`ROADMAP_PROGRESS.md` otomatiktir; bu değildir.

Biçim: [Keep a Changelog](https://keepachangelog.com/tr/1.1.0/) ·
Sürümleme: [SemVer](https://semver.org/lang/tr/) — `0.x` faz, `1.0` yayın.

**Her fazın kapanışında bu dosyaya bir sürüm bloğu eklenir.**
Blokta en az şunlar bulunur: eklenenler, kararlar (gerekçesiyle), ölçülen
sayılar, açık kalanlar.

---

## [Yayımlanmamış]

### Sıradaki
- Faz 3 · Çekirdek yazım (Bekçiler ve Yutucular) — **kurucu onayı bekliyor**

---

## [0.2.1] — 2026-08-07

**Kısıtlılık kapısında ölü kural.** Faz 2'nin kapanış ölçümleri sırasında
bulundu ve hemen kapatıldı.

### Kararlar

| # | Karar | Gerekçe |
|---|---|---|
| D28 | `LIVING_TRADITIONS` kimlikleri düzeltildi ve **kapıya bir kapı eklendi** | Listedeki `ityop-ya` ve `ma-ohi` hiçbir gelenek kimliğine denk gelmiyordu (`spec.json` `ityopya` ve `maohi` yazıyor). Denk gelmeyen satır sessizce ÖLÜ BİR KURALDIR: kapı o geleneği hiç denetlemez ve hiçbir yerde hata görünmez. Ityop'ya maddesi (Buda) zorunlu kısıtlılık kapısının **dışında** kalmıştı. `validate_spec.check_structure` artık her kimliğin gerçek bir geleneğe denk geldiğini denetliyor. |

### Neden önemli

Buda maddesi, kitabın **en hassas etik notunu** taşıyor: buda suçlaması
tarihsel olarak Beta Israel'e ve zanaatkâr kastlara yöneltilmiş, gerçek
insanlara zarar vermiş bir suçlamadır. Araştırmacı taramayı zaten yapmış ve
notu yazmıştı — **kapı yakalamamıştı**. Yani kapının sessizliği, kalitenin
kanıtı değil, araştırmacının titizliğinin gölgesiydi.

Yaşayan gelenek kapısı bu kitabın etik omurgasıdır (Risk 3). Bir omurga
kendini de denetlemelidir.

### Düzeltilenler

- `BOOK_STATS.md` "Kısıtlılık taraması" satırı yanlış paydayla (112) %39
  gösteriyordu; oysa tarama yalnızca yaşayan gelenek maddelerinde zorunlu.
  Artık **35/35 (%100)** ve gönüllü yapılan 9 tarama ayrıca belirtiliyor.
  "Buradaki her sayı ölçülmüştür" diyen bir belgede yanlış payda, yanlış
  sayının kendisi kadar pahalıdır.

---

## [0.2.0] — 2026-08-07

**FAZ 2 TAMAMLANDI.** Tasnif kilitlendi, çapraz referans grafiği kuruldu,
plaka ölçüm hattı kalibre edildi, madde sayfası dizildi ve ölçüldü.

### Devralınan iki tutarsızlık — kapatıldı

**① Sınıf dağılımı.** Yol haritası Bölüm 03.1'in hedefleri 120 maddelik
kapsam için hesaplanmıştı; kapsam Faz 1'de 112'ye kilitlendi. Hedef gerçeğe
göre güncellendi, madde zorlanmadı. Eski hedefler `roadmapTargetEntries` /
`roadmapTargetPages` olarak tarihsel kayıtta duruyor.

**② Akraba aile üyelikleri (55 mi 61 mi).** Soru, iki AYRI şeyin tek sütunda
toplanmasından doğuyordu. Ayrıştırıldı — üyelik ve manşet kadro. Hiçbir
araştırma atılmadı.

### Kararlar

| # | Karar | Gerekçe |
|---|---|---|
| D21 | Sınıf hedefi **ölçülen gerçeğe** güncellendi, madde yeniden sınıflandırılmadı | Hedefler 120 maddelik bir kitap için hesaplanmıştı ve o kitap artık yok. K1 tasnifin işleve göre olduğunu söyler; sayısal bir hedef işlevi ezemez. Yol haritası her iki yolu da meşru sayıyor. |
| D22 | **Boitatá V → I** | Tek sınıf düzeltmesi ve iki bağımsız kanıtı var. (1) Kendi araştırma dosyasının yazım notu: *"Ormanı koruyan ateş… Curupira ile aynı işlevin başka biçimi"* — Curupira sınıf I'dir. (2) Doğrulanan kod B19.4.2, sınıf I'in çıpa aralığında (B11–B19); sınıf V'inki A280 · B31 · F960. Sapma her iki sınıfta da hedefe yaklaştı. |
| D23 | Aile üyeliği **iki katmanlı**: üye (59) ve manşet kadro (48) | 55 ile 61 arasındaki fark bir çelişki değil, bir kategori hatasıydı. İki sayfalık bir açılışa 15 üye sığmaz; ama üyeliği 9'a indirmek de araştırılmış malzemeyi atmak olurdu. Manşet kadro açılışa, uzun kuyruk akraba imge tablosuna ve kendi maddesine gider. İkisi de tam üyedir. |
| D24 | Üç aile motif kodu düzeltildi | Faz 1'in madde düzeyindeki bulgusu aile düzeyine taşındı. **B**: `D113.1` *Transformation: man to wolf* → `D113.3` *man to fox* (aile tilki ailesidir). **C**: `G264` *La Belle Dame Sans Merci — witch entices **men*** → `G262` *Murderous witch* (ailenin avı erkek değil loğusa ve yeni doğandır). **G**: `F460` *Mountain-spirits* → `F567` *Wild man* (dört üyenin üçü F567 taşıyor). |
| D25 | **Dış hat kalınlığı kapı olmaktan çıkarıldı** | Kalibrasyonda kontur kalınlığı 2,9 / 4,2 / 5,83 px olan kurgular ayırt edilemedi — sebep geometrik: kontur (5,8 px) ile tarama periyodu (4,7 px) aynı mertebede. Ayırt edemeyen bir sayıyla plaka reddetmek, ölçüyormuş gibi yapmaktır. Sayı raporda kalıyor, karar vermiyor. Yerine **tarama darbesi/periyot** kapısı geldi — bandı sıklıktan türüyor ve doğruluğu %0,3 ölçüldü. |
| D26 | Sayfa bütçesi **380 → 436** | Prova dizgisi ölçtü: madde içeriği 2,558 sayfa, maliyeti 3 sayfa. Fark plaka kuralının bedelidir (plaka üst yarıya oturur → madde sayfa başından başlar). Yol haritası Faz 3 notu emrediyor: *"kelime hedefini değil sayfa bütçesini düzelt"*. K3 dokunulmadı; telif üç sürümde de pozitif kaldı. |
| D27 | Web plakası **kayıplıdan kayıpsıza** çevrildi | 1800 px / kalite 86 WebP 954 KB veriyordu — bütçenin üç katı. İnce 45° tarama kayıplı kodlayıcı için en kötü durumdur. 16 ton + kayıpsız, 1400 px → 159 KB ve artefaktsız; aynı boyutta kayıplı sürüm 474 KB'ydi. |

### Bulunan ve düzeltilen üç gerçek kusur

**① Plaka ölçümü 45° taramada √2 yanlıydı.** Kalınlık, tarama yönüne dik
olmayan kesitlerden okunuyordu. Şartnamedeki geometriye **birebir uyan** kurgu
plakası reddediliyordu — yani hat, doğru çizilmiş 112 plakanın tamamını geri
çevirecekti. Hata %41 → **%0,3**.

**② Plaka şartnamesi kendi kendisiyle çelişiyordu.** Hem "22–28 çizgi/cm" hem
"çizgi kalınlığı 1,4 pt" deniyordu; 25 çizgi/cm'de periyot 4,72 px, 1,4 pt ise
5,83 px — bir periyoda kendinden geniş bir darbe sığmaz.

**③ `selftest` kapı testi her faz kapanışında kendini yanlışlıyordu.**
"Bir üst kapı kapalı olmalı" varsayımı, phase2 açıldığı anda phase3 zaten
geçtiği için kırmızıya dönecekti. Metin kapılarındaki yöntem şema kapılarına
da getirildi: gerçek spec'ten türetilen dört kurgu, her kapı seviyesine tam
bir kusur. Dördü de yakalandı.

### Eklenenler

**Veri ve tasnif**
- `01_SOURCE/kin_map.json` — Faz 2'nin editoryal katmanı (elle yazılır):
  181 çapraz referans bağı, sekiz ayrışma cümlesi, sekiz açılış planı,
  altı sınıf açılışı konu başlığı
- `08_BUILD/classify.py` — kin_map → `spec.json` + `KIN_OPENINGS.md` +
  çapraz referans grafiği raporu; 13 kontrol
- `00_CONTEXT/KIN_OPENINGS.md` — sekiz karşılaştırma açılışının içerik planı
  (üretilir; 405 satır)
- `seed_import.py --sync` — kapsam kararı eklendiğinde tohum alanlarını
  araştırmayı silmeden tazeler
- 44 maddeye gerçek alternatif ad; diakritiksiz biçim artık **türetiliyor**
  (telaffuz rehberi 112 → 289 satır)

**Plaka hattı**
- `08_BUILD/tests/plate_fixtures.py` — geometrisi bilinen gravür kurguları
- `08_BUILD/tests/plate_selftest.py` — ölçümün doğruluğu + kapının ısırması
- `convert_plates.py --calibrate` — format bütçelerini plaka gelmeden ölçer
- `.github/workflows/plates.yml` → `calibration` işi

**Dizgi**
- `08_BUILD/entry_page.py` — madde sayfası tasarımı ve prova dizgisi
- `build.yml` fontları indiriyor (SIL OFL 1.1) — CI dizgiyi **ilk kez** sınıyor

### Ölçülenler

| | |
|---|---:|
| Çapraz referans bağı (karşılıklı) | 181 |
| Madde başına ortalama | 3,23 |
| Aileye bağlı madde | 59/112 |
| Manşet üye · uzun kuyruk | 48 · 11 |
| Telaffuz rehberi satırı | 289 |
| Plaka ölçüm doğruluğu (tarama darbesi) | %0,3 hata |
| 112 plakalık EPUB projeksiyonu | 3,74 MB (bütçe 6 MB) |
| Ölçülen madde içeriği | 2,558 sayfa |
| Sayfa bütçesi | **436** |
| Ciltsiz birim telif | 8,76 $ |

### Açık kalanlar

- [ ] **Pilot plaka seti (10 ham plaka)** — hat hazır ve kalibre; ham AI
  çıktısı hattın dışındaki tek girdidir ve kurucudan gelir
- [ ] **A1** — depo public kalacaksa proza nerede duracak (Faz 3 öncesi)
- [ ] **A3** — vektör temizlik dışarıya verilecek mi (pilot süresi ölçülünce)
- [ ] Dış hat tahmincisi gerçek plakalarda yeniden değerlendirilecek

---

## [0.1.0] — 2026-08-07

**FAZ 1 TAMAMLANDI.** Kapsam kilitlendi: **112 yaratık · 40 gelenek**.

### Eklenenler
- 112 araştırma dosyası (`01_SOURCE/research/`) — hepsi kapıdan geçti
- `01_SOURCE/motif_index.json` — **123 doğrulanmış Thompson kodu**
- `01_SOURCE/motif_index_full.json` — **24.975 kod**, tam nüshadan ayrıştırıldı
- `01_SOURCE/research_data/` — 40 gelenek dosyası (araştırmanın kaynağı)
- `00_CONTEXT/SOURCING_STANDARD.md` — kaynak gösterme ölçütü
- `08_BUILD/research_gen.py` — araştırma → 112 uniform dosya + spec senkronu
- `editions.py` → `verify_royalties()` — fiyat/telif doğrulaması
- `STYLE.md` — Cilt 1'den **üç gerçek** ses kalibrasyon paragrafı

### Kapsam kilidi
| | |
|---|---:|
| Aday | 120 |
| **Kilitlenen** | **112** |
| Düşürülen | 8 |
| Değiştirilen | 1 (Kaia → Temes Savsap) |
| Yeniden sınıflandırılan | 1 (Rusalka IV → VI) |
| Doğrulanmış | **112 (%100)** |

Düşen sekiz maddenin gerekçesi `SCOPE_DECISIONS.md` § 3'te. **Kırk gelenek
iddiası korundu** — hiçbir gelenek tamamen boşalmadı.

### Kararlar
| # | Karar | Gerekçe |
|---|---|---|
| D16 | Kapsam **112'de** kilitlendi, 100'de değil | Yol haritası "<112 ise kapsam 100'e iner" der. Ama 112 doğrulandı; tabana inmek doğrulanmış malzemeyi ATMAK olurdu. |
| D17 | `sv` (sub verbo) güçlü doğrulama sayıldı | SOURCING_STANDARD § 3 zaten `s.v.`'yi kesin yer sayıyordu; § 4'ün tablosu bunu yansıtmıyordu. İki bölüm çelişiyordu; çelişki giderildi. Ölçüt değişmedi: *okur kesin bir yere gidebiliyor mu*. |
| D18 | Düşen maddelerin araştırma dosyaları **korundu** | `09_ARCHIVE/dropped-research/`. Yapılan iş ve düşürme gerekçesi kayıt altında kalmalı. |
| D19 | Rusalka IV → VI | Zelenin 1916'nın BAŞLIĞI tezini söylüyor: *"Doğal olmayan ölümle ölenler ve rusalkalar"*. Tasnif işleve göredir, mekâna göre değil. |
| D20 | `selftest` kapı testi **dinamikleştirildi** | "phase1 kapalı olmalı" varsayımı Faz 1 bitince kendini yanlışlıyordu. Artık `.gate`i okuyup BİR ÜSTÜNÜN kapalı olduğunu sınıyor. |

### Motif kodu düzeltmeleri — **20 tohum kodu düzeltildi**
İki **sistematik** hata bulundu ve yazımdan önce giderildi:
- **`G264` gece cadısı ailesinin kodu değil.** Tanımı *"La Belle Dame Sans
  Merci — witch entices **men** with offers of love"*. 14 madde yanlış
  kodlanmıştı. Doğrusu `G262.0.1` / `G442` / `G262.1` ailesi.
- **`B31` bölüm başlığıdır, `B31.1` 'Roc'tur.** Sīmurgh `B31.5`, Garuḍa `B56`,
  Ziz `B31.1.0.1`, Camazotz `B31.4`, fırtına kuşları `A284.2`.

> ⚠ Önceki turda `B31`'in 'Roc' olduğu **yanlış** kaydedilmişti; tam nüsha
> ayrıştırması düzeltti. Tohum tablosunun Rukh için verdiği `B31.1` baştan
> doğruydu.

Ayrıca 18 tekil düzeltme (`D113.1` kurt≠tilki, `D113.2` sırtlan≠köpekgil,
`A812` earth-diver≠gövdeden-yeryüzü, `B733`→`E17` diriltme, …).

### Ölçülenler
| | |
|---|---:|
| Araştırma dosyası | 112 |
| Bağımsız kaynak künyesi | 328 |
| Madde başına ortalama künye | 2.9 |
| Doğrulanmış motif kodu | 123 |
| Çıkarılan motif kodu (tam nüsha) | 24.975 |
| Kısıtlılık taraması | 112/112 |

---

## [0.1.0-alpha] — 2026-08-07

Üretim sisteminin kurulumu. **Kitabın tek kelimesi yazılmadı.**

### Eklenenler

**Veri**
- `01_SOURCE/spec.json` — 120 tohum kaydı, master yol haritası § 04'ten
  *türetildi* (elle yazılmadı)
- `01_SOURCE/plate_subjects.json` — 120 İngilizce görsel betimleme
- `08_BUILD/seed_import.py` — yol haritası HTML → `spec.json`, `--check` moduyla

**Kalite kapıları**
- `08_BUILD/bestiarium.py` — kitap kayıt defteri (sınıf, aile, bant, yasak kalıp)
- `08_BUILD/validate_spec.py` — dört kapı seviyeli şema ve bütünlük denetimi
- `08_BUILD/qa_length.py` · `qa_voice.py` · `qa_drift.py` · `qa_echo.py` ·
  `qa_diacritics.py` — beş metin kapısı
- `08_BUILD/validate_structure.py` — depo, belge, varlık bütünlüğü
- `08_BUILD/tests/selftest.py` + `make_fixtures.py` — **kapıların kendi testi**

**İllüstrasyon**
- `08_BUILD/plates.py` — normalizasyon + beş parametreli tutarlılık ölçümü
- `08_BUILD/convert_plates.py` — baskı TIFF · Kindle PNG · A+ JPEG · WebP
- `08_BUILD/make_prompts.py` + `BESTIARIUM_IMAGE_PROMPTS.html` — 120 plakalık
  prompt kütüphanesi
- `00_CONTEXT/STYLE_PLATES.md` — çizgi dili şartnamesi

**Üretim**
- `08_BUILD/make_index.py` — dört dizin (gelenek · motif · akraba imge · telaffuz)
- `08_BUILD/update_docs.py` — `BOOK_STATS.md` + `ROADMAP_PROGRESS.md`
- `08_BUILD/bootstrap.sh` · `qa_all.sh`
- Codex Mythologica'dan 27 betik devralındı (kapak, iç blok, A+, DOCX/EPUB)

**Belgeler**
- `CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md` — altı faz, tek doğruluk kaynağı
- `00_CONTEXT/PROJECT_CONTEXT.md` · `STYLE.md` · `BRIEF.md` · `SCOPE_DECISIONS.md`
- `BESTIARIUM_KDP_PUBLISHING_GUIDE.md`
- `README.md` · `CONTRIBUTING.md` · `LICENSE` · `.gitignore`

**CI/CD**
- `.github/workflows/validate.yml` — her push'ta kalite kapıları
- `.github/workflows/build.yml` — DOCX/EPUB/PDF üretimi
- `.github/workflows/plates.yml` — plaka ölçümü
- `.github/workflows/release.yml` — etiketli sürüm
- Issue şablonları · PR şablonu

### Kararlar

| # | Karar | Gerekçe |
|---|---|---|
| D1 | Master yol haritasının **on fazı altı uygulama fazına** indirgendi | Altı faz tek başına sürüm etiketi hak etmeyecek kadar küçüktü. Her fazın sonunda yayınlanabilir bir artefakt olmalı. |
| D2 | **İllüstrasyon fazlara dağıtıldı**, tek fazda toplanmadı | Master yol haritası illüstrasyonu yazımla paralel yürütüyor ve bunu Mayıs 2027 hedefinin tek dayanağı sayıyor. Tek faza toplamak o kazancı yok eder. Artık her faz kendi sınıflarının plakalarını üretir. |
| D3 | `spec.json` **elle yazılmadı, türetildi** | 120 kaydı elle yazmak bir transkripsiyon hatası kaynağıdır. Yol haritası tek doğruluk kaynağıdır; `seed_import.py --check` ayrışmayı CI'da yakalar. |
| D4 | Kalite kapıları **standart kütüphaneyle** yazıldı | CI'ın ana doğrulama işi hiçbir kuruluma bağlı olmadan saniyeler içinde koşar. Ağır bağımlılıklar yalnızca üretimde. |
| D5 | Kapılar **kümülatif** ve `.gate` dosyasıyla yönetiliyor | Kalite geriye gidemez. Bir kapı açıldıktan sonra kapanamaz. |
| D6 | Metin kapıları metin yokken **0 döner** | Henüz açılmamış bir kapı yüzünden CI kırmızı yanmamalı. Ama bu, kapının kör olması riskini doğurur — `selftest.py` o riski kapatır. |
| D7 | Prompt **üretilir**, elle yazılmaz | Üslup gövdesi tek yerde durur; değişirse 120 prompt birlikte değişir. "Tek çizgi dili" şartı ancak böyle tutulabilir. |
| D8 | Depo **public**, proza `.gitignore`'da | Talimat public depo diyor; 92.000 kelimelik metnin açık depoda durması KDP fiyat eşleştirmesi, kamu malı yanlış sınıflandırması ve intihal riski taşır. Faz 3 öncesi kurucu kararı: yol haritası § A1. |
| D9 | Çakışan yaratık adları **kimlikte ayrıştırıldı** | Hellenic *Lámia* ve Euskal *Lamia* diakritik düşünce aynı slug'a iniyordu → `lamia-hellenic` · `lamia-euskal`. Dizinde çapraz gönderme zorunlu. |
| D10 | Birincil BISAC `FIC010000` → **`SOC011000`** | *Bestiarium* bir başvuru cildidir; Cilt 1 bir kurgu antolojisiydi. Üçüncül BISAC yine de Cilt 1'in rafında görünmeyi sağlar. |

### Ölçülenler

| | |
|---|---:|
| Yaratık kaydı | 120 |
| Gelenek | 40 (19'u Cilt 1'den devralındı) |
| Benzersiz Thompson motif kodu | 70 |
| Aileye bağlı madde | 61 |
| Kaynak riski yüksek gelenek | 8 |
| Üretilen prompt | 120 |
| Yazılan yeni betik | 15 |
| Devralınan betik | 27 |
| Otomatik kontrol (`qa_all.sh`) | 14 kapı |

### Bulunan tutarsızlıklar

Bunlar bu turda **keşfedildi** ve Faz 2'ye devredildi. İkisi de master yol
haritasının iki bölümü arasındaki gerçek farklardır:

- **Sınıf dağılımı.** Bölüm 03.1 hedefi ile Bölüm 04 tohum tablosu uyuşmuyor
  (I: 19≠22, III: 20≠22, V: 17≠14). Sayfa bütçesi hedef sayılara göre
  hesaplandığı için bu doğrudan baskı maliyetini etkiler.
- **Akraba aile üyelikleri.** Bölüm 03.2 "55 madde bir aileye bağlı" diyor;
  tohum tablosu **61** diyor. Fark C (9→14), D (8→9) ve E (9→15) ailelerinde.
  İki sayfalık bir karşılaştırma açılışına 15 üye sığmaz.

`validate_spec.py` ikisini de her koşuda uyarı olarak basar.

### Süreçte düzeltilenler

- **Test kurgusu kendi kendini tekrarlıyordu.** İlk `make_fixtures.py` sabit
  adımlı bir sayaçla kelime seçiyordu (31 kelimelik sözlük, 7 adım, gcd=1);
  üreteç aynı diziyi tekrarlıyor ve iki bölüm aynı 8-gram'ı taşıyordu.
  `qa_echo` bunu doğru şekilde yakaladı. Düzeltilen betik değil **kurgu** oldu.
- **`validate_structure.py` kendi kaynağını kirletiyordu.** Görünmez karakter
  tablosu o karakterleri *doğrudan* içeriyordu; tarama kendini yakaladı.
  Tablo kaçış dizisine çevrildi.
- **Satır içi kod, çift boşluk sanılıyordu.** Tipografi taraması kod
  bloklarını *silerek* maskeliyordu; `` `a` b `` ifadesi `  b` oluyor ve
  "çift boşluk" olarak raporlanıyordu. Artık tek bir yer tutucuya dönüşüyor.
- **`qa.py` Cilt 1'e özgüydü ve import anında çöküyordu.** Yol haritası
  Bölüm 10 onu devralınacak betikler arasında sayıyor ama dosya generic
  değil: modül düzeyinde `build/book.json` okuyor ve Mythologica'nın hikâye
  kimliklerine (`cu-chulainn`, `sekhmet`…) sabitlenmiş. `09_ARCHIVE/`'e
  taşındı. Bestiarium'un beş QA betiği zaten onun yerini fazlasıyla alıyor.
- **Boş klasörler depoya girmiyordu.** `.gitignore` `09_ARCHIVE/` dizinini
  komple yok sayıyordu; negatif kalıp (`!.gitkeep`) dizin dışlandığında
  çalışmaz. `09_ARCHIVE/*` biçimine çevrildi.
- **`plates.yml` pip önbelleği koşulsuzdu.** İş yalnızca plaka varsa pip
  kuruyor; kurmadığında `setup-python`'ın post adımı "cache folder doesn't
  exist" diye çöküyordu. Önbellek kaldırıldı.
- **Türkçe `İ` çıpayı kırıyordu.** `İ` küçültülünce `i` + U+0307 olur;
  slugifier birleşen işareti atıyor ve doğru bir bağlantıyı kırık sanıyordu.

### Açık kalanlar

- [ ] **A1** — depo public kalacaksa proza nerede duracak (Faz 3 öncesi)
- [ ] **A2** — kapsam 120/40 mı 100/35 mi (Faz 1, 3. hafta)
- [ ] **A3** — vektör temizlik dışarıya verilecek mi (Faz 2, pilot sonrası)
- [ ] `STYLE.md` ses kalibrasyon örnekleri Cilt 1'den kopyalanacak (Faz 1)
- [ ] `editions.py`'ye Bestiarium sürümleri eklenecek (Faz 1)

---

[Yayımlanmamış]: https://github.com/emredogan-cloud/codex-bestiarium/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/emredogan-cloud/codex-bestiarium/releases/tag/v0.2.1
[0.2.0]: https://github.com/emredogan-cloud/codex-bestiarium/releases/tag/v0.2.0
[0.1.0]: https://github.com/emredogan-cloud/codex-bestiarium/releases/tag/v0.1.0
[0.1.0-alpha]: https://github.com/emredogan-cloud/codex-bestiarium/releases/tag/v0.1.0-alpha
