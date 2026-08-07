# Codex Bestiarium — Üretim Sistemi

> **Bir kitap değil, bir kitabı üreten sistem.**
> Bu depo *Codex Bestiarium*'un yazım, illüstrasyon, dizgi, doğrulama ve
> yayın hattını barındırır. Kitabın kendisi İngilizcedir; bu depodaki
> belgeler, raporlar ve commit mesajları Türkçedir.

[![validate](https://github.com/emredogan-cloud/codex-bestiarium/actions/workflows/validate.yml/badge.svg)](https://github.com/emredogan-cloud/codex-bestiarium/actions/workflows/validate.yml)
[![build](https://github.com/emredogan-cloud/codex-bestiarium/actions/workflows/build.yml/badge.svg)](https://github.com/emredogan-cloud/codex-bestiarium/actions/workflows/build.yml)

---

## Kitap ne anlatıyor

Her kültürde bir su atı vardır. Her kültürde bir gece cadısı, bir eşik
bekçisi, bir fırtına kuşu vardır. Bu kitap yaratıkları anlatmıyor — **aynı
korkunun kırk ayrı yüzünü** anlatıyor.

Rafın tamamı yaratıkları **bölgeye** göre sıralıyor: Slav cildi, Kelt cildi,
İskandinav cildi. Bu kitap **işleve** göre sıralıyor. Okur "su atı" bölümünü
açtığında İrlanda'nın *each-uisce*'sini, İzlanda'nın *nykur*'unu, Finlandiya'nın
*näkki*'sini ve Filipinler'in *tikbalang*'ını yan yana görüyor.

| | |
|---|---|
| **Kapsam** | 120 yaratık · 40 gelenek · 6 sınıf · 8 akraba imge ailesi |
| **Hacim** | ~404 sayfa · ~92.000 kelime · 6 × 9 inç |
| **İllüstrasyon** | 120 çizgi plaka, tek gravür dilinde |
| **Formatlar** | Ciltsiz · Ciltli · Büyük punto · Kindle |
| **Seri** | Codex · Cilt 2 (Cilt 1: *Codex Mythologica*) |
| **Yayınevi** | Vâliçe Press |

---

## Bu depoda ne var, ne yok

**Var:** üretim hattının tamamı — kod, CI/CD, şema, doğrulayıcılar, plaka
prompt kütüphanesi, yol haritası, KDP kılavuzu, yaratık *metadata*'sı
(ad, sınıf, gelenek, motif kodu, kaynak künyeleri, çapraz referanslar).

**Yok:** kitabın **prozası**. `01_SOURCE/book.json` ve üretilmiş yayın
dosyaları `.gitignore`'dadır. Gerekçe ve alternatifler:
[yol haritası § A1](CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md#a1--depo-herkese-açık-manuscript-ne-olacak).

---

## Hızlı başlangıç

```bash
git clone https://github.com/emredogan-cloud/codex-bestiarium.git
cd codex-bestiarium

./08_BUILD/bootstrap.sh     # venv + fontlar + kapı testi
./08_BUILD/qa_all.sh        # bütün kalite kapıları
```

`bootstrap.sh` **yalnızca üretim** (plaka, dizgi, kapak, EPUB) için gerekir.
Kalite kapılarının hiçbiri üçüncü taraf pakete ihtiyaç duymaz; hepsi standart
kütüphaneyle koşar. CI'ın ana doğrulama işi bu yüzden saniyeler sürer.

---

## Kalite kapıları

Bu projenin merkezinde tek bir fikir var: **kalite ölçülür, göz kararıyla
kabul edilmez.** Her kapı bir komuttur, her komut bir çıkış kodu döner ve
CI o kodu okur.

| Kapı | Komut | Ne arar |
|---|---|---|
| Tohum | `seed_import.py --check` | `spec.json` master yol haritasıyla uyumlu mu |
| Şema | `validate_spec.py --gate <seviye>` | 120 kaydın alanları, kimlikleri, kaynakları, çapraz referansları |
| Yapı | `validate_structure.py` | klasör ağacı, adlandırma, başlık hiyerarşisi, bağlantılar, terminoloji, Unicode, JSON/YAML/HTML |
| Uzunluk | `qa_length.py --sections` | madde 620–790 bandında; yedi bölümün her biri kendi bandında |
| Ses | `qa_voice.py` | "it is said", oyun terimi, ölçülemez üstünlük, sevimlileştirme, ünlem |
| Sürüklenme | `qa_drift.py` | en sık 50 kelimede yükselen eğim |
| Tekrar | `qa_echo.py` | maddeler arası 8+ kelimelik birebir öbek |
| Diakritik | `qa_diacritics.py` | Ḫumbaba → Humbaba düşmesi, görünmez karakter |
| Plaka | `plates.py --measure` | çizgi kalınlığı, tarama açısı, sıklık, kontrast, kapsama |
| Format | `convert_plates.py --check` | Kindle bütçesi (plaka başına ≤60 KB) |
| Belge | `update_docs.py --check` | `BOOK_STATS.md` ve `ROADMAP_PROGRESS.md` bayat mı |

### Kapıların kendi testi

```bash
python3 08_BUILD/tests/selftest.py
```

Bu, hattın en önemli testidir. İki kurgu kitap çalıştırır: biri temiz, biri
her kapıya kasıtlı bir kusur yerleştirilmiş. Temiz olan geçmeli, kusurlu olan
**yakalanmalıdır**. Metin yokken yeşil kalan bir hat, kusur geldiğinde de
yeşil kalabilir — bu test o riski kapatır.

> Bu test ilk çalıştırmasında gerçek bir kusur buldu: kurgu üreteci sabit
> adımlı bir sayaç kullandığı için kendi kendini tekrarlıyordu ve `qa_echo`
> haklı olarak alarm verdi. Düzeltilen betik değil, **kurgu** oldu.

---

## Klasör yapısı

```
CODEX_BESTIARIUM/
├── 00_CONTEXT/     PROJECT_CONTEXT · BRIEF · STYLE · STYLE_PLATES
├── 01_SOURCE/      spec.json (TEK DOĞRULUK KAYNAĞI) · research/ · indexes.json
├── 02_MANUSCRIPT/  DOCX yedeği
├── 03_COVER/       artwork · PAPERBACK/ HARDCOVER/ LARGEPRINT/
├── 03_APLUS/       Amazon A+ İçerik modülleri
├── 04_PRINT/       ★ KDP'ye yüklenecek iç bloklar
├── 05_KINDLE/      reflowable EPUB (≤7 MB)
├── 06_REPORTS/     doğrulama çıktıları · üretim raporları
├── 07_ASSETS/      fonts · plates_raw (DEĞİŞTİRİLMEZ) · plates · plates_*
├── 08_BUILD/       bütün hat — her şey buradan üretilir
└── 09_ARCHIVE/     aşılmış sürümler
```

### Üç kural

1. **`spec.json` tek doğruluk kaynağıdır.** Dizinler, promptlar, istatistikler,
   dizgi — hepsi ondan türer. İki yerde tutulan bir sayı, er geç iki farklı
   sayı olur.
2. **`07_ASSETS/plates_raw/` asla değiştirilmez.** Ham AI çıktısı olduğu gibi
   durur; normalizasyon `plates.py` ile yapılır ve `plates/` içine yazar.
3. **Üretilen belge elle düzenlenmez.** `BOOK_STATS.md`, `ROADMAP_PROGRESS.md`,
   `BESTIARIUM_IMAGE_PROMPTS.html`, `06_REPORTS/INDEXES_PREVIEW.md` — hepsi
   bir sonraki üretimde kaybolur. Kaynağı düzenleyin, betiği çalıştırın.

---

## Belgeler

| Belge | Ne için |
|---|---|
| [`CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md`](CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md) | **Tek doğruluk kaynağı.** Altı faz, kapılar, kararlar, riskler |
| [`00_CONTEXT/PROJECT_CONTEXT.md`](00_CONTEXT/PROJECT_CONTEXT.md) | Projeyi aylar sonra devralacak kişi için |
| [`00_CONTEXT/STYLE.md`](00_CONTEXT/STYLE.md) | Yazım kuralları, ses, yasak kalıplar |
| [`00_CONTEXT/STYLE_PLATES.md`](00_CONTEXT/STYLE_PLATES.md) | Çizgi dili şartnamesi |
| [`00_CONTEXT/BRIEF.md`](00_CONTEXT/BRIEF.md) | Konumlanma, kitle, metadata, SEO |
| [`BESTIARIUM_IMAGE_PROMPTS.html`](BESTIARIUM_IMAGE_PROMPTS.html) | 120 plakalık prompt kütüphanesi (tarayıcıda açın) |
| [`BESTIARIUM_KDP_PUBLISHING_GUIDE.md`](BESTIARIUM_KDP_PUBLISHING_GUIDE.md) | KDP'de ekran ekran, düğme düğme yayın |
| [`BOOK_STATS.md`](BOOK_STATS.md) | Ölçülen istatistikler (otomatik) |
| [`ROADMAP_PROGRESS.md`](ROADMAP_PROGRESS.md) | Faz ilerlemesi (otomatik) |
| [`CHANGELOG.md`](CHANGELOG.md) | Kararlar ve değişiklikler |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Çalışma düzeni, dal ve commit kuralları |

---

## Durum

Faz 1'in **altyapı** kısmı tamamlandı; araştırma başlamayı bekliyor.
Güncel ölçüm için [`ROADMAP_PROGRESS.md`](ROADMAP_PROGRESS.md).

| Faz | Başlık | Durum | Etiket |
|---:|---|---|---|
| 1 | Altyapı, Araştırma ve Kapsam Kilidi | 🔨 altyapı hazır · araştırma bekliyor | `v0.1.0` |
| 2 | Tasnif, Veri Modeli ve Pilot Plaka Seti | ⏳ planlandı | `v0.2.0` |
| 3 | Çekirdek Yazım · Bekçiler ve Yutucular | ⏸ kurucu onayı bekliyor | `v0.3.0` |
| 4 | Genişleme · Şekil Değiştirenler ve Su Sakinleri | ⏸ | `v0.4.0` |
| 5 | Tamamlama, İllüstrasyon ve Editoryal İnceleme | ⏸ | `v0.5.0` |
| 6 | Üretim, KDP ve Lansman | ⏸ | `v1.0.0` |

---

## In English

This repository is the **production system** for *Codex Bestiarium*, the
second volume in the Codex series from Vâliçe Press: a reference bestiary of
120 creatures from 40 traditions, classified **by function rather than by
region**, with at least two independent sources and a Thompson motif code for
every entry.

The book is in English. The engineering documents, reports and commit messages
are in Turkish.

The repository holds the pipeline, not the prose: schema, validators, quality
gates, the plate-prompt library, the typesetting engine and the CI/CD that
refuses any push which lowers quality. The manuscript itself is deliberately
kept out of version control — see
[§ A1 of the roadmap](CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md#a1--depo-herkese-açık-manuscript-ne-olacak).

Every entry passes a two-independent-sources gate before it may be written.
Material from living traditions is screened for restriction: nothing known to
be restricted is retold — it is **named as restricted**. Australian Aboriginal
traditions are deliberately excluded and the reason is stated in the afterword,
as a standard rather than an omission.

---

## Lisans

- **Kod** (`08_BUILD/`, `.github/`) — MIT, bkz. [`LICENSE`](LICENSE).
- **Kitabın metni, illüstrasyonları ve kapağı** — © 2026 Emre Doğan · Vâliçe Press.
  Bütün hakları saklıdır. MIT lisansı bunları **kapsamaz**.
- **Fontlar** — Cinzel ve EB Garamond, SIL Open Font License 1.1.

Kitabın anlattığı folklor kamu malıdır; bu kitabın **prozası** değildir.
