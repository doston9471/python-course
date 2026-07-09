# =============================================================
# BASICS 7: TUPLES & SETS
# =============================================================
#
# BIG IDEA:
#   tuple — ordered, IMMUTABLE sequence (can't change after creation)
#   set   — unordered collection of UNIQUE items
# =============================================================


# --- Step 1: Tuples ------------------------------------------
point = (3, 4)
rgb = 255, 128, 0          # parentheses optional
alone = (42,)              # trailing comma makes a 1-item tuple
print(point, rgb, alone)
print(point[0], point[-1])
print(len(point))

# Unpacking (very common):
x, y = point
print(f"x={x}, y={y}")

# Tuples are immutable:
# point[0] = 99   # TypeError

print("-" * 50)


# --- Step 2: When to use tuples ------------------------------
# - Fixed-size records (x, y), (lat, lon)
# - Dict keys (lists can't be keys; tuples can)
# - Returning multiple values from a function
location = {(0, 0): "origin", (1, 2): "treasure"}
print(location[(1, 2)])

print("-" * 50)


# --- Step 3: Sets --------------------------------------------
letters = {"a", "b", "c", "a"}   # duplicate "a" is dropped
print(letters)                   # order not guaranteed

nums = set([1, 2, 2, 3, 3, 3])
print(nums)                      # {1, 2, 3}

print("-" * 50)


# --- Step 4: Set operations ----------------------------------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)     # union
print(a & b)     # intersection
print(a - b)     # difference
print(a ^ b)     # symmetric difference (in one, not both)

a.add(99)
a.discard(1)     # remove if present (no error if missing)
print(a)
print(3 in a)

print("-" * 50)


# --- Step 5: Deduplicating a list ----------------------------
names = ["Ann", "Bob", "Ann", "Cy", "Bob"]
unique = list(set(names))
print(unique)    # order may change


# =============================================================
# TRY IT YOURSELF:
#   1. Make a tuple of your (city, country) and unpack it.
#   2. Given two lists of tags, print the tags they share.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 7) =====")
place = ("Tashkent", "Uzbekistan")
city, country = place
print(f"{city}, {country}")

mine = ["python", "oop", "ruby"]
yours = ["ruby", "rails", "oop"]
print(set(mine) & set(yours))
