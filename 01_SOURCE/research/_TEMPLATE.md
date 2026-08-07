# <Yaratık Adı> — araştırma dosyası

<!--
  ŞABLON. Bu dosya `<creature-id>.md` adıyla kopyalanır.
  `<creature-id>` spec.json'daki `id` alanıdır — ör. `each-uisce.md`.

  BU BİR TASLAK DEĞİLDİR. Buraya proza yazılmaz. Bu dosya bir künye ve
  alıntı belgesidir; yazım Faz 3'te, bu dosyaya BAKARAK yapılır.

  Doldurduktan sonra spec.json'daki kaydı güncelleyin:
    sources · region · attested · motifVerified · restrictionScreened
    · altNames · variantNote · pronunciation (taslak) · status: "verified"
-->

| Alan | Değer |
|---|---|
| **id** | `<creature-id>` |
| **Ad** | <geleneğin kendi romanizasyonu, diakritikler korunur> |
| **Alternatif yazımlar** | <dizinde çapraz gönderme yapılacak> |
| **Gelenek** | <gelenek adı + işaret> |
| **Sınıf** | <I–VI> |
| **Akraba ailesi** | <A–H veya —> |
| **Plaka** | `plate-NNN` |
| **Telaffuz (taslak)** | <AKH-ish-keh biçiminde> |

---

## 1. Kaynaklar

> **En az iki BAĞIMSIZ kaynak zorunludur.** Motif dizini (Thompson) bağımsız
> kaynak *sayılmaz* — o bir tasniftir, bir tanıklık değil.
> İkinci kaynak bulunamıyorsa madde listeden düşer ve `SCOPE_DECISIONS.md`'ye
> yazılır. **Uydurulmaz.**

### Kaynak 1

- **Künye:** <Yazar, *Eser* (Yıl), cilt:sayfa>
- **Tür:** `primary` · `secondary` · `index`
- **Erişim:** <URL, kütüphane, arşiv — nereden görüldü>
- **İlgili alıntı:**
  > <birebir alıntı, kendi cümlemizle özetlemeden>

### Kaynak 2

- **Künye:**
- **Tür:**
- **Erişim:**
- **İlgili alıntı:**
  >

### Kaynak 3 (varsa)

- **Künye:**
- **Tür:**
- **Erişim:**

---

## 2. Motif kodu

| Kod | Thompson tanımı | Doğrulandı mı |
|---|---|---|
| `<B184.1.3>` | <Motif-Index'teki birebir tanım> | ⬜ |

> Tohum tablosundaki kod bir **öneridir**. Doğrulanmadan `motifVerified`
> işaretlenmez. Kod yanlışsa doğrusu buraya yazılır ve `spec.json` güncellenir.

---

## 3. Coğrafya ve ilk kayıt

- **Bölge:** <somut: "İrlanda ve İskoçya, kıyı gölleri" — "Kuzey Avrupa" değil>
- **İlk kayıt (attested):** <tarih ve künye: "17. yy sözlü derlemeler;
  O'Donovan 1856" — *"eski çağlardan beri"* YAZILMAZ>
- **Yayılım:** <hangi bölgelerde, hangi adlarla>

---

## 4. Fiziksel tarif

> Yalnızca **kaynakta geçen** özellikler. Kaynağı olmayan hiçbir detay
> yazılmaz — boşluk bırakmak daha iyidir. Bu bölüm hem maddenin 3. bölümünü
> hem de plaka promptunu besler.

-
-
-

**Ölçü:** <kaynakta ölçü veriliyorsa: "bir tekne boyu kanat açıklığı">

---

## 5. Davranış ve kayıtlı vaka

> Maddenin kalbi 4. bölümdür ve orada bir **olay** anlatılır. Mümkünse
> tarih ve yer verilen kayıtlı bir vaka bulun.

- **Ne yapar:**
- **Kayıtlı vaka:** <"Lough Neagh'li bir çocuk 1808'de birine bindi…">
- **Karşı önlem:** <folklorda anlatılan korunma yolu>

---

## 6. Varyantlar

> Çelişki bir kusur değil, kitabın otoritesinin kanıtıdır. Gizlenmez,
> gösterilir.

| Bölge / kaynak | Fark |
|---|---|
| | |

**Varyant notu (tek cümle, `spec.json` → `variantNote`):**
> <"İskoçya'da yiyicidir; İrlanda'da yalnızca boğar.">

---

## 7. Akrabalar

> 2–5 çapraz referans. Karşılıklı olmalı: A → B ise B → A.
> Her satırda **ayrışma noktası** bir cümlede söylenir.

| Madde (id) | İlişki | Ayrışma noktası |
|---|---|---|
| | | |

---

## 8. Kısıtlılık taraması

> **Yalnızca yaşayan gelenekler için zorunlu:** Inuit · Ainu · Sápmi ·
> Anishinaabe · Mā'ohi · Melanesia · Nguni · Tupi-Guarani · Yorùbá–Ashanti ·
> Tawantinsuyu · Ityop'ya · Bod · Mongol

- [ ] Kullanılan malzeme **yayımlanmış** mı?
- [ ] Kısıtlı olduğuna dair bir kayıt var mı? <varsa hangi kaynak>
- [ ] Kısıtlı bir anlatı **dışarıda bırakıldı** mı? <hangisi>
- [ ] Topluluktan okuyucu bulunabilir mi?

**Karar:**
> <"Yalnızca X ve Y'de yayımlanmış tarif kullanıldı. Z töreni kısıtlıdır ve
> anlatılmadı; maddede kısıtlı olduğu söylenecek.">

---

## 9. Modern kurgu etkisi

> Modern kurgu **kaynak sayılmaz**. Varsa tek cümlede ve "modern" etiketiyle
> anılır; yoksa bu bölüm boş kalır.

-

---

## 10. Yazım notları

> Faz 3'te yazacak kişiye (veya ajana) not. Neyi vurgula, neye dikkat et,
> hangi tuzağa düşme.

-

---

## Kontrol listesi

- [ ] En az iki **bağımsız** kaynak, tam künyeyle
- [ ] Motif kodu Thompson'dan **doğrulandı**
- [ ] Bölge somut, ilk kayıt tarihli
- [ ] Fiziksel tarifin her maddesi bir kaynağa dayanıyor
- [ ] Varyantlar not edildi
- [ ] 2–5 akraba, karşılıklı
- [ ] Kısıtlılık taraması yapıldı (yaşayan gelenekse)
- [ ] Telaffuz taslağı yazıldı
- [ ] `spec.json` güncellendi ve `status: "verified"` yapıldı
- [ ] **Bu dosyada tek bir proza cümlesi yok**
