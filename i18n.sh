#!/usr/bin/env bash
set -e
echo "🌐 Extracting…"  && pybabel extract -F babel.cfg -o messages.pot .
echo "🔄 Updating  …"  && pybabel update  -i messages.pot -d translations
echo "⚙️  Compiling…" && pybabel compile -d translations
echo "✅ Babel strings refreshed. Open your .po to translate!"
