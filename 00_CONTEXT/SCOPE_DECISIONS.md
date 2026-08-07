# SCOPE DECISIONS — kapsam kararları kaydı

> **Bu dosya Faz 1'in en önemli çıktısıdır.** Kaynak bulunamayan her madde
> buraya yazılır. Boş kalan bir satır, sessizce uydurulmuş bir maddeden
> **çok daha iyidir**.
>
> Kural: *120 sayısı kutsal değildir; doğruluk kutsaldır.*
>
> **KAPSAM KİLİTLENDİ — 7 Ağustos 2026.** Ölçüm: `python3 08_BUILD/research_gen.py --report`

---

## 1. KİLİTLENEN KAPSAM

| | |
|---|---:|
| **Yaratık** | **112** |
| **Gelenek** | **40** |
| Doğrulanmış madde | **112** |
| Araştırılan aday | 120 |
| Düşürülen | 8 |
| Yeniden sınıflandırılan | 1 |
| Değiştirilen | 1 |

**Faz 1 kapısı: `validate_spec --gate phase1` → 0 başarısız.** Eşik 112,
ölçülen 112.

> Alt başlık **"112 Legendary Creatures from 40 Traditions"** olarak
> güncellendi. Kırk gelenek iddiası **korundu** — düşen maddelerin hiçbiri
> bir geleneği tamamen boşaltmadı.

---

## 2. Zor sekiz gelenek — ÖLÇÜM SONUCU

Yol haritası bu sekiz geleneği kapsam riskinin merkezi saymış ve Faz 1'in
**onlarla başlamasını** emretmişti. Ölçüm o uyarıyı doğruladı.

| Gelenek | İşaret | Aday | Kilitlenen | Durum |
|---|---|---:|---:|---|
| Ainu | ᚼ | 3 | **3** | ✅ |
| Hayk | ✚ | 3 | **3** | ✅ |
| Ityop'ya | ✤ | 3 | **1** | ⚠ |
| Kartveli | ✛ | 3 | **1** | ⚠ |
| Melanesia | ◉ | 3 | **3** | ✅ |
| Mongol | ⚔ | 3 | **1** | ⚠ |
| Nusantara | ❋ | 3 | **1** | ⚠ |
| Sápmi | ❄ | 3 | **3** | ✅ |

**Ayrım kaynak YOKLUĞU değil, kaynak ERİŞİMİdir.** Geçenlerin
dijitalleştirilmiş birincil etnografisi veya hakemli makalesi var
(Batchelor 1901 tam metin, Conrad'ın iki makalesi, Deacon'ın JRAI makalesi).
Geçmeyenlerin kaynağı **gerçek ve mevcut** — Virsaladze 1973, Chikovani 1946,
Heissig 1980 — ama içerik düzeyinde doğrulanamıyor.

> Yol haritasının Kurucu Notları bunu öngörmüştü: *"Zor sekiz geleneğin
> kaynakları için üniversite kütüphanesi erişimi veya arşiv aboneliği
> gerekebilir. Bu, planlanmamış tek nakit kalemidir."* Ölçüm o kalemi
> **fiyatlandırdı: 8 madde.**

---

## 3. Düşürülen maddeler

Her biri için engel ve gerekçe yazılı. Araştırma dosyaları
[`09_ARCHIVE/dropped-research/`](../09_ARCHIVE/dropped-research/) altında
**korundu** — yapılan iş ve düşürme gerekçesi kayıt altında kalmalı.

### `almas`

Moğol yaban adamı. İki bağımsız kaynak katalog düzeyinin üstünde doğrulanamadı. Heissig 1980'in tam metni tarandı (390 KB); 'almas' geçmiyor. Kriptozooloji literatürü SOURCING_STANDARD § 2 uyarınca kaynak sayılmaz. Kütüphane erişimiyle Faz 2'de yeniden değerlendirilebilir.

### `chotgor`

Tek bağımsız kaynak bulunabildi (Heissig 1980) ve o da içerik düzeyinde doğrulanamadı — tam metin taramasında 'chotgor/čötgör' geçmiyor. İki bağımsız kaynak kuralı sağlanamadı.

### `ganen`

Etiyopya. Tek bağımsız kaynak bulunabildi; ikinci kaynak yok. Adın yayımlanmış literatürde yerleşik bir karşılığı bulunamadı.

