# SCOPE DECISIONS — kapsam kararları kaydı

> **Bu dosya Faz 1'in en önemli çıktısıdır.**
> Kaynak bulunamayan her madde buraya yazılır. Boş kalan bir satır, sessizce
> uydurulmuş bir maddeden **çok daha iyidir**.
>
> Kural: *120 sayısı kutsal değildir; doğruluk kutsaldır.*

---

## 1. Kapsam kapıları

| Kapı | Eşik | Ne olur |
|---|---:|---|
| Faz 1 tamamlanma | **≥112** madde iki bağımsız kaynakla doğrulanmış | Yedeklerle 120'ye tamamlanır |
| Kapsam tabanı | **100** | Altına inilirse kitap yeniden planlanır ve alt başlık değişir |
| Erken uyarı | 3. haftada **<70** doğrulanmış madde | 120/40 hedefi gerçekçi değil; 100/35'e inilir |

**Uydurmayla doldurmak yasaktır.** Kaynak gösterilmesi bu kitabın tek
savunmasıdır; bir tek uydurma madde o savunmayı bütün kitap için geçersiz
kılar.

---

## 2. Kaynak riski yüksek sekiz gelenek

Master yol haritası Bölüm 04 uyarısı: bu gelenekler İngilizce yayımlanmış
kaynak açısından zayıftır ve **projenin en olası kapsam riskidir**. Faz 1
bunlarla **başlar** — kolay gelenekler (Hellenic, Norðr, Yamato) sona
bırakılır, çünkü onları erken bulmak yanlış bir güven verir.

| Gelenek | İşaret | Maddeler | Kaynak durumu | Yedek aday |
|---|---|---|---|---|
| Melanesia | ◉ | Adaro · Masalai · Kaia | ⬜ aranmadı | — |
| Ainu | ᚼ | Koropokkuru · Repun Kamuy · Kenas-unarpe | ⬜ aranmadı | — |
| Kartveli | ✛ | Ochokochi · Kaji · Devi | ⬜ aranmadı | — |
| Hayk | ✚ | Vishap · Aralez · Nhang | ⬜ aranmadı | — |
| Sápmi | ❄ | Stállu · Ulda · Gufihtar | ⬜ aranmadı | — |
| Nusantara | ❋ | Pontianak · Orang Bunian · Rangda | ⬜ aranmadı | — |
| Ityop'ya | ✤ | Buda · Zar · Ganen | ⬜ aranmadı | — |
| Mongol | ⚔ | Almas · Olgoi-Khorkhoi · Chötgör | ⬜ aranmadı | — |

Durum işaretleri: ⬜ aranmadı · 🔍 aranıyor · ✅ iki kaynak bulundu ·
⚠ tek kaynak · ❌ kaynak yok, düşürüldü

---

## 3. Düşürülen maddeler

> Faz 1 boyunca doldurulur. Her satır bir karardır ve **gerekçesi zorunludur**.

| # | Madde | Gelenek | Neden düşürüldü | Yerine gelen | Tarih |
|---|---|---|---|---|---|
| — | *(henüz yok)* | | | | |

---

## 4. Yedek aday havuzu

> Düşen bir maddenin yerine geçebilecek adaylar. Aynı gelenek ve mümkünse
> aynı sınıftan olmalı — sınıf dağılımı bozulmasın.

| Aday | Gelenek | Sınıf | Motif (öneri) | Not |
|---|---|---|---|---|
| Ceffyl Dŵr | Kymru (41. gelenek) | IV | `B184.1.3` | Master yol haritası **opsiyonel** tutuyor. Kapsam 40'ta kilitlenirse yalnızca A ailesi karşılaştırma açılışında anılır, kendi maddesi olmaz. |
| Kitsune | Yamato | III | `D113.1` | B ailesinin üçüncü üyesi; Yamato'nun üç maddesi dolu olduğu için tohum listesinde yok. Bir Yamato maddesi düşerse ilk sıradaki yedek. |
| Aos Sí | Ériu | I | `F251` | H ailesinin beşinci üyesi; aynı durum. |

---

## 5. Kısıtlılık taraması — yaşayan gelenekler

> `spec.json` → `restrictionScreened` alanı Faz 1 kapısında **zorunludur**.
> Bu, kitabın etik omurgasıdır ve pazarlama malzemesi değildir.

**Kural:** yalnızca **yayımlanmış ve kısıtlanmamış** malzeme kullanılır.
Kısıtlı olduğu bilinen anlatı **anlatılmaz — kısıtlı olduğu söylenir**.

Taranması zorunlu gelenekler (`bestiarium.py` → `LIVING_TRADITIONS`):

Inuit · Ainu · Sápmi · Anishinaabe · Mā'ohi · Melanesia · Nguni ·
Tupi-Guarani · Yorùbá–Ashanti · Tawantinsuyu · Ityop'ya · Bod · Mongol

| Gelenek | Madde | Kısıtlılık bulgusu | Karar |
|---|---|---|---|
| — | *(Faz 1'de doldurulur)* | | |

### Kasıtlı dışarıda bırakılan

**Avustralya Aborjin gelenekleri.** Sebep kapsam eksikliği değildir: bu
geleneklerin çoğu anlatı **topluluk mülkiyetindedir** ve kimin anlatabileceği
kurala bağlıdır. Kaynağı doğrulanamayan ve izni olmayan malzemeyi bir başvuru
cildine koymak, kitabın kendi standardını ihlal eder.

Bu karar **Sonsöz'de açıkça yazılacaktır** — bir eksik olarak değil, bir
tercih olarak.

---

## 6. Motif kodu doğrulama kaydı

Tohum tablosundaki kodlar **önerilmiştir**. Her biri Thompson
*Motif-Index of Folk-Literature*'dan doğrulanır; doğrulanmayan kod
`motifVerified: false` kalır ve madde `verified` olamaz.

| Durum | Sayı |
|---|---:|
| Toplam benzersiz kod | 70 |
| Doğrulanmış | 0 |
| Reddedilmiş / düzeltilmiş | 0 |

> Güncel sayı için: `python3 08_BUILD/validate_spec.py --gate phase1 -v`
