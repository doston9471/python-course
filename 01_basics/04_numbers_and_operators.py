# =============================================================
# BASICS 4: NUMBERS & OPERATORS
# =============================================================
#
# BIG IDEA:
#   Python does math like a calculator. Comparisons return True/False.
#   Truthiness decides if a value counts as "yes" in an if/while.
# =============================================================


# --- Step 1: Arithmetic --------------------------------------
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)       # always float division -> 3.333...
print(10 // 3)      # floor division -> 3
print(10 % 3)       # remainder -> 1
print(2 ** 8)       # power -> 256

print("-" * 50)


# --- Step 2: Assignment shortcuts ----------------------------
n = 5
n += 2    # n = n + 2
n *= 3    # n = n * 3
print(n)  # 21

print("-" * 50)


# --- Step 3: Comparisons -------------------------------------
print(5 == 5)     # True  (equal)
print(5 != 3)     # True  (not equal)
print(5 > 3)
print(5 >= 5)
print(5 < 3)
print(5 <= 3)

# Chained comparisons (very Pythonic):
x = 7
print(1 < x < 10)   # True — like math

print("-" * 50)


# --- Step 4: Boolean operators -------------------------------
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

age = 20
print(age >= 18 and age < 65)

print("-" * 50)


# --- Step 5: Truthiness --------------------------------------
# Falsy values: False, None, 0, 0.0, "", [], {}, set()
# Everything else is truthy.
print(bool(0), bool(1))
print(bool(""), bool("hi"))
print(bool([]), bool([1]))
print(bool(None))

print("-" * 50)


# --- Step 6: Useful built-ins --------------------------------
print(abs(-7))
print(round(3.14159, 2))
print(min(3, 1, 4), max(3, 1, 4))
print(sum([1, 2, 3, 4]))


# =============================================================
# TRY IT YOURSELF:
#   1. Compute the average of 10, 20, 30.
#   2. Check whether a number is even (hint: % 2 == 0).
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 4) =====")
nums = [10, 20, 30]
avg = sum(nums) / len(nums)
print(f"average = {avg}")
n = 14
print(f"{n} is even? {n % 2 == 0}")
