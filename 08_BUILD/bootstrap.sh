#!/usr/bin/env bash
# =============================================================================
# CODEX BESTIARIUM — SIFIRDAN KURULUM
# =============================================================================
# Debian/Ubuntu'da PEP 668 yüzünden `pip install` doğrudan çalışmaz. Bu betik
# proje içine bir venv kurar; bütün üretim betikleri onu kullanır.
#
#   ./08_BUILD/bootstrap.sh
#
# Kalite kapıları venv'e İHTİYAÇ DUYMAZ — sistem python3'üyle koşarlar.
# Bu betik yalnızca üretim (plaka, dizgi, kapak, EPUB) için gerekir.
# =============================================================================
set -euo pipefail

BUILD="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$BUILD")"
VENV="$BUILD/.venv"

echo "▸ kök       : $ROOT"
echo "▸ venv      : $VENV"

if [ ! -d "$VENV" ]; then
  echo "▸ venv kuruluyor…"
  python3 -m venv "$VENV"
fi

"$VENV/bin/pip" install --quiet --upgrade pip
"$VENV/bin/pip" install --quiet -r "$BUILD/requirements.txt"
echo "▸ bağımlılıklar kuruldu"

# --- fontlar ---------------------------------------------------------------
FONTS="$ROOT/07_ASSETS/fonts"
if [ ! -f "$FONTS/Cinzel[wght].ttf" ]; then
  SRC="$ROOT/../CODEX_MYTHOLOGICA/07_ASSETS/fonts"
  if [ -d "$SRC" ]; then
    echo "▸ fontlar Codex Mythologica'dan kopyalanıyor…"
    mkdir -p "$FONTS"
    cp "$SRC"/*.ttf "$FONTS/"
  else
    echo "⚠ FONT YOK. Cinzel ve EB Garamond (SIL OFL 1.1) gerekli:"
    echo "  $FONTS/"
    echo "  Tipografik ses Cilt 1 ile AYNI olmalıdır — başka yüz kullanmayın."
  fi
fi
ls -1 "$FONTS" 2>/dev/null | sed 's/^/  font: /' || true

# --- sistem araçları -------------------------------------------------------
missing=()
for tool in pdftoppm pdfinfo pdffonts pdfimages; do
  command -v "$tool" >/dev/null 2>&1 || missing+=("$tool")
done
if [ ${#missing[@]} -gt 0 ]; then
  echo "⚠ eksik sistem aracı: ${missing[*]}"
  echo "  sudo apt-get install poppler-utils"
  echo "  (deneysel kapak/iç blok doğrulaması bunlarsız çalışmaz)"
else
  echo "▸ poppler-utils mevcut"
fi

# --- doğrulama -------------------------------------------------------------
echo
echo "▸ kalite kapıları çalıştırılıyor…"
cd "$ROOT"
python3 08_BUILD/validate_spec.py --gate draft
python3 08_BUILD/tests/selftest.py

echo
echo "✅ kurulum tamam."
echo
echo "Sıradaki komutlar:"
echo "  ./08_BUILD/qa_all.sh                    bütün kalite kapıları"
echo "  python3 08_BUILD/update_docs.py         BOOK_STATS + ROADMAP_PROGRESS"
echo "  python3 08_BUILD/make_prompts.py        prompt kütüphanesi"
echo "  python3 08_BUILD/plates.py --pilot -v   pilot plaka ölçümü"
