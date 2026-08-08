# PROJECT CONTEXT — CODEX BESTIARIUM

> **Bu belge, projeyi aylar sonra devralacak kişi (veya ajan) içindir.**
> Hiçbir şeyi hatırladığınız varsayılmaz. Buradaki her sayı ya bir dosyadan
> ölçülmüştür ya da bir kod satırından türetilmiştir; ikisi de gösterilmiştir.
>
> Son güncelleme: **8 Ağustos 2026** — Faz 6 üretim tamam, YAYIN BLOKE
> Kök dizin: `/home/emre/Downloads/MY-DİGİTAL-BOOK/CODEX_BESTIARIUM`

---

## 1. Bir cümlede durum

**Faz 6: dosyalar üretildi, yayın bloke.** Kitabın basılabilir
dosyaları hazır ve doğrulandı — üç iç blok sürümü (ciltsiz 435, ciltli
435, büyük punto 599 sayfa), reflowable Kindle EPUB (4,73 MB), DOCX
yedeği ve gerçek sayfa numaralı dört dizin. `qa_all` 32/32.

**YAYIN BEŞ NOKTADA BLOKE ve beşi de kurucuya bağlı:** kapak sanat
eseri teslim edilmedi (`03_COVER/artwork/` boş), fiziksel prova
sipariş edilmedi, KDP Previewer ve KDP yüklemesi hesap gerektiriyor,
ASIN yok. Ayrıntı: [`06_REPORTS/FAZ_6_RAPORU.md`](../06_REPORTS/FAZ_6_RAPORU.md) § 9.

**`v1.0.0` ATILMADI. YOL HARİTASI KAPATILMADI.** Yayın blokajı dururken
kapanış ilan edilmez.

---

### Faz 5 — tamamlandı

**Kitabın METNİ BİTTİ.** 112/112 madde, 6/6 sınıf
açılışı, 8/8 karşılaştırma açılışı, 7/7 ön ve arka madde bölümü.
Toplam **88.960 kelime**. 112 ham plaka doğrulandı, eşlendi ve
normalize edildi. Sayfa bütçesi kitabın **tamamı** dizilerek yeniden
kuruldu ve **değişmedi: 436 sayfa**. `.gate` → `phase3`, etiket
`v0.5.0`. **Proza depoda değildir** (karar A1/D29).

> **Üslup sürüklenmesi %8,9 → %1,6.** D40 kapatıldı: Faz 4'ün adıyla
> devrettiği üç kalıp kümesi 46/28/25 maddeden 1/0/1'e indi. Ayrıntı:
> § 11c ve CHANGELOG v0.5.0.

> **Üç editoryal geçiş yapıldı.** Düşman olgu denetimi 13 gerçek kusur
> buldu — beş maddede prozanın gösterdiği künye kayıtta yoktu, iki
> kaynak atfı tam metin taramasıyla çürüdü. Hepsi düzeltildi ve
> **146 düzeltmenin tamamı defterde** (`edits.json`): id, öncesi,
> sonrası, kategori, gerekçe.

> **Ana dil editörü paketi hazır ve dışarıya verilmedi.** Kurucu emri
> gereği Faz 5 insan işini beklemedi: metin, brifing ve işaretli
> bölümler `editor_pack.py` ile üretiliyor.

> Güncel ölçüm: [`BOOK_STATS.md`](../BOOK_STATS.md) ·
> kapsam kararları: [`SCOPE_DECISIONS.md`](SCOPE_DECISIONS.md) ·
> kaynak ölçütü: [`SOURCING_STANDARD.md`](SOURCING_STANDARD.md) ·
> açılış planları: [`KIN_OPENINGS.md`](KIN_OPENINGS.md)

### Faz 5 · Definition of Done

| # | Ölçüt | Durum |
|---|---|---|
| 1 | 112/112 madde, bütün metin kapıları 0 başarısız | ✅ |
| 2 | Bütün açılışlar (6 sınıf + 8 karşılaştırma) | ✅ |
| 3 | Ön ve arka maddenin tamamı, sayfa slotu içinde | ✅ 20 sayfa içerik / 26 slot |
| 4 | 112 plaka doğrulandı, normalize edildi, bütçede | ✅ |
| 5 | Düşman olgu denetimi ve itiraz listesi | ✅ `factcheck.py` · 13 kusur · hepsi düzeltildi |
| 6 | Bütün düzeltmeler programatik kayıtta | ✅ `edits.json` · 146 kayıt |
| 7 | Üslup uyumlama (D40) | ✅ sürüklenme %1,6 |
| 8 | Sayfa bütçesi tam kitapla yeniden doğrulandı | ✅ 436, değişmedi |
| 9 | Ana dil editörü paketi | ✅ üretildi · ⏳ insan geçişi bekliyor |
| 10 | CI yeşil, merge, `v0.5.0` | ✅ |

