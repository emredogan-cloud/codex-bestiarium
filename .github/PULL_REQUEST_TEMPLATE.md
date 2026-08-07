## Ne değişti

<!-- Bir cümle. "Faz 1 · Melanezya araştırması" gibi. -->

## Faz ve kapı

- **Faz:** <!-- 1–6 -->
- **Kapı seviyesi (`.gate`):** <!-- draft | phase1 | phase2 | phase3 -->
- **Bu PR kapıyı yükseltiyor mu?** <!-- hayır / evet → hangi seviyeye -->

## Kontrol listesi

- [ ] `./08_BUILD/qa_all.sh` yerelde **yeşil**
- [ ] `CHANGELOG.md` güncellendi (karar varsa **gerekçesiyle**)
- [ ] Üretilen belgeler tazelendi (`./08_BUILD/qa_all.sh --fix`)
- [ ] `spec.json` değiştiyse `seed_import.py --check` geçti
- [ ] Elle düzenlenmiş üretilmiş dosya **yok** (`BOOK_STATS.md`,
      `ROADMAP_PROGRESS.md`, `BESTIARIUM_IMAGE_PROMPTS.html`,
      `06_REPORTS/INDEXES_PREVIEW.md`)

### Araştırma içeriyorsa

- [ ] Her yeni maddede **≥2 bağımsız kaynak**, tam künyeyle
- [ ] Motif kodu Thompson'dan **doğrulandı** (tahmin değil)
- [ ] Yaşayan gelenekse **kısıtlılık taraması** yapıldı
- [ ] Kaynak bulunamayan madde `SCOPE_DECISIONS.md`'ye yazıldı

### Metin içeriyorsa

- [ ] Yedi bölüm tam ve **sırada**
- [ ] Kelime sayısı 620–790 bandında
- [ ] Yasak kalıp yok · ünlem yok · oyun terimi yok
- [ ] Diakritikler korundu
- [ ] Tek seferde **en fazla üç madde** yazıldı

### Plaka içeriyorsa

- [ ] Ham dosya `plates_raw/` içinde ve **değiştirilmedi**
- [ ] `plates.py --measure` tolerans dışı plaka göstermiyor
- [ ] `convert_plates.py --check` bütçeleri tutuyor

## Ölçülen etki

<!--
  Sayı verin. "120 → 120 madde, 0 → 9 doğrulanmış" gibi.
  BOOK_STATS.md'deki farkı buraya yapıştırabilirsiniz.
-->

## Not

<!-- Gözden geçirenin bilmesi gereken bir şey varsa. -->
