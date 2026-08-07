# SOURCING STANDARD — kaynak gösterme ölçütü

> **Bu belge Faz 1'de yazıldı ve kitabın tek savunmasını tanımlar.**
> Yol haritası "iki bağımsız kaynak" der ama *neyin* kaynak sayıldığını,
> *nasıl* künyeleneceğini ve *ne kadarının* doğrulanmış sayılacağını
> söylemez. Bu belge onu söyler.
>
> Yazıldı: 7 Ağustos 2026 · Faz 1

---

## 1. Neden bu belge var

Bu kitabın rakiplerinden tek farkı kaynak göstermesidir. Bir tek uydurma
künye, o farkı **bütün kitap için** geçersiz kılar — ve bir okur bunu bulur.

Ama tersi de doğru: doğrulayamadığı için hiçbir şey yazmayan bir yazar,
kitabı yazamaz. Ölçüt net olmalı.

---

## 2. Kaynak katmanları

Her kaynak dört katmandan birine girer. `spec.json` → `sources[].type`.

| Katman | Ne | Örnek | Bağımsız sayılır mı |
|---|---|---|---|
| `primary` | Birincil metin veya saha etnografisi | *Poetic Edda*; Fox, *The Threshold of the Pacific* (1924) | ✅ |
| `scholarly` | Hakemli akademik ikincil çalışma | Lindow, *Norse Mythology* (2001) | ✅ |
| `reference` | Yayımlanmış başvuru cildi / ansiklopedi | Rose, *Giants, Monsters, and Dragons* (2000) | ✅ |
| `index` | Motif veya masal tipi tasnifi | Thompson, *Motif-Index* | ❌ **asla** |

### İki bağımsız kaynak kuralı

Bir madde `verified` olabilmek için **en az iki** `index` olmayan kaynağa
ihtiyaç duyar ve bunlardan **en az biri** `primary` veya `scholarly` olmalıdır.

> İki ansiklopedi maddesi iki bağımsız kaynak **değildir** — ikisi de büyük
> ihtimalle aynı üçüncü kaynaktan türemiştir. Ansiklopedi bir *teyit*tir,
> bir *tanıklık* değildir.

Motif dizini asla bağımsız kaynak sayılmaz: o bir **tasniftir**, bir
tanıklık değil. Bir yaratığın `B184.1.3` altında sınıflandırılmış olması,
o yaratığın anlatıldığını değil, anlatının bir *türe* ait olduğunu söyler.

---

## 3. Künye biçimi ve **sayfa numarası kuralı**

Bu, en kolay ihlal edilen kuraldır. Doğrulanmamış bir sayfa numarası
yazmak, uydurma kaynak yazmakla **aynı şeydir** ve daha sinsidir çünkü
doğru görünür.

| Kaynak tipi | Doğru künye | Neden |
|---|---|---|
| Numaralı birincil metin | *Völuspá* 45–47 · *Kalevala* runo 26 · *Nihon Shoki* II | Numaralandırma metnin kendisinden gelir; sayfaya bağlı değildir |
| Başvuru cildi / ansiklopedi | Rose (2000), **s.v.** "Each-uisge" | Madde başlığıyla künye vermek **standarttır**; sayfa gereksizdir |
| Bölümlü monografi | Fox (1924), **Bölüm X** ("Adaro Spirits") | Bölüm başlığı doğrulandıysa yeter |
| Makale | Mead, *Anthropological Quarterly* 51:1 (1978), 69–75 | Sayfa aralığı künyenin parçasıdır ve doğrulanabilir |
| **Sayfası doğrulanmamış kitap** | sayfa **YAZILMAZ** | Uydurma sayfa = uydurma kaynak |

> **Kural:** sayfa numarası ancak (a) metnin kendi numaralandırmasıysa,
> (b) makale künyesinin parçasıysa veya (c) **gerçekten görüldüyse** yazılır.
> Aksi hâlde `s.v.` veya bölüm başlığı kullanılır. Boş bırakmak, uydurmaktan
> her zaman iyidir.

---

## 4. Doğrulama seviyeleri

Her kaynağın `verification` alanı, o künyenin **nasıl** teyit edildiğini
söyler. Bu alan boş bırakılamaz.

| Seviye | Anlamı | Güç |
|---|---|---|
| `fulltext` | Dijital nüshanın tam metni görüldü; alıntı birebir | güçlü |
| `toc` | İçindekiler veya bölüm başlığı görüldü; içerik oradan teyit edildi | güçlü |
| `article` | Cilt, sayı, sayfa aralığı ve kalıcı kimliği (DOI/JSTOR) doğrulanmış hakemli makale. Yer kesin ve kalıcıdır | güçlü |
| `canon` | Kendi iç numaralandırması olan standart eleştirel metin: *Völuspá* 45, *Kalevala* runo 26, *Nihon Shoki* II, Pliny *NH* VIII.32. Yer, metnin kendi atıf sistemidir ve baskıdan bağımsızdır | güçlü |
| `catalog` | Kütüphane/arşiv kataloğunda künye doğrulandı (varlık kesin, içerik değil) | zayıf |
| `secondary` | Başka bir yayımlanmış çalışmanın atfı üzerinden bilinir | zayıf |

