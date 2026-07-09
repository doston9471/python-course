# =============================================================
# BASICS 10: FUNCTIONS
# =============================================================
#
# BIG IDEA:
#   Functions package reusable behavior. `def` defines them;
#   `return` sends a value back to the caller.
# =============================================================


# --- Step 1: Defining & calling ------------------------------
def greet(name):
    return f"Hello, {name}!"


print(greet("Ada"))

print("-" * 50)


# --- Step 2: Multiple params & defaults ----------------------
def introduce(name, role="student"):
    return f"{name} is a {role}"


print(introduce("Ada"))
print(introduce("Ada", "engineer"))
print(introduce(role="scientist", name="Grace"))  # keyword args

print("-" * 50)


# --- Step 3: Returning multiple values -----------------------
def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)


lo, hi, avg = stats([10, 20, 30])
print(lo, hi, avg)

print("-" * 50)


# --- Step 4: *args and **kwargs ------------------------------
# *args  = extra positional args as a tuple
# **kwargs = extra keyword args as a dict
def log(label, *args, **kwargs):
    print(f"[{label}] args={args} kwargs={kwargs}")


log("info", 1, 2, 3, user="Ada", level=1)

print("-" * 50)


# --- Step 5: Docstrings & early return -----------------------
def is_adult(age):
    """Return True if age is 18 or older."""
    if age < 0:
        return False
    return age >= 18


print(is_adult(20), is_adult(15), is_adult.__doc__)

print("-" * 50)


# --- Step 6: Scope (local vs global) -------------------------
count = 0   # global


def bump():
    # Without `global`, this would create a NEW local `count`
    # and never touch the outer one.
    global count
    count += 1


bump()
bump()
print(f"count = {count}")

# Prefer returning values over mutating globals.


# =============================================================
# TRY IT YOURSELF:
#   1. Write `area(width, height=1)` returning width * height.
#   2. Write `join_words(*words)` that joins with a space.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 10) =====")


def area(width, height=1):
    return width * height


def join_words(*words):
    return " ".join(words)


print(area(5))
print(area(5, 3))
print(join_words("hello", "python", "world"))
