# Koropokkuru — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `koropokkuru` |
| **Ad** | Koropokkuru |
| **Alternatif yazımlar** | Korpokkur, Koro-pok-guru |
| **Gelenek** | Ainu ᚼ · Doğu Asya |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | H · Gizli halk |
| **Plaka** | `plate-064` |
| **Telaffuz (taslak)** | ko-ro-POK-koo-roo |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `fulltext`

- **Künye:** John Batchelor, *The Ainu and Their Folk-Lore* (Londra: Religious Tract Society, 1901)
- **Erişim:** archive.org/details/b29010664 — tam metin okundu
- **Yer:** Bölüm II — "The Pit-dwellers and Causes of Ainu Decrease"
- **Not:** Bölüm başlığı ve alıntı dijital tam metinden birebir okundu. Faz 5 turunda aynı bölümden İKİNCİ bir kayıt daha çıkarıldı: Batchelor yaprağı KENDİSİ ölçmüş — 'The largest burdock leaf I have ever seen on the island measured 4 feet 1 inch across when spread out, while the length of the stem was a good bit over 5 feet.' Ayrıca ikinci bir rivayet kaydediyor: cüceler bir iki kadem daha uzun, ve bir yaprağın altına beş ila on kişi sığınıyor.
- **İlgili alıntı:**

  > ten of them could easily take shelter beneath one burdock leaf

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Donald L. Philippi, *Songs of Gods, Songs of Humans: The Epic Tradition of the Ainu* (Tokyo/Princeton: University of Tokyo Press ve Princeton University Press, 1979)
- **Not:** Ainu kamuy yukar (tanrı destanları) külliyatının standart İngilizce eleştirel çevirisi.

### Kaynak 3 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F451` | Dwarfs in otherworld | ✅ |

**Gerekçe.** Tohum kodu F451 doğrulandı ve korundu. Koropokkuru çukur evlerde yaşayan küçük halktır; Thompson'ın cüce kümesi uyuyor. Ad Ainu'da 'altında yaşayan kişi' anlamına gelir ve Batchelor'ın devetabanı yaprağı alıntısı bunu doğrudan destekler.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Hokkaidō ve Kuril adaları; Ainu anlatılarında adanın ÖNCEKİ sakinleri
- **İlk kayıt (attested):** Batchelor'ın 1890'lardaki saha çalışmasından; 1901'de yayımlandı

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Çok küçük; Batchelor'ın kaydında bir 'burdock' yaprağının altına on kişi sığar
- Batchelor'ın ölçtüğü yaprak: 4 kadem 1 parmak eninde, sapı 5 kademden uzun
- Çukur evlerde (pit-dwelling) yaşar

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Ainu'dan önce adada yaşamış sayılır; çukur evleri ve taş aletleri onlara atfedilir. Balık bırakıp görünmeden kaybolduğu anlatılır.
- **Kayıtlı vaka:** Batchelor 1901, II. bölüm: derleyicinin KENDİ ölçümü. Ainu'dan 'onu bir yaprağın altına sığar' kaydını aldıktan sonra adada gördüğü en büyük yaprağı ölçüyor — açıldığında 4 kadem 1 parmak (yaklaşık 125 cm) eninde, sapı 5 kademden (yaklaşık 150 cm) uzun. Yani ölçü bir abartı değil, saha derleyicisinin sınadığı bir karşılaştırmadır. Batchelor ilk rivayetin 'büyük bir abartı' olduğunu kendisi söyler ve bir iki kadem daha uzun cücelerin geçtiği ikinci rivayeti de yanına koyar.
- **Karşı önlem:** Kaynakta doğrulanmış karşı önlem yok.

## 6. Varyantlar

| Bölge / kaynak | Fark |
|---|---|
| Batchelor 1901 | Ainu atalarınca yok edilmiş bir halk olarak anlatılır — arkeolojik açıklama işlevi taşır |

**Varyant notu.** Koropokkuru anlatısı bir yaratık anlatısı olduğu kadar bir ARKEOLOJİ açıklamasıdır: adadaki çukur ev kalıntılarına ad verir.

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Huldufólk** `huldufolk` | Ísland ❆ | `kin` | Huldufólk şimdiki zamandadır, Koropokkuru geçmiş zamanda — biri komşu, öteki önceki halk. |
| **Tokoloshe** `tokoloshe` | Nguni ◈ | `function` | İki küçük halk, iki ahlak: Koropokkuru balık bırakır, Tokoloshe geceleri gelir. |
| **Ulda** `ulda` | Sápmi ❄ | `kin` | Koropokkuru balık bırakıp kaybolur — verir; Ulda sürü güder ve adı anılmaz — kendi işine bakar. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Yalnızca yayımlanmış malzeme kullanıldı (Batchelor 1901 tam metin, Philippi 1979). Ainu tören bilgisi, iyomante ayrıntısı ve inaw yapımı KULLANILMAZ. Plakada gerçek bir Ainu deseni veya tören nesnesi çizilmez. Batchelor'ın misyoner çerçevesi eleştirel okunur; 'yok edildiler' anlatısı bir Ainu anlatısı olarak aktarılır, tarihsel gerçek olarak değil.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Gizli halk ailesinin (H) Doğu Asya üyesi — Huldufólk ve Ulda ile yan yana.
- Ayrışma noktası: Huldufólk hâlâ YANIBAŞIMIZDA, Koropokkuru ÖNCEKİ sakin. Biri şimdiki zamanda, diğeri geçmişte gizli.
- DİKKAT — BİTKİ ADI. Batchelor'ın İngilizcesi 'burdock' (dulavratotu, Arctium) diyor. Maddede 'butterbur' (devetabanı, Petasites japonicus / Ainu ve Japon kaynaklarındaki fuki) yazıldı. 4 kademlik yaprak fuki'ye uyar, dulavratotuna uymaz; yani düzeltme muhtemelen DOĞRUDUR ama kaynağın sözcüğü SESSİZCE değiştirilmiş olur. Kural: kaynağın dediği yazılır, ayrım gösterilir. Satır editörlüğü geçişinde ya Batchelor'ın sözcüğü kullanılacak ya da fark bir cümleyle söylenecek.
- Faz 5 kayıtlı vaka turu: derleyicinin kendi ölçümü, 4. bölüm için kayıtlı vaka ölçütünü karşılar.

## Kontrol listesi

- [x] En az iki bağımsız kaynak, tam künyeyle
- [x] En az biri primary/scholarly
- [x] En az biri kesin-yer doğrulamalı (fulltext/toc/canon/article)
- [x] Motif kodu doğrulandı ve gerekçelendirildi
- [x] Bölge somut, ilk kayıt tarihli
- [x] Fiziksel tarif kaynağa dayanıyor
- [x] Kısıtlılık taraması yapıldı (yaşayan gelenekse)
- [x] Telaffuz taslağı yazıldı
- [x] Bu dosyada proza cümlesi yok