### `kaji`

Gürcü gizli halkı. Wardrop 1894 tam metni tarandı; 'kaji' geçmiyor. Virsaladze 1973 ve Chikovani 1946 gerçek ve mevcut ama içerik düzeyinde doğrulanamıyor (kütüphane erişimi gerekiyor).

### `ochokochi`

Megrel orman adamı. Wardrop 1894 tam metninde geçmiyor. Gürcü kaynakları katalog düzeyinde kaldı.

### `orang-bunian`

Skeat 1900'ün bu maddeyi kapsadığı DOĞRULANAMADI (tam metinde 'Bunian' bulunamadı). Kapsam iddiası geri çekildi; ikinci bağımsız kaynak kesin-yer düzeyinde doğrulanamadı.

### `rangda`

Belo 1949 (*Bali: Rangda and Barong*, 59 s.) gerçek ve konuyu doğrudan işliyor, ama içerik düzeyinde kesin bir yer doğrulanamadı. Ayrıca Rangda YAŞAYAN bir tören uygulamasının merkezindedir ve maskesi kutsanmış nesnedir — kısıtlılık dikkati zaten yüksekti. Faz 2'de kütüphane erişimiyle yeniden değerlendirilecek.

### `zar`

Zar bir YARATIK değil bir ilişki/tutulma biçimidir; 'bestiary' maddesi olarak zorlama. Ayrıca kaynaklar kesin-yer düzeyinde doğrulanamadı ve uygulama yaşayandır. Kategorik olarak da kitaba uymuyor.

---

## 4. Değiştirilen ve yeniden sınıflandırılan

### kaia → Temes Savsap

Kaia bir yaratık değil, bir MASKE ADI ve desen motifidir. Williams, Drama of Orokolo (1940) tam metninde 'kaia' yalnızca iki bağlamda geçiyor: hevehe maskelerinin adlandırma dağarcığında (s. 253) ve bir aualari desen adı olarak (Şekil 18, s. 306). Genel bir ruh kategorisi olarak tanımı yok. Dahası hevehe döngüsü erkek BAŞLATMA (initiation) törenidir ve malzemesi kısıtlıdır — SOURCING_STANDARD § 6 uyarınca kullanılamaz. İki bağımsız, kısıtlanmamış kaynak bulunamadı.

**Yerine gelen.** Deacon'ın Malekula malzemesinde (1934) belgelenmiş, yayımlanmış ve kısıtlanmamış bir EŞİK BEKÇİSİ. Kitabın tezine Kaia'dan çok daha iyi oturuyor: F ailesinin (eşik bekçisi) Okyanusya üyesi olarak Kérberos ve Ḫumbaba'nın yanına giriyor. Sınıf VI → I ve aile — → F değişimi Faz 2'nin sınıf dağılımı uzlaştırmasına devredildi.

### rusalka → sınıf VI

Rusalka IV (Su Sakinleri) olarak tohumlanmıştı. Ama Zelenin'in klasik çalışmasının BAŞLIĞI tezini söylüyor: *Umershie neestestvennoju smert'ju i rusalki* — 'Doğal olmayan ölümle ölenler ve rusalkalar' (Petrograd, 1916). Zelenin rusalkayı 'zaloжnye pokojniki' (huzursuz ölüler) kategorisinin içine yerleştirir: rusalka suda ÖLMÜŞ kızın DÖNÜŞÜDÜR. Sınıf VI (Huzursuz Ölüler) kaynağın kendi tezine uyuyor; sınıf IV yalnızca bulunduğu YERİ tarif ediyordu. Kitabın tasnifi işleve göredir, mekâna göre değil — bu düzeltme o ilkeyi uyguluyor. Yan etki: sınıf IV 25→24 (yol haritası hedefi tam olarak 24), sınıf VI 7→8 (taban).

---

## 5. Motif kodu düzeltmeleri — Faz 1'in en değerli bulgusu

Tam Motif-Index (A–G bölümleri) indirilip yerel olarak ayrıştırıldı:
**24.975 kod ve tanımı** çıkarıldı, **123 kod** projeye alındı.
Tohum tablosundaki kodlar **öneri**ydi; doğrulama iki **sistematik** hata buldu.

### ① `G264` gece cadısı ailesinin kodu değil

