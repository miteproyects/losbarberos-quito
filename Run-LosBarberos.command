#!/usr/bin/env bash
# =============================================================================
#  Los Barberos Quito — one-click launcher (macOS)
#  Double-click this file in Finder to start the website.
#
#  Place anywhere inside ~/Desktop/OpenTF/Barberos/ — the script auto-finds
#  the losbarberos-quito project whether it sits next to this file or inside
#  a subfolder of the same name.
# =============================================================================
set -e

# --- 1. Resolve where this .command file lives -------------------------------
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# --- 2. Find the project folder ---------------------------------------------
if [ -f "$SCRIPT_DIR/app.py" ] && [ -d "$SCRIPT_DIR/components" ]; then
    PROJ="$SCRIPT_DIR"
elif [ -d "$SCRIPT_DIR/losbarberos-quito" ] && [ -f "$SCRIPT_DIR/losbarberos-quito/app.py" ]; then
    PROJ="$SCRIPT_DIR/losbarberos-quito"
else
    echo "──────────────────────────────────────────────────────────"
    echo " ❌  Cannot find the Los Barberos project (app.py)"
    echo "    Put this launcher inside Barberos/ or Barberos/losbarberos-quito/"
    echo "    Script location: $SCRIPT_DIR"
    echo "──────────────────────────────────────────────────────────"
    read -n 1 -s -r -p "Press any key to close..."
    exit 1
fi

cd "$PROJ"

# --- 3. Banner --------------------------------------------------------------
clear
cat <<'BANNER'
  ╔════════════════════════════════════════════════════════╗
  ║   💈   L O S   B A R B E R O S   ·   Q U I T O   💈   ║
  ║              Premium Barbershop · Local Dev            ║
  ╚════════════════════════════════════════════════════════╝
BANNER
echo "  📁  $PROJ"
echo

# --- 4. Pick a Python interpreter -------------------------------------------
PYTHON=""
for cand in python3.12 python3.11 python3.10 python3; do
    if command -v "$cand" >/dev/null 2>&1; then PYTHON="$cand"; break; fi
done
if [ -z "$PYTHON" ]; then
    echo "❌  Python 3 not found. Install it from https://www.python.org/downloads/"
    read -n 1 -s -r -p "Press any key to close..."
    exit 1
fi
echo "  🐍  Using $($PYTHON --version)"

# --- 5. Free port 8501 if busy ----------------------------------------------
PORT=8501
if lsof -ti:$PORT >/dev/null 2>&1; then
    echo "  ⚠  Port $PORT busy — killing existing process"
    lsof -ti:$PORT | xargs kill -9 2>/dev/null || true
    sleep 1
fi

# --- 6. Ensure dependencies are installed -----------------------------------
if ! "$PYTHON" -c "import streamlit, streamlit_option_menu" >/dev/null 2>&1; then
    echo "  📦  Installing dependencies (first run only)..."
    "$PYTHON" -m pip install --quiet --upgrade pip
    "$PYTHON" -m pip install --quiet -r requirements.txt
    echo "  ✓  Dependencies installed"
fi

# --- 7. Open the browser shortly after Streamlit starts ---------------------
( sleep 3 && open "http://localhost:$PORT" ) &

# --- 8. Run Streamlit (foreground so Ctrl+C in this Terminal stops it) ------
echo
echo "  🚀  Booting site → http://localhost:$PORT"
echo "      (close this Terminal window or press Ctrl+C to stop)"
echo
exec "$PYTHON" -m streamlit run app.py --server.port "$PORT"
