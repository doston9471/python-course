# =============================================================
# BASICS 11: COMPREHENSIONS
# =============================================================
#
# BIG IDEA:
#   Comprehensions build a new list/dict/set in one expression.
#   They're the Pythonic alternative to many short for-loops.
# =============================================================


# --- Step 1: List comprehension ------------------------------
# Long form:
squares = []
for n in range(6):
    squares.append(n * n)
print(squares)

# Short form:
squares = [n * n for n in range(6)]
print(squares)

print("-" * 50)


# --- Step 2: Filtering with if -------------------------------
evens = [n for n in range(10) if n % 2 == 0]
print(evens)

words = ["hi", "Python", "ok", "comprehension"]
long = [w.upper() for w in words if len(w) > 3]
print(long)

print("-" * 50)


# --- Step 3: Dict comprehension ------------------------------
names = ["Ann", "Bob", "Cy"]
lengths = {name: len(name) for name in names}
print(lengths)

# Flip keys/values (when values are unique):
flipped = {v: k for k, v in lengths.items()}
print(flipped)

print("-" * 50)


# --- Step 4: Set comprehension -------------------------------
letters = {ch.lower() for ch in "Hello"}
print(letters)   # unique letters, lowercased

print("-" * 50)


# --- Step 5: Nested / with existing loops --------------------
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]
print(flat)

# When a comprehension gets hard to read, use a normal for-loop.
# Clarity > cleverness.


# =============================================================
# TRY IT YOURSELF:
#   1. Build a list of the first 10 cubes (n**3).
#   2. From ["a", "bb", "ccc", "d"], keep only length > 1,
#      mapped to uppercase, as a list.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 11) =====")
cubes = [n ** 3 for n in range(10)]
print(cubes)
result = [w.upper() for w in ["a", "bb", "ccc", "d"] if len(w) > 1]
print(result)
