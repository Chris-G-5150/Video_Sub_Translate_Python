#!/usr/bin/env bash
# ------------------------------------------
# Ruff Safe Fix Script
# ------------------------------------------
# Runs Ruff safely: checks, auto-fixes simple issues,
# and formats code without altering behavior.
# ------------------------------------------

set -e  # stop on first error
set -o pipefail

echo "🐍 Running Ruff Safe Fix Script"
echo "Project root: $(pwd)"
echo

# 1️⃣ Check for Ruff installation
if ! command -v ruff &> /dev/null; then
    echo "❌ Ruff not found. Install with:"
    echo "   pip install ruff"
    exit 1
fi

# 2️⃣ Step 1: Static analysis — no fixes
echo "🔍 Checking code for lint issues..."
ruff check . --exit-non-zero-on-fix --show-fixes --no-fix || true
echo

# 3️⃣ Step 2: Safe auto-fix (only unambiguous fixes)
echo "🧹 Applying safe fixes..."
ruff check . --fix --unsafe-fixes=never || true
echo

# 4️⃣ Step 3: Format code (non-destructive)
echo "✨ Formatting code..."
ruff format .
echo

# 5️⃣ Step 4: Final verification
echo "🔁 Rechecking after fixes..."
ruff check . --no-fix || true
echo

echo "✅ Ruff safe fix complete!"