### Faz 4 · Definition of Done

| # | Ölçüt | Durum |
|---|---|---|
| 1 | Bütün metin kapıları 88 madde üzerinde 0 başarısız | ✅ |
| 2 | 93 plaka ölçüldü; dağılım pilot setle örtüşüyor | ⛔ **ham AI çıktısı yok** — kurucudan gelir (karar D39); hat hazır ve kalibre |
| 3 | A, B, E karşılaştırma açılışları; A ailesi ekstra geçişten geçti | ✅ 3/3 |
| 4 | Kin-Images Chart üretildi | ✅ `make_kin_chart.py` · 8 aile · 2 sayfa · plaka çerçeveleri D39'u bekliyor |
| 5 | Kindle dosya boyutu projeksiyonu bütçe içinde | ✅ 3,74 MB / 6,0 MB (kalibrasyonla) |
| 6 | CI yeşil, merge, `v0.4.0` | ✅ |

> **2. madde hakkında.** Faz 2 ve Faz 3'ün aynı maddesiyle aynı sebep,
> ve artık bir karar: **D39**. Ham AI plaka üretimi kurucunun işidir ve
> Faz 5'ten önce tamamlanacaktır. Hat bekleme durumunda hazır tutuldu ve
> Faz 4'te bir kez daha sınandı: `convert_plates --calibrate` 112
> plakalık Kindle projeksiyonunu ölçtü, `make_kin_chart` plaka
> çerçevelerini doğru oranda çizdi. Plakalar geldiğinde aynı komutlar
> çerçeveleri doldurur; yerleşim ve bütçe değişmez.

### Faz 3 · Definition of Done

| # | Ölçüt | Durum |
|---|---|---|
| 1 | `qa_length` · `qa_voice` · `qa_echo` · `qa_drift` · `qa_diacritics` — 0 başarısız | ✅ (qa_drift 1 **uyarı**: %21 sürüklenme) |
| 2 | 48 plaka normalize edildi ve ölçüldü | ⛔ **ham AI çıktısı yok** — hattın dışındaki tek girdi, kurucudan gelir |
| 3 | Sınıf I ve II açılışları + dört karşılaştırma açılışı | ✅ 6/6 |
| 4 | Prova dizgisi çalıştırıldı; ölçülen sayfa sayısı `BOOK_STATS.md`'de | ✅ 45/45 madde, gerçek metinle |
| 5 | Sürüklenme raporları `06_REPORTS/` içinde; eğim yükselmiyor | ⚠ rapor var; eğim **%21 yükseliyor** (uyarı bandı) |
| 6 | CI yeşil, merge, `v0.3.0` | ✅ |

> **2. madde hakkında.** Faz 2'nin aynı maddesi de aynı sebeple açıktı.
> Plaka hattı kurulu, kalibre ve sınanmış durumda; eksik olan tek şey ham
> AI çıktısıdır (`BESTIARIUM_IMAGE_PROMPTS.html` → görsel üreteç →
> `07_ASSETS/plates_raw/`). Bu, üretim hattının **dışındaki tek girdidir**
> ve kurucudan gelir. Geldiği anda `plates.py --normalize --pilot` yeterlidir.
> Faz 3'ün metin işi bu girdiye bağlı değildi ve tamamlandı.

### Faz 2 · Definition of Done

| # | Ölçüt | Durum |
|---|---|---|
| 1 | Her madde tam bir sınıfta; hiçbiri 8–32 bandı dışında | ✅ 18·27·19·24·16·8 |
| 2 | Sınıf ve aile tutarsızlığı **çözüldü**, karar CHANGELOG'da | ✅ D21–D24 |
| 3 | Sekiz ailenin ayrışma cümlesi yazıldı ve onaylandı | ✅ |
| 4 | Her maddede 2–5 karşılıklı çapraz referans; kırık yok | ✅ 181 bağ · ort 3,23 |
| 5 | 112 telaffuz alanı dolu | ✅ |
| 6 | Pilot set onaylandı; ölçülen dağılım `STYLE_PLATES.md`'de | ⚠ **hat hazır, ham plaka bekleniyor** |
| 7 | `.gate` → `phase2` | ✅ |
| 8 | CI yeşil, merge, `v0.2.0` | ✅ |

