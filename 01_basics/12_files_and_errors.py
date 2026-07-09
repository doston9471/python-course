# =============================================================
# BASICS 12: FILES & ERRORS
# =============================================================
#
# BIG IDEA:
#   Real programs talk to the outside world. You open files and
#   catch errors so one failure doesn't crash everything.
# =============================================================

from pathlib import Path


# --- Step 1: Writing a file ----------------------------------
# Prefer pathlib; `with` auto-closes the file (even on errors).
path = Path("/tmp/oop_python_basics_demo.txt")

with path.open("w", encoding="utf-8") as f:
    f.write("line 1\n")
    f.write("line 2\n")
print(f"wrote {path}")

print("-" * 50)


# --- Step 2: Reading a file ----------------------------------
with path.open("r", encoding="utf-8") as f:
    content = f.read()
print(repr(content))

with path.open("r", encoding="utf-8") as f:
    for line in f:                   # stream line by line
        print(">", line.strip())

print("-" * 50)


# --- Step 3: try / except ------------------------------------
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "can't divide by zero"


print(safe_divide(10, 2))
print(safe_divide(10, 0))

print("-" * 50)


# --- Step 4: Multiple excepts + else + finally ---------------
def parse_age(text):
    try:
        age = int(text)
    except ValueError as e:
        print(f"  bad input: {e}")
        return None
    except TypeError:
        print("  need a string")
        return None
    else:
        # runs only if NO exception was raised
        print("  parsed ok")
        return age
    finally:
        # ALWAYS runs (cleanup, logging…)
        print("  done parsing")


print("result:", parse_age("36"))
print("result:", parse_age("oops"))

print("-" * 50)


# --- Step 5: Raising your own errors -------------------------
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount


try:
    print(withdraw(100, 30))
    print(withdraw(100, 200))
except ValueError as e:
    print(f"blocked: {e}")

print("-" * 50)


# --- Step 6: File not found ----------------------------------
try:
    Path("/tmp/no_such_file_xyz.txt").read_text()
except FileNotFoundError as e:
    print(f"missing file: {e.filename}")

# Cleanup demo file
path.unlink(missing_ok=True)


# =============================================================
# TRY IT YOURSELF:
#   1. Write three names to a temp file, then read them back.
#   2. Write `safe_int(text)` that returns None on bad input.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 12) =====")
demo = Path("/tmp/oop_python_names.txt")
demo.write_text("Ada\nGrace\nAlan\n", encoding="utf-8")
print(demo.read_text(encoding="utf-8").strip().splitlines())
demo.unlink(missing_ok=True)


def safe_int(text):
    try:
        return int(text)
    except (ValueError, TypeError):
        return None


print(safe_int("42"), safe_int("nope"), safe_int(None))
