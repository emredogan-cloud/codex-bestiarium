#!/usr/bin/env bash
# =============================================================================
# CODEX BESTIARIUM — BÜTÜN KALİTE KAPILARI
# =============================================================================
# CI'ın çalıştırdığı komutun birebir aynısı. Push etmeden önce yerelde
# çalıştırın; yeşilse CI de yeşil olur.
#
#   ./08_BUILD/qa_all.sh                 mevcut kapı seviyesiyle
#   ./08_BUILD/qa_all.sh phase1          kapıyı yükselterek
#   ./08_BUILD/qa_all.sh --fix           üretilen belgeleri tazeleyerek
#
# Hiçbiri venv gerektirmez; hepsi standart kütüphaneyle koşar.
# =============================================================================
set -uo pipefail

BUILD="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$BUILD")"
cd "$ROOT"

GATE=""
FIX=0
for arg in "$@"; do
  case "$arg" in
    --fix) FIX=1 ;;
    draft|phase1|phase2|phase3) GATE="$arg" ;;
    *) echo "bilinmeyen argüman: $arg" >&2; exit 2 ;;
  esac
done

# Kapı seviyesi `.gate` dosyasındadır; yalnızca AÇIKÇA bir seviye verilirse
# o kazanır. (Eskiden `--fix` de kapıyı draft'a düşürüyordu — yani belgeleri
# tazeleyen koşu, açılmış kapıları hiç denetlemiyordu.)
if [ -z "$GATE" ]; then
  if [ -f ".gate" ]; then
    GATE="$(tr -d '[:space:]' < .gate)"
  else
    GATE="draft"
  fi
fi

PY="${PYTHON:-python3}"
FAILED=()
run () {
  local name="$1"; shift
  echo
  echo "──────────────────────────────────────────────────────────────────────"
  echo "▸ $name"
  echo "──────────────────────────────────────────────────────────────────────"
  if "$@"; then
    return 0
  else
    FAILED+=("$name")
    return 1
  fi
}

echo "════════════════════════════════════════════════════════════════════════"
echo "  CODEX BESTIARIUM · KALİTE KAPILARI · kapı: $GATE"
echo "════════════════════════════════════════════════════════════════════════"

# Dizin kapısı da kümülatiftir; Faz 2'den itibaren telaffuz zorunludur.
case "$GATE" in
  phase2|phase3) IDX_GATE="phase2" ;;
  *)             IDX_GATE="draft"  ;;
esac

# SIRA ÖNEMLİ: classify çapraz referansları spec'e yazar, research_gen o
# referansları araştırma dosyalarına basar, update_docs ikisini de ölçer.
if [ "$FIX" = "1" ]; then
  $PY 08_BUILD/classify.py >/dev/null
  # Editoryal defter → book-edited.json. `load_book()` varsa düzeltilmiş
  # metni tercih eder, yani BÜTÜN kapılar düzeltilmiş metni denetler.
  $PY 08_BUILD/edits.py --apply >/dev/null 2>&1 || true
  $PY 08_BUILD/research_gen.py >/dev/null
  $PY 08_BUILD/make_index.py --gate "$IDX_GATE" >/dev/null
  $PY 08_BUILD/make_prompts.py
  $PY 08_BUILD/editor_pack.py >/dev/null 2>&1 || true
  # SIRA: ön/arka madde ölçüsü BOOK_STATS'ın girdisidir. update_docs'tan
  # SONRA ölçülürse belge kendi girdisinden eski kalır ve "bayat belge"
  # kapısı, hiçbir şey bozulmamışken kırmızı yanar. Bir kez yaşandı.
  FIX_PY="$PY"
  [ -x "08_BUILD/.venv/bin/python" ] && FIX_PY="08_BUILD/.venv/bin/python"
  $FIX_PY 08_BUILD/matter_page.py --measure >/dev/null 2>&1 || true
  $PY 08_BUILD/update_docs.py
fi

# Tohum karşılaştırması master yol haritasını okur; o dosya KARDEŞ depodadır
# ve CI koşucusunda bulunmaz. Yoksa atlanır — var olmayan bir girdiyi
# kırmızıya çevirmek, gerçek bir kalite düşüşü değildir.
SEED_SRC="../CODEX_MYTHOLOGICA/03_CODEX_BESTIARIUM_MASTER_ROADMAP.html"
if [ -f "$SEED_SRC" ]; then
  run "tohum tablosu ↔ spec.json" $PY 08_BUILD/seed_import.py --check
