# FAZ 3 — NİHAİ RAPOR

> **Çekirdek Yazım · Bekçiler ve Yutucular**
> Tamamlanma: 7 Ağustos 2026 · Etiket `v0.3.0` · Kapı `phase3`
>
> Buradaki her sayı bir dosyadan ölçülmüştür. Ölçülemeyen alan **—** ile
> gösterilir. **Kitabın prozası bu depoda değildir** (karar A1/D29);
> görünen şey ölçüm, durum ve hattır.

---

## 1. Yönetici özeti

Kitabın **ilk 45 maddesi yazıldı**: sınıf I (THE GUARDIANS, 18) ve sınıf II
(THE DEVOURERS, 27), iki sınıf açılışı ve dört karşılaştırma açılışıyla
birlikte. **30.288 kelime** madde metni ve **3.111 kelime** açılış metni
üretildi. Bant dışı madde **sıfır**; bütün metin kapıları yeşil.

Faz 3 kitabın **sesini kurdu**. Yol haritasının deyişiyle sonraki 67 madde
bu 45'in ritmini takip edecektir, ve o ritim artık ölçülmüş bir sayıdır:
madde ortalaması 673 kelime, cümle ortalaması 16,7.

Fazın en değerli çıktısı metnin kendisi değil belki de şudur: **yazım
hattın beş gerçek kusurunu ortaya çıkardı ve üçü ölü kuraldı** — hiç
devreye girmemiş muafiyetler ve denetimler. Metin yokken yeşil yanan bir
hat, metin geldiğinde kırmızı yanmayı da becerememişti. Hepsi kapatıldı,
her biri kasıtlı bir kusurla sınandı.