Bir maddenin iki bağımsız kaynağından **en az birinin** doğrulaması
`fulltext`, `toc`, `canon` veya `article` olmalıdır.

> **Güç ölçütü "okudum mu" değil, "okur gidip bakabilir mi"dir.**
> Bir künye, okuru KESİN ve KALICI bir yere götürüyorsa güçlüdür. *Völuspá* 45
> her baskıda aynı kıtadır; JRAI 64 (1934), 129–175 her kütüphanede aynı
> makaledir; "Fox 1924, Bölüm X" doğrulanmış bir bölüm başlığıdır. Buna
> karşılık yalnızca "şu kitap vardır ve konuyu işler" demek, okuru 400 sayfaya
> gönderir — bu zayıftır.

> **`canon` neden güçlü sayılır?** Çünkü "Völuspá 45" bir sayfa numarası
> değildir; metnin kendi kıta numarasıdır ve her eleştirel baskıda aynı
> yeri gösterir. Böyle bir atıf, belirli bir nüshayı görmeyi gerektirmez —
> atıf sisteminin kendisi doğrulamadır. Buna karşılık "Fox 1924, s. 137"
> ancak o sayfa **görüldüyse** yazılabilir.
>
> `canon` yalnızca gerçekten numaralandırılmış metinler için kullanılır:
> destanlar, kutsal metinler, klasik eserler, saga ve edda şiirleri.
> Modern bir monografi `canon` olamaz.

---

## 5. Motif kodu doğrulaması

Tohum tablosundaki kodlar **önerilmiştir**. Bir kod `motifVerified: true`
olabilmek için:

1. Kod biçimsel olarak geçerli olmalı (`validate_spec.py` denetler), **ve**
2. Kodun Thompson tasnifindeki **tanımı** yazılmalı ve yaratığa uyduğu
   gösterilmeli.

Kod yaratığa uymuyorsa **değiştirilir** ve değişiklik araştırma dosyasına
gerekçesiyle yazılır. Tohum tablosuna sadakat, doğruluğun önüne geçmez.

> `motifNote` alanı bu gerekçeyi taşır ve boş bırakılamaz.

---

## 6. Yaşayan gelenek kapısı

`bestiarium.py` → `LIVING_TRADITIONS` listesindeki gelenekler için ek kapı:

- Yalnızca **yayımlanmış ve kısıtlanmamış** malzeme kullanılır.
- Kısıtlı olduğu bilinen anlatı **anlatılmaz — kısıtlı olduğu söylenir**.
- Tören nesnesi, maske deseni, klan işareti, başlatma (initiation) bilgisi
  ve yer-özel kutsal anlatı **kullanılmaz**, plakada **çizilmez**.
- Tarama sonucu `restrictionScreened: true` ve araştırma dosyasında
  **açık bir cümleyle** kaydedilir.

Bu, kitabın etik omurgasıdır ve pazarlama malzemesi değildir.

### Kasıtlı dışarıda bırakılan

**Avustralya Aborjin gelenekleri.** Anlatı çoğunlukla topluluk
mülkiyetindedir ve kimin anlatabileceği kurala bağlıdır. Kaynağı
doğrulanamayan ve izni olmayan malzemeyi bir başvuru cildine koymak,
kitabın kendi standardını ihlal eder. Sonsöz'de bir **tercih** olarak
yazılacaktır.

---

## 7. Bir madde ne zaman düşer

Aşağıdakilerden **herhangi biri** doğruysa madde listeden düşer ve
`SCOPE_DECISIONS.md`'ye gerekçesiyle yazılır:

- İkinci bağımsız kaynak bulunamadı
- Bulunan kaynakların hepsi `reference` katmanında ve hiçbiri `primary`/`scholarly` değil
- Bütün doğrulamalar `catalog` veya `secondary` seviyesinde kaldı
- Malzeme kısıtlı çıktı
- Motif kodu doğrulanamadı **ve** uygun bir alternatif bulunamadı

**120 sayısı kutsal değildir; doğruluk kutsaldır.**

---

## 8. Yasak

- Görmediğin bir sayfa numarasını yazmak
- "Muhtemelen şu kaynakta vardır" diye künye yazmak
- İki ansiklopediyi "iki bağımsız kaynak" saymak
- Motif dizinini bağımsız kaynak saymak
- Wikipedia'yı kaynak olarak künyelemek (kaynaklarına **gitmek** serbesttir
  ve teşvik edilir; kendisi künyelenmez)
- Kısıtlı olduğu bilinen bir anlatıyı "zaten yayımlanmış" diye kullanmak
