# =============================================================
# BASICS 15: JSON & PATHLIB
# =============================================================
#
# BIG IDEA:
#   Most apps read/write structured data. JSON is the usual format.
#   pathlib is the modern way to work with file paths.
# =============================================================

import json
from pathlib import Path


# --- Step 1: pathlib basics ----------------------------------
# Path objects understand / for joining (works on every OS).
base = Path("/tmp") / "oop_python_basics"
base.mkdir(parents=True, exist_ok=True)

print(base)
print(base.exists(), base.is_dir())
print(base.name)                 # last part
print(base.parent)               # directory above

print("-" * 50)


# --- Step 2: Read / write text the easy way ------------------
note = base / "note.txt"
note.write_text("hello from pathlib\n", encoding="utf-8")
print(note.read_text(encoding="utf-8").strip())

print("-" * 50)


# --- Step 3: JSON — Python <-> text --------------------------
# Python dict/list  ->  JSON object/array (string or file)
person = {
    "name": "Ada",
    "age": 36,
    "languages": ["Python", "Math"],
    "active": True,
    "nickname": None,
}

# to a string:
text = json.dumps(person, indent=2)
print(text)

# from a string:
restored = json.loads(text)
print(restored["name"], restored["languages"])

print("-" * 50)


# --- Step 4: JSON files with pathlib -------------------------
data_file = base / "person.json"
data_file.write_text(json.dumps(person, indent=2), encoding="utf-8")

loaded = json.loads(data_file.read_text(encoding="utf-8"))
print(loaded)

# Or with open() if you prefer streaming larger files:
with data_file.open("r", encoding="utf-8") as f:
    also = json.load(f)
print(also["age"])

print("-" * 50)


# --- Step 5: Type mapping (mental cheat sheet) ---------------
# Python          JSON
# dict            object { }
# list / tuple    array  [ ]
# str             string
# int / float     number
# True / False    true / false
# None            null
#
# Note: JSON keys are always strings. Sets & custom objects
# need conversion first.

print("-" * 50)


# --- Step 6: Listing & cleaning up ---------------------------
for path in sorted(base.iterdir()):
    print(f"  {path.name} ({path.stat().st_size} bytes)")

# Cleanup demo files:
note.unlink(missing_ok=True)
data_file.unlink(missing_ok=True)
base.rmdir()


# =============================================================
# TRY IT YOURSELF:
#   1. Write a list of 3 book dicts to books.json under /tmp.
#   2. Load it back and print each book's title.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 15) =====")

books_dir = Path("/tmp") / "oop_python_books"
books_dir.mkdir(parents=True, exist_ok=True)
books_file = books_dir / "books.json"

books = [
    {"title": "The Hobbit", "pages": 310},
    {"title": "Dune", "pages": 412},
    {"title": "Neuromancer", "pages": 271},
]
books_file.write_text(json.dumps(books, indent=2), encoding="utf-8")

for book in json.loads(books_file.read_text(encoding="utf-8")):
    print(book["title"])

books_file.unlink(missing_ok=True)
books_dir.rmdir()
