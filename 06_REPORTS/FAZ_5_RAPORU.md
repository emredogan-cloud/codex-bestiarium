# FAZ 5 · TAMAMLAMA — NİHAİ RAPOR

> **Durum: TAMAMLANDI.** 8 Ağustos 2026 · etiket `v0.5.0` ·
> merge PR #8 → `main` (`fbf052f`) · sürüm doğrulaması yeşil.
>
> Buradaki her sayı ya bir dosyadan ölçülmüştür ya da bir kod satırından
> türetilmiştir. Ölçülmemiş hiçbir rakam yoktur; ölçülemeyen her şey
> **UYARI**, **BLOKE** veya **İNSAN EYLEMİ GEREKİYOR** olarak
> işaretlenmiştir ve tamamlanmış gibi gösterilmemiştir.

---

## 1. Yönetici özeti

**Kitabın metni bitti.** 112/112 madde, 6/6 sınıf açılışı, 8/8
karşılaştırma açılışı, 7/7 ön ve arka madde bölümü, 112/112 normalize
plaka. Toplam **88.960 kelime**.

Faz 5'in beş işi vardı ve beşi de kapandı: son 24 maddeyi yazmak, ham
plaka setini hatta sokmak, bütün ön ve arka maddeyi yazmak, üç editoryal
geçişi yapmak ve sayfa bütçesini tam kitapla doğrulamak.

**① Sayfa bütçesi kitabın tamamı dizilerek yeniden kuruldu: 436, sapma
sıfır.** Faz 2 provadan tahmin etmiş, Faz 4 88 maddeyle doğrulamıştı. Faz
5 bileşen bileşen topladı — maddeler 336 (ölçüldü), açılışlar 28, ön/arka
madde 26 (ölçüldü), yapısal 14, dizinler 22, kaynaklar 10. Sapma sıfır
olduğu için BRIEF § 4'ün fiyat ve telif tablosu **değişmedi**.

**② Düşman olgu denetimi on üç GERÇEK kusur buldu.** Beş maddede prozanın
gösterdiği künye kaynak kaydında yoktu. Bir maddede yazarın başka bir
kitabı gösteriliyordu. Bir künye dört cilt tam metin taramasıyla çürüdü.
Bir kaynak yanlış figüre çıpalanmıştı. Üç yerde akraba ailesinin sayısı
yanlıştı. Hepsi düzeltildi ve düzeltmelerin tamamı deftere yazıldı.

**③ D40 kapatıldı: üslup sürüklenmesi %8,9 → %1,6.** Faz 4 raporunun
adıyla devrettiği üç kalıp kümesi 46/28/25 maddeden 1/0/1'e indi. Kısıt
cümlesi 19'dan 4'e. Bu, sayı düşürme egzersizi değildi: kalan 25 şablonun
tamamı sıradan İngilizcedir ve madde içi 74 tekrarın yalnızca üçü
düzeltildi, çünkü geri kalanı **kasıtlı koşutluktur**.

**④ Kayıtlı vaka turu iki vaka ekledi ve iki künyeyi çürüttü.** Aynı
yöntem hem ekliyor hem siliyor. Yalnızca eklemeyi raporlayan bir kitap o
yöntemi kullanmıyor demektir; bu rapor ikisini de yazıyor.

**⑤ Beş kez CI kırmızı yandı ve beşi de gerçek kusurdu.** Hiçbiri
"flaky" değildi, hiçbiri eşik düşürerek kapatılmadı. Sonuncusu — sürüm
iş akışının kırmızısı — projenin en eski sözleşmesinin üç yerde
çiğnendiğini gösterdi.

**Hiçbir kapı gevşetilmedi.** Beş kez kelime bandı bir düzeltmeyi geri
itti ve beş kez cümle banda uyduruldu.

---

## 2. Yol haritasının Faz 5 çıktıları

| # | Çıktı | Durum |
|---|---|---|
| 1 | Sınıf V · SKY AND STORM | ✅ **16/16** |
| 2 | Sınıf VI · THE RESTLESS DEAD | ✅ **8/8** |
| 3 | Karşılaştırma açılışı D · Fırtına kuşu | ✅ 568 kelime |
| 4 | Giriş (8 s) · Nasıl okunur (6 s) · Sonsöz (4 s) | ✅ 7/13 sayfa ölçüldü, slot içinde |
| 5 | Arka madde: yazar · seri · yorum · kolofon | ✅ 4/4 |
| 6 | Son plakalar (toplam 112) | ✅ **112/112** — D39 kapandı |
| 7 | Düşman olgu denetimi itiraz listesi | ✅ `factcheck.py` · 13 kusur |
| 8 | Bütün düzeltmeler programatik kayıtta | ✅ `edits.json` · 146 kayıt |
| 9 | `book-edited.json` — dizgiye giren metin | ✅ üretiliyor, kapılar onu denetliyor |

Yol haritası Faz 5'i 27 madde olarak planlamıştı (sınıf V 17, sınıf VI
10). Faz 2'nin sınıf dağılımı uzlaştırması sonrası gerçek sayı **24**'tür
(16 + 8) ve toplam yine 112'dir. Bu bir eksiklik değil, Faz 2'de
kilitlenmiş bir dağılımdır.

---

## 3. Yazım istatistikleri

