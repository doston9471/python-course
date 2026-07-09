# =============================================================
# BASICS 5: LISTS (arrays)
# =============================================================
#
# BIG IDEA:
#   A list is an ordered, mutable collection of items.
#   Think Ruby Array / JS Array.
# =============================================================


# --- Step 1: Creating lists ----------------------------------
empty = []
nums = [1, 2, 3, 4]
mixed = [1, "two", 3.0, True]   # any types are allowed
nested = [[1, 2], [3, 4]]

print(nums)
print(mixed)

print("-" * 50)


# --- Step 2: Indexing & slicing (same idea as strings) -------
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])       # apple
print(fruits[-1])      # date
print(fruits[1:3])     # ['banana', 'cherry']
print(len(fruits))     # 4

print("-" * 50)


# --- Step 3: Mutating lists ----------------------------------
fruits.append("elderberry")     # add to end
fruits.insert(1, "apricot")     # insert at index
fruits.extend(["fig", "grape"]) # add many
print(fruits)

fruits[0] = "APPLE"             # change by index
print(fruits)

popped = fruits.pop()           # remove & return last
print("popped:", popped)
fruits.remove("apricot")        # remove first matching value
print(fruits)

print("-" * 50)


# --- Step 4: Useful methods & ops ----------------------------
nums = [3, 1, 4, 1, 5]
print(sorted(nums))             # new sorted list
nums.sort()                     # sort in place
print(nums)
nums.reverse()
print(nums)
print(nums.count(1))
print(1 in nums)                # membership
print([1, 2] + [3, 4])          # concatenate
print([0] * 5)                  # [0, 0, 0, 0, 0]

print("-" * 50)


# --- Step 5: Unpacking ---------------------------------------
a, b, c = [10, 20, 30]
print(a, b, c)

first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)      # 1 [2, 3, 4] 5

print("-" * 50)


# --- Step 6: Copying carefully -------------------------------
original = [1, 2, 3]
alias = original                # same list! changing one changes the other
copy = original[:]              # shallow copy (or list(original) / original.copy())
alias.append(99)
print("original:", original)    # [1, 2, 3, 99]
print("copy:    ", copy)        # [1, 2, 3]


# =============================================================
# TRY IT YOURSELF:
#   1. Make a list of 5 favorite languages.
#   2. Add one, remove one, print the first and last.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 5) =====")
langs = ["Python", "Ruby", "Go", "Rust", "Elixir"]
langs.append("TypeScript")
langs.remove("Go")
print(langs[0], langs[-1])
print(langs)
