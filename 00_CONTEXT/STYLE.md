# STYLE — Codex Bestiarium yazım kuralları

> **Bu belge yazımın anayasasıdır.** Her madde yazılırken bağlama girer.
> `qa_voice.py` buradaki yasakların çoğunu otomatik denetler; denetlemediği
> kısım editoryal yargıdır ve o da burada yazılıdır.
>
> Kitabın dili **İngilizce**. Bu belge Türkçedir; örnekler İngilizcedir.

---

## 1. Tek cümlelik kural

**Belirsizlik cümlede değil, kaynak notunda yönetilir.**

Bu kitabın tek savunması kaynak göstermesidir. Cümleye "it is said" koymak,
o savunmayı cümle düzeyinde terk etmek demektir: okur, yazarın da emin
olmadığını anlar. Emin olunmayan şey yazılmaz; emin olunan şey **bildirici
kiple** yazılır ve nereden bilindiği yedinci bölümde söylenir.

---

## 2. Ses

### Yapılacak

| Kural | Örnek |
|---|---|
| **Bildirici kip.** | ✅ *"It waits at the ford."* — ❌ *"It is said to wait at the ford."* |
| **Somut ölçü.** Sıfat değil, sayı. | ✅ *"A wingspan the length of a boat."* — ❌ *"A gigantic wingspan."* |
| **Kayıtlı vaka.** Mümkün olduğunda tarih ve yer. | ✅ *"A boy from Lough Neagh mounted one in 1808."* |
| **Kısa cümle, uzun paragraf.** Ortalama 14–18 kelime. | Ritim, sözlü anlatının ritmidir. |
| **Yorum tek yerde.** Yalnızca 5. bölümde ("neden korkulur"). | Başka yerde yorum varsa taşı. |
| **Diakritikler korunur.** | Ḫumbaba · Sīmurgh · Húli jīng · Àbíkú |

### Yasak

| Yasak | Neden |
|---|---|
| *"It is said", "legend has it", "some say", "reputedly", "supposedly"* | Belirsizlik kaynak notunun işidir. |
| Oyun terminolojisi: *hit points, saving throw, weakness to, challenge rating* | Bu bir oyun kitabı değildir. |
| Uydurma detay | Kaynağı olmayan hiçbir özellik yazılmaz. **Boşluk bırakmak daha iyidir.** |
| Sevimlileştirme: *"actually quite", "misunderstood creature", "deep down"* | Yaratıkları sevimlileştiren her cümle kitabın gücünü düşürür. |
| Karşılaştırmalı üstünlük: *"the most terrifying", "the most famous"* | Ölçülemez iddia. |
| **Ünlem işareti** | Tüm kitapta **sıfır**. |

> `qa_voice.py` bu listelerin tamamını tarar. Liste `08_BUILD/bestiarium.py`
> içindedir; değişirse orada değişir, burada değil — ikisi ayrışırsa
> **kod geçerlidir**.

---

## 3. Yedi bölümlü madde yapısı

Her madde **tam olarak** bu sırayı izler. Sıra değişmez. Bir bölüm boşsa
madde **yazılmamıştır, kısaltılmamıştır**.

| # | Bölüm | Kelime | Kural | Örnek açılış |
|---|---|---:|---|---|
| 1 | **Açılış cümlesi** | 25–40 | Tek cümle. Tereddüt yok. Yaratığı **bir eylemle** tanımla. | *"It stands at the water's edge and waits to be ridden."* |
| 2 | **Nerede anlatılır** | 70–110 | Coğrafya + en erken kayıt. Tarih verilir; *"eski çağlardan beri"* yazılmaz. | *"Reported from the loughs of Connacht and the sea-lochs of the Hebrides…"* |
| 3 | **Neye benzer** | 110–160 | Somut, duyusal, tek paragraf. Ölçü verilir. Sıfat yığmak yasak. | *"A horse the colour of wet slate, its mane always dripping…"* |
| 4 | **Ne yapar** | 180–260 | Maddenin kalbi. Bir **olay** anlatılır — mümkünse kayıtlı bir vaka. | *"A boy from Lough Neagh mounted one in 1808…"* |
| 5 | **Neden korkulur veya sayılır** | 90–140 | İnsanî ihtiyaç. **Yorum burada yapılır, başka yerde değil.** | *"Every lough in Ireland has drowned someone…"* |
| 6 | **Akrabaları** | 50–80 | 2–5 çapraz referans, sayfa numarasıyla. Ayrışma noktası bir cümlede. | *"Compare Nykur (p. 214), Näkki (p. 209)…"* |
| 7 | **Kaynak notu** | 30–50 | Kısa künye + motif kodu. Varyant varsa burada. | *"Croker II:73; Thompson B184.1.3."* |

