# =============================================================
# ADVANCED 6: REGULAR EXPRESSIONS
# =============================================================
#
# BIG IDEA:
#   Regex describes TEXT PATTERNS. Use them to search, extract,
#   validate, and replace strings. Python's module is `re`.
#
#   Tip: if a simple `in` / `.startswith` / `.split` works, use that.
#   Reach for regex when the pattern gets structured.
# =============================================================

import re


# --- Step 1: search vs match vs fullmatch --------------------
text = "order #A42 shipped"

print(re.search(r"\d+", text))          # first digits anywhere
print(re.match(r"order", text))         # only at the START
print(re.fullmatch(r"\d+", "42"))       # entire string must match
print(re.fullmatch(r"\d+", "42x"))      # None

print("-" * 50)


# --- Step 2: Common pattern pieces ---------------------------
#   .        any char except newline
#   \d \w \s digit / word char / whitespace
#   \D \W \S opposite of above
#   * + ?    0+ / 1+ / 0-or-1
#   {n,m}    between n and m times
#   ^ $      start / end of string
#   []       character class   [A-Za-z]
#   | ()     or / group
print(re.findall(r"\w+", "hi, Python_3!"))
print(re.findall(r"[A-Z]\d+", "codes A1 B22 c3 D4"))

print("-" * 50)


# --- Step 3: Groups — extract pieces -------------------------
email = "ada@example.com"
m = re.search(r"([\w.]+)@([\w.]+)", email)
if m:
    print("user:", m.group(1))
    print("host:", m.group(2))
    print("all: ", m.group(0))

# Named groups:
m = re.search(r"(?P<user>[\w.]+)@(?P<host>[\w.]+)", email)
print(m.group("user"), m.group("host"))

print("-" * 50)


# --- Step 4: findall / finditer / sub ------------------------
log = "ERROR 1 / WARN 2 / ERROR 3"
print(re.findall(r"ERROR \d+", log))

for m in re.finditer(r"(ERROR|WARN) (\d+)", log):
    print(f"  {m.group(1)} -> {m.group(2)}")

cleaned = re.sub(r"\s+", " ", "  too   much   space  ")
print(repr(cleaned.strip()))

print("-" * 50)


# --- Step 5: Compile for reuse -------------------------------
phone_re = re.compile(r"^\+?\d{10,15}$")
for candidate in ["+998901234567", "123", "not-a-phone"]:
    ok = bool(phone_re.fullmatch(candidate))
    print(f"  {candidate!r}: {ok}")

print("-" * 50)


# --- Step 6: Flags -------------------------------------------
print(re.search(r"python", "I ❤️ Python", re.IGNORECASE))
print(re.findall(r"^item:.*", "item: a\nitem: b", re.MULTILINE))


# =============================================================
# TRY IT YOURSELF:
#   1. Extract all hashtags from "love #python and #oop now".
#   2. Validate that a username is 3–12 alphanumeric chars.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Advanced 6) =====")
print(re.findall(r"#\w+", "love #python and #oop now"))

username_re = re.compile(r"^[A-Za-z0-9]{3,12}$")
for name in ["ada", "a", "Ada_Lovelace", "grace99"]:
    # underscore not allowed in our rule — grace99 ok, Ada_Lovelace no
    print(f"  {name}: {bool(username_re.fullmatch(name))}")
