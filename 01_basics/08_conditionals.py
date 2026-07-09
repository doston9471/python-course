# =============================================================
# BASICS 8: CONDITIONALS (if / elif / else + match / case)
# =============================================================
#
# BIG IDEA:
#   Conditionals let your program choose a path based on True/False.
#   Indentation (usually 4 spaces) defines the block — no `end` keyword.
#
#   Python 3.10+ also has `match` / `case` — the switch/case equivalent
#   (structural pattern matching). Prefer if/elif for simple booleans;
#   prefer match when you're branching on a value's shape or several
#   fixed options.
# =============================================================


# --- Step 1: if / else ---------------------------------------
age = 20
if age >= 18:
    print("adult")
else:
    print("minor")

print("-" * 50)


# --- Step 2: elif (else if) ----------------------------------
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"grade = {grade}")

print("-" * 50)


# --- Step 3: and / or / not ----------------------------------
user = {"name": "Ada", "active": True, "role": "admin"}

if user["active"] and user["role"] == "admin":
    print("full access")

if not user["active"]:
    print("blocked")
else:
    print("allowed")

# Short-circuit: or returns first truthy, and returns first falsy
print(user.get("nickname") or "anonymous")

print("-" * 50)


# --- Step 4: Ternary (one-liner if/else) ---------------------
age = 16
status = "adult" if age >= 18 else "minor"
print(status)

print("-" * 50)


# --- Step 5: Membership in conditions ------------------------
fruit = "apple"
if fruit in ["apple", "banana", "cherry"]:
    print("known fruit")

code = "404"
if code in {"200", "201", "204"}:
    print("success")
elif code.startswith("4"):
    print("client error")
else:
    print("other")

print("-" * 50)


# --- Step 6: Truthiness in if --------------------------------
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Hello, stranger")   # empty string is falsy

items = [1]
if items:                       # non-empty list is truthy
    print(f"got {len(items)} item(s)")

print("-" * 50)


# --- Step 7: match / case (Python's switch) ------------------
# Like switch/case in other languages, but more powerful.
command = "start"

match command:
    case "start":
        print("starting...")
    case "stop":
        print("stopping...")
    case "pause" | "resume":   # several values in one case (OR)
        print("toggling pause")
    case _:                    # default (like else / default:)
        print(f"unknown command: {command}")

print("-" * 50)


# --- Step 8: match with guards & unpacking -------------------
# You can match structures (tuples, lists, dicts) and add `if` guards.
point = (0, 5)

match point:
    case (0, 0):
        print("origin")
    case (0, y):
        print(f"on Y axis at y={y}")
    case (x, 0):
        print(f"on X axis at x={x}")
    case (x, y) if x == y:
        print(f"on diagonal at ({x}, {y})")
    case (x, y):
        print(f"somewhere at ({x}, {y})")

# Dict-shaped matching:
event = {"type": "click", "x": 10, "y": 20}
match event:
    case {"type": "click", "x": x, "y": y}:
        print(f"clicked at ({x}, {y})")
    case {"type": "key", "key": key}:
        print(f"pressed {key}")
    case _:
        print("other event")

print("-" * 50)


# --- Step 9: if/elif vs match — when to use which ------------
# if/elif  -> conditions / comparisons (age >= 18, score bands)
# match    -> discrete values or structured shapes
status_code = 404
match status_code:
    case 200 | 201 | 204:
        print("success")
    case 400 | 404 | 422:
        print("client error")
    case 500 | 502 | 503:
        print("server error")
    case _:
        print("other status")


# =============================================================
# TRY IT YOURSELF:
#   1. Given a temperature, print "hot" (>=30), "cold" (<10),
#      or "ok" otherwise.  (use if/elif)
#   2. Print "ok to drive" only if age >= 18 AND has_license.
#   3. Using match/case: given day ("mon"..."sun"), print
#      "weekday" or "weekend". Handle an unknown day with _.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 8) =====")
temp = 22
if temp >= 30:
    print("hot")
elif temp < 10:
    print("cold")
else:
    print("ok")

age = 21
has_license = True
if age >= 18 and has_license:
    print("ok to drive")
else:
    print("cannot drive")

day = "sat"
match day:
    case "mon" | "tue" | "wed" | "thu" | "fri":
        print("weekday")
    case "sat" | "sun":
        print("weekend")
    case _:
        print("unknown day")
