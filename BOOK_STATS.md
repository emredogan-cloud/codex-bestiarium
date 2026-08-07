# BOOK STATS — Codex Bestiarium

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/update_docs.py · ELLE DÜZENLEMEYİN -->

> Son ölçüm: **2026-08-07** · dal `faz/3-cekirdek` · son etiket `v0.2.1` · 41 commit

Buradaki her sayı bir dosyadan ölçülmüştür. Hiçbiri elle girilmez ve
hiçbiri tahmin değildir. Ölçülemeyen alan **—** ile gösterilir.

## 1. Tek bakışta

| Ölçü | Şu an | Hedef | İlerleme |
|---|---:|---:|---|
| Yaratık kaydı | 112 | 112 | `████████████████████████` %100 |
| Gelenek | 40 | 40 | `████████████████████████` %100 |
| Araştırma dosyası | 112 | 112 | `████████████████████████` %100 |
| İki bağımsız kaynaklı madde | 112 | 112 | `████████████████████████` %100 |
| Doğrulanmış motif kodu | 112 | 112 | `████████████████████████` %100 |
| Telaffuz alanı dolu | 112 | 112 | `████████████████████████` %100 |
| Çapraz referansı olan madde | 112 | 112 | `████████████████████████` %100 |
| Kısıtlılık taraması · zorunlu (yaşayan gelenek) | 35 | 35 | `████████████████████████` %100 |
| Yazılmış madde | 45 | 112 | `██████████░░░░░░░░░░░░░░` %40 |
| Normalize plaka | 0 | 112 | `░░░░░░░░░░░░░░░░░░░░░░░░` %0 |
| Kelime (yazılmış) | 30,288 | 78,400 | `█████████░░░░░░░░░░░░░░░` %39 |
| Tahmini sayfa | 116 | 436 | `██████░░░░░░░░░░░░░░░░░░` %27 |

Kısıtlılık taraması yalnızca `LIVING_TRADITIONS` geleneklerinde
**zorunludur**; toplam 44 maddede yapıldı — 9 tanesi gönüllü. Zorunlu olmayan
bir taramayı yapmak serbesttir; zorunlu olanı atlamak kapıyı kırar.

Sayfa tahmini **260 kelime/sayfa** ile hesaplanır (Codex Mythologica'nın
ölçülen 6×9 · 11,2/15,6 pt dizgi yoğunluğu). Gerçek değer dizgi
çalıştırılınca `04_PRINT/` çıktısından okunur — model değil ölçüm geçerlidir.

## 2. Kapsam kapıları

| Kapı | Eşik | Şu an | Durum |
|---|---:|---:|---|
| Faz 1 tamamlanma — doğrulanmış madde | 112 | 112 | ✅ açık |
| Kapsam tabanı — altına inilirse kitap yeniden planlanır | 100 | 112 | ✅ açık |

## 3. Durum dağılımı

| Durum | Madde | Pay |
|---|---:|---:|
| `draft` | 0 | %0 |
| `verified` | 67 | %60 |
| `written` | 45 | %40 |
| `edited` | 0 | %0 |
| `final` | 0 | %0 |

## 4. Sınıf dağılımı

Yürürlükteki hedef **Faz 2'de ölçülen gerçektir**; yol haritası Bölüm
03.1'in sayıları 120 maddelik kapsam için hesaplanmıştı ve tarihsel
kayıt olarak korunur (bkz. `CHANGELOG.md` · karar D21).

| # | Sınıf | Madde | Hedef | Sapma | Sayfa | Yol haritası (120) |
|---|---|---:|---:|---:|---:|---:|
| I | THE GUARDIANS · Bekçiler | 18 | 18 | — | 54 | 22 / 56 s |
| II | THE DEVOURERS · Yutucular | 27 | 27 | — | 81 | 28 / 70 s |
| III | THE SHAPE-CHANGERS · Şekil Değiştirenler | 19 | 19 | — | 57 | 22 / 56 s |
| IV | THE WATER-DWELLERS · Su Sakinleri | 24 | 24 | — | 72 | 24 / 60 s |
| V | SKY AND STORM · Gök ve Fırtına | 16 | 16 | — | 48 | 14 / 36 s |
| VI | THE RESTLESS DEAD · Huzursuz Ölüler | 8 | 8 | — | 24 | 10 / 26 s |

### Sayfa bütçesi

Madde başına **3.0 sayfa** (yol haritası Bölüm 05.3'ün 304/120 ≈ 2,53 modelinden, kilitlenen
112 maddelik kapsama göre yeniden dağıtıldı).

| Kalem | Sayfa |
|---|---:|
| Maddeler (112 × 3.0) | 336 |
| Sınıf ve karşılaştırma açılışları | 28 |
| Ön/arka madde · dizinler · kaynaklar | 72 |
| **Toplam** | **436** |

## 5. Akraba imge aileleri

**Manşet** üyeler iki sayfalık karşılaştırma açılışına girer; **uzun
kuyruk** üyeleri akraba imge tablosunda ve kendi maddesinde durur.
İkisi de tam üyedir (bkz. `00_CONTEXT/KIN_OPENINGS.md`).

| Aile | İmge | Motif | Üye | Manşet | Uzun kuyruk |
|---|---|---|---:|---:|---:|
| **A** · Su atı | The Water Horse | `B184.1.3` | 4 | 4 | 0 |
| **B** · Tilki kadın | The Fox Woman | `D113.3` | 2 | 2 | 0 |
| **C** · Gece cadısı | The Night Hag | `G262` | 14 | 9 | 5 |
| **D** · Fırtına kuşu | The Storm Bird | `B31` | 9 | 9 | 0 |
| **E** · Derinlerin yılanı | The Serpent of the Deep | `B11.2.1.1` | 15 | 9 | 6 |
| **F** · Eşik bekçisi | The Threshold Guardian | `F150` | 8 | 8 | 0 |
| **G** · Yaban adamı | The Wild Man | `F567` | 4 | 4 | 0 |
| **H** · Gizli halk | The Hidden People | `F251` | 3 | 3 | 0 |

Aileye bağlı madde: **59/112** · bağımsız madde: 53

## 5b. Çapraz referans grafiği

| Ölçü | Değer |
|---|---:|
| Bağ (karşılıklı) | 181 |
| Madde başına ortalama | 3.23 |
| En az / en çok | 2 / 5 |
| Bantta (2–5) | 112/112 |

## 6. Bölge dağılımı

| Bölge grubu | Gelenek |
|---|---:|
| Kuzey Avrupa | 5 |
| Doğu Asya | 4 |
| Yakın Doğu | 4 |
| Güneydoğu Asya | 4 |
| Akdeniz | 3 |
| Afrika | 3 |
| Mezoamerika | 2 |
| Okyanusya | 2 |
| Kutup | 2 |
| Orta Asya | 2 |
| Kafkasya | 2 |
| Güney Asya | 1 |
| Batı Avrupa | 1 |
| Himalaya | 1 |
| Balkanlar | 1 |
| And | 1 |
| Amazon | 1 |
| Kuzey Amerika | 1 |

## 7. Madde uzunluğu

| Ölçü | Değer |
|---|---:|
| Yazılmış madde | 45 |
| Ortalama | 673 kelime |
| En kısa | 632 |
| En uzun | 707 |
| Bantta (620–790) | 45/45 |

---

*Bu dosya `08_BUILD/update_docs.py` tarafından üretilir. CI her push'ta
`--check` ile bayatlığını denetler; bayatsa derleme kırmızı yanar.*
