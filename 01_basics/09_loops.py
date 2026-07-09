# =============================================================
# BASICS 9: LOOPS
# =============================================================
#
# BIG IDEA:
#   for  — iterate over items in a sequence (lists, strings, ranges…)
#   while — repeat while a condition is True
# =============================================================


# --- Step 1: for over a list ---------------------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  I like {fruit}")

print("-" * 50)


# --- Step 2: range(start, stop, step) -------------------------
# stop is exclusive — range(5) means 0,1,2,3,4
for i in range(5):
    print(i, end=" ")
print()

for i in range(2, 8, 2):   # 2, 4, 6
    print(i, end=" ")
print()

print("-" * 50)


# --- Step 3: enumerate (index + value) -----------------------
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

for i, fruit in enumerate(fruits, start=1):
    print(f"  #{i} {fruit}")

print("-" * 50)


# --- Step 4: while -------------------------------------------
n = 3
while n > 0:
    print(f"  countdown {n}")
    n -= 1
print("  liftoff!")

print("-" * 50)


# --- Step 5: break and continue ------------------------------
for n in range(10):
    if n == 3:
        continue          # skip this iteration
    if n == 7:
        break             # stop the loop entirely
    print(n, end=" ")
print()

print("-" * 50)


# --- Step 6: else on loops (runs if loop didn't break) -------
for n in [2, 4, 6]:
    if n % 2 != 0:
        print("found odd")
        break
else:
    print("all even")     # ran because no break

print("-" * 50)


# --- Step 7: Nested loops & looping a dict -------------------
for row in range(1, 3):
    for col in range(1, 3):
        print(f"({row},{col})", end=" ")
    print()

scores = {"Ann": 10, "Bob": 20}
for name, score in scores.items():
    print(f"  {name} scored {score}")


# =============================================================
# TRY IT YOURSELF:
#   1. Print numbers 1–10, skipping multiples of 3.
#   2. Sum all numbers in [1, 2, 3, 4, 5] with a for loop.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 9) =====")
for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n, end=" ")
print()

total = 0
for n in [1, 2, 3, 4, 5]:
    total += n
print(f"sum = {total}")
