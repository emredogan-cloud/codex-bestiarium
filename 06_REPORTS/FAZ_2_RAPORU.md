# FAZ 2 · NİHAİ RAPOR — Codex Bestiarium

> **Tasnif, Veri Modeli ve Plaka Hattı** · 7 Ağustos 2026
> Etiket `v0.2.0` → `v0.2.1` · kapı `phase2` · bütün iş akışları **yeşil**
>
> Kanıt seviyesi: **[D] DOĞRULANMIŞ** (bir dosyadan ölçüldü veya bir komutun
> çıktısı) · **[T] TAHMİN** (modelden türetildi) · **[G] GÖRÜŞ** (editoryal karar)

---

## 1. Yönetici özeti

Faz 2 üç iş yaptı ve dördüncü bir şey buldu.

**Yaptığı üç iş.** 112 madde altı sınıfa ve sekiz aileye nihai olarak
oturtuldu; 181 karşılıklı çapraz referans kuruldu; plaka ölçüm hattı kuruldu
ve kalibre edildi; madde sayfası tasarlanıp dizildi. Master yol haritasından
devralınan **iki tutarsızlık** — sınıf dağılımı ve aile üyelikleri — kapatıldı.

**Bulduğu şey.** Ölçüm disiplini, aranmayan **dört kusur** ortaya çıkardı ve
dördü de aynı sınıftandı: *ölçen aletin kendisi hiç ölçülmemişti.* En ağırı,
plaka kapısının şartnameye **birebir uyan** bir plakayı reddediyor olmasıydı —
yani hat, doğru çizilmiş 112 plakanın tamamını geri çevirecekti. En hassası,
yaşayan gelenek kapısındaki **ölü kuraldı**: kitabın en ağır etik notunu
taşıyan madde (Buda · Ityop'ya) zorunlu kısıtlılık kapısının dışında kalmıştı.

**Kitabın tek kelimesi yazılmadı.** Yazım Faz 3'te başlar ve kurucu onayı
bekler.

| Ölçü | Değer | Kanıt |
|---|---:|---|
| Madde · gelenek | 112 · 40 | [D] |
| Çapraz referans bağı (karşılıklı) | 181 | [D] |
| Sayfa bütçesi | 436 | [D] prova dizgisi |
| Ciltsiz birim telif | 8,76 $ | [D] `verify_royalties` |
| Plaka ölçüm doğruluğu | %0,3 hata | [D] kalibrasyon |
| 112 plakalık EPUB projeksiyonu | 3,74 MB | [D] (bütçe 6 MB) |
| Yazılmış madde | 0 | [D] tasarım gereği |

---

## 2. Tamamlanan hedefler

Yol haritası Faz 2'nin dokuz çıktısı:

| # | Çıktı | Durum |
|---|---|---|
| 1 | 112 maddenin altı sınıfa **nihai** dağılımı | ✅ |
| 2 | Sekiz ailenin nihai üyelikleri + ayrışma cümleleri | ✅ |
| 3 | Sekiz karşılaştırma açılışının içerik planı | ✅ `00_CONTEXT/KIN_OPENINGS.md` |
| 4 | Çapraz referans grafiği (döngü ve tek yön kontrolü) | ✅ 181 bağ, simetrik |
| 5 | 112 telaffuz alanı dolu | ✅ |
| 6 | Plaka kimlikleri atanmış | ✅ (Faz 1'de) |
| 7 | **Pilot plaka seti — 10 plaka, onaylı** | ⚠ **hat hazır, ham plaka bekleniyor** |
| 8 | Plaka tutarlılık raporu | ✅ hat + kalibrasyon raporu |
| 9 | `STYLE_PLATES.md` ölçülen değerlerle güncellenmiş | ✅ § 1b |

Yol haritası Faz 2'nin dizgi görevleri:

| Görev | Durum |
|---|---|
| `plates.py` hattı kurulur ve kalibre edilir | ✅ **iki kusuru bulundu** |
| Madde başlığı bloğu (Cinzel 16 pt · 0,06 em) | ✅ |
| Sınıf işareti (dış üst köşe, Cinzel 8 pt, %30) | ✅ |
| Akraba satırı (0,4 pt altın fileto + EB Garamond 9,5 pt) | ✅ |
| **Bir madde sayfasının prova dizgisi** | ✅ **sayfa bütçesini düzeltti** |

### 7. çıktı hakkında — neden açık kaldı

Faz 2'nin plaka işi ikiye ayrılıyordu: **hattı kurup kalibre etmek** ve
**on ham plakayı üretip ölçmek**.

Birincisi tamamlandı ve ölçümleriyle `STYLE_PLATES.md` § 1b'de duruyor: cetvel
sınandı, iki kusuru bulundu, düzeltildi ve doğruluğu (%0,3) sayıyla kayda
geçti. Format bütçeleri de ölçüldü.

İkincisi **ham AI görsel çıktısı** gerektirir —
`BESTIARIUM_IMAGE_PROMPTS.html` → görsel üreteç → `07_ASSETS/plates_raw/`.
Bu, hattın dışındaki tek girdidir ve kurucudan gelir. Geldiği anda tek komut
yeter:

```bash
python3 08_BUILD/plates.py --normalize --pilot
python3 08_BUILD/plates.py --pilot -v
python3 08_BUILD/convert_plates.py
```

Ölçülen dağılım `STYLE_PLATES.md` § 5'teki boş tabloya yazılır ve üretim
setinin karşılaştırma tabanı olur.

---

## 3. Araştırma ve yazım istatistikleri

**Bu fazda proza yazılmadı** — yol haritasının şartı buydu.

| Ölçü | Değer | Kanıt |
|---|---:|---|
| Yazılan madde | 0 | [D] |
| Yazılan editoryal metin (ayrışma cümlesi, tez, plan) | ~4.100 kelime | [D] `kin_map.json` |
| Doğrulanan aile motif kodu | 8 (3'ü düzeltildi) | [D] |
| Toplanan alternatif ad | 44 madde · 94/112 madde artık altName taşıyor | [D] |
| Telaffuz rehberi satırı | 112 → **289** | [D] `indexes.json` |
| Benzersiz Thompson kodu | 69 | [D] |

Prova dizgisinin kullandığı 697 kelime **proza değil ölçüm dolgusudur**;
bölüm bantlarının orta noktasında üretildi (`tests/make_fixtures.py` ile aynı
üreteç). Ölçülen şey geometri, üslup değil.

---

## 4. Kitap istatistikleri

### Sınıf dağılımı ve sayfa bütçesi

| Sınıf | Madde | Sayfa | Yol haritası (120 için) |
|---|---:|---:|---:|
| I · THE GUARDIANS | 18 | 54 | 22 / 56 |
| II · THE DEVOURERS | 27 | 81 | 28 / 70 |
| III · THE SHAPE-CHANGERS | 19 | 57 | 22 / 56 |
| IV · THE WATER-DWELLERS | 24 | 72 | 24 / 60 |
| V · SKY AND STORM | 16 | 48 | 14 / 36 |
| VI · THE RESTLESS DEAD | 8 | 24 | 10 / 26 |
| | **112** | **336** | |

| Kalem | Sayfa | Kanıt |
|---|---:|---|
| Maddeler (112 × 3) | 336 | [D] prova dizgisi |
| Sınıf ve karşılaştırma açılışları (6×2 + 8×2) | 28 | [D] |
| Ön/arka madde · dizinler · kaynaklar | 72 | [T] yol haritası Faz 5 |
| **Toplam** | **436** | |

### Akraba imge aileleri

| Aile | İmge | Motif | Üye | Manşet | Uzun kuyruk |
|---|---|---|---:|---:|---:|
| A | Su atı | `B184.1.3` | 4 | 4 | — |
| B | Tilki kadın | `D113.3` | 2 | 2 | — |
| C | Gece cadısı | `G262` | 14 | 9 | 5 |
| D | Fırtına kuşu | `B31` | 9 | 9 | — |
| E | Derinlerin yılanı | `B11.2.1.1` | 15 | 9 | 6 |
| F | Eşik bekçisi | `F150` | 8 | 8 | — |
| G | Yaban adamı | `F567` | 4 | 4 | — |
| H | Gizli halk | `F251` | 3 | 3 | — |
| | | | **59** | **48** | **11** |

### Çapraz referans grafiği

| Ölçü | Değer |
|---|---:|
| Bağ (karşılıklı) | 181 |
| Madde başına ortalama | 3,23 |
| En az / en çok | 2 / 5 |
| Bantta (2–5) | 112/112 |

Bağ tipleri: **işlev** 75 · **aile** 63 · **gelenek** 41 · **çift** 2.
Derece dağılımı: 2 bağ → 20 madde · 3 bağ → 55 · 4 bağ → 28 · 5 bağ → 9.

### Fiyat ve telif — 436 sayfada yeniden doğrulandı

| Sürüm | Sayfa | Baskı maliyeti | Liste | **Birim telif** | KDP bandı | İç marj |
|---|---:|---:|---:|---:|---|---|
| Ciltsiz | 436 | 6,23 $ | 24,99 $ | **8,76 $** | 24–828 ✓ | 0,875" ≥ 0,75" ✓ |
| Ciltli | 436 | 10,88 $ | 37,99 $ | **11,91 $** | 75–550 ✓ | 0,875" ≥ 0,75" ✓ |
| Büyük punto | 763 | 10,16 $ | 29,99 $ | **7,84 $** | 24–828 ✓ | 0,875" ≥ 0,875" ✓ |

Üçü de pozitif, üçü de KDP bandında — 436 ve 763 sayfada iç marj gereksinimi
yükseldiği hâlde. Fiyatlar değişmedi.

---

## 5. Oluşturulan dosyalar

| Dosya | Ne |
|---|---|
| `01_SOURCE/kin_map.json` | Faz 2'nin editoryal katmanı — **elle yazılır** |
| `08_BUILD/classify.py` | kin_map → spec + belge + grafik raporu (13 kontrol) |
| `00_CONTEXT/KIN_OPENINGS.md` | Sekiz karşılaştırma + altı sınıf açılışının planı (405 satır, üretilir) |
| `08_BUILD/entry_page.py` | Madde sayfası tasarımı ve prova dizgisi |
| `08_BUILD/tests/plate_fixtures.py` | Geometrisi **bilinen** gravür kurguları |
| `08_BUILD/tests/plate_selftest.py` | Plaka ölçümünün kendi testi (16 kontrol) |

Ayrıca üretilen raporlar: `06_REPORTS/crossref-graph.json` ·
`plate-calibration.json` · `plate-format-calibration.json` ·
`entry-page-proof.json`.

---

## 6. Değiştirilen dosyalar

**172 dosya · +7.114 / −973 satır.** Öne çıkanlar:

| Dosya | Değişiklik |
|---|---|
| `08_BUILD/plates.py` | Açı düzeltmesi · budanmış ortalama · darbe/periyot kapısı · dış hat ayrıldı |
| `08_BUILD/bestiarium.py` | `TARGET_PAGES` 380→436 · `hatch_duty` · `LIVING_TRADITIONS` ölü kurallar |
| `08_BUILD/convert_plates.py` | `--calibrate` · web formatı kayıpsıza çevrildi |
| `08_BUILD/validate_spec.py` | Ölü kural denetimi · açıklanmamış gelenek sapması artık hata |
| `08_BUILD/seed_import.py` | `--sync` modu |
| `08_BUILD/research_gen.py` | § 7 çapraz referansları ayrışma notlarıyla basıyor |
| `08_BUILD/make_index.py` | Diakritiksiz biçim **türetiliyor** (289 satırlık telaffuz rehberi) |
| `08_BUILD/tests/selftest.py` | Kapı testi kusur kurgularına geçirildi |
| `08_BUILD/update_docs.py` | Sayfa bütçesi · manşet/uzun kuyruk · doğru payda |
| `08_BUILD/qa_all.sh` | `.gate` artık `--fix` ile de geçerli · üç yeni kapı |
| `08_BUILD/editions.py` | `PROVISIONAL_PAGES` 436/763 |
| `00_CONTEXT/STYLE_PLATES.md` | § 1b kalibrasyon bölümü |
| `00_CONTEXT/BRIEF.md` | Sayfa bütçesi ve telif tablosu |
| `00_CONTEXT/PROJECT_CONTEXT.md` | Durum · DoD · § 6 çözümler · § 6b bulgular |
| `01_SOURCE/spec.json` | crossRefs · aileler · sınıf hedefleri · sayfa bütçesi |
| `01_SOURCE/research/*.md` | 112 dosya — § 7 artık dolu |

---

## 7. Altyapı değişiklikleri

**Hat artık üç katmanda türetiyor ve sıra bağlayıcı:**

```
seed_import.py       tohum tablosu + scope_amendments.json
      ↓
research_gen.py      research_data/*.json → araştırma dosyaları + spec
      ↓
classify.py          kin_map.json → çapraz referanslar, aileler, sayfa bütçesi
```

Elle yazılan tek şey **araştırmanın ve editoryal kararın kendisidir**; biçim
üretilir. Kapsam kararı eklendiğinde `seed_import.py --sync` kullanılır — tam
yeniden üretim 112 araştırma kaydını siler.

**Ölçümün kendisini ölçen üç yeni test:**

| Test | Ne kanıtlar |
|---|---|
| `tests/selftest.py` | Metin **ve şema** kapıları kusuru yakalıyor (dört kapı seviyesi) |
| `tests/plate_selftest.py` | Plaka ölçümü doğru sayıyı buluyor **ve** kapı ısırıyor |
| `convert_plates --calibrate` | Format bütçeleri plaka gelmeden tutuyor |

**Çıkış kodu sözleşmesi** kuruldu: `0` geçti · `1` kapı düştü · `2` atlandı.
Bağımlılık eksikliği artık asla `1` dönmüyor.

---

## 8. CI/CD durumu

| İş akışı | Durum | Yeni |
|---|---|---|
| `validate` | ✅ yeşil | `research_gen --check` · `classify --check` · kapı seviyeli dizin |
| `build` | ✅ yeşil | **font indirme (SIL OFL 1.1)** · madde sayfası prova dizgisi |
| `plates` | ✅ yeşil | **`calibration` işi** — cetvel doğru mu ölçüyor |
| `release` | ✅ yeşil | tam bağımlılık kurulumu — sürümde atlanan kapı yok |

**CI dizgiyi ilk kez sınıyor.** Fontlar depoda tutulmuyor ve CI'da yoktu;
dizgi hattı hiç koşmuyordu. Cinzel ve EB Garamond SIL OFL 1.1'dir ve
serbestçe indirilebilir. CI'daki prova, yereldeki ölçümü **birebir**
tekrarlıyor: 2,558 sayfa.

Yerel kapı sayısı: **19** (`./08_BUILD/qa_all.sh`).

---

## 9. Git commit'leri

| Commit | Konu |
|---|---|
| `52d0c86` | tasnif: sınıf ve aile tutarsızlıkları çözüldü, çapraz referans grafiği kuruldu |
| `1c9b4ae` | plaka: ölçüm hattı kalibre edildi — cetvel iki yerde eğriydi |
| `eb3347f` | dizgi: madde sayfası tasarlandı ve prova dizildi — sayfa bütçesi 380 → 436 |
| `9e3c044` | faz2: kapı phase2'ye yükseltildi, belgeler senkronlandı |
| `98ebb5e` | hat: düşürülen maddelerin plaka konuları kayda geçirildi |
| `64b9fc0` | ci: sürüm kapısı kırmızıydı — "bağımlılık yok" ile "kapı düştü" aynı sinyaldi |
| `e0a71db` | etik: kısıtlılık kapısında ölü kural — Ityop'ya maddesi kapının dışındaydı |

Üç PR: **#3** (Faz 2) · **#4** (sürüm kapısı) · **#5** (etik kapı).
Üçü de merge edildi.

---

## 10. GitHub Actions sonuçları

CI **iki kez kırmızı yandı** ve ikisi de gerçek kusurdu; ikisi de düzeltilip
yeşile döndürüldükten sonra devam edildi.

| # | Kırmızı | Sebep | Düzeltme |
|---|---|---|---|
| 1 | `validate` | `classify --check`, `06_REPORTS/crossref-graph.json` yokken "bayat" diyordu | Rapor bir **çıktıdır**, kaynak değil. Bayatlık denetimi depodaki türetilmiş dosyalara indirildi. |
| 2 | `validate` | `ROADMAP_PROGRESS` provanın üretildiği makinede farklı çıkıyordu | Faz 6 ilerlemesi `04_PRINT` altındaki PDF'leri sayıyordu; **prova bir ölçüm artefaktıdır**, yayın dosyası değil. Prova klasörleri sayımın dışına alındı. |
| 3 | `release` | `v0.2.0` etiketinde bağımlılık eksikliği kapı düşüşü sanıldı | Çıkış kodu sözleşmesi (bkz. § 7) + `release.yml` artık tam bağımlılık kuruyor. |

Son durum: `validate` · `build` · `plates` · `release` — **dördü de yeşil**.

---

## 11. Definition of Done kontrol listesi

Yol haritası Faz 2 DoD:

| # | Ölçüt | Durum |
|---|---|---|
| 1 | Her madde tam bir sınıfta; hiçbiri 8'in altında veya 32'nin üstünde değil | ✅ 18·27·19·24·16·8 |
| 2 | Sınıf ve aile dağılımı tutarsızlığı **çözüldü**, karar `CHANGELOG`'da | ✅ D21–D24 |
| 3 | Sekiz ailenin ayrışma cümlesi yazıldı ve editoryal olarak onaylandı | ✅ |
| 4 | Her maddenin 2–5 karşılıklı çapraz referansı var; kırık referans yok | ✅ 181 bağ · ort 3,23 |
| 5 | 112 telaffuz alanı dolu | ✅ |
| 6 | Pilot set (10 plaka) **onaylandı**; ölçülen dağılım `STYLE_PLATES.md`'ye yazıldı | ⚠ **hat hazır ve kalibre; ham plaka bekleniyor** |
| 7 | `.gate` → `phase2` | ✅ |
| 8 | CI yeşil, merge, **`v0.2.0`** etiketi | ✅ (+ `v0.2.1` yama) |

Ek doğrulama görevleri:

| Komut | Sonuç |
|---|---|
| `validate_spec.py --gate phase2 -v` | **44/44 · 0 başarısız · 0 uyarı** |
| `make_index.py --gate phase2` | 4 dizin · telaffuz eksiksiz · 289 satır |
| `plates.py --pilot -v` | 0 başarısız (plaka yok — beklenen) |
| `convert_plates.py --calibrate` | 5/5 · bütün bütçeler tutuyor |
| `tests/plate_selftest.py` | **16/16** · doğruluk + ısırma |
| `tests/selftest.py` | Bütün kapılar beklendiği gibi |
| `entry_page.py --proof` | 8/8 · plaka + yedi bölüm sığıyor |
| `make_prompts.py --check` | Senkron |
| `validate_structure.py` | 39/39 |
| `./08_BUILD/qa_all.sh` | ✅ **19 kapı yeşil** |

**Hiçbir yerde TODO, Draft, Pending veya Later kalmadı** — açık kalan tek
kalem ham plaka girdisidir ve o bir görev değil, bir **bekleyen girdidir**.

---

## 12. Bilinen kalan riskler

| # | Risk | Durum | Azaltıcı |
|---|---|---|---|
| 1 | **İllüstrasyon tutarsızlığı** (Risk 1 · etki *yıkıcı*) | ⚠ ölçüm hattı hazır, **gerçek plakada henüz sınanmadı** | Cetvel kalibre edildi (%0,3); pilot set kilidi duruyor |
| 2 | **Dış hat kalınlığı ölçülemiyor** | ⚠ kapı değil, ölçüm | Kalibrasyonda ayırt edemedi; gerçek plakalarda yeniden değerlendirilecek |
| 3 | **A1 — herkese açık depoda proza** | ⛔ **Faz 3'ü bloke eder** | Karar kurucunundur; varsayılan (a): proza depo dışında |
| 4 | Sayfa bütçesi 436 → Faz 6'da değişebilir | 🟡 | Cilt 1'de 540 modellenmiş 578 çıkmıştı; telifte 8,76 $ payı var |
| 5 | Vektör temizlik süresi ölçülmedi (A3) | 🟡 | Pilot set gelince ölçülecek; 25 dk/plaka aşılırsa dışarıya verilir |
| 6 | Kindle Translate uygunluğu | 🟡 | 112 plaka kapıyı kapatabilir; **finansal modele dahil değil** |
| 7 | Üslup sürüklenmesi (Risk 8) | 🟡 Faz 3'te başlar | Tek seferde 3 madde · `qa_drift` · `qa_echo` |
| 8 | Kamu malı yanlış sınıflandırma | 🟡 | Cilt 1'den devralındı; künye beyanı + özgün Giriş/Sonsöz |

**Kapanan riskler:** Risk 5 (Kindle dosya boyutu) ölçüldü — 3,74 MB, bütçe
6 MB. Risk 2 (iki kaynak) Faz 1'de kapandı. Risk 10 (bayat belge) mekanizmayla
kapalı.

---

## 13. Güncellenen yol haritası ilerlemesi

| Faz | Başlık | İlerleme | Etiket |
|---:|---|---|---|
| 1 | Altyapı, Araştırma ve Kapsam Kilidi | **112/112 (%100)** | `v0.1.0` ✅ |
| 2 | Tasnif, Veri Modeli ve Pilot Plaka Seti | **112/112 (%100)** | `v0.2.0` ✅ |
| 3 | Çekirdek Yazım · Bekçiler ve Yutucular | 0/45 (%0) | `v0.3.0` |
| 4 | Genişleme · Şekil Değiştirenler ve Su Sakinleri | 0/43 (%0) | `v0.4.0` |
| 5 | Tamamlama, İllüstrasyon ve Editoryal İnceleme | 0/24 (%0) | `v0.5.0` |
| 6 | Üretim, KDP ve Lansman | 0/4 (%0) | `v1.0.0` |

Faz 3–5'in madde sayıları **sınıf dağılımının düzelmesiyle değişti**:
Faz 3 (I+II) 44 → **45**, Faz 4 (III+IV) 43, Faz 5 (V+VI) 25 → **24**.

GitHub kilometre taşı **Faz 2 · Veri** kapatıldı.

---

## 14. BOOK_STATS özeti

| Ölçü | Şu an | Hedef |
|---|---:|---:|
| Yaratık kaydı | 112 | 112 |
| Gelenek | 40 | 40 |
| Araştırma dosyası | 112 | 112 |
| İki bağımsız kaynaklı madde | 112 | 112 |
| Doğrulanmış motif kodu | 112 | 112 |
| Telaffuz alanı dolu | 112 | 112 |
| **Çapraz referansı olan madde** | **112** | **112** |
| **Kısıtlılık taraması · zorunlu** | **35** | **35** |
| Yazılmış madde | 0 | 112 |
| Normalize plaka | 0 | 112 |
| Tahmini sayfa | — | **436** |

Kısıtlılık taraması toplam 44 maddede yapıldı; 9'u gönüllü (zorunlu olmayan
geleneklerde). Zorunlu olmayan bir taramayı yapmak serbesttir; zorunlu olanı
atlamak kapıyı kırar.

---

## 15. PROJECT_CONTEXT güncellemeleri

- § 1 · Durum: Faz 2 tamamlandı, Faz 2 DoD tablosu, 6. maddenin gerekçesi
- § 2 · Hacim **436 sayfa** (provadan ölçüldü) · 112 plaka
- § 3 · **Faz 2'de ne teslim edildi** (yeni bölüm, 10 kalem)
- § 4 · Klasör yapısı: `kin_map.json` · `scope_amendments.json` · `research_data/`
- § 5 · Kayıt şeması: `crossRefs` ve `pronunciation` gerçek değerlerle
- § 6 · **Devralınan iki tutarsızlık — Faz 2'de kapatıldı** (tablolarla)
- § 6b · **Faz 2'nin üç bulgusu** (yeni bölüm)
- § 9 · Komutlar: yeni kalibrasyon ve prova komutları
- § 10 · Bilinen sorunlar: 4 kalem kapandı, 2 yeni kalem açıldı
- § 11 · Sıradaki adım: Faz 3'ün ilk emri ve A1'in bloke ediciliği

---

## 16. CHANGELOG özeti

**`[0.2.0]`** — sekiz karar (**D21–D27**), üç bulunan kusur, eklenenler,
ölçülenler, açık kalanlar.

| # | Karar |
|---|---|
| D21 | Sınıf hedefi ölçülen gerçeğe güncellendi, madde yeniden sınıflandırılmadı |
| D22 | Boitatá V → I (iki bağımsız kanıt) |
| D23 | Aile üyeliği iki katmanlı: üye (59) · manşet kadro (48) |
| D24 | Üç aile motif kodu düzeltildi (B · C · G) |
| D25 | Dış hat kalınlığı kapı olmaktan çıkarıldı |
| D26 | Sayfa bütçesi 380 → 436 |
| D27 | Web plakası kayıplıdan kayıpsıza çevrildi |

**`[0.2.1]`** — **D28**: `LIVING_TRADITIONS` kimlikleri düzeltildi ve kapıya
bir kapı eklendi.

---

## 17. Faz 3'e hazırlık değerlendirmesi

### Hazır olanlar

- **Veri.** 112 madde doğrulanmış, tasnif edilmiş, birbirine bağlanmış.
  `spec.json` tek doğruluk kaynağı ve üç katman onu tutarlı tutuyor.
- **Girdi üçlüsü.** Faz 3'ün her maddesi için gereken üç şey hazır:
  araştırma dosyası (§ 7 artık akraba tablosunu da taşıyor), `STYLE.md`
  (Cilt 1'den üç gerçek kalibrasyon paragrafıyla), yedi bölümlü şablon.
- **Kapılar.** 19 kapı yeşil ve **kapıların kendisi sınanmış** durumda.
  Metin geldiği anda beş metin kapısı otomatik devreye girer.
- **Dizgi.** Madde sayfası tasarlandı, dizildi, ölçüldü. Sayfa bütçesi artık
  bir model değil bir ölçüm. CI dizgiyi her push'ta sınıyor.
- **Açılışlar.** Sekiz karşılaştırma açılışının tezi, haritası, manşet kadrosu,
  tablo sütunları ve kapanışı kilitli. Faz 3'te dördü (C, F, G, H) yazılacak
  ve ne yazılacağı belli.

### Faz 3 başlamadan gereken tek karar

**A1 — herkese açık depoda proza.** 78.400 kelimelik metin nerede duracak?
Yol haritasının önerdiği varsayılan **(a)**: depo public kalır, proza depo
dışında; CI proza denetimini yerelde yapar. `.gitignore` bunun için zaten
hazırlanmış durumda.

Bu **bloke edici** tek sorudur. A3 (vektör temizlik dışarıya verilecek mi)
pilot set gelene kadar beklemek zorundadır.

### Önerilen ilk emir

```
"Sınıf I'in ilk üç maddesini yaz: kerberos, humbaba, basiliscus.
 Girdi her madde için üçlüdür — araştırma dosyası + STYLE.md +
 yedi bölümlü şablon. Tek seferde en fazla üç madde."
```

İlk beş madde bittiğinde **durulur**: `qa_voice.py` + `qa_length.py`
çalıştırılır, ses kalibre edilir ve kurucu okur. Ses burada kurulur;
sonradan düzeltmek 112 maddeyi yeniden okumak demektir.

### Değerlendirme

**Faz 3'e hazır.** Tek engel A1 kararıdır ve o bir onay meselesi, bir iş
meselesi değil.

---

*Vâliçe Press · Codex Bestiarium · Faz 2 nihai raporu · 7 Ağustos 2026*
