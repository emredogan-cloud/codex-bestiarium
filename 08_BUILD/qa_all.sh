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

GATE="draft"
FIX=0
for arg in "$@"; do
  case "$arg" in
    --fix) FIX=1 ;;
    draft|phase1|phase2|phase3) GATE="$arg" ;;
    *) echo "bilinmeyen argüman: $arg" >&2; exit 2 ;;
  esac
done

# Kapı seviyesi bir dosyada da tutulabilir; varsa o kazanır.
if [ -f ".gate" ] && [ $# -eq 0 ]; then
  GATE="$(tr -d '[:space:]' < .gate)"
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

if [ "$FIX" = "1" ]; then
  $PY 08_BUILD/update_docs.py
  $PY 08_BUILD/make_prompts.py
  $PY 08_BUILD/make_index.py --gate draft >/dev/null
fi

run "tohum tablosu ↔ spec.json"   $PY 08_BUILD/seed_import.py --check
run "spec şeması"                 $PY 08_BUILD/validate_spec.py --gate "$GATE" --json 06_REPORTS/spec-validation.json
run "depo ve belge bütünlüğü"     $PY 08_BUILD/validate_structure.py --json 06_REPORTS/structure.json
run "kalite kapılarının testi"    $PY 08_BUILD/tests/selftest.py
run "kelime bandı"                $PY 08_BUILD/qa_length.py --sections --json 06_REPORTS/qa-length.json
run "ses ve yasak kalıp"          $PY 08_BUILD/qa_voice.py --json 06_REPORTS/qa-voice.json
run "üslup sürüklenmesi"          $PY 08_BUILD/qa_drift.py --json 06_REPORTS/qa-drift.json
run "tekrar taraması"             $PY 08_BUILD/qa_echo.py --json 06_REPORTS/qa-echo.json
run "diakritik"                   $PY 08_BUILD/qa_diacritics.py --json 06_REPORTS/qa-diacritics.json
run "plaka tutarlılığı"           $PY 08_BUILD/plates.py --measure
run "plaka formatları"            $PY 08_BUILD/convert_plates.py --check
run "dizinler"                    $PY 08_BUILD/make_index.py --gate draft
run "üretilen belgeler güncel"    $PY 08_BUILD/update_docs.py --check
run "prompt kütüphanesi güncel"   $PY 08_BUILD/make_prompts.py --check

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
