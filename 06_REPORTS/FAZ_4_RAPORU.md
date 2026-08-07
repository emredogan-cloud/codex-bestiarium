# FAZ 4 · NİHAİ RAPOR

**Codex Bestiarium — Genişleme · Şekil Değiştirenler ve Su Sakinleri**
Sürüm `v0.4.0` · 7 Ağustos 2026 · dal `main`

> Buradaki her sayı bir dosyadan ölçülmüştür veya bir kod satırından
> türetilmiştir. Hiçbiri tahmin değildir. Ölçüm komutları her başlıkta
> gösterilmiştir.

---

## 1. Yönetici özeti

Faz 4 tamamlandı. Sınıf III (Şekil Değiştirenler, 19 madde) ve sınıf IV
(Su Sakinleri, 24 madde) yazıldı — **43 madde, 29.770 kelime** — iki sınıf
açılışı ve üç karşılaştırma açılışıyla birlikte. Kitap **88/112 maddeye**
ve **65.911 kelimeye** ulaştı.

Üç şey öne çıkıyor.

**① Üslup sürüklenmesi %21,0'dan %8,9'a düştü ve tek bir Faz 3 maddesi
üslup için açılmadı.** Kurucu kararı D40 düzeltmeyi Faz 5'e erteledi ve
yalnızca ölçüm istedi. Faz 4 on beş kez ölçtü, her ölçümü commit iletisine
yazdı ve düşüşü *yeni maddelerin somut mekanizma anlatmasından* aldı —
takvim, ters toynak, baştaki çanak, kuyruktaki el, ekimde yükselen ışık.
Erteleme bir taviz değildi; disiplinin kendisi düşüşü üretti.

**② `qa_echo` on dokuz kalıplaşma yakaladı ve hepsi gerçekti.** Üç ayrı
küme çıktı: yazarın çözümleyici kalıpları, karşılıklı çapraz referansların
aynı cümleyle kurulması, ve — en önemlisi — **yaşayan gelenek kısıt
cümlesinin boilerplate'e dönmesi**. Üçü de Faz 5'in uyumlama geçişine
somut hedef olarak devredildi.

**③ Yol haritasının "göz işi" olarak yazdığı iki görev mekanizmaya
çevrildi.** Akraba satırı ↔ `crossRefs` karşılaştırması ilk koşuşunda dört
gerçek kusur buldu (D42); ara prova dizgisi artık 88 maddenin tamamını
dizip dağılımı raporluyor (D45).

Sayfa bütçesi 88 maddenin tamamı gerçek metinle dizilerek yeniden
doğrulandı: **436 sayfa, değişmedi**.

Faz 4'ün tek açık maddesi Faz 2 ve Faz 3'ünkiyle aynıdır ve artık bir
karardır: **ham AI plaka üretimi kurucunundur (D39)** ve Faz 5'ten önce
gelecektir. Hat bekleme durumunda hazır tutuldu ve bu fazda bir kez daha
sınandı.

---

## 2. Tamamlanan hedefler

Yol haritası Faz 4'ün altı çıktısı ve durumları:

| # | Çıktı | Durum |
|---|---|---|
| 1 | Sınıf III · THE SHAPE-CHANGERS | ✅ **19/19** |
| 2 | Sınıf IV · THE WATER-DWELLERS | ✅ **24/24** |
| 3 | İki sınıf açılışı | ✅ III (542) · IV (561) |
| 4 | Karşılaştırma açılışları A · B · E | ✅ 549 · 540 · 534 |
| 5 | 45 normalize plaka (toplam 93) | ⛔ **ham AI çıktısı kurucudan (D39)** |
| 6 | Kin-Images Chart taslağı | ✅ `make_kin_chart.py` · 8 aile · 2 sayfa |

Yazım, editoryal ve doğrulama görevlerinin tamamı kapandı. Dizgi
görevlerinden plaka üretimine bağlı olanlar D39 kapsamındadır.

---

## 3. Yazım istatistikleri

`python3 08_BUILD/write_entry.py --status` · `qa_length` · `qa_voice`

| Ölçü | Faz 4 | Kitap (88 madde) |
|---|---:|---:|
| Yazılmış madde | **43** | **88/112** (%79) |
| Madde metni | **29.770** kelime | **60.074** kelime |
| Madde ortalaması | **692** (hedef 700 · sapma **%1,1**) | 683 |
| En kısa / en uzun | 652 / 752 | 632 / 752 |
| Bant dışı madde (620–790) | **0** | **0** |
| Bölüm bandı ihlali | **0** | **0** |
| Açılış | 5 · 2.726 kelime | 11 · 5.837 kelime |
| **Toplam metin** | — | **65.911** kelime |
| Kitap geneli cümle ortalaması | — | **16,9** (bant 14–18) |
| Ünlem işareti | 0 | **0** |
| Yasak belirsizlik kalıbı | 0 | **0** |
| Oyun terminolojisi · üstünlük iddiası · sevimlileştirme | 0 | **0** |
| Maddeler arası 8+ kelimelik tekrar | 0 | **0** |
| Diakritik düşürme | 0 | **0** |

