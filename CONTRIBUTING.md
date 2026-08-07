# Çalışma düzeni

> Bu depoda tek bir yazar var. Bu belge dışarıdan katkı çağrısı değil,
> **kendi disiplinimizin yazılı hâlidir** — ve altı ay sonra projeye dönen
> kişi için bir hatırlatmadır.

---

## 1. Tek kural

**CI kırmızıysa çalışma durur.**

Yeni bir madde yazılmaz, yeni bir plaka üretilmez, yeni bir faza geçilmez.
Önce kırmızı düzelir. Bu kural, kalitenin yavaş yavaş düşmesini engelleyen
tek mekanizmadır — çünkü kalite hiçbir zaman bir anda düşmez.

```bash
./08_BUILD/qa_all.sh          # push etmeden önce
```

Yerelde yeşilse CI de yeşil olur. İkisi ayrışıyorsa bu bir **hat arızasıdır**
ve `[hat]` etiketiyle issue açılır.

---

## 2. Dallar

| Dal | Ne için |
|---|---|
| `main` | Her zaman yeşil. Doğrudan push yok. |
| `faz/<n>-<konu>` | Faz işi — `faz/1-melanezya-arastirma` |
| `fix/<konu>` | Hat arızası — `fix/qa-echo-yanlis-pozitif` |

Bir faz birden çok PR'la yürüyebilir; **faz ancak etiketle kapanır**.

---

## 3. Commit mesajları

Türkçe. Biçim:

```
<alan>: <ne yapıldı>

<neden — bir veya iki cümle, gerekiyorsa>
```

**Alanlar:** `arastirma` · `tasnif` · `yazim` · `plaka` · `dizgi` · `kapak` ·
`hat` · `belge` · `ci` · `kapsam`

Örnekler:

```
arastirma: Melanezya üç madde — Adaro, Masalai, Kaia

Adaro ve Masalai için iki bağımsız kaynak bulundu. Kaia tek kaynakta
kaldı; SCOPE_DECISIONS.md'ye yazıldı, yedek aranıyor.
```

```
hat: qa_echo yanlış pozitifi düzeltildi

Kod bloklarını silmek satır numaralarını kaydırıyordu; artık boş
satırlarla maskeleniyor.
```

---

## 4. Üretilen dosyalar elle düzenlenmez

Bunlar bir sonraki üretimde **kaybolur**:

| Dosya | Kaynağı | Yeniden üretmek |
|---|---|---|
| `BOOK_STATS.md` | `spec.json` + `book.json` + git | `update_docs.py` |
| `ROADMAP_PROGRESS.md` | aynı | `update_docs.py` |
| `BESTIARIUM_IMAGE_PROMPTS.html` | `spec.json` + `plate_subjects.json` | `make_prompts.py` |
| `06_REPORTS/INDEXES_PREVIEW.md` | `spec.json` | `make_index.py` |
| `01_SOURCE/indexes.json` | `spec.json` | `make_index.py` |
| `06_REPORTS/*.json` | doğrulama koşuları | ilgili betik |

Değişmesi gereken şey çıktı değil **kaynaktır**. CI bunu `--check` ile
denetler ve bayat belge derlemeyi kırmızıya çevirir.

```bash
./08_BUILD/qa_all.sh --fix     # hepsini tazele
```

---

## 5. Kapı yükseltme

Kapı seviyesi `.gate` dosyasındadır ve **geri alınamayan tek manuel işlemdir**.

```bash
echo phase1 > .gate
./08_BUILD/qa_all.sh           # artık phase1 de zorunlu
```

Bir kapı ancak fazın Definition of Done listesi tamamlandığında yükselir.
`release.yml` etiketle kapı seviyesinin uyuştuğunu doğrular: `v0.1.0`
etiketi `.gate=phase1` bekler.

---

## 6. Faz kapanış listesi

Sırayla:

1. Fazın **Definition of Done** listesindeki her madde işaretlendi mi
2. `./08_BUILD/qa_all.sh --fix` → yeşil
3. `CHANGELOG.md`'ye sürüm bloğu eklendi — **kararlar gerekçesiyle**
4. `.gate` yükseltildi (gerekiyorsa)
5. PR açıldı, CI yeşil, `main`'e merge edildi
6. Etiket atıldı: `git tag -a v0.N.0 -m "…" && git push --tags`
7. `release.yml` GitHub Release'i CHANGELOG'dan üretti
8. GitHub Milestone kapatıldı

---

## 7. Yazım disiplini

**Tek seferde en fazla üç madde.**

Bu bir tercih değil, portföy denetiminde **ölçülmüş bir hatadır**. Dördüncü
maddeye başlarken bağlamda üç maddenin metni durur ve dördüncü onların
ritmine kayar.

Girdi her seferinde şu üçlüdür:

1. O maddenin araştırma dosyası
2. `00_CONTEXT/STYLE.md`
3. Yedi bölümlü şablon

Daha fazlası üslup sürüklenmesi üretir.

---

## 8. Kaynak disiplini

**Uydurma kaynak, projenin tek geri döndürülemez hatasıdır.**

Kaynak gösterilmesi bu kitabın tek savunmasıdır. Bir tek uydurma madde,
o savunmayı bütün kitap için geçersiz kılar — ve bir okur bunu bulur.

Bulunamıyorsa: madde düşer, `SCOPE_DECISIONS.md`'ye yazılır, yedek aranır.
Yedek de yoksa kapsam iner. **120 sayısı kutsal değildir; doğruluk kutsaldır.**

---

## 9. Yanlış negatif bulunca

Bir kapı gerçek bir kusuru **yakalamadıysa**, o kusuru düzeltmek yetmez.
`08_BUILD/tests/selftest.py` kurgusuna o kusur **eklenir** — aksi hâlde aynı
kör nokta geri gelir.

```bash
# 1. Kusuru make_fixtures.py'deki make_bad()'e ekle
# 2. selftest.py çalıştır — kapı hâlâ yakalamıyorsa betiği düzelt
# 3. selftest.py yeşil olana kadar devam et
python3 08_BUILD/tests/selftest.py
```

Bu, hattın kendini onarma mekanizmasıdır.

---

## 10. Dışarıdan katkı

Bu bir yayın projesidir; kitabın metnine ve illüstrasyonlarına dışarıdan
katkı **kabul edilmez** (telif ve editoryal tutarlılık).

Kabul edilenler:

- **Hat arızası bildirimi** — `[hat]` issue
- **Olgusal hata bildirimi** — bir yaratık yanlış anlatılmışsa, kaynağıyla
- **Kaynak önerisi** — özellikle kaynak riski yüksek sekiz gelenek için
- **Kısıtlılık uyarısı** — bir anlatının kısıtlı olduğunu biliyorsanız,
  bu **en değerli katkıdır** ve derhal işleme alınır

Kod (`08_BUILD/`) MIT lisanslıdır ve serbestçe kullanılabilir.