else
  echo
  echo "──────────────────────────────────────────────────────────────────────"
  echo "▸ tohum tablosu ↔ spec.json"
  echo "──────────────────────────────────────────────────────────────────────"
  echo "ATLANDI: master yol haritası bu ortamda yok ($SEED_SRC)"
fi
run "araştırma ↔ spec"           $PY 08_BUILD/research_gen.py --check
run "tasnif ↔ spec"               $PY 08_BUILD/classify.py --check
run "editoryal defter ↔ metin"    $PY 08_BUILD/edits.py --check
run "düşman olgu denetimi"        $PY 08_BUILD/factcheck.py --quiet --json 06_REPORTS/adversarial-review.json
run "spec şeması"                 $PY 08_BUILD/validate_spec.py --gate "$GATE" --json 06_REPORTS/spec-validation.json
run "depo ve belge bütünlüğü"     $PY 08_BUILD/validate_structure.py --json 06_REPORTS/structure.json
run "kalite kapılarının testi"    $PY 08_BUILD/tests/selftest.py
run "kelime bandı"                $PY 08_BUILD/qa_length.py --sections --json 06_REPORTS/qa-length.json
run "ses ve yasak kalıp"          $PY 08_BUILD/qa_voice.py --json 06_REPORTS/qa-voice.json
run "üslup sürüklenmesi"          $PY 08_BUILD/qa_drift.py --json 06_REPORTS/qa-drift.json
run "tekrar taraması"             $PY 08_BUILD/qa_echo.py --json 06_REPORTS/qa-echo.json
# Üslup uyumlama ÖLÇÜMÜ — kapı değil (D25/D47 içtihadı ve kurucunun Faz 5
# emri: "sayıyı yapay olarak küçültme"). qa_echo'nun göremediği kalıpları
# sayar ve her koşuda rapora yazar; kırmızı yakmaz.
run "üslup uyumlama ölçümü"       $PY 08_BUILD/qa_style.py --json 06_REPORTS/qa-style.json
run "diakritik"                   $PY 08_BUILD/qa_diacritics.py --json 06_REPORTS/qa-diacritics.json
# Plaka ölçümünün KENDİ testi. Pillow ve numpy ister; venv yoksa ATLANIR
# (çıkış 2). CI'da (plates.yml · calibration) bağımlılıklar kurulu olduğu
# için orada atlanamaz ve kırmızı yanabilir.
echo
echo "──────────────────────────────────────────────────────────────────────"
echo "▸ plaka ölçümünün kalibrasyonu"
echo "──────────────────────────────────────────────────────────────────────"
CAL_PY="$PY"
[ -x "08_BUILD/.venv/bin/python" ] && CAL_PY="08_BUILD/.venv/bin/python"
$CAL_PY 08_BUILD/tests/plate_selftest.py
case $? in
  0) ;;
  2) echo "ATLANDI: Pillow/numpy yok — ./08_BUILD/bootstrap.sh çalıştırın" ;;
  *) FAILED+=("plaka ölçümünün kalibrasyonu") ;;
esac

echo
echo "──────────────────────────────────────────────────────────────────────"
echo "▸ plaka format bütçeleri (kalibrasyon)"
echo "──────────────────────────────────────────────────────────────────────"
$CAL_PY 08_BUILD/convert_plates.py --calibrate
case $? in
  0) ;;
  2) echo "ATLANDI: Pillow yok — ./08_BUILD/bootstrap.sh çalıştırın" ;;
  *) FAILED+=("plaka format bütçeleri") ;;
esac

