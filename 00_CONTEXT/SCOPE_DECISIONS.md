# SCOPE DECISIONS — kapsam kararları kaydı

> **Bu dosya Faz 1'in en önemli çıktısıdır.**
> Kaynak bulunamayan her madde buraya yazılır. Boş kalan bir satır, sessizce
> uydurulmuş bir maddeden **çok daha iyidir**.
>
> Kural: *120 sayısı kutsal değildir; doğruluk kutsaldır.*
>
> Son ölçüm: **7 Ağustos 2026** · ölçüm komutu `python3 08_BUILD/research_gen.py --report`

---

## 1. Kapsam kapıları

| Kapı | Eşik | Şu an | Durum |
|---|---:|---:|---|
| Faz 1 tamamlanma — doğrulanmış madde | 112 | **13** | ⛔ kapalı |
| Kapsam tabanı | 100 | 120 (aday) | ✅ |
| Araştırılmış madde | 120 | **24** | 🔨 sürüyor |

**Uydurmayla doldurmak yasaktır.** Kaynak gösterilmesi bu kitabın tek
savunmasıdır; bir tek uydurma madde o savunmayı bütün kitap için geçersiz kılar.

---

## 2. Zor sekiz gelenek — ÖLÇÜM SONUCU

Yol haritası bu sekiz geleneği kapsam riskinin merkezi olarak işaretlemiş ve
Faz 1'in **onlarla başlamasını** emretmişti. Sekizi de tamamlandı. Sonuç:

| Gelenek | İşaret | Madde | Geçen | Durum |
|---|---|---:|---:|---|
| Ainu | ᚼ | 3 | **2** | ⚠ |
| Hayk | ✚ | 3 | **3** | ✅ |
| Ityop'ya | ✤ | 3 | **1** | ⚠ |
| Kartveli | ✛ | 3 | **0** | ⛔ |
| Melanesia | ◉ | 3 | **3** | ✅ |
| Mongol | ⚔ | 3 | **0** | ⛔ |
| Nusantara | ❋ | 3 | **1** | ⚠ |
| Sápmi | ❄ | 3 | **3** | ✅ |
| **Toplam** | | **24** | **13** | **%54** |

### Ne öğrendik

Zor sekiz gelenekte geçiş oranı **%54**. Yol haritasının
uyarısı doğrulandı: bu gelenekler İngilizce yayımlanmış kaynak açısından
gerçekten zayıf. Ama zayıflık **eşit dağılmıyor** — ayrım şu:

- **Geçenler**, hakemli makalesi veya dijitalleştirilmiş birincil etnografisi
  olan geleneklerdir (Sápmi'de Conrad'ın iki makalesi; Ainu'da Batchelor'ın
  tam metni; Melanezya'da Deacon'ın JRAI makalesi).
- **Geçmeyenler**, kaynağı var ama **dijital erişimi olmayan** geleneklerdir.
  Gürcü folklorunun temel derlemeleri (Virsaladze 1973, Chikovani 1946)
  mevcut ve gerçek; ama künye katalog düzeyinde doğrulanabiliyor, içerik
  düzeyinde doğrulanamıyor.

> **Bu bir kaynak yokluğu değil, kaynak ERİŞİMİ sorunudur** — ve çözümü
> kapsamı daraltmak değil, kütüphane erişimi almaktır. Yol haritasının Kurucu
> Notları bunu zaten öngörmüştü: *"Zor sekiz geleneğin kaynakları için
> üniversite kütüphanesi erişimi veya arşiv aboneliği gerekebilir. Bu,
> planlanmamış tek nakit kalemidir."* Ölçüm o kalemi **doğruladı**.

---

## 3. Düşen ve değişen maddeler

| # | Madde | Gelenek | Karar | Gerekçe |
|---|---|---|---|---|
| 120 | **Kaia** | Melanesia | ⛔ **düştü** → Temes Savsap | Bir yaratık değil, **maske adı ve desen motifi**. Williams, *Drama of Orokolo* (1940) tam metninde 'kaia' yalnızca hevehe maske adlandırma dağarcığında (s. 253) ve bir aualari desen adı olarak (Şekil 18, s. 306) geçiyor. Genel bir ruh kategorisi tanımı yok. Dahası hevehe erkek **başlatma** törenidir ve malzemesi kısıtlıdır. |

### Yerine gelen: Temes Savsap

Deacon'ın Malekula malzemesinde (1934) belgelenmiş, yayımlanmış ve
kısıtlanmamış bir **eşik bekçisi**: ölüler diyarının girişinde oturur ve
önündeki kum çizimini tamamlayamayan ölüyü geçirmez.

