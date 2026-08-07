# Kérberos — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `kerberos` |
| **Ad** | Kérberos |
| **Alternatif yazımlar** | — |
| **Gelenek** | Hellenic Ω · Akdeniz |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | F · Eşik bekçisi |
| **Plaka** | `plate-001` |
| **Telaffuz (taslak)** | KER-be-ros |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `canon`

- **Künye:** Hesiodos, *Theogonia*
- **Yer:** 311–312

### Kaynak 2 · `primary` · doğrulama `canon`

- **Künye:** Apollodoros, *Bibliotheca*
- **Yer:** 2.5.12

### Kaynak 3 · `reference` · doğrulama `sv`

- **Künye:** Carol Rose, *Giants, Monsters, and Dragons: An Encyclopedia of Folklore, Legend, and Myth* (Santa Barbara: ABC-CLIO, 2000)
- **Yer:** s.v. “Cerberus”

### Kaynak 4 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F150` | Access to otherworld | ✅ |

**Gerekçe.** F150 ('Access to otherworld') doğrulandı ve korundu. Kérberos'un işlevi bir hayvan olmak değil, öteki dünyaya ERİŞİMİ denetlemektir: girene izin verir, çıkana vermez. B15 ('Animals with unusual limbs') üç başı tanımlar ama işlevi kaçırır; eşik bekçisi ailesinin ortak kodu F150'dir.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Hellas; Hades'in kapısı, Akheron geçidi
- **İlk kayıt (attested):** Hesiodos, *Theogonia* (MÖ ~700); Homeros, *İlyada* VIII

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Üç başlı köpek
- Yılan kuyruklu ve boynunda yılanlar (Hesiodos)
- Elli baş sayısı da verilir (Hesiodos 312)

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Ölüler diyarının kapısında durur; girmeye izin verir, çıkmaya vermez. Herakles'in on ikinci işi onu zincirsiz çıkarmaktır.
- **Kayıtlı vaka:** Faz 3'te kaynaktan doğrudan okunacak.
- **Karşı önlem:** —

## 6. Varyantlar

| Bölge / kaynak | Fark |
|---|---|
| Hesiodos | Elli başlı |
| Yaygın gelenek | Üç başlı |

**Varyant notu.** Baş sayısı kaynaklar arasında değişir (üç, elli, yüz); madde bunu gizlemeyecek.

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Camazotz** `camazotz` | Maya 𝋠 | `kin` | İkisi de yeraltının bir odasını tutar; biri köpek, öteki yarasa — hayvan seçimi coğrafyanın seçimidir. |
| **Ḫumbaba** `humbaba` | Sumer 𒀭 | `kin` | Kérberos kapıyı, Ḫumbaba ormanı bekler; biri görevini sürdürür, öteki görevi yüzünden öldürülür. |
| **Makara** `makara` | Bharatiya ॐ | `function` | İkisi de bir kapıya aittir; Kérberos kapıda durur, Makara kapıya OYULUR — bekçi bir imgeye dönüşmüştür. |
| **Temes Savsap** `temes-savsap` | Melanesia ◉ | `kin` | İkisi de ölüler diyarının girişinde; Kérberos gücü, Temes Savsap bir SINAVI kullanır. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Eşik bekçisi ailesinin (F) Yunan üyesi ve ailenin çıpası.
- Ayrışma: Kérberos GÜÇLE engeller; Temes Savsap BİLGİYLE, Qílín BAKIŞLA.

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