> **6. madde hakkında.** Faz 2'nin plaka işi ikiye ayrılıyordu: *hattı kurup
> kalibre etmek* ve *on ham plakayı üretip ölçmek*. Birincisi tamamlandı ve
> ölçümleriyle `STYLE_PLATES.md` § 1b'de duruyor — cetvel sınandı, iki kusuru
> bulundu, düzeltildi, doğruluğu (%0,3) sayıyla kayda geçti. İkincisi **ham
> AI çıktısı** gerektirir: `BESTIARIUM_IMAGE_PROMPTS.html` → görsel üreteç →
> `07_ASSETS/plates_raw/`. Bu, hattın dışındaki tek girdidir ve kurucudan
> gelir. Geldiği anda `plates.py --normalize --pilot` yeterlidir.

### Faz 1 · Definition of Done

| # | Ölçüt | Durum |
|---|---|---|
| 1 | `validate_spec --gate phase1` 0 başarısız | ✅ |
| 2 | 112 araştırma dosyası, hepsi aynı yapıda | ✅ |
| 3 | `motifVerified:false` + `status!=draft` yok | ✅ |
| 4 | Yaşayan geleneklerde `restrictionScreened` | ✅ 112/112 |
| 5 | `BRIEF.md` yazıldı, kapsam **kilitlendi** | ✅ |
| 6 | `.gate` → `phase1` | ✅ |
| 7 | CHANGELOG · BOOK_STATS · ROADMAP_PROGRESS | ✅ |
| 8 | CI yeşil, merge, `v0.1.0` | ✅ |


---

## 1b. Üretim sistemi (ilk tur)

Üretim sistemi **kuruldu ve test edildi**: `spec.json`, on beş doğrulama
betiği, CI/CD hattı, prompt kütüphanesi ve altı fazlık uygulama yol haritası.
Faz 2 sonunda hat **on dokuz** betiğe çıktı ve üçü ölçümün kendisini sınıyor
(`selftest.py` · `plate_selftest.py` · `convert_plates --calibrate`).

---

## 2. Proje genel görünümü