İki şey açık kaldı ve ikisi de dürüstçe raporlanıyor: **plakalar** (hattın
dışındaki tek girdi, kurucudan gelir) ve **üslup sürüklenmesi %21** (uyarı
bandında, Faz 5'e devredildi).

---

## 2. Yazım istatistikleri

| Ölçü | Değer | Kaynak |
|---|---:|---|
| Yazılmış madde | **45** | `qa_length` |
| Madde metni | **30.288 kelime** | `qa_length` |
| Açılış metni | **3.111 kelime** | `write_entry --status` |
| **Toplam üretilen proza** | **33.399 kelime** | |
| Madde ortalaması | **673** (hedef 700 · sapma %3,9) | `qa_length` |
| En kısa madde | 632 (Stállu) | `qa_length` |
| En uzun madde | 707 (Kérberos) | `qa_length` |
| 620–790 bandı dışında | **0** | `qa_length` |
| Bölüm bandı dışında | **0** | `qa_length --sections` |
| Kitap geneli cümle ortalaması | **16,7** (bant 14–18) | `qa_voice` |
| Ünlem işareti | **0** | `qa_voice` |
| Yasak belirsizlik kalıbı | **0** | `qa_voice` |
| Oyun terminolojisi | **0** | `qa_voice` |
| Ölçülemez üstünlük iddiası | **0** | `qa_voice` |
| Sevimlileştirme kalıbı | **0** | `qa_voice` |
| Maddeler arası 8+ kelimelik tekrar | **0** | `qa_echo` |
| Birebir kopya paragraf | **0** | `qa_echo` |
| Tekrar eden açılış cümlesi | **0** | `qa_echo` |
| Diakritik düşürülmüş ad | **0** | `qa_diacritics` |
| Yazım turu (parti) | 15 parti × 3 madde + 6 açılış | |

**Üç madde kuralı (K13) hiç ihlal edilmedi.** Her parti üç maddeydi;
`write_entry.py --merge` bant dışı bir partiyi reddediyor ve dört kez
reddetti.

---

## 3. Tamamlanan yaratıklar

### Sınıf I · THE GUARDIANS — 18/18

| # | Madde | Gelenek | Aile | Kelime |
|---:|---|---|---|---:|
| 1 | Kérberos | Hellenic | F | 707 |
| 19 | Ḫumbaba | Sumer | F | 703 |
| 26 | Basiliscus | Romana | F | 682 |
| 29 | Qílín | Zhōnghuá | F | 698 |
| 34 | Camazotz | Maya | F | 695 |
| 39 | Domovoy | Slovjan | — | 676 |
| 61 | Basajaun | Euskal | G | 689 |
| 64 | Koropokkuru | Ainu | H | 684 |
| 65 | Repun Kamuy | Ainu | — | 692 |
| 69 | Ông Ba Mươi | Việt | — | 681 |
| 77 | Migoi | Bod | G | 686 |
| 82 | Aralez | Hayk | F | 707 |
| 85 | Golem | Talmud | F | 706 |
| 98 | Curupira | Tupi-Guarani | G | 685 |
| 99 | Boitatá | Tupi-Guarani | — | 691 |
| 105 | Ulda | Sápmi | H | 677 |
| 107 | Huldufólk | Ísland | H | 665 |
| 112 | Temes Savsap | Melanesia | F | 694 |

### Sınıf II · THE DEVOURERS — 27/27

| # | Madde | Gelenek | Aile | Kelime |
|---:|---|---|---|---:|
| 2 | Chímaira | Hellenic | — | 689 |
| 3 | Lámia | Hellenic | C | 668 |
| 4 | Ammit | Kemet | — | 667 |
| 7 | Fenrir | Norðr | — | 667 |
| 21 | Lamashtu | Sumer | C | 661 |
| 25 | Strix | Romana | C | 663 |
| 42 | Adze | Yorùbá · Ashanti | C | 674 |
| 48 | Ponaturi | Mā'ohi | — | 660 |
| 49 | Qalupalik | Inuit | C | 657 |
| 50 | Amarok | Inuit | — | 669 |
| 52 | Al Karısı | Türk | C | 670 |
| 53 | Karakoncolos | Türk | — | 681 |
| 55 | Ghūl | ʿArab | — | 676 |
| 60 | Ajatar | Suomi | — | 669 |
| 66 | Kenas-unarpe | Ainu | C | 661 |
| 68 | Ma lai | Việt | C | 646 |
| 71 | Krasue | Siam | C | 644 |
| 73 | Aswang | Filipin | C | 670 |
| 74 | Manananggal | Filipin | C | 676 |
| 79 | Srin-po | Bod | — | 642 |
| 80 | Olgoi-Khorkhoi | Mongol | — | 664 |
| 84 | Devi | Kartveli | — | 661 |
| 86 | Lilith | Talmud | C | 644 |
| 89 | Tokoloshe | Nguni | — | 660 |
| 96 | Pishtaco | Tawantinsuyu | — | 642 |
| 103 | Windigo | Anishinaabe | — | 657 |
| 104 | Stállu | Sápmi | G | 632 |

### Açılışlar — 6/6

| Açılış | Kelime |
|---|---:|
| Sınıf I · THE GUARDIANS | 509 |
| Sınıf II · THE DEVOURERS | 521 |
| Aile C · The Night Hag | 536 |
| Aile F · The Threshold Guardian | 513 |
| Aile G · The Wild Man | 522 |
| Aile H · The Hidden People | 510 |

---

## 4. Tamamlanan sayfalar

**45 maddenin tamamı GERÇEK metinle dizildi.** Faz 2'nin prova dizgisi
ölçüm dolgusuyla çalışıyordu ve gerekçesi doğruydu — o fazda proza yoktu.
Faz 3'te `entry_page.py` gerçek metni okuyacak biçimde genişletildi (D36);
dolguyla ölçmeye devam etmek modeli modele karşı sınamak olurdu.

| | Faz 2 modeli (dolgu) | **Faz 3 ölçümü (gerçek metin)** |
|---|---:|---:|
| İçerik yüksekliği | 2,558 sayfa | **2,144 sayfa** |
| En az / en çok | — | 2,018 / 2,245 |
| Faturalanan sayfa/madde | 3,0 | **3,0** |
| Sınıf I + II toplamı | 135 sayfa | **135 sayfa** |
| Açılışlar (6 × 2) | 12 sayfa | 12 sayfa |
| **Faz 3 toplamı** | 147 | **147** |

**Sayfa bütçesi değişmedi.** Model muhafazakârmış: gerçek metin dolgudan
%16 daha az dikey yer kaplıyor. Ama plaka kuralı yüzünden her madde sayfa
başından başlıyor ve 3 sayfa faturalanıyor, dolayısıyla **436 sayfalık
toplam bütçe ve fiyat modeli olduğu gibi geçerli**.

Yol haritasının kuralı: *"Sayfa sayısı hedeften %5'ten fazla saparsa
kelime hedefini değil sayfa bütçesini düzelt ve kurucuya bildir."*
**Sapma %0. Düzeltme gerekmedi.**

Yan bulgu: madde başına boş kalan alan modelin öngördüğünden fazla
(0,86 sayfa yerine 0,44). Bu, Faz 6'da dizgi esnekliği demektir.

---

## 5. Yazılan kelimeler

| | Kelime |
|---|---:|
| Madde metni (45) | 30.288 |
| Açılış metni (6) | 3.111 |
| **Toplam** | **33.399** |
| Kitap hedefi | 78.400 |
| İlerleme | **%42,6** |

---

## 6. Eklenen çapraz referanslar

Faz 3 **yeni çapraz referans eklemedi** ve eklememesi gerekiyordu.
181 karşılıklı bağın tamamı Faz 2'de `kin_map.json`'da kurulmuş ve
`classify.py` tarafından `spec.json`'a yazılmıştı.

Faz 3'ün işi bu bağları **metne geçirmekti**: 45 maddenin 6. bölümü
("Akrabaları") `spec.json`'daki `crossRefs` alanından yazıldı.

| Ölçü | Değer |
|---|---:|
| Faz 3 maddelerinin taşıdığı bağ | **140** |
| Madde başına ortalama | 3,11 |
| En az / en çok | 2 / 5 |
| Kırık bağ | **0** |
| `crossRefs` ile tutmayan akraba satırı | **0** |

Yol haritasının editoryal görevi — *"Akraba satırlarını `spec.json`'daki
`crossRefs` ile karşılaştır"* — 45 maddede tek tek uygulandı.

---

## 7. Araştırma kullanımı

Her madde **yalnızca** kendi araştırma dosyasından yazıldı. Kurucu emri
mutlaktı: uydurma mitoloji yok, uydurma tarihsel iddia yok, uydurma
künye yok.

| Ölçü | Değer |
|---|---:|
| Kullanılan araştırma dosyası | 45/45 |
| Dosyada olmayan detay yazıldı | **0** |
| Uydurulan künye | **0** |
| Kısıtlılık kapısı altındaki madde | **22** |

### Kısıtlılık kapısı — 22 madde

Yaşayan gelenekler için yalnızca yayımlanmış ve kısıtlanmamış malzeme
kullanıldı; tören bilgisi, başlatma bilgisi ve topluluk-özel anlatı
**kullanılmadı**.

| Madde | Uygulanan kısıt |
|---|---|
| Koropokkuru · Repun Kamuy · Kenas-unarpe | Ainu tören bilgisi, iyomante, inaw yok; Batchelor'ın misyoner çerçevesi eleştirel okundu |
| Ulda · Stállu | Sámi yoik, siida bilgisi, tören yok; derleyici çerçevesi metinde anıldı |
| Migoi · Srin-po | Manastır uygulaması ve yer-özel kutsal anlatı yok; kriptozooloji kaynak sayılmadı |
| Curupira · Boitatá | Yalnızca yayımlanmış derleme; Anchieta'nın misyoner çerçevesi eleştirel okundu |
| Golem · Lilith | Sefer Yetzirah harf/ad uygulaması ve muska METNİ aktarılmadı |
| Qalupalik · Amarok | Angakkuq uygulaması yok; Rasmussen eleştirel okundu |
| Boitatá · Olgoi-Khorkhoi | Topluluk-özel anlatı ve şaman uygulaması yok; kriptozooloji kaynak sayılmadı |
| Ponaturi | Iwi-özel anlatı ve whakapapa yok |
| Temes Savsap | Maki derece töreni ve başlatma bilgisi yok |
| Windigo | 'Windigo psikozu' tanısı **yeniden üretilmedi** |
| Adze · Aswang · Tokoloshe · Pishtaco | Suçlama yeniden üretilmedi; teşhis yöntemi aktarılmadı |

**Dört madde etik hattın en ağır ucunda.** Adze, Aswang, Tokoloshe ve
Pishtaco'ya bağlı suçlamalar gerçek insanlara yöneltilmiş ve gerçek
şiddet üretmiştir. Bu maddeler inancın var olduğunu ve yayımlanmış
kaynaklarda aldığı biçimi bildiriyor; hiçbir birey, aile, kasaba veya
insan kategorisini "muhtemel" diye anmıyor, hiçbir teşhis yöntemini işe
yararmış gibi aktarmıyor. Aswang'ın göz bebeği testi **çalışamayacağını
göstermek için** tarif edildi. Bu, D28'de kurulan Buda hattının aynısıdır.

### Bulgu — "kayıtlı vaka" açığı

| | |
|---|---:|
| Araştırma dosyasında **gerçek** vaka | **3/45** |
| *"Faz 3'te kaynaktan doğrudan okunacak"* yazan | **42/45** |

Faz 1 kayıtlı vakayı bilinçli olarak Faz 3'e ertelemişti. Faz 3 bu açığı
**uydurarak kapatmadı**: 4. bölümler dosyadaki `behaviour`, `variants`,
`counter` ve dosyanın işaret ettiği kanonik olaydan yazıldı.

Tam anlamıyla tarihli/adlı vaka yazılabilen üç madde:

| Madde | Vaka | Kaynak |
|---|---|---|
| Strix | Beş günlük Proca; alıç dalı, üç vuruş, domuz sakatatı sunumu | Ovidius, *Fasti* VI.131–168 |
| Olgoi-Khorkhoi | Moğol yetkililerden bir meclis yaratığı oybirliğiyle tarif eder — hiçbiri görmemiştir | Andrews 1926 |
| Devi | Üç, beş, dokuz ve on başlı kardeşler sırayla gönderilir | Wardrop 1894, *Ghvthisavari* |

Ayrıntı ve karar seçenekleri: `PROJECT_CONTEXT.md` § 12. **Karar
kurucunundur ve Faz 4 başlamadan verilmelidir.**

---

## 8. Oluşturulan dosyalar

### Depoda (public)

| Dosya | Ne |
|---|---|
| `08_BUILD/write_entry.py` | Yazım tezgâhı — bölüm bantları ve cümle ortalaması cetveli |
| `01_SOURCE/manuscript_metrics.json` | Depo dışındaki metnin ÖLÇÜSÜ; proza içermez |
| `06_REPORTS/FAZ_3_RAPORU.md` | Bu belge |

### Depo dışında (karar A1/D29)

| Dosya | Ne |
|---|---|
| `01_SOURCE/book.json` | **Manuscript** — 45 madde, 6 açılış, 33.399 kelime |
| `06_REPORTS/phase3-typeset-measurement.json` | 45 maddenin prova ölçümü |
| `04_PRINT/PROOF/entry-*.pdf` | Prova dizgisi çıktıları |

---

## 9. Değiştirilen dosyalar

| Dosya | Değişiklik |
|---|---|
| `.gitignore` | A1/D29 politikası; taslak, özel not, manuscript dökümü kalıpları |
| `08_BUILD/validate_structure.py` | `check_manuscript_leak` — proza sızıntısı kapısı (D30) |
| `08_BUILD/research_gen.py` | Yazım durumu artık ezilmiyor (D31) |
| `08_BUILD/qa_diacritics.py` | Büyük/küçük harf duyarlılığı (D32) + gerçek ad muafiyeti (D35) |
| `08_BUILD/qa_echo.py` | Kaynak notu muafiyeti + `ALLOWED_ECHOES` canlandırıldı (D34) |
| `08_BUILD/qa_drift.py` | Rapor yargıladığı sayıyı gösteriyor (D37) |
| `08_BUILD/entry_page.py` | Gerçek metinle dizgi (D36) |
| `08_BUILD/update_docs.py` | Manuscript ölçüsü depodan okunuyor (D38) |
| `01_SOURCE/spec.json` | 45 maddenin durumu `written` |
| `CHANGELOG.md` · `PROJECT_CONTEXT.md` · `BOOK_STATS.md` · `ROADMAP_PROGRESS.md` | Senkronlandı |
| `.gate` | `phase2` → `phase3` |

**17 dosya · +1.425 / −90 satır** (v0.2.1..v0.3.0)

---

## 10. Altyapı değişiklikleri

Faz 3 yazım fazıydı ama hattın **beş gerçek kusurunu** ortaya çıkardı.
Üçü ölü kuraldı: hiç devreye girmemiş muafiyetler ve denetimler.

| # | Kusur | Etki | Sınandı mı |
|---|---|---|---|
| D31 | `research_gen` yazım durumunu her tazelemede `verified`'a geri alıyordu | Tamamlanmış yazım işi **her `--fix` koşusunda kaybolurdu** | ✅ |
| D32 | `qa_diacritics` büyük/küçük harf duyarsız arıyordu | `Lóng` → `Long`; kitap "long" sözcüğünü hiç kullanamazdı — **doğru metni reddeden cetvel** | ✅ |
| D35 | `qa_diacritics` Bask `Lamia`yı `Lámia`nın düşürülmüşü sanıyordu | Bask maddesi ve ona yapılan **her çapraz referans yazılamazdı** | ✅ |
| D34 | `qa_echo` tutarlı künyeyi "üslup tekrarı" sayıyordu; `ALLOWED_ECHOES` **ölü kuraldı** | Yazar her maddede farklı künye uydurmaya zorlanırdı — bir başvuru cildinde kusurun ta kendisi | ✅ |
| D38 | `BOOK_STATS` metni olmayan depoda üretilemiyordu | **Her yazım commit'i CI'da kırmızı yanardı** | ✅ |

Ek olarak iki iyileştirme: `entry_page.py` gerçek metinle diziyor (D36),
`qa_drift` yargıladığı sayıyı gösteriyor (D37).

> Faz 2'nin dersi tekrar etti: **eşleşmeyen kural ölü kuraldır.**
> D28 (`ityop-ya`), D30 (yol kalıbı), D34 (`ALLOWED_ECHOES`) — üçü de
> aynı sınıf. Kapının sessizliği kalitenin kanıtı değildir.

---

## 11. `.gitignore` politika değişiklikleri

**Karar A1 kapatıldı: (a) şıkkı** — kurucu emri, 7 Ağustos 2026.
Depo **PUBLIC** kalır; ticari değeri olan manuscript depo **DIŞINDA** yaşar.

### Eklenen kalıplar

```
01_SOURCE/book-*.json          # her ara biçim
02_MANUSCRIPT/*                # taslak bölümler, dökümler
00_CONTEXT/private/            # özel editoryal notlar
**/*.private.md
**/*_PRIVATE.md
06_REPORTS/editorial/
```

### Açık kalan (kasıtlı)

otomasyon · hat · CI/CD · doğrulama · belgeler · **araştırma dosyaları**
(künye ve alıntı notudur, proza değildir; iki kaynak kapısının
denetlenebilmesi için gereklidirler) · **ölçümler**

### Politika mekanizmaya bağlandı (D30)

`.gitignore` bir **yol** listesidir ve başka bir ada konan proza dosyasını
yakalamaz. `validate_structure.check_manuscript_leak` eklendi:

1. `.gitignore` kuralı hâlâ yerinde mi
2. Proza yolları takip ediliyor mu
3. **İçerik:** takip edilen dosyalarda madde açılış cümlesi geçiyor mu

Kasıtlı bir sızıntı yerleştirilerek sınandı: **yakaladı.**

---

## 12. CI/CD durumu

| İş akışı | Durum | Son koşu |
|---|---|---|
| `validate` | ✅ yeşil | `main` |
| `build` | ✅ yeşil | `main` |
| `plates` | ✅ yeşil | `main` |
| `release` | ✅ yeşil | `v0.3.0` |

**CI iki kez kırmızı yandı ve iki kez yazım durduruldu:**

1. `BOOK_STATS` bayat (D38) — kök neden A1/D29'un doğrudan sonucuydu.
   Çözüldü, `book.json` gizlenerek sınandı.
2. Yerel kapı kırmızıyken push edildi (iki kez). Her ikisinde de hata
   bir sonraki komutta yakalandı ve **bir sonraki commit'te** düzeltildi;
   `main` hiçbir zaman kırmızı almadı.

---

## 13. Git commit'leri

**24 commit** (v0.2.1..v0.3.0), tamamı `faz/3-cekirdek` dalında,
PR #6 ile `main`'e merge edildi.

| Tür | Adet |
|---|---:|
| `yazim:` — madde partileri | 16 |
| `duzeltme:` — eko temizliği | 2 |
| `hat:` / `ci:` / `politika:` — altyapı | 3 |
| `belge:` — belge senkronu | 1 |
| Merge | 2 |

---

## 14. GitHub Actions sonuçları

- PR #6: bütün kapılar `pass`
- `main` merge sonrası: `validate` · `build` · `plates` ✅
- `v0.3.0` etiketi: `release` ✅ — **GitHub Release otomatik oluştu**
  (`Codex Bestiarium v0.3.0`, pre-release)

---

## 15. Definition of Done kontrol listesi

| # | Ölçüt | Durum |
|---|---|---|
| 1 | `qa_length` · `qa_voice` · `qa_echo` · `qa_drift` · `qa_diacritics` — 0 başarısız | ✅ (qa_drift **1 uyarı**) |
| 2 | 48 plaka normalize edildi ve ölçüldü; tolerans dışı sıfır | ⛔ **ham AI çıktısı yok** |
| 3 | Sınıf I ve II açılışları + dört karşılaştırma açılışı | ✅ 6/6 |
| 4 | Prova dizgisi çalıştırıldı; ölçülen sayfa `BOOK_STATS.md`'de | ✅ 45/45, gerçek metinle |
| 5 | Sürüklenme raporları `06_REPORTS/`'ta; eğim yükselmiyor | ⚠ rapor var; eğim **%21 yükseliyor** |
| 6 | CI yeşil, merge, `v0.3.0` etiketi | ✅ |

**Dört ölçüt tam, biri uyarılı, biri bloke.**

### 2. ölçüt neden bloke

Plaka hattı kurulu, kalibre ve sınanmış durumda (Faz 2, `plate_selftest`
%0,3 doğruluk). Eksik olan tek şey **ham AI çıktısıdır**:
`BESTIARIUM_IMAGE_PROMPTS.html` → görsel üreteç → `07_ASSETS/plates_raw/`.
Bu, üretim hattının **dışındaki tek girdidir** ve kurucudan gelir.
Faz 2'nin 6. ölçütü de aynı sebeple açıktı. **Faz 3'ün metin işi bu
girdiye bağlı değildi ve tamamlandı.**

---

## 16. Kalan riskler

| # | Risk | Olasılık | Etki | Durum |
|---|---|---|---|---|
| 1 | **Ham plaka seti gelmezse** 45 (ve sonunda 112) plaka üretilemez | — | **yüksek** | Kurucudan bekleniyor; iki fazdır açık |
| 2 | **Üslup sürüklenmesi %21** uyarı bandında; 112 maddede %35 başarısızlık eşiğine yaklaşabilir | orta | orta | Faz 4'te her 5 maddede `qa_drift`; Faz 5 editoryal inceleme |
| 3 | **Kayıtlı vaka açığı** kalan 67 maddede de sürecek | **yüksek** | orta | Karar kurucunun (§ 7) |
| 4 | Madde ortalaması hedefin **%3,9 altında** (673 vs 700); 112 maddede ~3.000 kelime eksik | — | düşük | Sayfa bütçesi ölçüldü ve **etkilenmedi** |
| 5 | `Lámia`/`Lamia` belirsizliği otomatik denetlenemiyor | düşük | düşük | Faz 5 düşman denetçi oturumuna devredildi (D35) |
| 6 | Proza depo dışında; CI metin kapılarını **boş koşuyor** | — | orta | Kabul edilen A1(a) bedeli; yerelde `qa_all.sh` tam koşuyor, ölçü depoda (D38) |

---

## 17. BOOK_STATS özeti

| Ölçü | Şu an | Hedef |
|---|---:|---:|
| Yaratık kaydı | 112 | 112 |
| **Yazılmış madde** | **45** | 112 |
| **Kelime (yazılmış)** | **33.399** | 78.400 |
| Normalize plaka | **0** | 112 |
| Durum `written` | 45 | — |
| Durum `verified` | 67 | — |

---

## 18. ROADMAP_PROGRESS özeti

| Faz | Başlık | İlerleme | Etiket |
|---:|---|---|---|
| 1 | Altyapı, Araştırma, Kapsam | 112/112 (%100) | `v0.1.0` |
| 2 | Tasnif, Veri Modeli, Plaka | 112/112 (%100) | `v0.2.0` |
| **3** | **Çekirdek Yazım** | **45/45 (%100)** | **`v0.3.0`** |
| 4 | Genişleme | 0/43 (%0) | `v0.4.0` |
| 5 | Tamamlama ve İnceleme | 0/24 (%0) | `v0.5.0` |
| 6 | Üretim ve Lansman | 0/4 (%0) | `v1.0.0` |

---

## 19. PROJECT_CONTEXT güncellemeleri

- § 1 — Faz 3 durumu ve Definition of Done tablosu
- § 11 — sıradaki adım Faz 4; A1 kapandı; devredilen üç kalem
- **§ 12 — yeni:** "kayıtlı vaka" açığı, sayılarla ve karar seçenekleriyle

---

## 20. CHANGELOG özeti

`[0.3.0]` bloğu eklendi: ölçülenler, prova dizgisi karşılaştırması,
sürüklenme uyarısı, on karar (D29–D38).

| Karar | Konu |
|---|---|
| D29 | A1 kapandı — depo public, proza dışarıda |
| D30 | Politika içerikten denetleniyor |
| D31 | Araştırma hattı yazım durumunun sahibi değil |
| D32 | `qa_diacritics` harf duyarlı |
| D33 | Cümle uzunluğu nişanı 16,0 |
| D34 | `qa_echo` künye muafiyeti; ölü kural canlandırıldı |
| D35 | Gerçek ad çakışması bayraklanmıyor |
| D36 | `entry_page` gerçek metinle diziyor |
| D37 | `qa_drift` yargıladığı sayıyı gösteriyor |
| D38 | Manuscript ölçüsü depoya alındı |

---

## 21. Faz 4 hazırlık değerlendirmesi

**Faz 4 teknik olarak hazırdır.**

| Girdi | Durum |
|---|---|
| Araştırma dosyaları (sınıf III + IV, 43 madde) | ✅ hazır, hepsi `verified` |
| Çapraz referanslar | ✅ Faz 2'de kilitli |
| Açılış planları (A · B · E) | ✅ `KIN_OPENINGS.md`'de kilitli |
| Yazım tezgâhı | ✅ `write_entry.py`, kalibre |
| Kalite kapıları | ✅ beş kusuru kapatılmış, sınanmış |
| Ses kalibrasyonu | ✅ 45 maddede ölçüldü: 673 kelime · 16,7 cümle |
| Sayfa bütçesi | ✅ gerçek metinle doğrulandı |

**Faz 4 kapsamı:** sınıf III (19) + sınıf IV (24) = **43 madde**, üç
karşılaştırma açılışı (A · B · E). *Yol haritası 22+24=46 diyor; bu da
120 maddelik aşılmış kapsamdan gelir — Faz 3'ün 48/45 farkıyla aynı
sebep, D21.*

### Faz 4'ten önce kurucudan beklenen üç karar

1. **Kayıtlı vaka** — bugünkü çözümle devam mı, ek araştırma turu mu? (§ 7)
2. **Ham plaka seti** — iki fazdır bekliyor; Faz 5'in illüstrasyon işi
   buna bağlı ve takvim riski büyüyor.
3. **Üslup sürüklenmesi** — Faz 5'e mi bırakılsın, Faz 4'te mi
   müdahale edilsin?

### Ses kalibrasyonu okuması

Yol haritası: *"Bu fazın ilk beş maddesi bittiğinde sizden okumanızı
isteyeceğim. Ses burada kurulur."* Ses **ölçüldü** ve bantta; ama
**kurucu henüz okumadı**. Faz 4 başlamadan önce en az beş maddenin
okunması önerilir — ölçüm sesin bantta olduğunu söyler, doğru ses
olduğunu söylemez.

---

*Faz 3 tamamlandı. Faz 4 kurucu onayı bekliyor.*
