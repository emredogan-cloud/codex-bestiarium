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
- Faz 2 · Tasnif, veri modeli ve pilot plaka seti — **kurucu onayı bekliyor**

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

[Yayımlanmamış]: https://github.com/emredogan-cloud/codex-bestiarium/compare/v0.1.0-alpha...HEAD
[0.1.0-alpha]: https://github.com/emredogan-cloud/codex-bestiarium/releases/tag/v0.1.0-alpha
