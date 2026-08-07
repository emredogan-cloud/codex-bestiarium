# ROADMAP PROGRESS — Codex Bestiarium

<!-- OTOMATİK ÜRETİLDİ — 08_BUILD/update_docs.py · ELLE DÜZENLEMEYİN -->

> Son ölçüm: **2026-08-07** · dal `faz/1-arastirma` · son etiket `v0.1.0-alpha`

Kaynak: [`CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md`](CODEX_BESTIARIUM_IMPLEMENTATION_ROADMAP.md)

## Faz durumu

| Faz | Başlık | İlerleme | Ölçüt | Etiket | Kilometre taşı |
|---:|---|---|---|---|---|
| **1** | Altyapı, Araştırma ve Kapsam Kilidi | `███░░░░░░░░░░░░░` 22/120 (%18) | iki bağımsız kaynaklı madde | `v0.1.0` | Faz 1 · Temel |
| **2** | Tasnif, Veri Modeli ve Pilot Plaka Seti | `███░░░░░░░░░░░░░` 24/120 (%20) | telaffuz + tasnif tamamlanmış madde | `v0.2.0` | Faz 2 · Veri |
| **3** | Çekirdek Yazım · Bekçiler ve Yutucular | `░░░░░░░░░░░░░░░░` 0/49 (%0) | sınıf I + II maddeleri yazıldı | `v0.3.0` | Faz 3 · Çekirdek |
| **4** | Genişleme · Şekil Değiştirenler ve Su Sakinleri | `░░░░░░░░░░░░░░░░` 0/45 (%0) | sınıf III + IV maddeleri yazıldı | `v0.4.0` | Faz 4 · Genişleme |
| **5** | Tamamlama, İllüstrasyon ve Editoryal İnceleme | `░░░░░░░░░░░░░░░░` 0/26 (%0) | sınıf V + VI maddeleri yazıldı | `v0.5.0` | Faz 5 · Tamamlama |
| **6** | Üretim, KDP ve Lansman | `░░░░░░░░░░░░░░░░` 0/4 (%0) | üretilmiş yayın dosyası ailesi | `v1.0.0` | Faz 6 · Üretim |

## Kalite kapıları — şu anki durum

| Kapı | Komut | Ne zaman açılır |
|---|---|---|
| Şema | `validate_spec.py --gate draft` | her zaman |
| Araştırma | `validate_spec.py --gate phase1` | Faz 1 sonunda |
| Tasnif | `validate_spec.py --gate phase2` | Faz 2 sonunda |
| Yazım | `validate_spec.py --gate phase3` | Faz 3'ten itibaren |
| Kelime bandı | `qa_length.py --sections` | metin geldiğinde |
| Ses | `qa_voice.py` | metin geldiğinde |
| Sürüklenme | `qa_drift.py` | haftalık, Faz 3'ten itibaren |
| Tekrar | `qa_echo.py` | metin geldiğinde |
| Diakritik | `qa_diacritics.py` | her zaman |
| Plaka | `plates.py --measure` | plaka geldiğinde |
| Yapı | `validate_structure.py` | her push |

## Sonraki eylem

**Faz 1 · Araştırma.** 22/120 maddede iki
bağımsız kaynak var. Kapı 112'de açılıyor.

Sıra yol haritasının emrettiği gibi **en zor sekiz gelenekten**
başlar — kapsamı bunlar belirler:

- **Ainu** ᚼ — 2/3 · Koropokkuru, Repun Kamuy, Kenas-unarpe
- **Nusantara** ❋ — 1/3 · Pontianak, Orang Bunian, Rangda
- **Mongol** ⚔ — 0/3 · Almas, Olgoi-Khorkhoi, Chötgör
- **Hayk** ✚ — 3/3 · Vishap, Aralez, Nhang
- **Kartveli** ✛ — 0/3 · Ochokochi, Kaji, Devi
- **Ityop'ya** ✤ — 1/3 · Buda, Zar, Ganen
- **Sápmi** ❄ — 3/3 · Stállu, Ulda, Gufihtar
- **Melanesia** ◉ — 3/3 · Adaro, Masalai, Temes Savsap

---

*Bu dosya `08_BUILD/update_docs.py` tarafından üretilir.*