| Ölçü | Sınıf V | Sınıf VI | Faz 5 |
|---|---:|---:|---:|
| Madde | 16 | 8 | **24** |
| Kelime | 10.449 | 5.316 | **15.765** |
| Madde ortalaması | 653,1 | 664,5 | **656,9** |
| En kısa | 621 | 628 | 621 |
| En uzun | 682 | 715 | 715 |
| Bant dışı | 0 | 0 | **0** |

Bant 620–790. Faz 5 maddeleri bandın alt yarısında toplandı ve bu
kasıtlıdır: son iki sınıfın kaynak temeli daha ince, ve **kaydın
söylemediği yazılmaz**.

| Ölçü | Değer |
|---|---:|
| 112 maddenin toplamı | 75.836 kelime |
| Madde ortalaması | 677,1 |
| Sınıf açılışları (6) | 3.123 |
| Karşılaştırma açılışları (8) | 4.288 |
| Ön ve arka madde (7) | 5.713 |
| **Kitap toplamı** | **88.960** |

Faz 5'te 21 gelenekten madde yazıldı.

---

## 4. Ön ve arka madde — yeni proza

| Bölüm | Kelime | Sayfa (ölçüldü) | Slot |
|---|---:|---:|---:|
| `introduction` — Forty Faces of One Fear | 2.484 | 7 | 8 |
| `how-to-read` — How to Read This Book | 1.391 | 5 | 6 |
| `epilogue` — What Is Not Here | 1.029 | 4 | 4 |
| `about-author` | 177 | 1 | 2 |
| `series` | 197 | 1 | 2 |
| `review-call` | 170 | 1 | 2 |
| `colophon` | 261 | 1 | 2 |
| **Toplam** | **5.709** | **20** | **26** |

Aradaki altı sayfa israf değildir: her bölüm recto'dan başlar ve tek
sayfada biten bölüm arkasına boş sayfa bırakır.

**Giriş** editoryal tez olarak yazıldı, madde olarak değil: yakınsama
olgusu, işleve göre tasnifin gerekçesi ve bedeli, sekiz akraba imge, iki
kaynak kuralı, kısıtlı malzeme kuralının neye mal olduğu, "ne değildir"
listesi ve nasıl itiraz edileceği.

**Sonsöz** kurucunun istediği dört konuyu savunmacı olmayan bir dille
taşıyor: Aborjin geleneklerinin dışarıda bırakılması (bir eksik değil, bir
standart beyanı), kitabın içindeki kısıt kuralı, kaynaklanamayan sekiz
madde ve kütüphane erişimi, kayıtlı vaka açığı ve yeni turun iki vaka
eklerken iki künyeyi çürüttüğü.

---

## 5. Sayfa bütçesi — TAM KİTAP ölçüldü

Bileşen tablosu `CHANGELOG.md` → 0.5.0 → *"Sayfa bütçesi"* başlığında
duruyor ve burada tekrarlanmıyor. Özeti tek satırda:

> ölçülen madde sayfası **336** + açılış **28** + ön/arka madde **26**
> + yapısal ön madde **14** + dizin **22** + kaynak **10** = **436**,
> bütçe **436**, **fark 0**.

Madde içeriği dağılımı (112 maddenin tamamı dizildi):
en az **2,018** · ortalama **2,134** · en çok **2,273** sayfa.
Kabul bandı 2,0–3,0. Hiçbir madde dördüncü sayfaya taşmıyor.

**Fiyat ve telif tablosu değişmedi.** BRIEF § 4'ün bütün rakamları 436
sayfa üzerinden hesaplanmıştı; sapma sıfır olduğu için ciltsiz 24,99 $ ·
birim telif 8,76 $ · başabaş ACOS %41,6 aynen geçerli.

---

## 6. Plakalar — D39 kapandı

Kurucu 112 ham PNG'yi teslim etti ve set **bağımsız olarak doğrulandı**:
dosya sayısı, adlar, boyutlar, bütünlük, kopya, eksik kimlik ve 112
yaratık kaydıyla eşleme. Dosya adlarının doğru olduğu **varsayılmadı**.

| Ölçü | Değer |
|---|---:|
| Ham dosya | 112 |
| Maddeye eşlenen | **112 / 112** |
| Normalize edilen | 112 |
| Tutarlılık kapısından geçen | **112 / 112** |
| Format bütçesi | 7/7 geçti |

Ham dosyalar **değiştirilmedi**; `07_ASSETS/aplus_raw/` girdi olarak
dokunulmaz tutuldu. Kanonik olmayan dosya adları manifestoda eşlendi,
diskte yeniden adlandırılmadı.

Üç plaka kararı bu fazda alındı ve gerekçeleri CHANGELOG'da: D47 (üç
tarama ölçümü kapı olmaktan çıktı, yerine ton dağılımı kapısı), D48
(kapsama hedefi şartnamenin geometrisinden türetildi), D49 (Kindle ve web
iki tonlu — 24,8 MB → 4,7 MB).

---

## 7. Kayıtlı vaka turu (D50)

Kurucu C kararını Faz 5'te güncelledi: kısa ve hedefli bir tur serbest,
kaynak hızlıca bulunmazsa durulur. Sınır önceden kondu ve uygulandı.

