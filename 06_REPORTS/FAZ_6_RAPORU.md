# FAZ 6 · ÜRETİM, KDP VE LANSMAN — DURUM RAPORU

> **Durum: ÜRETİM TAMAMLANDI · YAYIN BLOKE.**
> 8 Ağustos 2026 · dal `faz/6-uretim` · CI yeşil.
>
> Bu rapor bir kapanış raporu **değildir** ve öyle gösterilmiyor. Yol
> haritası ve kurucu emri, yayın için tamamlanması gereken beş adımı
> sayıyor; ikisi kurucunun elindeki bir girdiye, üçü kurucunun KDP
> hesabına bağlı. Hiçbiri atlanamaz, hiçbiri taklit edilemez.
>
> **`v1.0.0` ETİKETİ ATILMADI. YOL HARİTASI KAPATILMADI.**
> Kurucu emri § 38: *"Never declare publication complete while a
> publication blocker remains."*

---

## 1. Yönetici özeti

Faz 6'nın mühendislik yarısı bitti. Kitabın **basılabilir dosyaları
üretildi ve doğrulandı**: üç iç blok sürümü, reflowable Kindle EPUB,
DOCX yedeği, gerçek sayfa numaralı dört dizin.

Faz 6'ya girerken üretim hattının **var olmadığı** ortaya çıktı.
`make_pdf.py`, `model.py`, `matter.py`, `make_docx_epub.py` ve
`validate_interior.py` Cilt 1'den devralınmıştı ve **Codex Mythologica
üretiyordu** — on dokuz uygarlığın yetmiş altı miti. `build_all.sh` ve
`ebook_size.py` hiç yoktu. Fazın çekirdek işi bu oldu.

**Bağımsız satır editörü** (kurucunun Faz 6 kararı) manuscript'in
tamamını okudu, 83 düzeltme uyguladı ve ardından **yedi olgusal kusur**
ile **bir kapı deliği** raporladı. Hepsi düzeltildi.

**Yayın bloke.** Kapak sanat eseri teslim edilmedi; fiziksel prova ve
KDP yükleme kurucunun hesabını gerektiriyor.

---

## 2. Üretilenler

| # | Çıktı | Durum | Ölçü |
|---|---|---|---|
| 1 | Ciltsiz iç blok PDF | ✅ | 435 sayfa · 103,4 MB · fontlar gömülü |
| 2 | Ciltli iç blok PDF | ✅ | 435 sayfa |
| 3 | Büyük punto iç blok PDF | ✅ | 599 sayfa |
| 4 | Kindle EPUB (reflowable) | ✅ | 4,73 MB / 7,0 bütçe · 138 bölüm · 112 plaka |
| 5 | DOCX yedeği | ✅ | 0,19 MB |
| 6 | Dört dizin, gerçek sayfa numarasıyla | ✅ | 112/112 doğrulandı |
| 7 | Sayfa haritası (`pagemap.json`) | ✅ | depoda |
| 8 | Ciltsiz kapak (krem + beyaz) | ⛔ | **sanat eseri yok** |
| 9 | Ciltli kapak | ⛔ | **sanat eseri yok** |
| 10 | Büyük punto kapak | ⛔ | **sanat eseri yok** |
| 11 | A+ İçerik 5 modül | ⛔ | kapak sanat eserine bağlı |

---

## 3. Sayfa bütçesi — ölçüldü, zorlanmadı

| | |
|---|---:|
| Faz 5 bütçesi | 436 |
| **Faz 6 ölçümü (ciltsiz)** | **435** |
| Fark | **−1** |

Kurucu emri § 10: *"Do not manually force it to 436."* Zorlanmadı.
Baskı maliyetine etkisi sayfa başına 0,012 $ üzerinden **0,012 $**;
birim telif ve başabaş ACOS değişmiyor. `BRIEF.md` güncellendi.

Büyük punto **599** sayfa. Cilt 1'de aynı sürüm için 540 modellenmiş,
578 çıkmıştı — aynı büyüklük sınıfında.

---

## 4. Doğrulama sonuçları

| Denetim | Ciltsiz | Ciltli | Büyük punto |
|---|---|---|---|
| `validate_interior` | 23/24 · 0 başarısız | 23/24 · 0 | 26/27 · 0 |
| `pdffonts` — gömülmeyen font | yok | yok | yok |
| Görsel çözünürlüğü | 450 PPI | 450 PPI | 450 PPI |
| Kesim, marj, iç marj | geçti | geçti | geçti |

