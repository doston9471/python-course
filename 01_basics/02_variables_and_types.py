# =============================================================
# BASICS 2: VARIABLES & TYPES
# =============================================================
#
# BIG IDEA:
#   A variable is a name that points to a value.
#   Python figures out the type for you (dynamic typing).
# =============================================================


# --- Step 1: Assigning variables -----------------------------
name = "Ada"
age = 36
height = 1.65
is_alive = True
nickname = None          # "no value" / empty

print(name, age, height, is_alive, nickname)

print("-" * 50)


# --- Step 2: Types with type() -------------------------------
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_alive))    # <class 'bool'>
print(type(nickname))    # <class 'NoneType'>

print("-" * 50)


# --- Step 3: Reassignment & multiple assignment --------------
x = 10
x = 20                   # now x points to 20
print(f"x = {x}")

a, b, c = 1, 2, 3        # unpack on one line
print(a, b, c)

# Swap without a temp variable:
a, b = b, a
print(f"swapped: a={a}, b={b}")

print("-" * 50)


# --- Step 4: Naming rules ------------------------------------
# Good: snake_case, descriptive
user_name = "grace"
total_count = 5
_is_private_by_convention = True

# Bad / invalid:
# 2cool = 1      # can't start with a digit
# my-var = 1     # hyphen not allowed
# class = 1      # reserved keyword

print("-" * 50)


# --- Step 5: Converting types (casting) ----------------------
print(int("42"))         # 42
print(float("3.14"))     # 3.14
print(str(100))          # "100"
print(bool(1), bool(0))  # True False
print(bool(""), bool("hi"))  # False True  (empty string is falsy)

print("-" * 50)


# --- Step 6: Constants (by convention) -----------------------
# Python has no true constants. ALL_CAPS means "please don't change".
MAX_USERS = 100
PI = 3.14159
print(MAX_USERS, PI)


# =============================================================
# TRY IT YOURSELF:
#   1. Create variables for city, population, and is_capital.
#   2. Print them with their types.
#   3. Convert the string "99" to an int and add 1.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 2) =====")
city = "Tashkent"
population = 2_800_000   # underscores allowed in numbers for readability
is_capital = True
print(city, type(city))
print(population, type(population))
print(is_capital, type(is_capital))
print(int("99") + 1)