| | |
|---|---|
| **Ürün** | *Codex Bestiarium: A World Bestiary* — Codex Serisi Cilt II |
| **Yazar / künye** | Emre Doğan · Vâliçe Press |
| **Dil** | Kitabın kendisi **İngilizce**. Bu belgeler ve raporlar Türkçe. |
| **Kapsam** | **112 yaratık · 40 gelenek** (Faz 1'de kilitlendi) · 6 sınıf · 8 akraba imge ailesi |
| **Hacim** | **436 sayfa** (Faz 4 provasında 88 maddeyle yeniden doğrulandı) · ~78.400 kelime · 6 × 9 inç |
| **İllüstrasyon** | 112 çizgi plaka, tek gravür dilinde |
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

## 3. Faz 2'de ne teslim edildi

| # | Teslim | Yol |
|---|---|---|
| 1 | Faz 2'nin editoryal katmanı — 181 bağ, 8 ayrışma cümlesi, 8 açılış planı | `01_SOURCE/kin_map.json` |
| 2 | Tasnif motoru — kin_map → spec + belge + grafik raporu | `08_BUILD/classify.py` |
| 3 | Sekiz karşılaştırma + altı sınıf açılışının içerik planı | `00_CONTEXT/KIN_OPENINGS.md` |
| 4 | Kapsam kararı sonrası tohum senkronu | `seed_import.py --sync` |
| 5 | **Plaka ölçümünün kendi testi** — bilinen geometriyle | `08_BUILD/tests/plate_selftest.py` |
| 6 | Kalibrasyon kurguları (iyi + altı kusurlu) | `08_BUILD/tests/plate_fixtures.py` |
| 7 | Format bütçelerinin plaka gelmeden ölçümü | `convert_plates.py --calibrate` |
| 8 | **Madde sayfası tasarımı ve prova dizgisi** | `08_BUILD/entry_page.py` |
| 9 | Şema kapılarının kusur kurguları (dört seviye) | `tests/make_fixtures.py` |
| 10 | CI: plaka kalibrasyonu · prova dizgisi · font indirme | `.github/workflows/` |

---

## 3b. İlk turda ne yapıldı (üretim sistemi)

Talimat açıktı: *"Your first responsibility is to build a production system…
Treat this book like a software product."* Yapılan tam olarak budur.

| # | Teslim | Yol |
|---|---|---|
| 1 | Bölüm 10'daki klasör ağacı | depo kökü |
| 2 | Fontlar ve devralınan 27 betik Mythologica'dan kopyalandı | `07_ASSETS/fonts/` · `08_BUILD/` |
| 3 | **120 tohum kaydı** master yol haritasından *türetildi* (Faz 1'de 112'ye kilitlendi) | `01_SOURCE/spec.json` |
| 4 | Kitap kayıt defteri — sınıflar, aileler, bantlar, yasak kalıplar | `08_BUILD/bestiarium.py` |
| 5 | Şema doğrulayıcı, dört kapı seviyesiyle | `08_BUILD/validate_spec.py` |
| 6 | Beş metin kalite kapısı | `08_BUILD/qa_*.py` |
| 7 | **Kapıların kendi testi** — kasıtlı kusurlu kurgu ile | `08_BUILD/tests/selftest.py` |
| 8 | Plaka normalizasyonu + tutarlılık ölçümü | `08_BUILD/plates.py` |
| 9 | Plaka format dönüştürücü (baskı · Kindle · A+ · web) | `08_BUILD/convert_plates.py` |
| 10 | Dört dizin üreticisi | `08_BUILD/make_index.py` |
| 11 | Plaka prompt kütüphanesi (bugün 112) | `BESTIARIUM_IMAGE_PROMPTS.html` |
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
│   ├── spec.json            112 kayıt — TEK DOĞRULUK KAYNAĞI
│   ├── kin_map.json         Faz 2 editoryal katmanı — ELLE yazılır
│   ├── scope_amendments.json kapsam kararları — tohumun üstüne biner
│   ├── plate_subjects.json  İngilizce görsel betimlemeler
│   ├── indexes.json         üretilmiş dört dizin
│   ├── research_data/       40 gelenek dosyası — araştırmanın kaynağı
│   ├── research/<id>.md     112 araştırma dosyası (üretilir)
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
│   ├── plates/              normalize edilmiş 112 plaka
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
  "pronunciation": "AKH-ish-keh",  // Faz 1'de toplandı
  "tradition": "eriu",
  "class": "IV",                   // I–VI
  "motif": ["B184.1.3"],           // Thompson kodları
  "motifVerified": false,          // Faz 1 kapısı
  "kinFamily": "A",                // A–H veya null
  "altNames": [],
  "region": "",                    // Faz 1
  "attested": "",                  // Faz 1
  "sources": [],                   // Faz 1: ≥2 BAĞIMSIZ kaynak
  "crossRefs": ["nakki", "nykur"], // Faz 2: 2–5, KARŞILIKLI — classify.py üretir
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
| Yaratık kaydı | **112** |
| Gelenek | **40** (19'u Cilt 1'den devralındı) |
| Benzersiz Thompson kodu | 69 |
| Aileye bağlı madde | 59/112 (48 manşet · 11 uzun kuyruk) |
| Çapraz referans bağı | 181 karşılıklı · madde başına ort. 3,23 |
| Kaynak riski yüksek gelenek | 8 |

---

## 6. ✅ Devralınan iki tutarsızlık — Faz 2'de kapatıldı

İkisi de **hata değildi**, master yol haritasının iki bölümü arasındaki gerçek
farklardı. İkisi de doğrudan sayfa bütçesine, dolayısıyla baskı maliyetine
bağlıydı. Kararlar `CHANGELOG.md` D21–D24'te gerekçeleriyle duruyor.

### ① Sınıf dağılımı → hedef gerçeğe getirildi

Bölüm 03.1'in hedefleri **120 maddelik** bir kitap için hesaplanmıştı; kapsam
Faz 1'de 112'ye kilitlendi ve o kitap artık yok. K1 tasnifin **işleve göre**
olduğunu söyler — sayısal bir hedef işlevi ezemez. Bu yüzden hedef güncellendi,
madde zorlanmadı.

| Sınıf | Bölüm 03.1 (120 için) | **Yürürlükteki** | Sayfa |
|---|---:|---:|---:|
| I · Bekçiler | 22 | **18** | 54 |
| II · Yutucular | 28 | **27** | 81 |
| III · Şekil Değiştirenler | 22 | **19** | 57 |
| IV · Su Sakinleri | 24 | **24** | 72 |
| V · Gök ve Fırtına | 14 | **16** | 48 |
| VI · Huzursuz Ölüler | 10 | **8** | 24 |
| | 120 | **112** | **336** |

Eski hedefler `classes[].roadmapTargetEntries` olarak tarihsel kayıtta duruyor.

**Tek sınıf düzeltmesi: Boitatá V → I** (D22). İki bağımsız kanıt: araştırma
dosyasının kendi yazım notu (*"Curupira ile aynı işlevin başka biçimi"* —
Curupira sınıf I'dir) ve doğrulanmış kod `B19.4.2`'nin sınıf I'in çıpa
aralığında (B11–B19) olması. Sapma her iki sınıfta da hedefe **yaklaştı**.

### ② Akraba aile üyelikleri → iki katmana ayrıldı

55 ile 61 arasındaki fark bir çelişki değil, bir **kategori hatasıydı**: tek
sütunda iki ayrı şey toplanmıştı.

| Katman | Ne | Sayı | Nerede görünür |
|---|---|---:|---|
| **üye** | imgeyi taşıyan her madde | 59 | akraba imge tablosu · kendi maddesi · Kin-Images Chart |
| **manşet** | açılışın karşılaştırdığı kadro (≤9) | 48 | iki sayfalık karşılaştırma açılışı |
| uzun kuyruk | üye ama manşet değil | 11 | açılışın kapanış paragrafında anılır |

İkisi de tam üyedir; fark yalnızca **iki sayfaya ne sığdığıdır**. Böylece ne
araştırılmış malzeme atıldı ne de açılış taşırıldı.

| Aile | Üye | Manşet | Uzun kuyruk |
|---|---:|---:|---:|
| A · Su atı | 4 | 4 | — |
| B · Tilki kadın | 2 | 2 | — |
| C · Gece cadısı | 14 | 9 | 5 |
| D · Fırtına kuşu | 9 | 9 | — |
| E · Derinlerin yılanı | 15 | 9 | 6 |
| F · Eşik bekçisi | 8 | 8 | — |
| G · Yaban adamı | 4 | 4 | — |
| H · Gizli halk | 3 | 3 | — |

Ayrıca **üç aile motif kodu düzeltildi** (D24): B `D113.1`→`D113.3`,
C `G264`→`G262`, G `F460`→`F567`. Üçü de Faz 1'in madde düzeyinde bulduğu
sistematik hatanın aile düzeyindeki karşılığıydı.

---

## 6b. Faz 2'nin üç bulgusu

Bu üçü **aranmıyordu**; ölçüm disiplini onları buldu.

### ① Plaka cetveli eğriydi ve doğru plakaları reddedecekti

Kalınlık ölçümü, tarama yönüne *dik olmayan* kesitlerden okunuyordu. 45°
taramada koşu uzunluğu gerçek kalınlığın **√2 katıdır**; şartnamenin
geometrisine **birebir uyan** bir plaka bu yüzden reddediliyordu. Hat, doğru
çizilmiş 112 plakanın tamamını geri çevirecekti.

Düzeltildikten sonra hata **%41 → %0,3**. Kanıt: `tests/plate_selftest.py`,
geometrisi bilinen kurgularla. Ayrıntı: `STYLE_PLATES.md` § 1b.

### ② Plaka şartnamesi kendi kendisiyle çelişiyordu

Hem "22–28 çizgi/cm" hem "çizgi kalınlığı 1,4 pt" deniyordu. 25 çizgi/cm'de
periyot **4,72 px**, 1,4 pt ise **5,83 px** — bir periyoda kendinden geniş bir
darbe sığmaz. İkisi ayrıldı: tarama darbesi periyoda **oranla** ölçülüyor
(bandı sıklıktan türüyor, çelişemez), dış hat ayrı raporlanıyor ve **kapı
değil** — çünkü kalibrasyonda 2,9 / 4,2 / 5,83 px konturları ayırt edemedi.

### ③ Sayfa bütçesi 380 değil 436

Prova dizgisi (`entry_page.py`) ölçtü: madde **içeriği** 2,558 sayfa (yol
haritasının 2,53 modelini doğrular), madde **maliyeti** 3 sayfa. Aradaki
0,442 sayfa plaka kuralının bedelidir — plaka üst yarıya oturduğu için her
madde sayfa başından başlar. 112 maddede 50 sayfa.

Telif üç sürümde de pozitif kaldı (ciltsiz 9,43 $ → 8,76 $) ve K3 (700
kelime) dokunulmadı.

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

# kurulum (venv + font; font yoksa Google Fonts'tan iner)
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
python3 08_BUILD/classify.py --check
python3 08_BUILD/tests/plate_selftest.py -v     # cetvel doğru mu ölçüyor
python3 08_BUILD/convert_plates.py --calibrate  # format bütçeleri
python3 08_BUILD/entry_page.py --proof -v       # madde sayfası prova dizgisi
python3 08_BUILD/plates.py --pilot -v
python3 08_BUILD/make_index.py --gate phase2
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
| 1 | Sınıf dağılımı tutarsızlığı (§ 6①) | ✅ **Faz 2'de çözüldü** — D21, D22 |
| 2 | Akraba aile üyelik tutarsızlığı (§ 6②) | ✅ **Faz 2'de çözüldü** — D23, D24 |
| 3 | Kapsam 120/40 mı 100/35 mi | ✅ **Faz 1'de kilitlendi** — 112/40 |
| 4 | `STYLE.md` ses kalibrasyon örnekleri | ✅ **Faz 1'de** Cilt 1'den kopyalandı |
| 5 | **Ham plaka seti** | ⚠ hat hazır ve kalibre; **kurucu Faz 5 öncesi üretecek** — karar D39 |
| 6 | **Herkese açık depoda proza** | ⛔ Faz 3 öncesi karar — [yol haritası § A1](../CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md#a1--depo-herkese-açık-manuscript-ne-olacak) |
| 7 | Vektör temizlik dışarıya verilecek mi | pilot süresi ölçülünce — [§ A3](../CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md#a3--vektör-temizlik-dışarıya-verilecek-mi) |
| 8 | Dış hat kalınlığı tahmincisi kalibre edilemedi | gerçek plakalarda yeniden değerlendirilecek (§ 6b②) |
| 9 | Kindle Translate uygunluğu belirsiz | 112 plaka kapıyı kapatabilir; **finansal modele dahil edilmedi** |
| 10 | Kamu malı yanlış sınıflandırma riski | Cilt 1'den devralındı; künyede özgünlük beyanı + özgün Giriş/Sonsöz savunma olarak yazılacak |

---

## 11. Sıradaki adım

**Kurucu onayı bekleniyor.** Faz 1, 2, 3 ve 4 tamamlandı. **Faz 5 onay
gelmeden başlamaz.**

Faz 5 sınıf V (Gök ve Fırtına, 16) ve sınıf VI (Huzursuz Ölüler, 8)
maddelerini yazar: **24 madde**. Ayrıca **D · Fırtına kuşu** karşılaştırma
açılışı, bütün ön/arka madde ve **üç editoryal geçiş**. Yol haritası Faz 5
için 17+10=27 diyor; bu sayı 120 maddelik aşılmış kapsamdan gelir (D21).

Onay geldiğinde ilk emir:

```
"Sınıf V'in ilk üç maddesini yaz. Girdi her madde için üçlüdür —
 araştırma dosyası + STYLE.md + yedi bölümlü şablon.
 Tek seferde en fazla üç madde."
```

> **`.gate` Faz 4'te de `phase3` kaldı ve Faz 5'te de kalır.** Kapı
> seviyeleri `draft → phase1 → phase2 → phase3` ile biter; `phase3` bir
> *faz adı* değil, **yazım kapısının** adıdır ve yazılan her maddeyi
> denetler. Yazım fazları yeni seviye açmaz, açılmış olanı taşır.

### Faz 5'e devredilen dört şey

1. **Üslup uyumlama geçişi (D40)** — yol haritası Faz 5 § ①'de kilitli
   ve DoD 4b'ye bağlı. Faz 4 sürüklenmeyi %21'den %8,9'a indirdi ama
   *düzeltmeden*: düşüş yeni maddelerden geldi, eski metin açılmadı.
   Geçiş üç somut hedefle başlar (§ 11c).
2. **Ham plaka seti (D39)** — hattın dışındaki tek girdi. 88 maddenin
   plakası da buna bağlı. Kurucu Faz 5'ten önce üretecek.
3. **Kayıtlı vaka açığı (D41)** — kapalı; gelecek baskı notu yol
   haritası Faz 5 § ②'de.
4. **Tikbalang'ın madde içi tekrarı** — açılış cümlesi ile 3. bölüm aynı
   öbeği taşıyor (*"a horse's head on a man's body"*). `qa_echo` madde
   İÇİ öbek tekrarını bu biçimde aramıyor; D40 gereği metin açılmadı.

---

## 11c. Faz 4'ün bulgusu: sürüklenme nereden geliyor

Sürüklenme Faz 4'te **düzeltilmedi, on beş kez ölçüldü** (D40) ve her
ölçüm bir commit iletisine geçti:

```
%21,0 → 15,0 → 13,2 → 8,7 → 9,8 → 9,1 → 10,5 → 10,4
      → 12,0 → 14,1 → 16,5 → 13,4 → 11,9 → 10,3 → 10,5 → 8,9
```

Faz 3 kapanışında **%21,0**, Faz 4 kapanışında **%8,9**. Cümle uzunluğu
ritmi eğimi %+8,9'dan **%+2,7**'ye indi.

**Düşüş bir düzeltmeden gelmedi.** Sınıf III ve IV maddeleri somut bir
mekanizma anlatıyor — takvim, ters toynak, başındaki çanak, kuyruktaki
el, ekimde yükselen ışık — ve somut mekanizma çözümleyici dağarcığı
seyreltiyor. Ortadaki tırmanış (%8,7 → %16,5) da aynı şeyin tersidir.

### Faz 5 uyumlama geçişinin üç somut hedefi

`qa_echo` Faz 4'te **on dokuz** kalıplaşma yakaladı ve üç kümeye ayrıldılar.
Kapı yalnızca **birebir 8 kelimelik** çakışmayı görür; kalanı görmez ve
geçişin işi tam olarak kalanıdır.

| # | Küme | Örnek |
|---|---|---|
| ① | **Yazarın çözümleyici kalıpları** | *"What the tradition supplies is not…"* — metinde sekiz yerde. Ayrıca *"almost every creature in this book is a…"*, *"that is the whole of the account"*. Sürüklenmenin yükselen sözcük listesi aynı yeri gösteriyor: **kitabın kendine göndermesi**. |
| ② | **Yaşayan gelenek kapısının boilerplate'e dönmesi** | Üç kez yakalandı (Tupilaq ↔ Repun Kamuy, Masalai ↔ Taniwha, Inkanyamba ↔ Amaru). Kısıt cümlesi kalıplaşırsa okur onu atlamayı öğrenir. **Etik kapı her maddede yeniden kurulmalı.** |
| ③ | **Karşılıklı çapraz referansın aynı cümleyle kurulması** | Nahual ↔ Way, Taniwha ↔ Inkanyamba. Faz 3'ün Lámia ↔ Strix kusuruyla aynı. Karşılıklı bir çift aynı fikri anlatabilir, aynı kelimeleri kullanamaz. |

---

## 11b. Kurucu kararları — 7 Ağustos 2026

Faz 3 raporunun kurucuya bıraktığı üç soru kapandı. **Üçü de artık açık
soru değildir.** Tam gerekçeler: `CHANGELOG.md` D39–D41.

| Konu | Karar | Faz 4'te ne yapılır |
|---|---|---|
| **A · İllüstrasyon** | Ham AI plaka üretimi **kurucunun sorumluluğudur** ve **Faz 5'ten önce** tamamlanacaktır. Faz 4 bu yüzden bloklanmaz. | Hat bekleme durumunda **hazır** tutulur ve bozulmaz. Plakaya bağlı Definition of Done maddeleri açık kalır ve sebebi yazılır. |
| **B · Üslup sürüklenmesi** | Mevcut sürüklenme (%21) Faz 4'te **düzeltilmez**. Faz 3 metni yeniden yazılmaz. | `qa_drift` düzenli koşar (her beş maddede), her ölçüm kayda geçer, artış olursa belgelenir. Düzeltme **Faz 5'in editoryal geçişine** aittir. |
| **C · Kayıtlı vaka açığı** | ⚠ **Faz 5'te GÜNCELLENDİ (D50).** Kısa ve hedefli bir tur SERBEST; kaynak hızlıca bulunmazsa DURULUR. Tur yapıldı: iki vaka bulundu, iki kaynak atfı çürüdü. | 4. bölümler yalnızca araştırma dosyasındaki malzemeden yazılır. **Tarihsel vaka uydurulmaz, örnek uydurulmaz.** Konu gelecek bir baskıda yeniden açılabilir; not Faz 5'te. |

> Üçünün ortak yanı: hiçbiri bir kapıyı gevşetmiyor. Ertelenen şey
> **düzeltme**dir, **ölçüm** değil.

---

## 12. Faz 3'ün bulgusu: "kayıtlı vaka" açığı

Yol haritası maddenin 4. bölümü için şunu istiyor:

> *"Ne yapar" bölümünde bir OLAY anlat, bir özellik listesi değil. Mümkünse
> kayıtlı bir vaka: "A boy from Lough Neagh mounted one in 1808…"*

Faz 3'ün ilk işi bu girdiyi aramak oldu. Sonuç:

| | |
|---|---:|
| Faz 3 kapsamındaki madde | 45 |
| Araştırma dosyasında **gerçek** vaka | **3** |
| *"Faz 3'te kaynaktan doğrudan okunacak"* yazan | **42** |

Yani Faz 1, kayıtlı vakayı bilinçli olarak **Faz 3'e ertelemişti** ve
erteleme dosyalara yazılmıştı. Faz 3 bu açığı **uydurarak kapatmadı.**

### Ne yapıldı

Kurucu emri mutlaktı: *"Never invent mythology. Never invent historical
claims. Never fabricate references."* Yol haritası da aynı yerde
diyor ki *"dosyada olmayan hiçbir detay yazılmaz"*.

Dolayısıyla 4. bölümler **yalnızca araştırma dosyasındaki** malzemeden
yazıldı: `behaviour` alanı, `variants`, `counter` ve dosyanın işaret
ettiği kanonik olay. Klasik ve destansı maddelerde kanonik olayın kendisi
zaten kayıtlı bir vakadır ve künyesi dosyadadır — Herakles'in on ikinci
işi (Apollodoros 2.5.12), Ḫumbaba'nın öldürülmesi (Tablet V), Yarasa
Evi'nde Hunahpú'nun başı (Popol Vuh II).

**Üç maddede tam anlamıyla tarihli/adlı vaka yazılabildi:**

| Madde | Vaka | Kaynak |
|---|---|---|
| Strix | Beş günlük Proca; alıç dalı, üç vuruş, domuz sakatatının sunulması | Ovidius, *Fasti* VI.131–168 |
| Olgoi-Khorkhoi | Moğol yetkililerden bir meclis yaratığı oybirliğiyle tarif eder — hiçbiri görmemiştir | Andrews 1926 |
| Devi | Üç, beş, dokuz ve on başlı kardeşler sırayla gönderilir | Wardrop 1894, *Ghvthisavari* |

### Faz 4–5 için ne demek

Bu bir **eksik değil, ertelenmiş bir araştırma kalemidir** ve kalan 67
maddede de aynı biçimde karşılaşılacaktır. İki seçenek vardı:

1. **Bugünkü çözüm** — 4. bölüm dosyadaki malzemeden yazılır; kanonik olay
   varsa vaka odur. Uydurma riski sıfır, "tarih ve yer" oranı düşük.
2. **Ek araştırma turu** — 109 maddenin `incident` alanı için kaynak
   metinlere dönülür. Maliyetli ve Faz 1'in bütçesinde yoktu.

**Kurucu (1)'i seçti** — karar C, 7 Ağustos 2026 · CHANGELOG D41.
Faz 4 aynı yöntemle yazılır. Tarihsel vaka uydurulmaz, örnek uydurulmaz;
kayıt yoksa cümle de yoktur. Konu, yeni doğrulanmış kaynak bulunursa
**gelecek bir baskıda** yeniden açılabilir ve bu not Faz 5'e bırakıldı.