**Toplam hedef: 700 kelime ± %12 → 620–790.**

Bu bant **sert bir kısıttır**:
- 620'nin altı → madde yüzeysel, "başvuru cildi" iddiası düşer
- 790'ın üstü → kitap 440 sayfaya taşar, baskı maliyeti ve fiyat bozulur

`qa_length.py --sections` hem toplamı hem yedi bölümün her birini denetler.
Toplam bandı tutturup bölüm bandını kaçıran madde, biçimi doğru ama **oranı
bozuk** maddedir; o da yakalanır.

> **7. bölüm yasak kalıp taramasından muaftır.** Kaynak notunda *"reported",
> "attested", "recorded"* gibi ifadeler yerindedir — belirsizliğin yönetildiği
> yer orasıdır.

---

## 4. Adlandırma

1. **Birincil ad geleneğin kendi romanizasyonudur** ve diakritikleri korunur.
   Diakritik düşürmek, Mendîran'daki hatanın tekrarı olur.
2. **Alternatif yazımlar** `spec.json` → `altNames` alanında toplanır ve
   dizinde çapraz gönderme yapılır (okur "Aughisky" arar, "Each-uisce"a gider).
3. **İngilizce yerleşik ad varsa** parantezde **bir kez** verilir, sonra
   kullanılmaz.
4. **Telaffuz her maddede zorunludur** — hem okur için hem sesli kitap için.
5. **Tanrı adları** yalnızca gerektiğinde geçer. Bu kitap tanrıları değil
   **yaratıkları** anlatır; tanrı gerekiyorsa Codex Mythologica'ya gönderme
   yapılır.

`qa_diacritics.py` bir adın diakritiksiz hâlinin metinde geçtiği her yeri bulur.

---

## 5. Lore ve kaynak kuralları

### İki bağımsız kaynak kuralı

Hiçbir madde tek kaynakla yazılmaz. İkinci kaynak bulunamıyorsa **madde
listeden düşer**. 120 sayısı kutsal değildir; **doğruluk kutsaldır.**

Motif dizini (Thompson) *bağımsız kaynak sayılmaz* — o bir tasniftir, bir
tanıklık değil. `validate_spec.py` bunu ayırır.

### Varyantlar gizlenmez, gösterilir

> *"İskoçya'da yer, İrlanda'da yalnızca boğar."*

Çelişki bir kusur değil, kitabın otoritesinin kanıtıdır.

### Modern kurgu kaynak sayılmaz

Bir yaratığın Tolkien, D&D veya bir video oyunundaki hâli kitabın konusu
değildir. Popüler kültür etkisi varsa **tek cümlede** ve **"modern" etiketiyle**
anılır. `qa_voice.py` etiketsiz göndermeyi yakalar.

### Yaşayan geleneklerde ek kapı

İnuit, Ainu, Sápmi, Anishinaabe, Māori ve diğer Okyanusya, Nguni, Amazon,
Andean, Tibet, Moğol ve Etiyopya gelenekleri için:

> Yalnızca **yayımlanmış ve kısıtlanmamış** malzeme kullanılır.
> Kısıtlı olduğu bilinen anlatı **anlatılmaz — kısıtlı olduğu söylenir.**