Tohum, C ailesinin **tamamına** (14 madde) `G264` atamıştı:

> **G264.** *La Belle Dame Sans Merci. Witch entices men with offers of love
> and then deserts or destroys them.*

Bu **erkekleri** baştan çıkaran bir figürdür. Loğusayı ve yeni doğanı avlayan
gece cadısıyla ilgisi yoktur. Doğru kodlar:

| Kod | Tanım | Kime |
|---|---|---|
| `G262.0.1` | Lamia. Witch who eats children | Lámia, Pontianak, Kenas-unarpe |
| `G442` | Child-stealing demon | Lamashtu, Lilith, Al Karısı, Qalupalik |
| `G262.1` | Witch sucks blood | Strix, Adze, Aswang, Manananggal, Krasue |
| `G262.1.3` | Witches suck blood from the navel of a child | Ma lai |
| `G262.5` | Witch takes out man's liver | Kumiho, Al Karısı |
| `G302.9.4` | Demons injure and strangle little children | Lilith |

> Kitabın **en güçlü tek bölümü** — dokuz geleneğin tek korkuda buluştuğu
> gece cadısı açılışı — yanlış bir kod üzerine kuruluydu. Yazımdan **önce**
> yakalandı.

### ② `B31` bir bölüm başlığıdır, `B31.1` 'Roc'tur

> ⚠ **Bu bulgu önceki turda YANLIŞ kaydedilmişti.** İlk kısmi okuma `B31`'i
> 'Roc' sanmıştı. Tam nüsha ayrıştırması düzeltti: `B31` bölüm başlığı
> (*Giant birds*), `B31.1` ise *Roc*. Tohum tablosunun Rukh için verdiği
> `B31.1` **baştan doğruydu**.

| Madde | Tohum | Doğru | Tanım |
|---|---|---|---|
| Sīmurgh | `B31` | **`B31.5`** | Simorg: giant bird |
| Garuḍa | `B31` | **`B56`** | Garuda-bird. Lower part man, upper part bird |
| Ziz | `B31` | **`B31.1.0.1`** | The bird Ziz |
| Anzû | `B31` | **`B31.1`** | Roc |
| Camazotz | `B31.1` | **`B31.4`** | Giant bat |
| Khyung · Animikii · Impundulu | `B31`/`B31.1` | **`A284.2`** | Thunderbird |
| Rukh | `B31.1` | **`B31.1`** ✓ | Roc — tohum doğruydu |

### ③ Tekil düzeltmeler

| Madde | Tohum | Doğru | Sebep |
|---|---|---|---|
| Húli jīng · Kumiho | `D113.1` | **`D113.3`** | `D113.1` = *man to **wolf***; `D113.3` = *man to fox* |
| Buda | `D113.2` | **`D110`** | Sırtlan köpekgil **değildir** (Hyaenidae ayrı familya) |
| Vârcolac | `D113.1` | **`A737.1`** | *Eclipse caused by monster devouring sun or moon* — işlevi kurt olmak değil AY YEMEK |
| Aralez | `B733` | **`E17`** | *Resuscitation by licking corpse* — birebir tanım; kod B değil E bölümünde |
| Cipactli | `A812` | **`A831`** | `A812` = *Earth Diver*; Cipactli'de yeryüzü GÖVDESİNDEN yapılır |
| Ammit | `G303` | **`E751.1`** | *Souls weighed at Judgment Day* — Ammit şeytan değil yargı aygıtı |
| Way | `D110` | **`E715`** | *Separable soul kept in animal* — way dönüşmez, AYRILIR |
| Draugr | `E230` | **`E422`** | *The living corpse* — hayalet değil, yürüyen ceset |
| Fenrir | `B871.1` | **`B871`** | `B871.1` = *giant **domestic** beasts*; kurt evcil değildir |
| Camazotz | `B31.1` | **`B31.4`** | Yarasa kuş değildir |
| Skuggabaldur | `B871` | **`B14`** | Dev değil MELEZ |
| Boitatá | `B11.1` | **`B19.4.2`** | *Fiery serpent* |
| Ông Ba Mươi | `B871` | **`B19.10`** | *Mythical tiger* |
| Herensuge | `B11` | **`B11.2.3.1`** | *Seven-headed dragon* |
| Masalai | `F400` | **`F460`** | Masalai bir YER ruhudur |
| Domovoy | `F480` | **`F482`** | `F480` bölüm başlığı; `F482` = *Brownie (nisse)* |
| Basajaun · Migoi · Curupira · Ochokochi · Almas | `F460` | **`F567`** | *Wild man* — G ailesinin tam kodu |
| Perī · ʿIfrīt | `F300`/`F402` | **`G307`** | *Jinn* |
| Xtabay | `F302` ✓ | `F302` | *Fairy mistress* — tohum doğruydu |

