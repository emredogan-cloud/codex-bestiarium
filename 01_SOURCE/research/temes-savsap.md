# Temes Savsap — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `temes-savsap` |
| **Ad** | Temes Savsap |
| **Alternatif yazımlar** | — |
| **Gelenek** | Melanesia ◉ · Okyanusya |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | F · Eşik bekçisi |
| **Plaka** | `plate-112` |
| **Telaffuz (taslak)** | TEH-mes SAV-sap |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `primary` · doğrulama `article`

- **Künye:** A. Bernard Deacon ve Camilla H. Wedgwood, "Geometrical Drawings from Malekula and other Islands of the New Hebrides", *Journal of the Royal Anthropological Institute of Great Britain and Ireland* 64 (1934), 129–175
- **Erişim:** JRAI cilt 64; makale künyesi ve sayfa aralığı doğrulandı
- **Yer:** 129–175
- **Not:** Deacon'ın topladığı ~45 geometrik kum çizimi ve ölüler diyarının girişindeki figürle ilişkileri.

### Kaynak 2 · `primary` · doğrulama `catalog`

- **Künye:** A. Bernard Deacon, *Malekula: A Vanishing People in the New Hebrides*, yay. haz. Camilla H. Wedgwood (Londra: Routledge, 1934)
- **Erişim:** odsas.net/scan_sets.php?set_id=833 — sayfa sayfa dijital nüsha
- **Not:** Deacon saha çalışması sırasında öldü; malzemeyi Wedgwood yayına hazırladı.

### Kaynak 3 · `scholarly` · doğrulama `catalog`

- **Künye:** John Layard, *Stone Men of Malekula* (Londra: Chatto & Windus, 1942)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `F150` | Access to otherworld | ✅ |

**Gerekçe.** F150 ('Access to otherworld') doğrulandı ve seçildi. Temes Savsap tam olarak öteki dünyaya ERİŞİMİ denetler: önündeki kum çizimini tamamlayamayan ölü geçemez. F156 ('Door to otherworld') de değerlendirildi; F150 daha genel ve geçiş SINAVINI da kapsadığı için tercih edildi.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Malekula (Malakula) adası, Vanuatu (eski Yeni Hebridler)
- **İlk kayıt (attested):** Deacon'ın 1926–27 saha çalışması; 1934'te iki ayrı yayında
- **Yayılım:** Malekula ve çevre adalar; kum çizimi geleneği Vanuatu'nun kuzeyinde yaygın

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Dişi bir ruh; ölüler diyarının girişinde oturur
- Önündeki kumda tamamlanmış bir geometrik figür bulunur

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Yaklaşan ölünün önünde duran kum çizimini yarılar. Ölü figürü tamamlayamazsa geçemez.
- **Kayıtlı vaka:** Faz 3'te Deacon–Wedgwood makalesinden doğrudan okunacak.
- **Karşı önlem:** Kum çizimini eksiksiz ve tek çizgide tamamlayabilmek — bu yüzden çizim öğrenilir ve tekrarlanır.

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Aralez** `aralez` | Hayk ✚ | `kin` | İkisi de ölümün eşiğinde durur: Aralez geri gönderir, Temes Savsap geçirmez. |
| **Camazotz** `camazotz` | Maya 𝋠 | `kin` | Temes Savsap geçişi bilgiye bağlar; Camazotz geçeni keser. Sınav ile infaz. |
| **Kérberos** `kerberos` | Hellenic Ω | `kin` | İkisi de ölüler diyarının girişinde; Kérberos gücü, Temes Savsap bir SINAVI kullanır. |
| **Masalai** `masalai` | Melanesia ◉ | `tradition` | Melanezya'nın iki sınırı: biri arazinin, öteki ölümün. |

## 8. Kısıtlılık taraması

> **Yaşayan gelenek — bu tarama zorunludur.**

Kum çizimi geleneği yayımlanmış ve akademik olarak geniş biçimde tartışılmıştır (matematik tarihi literatüründe de). Malekula'nın Maki derece töreni ve ona bağlı BAŞLATMA bilgisi KULLANILMAZ. Plakada gerçek bir kum çizimi deseni birebir çizilmez — desenler yer ve soy bağlıdır; yalnızca figürün önünde 'tamamlanmamış bir çizgi' soyutlaması gösterilir.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Bu madde tohum tablosundaki Kaia'nın yerine geldi; gerekçe SCOPE_DECISIONS.md'de.
- Eşik bekçisi ailesinin (F) Okyanusya üyesi — Kérberos ve Ḫumbaba ile yan yana basılacak.
- Ayrışma noktası güçlü: Kérberos GÜÇLE engeller, Temes Savsap BİLGİYLE engeller. Geçiş bedeli kas değil hafızadır.

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