# Madde sayfası prova dizgisi. reportlab + font ister; ikisi de yoksa atlanır.
# Sayfa bütçesinin (436 sayfa) tek dayanağı bu ölçümdür.
echo
echo "──────────────────────────────────────────────────────────────────────"
echo "▸ madde sayfası prova dizgisi"
echo "──────────────────────────────────────────────────────────────────────"
if ls 07_ASSETS/fonts/*.ttf >/dev/null 2>&1; then
  $CAL_PY 08_BUILD/entry_page.py --proof
  case $? in
    0) ;;
    2) echo "ATLANDI: reportlab yok — ./08_BUILD/bootstrap.sh çalıştırın" ;;
    *) FAILED+=("madde sayfası prova dizgisi") ;;
  esac
  # Ön ve arka madde de sayfa bütçesinin parçasıdır (BRIEF § 7: giriş 8 ·
  # nasıl okunur 6 · sonsöz 4 · arka madde 8). Maddeler ölçülüp bu bölümler
  # ölçülmezse bütçenin 26 sayfası denetimsiz kalır.
  $CAL_PY 08_BUILD/matter_page.py --check
  case $? in
    0) echo "[  ok ] ön/arka madde sayfa bütçesi" ;;
    2) echo "ATLANDI: ön/arka madde henüz yazılmadı veya reportlab yok" ;;
    *) FAILED+=("ön/arka madde sayfa bütçesi") ;;
  esac
else
  echo "ATLANDI: font yok — ./08_BUILD/bootstrap.sh çalıştırın"
fi

# Plaka adımları GÖRÜNTÜ KÜTÜPHANESİ ister. Yukarıdaki kalibrasyon
# adımlarıyla aynı sözleşme: venv varsa onunla koş, çıkış 2 = ATLANDI.
# Faz 5'e kadar bu adımlar plaka olmadığı için sessizce geçiyordu; 112
# plaka gelince Pillow'suz bir makinede kırmızı yanmaya başladılar.
# Eksik bir isteğe bağlı bağımlılık, kalite düşüşüyle aynı sinyali
# vermemelidir (aynı gerekçe: Faz 2 · D-sürüm kapısı).
plate_step () {
  local name="$1"; shift
  echo
  echo "──────────────────────────────────────────────────────────────────────"
  echo "▸ $name"
  echo "──────────────────────────────────────────────────────────────────────"
  $CAL_PY "$@"
  case $? in
    0) ;;
    2) echo "ATLANDI: Pillow/numpy yok — ./08_BUILD/bootstrap.sh çalıştırın" ;;
    *) FAILED+=("$name") ;;
  esac
}

plate_step "plaka manifestosu"     08_BUILD/plate_manifest.py --check
plate_step "plaka tutarlılığı"     08_BUILD/plates.py --measure
plate_step "plaka formatları"      08_BUILD/convert_plates.py --check
run "kin-images chart"            $PY 08_BUILD/make_kin_chart.py --check
# Editör teslim paketinin ÖLÇÜSÜ güncel mi. Metin yoksa çıkış 2 = ATLANDI
# (CI'da proza bulunmaz); aynı sözleşme.
echo
echo "──────────────────────────────────────────────────────────────────────"
echo "▸ editör teslim paketi"
echo "──────────────────────────────────────────────────────────────────────"
$PY 08_BUILD/editor_pack.py --check
case $? in
  0) ;;
  2) echo "ATLANDI: metin yok — teslim paketi yazımdan sonradır" ;;
  *) FAILED+=("editör teslim paketi") ;;
esac

run "dizinler"                    $PY 08_BUILD/make_index.py --gate "$IDX_GATE"
run "üretilen belgeler güncel"    $PY 08_BUILD/update_docs.py --check
run "prompt kütüphanesi güncel"   $PY 08_BUILD/make_prompts.py
  $PY 08_BUILD/editor_pack.py >/dev/null 2>&1 || true
  # SIRA: ön/arka madde ölçüsü BOOK_STATS'ın girdisidir. update_docs'tan
  # SONRA ölçülürse belge kendi girdisinden eski kalır ve "bayat belge"
  # kapısı, hiçbir şey bozulmamışken kırmızı yanar. Bir kez yaşandı.
  FIX_PY="$PY"
  [ -x "08_BUILD/.venv/bin/python" ] && FIX_PY="08_BUILD/.venv/bin/python"
  $FIX_PY 08_BUILD/matter_page.py --measure >/dev/null 2>&1 || true --check

echo
echo "════════════════════════════════════════════════════════════════════════"
if [ ${#FAILED[@]} -eq 0 ]; then
  echo "  ✅ BÜTÜN KAPILAR YEŞİL · kapı seviyesi: $GATE"
  echo "════════════════════════════════════════════════════════════════════════"
  exit 0
fi
echo "  ⛔ ${#FAILED[@]} KAPI KIRMIZI"
for f in "${FAILED[@]}"; do echo "     · $f"; done
echo "════════════════════════════════════════════════════════════════════════"
echo
echo "  Kalite düştü. Düzeltilmeden devam edilmez."
echo "  Üretilen belge bayatsa:  ./08_BUILD/qa_all.sh --fix"
exit 1