Bütün doğrulanmış tanımlar: [`01_SOURCE/motif_index.json`](../01_SOURCE/motif_index.json) — **123 kod**.
Tam çıkarım (24.975 kod): [`01_SOURCE/motif_index_full.json`](../01_SOURCE/motif_index_full.json).

---

## 6. Kaynak istatistikleri

| Kaynak katmanı | Sayı |
|---|---:|
| `primary` | 96 |
| `scholarly` | 143 |
| `reference` | 89 |
| **Toplam bağımsız künye** | **328** |

| Doğrulama seviyesi | Sayı | Güç |
|---|---:|---|
| `fulltext` | 4 | güçlü |
| `toc` | 6 | güçlü |
| `canon` | 42 | güçlü |
| `article` | 15 | güçlü |
| `sv` | 89 | güçlü |
| `catalog` | 172 | zayıf |
| `secondary` | 0 | zayıf |

Madde başına ortalama künye: **2.9**

---

## 7. Kısıtlılık taraması

Kilitlenen 112 maddenin **44**'inde kısıtlılık alanı dolduruldu.
Yaşayan gelenek maddelerinin **tamamı** tarandı.

| Madde | Bulgu | Karar |
|---|---|---|
| **Kaia** | Hevehe erkek **başlatma** töreninin maske adı — yaratık değil | ⛔ düştü → Temes Savsap |
| **Rangda** | Yaşayan tören; maske kutsanmış nesne | ⛔ düştü (kaynak doğrulanamadı) |
| **Zar** | Yaşayan uygulama; ruh adları kısıtlı — ayrıca 'yaratık' değil | ⛔ düştü |
| **Buda** | Beta Israel ve zanaatkâr kastlara yöneltilmiş **suçlama** | ✅ kalır — madde suçlamayı yeniden üretmeyecek |
| **Aswang** | Capiz sakinlerine yöneltilmiş suçlama | ✅ kalır — aynı etik dikkat |
| **Tokoloshe** | Büyücülük suçlaması; gerçek şiddete yol açmış | ✅ kalır — aynı etik dikkat |
| **Windigo** | 'Windigo psikozu' tanısı sömürge psikiyatrisinin kurgusu | ✅ kalır — tanı yeniden üretilmeyecek |
| **Pishtaco** | Yabancı linçleriyle ilişkili | ✅ kalır — sömürünün biçimi olarak anlatılacak |
| **Tupilaq** | Büyü uygulaması | ✅ kalır — yapım yöntemi ve sözler KULLANILMAZ |

### Kasıtlı dışarıda bırakılan

**Avustralya Aborjin gelenekleri.** Anlatı çoğunlukla topluluk
mülkiyetindedir ve kimin anlatabileceği kurala bağlıdır. Sonsöz'de bir
**tercih** olarak yazılacaktır.

---

## 8. Yedek aday havuzu — Faz 2 için

Düşen 8 madde için yedek aranmadı: kapsam 112'de kilitlendi ve bu sayı
tabanın (100) **üstünde**. Yedekler ancak kapsam yeniden açılırsa gerekir.

| Aday | Gelenek | Not |
|---|---|---|
| Ceffyl Dŵr | Kymru (41.) | Master yol haritası opsiyonel tutuyor |
| Kitsune | Yamato | B ailesinin üçüncü üyesi |
| Aos Sí | Ériu | H ailesinin beşinci üyesi |
| Langsuir | Nusantara | Skeat 1900'de pontianak'tan **ayrı** kaydedilmiş |

> Kütüphane erişimi sağlanırsa **öncelik düşen 8 maddedir** — özellikle
> Kartveli (Ochokochi, Kaji) ve Mongol (Almas, Chötgör), çünkü bu iki
> gelenek şu an tek maddeyle temsil ediliyor.