| Madde | Sonuç |
|---|---|
| **Kappa** | ✅ *Tōno monogatari* 58, Japonca özgün tam metinden: adı geçen ırmak (小烏瀬川), gölet (姥子淵), hane (新屋), ve bir **köy meclisi kararı** — öldürmek mi bağışlamak mı |
| **Koropokkuru** | ✅ Batchelor yaprağı **kendisi ölçmüş**: 4 kadem 1 parmak eninde, sapı 5 kademden uzun |
| **Each-uisce** | ⛔ Croker künyesi **çürüdü** — dört cilt tarandı, yaratık hiçbirinde geçmiyor |
| **Pontianak** | ⛔ Skeat **yanlış çıpalanmış** — onun pontianak'ı langsuir'ın ölü doğan çocuğu |
| Tokoloshe · Strigoi | — nüsha hızlıca bulunamadı → **arama durduruldu** |

**Turun asıl getirisi vaka değil, kusur oldu.** Altı maddede iki çürük
atıf — bu oran, düşman olgu denetiminin bu fazın en değerli işi olduğunu
söyledi ve o geçiş buradan başlatıldı.

Değişmeyen kural: vaka, tarih, tanık, sefer, alıntı, künye uydurulmaz;
folklor tarihsel olguya çevrilmez.

---

## 8. Geçiş 1 · Düşman olgu denetimi

`08_BUILD/factcheck.py` — prozanın kaydın ötesine geçtiği yeri arar:
dayanaksız tarih, atıf konumunda kayıtta olmayan soyadı, maddenin
listesinde olmayan motif kodu, aileyle ayrışan sayı.

**İlk koşu 67 itiraz verdi ve 54'ü ARACIN kusuruydu.** Araç düzeltildi,
metin değil:

| Araç kusuru | Nasıl düzeltildi |
|---|---|
| Künyeler aralığı kısaltıyor ("1855–63"), proza açıyor | kapalı aralık genişletmesi |
| "He published…", "Only published material…" atıf sanılıyordu | zamir ve belirteç listesi |
| "Philippi's" iyelik ekiyle künyeden ayrılıyordu | ek soyuluyor |
| "the two entries" aile boyu iddiası sanılıyordu | yalnızca "other" veya akraba bağlamı sayılıyor |
| Tohum kodu düzeltmeleri spec'e taşınmıyordu | `research_gen` artık `motifNote` ve `motifChanged` taşıyor — **bu bir araç kusuru değil, gerçek bir KAYIT eksiğiydi** |

**Kalan 13 itirazın hepsi gerçekti:**

