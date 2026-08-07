# CODEX BESTIARIUM — UYGULAMA YOL HARİTASI

> **Bu belge tek doğruluk kaynağıdır.**
> Master yol haritası (`03_CODEX_BESTIARIUM_MASTER_ROADMAP.html`) *ne* yapılacağını
> söyler; bu belge *nasıl, hangi sırayla, hangi kapıdan geçerek* yapılacağını söyler.
> İkisi çeliştiğinde **bu belge** geçerlidir ve çelişki `CHANGELOG.md`'ye yazılır.
>
> Oluşturma: **7 Ağustos 2026** · Sürüm **1.0** · Vâliçe Press · Codex Serisi Cilt II
> Kök dizin: `/home/emre/Downloads/MY-DİGİTAL-BOOK/CODEX_BESTIARIUM`

---

## İçindekiler

- [0. Tek bakışta](#0-tek-bakışta)
- [1. Master yol haritasından on faz → altı faz](#1-master-yol-haritasından-on-faz--altı-faz)
- [2. Kapı sistemi](#2-kapı-sistemi)
- [3. Devralınan ve yeni araçlar](#3-devralınan-ve-yeni-araçlar)
- [4. Kilitlenmiş kararlar](#4-kilitlenmiş-kararlar)
- [5. Açık kararlar — kurucudan yanıt bekleyen](#5-açık-kararlar--kurucudan-yanıt-bekleyen)
- [FAZ 1 — Altyapı, Araştırma ve Kapsam Kilidi](#faz-1--altyapı-araştırma-ve-kapsam-kilidi)
- [FAZ 2 — Tasnif, Veri Modeli ve Pilot Plaka Seti](#faz-2--tasnif-veri-modeli-ve-pilot-plaka-seti)
- [FAZ 3 — Çekirdek Yazım · Bekçiler ve Yutucular](#faz-3--çekirdek-yazım--bekçiler-ve-yutucular)
- [FAZ 4 — Genişleme · Şekil Değiştirenler ve Su Sakinleri](#faz-4--genişleme--şekil-değiştirenler-ve-su-sakinleri)
- [FAZ 5 — Tamamlama, İllüstrasyon ve Editoryal İnceleme](#faz-5--tamamlama-i̇llüstrasyon-ve-editoryal-i̇nceleme)
- [FAZ 6 — Üretim, KDP ve Lansman](#faz-6--üretim-kdp-ve-lansman)
- [6. Risk kaydı](#6-risk-kaydı)
- [7. Yarın sabah ne yapılacak](#7-yarın-sabah-ne-yapılacak)

---

## 0. Tek bakışta

| | |
|---|---|
| **Ürün** | *Codex Bestiarium: A World Bestiary* — Codex Serisi Cilt II |
| **Kitabın dili** | **İngilizce.** Bu belgeler, raporlar ve commit mesajları Türkçe. |
| **Kapsam** | 120 yaratık · 40 gelenek · 6 sınıf · 8 akraba imge ailesi |
| **Hacim** | ~404 sayfa · ~92.000 kelime · 6 × 9 inç |
| **İllüstrasyon** | 120 çizgi plaka, tek gravür dilinde |
| **Formatlar** | Ciltsiz · Ciltli · Büyük punto · Kindle |
| **Toplam iş** | ~436 saat · 6 faz |
| **Takvim** | Eylül 2026 başlangıç → **Mayıs 2027** yayın (ayda ~55 saat) |
| **Depo** | `emredogan-cloud/codex-bestiarium` — public |

### Faz yükü dağılımı

| Faz | Başlık | Saat | Madde | Sayfa | Kelime | Etiket |
|---:|---|---:|---:|---:|---:|---|
| 1 | Altyapı, Araştırma ve Kapsam Kilidi | 55 | 0 yazılır · 120 araştırılır | 0 | ~24.000 (araştırma notu) | `v0.1.0` |
| 2 | Tasnif, Veri Modeli ve Pilot Plaka Seti | 84 | 0 yazılır · 120 doğrulanır | 0 | ~4.000 (tasnif metni) | `v0.2.0` |
| 3 | Çekirdek Yazım · Bekçiler ve Yutucular | 68 | **48** | **138** | ~35.600 | `v0.3.0` |
| 4 | Genişleme · Şekil Değiştirenler ve Su Sakinleri | 64 | **45** | **126** | ~33.100 | `v0.4.0` |
| 5 | Tamamlama, İllüstrasyon ve Editoryal İnceleme | 99 | **27** | **140** | ~24.900 | `v0.5.0` |
| 6 | Üretim, KDP ve Lansman | 66 | — | 404 dizilir | — | `v1.0.0` |
| | **Toplam** | **436** | **120** | **404** | **~93.600** | |

Sayfa sayıları master yol haritası Bölüm 05.3'ün sayfa bütçesinden gelir.
Kelime sayıları madde başına 700 kelime × madde sayısı + ön/arka madde payıdır.
**Bunlar model değil hedeftir**; gerçek değer dizgi çalıştırıldığında
`04_PRINT/` çıktısından ölçülür ve `BOOK_STATS.md` otomatik güncellenir.

---

## 1. Master yol haritasından on faz → altı faz

Master yol haritası on faz tanımlar. Uygulama altı fazda yürür çünkü on faz,
altısı tek başına bir sürüm etiketi hak etmeyecek kadar küçük parçalar içerir
ve her fazın sonunda bir **yayınlanabilir artefakt** olması gerekir.

| Master faz | Saat | Uygulama fazı |
|---|---:|---|
| Faz 0 · Araştırma | 45 | **1** |
| Faz 1 · Ana hat ve kapsam kilidi | 10 | **1** |
| Faz 2 · Dünya yapısı — tasnif ve akraba aileler | 15 | **2** |
| Faz 3 · Yaratık veritabanı | 35 | **2** |
| Faz 6 · İllüstrasyon — hat kurulumu + pilot | 34 | **2** |
| Faz 4 · Madde yazımı (sınıf I–II) | 42 | **3** |
| Faz 6 · İllüstrasyon (48 plaka) | 26 | **3** |
| Faz 4 · Madde yazımı (sınıf III–IV) | 39 | **4** |
| Faz 6 · İllüstrasyon (45 plaka) | 25 | **4** |
| Faz 4 · Madde yazımı (sınıf V–VI + matter) | 24 | **5** |
| Faz 6 · İllüstrasyon (27 plaka) | 15 | **5** |
| Faz 5 · Editoryal inceleme | 60 | **5** |
| Faz 7 · Dizgi ve dosya üretimi | 28 | **6** |
| Faz 8 · Yayın | 16 | **6** |
| Faz 9 · Pazarlama | 22 | **6** |

**İllüstrasyon neden dağıtıldı?** Master yol haritası illüstrasyonu (Faz 6)
yazımla (Faz 4) *paralel* yürütür ve bunu Mayıs 2027 hedefinin tek dayanağı
olarak gösterir. Paralel bir işi tek bir uygulama fazına toplamak o kazancı
yok eder. Bunun yerine illüstrasyon, yazımla **aynı fazın içinde** ve **aynı
sınıfların plakaları** olarak yürür: sınıf I ve II yazılırken sınıf I ve II
plakaları üretilir. Böylece her fazın sonunda o sınıfın maddesi *ve* plakası
birlikte biter — yarım bir bölüm kalmaz.

---

## 2. Kapı sistemi

Kapılar **kümülatiftir**. Bir kapı açıldıktan sonra kapanamaz: sonraki her
push, açılmış bütün kapılardan geçmek zorundadır. Kalite geriye gidemez.

| Kapı | Komut | Açıldığı an |
|---|---|---|
| `draft` | `validate_spec.py --gate draft` | şimdi — her zaman açık |
| `phase1` | `validate_spec.py --gate phase1` | Faz 1 bitişi |
| `phase2` | `validate_spec.py --gate phase2` | Faz 2 bitişi |
| `phase3` | `validate_spec.py --gate phase3` | Faz 3 başlangıcı |

Aktif kapı seviyesi depo kökündeki **`.gate`** dosyasında durur. Bir fazı
kapatmak, o dosyayı yükseltmek demektir — ve bu, geri alınamayan tek
manuel işlemdir.

```bash
./08_BUILD/qa_all.sh              # .gate dosyasındaki seviyeyle
echo phase1 > .gate               # kapıyı yükselt (faz kapanışında)
./08_BUILD/qa_all.sh              # artık phase1 de zorunlu
```

### Metin kapıları

Bu betikler metin yokken **0 döner** ve CI'ı yeşil bırakır; metin geldiğinde
otomatik devreye girerler. Bu davranış `08_BUILD/tests/selftest.py` ile
kanıtlanmıştır — kasıtlı kusurlu bir kurgu kitap çalıştırılır ve her betiğin
o kusuru yakaladığı doğrulanır. **Yakalamayan bir kapı, kapı değildir.**

| Betik | Ne arar | Kırmızı yakma ölçütü |
|---|---|---|
| `qa_length.py` | kelime bandı | madde 620–790 dışında, bölüm bandı dışında, boş bölüm |
| `qa_voice.py` | yasak kalıp | "it is said", oyun terimi, üstünlük, sevimlileştirme, ünlem |
| `qa_drift.py` | üslup sürüklenmesi | en sık 50 kelimede %35'ten büyük eğim |
| `qa_echo.py` | tekrar | maddeler arası 8+ kelimelik birebir öbek |
| `qa_diacritics.py` | adlandırma | diakritik düşürülmüş ad, görünmez karakter |
| `plates.py` | çizgi dili | tolerans dışı plaka |
| `validate_structure.py` | depo | kırık bağlantı, bayat belge, terminoloji, yapı |

---

## 3. Devralınan ve yeni araçlar

Codex Mythologica'nın hattı **kitaba özgü değildir**; `editions.py` bir sürüm
kayıt defteri, `paths.py` bir yol tablosudur. İkisi de olduğu gibi devralındı.

| Betik | Kaynak | İşi | Bu projede yeni iş |
|---|---|---|---:|
| `cover_spec.py` · `typography.py` · `make_cover_*.py` · `validate_cover.py` | Mythologica | kapak geometrisi, tipografi, PDF, 39–45 kontrol | 0 sa |
| `editions.py` · `paths.py` | Mythologica | sürüm kayıt defteri, yol tablosu | 0 sa |
| `make_pdf.py` · `matter.py` · `model.py` | Mythologica | iç blok, ön/arka madde | 4 sa |
| `aplus_*.py` · `make_aplus*.py` · `validate_aplus.py` | Mythologica | A+ modülleri, 79 kontrol | 2 sa |
| `edits.py` · `qa.py` | Mythologica | programatik düzeltme kaydı | 2 sa |
| `make_docx_epub.py` | Mythologica | DOCX + EPUB | 3 sa |
| **`bestiarium.py`** | **YENİ** | kitap kayıt defteri — sınıf, aile, bant, yasak kalıp | ✅ hazır |
| **`seed_import.py`** | **YENİ** | master yol haritası § 04 → `spec.json` | ✅ hazır |
| **`validate_spec.py`** | **YENİ** | şema + bütünlük + kapı seviyeleri | ✅ hazır |
| **`qa_voice.py` · `qa_length.py` · `qa_drift.py` · `qa_echo.py` · `qa_diacritics.py`** | **YENİ** | metin kalite kapıları | ✅ hazır |
| **`plates.py`** | **YENİ** | plaka normalizasyonu + tutarlılık ölçümü | ✅ hazır |
| **`convert_plates.py`** | **YENİ** | PNG → baskı TIFF · Kindle PNG · A+ JPEG · WebP | ✅ hazır |
| **`make_index.py`** | **YENİ** | dört dizin | ✅ hazır |
| **`make_prompts.py`** | **YENİ** | 120 plakalık prompt kütüphanesi | ✅ hazır |
| **`validate_structure.py`** | **YENİ** | depo, belge, varlık bütünlüğü | ✅ hazır |
| **`update_docs.py`** | **YENİ** | `BOOK_STATS.md` + `ROADMAP_PROGRESS.md` | ✅ hazır |
| **`tests/selftest.py`** | **YENİ** | kalite kapılarının kendi testi | ✅ hazır |

Master yol haritası yeni mühendisliği **54 saat** olarak modellemişti.
Bu turda **tamamı yazıldı ve test edildi** — Faz 1–2 saatlerinden düşülmüştür.

---

## 4. Kilitlenmiş kararlar

Bunlar tartışmaya kapalıdır. Değişirse takvim yeniden hesaplanır ve
`CHANGELOG.md`'ye gerekçesiyle yazılır.

| # | Karar | Gerekçe |
|---|---|---|
| K1 | Tasnif **işleve göre**, bölgeye göre değil | Kitabın tek ayrışma noktası. Bölgesel seriler bunu geriye dönük kuramaz. |
| K2 | Her maddede **≥2 bağımsız kaynak + ≥1 Thompson kodu** | Kitabı derlemeden başvuru cildine yükselten tek şey. |
| K3 | Madde **700 kelime ± %12** (620–790) | 620 altı yüzeysel; 790 üstü kitabı 440 sayfaya taşır ve fiyatı bozar. |
| K4 | **Yedi bölümlü madde yapısı**, sıra değişmez | Bir bölüm boşsa madde yazılmamıştır, kısaltılmamıştır. |
| K5 | **Yumuşatma yok** | Cilt 1'in editoryal kararı korunur. |
| K6 | Trim **6 × 9 inç** · krem kâğıt · siyah-beyaz · mat kapak | Cilt 1 ile rafta hizalı; normal trim maliyeti. |
| K7 | Tipografi **Cinzel + EB Garamond** (SIL OFL 1.1) | Seri sesi değişmez. |
| K8 | Ciltli **lansmanla birlikte** açılır | Bu bir hediye ürünü; Cilt 1'den farklı. |
| K9 | Genişletilmiş dağıtım **açılmaz** · KDP Select'e **girilmez** | Telif 9,14 $ → 4,15 $ düşer; KU'da başvuru cildi zayıftır. |
| K10 | Avustralya Aborjin gelenekleri **kitaba alınmaz** | Anlatı topluluk mülkiyetindedir; Sonsöz'de bir tercih olarak yazılır. |
| K11 | Kindle **reflowable** üretilir | Kindle Translate uygunluğu için tek şans; sabit düzen o kapıyı kapatır. |
| K12 | Plaka toleransı **ölçülür**, göz kararıyla kabul edilmez | 120 plakada göz kalibrasyonu kayar. Bu, projenin tek gerçek başarısızlık modudur. |
| K13 | Tek seferde **en fazla üç madde** yazılır | Daha fazlası üslup sürüklenmesi üretir — portföy denetiminde ölçülmüş bir hata. |
| K14 | `spec.json` **tek doğruluk kaynağıdır** | Dizinler, promptlar, dizgi, istatistik — hepsi ondan türer. |

---

## 5. Açık kararlar — kurucudan yanıt bekleyen

> Bunlar **Faz 1'i bloke etmez** ama Faz 3 başlamadan yanıtlanmalıdır.

### Durum tablosu — 7 Ağustos 2026

| # | Konu | Durum |
|---|---|---|
| A1 | Depo public, proza nerede durur | ✅ **kapandı** — (a) şıkkı · CHANGELOG D29, D30 |
| A2 | Kapsam 120/40 mı 100/35 mi | ✅ **kapandı** — Faz 1'de 112/40'a kilitlendi |
| A3 | Vektör temizlik dışarıya verilecek mi | ⏳ açık — pilot süresi ölçülünce; ham plaka girdisine bağlı (D39) |
| A4 | İllüstrasyon: ham AI plakaları kim üretir | ✅ **kapandı** — kurucu üretir, Faz 5'ten önce · D39 |
| A5 | Üslup sürüklenmesi ne zaman düzeltilir | ✅ **kapandı** — Faz 5, editoryal geçiş · D40 |
| A6 | Kayıtlı vaka açığı için ek araştırma turu | ✅ **kapandı** — yapılmaz; davranış temelli yaklaşım sürer · D41 |

### A1 · Depo herkese açık, manuscript ne olacak?

Depo talimat gereği **public**tir. Bugün bunun bir maliyeti yok: depoda kod,
CI, belge ve *metadata* var — **proza yok**. Ama Faz 3'te 92.000 kelimelik
metin gelecek ve o metnin herkese açık bir depoda durması üç somut risk taşır:

1. **KDP fiyat eşleştirmesi.** Amazon, aynı içeriği başka bir yerde ücretsiz
   bulursa e-kitap fiyatını sıfıra çekebilir.
2. **Kamu malı yanlış sınıflandırması.** Cilt 1'in bilinen sorunlarından
   biri buydu (`PROJECT_CONTEXT.md` § 13, sorun 5). Herkese açık tam metin
   bu riski artırır.
3. **İntihal ve AI eğitim verisi.** Metin doğrudan kopyalanabilir hâle gelir.

**Şu anki yapılandırma (varsayılan):** `.gitignore` proza yollarını
(`01_SOURCE/book*.json`, `04_PRINT/**/*.pdf`, `05_KINDLE/*.epub`,
`02_MANUSCRIPT/*.docx`) dışarıda tutar. CI, proza *varsa* denetler; yoksa
yeşil kalır. Araştırma dosyaları (`01_SOURCE/research/`) **depodadır** —
onlar künye ve alıntı notudur, kitabın prozası değildir ve iki kaynak
kapısının denetlenebilmesi için gereklidirler.

**Faz 3 başlamadan seçilecek:**

| Seçenek | Ne olur | Öneri |
|---|---|---|
| **(a)** Depo public kalır, proza depo dışında | CI proza denetimini yerelde yapar (`./08_BUILD/qa_all.sh`); üretim hattı ve belgeler açık kalır | ✅ **önerilen** |
| (b) Depo private olur, proza depoya girer | CI tam kapsam denetler; açık kaynak vitrini kaybolur | değerli ama vitrin kaybı |
| (c) Depo public, proza da depoda | Tam CI + tam vitrin; yukarıdaki üç risk kabul edilir | önerilmez |

### A2 · Kapsam: 120/40 mı, 100/35 mi?

Master yol haritası (b) şıkkını öneriyor: 120/40 korunur, yayın Mayıs 2027.
Bu belge o öneriyi **varsayılan olarak almıştır**. Faz 1'in üçüncü haftasında
doğrulanmış madde sayısı 70'in altındaysa karar yeniden açılır.

### A3 · Vektör temizlik dışarıya verilecek mi?

Master yol haritası plaka başına ~25 dakika insan geçişi ve dışarıya verme
maliyetini plaka başına 2–4 $ olarak modelliyor (120 plakada 240–480 $).
Faz 2'nin pilot seti bittiğinde gerçek süre ölçülecek ve karar verilecek.

---

## FAZ 1 — Altyapı, Araştırma ve Kapsam Kilidi

> **55 saat** · bağımlılık: yok · **Git etiketi `v0.1.0`** · Kilometre taşı **Faz 1 · Temel**

### Amaç

120 adayın her biri için iki bağımsız kaynak bulmak, Thompson motif kodunu
doğrulamak ve kapsamı **kilitlemek**. Bu fazın çıktısı metin değil,
**doğrulanmış bilgidir**. Bir tek cümle proza yazılmaz.

Sıra kasıtlıdır: **en zor sekiz gelenekle başlanır** (Melanesia, Ainu,
Kartveli, Hayk, Sápmi, Nusantara, Ityop'ya, Mongol) çünkü kapsamı bunlar
belirleyecektir. Kolay olanlar (Hellenic, Norðr, Yamato) sona bırakılır —
onlar zaten bulunacaktır ve erken bulmak yanlış bir güven verir.

### Çıktılar

| # | Çıktı | Yol |
|---|---|---|
| 1 | 120 araştırma dosyası | `01_SOURCE/research/<id>.md` |
| 2 | Doğrulanmış Thompson kod listesi | `spec.json` → `motifVerified: true` |
| 3 | Kaynak bulunamayan adaylar + yedek liste | `00_CONTEXT/SCOPE_DECISIONS.md` |
| 4 | Yaşayan gelenek kısıtlılık taraması | `spec.json` → `restrictionScreened: true` |
| 5 | Nihai 40 gelenek ve madde sayısı — **kilitli** | `00_CONTEXT/BRIEF.md` |
| 6 | Sayfa bütçesinin bölüm bölüm dağılımı | `00_CONTEXT/BRIEF.md` |
| 7 | Fiyat ve telif doğrulaması | `00_CONTEXT/BRIEF.md` |
| 8 | *(bu turda teslim edildi)* üretim sistemi, CI/CD, belgeler | depo kökü |

**Tahmini sayfa:** 0 (manuscript) · **Tahmini kelime:** ~24.000 (araştırma notu, 120 × ~200)
**Yaratık sayısı:** 0 yazılır · **120 araştırılır**

### Araştırma görevleri

- [ ] Her madde için **≥2 bağımsız kaynak** bul. Künye tam olacak: yazar, eser, yıl, sayfa.
- [ ] Motif kodunu **Thompson Motif-Index**'ten doğrula. Tohum tablosundaki kod bir *öneridir*; doğrulanmadan `motifVerified` işaretlenmez.
- [ ] Varyantları not et: "İskoçya'da yer, İrlanda'da yalnızca boğar" — çelişki kusur değil, otoritenin kanıtıdır.
- [ ] Yaşayan gelenek maddeleri için **kısıtlılık taraması**: yalnızca yayımlanmış ve kısıtlanmamış malzeme. Kısıtlı olduğu bilinen anlatı **anlatılmaz, kısıtlı olduğu söylenir**.
- [ ] `region` ve `attested` alanlarını doldur. "Eski çağlardan beri" yazılmaz; tarih verilir.
- [ ] Telaffuz taslağı topla (Faz 2'de kesinleşir).
- [ ] Kaynak bulunamayan maddeyi **listeden düşür** ve yedeğini not et.

### Yazım görevleri

- [ ] **Yok.** Bu fazda proza yazılmaz. Araştırma dosyası bir künye ve alıntı belgesidir, bir taslak değil.
- [ ] `00_CONTEXT/STYLE.md`'ye Codex Mythologica'dan **gerçek** üç örnek paragraf eklenir (ses kalibrasyonu için).

### Editoryal görevler

- [ ] `00_CONTEXT/BRIEF.md` yazılır: konumlanma, kitle, ne **değil**.
- [ ] Yasak kalıp listesi gözden geçirilir; `bestiarium.py` içindeki liste güncellenir.
- [ ] Kapsam kararı yazılır: 120/40 mı, 100/35 mi (bkz. [A2](#a2--kapsam-12040-mı-10035-mi)).

### Dizgi görevleri

- [ ] Fontlar `07_ASSETS/fonts/` içinde doğrulanır (Cinzel + EB Garamond, SIL OFL 1.1).
- [ ] `editions.py`'de Bestiarium sürümleri tanımlanır (ciltsiz · ciltli · büyük punto), sayfa sayısı **tahmini** olarak girilir ve `provisional: true` işaretlenir.
- [ ] Sayfa sayısı hedef fiyatta pozitif telif veriyor mu — hesaplanır.

### Doğrulama görevleri

- [ ] `python3 08_BUILD/seed_import.py --check` — spec tohum tablosuyla uyumlu
- [ ] `python3 08_BUILD/validate_spec.py --gate phase1 -v` — **0 başarısız**
- [ ] `python3 08_BUILD/validate_structure.py` — **0 başarısız**
- [ ] `python3 08_BUILD/tests/selftest.py` — bütün kapılar beklendiği gibi
- [ ] `python3 08_BUILD/update_docs.py --check` — belgeler güncel
- [ ] CI **yeşil** (`.github/workflows/validate.yml`)

### Tamamlanma ölçütü

**≥112 madde iki bağımsız kaynakla doğrulanmış.** Yedeklerle 120'ye
tamamlanır. Bu sayının altında kalınırsa kapsam **100'e indirilir** —
uydurmayla doldurulmaz. Uydurma, kitabın tek savunmasını yok eder.

### Definition of Done

1. `validate_spec.py --gate phase1` **0 başarısız** veriyor.
2. 120 (veya kilitlenen sayı) araştırma dosyası depoda ve her biri `_TEMPLATE.md` yapısını taşıyor.
3. Hiçbir maddede `motifVerified: false` **ve** `status != "draft"` birlikte değil.
4. Yaşayan gelenek maddelerinin tamamında `restrictionScreened: true`.
5. `00_CONTEXT/BRIEF.md` yazıldı ve kapsam **kilitlendi**.
6. `.gate` dosyası `phase1` olarak yükseltildi.
7. `CHANGELOG.md`'ye faz kaydı düşüldü; `BOOK_STATS.md` ve `ROADMAP_PROGRESS.md` tazelendi.
8. CI yeşil, `main`'e merge edildi, **`v0.1.0`** etiketi atıldı.

### Claude notları

- **Araştırmacı rolünde çalış, Yazar rolünde değil.** Bu fazda tek bir edebî cümle yazma. Başlangıç emri birebir şudur: *"Melanezya, Ainu ve Kartveli geleneklerinden dokuz yaratık için iki bağımsız kaynak bul, Thompson motif kodlarını doğrula ve `research/<id>.md` dosyalarını yaz. Proza yazma."*
- **Kaynak uydurma.** Bulunmayan bir kaynağı "muhtemelen şurada vardır" diye yazma. Bulunamadıysa maddeyi düşür ve `SCOPE_DECISIONS.md`'ye yaz. Bu, projenin en kolay ihlal edilen ve en pahalı kuralıdır.
- **Bir gelenek bitmeden diğerine geçme.** Gelenek başına üç madde; üçü de bitmeden sonraki geleneğe geçilmez. Yarım bırakılan gelenek, kapsam sayımını yanıltır.
- Her araştırma dosyası bittiğinde `spec.json`'daki ilgili kaydı güncelle (`sources`, `region`, `attested`, `motifVerified`, `status: "verified"`).
- Haftada bir `validate_spec.py --gate phase1` çalıştır. Kapı henüz kapalı olacak; **kaç maddenin geçtiğini** ölç ve `ROADMAP_PROGRESS.md`'ye bak.

### Kurucu notları

- **Bu fazın sonunda kapsam kilitlenir ve bir daha açılmaz.** Kilitten sonra "şu yaratığı da ekleyelim" demek, takvimi yeniden hesaplatmak demektir. Eklemek istediğiniz her şeyi *şimdi* söyleyin.
- Üçüncü haftada bir ara kontrol yapın: doğrulanmış madde sayısı 70'in altındaysa 120/40 hedefi gerçekçi değildir ve 100/35'e inmek **başarısızlık değil, doğru karardır**.
- [A1](#a1--depo-herkese-açık-manuscript-ne-olacak) ve [A3](#a3--vektör-temizlik-dışarıya-verilecek-mi) sorularını bu faz biterken yanıtlayın.
- Zor sekiz geleneğin kaynakları için üniversite kütüphanesi erişimi veya arşiv aboneliği gerekebilir. Bu, planlanmamış tek nakit kalemidir.

### Git etiketi

`v0.1.0` — *Araştırma tamamlandı, kapsam kilitlendi*

### Kilometre taşı

**Faz 1 · Temel** — GitHub Milestone: `Faz 1 · Temel`

---

## FAZ 2 — Tasnif, Veri Modeli ve Pilot Plaka Seti

> **84 saat** · bağımlılık: Faz 1 · **Git etiketi `v0.2.0`** · Kilometre taşı **Faz 2 · Veri**

### Amaç

Doğrulanmış 120 maddeyi **yapıya** oturtmak: her madde tam bir sınıfa, sekiz
aile nihai üyeliklerine, her madde 2–5 çapraz referansa kavuşur. Aynı fazda
çizgi dili **kilitlenir**: on plakalık pilot set üretilir, ölçülür ve
onaylanır. Pilot onaylanmadan tek bir üretim plakası çizilmez.

> ⚠ **Bu faz bir tutarsızlık devralıyor ve onu çözmek zorunda.**
> Master yol haritası Bölüm 03.1 sınıf başına hedef madde sayısı verir;
> Bölüm 04'teki tohum tablosunun gerçek dağılımı ondan sapar:
>
> | Sınıf | Hedef | Tohum | Sapma |
> |---|---:|---:|---:|
> | I · Bekçiler | 22 | 19 | **−3** |
> | II · Yutucular | 28 | 29 | +1 |
> | III · Şekil Değiştirenler | 22 | 20 | **−2** |
> | IV · Su Sakinleri | 24 | 25 | +1 |
> | V · Gök ve Fırtına | 14 | 17 | **+3** |
> | VI · Huzursuz Ölüler | 10 | 10 | — |
>
> `validate_spec.py` bunu her çalıştırmada uyarı olarak basar. Faz 2 ya
> maddeleri yeniden sınıflandırarak hedefe yaklaştırır ya da **hedefi
> gerçeğe göre günceller** ve sayfa bütçesini yeniden dağıtır. İkisi de
> meşrudur; **çözümsüz bırakmak değildir**, çünkü sayfa bütçesi doğrudan
> baskı maliyetine ve fiyata bağlıdır.
>
> Aynı şekilde akraba aile üyelikleri de sapıyor: Bölüm 03.2 tablosu 55
> maddenin bir aileye bağlı olduğunu söylüyor, tohum tablosu **61** diyor
> (C ailesi 9 yerine 14, E ailesi 9 yerine 15). Faz 2 hangisinin doğru
> olduğunu karara bağlar.

### Çıktılar

| # | Çıktı | Yol |
|---|---|---|
| 1 | 120 maddenin altı sınıfa **nihai** dağılımı | `spec.json` |
| 2 | Sekiz ailenin nihai üyelikleri + ayrışma cümleleri | `spec.json` → `kinFamilies` |
| 3 | Sekiz karşılaştırma açılışının içerik planı | `00_CONTEXT/KIN_OPENINGS.md` |
| 4 | Çapraz referans grafiği (döngü ve tek yön kontrolü) | `spec.json` → `crossRefs` |
| 5 | 120 telaffuz alanı dolu | `spec.json` → `pronunciation` |
| 6 | Plaka kimlikleri atanmış | `spec.json` → `plate` ✅ *zaten atandı* |
| 7 | **Pilot plaka seti — 10 plaka, onaylı** | `07_ASSETS/plates/` |
| 8 | Plaka tutarlılık raporu | `06_REPORTS/plate-consistency.json` |
| 9 | `STYLE_PLATES.md` ölçülen değerlerle güncellenmiş | `00_CONTEXT/STYLE_PLATES.md` |

**Tahmini sayfa:** 0 (manuscript) · **Tahmini kelime:** ~4.000 (ayrışma cümleleri + açılış planları)
**Yaratık sayısı:** 0 yazılır · **120 doğrulanır ve tasnif edilir**

### Araştırma görevleri

- [ ] Telaffuz rehberini kesinleştir (120 kayıt). Sesli kitabın en zor kısmı burada çözülür — Faz 6'da değil.
- [ ] Alternatif yazımları (`altNames`) topla; dizinde çapraz gönderme yapılacak (okur "Aughisky" arar, "Each-uisce"a gider).
- [ ] Aile üyeliği tartışmalı maddeler için kaynağa dön: C ve E ailelerinin gerçek sınırı nerede?

### Yazım görevleri

- [ ] Sekiz ailenin **ayrışma cümlesi** yazılır. Ölçüt sert: cümle *gerçek* bir fark söylemeli, süsleme olmamalı. "İrlanda'da yiyicidir, İzlanda'da boğar" geçer; "her kültürde farklı yorumlanır" geçmez.
- [ ] Sekiz karşılaştırma açılışının **planı** yazılır (harita + tablo + hangi plakalar yan yana). Metni Faz 5'te yazılır.
- [ ] Altı sınıf açılışının **konu başlıkları** belirlenir.

### Editoryal görevler

- [ ] **Sınıf dağılımı tutarsızlığı çözülür** (yukarıdaki kutu). Karar `CHANGELOG.md`'ye gerekçesiyle yazılır.
- [ ] **Aile üyelik tutarsızlığı çözülür** (55 mi 61 mi).
- [ ] Sayfa bütçesi nihai sınıf dağılımına göre yeniden dağıtılır; toplam 404 korunur.
- [ ] Her madde en az 2 çapraz referans alır; referanslar **karşılıklı** olur (A→B ise B→A).

### Dizgi görevleri

- [ ] `08_BUILD/plates.py` hattı kurulur ve pilot sette kalibre edilir.
- [ ] Madde başlığı bloğu tasarlanır (Cinzel 500 · 16 pt · 0,06 em aralık + altında gelenek · sınıf · motif satırı).
- [ ] Sınıf işareti (dış üst köşe, Cinzel 8 pt, %30 opaklık) `matter.py`'ye eklenir.
- [ ] Akraba satırı stili (0,4 pt altın fileto + EB Garamond 9,5 pt) tanımlanır.
- [ ] **Bir madde sayfasının prova dizgisi** üretilir — plaka + başlık bloğu + yedi bölüm gerçekten sığıyor mu?

### Doğrulama görevleri

- [ ] `validate_spec.py --gate phase2 -v` — **0 başarısız**
- [ ] `make_index.py --gate phase2` — dört dizin üretiliyor, telaffuz eksiksiz
- [ ] `plates.py --pilot -v` — **tolerans dışı plaka sıfır**
- [ ] `convert_plates.py --check` — pilot setin bütün formatları üretildi, bütçeler tutuyor
- [ ] `make_prompts.py --check` — prompt kütüphanesi spec ile senkron
- [ ] Prova dizgisi: madde sayfasında plaka + metin taşmıyor
- [ ] CI yeşil

### Tamamlanma ölçütü

`validate_spec.py --gate phase2` **0 başarısız** *ve* pilot setin on
plakasının tamamı tolerans bandında *ve* prova dizgisinde bir madde sayfası
taşmadan oturuyor.

### Definition of Done

1. Her madde tam bir sınıfta; hiçbir sınıf 8'in altında veya 32'nin üstünde değil.
2. Sınıf ve aile dağılımı tutarsızlığı **çözüldü** ve karar `CHANGELOG.md`'de.
3. Sekiz ailenin ayrışma cümlesi yazıldı ve editoryal olarak onaylandı.
4. Her maddenin 2–5 karşılıklı çapraz referansı var; kırık referans yok.
5. 120 telaffuz alanı dolu.
6. Pilot set (10 plaka) **onaylandı**; ölçülen dağılım `STYLE_PLATES.md`'ye yazıldı.
7. `.gate` → `phase2`.
8. CI yeşil, merge, **`v0.2.0`** etiketi.

### Claude notları

- **Pilot set kilididir.** On plaka onaylanmadan `plates_raw/` içine on birinci dosyayı koyma. Onay ölçütü göz değil, `plates.py --pilot` çıktısıdır.
- Pilot için altı sınıftan örnek seç: `kerberos` (I), `lamia-hellenic` (II), `kumiho` (III), `each-uisce` (IV), `simurgh` (V), `draugr` (VI) + `manananggal`, `animikii`, `huldufolk`, `curupira`. Bu liste `plates.py` içinde `PILOT_IDS` olarak tanımlıdır.
- Çapraz referansları **karşılıklı** kur. `validate_spec.py` tek yönlü bağı uyarı olarak basar; uyarıyı bırakma.
- Ayrışma cümlesini yazarken kendine sor: *bu cümle iki geleneği gerçekten ayırıyor mu, yoksa ikisi hakkında da doğru olan bir şey mi söylüyor?* İkincisiyse süslemedir, sil.
- Sınıf tutarsızlığını çözerken **maddeyi zorlama**. Bir yaratık iki sınıfa da uyuyorsa, hangi *işlevin* onu tanımladığına bak — kitabın tezi budur.

### Kurucu notları

- **Pilot seti gözünüzle onaylayın.** Ölçüm bandı geçiyor olabilir ama on plaka yan yana konduğunda "aynı elden çıkmış" görünmüyorsa, ölçüm eksik demektir; bana söyleyin, tolerans bandını daraltalım.
- Vektör temizlik süresini bu fazda ölçeceğiz. Plaka başına 25 dakikayı aşıyorsa [A3](#a3--vektör-temizlik-dışarıya-verilecek-mi) kararını dışarıya vermek yönünde alın: 120 plaka × 25 dk = 50 saat, sizin en pahalı saatiniz.
- Sınıf dağılımı kararı sizindir. Ben ölçümü ve iki seçeneği sunacağım; hangisinin kitabın tezine daha uygun olduğunu siz bileceksiniz.

### Git etiketi

`v0.2.0` — *Tasnif kilitlendi, çizgi dili onaylandı*

### Kilometre taşı

**Faz 2 · Veri** — GitHub Milestone: `Faz 2 · Veri`

---

## FAZ 3 — Çekirdek Yazım · Bekçiler ve Yutucular

> **68 saat** · bağımlılık: Faz 2 · **Git etiketi `v0.3.0`** · Kilometre taşı **Faz 3 · Çekirdek**

### Amaç

Kitabın en kalabalık iki sınıfını yazmak ve aynı sınıfların plakalarını
üretmek. Bu faz kitabın **sesini kurar**: sonraki 72 madde bu 48'in ritmini
takip edecektir. Bu yüzden ilk beş madde bittiğinde ayrı bir ses kalibrasyonu
oturumu yapılır.

Sınıf II içinde **gece cadısı ailesi (C)** vardır — master yol haritasının
"kitabın en güçlü tek bölümü" dediği yer. Dokuz gelenek, tek bir korku.
O karşılaştırma açılışının metni bu fazda yazılır.

### Çıktılar

| # | Çıktı | Yol |
|---|---|---|
| 1 | Sınıf I · THE GUARDIANS — 19 madde | `01_SOURCE/book.json` |
| 2 | Sınıf II · THE DEVOURERS — 29 madde | `01_SOURCE/book.json` |
| 3 | İki sınıf açılışı (2'şer sayfa) | `book.json` → `classOpenings` |
| 4 | Karşılaştırma açılışları: **C · Gece cadısı**, **F · Eşik bekçisi**, **G · Yaban adamı**, **H · Gizli halk** | `book.json` → `kinOpenings` |
| 5 | 48 normalize plaka | `07_ASSETS/plates/` |
| 6 | Haftalık sürüklenme raporları | `06_REPORTS/qa-drift.json` |

**Tahmini sayfa:** **138** (I: 64 · II: 74) · **Tahmini kelime:** ~35.600 (48 × 700 + 4 açılış × ~550)
**Yaratık sayısı:** **48**

### Araştırma görevleri

- [ ] Yazım sırasında ortaya çıkan boşluklar için araştırma dosyasına dön; **dosyada olmayan hiçbir detay yazılmaz**.
- [ ] C ailesinin dokuz üyesi için doğum ölümleri bağlamını derinleştir (karşılaştırma açılışı bunu taşıyacak).
- [ ] Kayıtlı vaka arayışı: mümkün olduğunda tarih ve yer verilen bir olay. "Ne yapar" bölümünün kalbi budur.

### Yazım görevleri

- [ ] 48 maddeyi yedi bölümlü şablonla yaz. **Tek seferde en fazla üç madde.**
- [ ] Ritim: haftada 12 madde · 4 hafta.
- [ ] Girdi her seferinde şu üçlüdür: o maddenin araştırma dosyası + `STYLE.md` + yedi bölümlü şablon. Daha fazlası üslup sürüklenmesi üretir.
- [ ] İlk beş madde bittiğinde **dur**: `qa_voice.py` + `qa_length.py` çalıştır, sesi kalibre et, sonra devam et.
- [ ] Sınıf I ve II açılışlarını yaz (her biri 2 sayfa).
- [ ] Dört karşılaştırma açılışını yaz (C, F, G, H).

### Editoryal görevler

- [ ] Her 5 maddede bir kalite kapısı turu.
- [ ] Haftalık `qa_drift.py`: en sık 50 kelimede yükselen eğim var mı?
- [ ] Yorum yalnızca 5. bölümde ("neden korkulur"). Başka yerde yorum varsa taşı.
- [ ] Akraba satırlarını (6. bölüm) `spec.json`'daki `crossRefs` ile karşılaştır — tutmayan varsa biri yanlıştır.

### Dizgi görevleri

- [ ] 48 plakayı üret, normalize et, ölç.
- [ ] Sınıf I ve II bölümlerinin **prova dizgisi**; gerçek sayfa sayısını ölç ve `BOOK_STATS.md`'deki tahminle karşılaştır.
- [ ] Sayfa sayısı hedeften %5'ten fazla saparsa kelime hedefini değil **sayfa bütçesini** düzelt ve kurucuya bildir (baskı maliyeti değişir).

### Doğrulama görevleri

- [ ] `qa_length.py --sections -v` — 48 maddenin tamamı bantta, hiçbir bölüm boş değil
- [ ] `qa_voice.py -v` — yasak kalıp **sıfır**
- [ ] `qa_echo.py -v` — maddeler arası 8+ kelimelik tekrar **sıfır**
- [ ] `qa_drift.py -v` — eğim %20'nin altında
- [ ] `qa_diacritics.py -v` — diakritik düşürülmemiş
- [ ] `plates.py --measure -v` — 48 plakanın tamamı bantta
- [ ] `validate_spec.py --gate phase3 -v`
- [ ] CI yeşil

### Tamamlanma ölçütü

48 maddenin tamamı `status: "written"`, bütün metin kapıları **0 başarısız**,
48 plaka tolerans bandında.

### Definition of Done

1. `qa_length` · `qa_voice` · `qa_echo` · `qa_drift` · `qa_diacritics` — hepsi 0 başarısız.
2. 48 plaka normalize edildi ve ölçüldü; tolerans dışı sıfır.
3. Sınıf I ve II açılışları + dört karşılaştırma açılışı yazıldı.
4. Prova dizgisi çalıştırıldı; ölçülen sayfa sayısı `BOOK_STATS.md`'de.
5. Haftalık sürüklenme raporları `06_REPORTS/` içinde ve eğim yükselmiyor.
6. CI yeşil, merge, **`v0.3.0`** etiketi.

### Claude notları

- **Üç madde kuralı gerçek bir kısıttır, öneri değil.** Dördüncü maddeye başlarken bağlamda üç maddenin metni durur ve dördüncü onların ritmine kayar. Bu ölçülmüş bir hatadır.
- Açılış cümlesi **tek cümledir** ve yaratığı **bir eylemle** tanımlar. "It stands at the water's edge and waits to be ridden." — tereddüt yok, "bazılarına göre" yok.
- "Ne yapar" bölümünde bir **olay** anlat, bir özellik listesi değil. Mümkünse kayıtlı bir vaka: *"A boy from Lough Neagh mounted one in 1808…"*
- Sıfat yığma. Ölçü ver: "kanat açıklığı bir tekne boyu" — "devasa" değil.
- Her maddeyi bitirdiğinde `qa_length.py` çalıştır. Bant dışıysa **hemen** düzelt; on madde sonra düzeltmek on maddenin ritmini bozar.
- C ailesi açılışını yazarken dikkat: dokuz gelenek anlatılacak ama bu bir liste değil, bir **tez** olacak. Ortak korku doğum ölümüdür; her gelenek ona farklı bir yüz vermiştir.

### Kurucu notları

- Bu fazın ilk beş maddesi bittiğinde **sizden okumanızı isteyeceğim**. Ses burada kurulur; sonradan düzeltmek 120 maddeyi yeniden okumak demektir.
- Prova dizgisinde ölçülen sayfa sayısı tahminden saparsa fiyat modeli değişir. Cilt 1'de büyük punto 540 sayfa modellenmiş, 578 çıkmıştı — model değil ölçüm geçerlidir.
- Haftada 12 madde iddialı bir ritimdir. 9'un altına düşerse takvim kayıyor demektir (Risk 4); bana söyleyin, kapsamı değil **takvimi** düzeltelim.

### Git etiketi

`v0.3.0` — *Bekçiler ve Yutucular yazıldı*

### Kilometre taşı

**Faz 3 · Çekirdek** — GitHub Milestone: `Faz 3 · Çekirdek`

---

## FAZ 4 — Genişleme · Şekil Değiştirenler ve Su Sakinleri

> **64 saat** · bağımlılık: Faz 3 · **Git etiketi `v0.4.0`** · Kilometre taşı **Faz 4 · Genişleme**

### Amaç

Sınıf III ve IV'ü yazmak ve plakalarını üretmek. Bu faz **su atı (A)** ve
**derinlerin yılanı (E)** ailelerini taşır — kitabın kapak adayı ve okur
mıknatısı buradan çıkar. Ayrıca **tilki kadın (B)** ailesi burada tamamlanır.

Bu fazın asıl riski sürüklenmedir: 48 madde geride kalmıştır ve ses kalıba
oturmaya başlar. `qa_drift.py` bu fazda haftalık değil, **her beş maddede**
çalıştırılır.

### Kurucu kararları — 7 Ağustos 2026 (D39 · D40 · D41)

Faz 3 raporunun kurucuya bıraktığı üç soru, Faz 4 başlamadan karara
bağlandı. Tam gerekçeler `CHANGELOG.md` D39–D41'de.

| Karar | Faz 4'e etkisi |
|---|---|
| **D39 · İllüstrasyon** — ham AI plaka üretimi kurucunun sorumluluğudur ve Faz 5'ten önce tamamlanacaktır | Aşağıdaki dizgi görevlerinden **plaka üretimine bağlı olanlar** bu fazda kapatılamaz ve Faz 4 bu yüzden bloklanmaz. Hat bekleme durumunda hazır tutulur. |
| **D40 · Üslup sürüklenmesi** — mevcut %21 Faz 4'te düzeltilmez | `qa_drift` her beş maddede koşar ve **ölçüm kayda geçer**; Faz 3 metni yeniden yazılmaz. Düzeltme Faz 5'in editoryal geçişine aittir. |
| **D41 · Kayıtlı vaka açığı** — ek araştırma turu yapılmaz | 4. bölümler yalnızca araştırma dosyasındaki malzemeden yazılır. Aşağıdaki "kayıtlı vaka ara" görevi bu çerçevede okunur: **aranır, bulunamazsa uydurulmaz.** |

### Çıktılar

| # | Çıktı | Yol |
|---|---|---|
| 1 | Sınıf III · THE SHAPE-CHANGERS — 20 madde | `01_SOURCE/book.json` |
| 2 | Sınıf IV · THE WATER-DWELLERS — 25 madde | `01_SOURCE/book.json` |
| 3 | İki sınıf açılışı | `book.json` → `classOpenings` |
| 4 | Karşılaştırma açılışları: **A · Su atı**, **B · Tilki kadın**, **E · Derinlerin yılanı** | `book.json` → `kinOpenings` |
| 5 | 45 normalize plaka (toplam 93) | `07_ASSETS/plates/` |
| 6 | **Kin-Images Chart** taslağı — okur mıknatısı | `03_APLUS/kin-images-chart.pdf` |

**Tahmini sayfa:** **126** (III: 60 · IV: 66) · **Tahmini kelime:** ~33.100 (45 × 700 + 3 açılış)
**Yaratık sayısı:** **45**

### Araştırma görevleri

- [ ] A ailesinin dört üyesi (Each-uisce · Nykur · Näkki · Tikbalang) için ayrışma noktalarını kaynaktan teyit et: İrlanda'da yiyici, İzlanda'da boğan, Filipinler'de yolu şaşırtan.
- [ ] E ailesinin sınırını kesinleştir (Faz 2'nin kararına göre 9 veya 15 üye).
- [ ] Kappa, Rusalka, Iara gibi "boğulma folkloru" maddelerinde kayıtlı vaka ara.

### Yazım görevleri

- [ ] 45 maddeyi yaz. **Tek seferde en fazla üç madde.**
- [ ] Ritim: haftada 12 madde · ~4 hafta.
- [ ] Sınıf III ve IV açılışlarını yaz.
- [ ] A, B, E karşılaştırma açılışlarını yaz.
- [ ] A ailesi açılışı **kitabın vitrinidir**: A+ içerikte, reklamda ve okur mıknatısında kullanılacak. Buna fazladan bir editoryal geçiş ayır.

### Editoryal görevler

- [ ] **Her 5 maddede** `qa_drift.py` (Faz 3'te haftalıktı — sürüklenme riski burada artar).
- [ ] Faz 3'ün 48 maddesiyle bu fazın maddeleri arasında `qa_echo.py` çalıştır: 93 madde arası tekrar.
- [ ] Çapraz referansları güncelle: yeni yazılan maddeler Faz 3'ün maddelerine bağlanacak.
- [ ] Faz 3'ten kalan editoryal itirazları kapat.

### Dizgi görevleri

- [ ] 45 plakayı üret, normalize et, ölç.
- [ ] **A ailesinin dört plakasını yan yana** dizip karşılaştır — aynı ölçek, aynı bakış yönü, aynı çizgi ağırlığı mı?
- [ ] Kin-Images Chart'ı üret (okur mıknatısı + A+ modülü m3).
- [ ] 93 maddelik ara prova dizgisi; sayfa bütçesini kontrol et.

### Doğrulama görevleri

- [ ] Bütün metin kapıları — **0 başarısız** (93 madde üzerinde)
- [ ] `plates.py --measure -v` — 93 plaka bantta
- [ ] `plates.py` dağılım raporu: pilot setle üretim setinin ölçülen dağılımları **örtüşüyor mu**
- [ ] `convert_plates.py --check` — Kindle bütçesi 120 plakaya ekstrapole edildiğinde ≤6 MB
- [ ] CI yeşil

### Tamamlanma ölçütü

93 madde `status: "written"`, bütün kapılar 0 başarısız, 93 plaka bantta,
pilot ile üretim dağılımları örtüşüyor.

### Definition of Done

1. Bütün metin kapıları 93 madde üzerinde 0 başarısız.
2. 93 plaka ölçüldü; tolerans dışı sıfır; dağılım pilot setle örtüşüyor.
3. A, B, E karşılaştırma açılışları yazıldı; A ailesi açılışı ekstra geçişten geçti.
4. Kin-Images Chart üretildi.
5. Kindle dosya boyutu projeksiyonu bütçe içinde.
6. CI yeşil, merge, **`v0.4.0`** etiketi.

### Claude notları

- **Sürüklenme bu fazda başlar.** 48 madde geride; bağlamda o ritim var. Her beş maddede `qa_drift.py` çalıştır ve eğim %20'yi geçerse dur, `STYLE.md`'yi yeniden oku, sonraki maddeyi sıfırdan kur.
- `qa_echo.py`'yi **bütün 93 madde üzerinde** çalıştır, yalnızca yeni 45'te değil. Tekrar, uzak maddeler arasında oluşur.
- Su ailesi maddelerinde tek bir cümle kalıbına düşme riski yüksek: hepsi kıyıda bekler, hepsi çeker, hepsi boğar. **Ayrışmayı yaz**, ortaklığı değil — ortaklık zaten karşılaştırma açılışında anlatılıyor.
- A ailesi açılışı reklam ve A+ içeriğe gidecek. Onu bir bölüm girişi gibi değil, **kitabın tezinin özeti** gibi yaz.

### Kurucu notları

- A ailesi açılışı ve Kin-Images Chart, kitabın pazarlamasının çekirdeğidir. Bu fazın sonunda ikisini de gözden geçirin.
- 93 plaka yan yana konduğunda "tek elden" görünüyor mu? Bu, göz kontrolü yapmanız gereken ikinci ve son andır (birincisi pilot setti).
- Ara prova dizgisinde sayfa sayısı 404'ün çok üstüne çıkıyorsa şimdi müdahale edilir; Faz 6'da müdahale etmek bütün metni yeniden akıtmak demektir.

### Git etiketi

`v0.4.0` — *Şekil Değiştirenler ve Su Sakinleri yazıldı*

### Kilometre taşı

**Faz 4 · Genişleme** — GitHub Milestone: `Faz 4 · Genişleme`

---

## FAZ 5 — Tamamlama, İllüstrasyon ve Editoryal İnceleme

> **99 saat** · bağımlılık: Faz 4 · **Git etiketi `v0.5.0`** · Kilometre taşı **Faz 5 · Tamamlama**

### Amaç

Kalan 27 maddeyi, bütün ön/arka maddeyi ve son 27 plakayı bitirmek; ardından
kitabın tamamını **üç editoryal geçişten** geçirmek. Bu fazın sonunda
manuscript **dizgiye hazırdır** — sonrasında tek bir cümle değişmez.

Üç geçiş sırayla: düşman olgu denetimi (30 sa) → satır editörlüğü (20 sa) →
ana dil geçişi (10 sa, dış kaynak).

### ⚠ Faz 4'ten devralınan iki zorunluluk (D40 · D41)

Bu iki madde Faz 4'te **bilerek ertelendi** ve buraya bırakıldı. Faz 5
onları kapatmadan tamamlanmış sayılmaz.

**① Tam editoryal üslup uyumlama geçişi — D40.**
Faz 3'ün 45 maddesi ölçüldüğünde `qa_drift` %21 sürüklenme raporladı ve
Faz 4 boyunca ölçüm sürdü. Kurucu kararı: **Faz 4 bu sürüklenmeyi
düzeltmez, izler.** Düzeltmenin yeri burasıdır ve **Geçiş 2'nin (satır
editörlüğü) ayrılmaz parçasıdır.** Gerekçe: sürüklenme bir *madde*
kusuru değil bir *seri* kusurudur — 45 maddeyi ayrı, 88'i ayrı düzeltmek
iki farklı üslup üretir. Kitabın tamamı elde olduğunda tek geçişte ele
alınır.

Uyumlama geçişi şunları kapsar:

- [ ] `qa_drift.py` çıktısındaki **yükselen sözcük listesini** kaynak al: çözümleyici kayda ait dağarcık (*about · rather · nothing · person · people · creature · figure*) sınıf ilerledikçe kalınlaşıyor.
- [ ] 5. bölümlerin (*neden korkulur*) soyutluk seviyesini kitap boyunca eşitle — `STYLE.md` § 7 örnek 3: yorum **tez cümlesiyle değil sahneyle** taşınır.
- [ ] Erken maddelerle geç maddelerin cümle uzunluğu dağılımını karşılaştır; ikisi de 14–18 bandında olsa bile **eğim** kalmamalı.
- [ ] Geçiş sonunda `qa_drift.py` yeniden koşar ve **eğim düşmüş olmalıdır**. Ölçüm `06_REPORTS/qa-drift.json` ile karşılaştırmalı raporlanır.
- [ ] Her düzeltme diğerleri gibi `edits.json`'a girer; elle düzenleme yok.

**② Kayıtlı vaka açığı — D41 · gelecek baskı notu.**
Araştırma dosyalarının `incident` alanı 112 maddenin 109'unda *"Faz 3'te
kaynaktan doğrudan okunacak"* diyor. Kurucu kararı: **ek tarihsel
araştırma turu yapılmaz**; 4. bölümler dosyadaki `behaviour`, `variants`,
`counter` ve kanonik olaydan yazılır. Bu, Faz 3'te ve Faz 4'te böyle
yapıldı ve Faz 5'te de böyle yapılacaktır.

> **Bu konu kapatılmıştır, gizlenmemiştir.** Yeni *doğrulanmış* kaynaklar
> ortaya çıkarsa — arşiv dijitalleştirmesi, yeni bir bilimsel derleme,
> erişilebilir hâle gelen bir saha kaydı — konu **gelecek bir baskıda**
> yeniden açılabilir. O zamana kadar geçerli kural değişmez:
> **uydurma yok. Kayıt yoksa cümle de yok.**
> Sonsöz bu tercihi savunmacı olmayan bir dille yazar (aynı yerde
> Aborjin geleneklerinin dışarıda bırakılması da anlatılıyor).

### Çıktılar

| # | Çıktı | Yol |
|---|---|---|
| 1 | Sınıf V · SKY AND STORM — 17 madde | `01_SOURCE/book.json` |
| 2 | Sınıf VI · THE RESTLESS DEAD — 10 madde | `01_SOURCE/book.json` |
| 3 | Karşılaştırma açılışı: **D · Fırtına kuşu** | `book.json` → `kinOpenings` |
| 4 | Giriş (8 s) · "Bu kitap nasıl okunur" (6 s) · Sonsöz (4 s) | `book.json` → `frontMatter` / `backMatter` |
| 5 | Arka madde: yazar hakkında · seri · yorum çağrısı · QR · kolofon | `book.json` → `backMatter` |
| 6 | Son 27 plaka (toplam **120**) | `07_ASSETS/plates/` |
| 7 | Düşman olgu denetimi itiraz listesi | `06_REPORTS/adversarial-review.json` |
| 8 | Bütün düzeltmeler programatik kayıtta | `01_SOURCE/edits.json` |
| 9 | `book-edited.json` — dizgiye giren metin | `01_SOURCE/book-edited.json` |

**Tahmini sayfa:** **140** (V: 40 · VI: 28 · ön madde 14 · giriş 8 · nasıl okunur 6 · sonsöz 4 · dizinler 22 · kaynaklar 10 · arka madde 8)
**Tahmini kelime:** ~24.900 (27 × 700 + ~6.000 matter)
**Yaratık sayısı:** **27**

### Araştırma görevleri

- [ ] D ailesinin sekiz üyesi için ayrışma noktalarını teyit et (Mezopotamya'da hırsız, İran'da bilge, Kuzey Amerika'da savaşçı).
- [ ] Sonsöz için: neyin dışarıda bırakıldığı ve **nedeni**. Aborjin gelenekleri kararı burada açıkça yazılır — bir eksik olarak değil, bir tercih olarak.
- [ ] Kaynaklar bölümü için 120 maddenin künyelerini gelenek gruplarına göre derle.

### Yazım görevleri

- [ ] 27 maddeyi yaz. **Tek seferde en fazla üç madde.**
- [ ] Sınıf V ve VI açılışları.
- [ ] D karşılaştırma açılışı.
- [ ] **Giriş — "Aynı korkunun kırk yüzü"** (8 sayfa): editoryal tez, kapsam, ne *değil*. Kitabın en çok okunan sayfaları burasıdır.
- [ ] **"Bu kitap nasıl okunur"** (6 sayfa): altı sınıfın açıklaması, motif kodları ne işe yarar, akraba imge sistemi.
- [ ] **Sonsöz** (4 sayfa): neden bu tasnif, neyin dışarıda bırakıldığı.
- [ ] Arka madde: yazar hakkında, Codex serisindeki diğer ciltler, yorum çağrısı, QR, kolofon.

### Editoryal görevler

- [ ] **Geçiş 1 · Düşman olgu denetimi (30 sa).** Ayrı bir oturum, **yalnızca bitmiş metni görerek** (araştırma notları verilmeden), her olgusal iddiayı çürütmeye çalışır. Çıktı: itiraz listesi.
- [ ] **Geçiş 2 · Satır editörlüğü (20 sa).** Kesme ve sıkıştırma. Hiçbir madde %8'den fazla uzamaz. **Üslup uyumlama geçişi buranın parçasıdır — D40, yukarıdaki ① maddesi.**
- [ ] **Geçiş 3 · Ana dil geçişi (10 sa, dış kaynak).** Ana dili İngilizce bir satır editörü — ses doğallığı. **Dışarıya verilecek ilk iştir.**
- [ ] Her düzeltme `edits.json`'a kaydedilir: `id`, öncesi, sonrası, kategori, gerekçe. **Elle düzenleme yapılmaz.**
- [ ] Tırnak dengesi 1:1; bölüm numarası sızıntısı sıfır.

### Dizgi görevleri

- [ ] Son 27 plakayı üret, normalize et, ölç.
- [ ] **120 plakanın tamamının tutarlılık raporu.**
- [ ] `make_index.py` ile dört dizini üret (sayfa numaraları henüz `—`).
- [ ] Tam kitap prova dizgisi; gerçek sayfa sayısını ölç.
- [ ] Sayfa sayısı 404'ten saparsa fiyat ve telif yeniden hesaplanır.

### Doğrulama görevleri

- [ ] Bütün metin kapıları **120 madde + matter** üzerinde — 0 başarısız
- [ ] `plates.py --measure -v` — 120 plaka, tolerans dışı sıfır
- [ ] `validate_spec.py --gate phase3 -v` — 120 madde `edited` veya `final`
- [ ] `edits.json` kayıtlı mı; elle düzenleme var mı (olmamalı)
- [ ] `make_index.py --gate phase2` — dört dizin üretiliyor
- [ ] CI yeşil

### Tamamlanma ölçütü

120 madde + bütün ön/arka madde yazıldı, üç editoryal geçişten geçti,
120 plaka tolerans bandında, `book-edited.json` üretildi.

### Definition of Done

1. `book-edited.json` mevcut ve bütün kapılar onun üzerinde 0 başarısız.
2. 120 plaka ölçüldü; tolerans dışı sıfır.
3. Üç editoryal geçiş tamamlandı; itiraz listesindeki her madde kapatıldı.
4. Her düzeltme `edits.json`'da; elle düzenleme yok.
4b. **Üslup uyumlama geçişi yapıldı (D40); `qa_drift` eğimi geçiş öncesine göre düşmüş ve ölçüm raporlanmış.**
5. Tam prova dizgisi çalıştırıldı; ölçülen sayfa sayısı `BOOK_STATS.md`'de.
6. Ölçülen sayfa sayısıyla fiyat ve telif yeniden doğrulandı.
7. CI yeşil, merge, **`v0.5.0`** etiketi.

### Claude notları

- **Düşman denetimini gerçekten düşman yap.** Araştırma dosyalarını o oturuma verme. Amaç metni savunmak değil, çürütmektir. Çürütülemeyen iddia kalır; çürütülen iddia ya kaynağa geri döner ya da silinir.
- Düzeltmeleri **`edits.py` üzerinden** uygula. Elle düzenleme, bir sonraki derlemede sessizce kaybolur ve neyin neden değiştiğini kimse bilemez.
- Giriş bölümü kitabın en çok okunan sayfasıdır (Amazon "Look Inside" oradan başlar). Ona bir madde gibi değil, **satış metni + editoryal tez** olarak yaklaş.
- Sonsöz'de Aborjin kararını **savunmacı olmayan** bir dille yaz. Bu bir özür değil, bir standart beyanıdır.
- Ana dil geçişi dışarıya verilecek. Editöre gönderilecek paketi hazırla: `book-edited.json` → okunabilir DOCX + `STYLE.md` + yasak kalıp listesi.

### Kurucu notları

- **Ana dil editörünü bu fazdan önce bulun.** 10 saatlik bir iş ama doğru kişiyi bulmak haftalar alabilir. Faz 4 biterken aramaya başlayın.
- Bu fazın sonunda manuscript **kilitlenir**. Faz 6'da metin değişmez — değişirse sayfa sayısı, dizin numaraları, sırt genişliği ve kapak geometrisi birlikte değişir.
- Ölçülen sayfa sayısı 404'ün üstüne çıkarsa iki seçenek var: kesmek veya fiyatı yükseltmek. Kesmek daha ucuzdur.

### Git etiketi

`v0.5.0` — *Manuscript tamamlandı ve editoryal incelemeden geçti*

### Kilometre taşı

**Faz 5 · Tamamlama** — GitHub Milestone: `Faz 5 · Tamamlama`

---

## FAZ 6 — Üretim, KDP ve Lansman

> **66 saat** · bağımlılık: Faz 5 · **Git etiketi `v1.0.0`** · Kilometre taşı **Faz 6 · Üretim**

### Amaç

Kilitlenmiş manuscript'i **yayınlanabilir dosyalara** çevirmek, KDP'ye
yüklemek ve lansmanı yürütmek. Bu fazda metin değişmez; yalnızca üretim
mühendisliği yapılır.

Bu faz, KDP kılavuzunun (`BESTIARIUM_KDP_PUBLISHING_GUIDE.md`) adım adım
uygulandığı fazdır.

### Çıktılar

| # | Çıktı | Yol |
|---|---|---|
| 1 | Ciltsiz iç blok PDF (6×9, ~404 s, gömülü fontlar) | `04_PRINT/PAPERBACK/` |
| 2 | Ciltli iç blok + ciltli kapak | `04_PRINT/HARDCOVER/` · `03_COVER/HARDCOVER/exports/` |
| 3 | Büyük punto iç blok + kapak | `04_PRINT/LARGEPRINT/` · `03_COVER/LARGEPRINT/exports/` |
| 4 | Ciltsiz kapak PDF (krem + beyaz) | `03_COVER/PAPERBACK/exports/` |
| 5 | Kindle EPUB — reflowable, ≤7 MB | `05_KINDLE/` |
| 6 | DOCX yedeği | `02_MANUSCRIPT/` |
| 7 | Dört dizin, **gerçek sayfa numaralarıyla** | `01_SOURCE/indexes.json` |
| 8 | A+ İçerik — 5 modül | `03_APLUS/exports/` |
| 9 | Metadata: 3+3 kategori, 7 anahtar kelime | `00_CONTEXT/BRIEF.md` |
| 10 | SEO varlıkları ve ürün açıklaması | `00_CONTEXT/BRIEF.md` |
| 11 | Üretim ve doğrulama raporları | `06_REPORTS/<SÜRÜM>/` |

**Tahmini sayfa:** 404 dizilir · **Tahmini kelime:** — (yeni metin yok)
**Yaratık sayısı:** — (yeni madde yok)

### Araştırma görevleri

- [ ] Rakip raf gözlemi tazelenir (kategori, fiyat bandı, yorum sayısı) — reklam hedeflemesi için.
- [ ] ARC dağıtım kanalları doğrulanır (StoryOrigin, BookSirens güncel şartları).

### Yazım görevleri

- [ ] Ürün açıklaması (Amazon listing) yazılır.
- [ ] A+ modül metinleri yazılır (5 modül).
- [ ] Basın kiti metni ve ARC tanıtım mektubu.
- [ ] **Kitabın gövdesinde tek kelime değişmez.**

### Editoryal görevler

- [ ] Dizgi sonrası son okuma: dul/yetim satır, kırık tirelenme, sayfa sonu kopan madde.
- [ ] Dizin sayfa numaralarının gerçekten doğru olduğu **gözle** doğrulanır (rastgele 20 madde).
- [ ] A+ metinlerinde rakip ürün karşılaştırması **yok** (Amazon yasaklar).

### Dizgi görevleri

- [ ] `./08_BUILD/build_all.sh` — üç sürüm iç blok + kapak.
- [ ] `make_index.py --gate phase6 --pagemap 04_PRINT/PAPERBACK/pagemap.json`
- [ ] `make_docx_epub.py` — DOCX + reflowable EPUB.
- [ ] `convert_plates.py` — 120 plakanın Kindle sürümü; toplam ≤6 MB.
- [ ] Kapak sanat eseri ≥3922 px genişlikte üretilir. **Cilt 1'deki 112 PPI hatası tekrarlanmaz.**
- [ ] `validate_cover.py` — ciltsiz ve ciltli, her iki kâğıt için.
- [ ] 160 piksel testi: küçük resimde başlık hâlâ **kelime olarak** okunuyor mu?

### Doğrulama görevleri

- [ ] `pdffonts` — gömülü olmayan font **yok** (dört ayrı font görünmeli)
- [ ] İç marj sayfa sayısına göre doğru (404 sayfada 0,75 inç; KDP tablosu 301–500 için 0,625 asgari)
- [ ] `validate_interior.py` — 0 başarısız, üç sürüm
- [ ] `validate_cover.py` — 0 başarısız, üç sürüm × iki kâğıt
- [ ] `ebook_size.py` / `convert_plates.py --check` — EPUB ≤7 MB
- [ ] `validate_aplus.py` — 79 kontrol, 0 başarısız
- [ ] `validate_structure.py --strict` — 0 başarısız, 0 uyarı
- [ ] KDP Print Previewer: sırt yazısı katlama çizgileri arasında ve ortalanmış — **ekran görüntüsü alınır**
- [ ] **Prova kopyası sipariş edilir ve elde tutulur** (Türkiye'ye 2–3 hafta)

### Tamamlanma ölçütü

Üç format KDP'de **yayında**, prova kopyası elde görüldü, indeksleme testi
geçti, Cilt 1 ve Cilt 2 aynı seri sayfasında görünüyor.

### Definition of Done

1. Ciltsiz · ciltli · büyük punto · Kindle — dördü de yayında.
2. Bütün doğrulama betikleri 0 başarısız.
3. Prova kopyası **elde tutuldu** ve kontrol listesi işaretlendi.
4. A+ İçerik yayında (5 modül).
5. Seri alanı üç formatta birebir aynı: `Codex` · Cilt 2.
6. AI beyanı işaretlendi: metin AI destekli · kapak AI üretimi · **illüstrasyonlar AI üretimi**.
7. ASIN kaydedildi; reklam kampanyaları açıldı.
8. `PROJECT_CONTEXT.md` yayın sonrası durumla güncellendi.
9. CI yeşil, merge, **`v1.0.0`** etiketi.

### Claude notları

- **Ciltsizi yükle, sonra "+ Create Hardcover" ve "+ Create Kindle eBook" ile diğerlerini ekle.** Sıfırdan yeni kitap oluşturma — metadata kopyalanmaz ve formatlar ürün sayfasında birbirine bağlanmaz.
- Kâğıt seçimi kapak dosyasını belirler: Cream → `..._cream_KDP.pdf`, White → `..._white_KDP.pdf`. Aradaki fark 2,1 mm'dir ve yanlış eşleşme sırt yazısını doğrudan katlama çizgisine kaydırır.
- Ciltli kapak geometrisi Cilt 1'de KDP'nin resmî Case Laminate şablonundan kalibre edildi (karton sırt payı 0,125" değil **0,1885"**). `kdp_calibration.json` devralındı; **yeniden keşfetme**.
- Dizin sayfa numaralarını `pagemap.json`'dan oku. Elle girme — Cilt 1'de sırt kaymasının kaynağı tam olarak buydu.
- EPUB'ı **reflowable** üret. Sabit düzen, Kindle Translate kapısını kalıcı olarak kapatır.

### Kurucu notları

- **Prova kopyasını fiyatlandırmadan önce sipariş edin.** Türkiye'ye kargo 2–3 hafta; plana ekleyin.
- Provada bakılacaklar: iç marjda metin cilde giriyor mu · sayfa numaraları doğru mu · sırt yazısı ortalanmış mı · **çizgi plakaların ince çizgileri baskıda kayboluyor mu**. Sonuncusu bu kitaba özgü ve en kritik olanıdır.
- W-8BEN ile ABD stopajı %30 yerine %10. Adres uyuşmazlığında %24 yedek stopaj eklenir — adresi dikkatli girin.
- Reklamı **Kindle'a** verin, ciltsizi organik keşfe bırakın: e-kitabın başabaş ACOS'u iki kat toleranslı.
- Cilt 1'in satışındaki değişimi ölçün. Seri etkisinin tek gerçek testi budur.

### Git etiketi

`v1.0.0` — *Codex Bestiarium yayında*

### Kilometre taşı

**Faz 6 · Üretim** — GitHub Milestone: `Faz 6 · Üretim`

---

## 6. Risk kaydı

Master yol haritası Bölüm 13'ten devralındı; her riske **bu hattın hangi
mekanizmayla** karşılık verdiği eklendi.

| # | Risk | Olasılık | Etki | Bu hattaki mekanizma | Erken uyarı |
|---|---|---|---|---|---|
| 1 | İllüstrasyon tutarsızlığı | Orta | **Yıkıcı** | Pilot set kilidi · `plates.py` ölçümü · otomatik ret · `make_prompts.py` tek üslup gövdesi | Pilot sette ölçüm dağılımının geniş çıkması |
| 2 | İki kaynak bulunamaması | **Yüksek** | Orta | `validate_spec.py --gate phase1` · ≥112 kapısı · yedek aday listesi | Faz 1'in 3. haftasında doğrulanmış madde < 70 |
| 3 | Kültürel duyarlılık hatası | Orta | **Yüksek** | `restrictionScreened` alanı kapıda zorunlu · `LIVING_TRADITIONS` listesi · Sonsöz'de açık beyan | Erken yorumlarda "yanlış" veya "izinsiz" ifadesi |
| 4 | Takvim kayması | **Yüksek** | Orta | Faz başına etiket · `ROADMAP_PROGRESS.md` otomatik ölçüm · kapsam kilidi | Faz 3–5'te haftada < 9 madde |
| 5 | Kindle dosya boyutu telifi yiyor | Orta | Orta | `convert_plates.py` bütçe kapısı · plaka başına ≤60 KB · 120'ye ekstrapolasyon | EPUB > 6 MB projeksiyonu |
| 6 | Rakip serinin küresel cildi rafı tutuyor | Orta | Orta | Ayrışma yapıda: işlevsel tasnif + karşılaştırma açılışları + motif kodları | Ana sorgularda ilk sayfaya girilememesi |
| 7 | AI illüstrasyon tepkisi | Orta | Orta | Künyede dürüst beyan · illüstrasyon notunda süreç · insan eliyle vektör temizliği | Folklor/illüstrasyon topluluklarında olumsuz yankı |
| 8 | Üslup sürüklenmesi | **Yüksek** | Orta | Tek seferde 3 madde · `qa_drift.py` · `qa_echo.py` · yasak kalıp listesi | En sık 50 kelimede yükselen eğim |
| 9 | **Herkese açık depoda proza** | Orta | **Yüksek** | `.gitignore` proza yollarını dışarıda tutar · [A1](#a1--depo-herkese-açık-manuscript-ne-olacak) kararı Faz 3 öncesi | Faz 3 başlarken karar verilmemiş olması |
| 10 | **Bayat belge** | Yüksek | Düşük | `update_docs.py --check` CI kapısı · elle yazılmayan istatistik | — (mekanizma sürekli çalışır) |

---

## 7. Yarın sabah ne yapılacak

Bu bölüm, bir sonraki oturumun planlama yapmadan doğrudan işe başlaması içindir.

```bash
cd /home/emre/Downloads/MY-DİGİTAL-BOOK/CODEX_BESTIARIUM

./08_BUILD/bootstrap.sh          # venv + font + kapı testi
./08_BUILD/qa_all.sh             # her şey yeşil mi?
```

Sonra, sırayla:

1. **Kurucu onayını al.** Faz 1 ve 2 planlandı; yazım Faz 3'te başlıyor. Onay gelmeden Faz 3'e geçilmez.
2. **[A1](#a1--depo-herkese-açık-manuscript-ne-olacak), [A2](#a2--kapsam-12040-mı-10035-mi), [A3](#a3--vektör-temizlik-dışarıya-verilecek-mi) sorularını yanıtla.**
3. **Faz 1'e başla.** Araştırmacı rolünde, gelenek gelenek. İlk hedef **en zor sekiz gelenek**: Melanesia, Ainu, Kartveli, Hayk, Sápmi, Nusantara, Ityop'ya, Mongol. Kolay olanlar (Hellenic, Norðr, Yamato) sona bırakılır.
4. **Paralelde pilot plaka setini başlat.** On plaka, altı sınıftan. Faz 1 biterken çizgi dili kilitlenmiş olmalı.

### Tek cümlelik başlangıç emri

> *"Melanezya, Ainu ve Kartveli geleneklerinden dokuz yaratık için iki bağımsız
> kaynak bul, Thompson motif kodlarını doğrula ve `01_SOURCE/research/<id>.md`
> dosyalarını yaz. Proza yazma."*

---

*Vâliçe Press · Codex Bestiarium · Uygulama Yol Haritası v1.0 · 7 Ağustos 2026*