Kitabın tezine Kaia'dan **çok daha iyi** oturuyor: F ailesinin (eşik bekçisi)
Okyanusya üyesi olarak Kérberos ve Ḫumbaba'nın yanına giriyor. Ayrışma noktası
güçlü: **Kérberos güçle engeller, Temes Savsap bilgiyle** — geçiş bedeli kas
değil hafızadır.

Sınıf VI → I ve aile — → F değişimi Faz 2'nin sınıf dağılımı uzlaştırmasına
devredildi. Karar `01_SOURCE/scope_amendments.json`'da makine okunur hâlde.

---

## 4. Kapıdan geçmeyen maddeler

Bunlar **düşmedi** — doğrulaması tamamlanmadı. Her biri için engel yazılı.

| # | Madde | Gelenek | Engel |
|---|---|---|---|
| 65 | `repun-kamuy` | Ainu | hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |
| 77 | `orang-bunian` | Nusantara | hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |
| 78 | `rangda` | Nusantara | hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |
| 82 | `almas` | Mongol | hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |
| 83 | `olgoi-khorkhoi` | Mongol | hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil; yaşayan gelenek — restriction alanı boş |
| 84 | `chotgor` | Mongol | 1 bağımsız kaynak (≥2 gerekir; motif dizini sayılmaz); hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |
| 88 | `ochokochi` | Kartveli | hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |
| 89 | `kaji` | Kartveli | hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |
| 90 | `devi` | Kartveli | hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |
| 95 | `zar` | Ityop'ya | hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |
| 96 | `ganen` | Ityop'ya | 1 bağımsız kaynak (≥2 gerekir; motif dizini sayılmaz); hiçbir bağımsız kaynağın doğrulaması fulltext/toc/canon/article değil |

### Engel türlerine göre

- **11** madde — kaynaklar yalnızca katalog düzeyinde doğrulandı
- **2** madde — ikinci bağımsız kaynak bulunamadı

---

## 5. Motif kodu düzeltmeleri — Faz 1'in en değerli bulgusu

Tohum tablosundaki kodlar **öneri**ydi. Doğrulama iki sistematik hata buldu.
Her ikisi de kitabın **karşılaştırma açılışlarını** doğrudan ilgilendiriyor.

### ① G264 gece cadısı ailesinin kodu değil

Tohum tablosu **C ailesinin tamamına** (14 madde) `G264` atamıştı.
Doğrulanan tanım:

> **G264.** *La Belle Dame Sans Merci. Witch entices men with offers of love
> and then deserts or destroys them.*

Bu, **erkekleri** baştan çıkaran bir figürdür. Loğusayı ve yeni doğanı avlayan
gece cadısıyla ilgisi yoktur. Doğru kod:

> **G262.0.1.** *Lamia. Witch who eats children.*

— ki bu, ailenin Yunan üyesinin **adını taşıyor**. İlgili alt kodlar da
doğrulandı ve maddeye göre kullanılacak:

| Kod | Tanım | Kime |
|---|---|---|
| `G262.0.1` | Lamia. Witch who eats children | ailenin ortak kodu |
| `G262.1` | Witch sucks blood | Strix, Adze, Manananggal, Krasue |
| `G262.1.2` | Witch sucks blood from woman's or child's breasts | Al Karısı, Lamashtu |
| `G262.1.3` | Witches suck blood from the navel of a child | Ma lai |
| `G262.5` | Witch takes out man's liver | **Kumiho**, Al Karısı |
| `G302.9.4` | Demons injure and strangle little children | Lamashtu, Lilith |

> Kitabın **en güçlü tek bölümü** — dokuz geleneğin tek korkuda buluştuğu
> gece cadısı açılışı — yanlış bir motif kodu üzerine kuruluydu. Yazımdan
> **önce** yakalandı. Faz 1 tek başına bunun için bile değerdi.

### ② B31 'fırtına kuşu' değil 'Roc'

Tohum tablosu D ailesinin çoğuna `B31` atamıştı. Doğrulanan tanım:

> **B31.** *Roc. A giant bird which carries off men in its claws.*

Alt kodlar ayrı ayrı doğrulandı ve maddeler **kendi kodlarını** almalı:

| Madde | Tohum | **Doğru** | Tanım |
|---|---|---|---|
| Sīmurgh | `B31` | **`B31.5`** | Simorg: giant bird |
| Garuḍa | `B31` | **`B56`** | Garuda-bird. Lower part man, upper part bird |
| Ziz | `B31` | **`B31.1.0.1`** | The bird Ziz |
| Rukh | `B31.1` | **`B31`** | Roc |
| Animikii · Impundulu · Khyung | `B31` | **`A284`** (aday) | God of thunder |

