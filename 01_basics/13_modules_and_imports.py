# =============================================================
# BASICS 13: MODULES & IMPORTS
# =============================================================
#
# BIG IDEA:
#   Real programs are split across files. A MODULE is a .py file.
#   `import` loads code from another module so you can reuse it.
# =============================================================


# --- Step 1: Import a whole module ---------------------------
import math

print(math.pi)
print(math.sqrt(16))
print(math.ceil(3.2))

print("-" * 50)


# --- Step 2: Import specific names ---------------------------
from math import pi, sqrt

print(pi)
print(sqrt(25))
# print(math.ceil(1.1))  # NameError — math itself wasn't imported

print("-" * 50)


# --- Step 3: Aliases (as) ------------------------------------
import math as m
from datetime import datetime as dt

print(m.floor(3.9))
print(dt.now().year)

print("-" * 50)


# --- Step 4: Common stdlib modules you'll see a lot ----------
import random
import json
from collections import Counter
from pathlib import Path

print(random.randint(1, 6))
print(Counter("banana"))          # counts each letter
print(Path(".").resolve().name)

print("-" * 50)


# --- Step 5: if __name__ == "__main__" -----------------------
# When you RUN a file directly, __name__ is "__main__".
# When another file IMPORTS it, __name__ is the module name.
# Put demo/CLI code under this guard so imports stay clean.

def double(n):
    return n * 2


def _demo():
    print("running as a script...")
    print(double(21))


if __name__ == "__main__":
    _demo()

print("-" * 50)


# --- Step 6: Your own modules (how projects grow) ------------
# Imagine a file helpers.py:
#     def shout(text): return text.upper()
#
# Then in main.py:
#     from helpers import shout
#     print(shout("hello"))
#
# Rules of thumb:
#   - one idea per file / module
#   - prefer `from x import y` for a few names
#   - prefer `import x` when you use many names from x
#   - avoid `from x import *` (pollutes namespace, hard to track)

# Relative imports (packages) come later when you add folders
# with __init__.py. For now, same-folder imports are enough.


# =============================================================
# TRY IT YOURSELF:
#   1. Import `statistics` and print the mean of [1, 2, 3, 4, 5].
#   2. Write a function `greet(name)` and call it only inside
#      `if __name__ == "__main__":`.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 13) =====")

import statistics

print(statistics.mean([1, 2, 3, 4, 5]))


def greet(name):
    return f"Hi, {name}!"


if __name__ == "__main__":
    print(greet("Ada"))