| Denetim | Sonuç |
|---|---|
| `verify_index` — dizin ↔ basılı sayfa | **112/112** |
| `verify_index` — basılı çapraz referans | **346 / 0 uyuşmayan** |
| `make_index --gate phase6` | 6/6 |
| `qa_glyphs` | eksik glif yok · 8 düşüm |
| `qa_all` | **32/32** |
| Üretim ↔ manuscript bütünlüğü | 224 parça · 0 eksik |

Son satır önemli: basılı PDF'ten çıkarılan metin, 112 maddenin açılış
cümlesi ve kaynak notuyla, altı sınıf ve sekiz aile açılışıyla, yedi
ön/arka madde bölümüyle ve kırk gelenek adıyla karşılaştırıldı.
**Üretimde hiçbir şey düşmedi.**

---

## 5. Bağımsız satır editörü — Geçiş 3

Kurucu Faz 6'da bu geçişi bir alt ajana verdi. Editör örnekleme yapmadı:
7 ön/arka madde bölümü, 6 sınıf açılışı, 8 akraba açılışı ve 112
maddenin 784 bölümünün tamamı. **83 düzeltme**, beş partide, her
partiden sonra kapılar koşularak. Bir partide `qa_echo` kırmızı yandı;
kapı haklıydı, editör kendi düzeltmesini yeniden yazdı.

**Bulduğu kalıplar** — Faz 5'in temizlediklerinin farklı kılıktaki
ikizleri: *"worth stating / noting / pausing on"* 26 yerde, *"is doing
something precise"* 13, *"that is not decorative"* 10 (ikisi iki farklı
sınıf açılışında birebir aynı cümle), on üç karşılıklı akraba satırı
hâlâ birbirinin aynası.

**Doğrulandı, körü körüne kabul edilmedi:** madde 112→112, bölüm
784→784, açılış 6/8→6/8, kaynak değişmedi, kelime −273. Editörün
kasıtlı olarak DOKUNMADIKLARI da denetlendi ve doğru: Qílín'in tek
cümledeki koşutluğu, bütün yaşayan gelenek kısıt cümleleri, "here the
entry has to stop" duraklamaları.

---

## 6. Yedi olgusal kusur — hepsi düzeltildi