Bu, kitabın etik omurgasıdır ve **pazarlama malzemesi değildir**.
`spec.json` → `restrictionScreened` alanı Faz 1 kapısında zorunludur.

### Kasıtlı dışarıda bırakılanlar

**Avustralya Aborjin gelenekleri kitaba alınmamıştır.** Sebep kapsam eksikliği
değildir: bu geleneklerin çoğu anlatı **topluluk mülkiyetindedir** ve kimin
anlatabileceği kurala bağlıdır. Kaynağı doğrulanamayan ve izni olmayan
malzemeyi bir başvuru cildine koymak, kitabın kendi standardını ihlal eder.

Bu karar **Sonsöz'de açıkça yazılacaktır** — bir eksik olarak değil, bir
tercih olarak. Savunmacı bir dille değil, bir standart beyanı olarak.

---

## 6. Tipografi ve noktalama

| Kural | Doğru | Yanlış |
|---|---|---|
| Tırnak | `“…”` `‘…’` | `"…"` `'…'` |
| Uzun tire | `—` (boşluksuz veya ince boşluklu) | `--` · ` - ` |
| Üç nokta | `…` | `...` |
| Kesme | `’` | `'` |

`validate_structure.py` belgelerde, `qa_voice.py` metinde denetler.
Metinde düz tırnak veya ` - ` görülürse dizgiye giden yolda bir yerde
normalizasyon atlanmış demektir.

---

## 7. Ses kalibrasyon örnekleri

> **Faz 1 görevi.** Codex Mythologica'dan **gerçek** üç paragraf buraya
> kopyalanacak: biri anlatı, biri betimleme, biri yorum. Bunlar uydurulmaz —
> `../CODEX_MYTHOLOGICA/01_SOURCE/book-edited.json` içinden seçilir ve
> kaynağı (hikâye adı, bölüm) belirtilir.
>
> Amaç: yeni ciltteki sesin Cilt 1'le aynı olduğunu **ölçebilmek**. Örnekler
> yerleştirilmeden Faz 3'e (yazım) geçilmez.

```
[ Örnek 1 — anlatı sesi ]      → Faz 1'de doldurulacak
[ Örnek 2 — betimleme sesi ]   → Faz 1'de doldurulacak
[ Örnek 3 — yorum sesi ]       → Faz 1'de doldurulacak
```

---

## 8. Her madde için kalite kontrol listesi

Bir madde "yazıldı" sayılmadan önce:

- [ ] Yedi bölümün hepsi var ve **sırada**
- [ ] Kelime sayısı 620–790 bandında
- [ ] Her bölüm kendi bandında
- [ ] En az **iki bağımsız kaynak**, künyeleriyle
- [ ] En az bir **Thompson motif kodu**, doğrulanmış
- [ ] Telaffuz alanı dolu
- [ ] 2–5 akraba çapraz referansı, **karşılıklı**
- [ ] Yasak kalıp taraması temiz (`qa_voice.py`)
- [ ] Plaka kimliği atanmış ve tutarlılık bandında
- [ ] Diakritikler doğru (`qa_diacritics.py`)
- [ ] Düşman denetçi oturumundan geçti (Faz 5)

---

## 9. Üretim disiplini

**Tek seferde en fazla üç madde.**

Dördüncü maddeye başlarken bağlamda üç maddenin metni durur ve dördüncü
onların ritmine kayar. Bu bir tercih değil, portföy denetiminde **ölçülmüş
bir hatadır**.

Girdi her seferinde şu üçlüdür:

1. O maddenin araştırma dosyası (`01_SOURCE/research/<id>.md`)
2. Bu belge (`STYLE.md`)
3. Yedi bölümlü şablon

Daha fazlası üslup sürüklenmesi üretir. `qa_drift.py` haftalık (Faz 4'ten
itibaren her beş maddede) çalışır ve en sık 50 kelimede yükselen eğim arar.