> Anzû, Animikii, Impundulu ve Khyung **fırtına** kuşlarıdır, roc değil.
> `A284` ('God of thunder') doğrulandı ve Faz 2'de değerlendirilecek.

### ③ Tekil düzeltmeler

| Madde | Tohum | Doğru | Sebep |
|---|---|---|---|
| Húli jīng · Kumiho | `D113.1` | **`D113`** | `D113.1` = *Transformation: man to **wolf***. Tilki kurt değildir. `D113` = *man to canine animal (wild)* — tilki köpekgildir. |
| Buda | `D113.2` | **`D110`** | Sırtlan **köpekgil değildir** (Hyaenidae ayrı familya). `D110` = *man to wild beast (mammal)*. |
| Draugr | `E230` | **`E422`** (aday) | `E422` = *The living corpse. Revenant is not a specter but has the attributes of a living person* — draugr'ın tanımı bu. |
| Masalai | `F400` | **`F460`** | Masalai bir **yer** ruhudur; genel 'ruhlar ve cinler' kodu tanımlayıcı özelliğini kaybediyor. |
| Vishap | `B11` | **`B11.3`** | `B11.3` = *Habitat of dragon*. Vişapı ayıran şey ejderha olması değil, dağ gölüne **bağlı** olması. |
| Gufihtar | `F300` | **`F400`** | `F300` bağımsız tanım taşımıyor (yalnızca bölüm başlığı). |

Bütün doğrulanmış tanımlar: [`01_SOURCE/motif_index.json`](../01_SOURCE/motif_index.json) — **67 kod**, iki dijital nüshadan birebir.

---

## 6. Yedek aday havuzu

| Aday | Gelenek | Sınıf | Not |
|---|---|---|---|
| Ceffyl Dŵr | Kymru (41. gelenek) | IV | Master yol haritası **opsiyonel** tutuyor. Kapsam 40'ta kilitlenirse yalnızca A ailesi açılışında anılır. |
| Kitsune | Yamato | III | B ailesinin üçüncü üyesi; bir Yamato maddesi düşerse ilk yedek. |
| Aos Sí | Ériu | I | H ailesinin beşinci üyesi; aynı durum. |
| Langsuir | Nusantara | II/VI | Skeat 1900'de pontianak'tan **ayrı** kaydedilmiş; bağımsız madde olabilir. |

---

## 7. Kısıtlılık taraması — yaşayan gelenekler

Araştırılan 24 maddenin tamamında `restrictionScreened` alanı dolduruldu.
Üç madde **kısıtlılık gerekçesiyle** özel not taşıyor:

| Madde | Bulgu | Karar |
|---|---|---|
| **Kaia** | Hevehe erkek başlatma töreninin maske adı | ⛔ **düştü** |
| **Rangda** | Yaşayan tören uygulaması; maske kutsanmış nesne | ✅ kalır — Belo'nun yayımlanmış betimlemesi kullanılır; **maske birebir çizilmez**, tören sırası ve mantra kullanılmaz |
| **Zar** | Yaşayan uygulama; ruh adları ve davet formülleri kısıtlı | ⚠ kalır ama yalnızca akademik betimleme; Faz 2'de 'yaratık' sayılıp sayılmayacağı yeniden değerlendirilecek |
| **Buda** | Gerçek topluluklara (Beta Israel, zanaatkâr kastlar) yöneltilmiş **suçlama** | ⚠ kalır — madde suçlamayı yeniden üretmeyecek; Reminick'in toplumsal çözümlemesi maddenin parçası olacak |

### Kasıtlı dışarıda bırakılan

**Avustralya Aborjin gelenekleri.** Anlatı çoğunlukla topluluk mülkiyetindedir
ve kimin anlatabileceği kurala bağlıdır. Sonsöz'de bir **tercih** olarak
yazılacaktır.

---

## 8. Motif kodu doğrulama kaydı

| Durum | Sayı |
|---|---:|
| Doğrulanmış tanım (motif_index.json) | 67 |
| `motifVerified: true` madde | 11 |
| Düzeltilen tohum kodu | 8 |
| Doğrulanamayan tohum kodu | 12 |

Doğrulanamayan kodların çoğu Thompson'ın **B400–B899** ve **D1000+**
aralığındadır; bu aralıklar bu turda erişilen dijital nüshalarda yer almıyor.
Faz 2'de tam nüshadan (Indiana University Press baskısı veya HathiTrust)
teyit edilecek.
