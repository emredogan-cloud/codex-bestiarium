# Aralez — araştırma dosyası

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/research_gen.py
     Kaynak: 01_SOURCE/research_data/<gelenek>.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `aralez` |
| **Ad** | Aralez |
| **Alternatif yazımlar** | Arlez, Yaralez |
| **Gelenek** | Hayk ✚ · Kafkasya |
| **Sınıf** | I · THE GUARDIANS (Bekçiler) |
| **Akraba ailesi** | F · Eşik bekçisi |
| **Plaka** | `plate-082` |
| **Telaffuz (taslak)** | ah-rah-LEZ |
| **Durum** | `draft` |

## 1. Kaynaklar

> Ölçüt: [`00_CONTEXT/SOURCING_STANDARD.md`](../../00_CONTEXT/SOURCING_STANDARD.md)
> — ≥2 bağımsız kaynak, en az biri `primary`/`scholarly`, en az birinin
> doğrulaması `fulltext`/`toc`. Motif dizini bağımsız kaynak **sayılmaz**.

### Kaynak 1 · `scholarly` · doğrulama `toc`

- **Künye:** Mardiros H. Ananikian, *Armenian Mythology*, *The Mythology of All Races* içinde, Cilt VII (Boston: Marshall Jones, 1925)
- **Erişim:** archive.org — kamuya açık dijital nüsha
- **Yer:** Bölüm "The World of Spirits and Monsters"
- **Not:** İçindekiler dijital nüshadan doğrulandı; bölüm başlıkları birebir.

### Kaynak 2 · `scholarly` · doğrulama `catalog`

- **Künye:** Manuk Abeghyan, "The Stelae Called 'Vishaps' as Monuments to the Goddess Astghik-Derketo", *Works* 7 (Erivan, 1975)

### Kaynak 3 · `index` · doğrulama `fulltext`

- **Künye:** Stith Thompson, *Motif-Index of Folk-Literature*, gözden geçirilmiş baskı (Bloomington: Indiana University Press, 1955–58)

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı |
|---|---|---|
| `E17` | Resuscitation by licking corpse | ✅ |

**Gerekçe.** TOHUM KODU DEĞİŞTİRİLDİ. Tohum B733 ('Animals are spirit-sighted') idi — aralez'in işlevi görmek değil DİRİLTMEKTİR. Tam Motif-Index ayrıştırmasında bulunan E17'nin tanımı birebir: 'Resuscitation by licking corpse'. Aralez'in yaptığı şey tam olarak budur.

> ⚠ **Tohum kodu değiştirildi.** B733 → E17. Kod B (hayvan) bölümünde değil E (ölüler/diriltme) bölümünde olmalıydı.

## 3. Coğrafya ve ilk kayıt

- **Bölge:** Tarihî Ermenistan; savaş alanları anlatılarında
- **İlk kayıt (attested):** Ananikian 1925'te derlenmiş erken Ermeni kaynaklarından

## 4. Fiziksel tarif

> Yalnızca kaynakta geçen özellikler. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

- Köpek benzeri ruh
- Kimi kayıtta kanatlı

## 5. Davranış ve kayıtlı vaka

- **Ne yapar:** Savaşta ölen kahramanın üzerine iner ve yarasını yalayarak diriltir.
- **Kayıtlı vaka:** Faz 3'te Ananikian'dan doğrudan okunacak.
- **Karşı önlem:** —

## 6. Varyantlar

*Kaynaklarda anlamlı bir varyant ayrımı kaydedilmedi.*

## 7. Akrabalar

> Faz 2 çıktısı. Kaynak: [`01_SOURCE/kin_map.json`](../kin_map.json) ·
> bağlar **karşılıklıdır** ve `08_BUILD/classify.py` tarafından kurulur.
> Bu tablo maddenin 6. bölümünün ("Akrabaları") ham malzemesidir.

| Madde | Gelenek | Bağ | Ayrışma noktası |
|---|---|---|---|
| **Golem** `golem` | Talmud ✡ | `kin` | Golem adla canlandırılır ve harf silinince çöker; Aralez yalayarak diriltir. Biri yazının, öteki bedenin işi. |
| **Nhang** `nhang` | Hayk ✚ | `tradition` | Hayk'ın iki ucu: biri kanı alır, öteki yarayı iyileştirir. |
| **Temes Savsap** `temes-savsap` | Melanesia ◉ | `kin` | İkisi de ölümün eşiğinde durur: Aralez geri gönderir, Temes Savsap geçirmez. |

## 8. Kısıtlılık taraması

Bu gelenek `LIVING_TRADITIONS` listesinde değil; ek kapı uygulanmaz.

## 9. Modern kurgu etkisi

Kaydedilmedi.

## 10. Yazım notları

- Kitabın tek DİRİLTEN varlığı; yutucuların karşıtı.
- Eşik bekçisi ailesinde (F) sınıflandırılmış ama işlevi bekçilik değil DİRİLTME; Faz 2'de aile üyeliği yeniden düşünülmeli.

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