Yazım disiplini hiç bozulmadı: **on beş partide 43 madde**, parti başına en
fazla üç. Her parti önce `write_entry --measure` ile ölçüldü, bant dışıysa
düzeltildi, sonra işlendi.

---

## 4. Tamamlanan yaratıklar

### Sınıf III · THE SHAPE-CHANGERS (19)

Tengu · Púca · Nahual · Húli jīng · Kumiho · Dokkaebi · Xtabay · Way ·
Anansi · Perī · ʿIfrīt · Tupilaq · Tikbalang · Nhang · Buda · Vârcolac ·
Gufihtar · Skuggabaldur · Masalai

### Sınıf IV · THE WATER-DWELLERS (24)

Apep · Jörmungandr · Yamata-no-Orochi · Kappa · Nāga · Makara ·
Each-uisce · Cipactli · Ahuizotl · Imugi · Taniwha · Moʻo · Şahmeran ·
Iku-Turso · Näkki · Lamia · Thuồng luồng · Phaya Nak · Inkanyamba ·
Amaru · Iara · Mishipeshu · Nykur · Adaro

### Tamamlanan aileler

| Aile | Durum |
|---|---|
| **A · Su atı** | ✅ 4/4 üye yazıldı, açılış yazıldı — **kitabın vitrini** |
| **B · Tilki kadın** | ✅ 2/2, açılış yazıldı |
| **E · Derinlerin yılanı** | 11/15 üye (kalan 4 sınıf V'te), açılış yazıldı |

---

## 5. Tamamlanan sayfalar

`python3 08_BUILD/entry_page.py --measure-all`
Rapor: `06_REPORTS/phase4-typeset-measurement.json`

**88 maddenin tamamı gerçek metinle dizildi.**

| | Faz 3 (45 madde) | **Faz 4 (88 madde)** |
|---|---:|---:|
| İçerik yüksekliği (ortalama) | 2,144 sayfa | **2,143 sayfa** |
| En az / en çok | 2,018 / 2,245 | 2,018 / **2,273** |
| Bant (2,0–3,0) dışı | 0 | **0** |
| Faturalanan sayfa | 135 | **264** (bütçe 264) |
| 112 maddeye izdüşüm | 336 | **336** |

Faz 3'te 45 maddede 2,144, Faz 4'te 88 maddede 2,143 — **iki kat metinde
0,001 sayfa fark.** Model doğrulanmış durumda.

| Kalem | Sayfa |
|---|---:|
| Maddeler (112 × 3,0) | 336 |
| Sınıf ve karşılaştırma açılışları | 28 |
| Ön/arka madde · dizinler · kaynaklar | 72 |
| **Toplam** | **436** |

**Sayfa bütçesi değişmedi.** Kurucu notunun "%5'ten fazla saparsa bildir"
eşiği aşılmadı (sapma %0). 436 sayfalık toplam ve fiyat modeli olduğu gibi
geçerli.

---

## 6. Yazılan kelimeler

| | Kelime |
|---|---:|
| Faz 4 madde metni | 29.770 |
| Faz 4 açılış metni | 2.726 |
| **Faz 4 toplamı** | **32.496** |
| Faz 3'ten devralınan | 33.415 |
| **Kitaptaki toplam metin** | **65.911** |
| Hedef (112 × 700 + açılışlar) | ~82.700 |
| İlerleme | **%80** |

---

## 7. Çapraz referanslar

`python3 08_BUILD/classify.py --check` · `06_REPORTS/crossref-graph.json`

| Ölçü | Değer |
|---|---:|
| Grafikteki bağ (karşılıklı) | 181 |
| Düğüm | 112 |
| Madde başına ortalama | 3,23 |
| Bantta (2–5) | 112/112 |
| Tek yönlü bağ | **0** |
| **Faz 4 maddelerine dokunan bağ** | **94** |
| ikisi de Faz 4'te | 46 |
| **Faz 1–3'e köprü** | **48** |

Faz 4 kendi içine kapanmadı: bağların **yarıdan fazlası** daha önce yazılmış
maddelere gidiyor. Yol haritasının "yeni yazılan maddeler Faz 3'ün
maddelerine bağlanacak" görevi buradan ölçülür.

**Yeni kapı (D42):** `classify.verify_kin_text` her maddenin 6. bölümünü
`spec.crossRefs` ile karşılaştırıyor. İlk koşuda **dört gerçek kusur**
buldu — `huldufolk→gufihtar`, `adze→buda`, `karakoncolos→strigoi`,
`stallu→migoi` — dördü de Faz 3 metninde, dördü de aynı sebepten: bağın
öteki ucu o sırada yazılmamıştı. Dört akraba satırı yeniden yazıldı,
dördü de 50–80 bandında kaldı.

---

## 8. Araştırma kullanımı

| Ölçü | Değer |
|---|---:|
| Faz 4'ün 43 maddesinde kaynak atfı | **168** |
| Benzersiz künye | **83** |
| `primary` | 34 |
| `scholarly` | 57 |
| `reference` | 35 |
| `index` (Thompson) | 42 |
| Tohum motif kodu Faz 1'de düzeltilmiş madde | **16/43** |
| Yaşayan gelenek kapısındaki madde | **12/43** |

### Kayıtlı vaka açığı — D41 uygulandı

Faz 4'ün 43 maddesinin **hiçbirinde** araştırma dosyası hazır bir kayıtlı
vaka taşımıyordu; 43'ünde de alan *"Faz 3'te kaynaktan doğrudan okunacak"*
diyordu. Kurucu kararı D41 gereği **ek araştırma turu yapılmadı ve vaka
uydurulmadı.**

4. bölümler yalnızca dosyadaki `behaviour`, `variants`, `counter` ve
dosyanın işaret ettiği kanonik olaydan yazıldı. Klasik ve kayıtlı
maddelerde kanonik olayın kendisi zaten bir vakadır ve künyesi dosyadadır.
**Faz 4'te tam anlamıyla kaynak-künyeli vaka yazılabilen maddeler:**

| Madde | Vaka | Kaynak |
|---|---|---|
| Yamata-no-Orochi | Sekiz kızın yedisi alınmış; sekiz fıçı sake, sekiz kapılı çit, sekiz sehpa; kuyruktan Kusanagi çıkar | Kojiki I.19 (712) |
| Jörmungandr | Öküz başı yem, Hymir'in teknesi, hattın kesilmesi; Ragnarök'te dokuz adım | Hymiskviða 21–24 · Gylfaginning 48 |
| Anansi | Hikâyelerin Nyame'den satın alınması; bedel dört tehlikeli varlık | Rattray 1930 |
| ʿIfrīt | Süleyman'ın huzurunda tahtı getirmeyi öneren ve geçilen varlık | Kur'an 27:39 |
| Iku-Turso | Yakalanır, sorgulanır, bir daha çıkmayacağına yemin ettirilir | Kalevala runo 42 |
| Şahmeran | Camsab'ın ihaneti; öldürülmesi; etinden şifa | Boratav 1958 |
| Ahuizotl | Ceset gözleri, dişleri ve tırnakları alınmış bulunur | Florentine Codex XI |
| Each-uisce | İskoçya kaydında karaciğerin kıyıya vurması | Croker 1825 II |
| Tikbalang | Gömleği ters giymek; ensedeki üç altın kıl | Ramos 1967, 1971 |
| Phaya Nak | Her yıl ekimde Mekong'dan yükselen ışık topları | Anuman Rajadhon 1968 |

**Uydurma sıfır.** Dört maddede kaynağın taşıdığı ayrıntı, dosyada
olmadığı için yazılmadı ve yazılmadığı söylendi (örnek: Anansi'nin dört
varlığının adları Rattray'in metnindedir; madde adları vermez, kaynağın
taşıdığını söyler).

### Yaşayan gelenek kapısı

12 madde kapı altındaydı ve 12'sinde de kısıtlı malzeme yazılmadı, **ve
yazılmadığı maddede açıkça söylendi**: Anansi (Akan anlatım hakkı) ·
Taniwha (iwi/hapū mülkiyeti, whakapapa) · Moʻo (ʻohana bağı, mele, pule) ·
Tupilaq (yapım yöntemi ve sözler) · Buda (Beta Israel suçlaması) ·
Inkanyamba · Amaru (huaca) · Iara · Mishipeshu (Midewiwin) · Gufihtar ·
Adaro (klan toprak iddiaları) · Masalai (ples masalai adı ve konumu).

Üç madde ayrıca özel editoryal karar gerektirdi:

- **Buda** — anlatılan şey bir yaratık değil bir **suçlamadır**, ve
  suçlama tarihsel olarak Beta Israel'e ve zanaatkâr gruplara yöneltilmiştir.
  Madde suçlamayı yeniden üretmeyi açıkça reddediyor; 5. bölümün tamamını
  Reminick'in toplumsal çözümlemesi taşıyor.
- **Adaro** — Fox (1924, misyoner çerçevesi) ile Scott (2007, Arosi sahası)
  **çelişiyor**. Madde çelişkiyi gösteriyor, birini seçip ötekini
  gizlemiyor. 'Merman' kelimesi kullanılmadı ve kullanılmama gerekçesi
  yazıldı.
- **Taniwha** — 'canavar' kelimesi açıkça reddedildi. Koruyucu/tehlike
  ikiliği bir çelişki değil, iki ayrı **ilişkinin** tarifi.

---

## 9. Oluşturulan dosyalar

| Dosya | Ne |
|---|---|
| `08_BUILD/make_kin_chart.py` | Kin-Images Chart / A+ modülü m3 üreteci (294 satır) |
| `03_APLUS/kin-images-chart.pdf` | Grafik — `.gitignore`'da (D46), ölçüsü depoda |
| `06_REPORTS/kin-images-chart.json` | Grafiğin ölçüsü |
| `06_REPORTS/phase4-typeset-measurement.json` | 88 maddenin prova dizgisi ölçümü |
| `06_REPORTS/FAZ_4_RAPORU.md` | Bu belge |

---

## 10. Değiştirilen dosyalar

`git diff --stat v0.3.0..v0.4.0` — **15 dosya · +2.829 / −346**

| Dosya | Ne değişti |
|---|---|
| `01_SOURCE/book.json` | 43 madde + 5 açılış · **depo dışında** (A1/D29) |
| `01_SOURCE/spec.json` | 43 madde `verified` → `written`; `kinFamilies[].divergenceEn` |
| `01_SOURCE/kin_map.json` | 8 aileye `divergenceEn` (D44) |
| `01_SOURCE/manuscript_metrics.json` | depo dışı metnin ölçüsü (D38) |
| `08_BUILD/classify.py` | `verify_kin_text` kapısı (D42) + İngilizce ayrışma kapısı (D44) |
| `08_BUILD/entry_page.py` | `--measure-all` (D45) |
| `08_BUILD/update_docs.py` | `FOUNDER_DECISIONS` + `check_decision_links` |
| `08_BUILD/qa_all.sh` | "kin-images chart" adımı |
| `.gitignore` | `03_APLUS/*.pdf` (D46) |
| `CHANGELOG.md` | 0.4.0 bloğu · D39–D46 · bayat bağlantı listesi düzeltildi |
| `00_CONTEXT/PROJECT_CONTEXT.md` | § 1, § 11, yeni § 11b ve § 11c |
| `CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md` | Faz 4 ve Faz 5 kurucu kararı blokları · § 5 durum tablosu |
| `BOOK_STATS.md` · `ROADMAP_PROGRESS.md` | otomatik üretildi |

---

## 11. Altyapı değişiklikleri

Faz 4 dört yeni **kapı** ekledi. Hepsi CI'da her push'ta koşuyor.

### ① `classify.verify_kin_text` — 6. bölüm ↔ `spec.crossRefs` (D42)

Yol haritası bunu Faz 4'ün editoryal görevi olarak *göz işiyle* istiyordu.
112 maddede göz kayar. Kapı **iki yönlü** kaçağı arıyor:

- spec'te bağ var, metinde ad yok → dizin ve akraba imge tablosu bağı
  gösterir, okur maddeye gider ve bulamaz;
- metinde ad var, spec'te bağ yok → karşılıklılık kırılmıştır.

Kelime sınırına saygılı arıyor: düz alt dize araması "Devi"yi "Devil"
içinde bulurdu — Faz 3'ün D32 kusuru. **Sınandı:** Kérberos'un satırından
Ḫumbaba silindiğinde kapı yakaladı (çıkış 1), sonra geri alındı.

### ② İngilizce ayrışma cümlesi kapısı (D44)

Kin-Images Chart bir **okur mıknatısıdır** ve okura gider. `kin_map`
ayrışma cümlesini yalnızca Türkçe taşıyordu ve grafik ilk üretimde Türkçe
bastı. Sekiz aileye İngilizcesi eklendi; `classify` eksikse kırmızı
yakıyor. **Proje dilinin pazarlama artefaktına sızması bir daha sessizce
olamaz.**

### ③ `update_docs.check_decision_links`

`ROADMAP_PROGRESS.md` otomatik üretilir ve elle yazılamaz; kurucu kararları
bu yüzden üreticiye girdi ve yalnızca kararın **sonucunu** taşıyor —
gerekçe tek yerde, CHANGELOG'da. Bağın kopmaması kapıya bağlandı: her
karar kimliği CHANGELOG'da aranıyor. **Sınandı:** D41 → D99 yapıldığında
kapı yakaladı.

### ④ `entry_page --measure-all` (D45)

Tek maddelik prova **geometriyi** doğrular; bu **bütçeyi**. Bir maddenin
sığması 112 maddenin 336 sayfaya sığdığı anlamına gelmez, ve sığmayan madde
dağılımın **üst ucunda** olur. Üretilen PDF'ler atılır; depoda yalnızca
sayı kalır (bir prova PDF'i prozadır — A1/D29).

### Ayrıca

- `make_kin_chart.py` — grafik `spec.json` + `kin_map.json`'dan **türetilir**;
  tek bir editoryal cümle içermez. Plaka çerçeveleri doğru oranda (1:1,25)
  çiziliyor ve içine plaka kimliği yazılıyor.
- `qa_all.sh` — "kin-images chart" adımı.

Hat artık **yirmi bir** betik; beşi ölçümün kendisini sınıyor
(`selftest.py` · `plate_selftest.py` · `convert_plates --calibrate` ·
`entry_page --check` · `make_kin_chart --check`).

---

## 12. CI/CD durumu

**Faz 4 boyunca CI hiç kırmızı yanmadı.** On dokuz push, on dokuz yeşil.

`main` üzerindeki son durum (etiket `v0.4.0`):

| İş akışı | Durum | Süre |
|---|---|---|
| `validate` | ✅ success | 40s |
| `build` | ✅ success | 1m10s |
| `plates` | ✅ success | 23s |
| `release` | ✅ success | 41s |

PR #7'nin bütün kontrolleri geçti: depo/belge/varlık bütünlüğü · kalite
kapılarının kendi testi · kapı seviyesi · metin kalite kapıları · üretilen
belgeler bayat mı · veri bütünlüğü · üretim zinciri · DOCX/EPUB/PDF ·
ölçüm kalibrasyonu · prompt kütüphanesi · tutarlılık raporu.

Yerel kapı turu (`./08_BUILD/qa_all.sh`): **BÜTÜN KAPILAR YEŞİL**, kapı
seviyesi `phase3`.

---

## 13. Git commit'leri

**19 commit** (`v0.3.0..v0.4.0`), hepsi ölçümle birlikte:

| # | Commit | Konu |
|---|---|---|
| 1 | `d0565d8` | karar: kurucunun üç kararı — D39, D40, D41 |
| 2 | `9461467` | Tengu, Púca, Nahual (48/112) |
| 3 | `6b64e5d` | Húli jīng, Kumiho, Dokkaebi — aile B tamam (51) |
| 4 | `77c4618` | Xtabay, Way, Anansi (54) |
| 5 | `d802c31` | Perī, ʿIfrīt, Tupilaq (57) |
| 6 | `3eaab2f` | Tikbalang, Nhang, Buda (60) |
| 7 | `eaeac6b` | Vârcolac, Gufihtar, Skuggabaldur (63) |
| 8 | `25fd182` | Masalai, Apep, Kappa — **SINIF III TAMAM** (66) |
| 9 | `d70e761` | Jörmungandr, Makara, Cipactli (69) |
| 10 | `a240b00` | Nāga, Ahuizotl, Each-uisce (72) |
| 11 | `8ecd175` | Yamata-no-Orochi, Moʻo, Şahmeran (75) |
| 12 | `0e8ba50` | Iku-Turso, Lamia, Näkki (78) |
| 13 | `ab09a99` | Imugi, Thuồng luồng, Iara (81) |
| 14 | `b38a58e` | Taniwha, Mishipeshu, Nykur (84) |
| 15 | `4537144` | Phaya Nak, Inkanyamba, Adaro (87) |
| 16 | `9179afb` | Amaru — **SINIF IV TAMAM**, 43/43 (88) |
| 17 | `c0e91e0` | beş açılış — **FAZ 4 YAZIMI TAMAM** |
| 18 | `282731e` | dizgi: ara prova, Kindle projeksiyonu, Kin-Images Chart |
| 19 | `3987333` | belge: Faz 4 kapanış — CHANGELOG v0.4.0, D42–D46 |

Merge: PR #7 → `main` (`7ce2fdf`). Etiket: `v0.4.0`.

> **İki commit iletisinde sayı hatası yapıldı** ve ikisi de sonraki
> commit'te açıkça düzeltildi (`77c4618` ve `3eaab2f`'in sürüklenme
> değerleri). Sebep aynıydı: sayı ölçülmeden yazıldı. Süreç düzeltildi —
> parti döngüsü artık `qa_drift` ve `qa_voice` değerlerini commit'ten
> **önce** basıyor ve ileti o çıktıdan kopyalanıyor.

---

## 14. GitHub Actions sonuçları

| Olay | Sonuç |
|---|---|
| Faz 4 dalına 19 push | ✅ hepsi yeşil |
| PR #7 kontrolleri | ✅ hepsi geçti |
| `main`'e merge sonrası validate · build · plates | ✅ yeşil |
| `v0.4.0` etiketiyle `release` | ✅ yeşil, 41s |
| GitHub Release | ✅ [v0.4.0](https://github.com/emredogan-cloud/codex-bestiarium/releases/tag/v0.4.0) — `github-actions[bot]`, pre-release |

Release notu CHANGELOG'un 0.4.0 bloğundan otomatik üretildi. **Sürüm
otomasyonu doğrulandı.**

---

## 15. Definition of Done kontrol listesi

| # | Ölçüt | Durum |
|---|---|---|
| 1 | Bütün metin kapıları 88 madde üzerinde 0 başarısız | ✅ |
| 2 | 93 plaka ölçüldü; dağılım pilot setle örtüşüyor | ⛔ **ham AI çıktısı kurucudan (D39)** |
| 3 | A, B, E açılışları; A ailesi ekstra editoryal geçişten geçti | ✅ 3/3 |
| 4 | Kin-Images Chart üretildi | ✅ |
| 5 | Kindle dosya boyutu projeksiyonu bütçe içinde | ✅ 3,74 / 6,0 MB |
| 6 | CI yeşil, merge, `v0.4.0` etiketi | ✅ |

**2. madde hakkında.** Faz 2 ve Faz 3'ün aynı maddesiyle aynı sebep, ve
artık bir karar. Hat bekleme durumunda hazır tutuldu ve Faz 4'te iki kez
sınandı: `convert_plates --calibrate` 112 plakalık Kindle projeksiyonunu
ölçtü (3,74 MB), `make_kin_chart` 48 plaka çerçevesini doğru oranda çizdi.
Plakalar geldiğinde aynı komutlar çerçeveleri doldurur; **yerleşim, ölçek
ve sayfa sayısı değişmez.**

---

## 16. Sürüklenme izleme sonuçları

`python3 08_BUILD/qa_drift.py -v` · `06_REPORTS/qa-drift.json`

Kurucu kararı D40: **düzeltme yok, ölçüm var.** Faz 4 on beş kez ölçtü ve
her ölçüm bir commit iletisine geçti.

```
Faz 3 kapanışı           %21,0   eğim +0,355/madde
 ↓
%15,0 → 13,2 → 8,7 → 9,8 → 9,1 → 10,5 → 10,4 → 12,0
      → 14,1 → 16,5 → 13,4 → 11,9 → 10,3 → 10,5
 ↓
Faz 4 kapanışı            %8,9   eğim +0,082/madde
```

| Ölçü | Faz 3 kapanışı | **Faz 4 kapanışı** |
|---|---:|---:|
| En sık 50 kelimede eğim | %+21,0 (uyarı) | **%+8,9** ✅ |
| eğim/madde | +0,355 | **+0,082** |
| Cümle uzunluğu ritmi | %+8,9 | **%+2,7** |
| Sözcük dağarcığı zenginliği | %+6,4 | %+5,9 |
| Kitap geneli cümle ortalaması | 16,7 | 16,9 |

### Düşüş nereden geldi

**Bir düzeltmeden gelmedi.** Tek bir Faz 3 maddesi üslup için açılmadı.
Sınıf III ve IV maddeleri somut bir mekanizma anlatıyor — doğum gününe
bağlı hayvan, ters toynak, baştaki su dolu çanak, kuyruğun ucundaki el,
ekimde ırmaktan yükselen ışık, sekiz kapılı çit — ve somut mekanizma
çözümleyici dağarcığı seyreltiyor.

Ortadaki tırmanış (%8,7 → %16,5) de kaydedildi ve gizlenmedi. **D40'ın
istediği tam olarak buydu: düzeltme değil belgeleme.**

### Faz 5 uyumlama geçişine devredilen üç hedef

`qa_echo` Faz 4'te **on dokuz** kalıplaşma yakaladı. Kapı yalnızca birebir
sekiz kelimelik çakışmayı görür; geçişin işi görmediğidir.

| # | Küme | Kanıt |
|---|---|---|
| ① | **Yazarın çözümleyici kalıpları** | *"What the tradition supplies is not…"* metinde **sekiz** yerde. Ayrıca *"almost every creature in this book is a…"*, *"that is the whole of the account"*, *"is the mistake this entry exists to prevent"*. Sürüklenmenin yükselen sözcük listesi aynı yeri gösteriyor: *about · nothing · creature · person · rather · tradition* — **kitabın kendine göndermesi**. |
| ② | **Yaşayan gelenek kapısının boilerplate'e dönmesi** | Üç kez yakalandı: Tupilaq ↔ Repun Kamuy, Masalai ↔ Taniwha, Inkanyamba ↔ Amaru. Kısıt cümlesi kalıplaşırsa okur onu atlamayı öğrenir. **Etik kapı her maddede yeniden kurulmak zorunda.** |
| ③ | **Karşılıklı çapraz referansın aynı cümleyle kurulması** | Nahual ↔ Way, Taniwha ↔ Inkanyamba. Faz 3'ün Lámia ↔ Strix kusuruyla aynı sınıf. |

Ayrıca iki tekil bulgu:

- **Künye ekosu proza içinde.** Skuggabaldur ile Nykur aynı sekiz kelimeyle
  açılıyordu (*"Jón Árnason collected it for the Íslenzkar þjóðsögur"*).
  D34 kaynak notunu muaf tutar ve gerekçesi doğrudur; **aynı muafiyet 2.
  bölüm için geçerli değildir.** Künye korundu, cümle yeniden kuruldu.
- **Açılışlar on iki kusur üretti** ve hepsi tek sınıftandı: açılış,
  maddeyi kendi cümleleriyle özetliyordu. Bir açılışın işi maddeleri
  tekrarlamak değil aralarındaki farkı kurmaktır; birebir tekrar eden
  iki sayfa boşa gider.

---

## 17. Uygulanan kurucu kararları

### D39 · İllüstrasyon

> Ham AI plaka üretimi kurucunun sorumluluğudur ve Faz 5'ten önce
> tamamlanacaktır. Faz 4 bu yüzden bloklanmaz; hat bekleme durumunda hazır
> tutulur.

**Uygulandı.** Faz 4 metin işi plakaya bağlı olmadan tamamlandı. Hat iki
kez sınandı: `convert_plates --calibrate` (112 plakalık Kindle
projeksiyonu 3,74 MB) ve `make_kin_chart` (48 çerçeve, doğru oranda,
plaka kimliğiyle etiketli). Plakaya bağlı DoD maddesi açık kaldı ve sebebi
raporda yazılı.

### D40 · Üslup sürüklenmesi

> Mevcut %21 Faz 4'te düzeltilmez, ölçülür. Faz 3 metni yeniden yazılmaz.
> Düzeltme Faz 5'in editoryal geçişine aittir.

**Uygulandı.** On beş ölçüm, on beş commit iletisi, sıfır Faz 3 üslup
müdahalesi. Düzeltme yol haritasının Faz 5 bölümüne açıkça yazıldı
(§ ① ve DoD 4b).

**Bir istisna gibi görünen ama olmayan durum (D43):** Yeni kapı dört Faz 3
maddesinde **kırık çapraz referans** buldu ve bunlar düzeltildi. D40 üslup
sürüklenmesini erteler; kırık bir çapraz referans üslup değil **doğruluk**
kusurudur ve "kalite geriye gidemez" onu düzeltmeyi emreder. Ayrım rapora
ve CHANGELOG'a yazıldı.

### D41 · Kayıtlı vaka açığı

> Ek tarihsel araştırma turu yapılmaz. Davranış temelli editoryal yaklaşım
> sürer. Vaka uydurulmaz.

**Uygulandı.** 43 maddenin hiçbirinde hazır vaka yoktu; hiçbiri
uydurulmadı. On maddede kaynak-künyeli kanonik olay yazılabildi (§ 8).
Dört maddede kaynağın taşıdığı ama dosyada olmayan ayrıntı **yazılmadı ve
yazılmadığı söylendi.** Gelecek baskı notu yol haritası Faz 5 § ②'de.

---

## 18. Kalan riskler

| # | Risk | Durum |
|---|---|---|
| 1 | **Ham plaka seti** — hattın dışındaki tek girdi | ⚠ D39 · kurucu Faz 5'ten önce üretecek. 88 maddenin plakası buna bağlı. |
| 2 | **Üslup sürüklenmesi** — %8,9, bandın altında ama sıfır değil | ⚠ D40 · Faz 5 uyumlama geçişi üç somut hedefle başlıyor (§ 16) |
| 3 | **Yaşayan gelenek cümlesinin kalıplaşması** | ⚠ üç kez yakalandı; etik kapının okunmayı bırakması gerçek bir risk |
| 4 | Tikbalang'ın madde içi tekrarı | ⚠ `qa_echo` madde İÇİ öbek tekrarını aramıyor; D40 gereği açılmadı, Faz 5'e not |
| 5 | Dış hat kalınlığı tahmincisi kalibre edilemedi | ⚠ gerçek plakalarda yeniden değerlendirilecek (Faz 2 § 6b②) |
| 6 | Kindle Translate uygunluğu belirsiz | ⚠ 112 plaka kapıyı kapatabilir; finansal modele dahil değil |
| 7 | Kamu malı yanlış sınıflandırma riski | ⚠ Cilt 1'den devralındı; özgün Giriş/Sonsöz savunma olarak Faz 5'te yazılacak |
| 8 | Vektör temizlik dışarıya verilecek mi (A3) | ⏳ ham plaka girdisine bağlı |
| 9 | Ana dil editörü henüz bulunmadı | ⏳ kurucu notu: "Faz 4 biterken aramaya başlayın" — **şimdi** |

**Takvim riski (Risk 4) gerçekleşmedi.** Yol haritası haftada 12 madde
öngörüyordu; Faz 4'ün 43 maddesi tek oturumda, on beş partide, kapı
disiplini bozulmadan yazıldı.

---

## 19. BOOK_STATS özeti

`python3 08_BUILD/update_docs.py` — otomatik üretildi

| Ölçü | Şu an | Hedef | İlerleme |
|---|---:|---:|---|
| Yaratık kaydı | 112 | 112 | %100 |
| Gelenek | 40 | 40 | %100 |
| İki bağımsız kaynaklı madde | 112 | 112 | %100 |
| Doğrulanmış motif kodu | 112 | 112 | %100 |
| Çapraz referansı olan madde | 112 | 112 | %100 |
| **Yazılmış madde** | **88** | 112 | **%79** |
| **Kelime (yazılmış)** | **~66.000** | 78.400 | **%84** |
| Normalize plaka | 0 | 112 | %0 ⚠ D39 |

### Durum dağılımı

| Durum | Madde | Pay |
|---|---:|---:|
| `draft` | 0 | %0 |
| `verified` | 24 | %21 |
| `written` | **88** | **%79** |
| `edited` · `final` | 0 | %0 |

### Sınıf dağılımı

| # | Sınıf | Madde | Yazıldı |
|---|---|---:|---|
| I | THE GUARDIANS | 18 | ✅ 18/18 |
| II | THE DEVOURERS | 27 | ✅ 27/27 |
| III | THE SHAPE-CHANGERS | 19 | ✅ **19/19** |
| IV | THE WATER-DWELLERS | 24 | ✅ **24/24** |
| V | SKY AND STORM | 16 | 0/16 |
| VI | THE RESTLESS DEAD | 8 | 0/8 |

---

## 20. ROADMAP_PROGRESS özeti

| Faz | Başlık | İlerleme | Etiket |
|---:|---|---|---|
| 1 | Altyapı, Araştırma ve Kapsam Kilidi | 112/112 (%100) | `v0.1.0` |
| 2 | Tasnif, Veri Modeli ve Pilot Plaka Seti | 112/112 (%100) | `v0.2.0` |
| 3 | Çekirdek Yazım · Bekçiler ve Yutucular | 45/45 (%100) | `v0.3.0` |
| **4** | **Genişleme · Şekil Değiştirenler ve Su Sakinleri** | **43/43 (%100)** | **`v0.4.0`** |
| 5 | Tamamlama, İllüstrasyon ve Editoryal İnceleme | 0/24 (%0) | `v0.5.0` |
| 6 | Üretim, KDP ve Lansman | 0/4 (%0) | `v1.0.0` |

Belge ayrıca **Yürürlükteki kurucu kararları** bölümünü taşıyor (D39–D41);
gerekçeler CHANGELOG'da, sonuçlar burada, bağ kapıya bağlı.

---

## 21. PROJECT_CONTEXT güncellemeleri

| Bölüm | Ne değişti |
|---|---|
| § 1 | Faz 4'e güncellendi; Faz 4 DoD tablosu eklendi |
| § 2 | Hacim satırı: 436 sayfa **88 maddeyle yeniden doğrulandı** |
| § 10 | Bilinen sorun 5 (plaka) D39'a bağlandı |
| **§ 11** | "Sıradaki adım" Faz 5'e çevrildi; Faz 5'e devredilen dört şey |
| **§ 11b** | *(Faz 4 başında eklendi)* Kurucu kararları A/B/C → D39–D41 |
| **§ 11c** | *(yeni)* Sürüklenme nereden geliyor + Faz 5'in üç somut hedefi |
| § 12 | Kayıtlı vaka açığı: kurucu (1)'i seçti — D41 |

---

## 22. CHANGELOG özeti

`[0.4.0] — 2026-08-07` bloğu şunları taşıyor:

- **Ölçülenler** tablosu (Faz 4 · kitap)
- **Üslup sürüklenmesi** — on altı ölçümlük dizi, D40 gerekçesiyle
- **Prova dizgisi** — Faz 3 ile Faz 4 karşılaştırması
- **Kararlar D42–D46**
- **`qa_echo` — on dokuz kusur**, üç kümeye ayrılmış dökümü
- **Eklenenler** listesi

Ayrıca `[Yayımlanmamış]` bloğundaki **kurucu kararları D39–D41** Faz 4'ün
başında eklenmişti ve yerinde duruyor.

**Bayat bağlantı listesi düzeltildi:** `v0.3.0` hiç eklenmemişti ve
`[Yayımlanmamış]` hâlâ `v0.2.1`'e karşılaştırıyordu.

---

## 23. Faz 5 hazırlık değerlendirmesi

### Hazır olanlar

| | |
|---|---|
| ✅ | **88/112 madde yazıldı**, hepsi kapılardan geçti |
| ✅ | Sesin ve ritmin ölçüsü sabit: cümle ortalaması 16,9, bant dışı madde 0 |
| ✅ | Sayfa bütçesi 88 maddeyle doğrulandı — 436, değişmedi |
| ✅ | Kalan 24 maddenin araştırma dosyaları hazır (Faz 1'de tamamlandı) |
| ✅ | D ailesi açılış planı `KIN_OPENINGS.md`'de kilitli |
| ✅ | Kapı hattı 21 betik; beşi ölçümün kendisini sınıyor |
| ✅ | CI yeşil, `v0.4.0` etiketli, release yayımlandı |
| ✅ | Faz 5'in iki zorunluluğu yol haritasına yazıldı ve DoD'ye bağlandı |

### Faz 5 başlamadan gereken

| # | Gereklilik | Kim | Aciliyet |
|---|---|---|---|
| 1 | **Ham AI plaka seti** — 112 plaka, `07_ASSETS/plates_raw/` | kurucu | **yüksek** — D39 bunu Faz 5'ten önce şart koşuyor |
| 2 | **Ana dil editörü** (Geçiş 3, 10 saat, dış kaynak) | kurucu | **yüksek** — yol haritası "Faz 4 biterken aramaya başlayın" diyor; doğru kişiyi bulmak haftalar alabilir |
| 3 | Faz 5 başlama onayı | kurucu | — |

### Faz 5'in yükü

24 madde (sınıf V: 16, sınıf VI: 8) · D karşılaştırma açılışı · sınıf V ve
VI açılışları · Giriş (8 s) · "Bu kitap nasıl okunur" (6 s) · Sonsöz (4 s) ·
arka madde · **üç editoryal geçiş** (düşman olgu denetimi 30 sa, satır
editörlüğü + **üslup uyumlama** 20 sa, ana dil geçişi 10 sa) · son 24 plaka ·
tam kitap prova dizgisi.

Yol haritası bu fazı **99 saat** olarak modelliyor ve en ağır faz odur.

### Değerlendirme

**Faz 5 teknik olarak hazırdır.** Yazım hattı, kapılar, dizgi ölçümü,
grafik üretimi ve sürüm otomasyonu 88 maddede sınandı ve çalışıyor.
Metnin kalan %21'i aynı disiplinle yazılabilir.

**İki dış girdi kritik yolda:** ham plakalar (D39) ve ana dil editörü.
İkincisi yalnızca Geçiş 3'ü etkiler; birincisi Faz 5'in illüstrasyon
işinin tamamını ve Faz 6'nın üretimini bekletir.

---

**FAZ 4 TAMAMLANDI.**
Sıradaki: **Faz 5 · Tamamlama** — kurucu onayı bekleniyor.

*Bu rapor `06_REPORTS/FAZ_4_RAPORU.md` olarak depoda durur.*
