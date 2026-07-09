# =============================================================
# BASICS 14: USEFUL BUILTINS — zip, lambda, sorting, is vs ==
# =============================================================
#
# BIG IDEA:
#   A handful of built-ins show up everywhere. Master these and a
#   lot of "real" Python suddenly looks familiar.
# =============================================================


# --- Step 1: enumerate (recap) & zip -------------------------
names = ["Ann", "Bob", "Cy"]
scores = [10, 20, 15]

for i, name in enumerate(names, start=1):
    print(f"  #{i} {name}")

print("---")
# zip pairs items from multiple sequences (stops at shortest)
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# Turn pairs into a dict:
print(dict(zip(names, scores)))

print("-" * 50)


# --- Step 2: lambda — tiny anonymous functions ---------------
# Use for short one-liners passed into other functions.
# Prefer `def` when the body needs a name or >1 line.
add = lambda a, b: a + b
print(add(2, 3))

nums = [3, 1, 4, 1, 5]
print(sorted(nums, key=lambda n: -n))          # descending via key
print(sorted(["bb", "a", "ccc"], key=len))     # sort by length

print("-" * 50)


# --- Step 3: map & filter (optional style) -------------------
# Modern Python often prefers comprehensions, but you'll see these.
nums = [1, 2, 3, 4, 5]
print(list(map(lambda n: n * 2, nums)))        # [2, 4, 6, 8, 10]
print(list(filter(lambda n: n % 2 == 0, nums))) # [2, 4]

# Same with comprehensions (usually clearer):
print([n * 2 for n in nums])
print([n for n in nums if n % 2 == 0])

print("-" * 50)


# --- Step 4: Sorting deep dive -------------------------------
people = [
    {"name": "Cy", "age": 30},
    {"name": "Ann", "age": 25},
    {"name": "Bob", "age": 25},
]

# sorted() returns a NEW list; list.sort() mutates in place
by_age = sorted(people, key=lambda p: p["age"])
print(by_age)

# Sort by age, then name (tuple key):
by_age_name = sorted(people, key=lambda p: (p["age"], p["name"]))
print(by_age_name)

# Reverse:
print(sorted([3, 1, 2], reverse=True))

print("-" * 50)


# --- Step 5: == vs is ----------------------------------------
# ==  -> value equality  ("do these look the same?")
# is  -> identity        ("are these the SAME object in memory?")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  — same contents
print(a is b)   # False — different objects
print(a is c)   # True  — same object

# Always compare to None with `is` / `is not`:
x = None
print(x is None)
print(x is not None)

print("-" * 50)


# --- Step 6: any / all ---------------------------------------
print(any([False, False, True]))   # True  — at least one truthy
print(all([True, True, True]))     # True  — every item truthy
print(all([True, False, True]))    # False

ages = [19, 22, 17]
print(all(age >= 18 for age in ages))  # False — generator works too


# =============================================================
# TRY IT YOURSELF:
#   1. zip ["a","b","c"] with [1,2,3] into a dict.
#   2. Sort ["python", "go", "ruby"] by length ascending.
#   3. Show that two equal strings can be == but explain when
#      `is` is the right tool (hint: None).
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 14) =====")
print(dict(zip(["a", "b", "c"], [1, 2, 3])))
print(sorted(["python", "go", "ruby"], key=len))

s1 = "hi"
s2 = "hi"
print(s1 == s2)             # value equal
print(None is None)         # identity check — correct for None