| # | Kusur | Kanıt |
|---|---|---|
| 1 | Sınıf I açılışı "iki akraba imgesi… sekiz madde hiçbirine ait değil" | Gerçek: **üç** aile (F:8, G:3, H:3), ailesiz **dört** madde |
| 2 | Sınıf II açılışı "on dördünden geçiyor" | C ailesinin bu sınıftaki üye sayısı **on iki** (ikisi sınıf VI'da) |
| 3 | Aile A açılışı "İrlanda ve İskoçya'da yaratık adamı yer" | `each-uisce` ve `nykur` ikisi de tersini söylüyor: İrlanda **boğar**, İskoçya **yer** |
| 4–6 | Adaro üç maddede "güneş ışını üzerinde geliyor / ışığı silah yapıyor" | Adaro'nun kaydında **ışık geçmiyor**; kayıt uçan balıktan söz ediyor |
| 7 | Sonsöz'ün 120/112 aritmetiği yedekler sayılmadan toplanmıyordu | — |

Editörün ayrıca doğrulanmasını istediği Ḫumbaba iddiası incelendi ve
**korundu**: madde "yüz, tabletlerin ısrar ettiği ayrıntıdır" diyor.

---

## 7. Bulunan kapı delikleri

**① Düz kesme işareti hiç aranmıyordu.** Manuscript'te 274 düz kesme
işareti (U+0027), sıfır tipografik. `STYLE.md` § 6 "düz tırnak kapıyı
kırar" diyor ama `qa_voice` yalnızca düz ÇİFT tırnağı arıyor ve UYARI
basıyordu. Kitabın neredeyse her sayfasında *dog's*, *don't* dikey bir
tırnakla dizilecekti. Kaynak normalize edildi, kapı yazılı kurala
uyduruldu ve artık **BAŞARISIZLIK** basıyor (D62).

**② Koşan başlık hiç basılmıyordu.** 28 örnek sayfanın sıfırında üst
bantta mürekkep vardı. `PLAN.resolve()` çağrılmıyordu. Hata SESSİZDİ:
PDF sorunsuz üretiliyor, hiçbir sayfada başlık olmuyordu.
`validate_interior` yakaladı.

**③ Tek boş tablo hücresi 435 sayfaya gömülmemiş Helvetica soktu.**
reportlab'in hücre varsayılan fontu Helvetica'dır. KDP gömülmemiş font
kabul etmez. `pdffonts` yakaladı.

**④ Eksik glif sessizdi.** Kaynaklar sayfasında "ʿArab" bozuk kutu
olarak çıkıyordu. Gözle bulundu → `qa_glyphs.py` yazıldı → sekiz
karakterin daha aynı durumda olduğu ortaya çıktı, hepsi yaratık ve
gelenek adlarında.

**⑤ Kitapta Türkçe basılıyordu.** Kırk gelenek haritası "KAFKASYA",
"KUTUP", "YAKIN DOĞU" yazıyordu; akraba dizini ayrışma cümlesini Türkçe
basıyordu. `spec.json` proje dilindedir ve öyle kalmalı — kitap
İngilizce.

**⑥ Faz 6 ilerlemesi üretildiği makineye göre değişiyordu** (D63).

---

## 8. Yeni araçlar

| Betik | Ne yapar |
|---|---|
| `make_book.py` | Kitabın tamamını dizer, iki geçiş + doğrulama, `pagemap.json` yayar |
| `make_ebook.py` | Reflowable EPUB 3 + DOCX |
| `front_matter.py` | Yapısal ön madde, künye ve **AI beyanı** |
| `qa_glyphs.py` | Basılan her karakterin glifi var mı |
| `verify_index.py` | Dizin ve çapraz referans sayfaları ↔ basılı PDF |
| `production_manifest.py` | Üretim çıktısının depoda duran ölçüsü |

`qa_all` 28 → **32 adım**.

---

## 9. ⛔ BLOKAJLAR — yayın bunlar olmadan yapılamaz

### B1 · Kapak sanat eseri teslim edilmedi — **KURUCU GİRDİSİ**

`03_COVER/artwork/` **boş**. `make_cover_art.py` girdi olarak
`paperback-artwork-textless.png` bekliyor.

**Etkisi:** dört kapağın hiçbiri üretilemez (ciltsiz krem, ciltsiz
beyaz, ciltli, büyük punto). `validate_cover`, 160 piksel küçük resim
testi ve A+ İçerik de buna bağlı.

**Gerekli:** metinsiz kapak sanat eseri, ≥3922 px genişlikte.
Cilt 1'deki 112 PPI hatası tekrarlanmamalı. Bu, Faz 5'teki ham plaka
teslimiyle aynı sınıfta bir kurucu girdisidir (D39).

**Hazır olan:** kapak geometrisi (`cover_spec.py`), KDP ciltli
kalibrasyonu (`kdp_calibration.json` — yeniden keşfedilmedi), sırt
genişliği artık **ölçülmüş** 435 sayfadan hesaplanabilir.

### B2 · Fiziksel prova kopyası — **KURUCU EYLEMİ**

Yol haritası ve kurucu emri (§ 19) bunu **sert bir kapı** olarak
tanımlıyor: *"Do not treat a generated PDF as equivalent to a physical
proof."* Sipariş KDP hesabından verilir, Türkiye'ye kargo 2–3 hafta.

Provada bakılacak tek kritik şey kurucunun kendi yazdığıdır: **çizgi
plakaların ince çizgileri baskıda kayboluyor mu.** Bu faz o riski
ölçerek azalttı (450 DPI seçimi, § 3) ama ölçüm provanın yerine geçmez.

### B3 · KDP Print Previewer — **HESAP GEREKTİRİR**

Sırt yazısının katlama çizgileri arasında olduğunun ekran görüntüsüyle
kanıtlanması isteniyor. Yükleme yapılmadan çalıştırılamaz ve zaten
kapak dosyası yok (B1).

### B4 · KDP yayını — **HESAP VE KURUCU ONAYI GEREKTİRİR**

Dört formatın yüklenmesi, fiyatlandırma, vergi bilgisi (W-8BEN),
kategori ve anahtar kelime girişi, AI beyanı kutusu. Bunlar kurucunun
hesabında, kurucunun adına ve geri alınamaz işlemlerdir. Otonom
yapılmadı ve yapılmamalıydı.

### B5 · ASIN, A+ yayını, reklam — **B4'e bağlı**

---

## 10. Kurucu emrinin madde madde durumu

| § | İstenen | Durum |
|---|---|---|
| 4–7 | Bağımsız editör alt ajanı, tam yetkiyle | ✅ |
| 8 | Editör çıktısının doğrulanması | ✅ |
| 9 | Manuscript dondurma | ✅ metin donduruldu |
| 10 | Gerçek sayfa kalibrasyonu | ✅ 435, zorlanmadı |
| 11 | Gerçek `pagemap` + dört dizin + 20 madde doğrulama | ✅ 112/112 + 346 çapraz referans |
| 12 | Üretim çıktıları | ⚠ 7/11 · kapaklar ve A+ bloke |
| 13–14 | Format kuralları, reflowable Kindle | ✅ |
| 15 | Kapak mühendisliği | ⛔ B1 |
| 16 | İç blok doğrulaması | ✅ 0 başarısız, üç sürüm |
| 17 | Görsel kitap denetimi | ✅ altı kusur bulundu |
| 18 | KDP Previewer | ⛔ B3 |
| 19 | Fiziksel prova | ⛔ B2 |
| 20–22 | KDP metadata, AI beyanı, ürün oluşturma | ⚠ beyan künyede yazılı; yükleme B4 |
| 23 | A+ İçerik | ⛔ B1 |
| 24–26 | Nihai okur denetimi | ⚠ § 11 |
| 27 | Editörün son geçişi | ⚠ § 11 |
| 28 | Kapı matrisi | ⚠ § 12 |
| 29–37 | Kilit, yayın, etiket, kapanış | ⛔ **yapılmadı** |

---

## 11. Nihai okur denetimi — kısmen yapıldı

**Yapılan.** Üretilen PDF'ten metin çıkarıldı ve manuscript'le
karşılaştırıldı (0 eksik). Kitabın omurgası — ön madde, altı sınıf
açılışı, sekiz aile açılışı, sonsöz, arka madde, kaynaklar — baştan
sona okundu. Başlangıç, orta ve son bölgelerden sayfalar görsel olarak
denetlendi (3, 9, 10, 13, 22, 25–28, 53, 62, 191, 200, 291, 300, 384,
387, 399, 408, 416, 425, 426, 434, 435). Bağımsız editör 784 bölümün
tamamını okudu ve raporladı.

**Yapılmayan ve neden.** Kurucu emri § 25 nihai denetimin **basılı
son artefakt üzerinden** yapılmasını istiyor. O artefakt henüz eksik:
kapaksız bir kitap okunmuş sayılmaz ve fiziksel prova görülmedi.
Denetimin kapak, sırt, arka kapak ve fiziksel okuma deneyimi kısmı
**B1 ve B2 çözülene kadar yapılamaz**.

**Bulunan okuma deneyimi gözlemi.** Her madde üç sayfalık bir yuvaya
kuruluyor ve ölçülen içeriği 2,13 sayfa; yani her maddenin üçüncü
sayfası büyük ölçüde boş. Bu Faz 2'de kararlaştırılmış ve bütçeye
girmiş bir tasarımdır (plaka kuralının bedeli) — kusur değil. Ama okur
deneyimi olarak fark edilir ve gelecek baskıda yeniden değerlendirmeye
değer. Faz 6'da değiştirilmedi: sayfa bütçesi, fiyat, sırt genişliği ve
kapak geometrisi buna bağlı ve bu faz metni ve tasarımı değil üretimi
yapar.

---

## 12. Kapı matrisi

| Kapı | Durum |
|---|---|
| selftest · validate_spec · validate_structure | ✅ |
| qa_all (32 adım) | ✅ |
| qa_voice · qa_length · qa_drift · qa_echo · qa_diacritics · qa_style | ✅ |
| qa_glyphs | ✅ |
| factcheck (+ çapraz referans) | ✅ |
| classify --check | ✅ |
| plaka manifestosu · tutarlılık · formatlar | ✅ |
| validate_interior (üç sürüm) | ✅ |
| EPUB bütçesi | ✅ 4,73/7,0 MB |
| dizin ve sayfa haritası doğrulaması | ✅ |
| CI | ✅ |
| validate_cover | ⛔ B1 |
| A+ doğrulaması | ⛔ B1 |
| KDP Previewer | ⛔ B3 |
| fiziksel prova | ⛔ B2 |
| nihai okur denetimi | ⚠ kısmi (§ 11) |

**Hiçbir kapı gevşetilmedi. Hiçbir hata uyarıya çevrilmedi.**
Aksine üç kapı sıkılaştırıldı: düz kesme işareti artık kırıyor, görsel
denetimi "hiç görsel olmasın"dan "≥300 PPI"ye çevrildi, çapraz referans
dayanağı yeni bir denetim olarak eklendi.

---

## 13. Sıradaki adım — kurucuya

1. **Kapak sanat eserini teslim edin** (B1). Hat hazır; sırt genişliği
   artık ölçülmüş 435 sayfadan hesaplanıyor.
2. Kapaklar üretilip doğrulandıktan sonra **prova kopyası sipariş edin**
   (B2) ve ince çizgileri elde kontrol edin.
3. Prova temizse **KDP yüklemesi** (B4) — ciltsiz önce, sonra
   "+ Create Hardcover" ve "+ Create Kindle eBook".
4. Yayın doğrulandıktan sonra `v1.0.0` etiketi ve yol haritası kapanışı.

**Bu rapor yazıldığı anda otonom çalışma durdu.** Sıradaki eylem
kurucunundur.