| Sınıf | Sayı |
|---|---:|
| Kayıtta olmayan künye (Rose, beş maddede) | 5 |
| Çürüyen kaynak atfı (Croker) | 2 |
| Aile sayısıyla ayrışma (C ailesi 14 üyeli, proza "sekiz" diyordu) | 3 |
| Yanlış künye (Hammond-Tooke'un başka kitabı) | 1 |
| Kaynak yanlış çıpalanmış (Skeat) | 1 |
| Ayrıntı kaynakla ayrışıyor (delik ensede) | 1 |

**Bir istisna yazıldı:** `lemures/Ovid`. Kayıt Türkçe ve "Ovidius"
künyeliyor, kitap İngilizce ve "Ovid" yazıyor. Bu bir kaynak kusuru değil
dil sınırıdır. İstisna dosyası **gerekçesiz satır kabul etmiyor**.

---

## 9. Geçiş 2 · Satır editörlüğü ve üslup uyumlama (D40)

Faz 4 raporunun § 16'da adıyla devrettiği üç küme ve ölçülen düşüş:

| Ölçülen küme | Düşüş |
|---|---|
| Yazarın çözümleyici kalıpları | 46 maddeden **1**'e |
| Çapraz referans kalıbı | 28'den **0**'a |
| "That is the whole of…" | 25'ten **1**'e |
| Yaşayan gelenek kısıt cümlesi | 19'dan **4**'e |
| 5–7 kelimelik şablon | 54'ten **25**'e |
| Madde içi tekrar | 79'dan **74**'e |

**Kısıt cümlesi en önemlisiydi.** Sekiz madde "Only published material is
used here" ile açılıyordu. Kalıplaşan bir etik kapıyı okur atlamayı
öğrenir. Her cümle artık o geleneğin kendi kısıtını adıyla söylüyor:
iyomante, inaw, yoik, siida, angakkuq, ʻohana, masalai yeri.

**Çapraz referans kalıbı sıfırlandı.** Yirmi sekiz akraba satırı üç
kalıptan biriyle kuruluyordu ve karşılıklı çiftler birbirinin aynadaki
hâliydi: Kappa↔Tengu, Xtabay↔Way, Nāga↔Makara, Sīmurgh↔Perī,
Zmey↔Rusalka, Iku-Turso↔Näkki, Kumiho↔Dokkaebi.

**Ne yapılmadı ve neden.** Kalan 25 şablonun tamamı sıradan İngilizcedir
("at the other end of", "and it is the only"). Madde içi 74 tekrarın
yalnızca üçü düzeltildi: Qilin'in tek cümledeki iki *will not tread on*'u,
Aralez'in köpek çağrışımı, Huldufólk'un *gone/alive* karşıtlığı ve
Ḫumbaba'nın *at a distance* yankısı **kasıtlı koşutluktur**. Bunları
bozmak, kurucunun açıkça yasakladığı şey olurdu: *"sayıyı yapay olarak
küçültme."*

---

## 10. Geçiş 3 · Ana dil editörü — İNSAN EYLEMİ GEREKİYOR

> **DURUM: PAKET HAZIR, İŞ YAPILMADI.** Bu bir tamamlanma değildir ve
> öyle gösterilmiyor.

Kurucu emri: insan editör tek izinli dış bağımlılıktır ve **beklenmez**.
Faz 5 beklemedi; paketi üretti ve devam etti.

`08_BUILD/editor_pack.py` üç dosya üretiyor: DOCX (1,5 satır aralığı),
Markdown ve `EDITOR_BRIEF.md`. Üçü de proza ve depo dışında.

**Brifing** işin ne olduğunu (ses doğallığı), neyin sabit olduğunu (bölüm
sırası, kelime bantları, olgular, diakritikler) ve hattın mekanik olarak
neyi kırmızı yakacağını söylüyor. Yasak kalıp listeleri `bestiarium.py`den
türetiliyor — elle yazılan bir brifing bir sonraki turda bayatlar.

**İşaretli bölümler ölçümden türetiliyor**, 784 bölümün 293'ü:

| Ölçüt | Bölüm |
|---|---:|
| Defterin dokunduğu | 130 |
| Ritim aykırısı (dağılımın en alt/üst %5'i) | 111 |
| Bant kenarı (%4 içinde) | 59 |
| Yaşayan gelenek kısıtı | 20 |
| Diakritik yoğun | 14 |
| Yeni proza (ön/arka madde) | 7 |

İlk deneme 363 işaretledi — %46'lık bir öncelik listesi öncelik listesi
değildir. İki eşik **ölçülerek** daraltıldı: blok cümle ortalamasının
dağılımına bakıldı (560 blok, ortalama 14,9; %5 → 12,3, %95 → 17,8) ve
13–19 aralığının dağılımın ortasını işaretlediği görüldü.

---

## 11. Editoryal düzeltme defteri

**146 düzeltme · 81 madde · kelime farkı +5.** Elle düzenleme yapılmadı.

| Kategori | Sayı |
|---|---:|
| Üslup — yazarın çözümleyici kalıpları | 55 |
| Üslup — çapraz referans kalıbı kırıldı | 28 |
| Üslup — "that is the whole of…" | 27 |
| Üslup — kısıt cümlesi boilerplate'ten çıkarıldı | 15 |
| Olgu — kayıtta olmayan künye | 5 |
| Sayı — aile boyutlarıyla ayrışma | 3 |
| Sayı — akraba ailesiyle ayrışma | 3 |
| Üslup — madde içi tekrar | 3 |
| Olgu — kaynak atfı çürüdü | 2 |
| Olgu — yanlış künye · yanlış çıpalanmış · atıf kesinliği · ayrıntı ayrışması | 4 |
| Terminoloji — belirsizlik | 1 |

`before` alanı bir **sınamadır**: metin defterden sonra değiştiyse
eşleşme tutmaz ve kapı kırmızı yanar. Defter ham metni okur, kendi
ürettiğini değil. `load_book()` düzeltilmiş metni tercih ettiği için
**bütün kapılar düzeltilmiş metni denetliyor**.

---

## 12. Beş kez bant düzeltmeyi geri itti

| Madde | Ne oldu | Nasıl çözüldü |
|---|---|---|
| `nakki/kin` | 81 kelime, bant 50–80 | cümle kısaltıldı |
| `abiku/looks` | 109, bant 110–160 | cümle kaydın sessizliğini söyleyecek biçimde uzatıldı |
| `simurgh/looks` | 108 | uzatıldı |
| `tokoloshe/looks` | 109 | uzatıldı |
| `impundulu/sources` | 28, bant 30–50 | kayıtta duran ve anılmayan Berglund eklendi |

Beşinde de **bant değiştirilmedi**. Sonuncusu ayrıca bir iyileşme: bant,
eksik künyeyle değil gerçek künyeyle dolduruldu.

---

## 13. Oluşturulan dosyalar

| Dosya | Ne yapar |
|---|---|
| `08_BUILD/plate_manifest.py` | yaratık → plaka → ham dosya sözleşmesi |
| `08_BUILD/matter_page.py` | ön/arka madde dizgisi ve sayfa ölçümü |
| `08_BUILD/factcheck.py` | düşman olgu denetimi |
| `08_BUILD/edits.py` | editoryal düzeltme defteri |
| `08_BUILD/qa_style.py` | üslup uyumlama ölçümü |
| `08_BUILD/editor_pack.py` | ana dil editörü teslim paketi |
| `01_SOURCE/plate_manifest.json` | eşleme sözleşmesi (depoda) |
| `01_SOURCE/matter_measurement.json` | ön/arka madde ölçüsü (depoda) |
| `01_SOURCE/edits_summary.json` | defterin ölçüsü (depoda) |
| `01_SOURCE/editor_pack.json` | teslim paketinin ölçüsü (depoda) |
| `01_SOURCE/factcheck_allow.json` | gerekçeli istisnalar (depoda) |

Depoda kalan beş JSON'un hiçbiri proza içermez.

---

## 14. Değiştirilen dosyalar

25 dosya. Öne çıkanlar:

- `bestiarium.py` — `MATTER_SECTIONS`, `EDITOR_COPY_STEM`, plaka kapsama hedefi
- `plates.py` — normalize sırası, güvenli kenar, ton kapısı, D47/D48
- `convert_plates.py` — iki tonlu Kindle/web (D49)
- `textutil.py` — paragraf sonu artık cümle sonu (D56)
- `research_gen.py` — `motifNote` ve `motifChanged` spec'e taşınıyor
- `update_docs.py` — ön/arka madde tablosu, Faz 6 sayımı düzeltildi (D55)
- `qa_all.sh` — altı yeni adım, `soft_run`, sıra düzeltmesi
- `validate_structure.py` — `02_MANUSCRIPT` doküman taramasının dışında
- `tests/selftest.py` — cümle bölücü gerileme testleri
- Dört araştırma dosyası ve `spec.json` — kayıtlı vaka turunun bulguları

---

## 15. Altyapı: qa_all 22 → 28 adım

Faz 5 hatta altı yeni adım ekledi: plaka manifestosu, ön/arka madde
sayfa bütçesi, editoryal defter, düşman olgu denetimi, üslup uyumlama
ölçümü, editör teslim paketi.

Beşi **kapı**, biri **ölçüm**. Ayrım kasıtlıdır ve D25/D47 içtihadına
dayanır: ölçemediğin şeyi kapı yapma, ölçebildiğin şeyi rapor et.

---

## 16. CI/CD durumu

| Olay | Sonuç |
|---|---|
| `faz/5-tamamlama` dalına push | 22 koşu · **17 yeşil, 5 kırmızı** |
| PR #8 kontrolleri | ✅ 19/19 geçti |
| `main`'e merge sonrası validate · build · plates | ✅ yeşil |
| `v0.5.0` ilk etiket · release | ⛔ **kırmızı** |
| PR #9 (çıkış kodu sözleşmesi) | ✅ geçti, merge edildi |
| `v0.5.0` yeniden etiket · release | ✅ **yeşil** |
| GitHub Release | ✅ yayımlandı, taslak değil |

**Beş kırmızının beşi de gerçekti.** Hiçbiri yeniden çalıştırmayla
geçmedi, hiçbiri eşik düşürerek kapatılmadı. § 17'de tek tek.

---

## 17. Beş CI kırmızısı ve sebepleri

**① Plaka adımları sistem Python'uyla koşuyordu.** Pillow yoktu, çıkış 1
verdi. Eksik bir isteğe bağlı bağımlılık kalite düşüşüyle aynı sinyali
vermemelidir; çıkış 2 sözleşmesi uygulandı.

**② BOOK_STATS plaka sayımı yerelde ve CI'da ayrışıyordu.** Belge
gitignore'daki klasörü sayıyordu: yerelde 112, CI'da 0. D38 kalıbı
uygulandı — depoya manifesto girdi, sayım oradan okunuyor. Doğrulama:
`07_ASSETS/plates` geçici olarak taşınarak sınandı.

**③ Editörün çalışma kopyası Faz 6 yayın dosyası sayılıyordu.** Faz 6 hiç
başlamamışken %25 görünüyordu ve belge, dosyanın üretildiği makinede
değişiyordu. Ad tek doğruluk kaynağına taşındı. Yeniden üretim yöntemi:
`git clone file://… -b main` ile temiz klon.

**④ ve ⑤ · İki yazım push'u** — dalın erken commit'lerinde aynı ①
sebebiyle.

**⑥ Sürüm iş akışının kırmızısı — en öğreticisi.** `release`, `qa_all`ın
TAMAMINI koşuyor; `validate` koşmuyor. Yani Faz 5'te eklenen adımlar ilk
kez proza ve plaka **bulunmayan** bir ortamda çalıştı ve üçü birden
"eksik girdi"yi "kusur" ile aynı sinyale çevirdi:

- `qa_all`ın üç yeni adımı `run` ile eklenmişti; `run` sıfırdan farklı her
  kodu başarısızlık sayar → `soft_run` eklendi
- `plate_manifest --check` ham dizin yokken 1 dönüyordu → manifestonun
  kendi tutarlılığı denetleniyor, çıkış 2
- `plate_fixtures` Pillow yokken 1 dönüyordu → çıkış 2

**Gevşetme olmadığı sınandı ve kanıt yazıldı:**

| Ortam | Beklenen | Ölçülen |
|---|---|---|
| Ham dizin var | tam eşleşme koşar | çıkış 0 |
| Ham dizin yok + manifesto sağlam | ATLANDI | çıkış **2** |
| Ham dizin yok + manifesto **BOZUK** | kapı ısırır | çıkış **1** |

Üçüncü satır kapının hâlâ ısırdığının kanıtıdır.

---

## 18. Git commit'leri

Faz 5 dalında **20 commit**:

| # | Commit | Konu |
|---|---|---|
| 1 | `d6c17c4` | 112 ham plaka eşlendi, normalize edildi, bütçeye sokuldu |
| 2–8 | `abf2d58`…`931e01a` | sınıf V — 16 madde, üçerli partiler |
| 9 | `9ed3adb` | Animikii'nin kaynak paragrafı kalıplaşmıştı |
| 10–12 | `4740f0a`…`ab4e1e6` | sınıf VI — 8 madde · **112/112 TAMAM** |
| 13 | `728916b` | son üç açılış — **bütün açılışlar tamam** |
| 14 | `cdc58b1` | kayıtlı vaka turu |
| 15 | `2f9266b` | ön ve arka madde + `matter_page.py` |
| 16 | `635bade` | düşman olgu denetimi + defter |
| 17 | `8131ec0` | üslup uyumlama — D40 kapandı |
| 18 | `d18f05a` | ana dil editörü teslim paketi |
| 19 | `234f7dc` | CI: editör kopyası Faz 6 sayımından çıkarıldı |
| 20 | `05b6cf8` | belge: CHANGELOG v0.5.0, D47–D56 |

Ayrıca `main` üzerinde: PR #8 merge (`fbf052f`), PR #9 çıkış kodu
sözleşmesi (`74f84fc`).

**Bu fazda commit iletisinde ölçülmemiş sayı yazılmadı.** Faz 4'te iki
kez yapılmış ve düzeltilmişti; süreç değişikliği (ölçümü commit'ten önce
basmak) tuttu.

---

## 19. Definition of Done

| # | Ölçüt | Durum |
|---|---|---|
| 1 | 112/112 madde yazıldı | ✅ |
| 2 | Bütün metin kapıları 0 başarısız | ✅ 28/28 |
| 3 | Sınıf açılışı 6/6 | ✅ |
| 4 | Karşılaştırma açılışı 8/8 | ✅ |
| 5 | Giriş yazıldı | ✅ 7 sayfa / 8 slot |
| 6 | "Bu kitap nasıl okunur" yazıldı | ✅ 5 / 6 |
| 7 | Sonsöz yazıldı | ✅ 4 / 4 |
| 8 | Arka madde yazıldı | ✅ 4 bölüm |
| 9 | Aborjin kararı Sonsöz'de, savunmacı olmayan dille | ✅ |
| 10 | Kayıtlı vaka notu Sonsöz'de | ✅ |
| 11 | 112 plaka doğrulandı ve eşlendi | ✅ |
| 12 | Ham plakalar değiştirilmedi | ✅ |
| 13 | Plaka ↔ metin manifestosu CI'da denetleniyor | ✅ |
| 14 | Düşman olgu denetimi yapıldı | ✅ 13 kusur |
| 15 | Bütün düzeltmeler defterde | ✅ 146 |
| 16 | Elle düzenleme yapılmadı | ✅ |
| 17 | Üslup uyumlama (D40) | ✅ %8,9 → %1,6 |
| 18 | Çapraz referans bütünlüğü | ✅ `classify --check` yeşil |
| 19 | Yaşayan gelenek kapısı korundu ve kalıptan çıkarıldı | ✅ 19 → 4 |
| 20 | Tam kitap dizgisi ölçüldü | ✅ 112/112 |
| 21 | Sayfa bütçesi yeniden doğrulandı | ✅ 436, sapma 0 |
| 22 | Telif tablosu yeniden bakıldı | ✅ değişmedi |
| 23 | Dört dizin üretildi | ✅ ⚠ sayfa numarası Faz 6 |
| 24 | `book-edited.json` üretiliyor | ✅ |
| 25 | Belgeler eşitlendi | ✅ 6 belge |
| 26 | CHANGELOG 0.5.0 bloğu | ✅ D47–D56 |
| 27 | CI yeşil | ✅ |
| 28 | Merge → `main` | ✅ PR #8 |
| 29 | Etiket `v0.5.0` | ✅ |
| 30 | GitHub Release doğrulandı | ✅ yayımlandı |
| 31 | Ana dil editörü geçişi | 📦 **İNSAN EYLEMİ GEREKİYOR** |
| 32 | Faz 5 raporu | ✅ bu belge |

---

## 20. Kurucu kararlarının uygulanması

**A · Ham plaka üretimi kurucunundur (D39).** Kurucu 112 PNG'yi teslim
etti; hat bekleme durumundan çıktı ve hepsini işledi. **D39 kapandı.**

**B · Üslup sürüklenmesi Faz 5'in işidir (D40).** Yapıldı. § 9.

**C · Kayıtlı vaka açığı.** Faz 4'te "ek tur yapılmaz"dı; kurucu Faz 5'te
**güncelledi**. Tur yapıldı, sınırı önceden kondu ve uygulandı. § 7.

**Uydurma yasağı.** Bu fazda hiçbir vaka, tarih, tanık, sefer, alıntı
veya künye uydurulmadı. Tersi oldu: **var olan iki künye çürütüldü ve
kaldırıldı**, beş künye kayıtta bulunmadığı için prozadan çıkarıldı.

---

## 21. Yaşayan gelenek ve etik kapı

| Ölçü | Değer |
|---|---:|
| Kısıtlılık taraması yapılan madde | 44 |
| Yaşayan gelenek maddesi | tamamı tarandı |
| Kısıt cümlesi kalıplaşması | 19 → **4** |

Kısıt cümlesi bu fazda yeniden yazıldı ve **daralmadı, somutlaştı**:
her madde artık o geleneğin kendi kısıtını adıyla söylüyor. Editör
brifingi de ayrı bir uyarı taşıyor — o cümlelerde doğruluk doğallıktan
önce gelir.

Sonsöz Aborjin kararını bir eksik olarak değil **bir standart beyanı**
olarak yazıyor ve kitabın içindeki kısıt kuralının neye mal olduğunu da
söylüyor: üç yaratık yalnızca bu sebeple düştü.

---

## 22. Kalan riskler ve açık kalanlar

| # | Konu | Sınıf |
|---|---|---|
| 1 | **Ana dil editörü geçişi yapılmadı** | 📦 İNSAN EYLEMİ GEREKİYOR |
| 2 | Dizin sayfa numaraları yok | ⚠ UYARI — gerçek dizgi Faz 6 |
| 3 | Kindle Translate uygunluğu belirsiz | ⚠ UYARI — finansal modelde yok |
| 4 | Kartveli ve Mongol tek maddeyle temsil | ⚠ UYARI — kütüphane erişimi |
| 5 | Kayıtlı vaka oranı düşük | ⚠ UYARI — kayıt elverdiği kadar |
| 6 | Dış hat kalınlığı tahmincisi kalibre değil | ⚠ UYARI — Faz 2'den devir |
| 7 | Kamu malı yanlış sınıflandırma riski | ⚠ UYARI — özgün Giriş/Sonsöz savunma olarak yazıldı |

**Hiçbir uyarı tamamlanma gibi gösterilmedi.**

---

## 23. BOOK_STATS özeti

| Ölçü | Değer | Hedef |
|---|---:|---:|
| Yaratık | 112 | 112 |
| Gelenek | 40 | 40 |
| Yazılmış madde | 112 | 112 |
| Normalize plaka | 112 | 112 |
| Kelime | 88.960 | 78.400 |
| Tahmini sayfa (model) | 342 | 436 |
| **Ölçülen sayfa (dizgi)** | **436** | **436** |

Model ile ölçüm arasındaki fark beklenendir ve belgede yazılıdır:
model 260 kelime/sayfa varsayar, gerçek dizgi plakayı, başlık bloğunu ve
her maddenin yarım kalan son sayfasını da sayar. **Model değil ölçüm
geçerlidir.**

---

## 24. ROADMAP_PROGRESS özeti

| Faz | İlerleme |
|---|---|
| 0 · Kurulum | ✅ |
| 1 · Araştırma | ✅ 112/112 |
| 2 · Tasnif | ✅ |
| 3 · Yazım I | ✅ 45/45 |
| 4 · Yazım II | ✅ 43/43 |
| **5 · Tamamlama** | ✅ **24/24** |
| 6 · Üretim, KDP, Lansman | ⬜ 0/4 |

Faz 6 sayacı **0/4** ve doğrudur: hiçbir yayın dosyası üretilmedi.
Editörün çalışma kopyası bilerek sayılmıyor (D55).

---

## 25. PROJECT_CONTEXT güncellemeleri

§ 1 yeniden yazıldı ve Faz 5 DoD tablosu kondu. Kurucu kararı C'nin
güncellendiği tabloda görünüyor — eski hâli "ek tur yapılmaz" diyordu ve
artık doğru değildi. Devralacak kişi için kritik: **eski bir kararın
güncellendiği yazılmazsa, belge sessizce yanlış olur.**

---

## 26. CHANGELOG özeti

0.5.0 bloğu: ölçülen sayılar, on karar (D47–D56) gerekçeleriyle, sayfa
bütçesi tablosu, düşman denetiminin on üç kusuru, üslup uyumlamasının
önce/sonra tablosu, eklenen altı betik ve beş açık kalan.

`update_docs.check_decision_links` her kurucu kararının gerekçesinin
CHANGELOG'da durduğunu denetliyor; kopuk bağ CI'yı kırmızı yakar.

---

## 27. Ölçüm araçlarının kendi kusurları

Bu fazın en tekrarlayan dersi: **bir denetim aracı, ölçtüğü şey kadar
kendi doğruluğundan da sorumludur.**

| Araç | Kusur | Sonuç |
|---|---|---|
| `factcheck` | 67 itirazın 54'ü aracın kendi kusuruydu | araç düzeltildi, metin değil |
| `editor_pack` | 784 bölümün 363'ünü işaretledi | eşikler dağılım ölçülerek daraltıldı |
| `qa_style` | madde içi 74 tekrarın çoğu kasıtlı koşutluk | sayı hedef alınmadı |
| `textutil.sentences` | noktalamasız başlık sonraki cümleye yapışıyordu | paragraf sonu cümle sonu sayıldı (D56) |
| `update_docs` | editör kopyasını yayın dosyası sayıyordu | tek doğruluk kaynağına taşındı (D55) |
| `plate_manifest` | eksik girdiyi kusur sayıyordu | çıkış 2 sözleşmesi |

Yanlış pozitif üreten bir kapı, gerçek kusurları gürültünün altına
gömer — ve bu, sessizce kör kalan bir kapıdan çok da iyi değildir.

---

## 28. İki yazarlı dosya sorunu

`matter_page` ölçüyü önce `manuscript_metrics.json`'a yazıyordu ve
`update_docs` her koşuda siliyordu. İki yazar, tek dosya, **sessiz
kayıp**.

Çözüm plaka manifestosuyla aynı: ölçüyü ölçen betik kendi dosyasına
yazar, diğerleri yalnızca okur (D51). Bu artık bir kalıp: `plate_manifest`,
`matter_page`, `edits`, `editor_pack` — dördü de kendi ölçü dosyasının
tek yazarı.

---

## 29. Metin kapılarının bulduğu kusurlar

| Kapı | Bulduğu |
|---|---:|
| `qa_echo` | ~24 birebir tekrar — hepsi gerçekti, hepsi metinde düzeltildi |
| `qa_length` | 5 bant ihlali |
| `qa_voice` | yasak kalıp yakalamaları |
| `qa_diacritics` | gövde metninde "Garuda-bird" dizin yazımı |
| `classify --check` | çapraz referans bütünlüğü |
| `factcheck` | 13 olgusal kusur |
| `validate_structure` | kitabın kendi dizini ile Thompson'ın eseri aynı adı taşıyordu |

`qa_echo`nun tekrarlayan bulgusu yine çıktı: **açılış, maddeyi maddenin
kendi cümleleriyle özetliyordu**. Beş kez giriş bölümünde, üç kez
açılışlarda. Bir açılışın işi maddeleri tekrarlamak değil, aralarındaki
farkı kurmaktır.

---

## 30. Sayısal özet

| | |
|---|---:|
| Bu fazda yazılan madde | 24 |
| Bu fazda yazılan kelime | 15.765 + 5.713 (matter) + 1.559 (açılış) |
| Kitabın toplam kelimesi | **88.960** |
| İşlenen plaka | 112 |
| Editoryal düzeltme | 146 |
| Bulunan olgusal kusur | 13 |
| Çürütülen künye | 2 |
| Kaldırılan dayanaksız künye | 5 |
| Yeni betik | 6 |
| Yeni kapı/ölçüm adımı | 6 |
| Commit | 20 (+2 `main`) |
| CI koşusu | 22 (17 yeşil, 5 gerçek kırmızı) |
| Alınan karar | 10 (D47–D56) |
| Gevşetilen kapı | **0** |

---

## 31. Faz 6 hazırlık değerlendirmesi

**Hazır.** Faz 6'nın girdisi metin, plaka ve şartnamedir; üçü de tam.

| Girdi | Durum |
|---|---|
| Metin | ✅ 112 madde + açılışlar + ön/arka madde |
| Plaka | ✅ 112 normalize, dört format kalibre |
| Sayfa bütçesi | ✅ 436, ölçüldü |
| Dizinler | ✅ üretiliyor · ⚠ sayfa numarası dizgiden gelecek |
| Kapak şartnamesi | ✅ Faz 2'den, sırt kalınlığı 436 sayfaya göre |
| Fiyat ve telif | ✅ değişmedi |

**Faz 6'nın ilk işi ana dil editörü olmalıdır.** Paket hazır ve
dışarıya verilmeye uygun; editör dönüşü `edits.json`'a işlenip
`book-edited.json` yeniden üretilir ve bütün kapılar yeniden koşar.

**Faz 6'nın ilk kapısı dizin sayfa numaralarıdır.** `make_index` şu an
uyarı veriyor ve doğru veriyor: `04_PRINT/PAPERBACK/pagemap.json` gerçek
dizgiden gelecek.

---

## 32. Bu fazın üç dersi

**① Katalog düzeyinde doğrulanmış künye, doğrulanmış sayılmaz.** Faz 1
bunu `verification` alanıyla biliyordu; Faz 5 bedelini ölçtü — altı
maddede iki çürük atıf. Kural artık yazılı: kaynağın kendisi okunur.

**② Bir ölçüm aracının ilk çıktısı, aracın kendi kusurlarının
listesidir.** `factcheck`in 67 itirazının 54'ü, `editor_pack`in 363
işaretinin 70'i araçtandı. Aracı düzeltmeden metne dokunmak, metni
aracın hatasına uydurmak olurdu.

**③ Bir kapı, yalnızca çalıştığı ortamda denetlenmiştir.** Faz 5'in altı
yeni adımı yirmi iki koşu boyunca yeşil kaldı ve ilk kez sürüm iş
akışında, proza ve plaka bulunmayan bir ortamda çalıştığında üçü birden
yanlış davrandı. Bir hattın tam kapsamı, en dar ortamında sınanır.

---

## 33. Kapanış

Faz 5 yol haritasının dokuz çıktısını da teslim etti. Kitabın metni
bitti: 112 madde, on dört açılış, yedi ön ve arka madde bölümü, 112
plaka, 88.960 kelime, ölçülen 436 sayfa.

Üç editoryal geçişin ikisi yapıldı ve üçüncüsü **yapılmadı** — insan
işidir, paketi hazırdır ve bu rapor onu tamamlanmış göstermiyor.

On üç olgusal kusur bulundu ve düzeltildi. İki künye çürütüldü. Beş
dayanaksız künye kaldırıldı. Üslup sürüklenmesi %1,6'ya indi. Beş CI
kırmızısının beşi de gerçekti ve beşi de kapı gevşetilmeden kapatıldı.

Sayfa bütçesi 436'da durdu ve fiyat tablosu bu yüzden değişmedi.

**Sıradaki: Faz 6 · Üretim, KDP ve Lansman — kurucu onayı bekliyor.**

---

*Rapor 8 Ağustos 2026'da yazıldı. Bütün sayılar `06_REPORTS/` altındaki
JSON raporlarından ve `git` geçmişinden okunmuştur.*
