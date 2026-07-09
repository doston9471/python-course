# =============================================================
# ADVANCED 4: VIRTUALENVS, PIP & UV  (tooling)
# =============================================================
#
# BIG IDEA:
#   Don't install packages into your system Python. Use a virtual
#   environment (venv) so each project gets its own isolated deps.
#
#   This lesson is a runnable cheat sheet — run it to print the
#   commands, then try them in your terminal.
# =============================================================

import sys
import subprocess
from pathlib import Path


print("Your current Python:")
print(f"  executable: {sys.executable}")
print(f"  version:    {sys.version.split()[0]}")
print(f"  prefix:     {sys.prefix}")

print("-" * 50)


# --- Step 1: Why venvs? --------------------------------------
print("""
WHY VIRTUAL ENVIRONMENTS?
-------------------------
Projects need different package versions. A venv keeps them separate
so Project A (Django 4) doesn't break Project B (Django 5).
""")

print("-" * 50)


# --- Step 2: Classic tools — venv + pip ----------------------
print("""
OPTION A: stdlib venv + pip
---------------------------
# create (once per project)
python3 -m venv .venv

# activate (every new terminal)
source .venv/bin/activate          # macOS / Linux
# .venv\\Scripts\\activate         # Windows

# install packages
pip install requests
pip install -r requirements.txt

# freeze what you use
pip freeze > requirements.txt

# deactivate
deactivate
""")

print("-" * 50)


# --- Step 3: Modern option — uv ------------------------------
print("""
OPTION B: uv (fast, recommended)
--------------------------------
# install uv once
brew install uv
# or: curl -LsSf https://astral.sh/uv/install.sh | sh

# create + sync deps (reads pyproject.toml / requirements)
uv venv
source .venv/bin/activate
uv pip install requests

# or the all-in-one project flow:
uv init myapp
cd myapp
uv add requests
uv run python main.py
""")

print("-" * 50)


# --- Step 4: Minimal requirements.txt example ----------------
demo = Path("/tmp/oop_python_reqs_demo")
demo.mkdir(parents=True, exist_ok=True)
reqs = demo / "requirements.txt"
reqs.write_text("requests==2.32.3\n", encoding="utf-8")
print(f"Example requirements.txt written to {reqs}")
print(reqs.read_text())

print("-" * 50)


# --- Step 5: Check if a package is importable ----------------
def package_status(name: str) -> str:
    try:
        __import__(name)
        return "installed"
    except ImportError:
        return "NOT installed"


for pkg in ["json", "pathlib", "requests", "pytest"]:
    # json/pathlib are stdlib; requests/pytest are third-party
    label = pkg if pkg not in {"json", "pathlib"} else f"{pkg} (stdlib)"
    print(f"  {label}: {package_status(pkg)}")

print("-" * 50)


# --- Step 6: Show pip (if available) -------------------------
try:
    out = subprocess.check_output(
        [sys.executable, "-m", "pip", "--version"],
        text=True,
        stderr=subprocess.STDOUT,
    )
    print("pip:", out.strip())
except Exception as e:
    print("pip not available via this Python:", e)


# =============================================================
# TRY IT YOURSELF (in your terminal, not this file):
#   1. cd into this project and create a venv:  python3 -m venv .venv
#   2. Activate it and `pip install pytest`
#   3. `pip freeze` and confirm pytest is listed
# =============================================================


print("\n===== SOLUTION / CHECKLIST (Advanced 4) =====")
print("""
[ ] python3 -m venv .venv
[ ] source .venv/bin/activate
[ ] pip install pytest   (or: uv pip install pytest)
[ ] pip freeze | grep -i pytest
[ ] deactivate when done
""")

# cleanup demo file
reqs.unlink(missing_ok=True)
demo.rmdir()
