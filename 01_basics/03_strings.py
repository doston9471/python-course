# =============================================================
# BASICS 3: STRINGS
# =============================================================
#
# BIG IDEA:
#   Strings are sequences of characters. You create them with
#   quotes. f-strings are the modern way to embed values.
# =============================================================


# --- Step 1: Creating strings --------------------------------
s1 = "double quotes"
s2 = 'single quotes'
s3 = """multi-
line
string"""
print(s1)
print(s2)
print(s3)

print("-" * 50)


# --- Step 2: f-strings (preferred) ---------------------------
name = "Ada"
age = 36
print(f"My name is {name} and I am {age}.")
print(f"Next year I'll be {age + 1}.")
print(f"{name.upper()} — {age}")

# Older styles (still around):
print("Hello, {}".format(name))
print("Hello, %s" % name)

print("-" * 50)


# --- Step 3: Indexing & slicing ------------------------------
# Characters are numbered starting at 0.
text = "Python"
print(text[0])       # P
print(text[-1])      # n  (last character)
print(text[0:3])     # Pyt  (start inclusive, end exclusive)
print(text[:2])      # Py
print(text[2:])      # thon
print(text[::2])     # Pto  (every 2nd char)
print(text[::-1])    # nohtyP  (reverse)

print("-" * 50)


# --- Step 4: Useful string methods ---------------------------
msg = "  Hello, World!  "
print(msg.strip())           # trim whitespace
print(msg.lower())
print(msg.upper())
print(msg.replace("World", "Python"))
print("hello".startswith("he"))
print("hello".endswith("lo"))
print("a,b,c".split(","))    # list: ['a', 'b', 'c']
print("-".join(["a", "b", "c"]))  # "a-b-c"
print(len("hello"))          # 5

print("-" * 50)


# --- Step 5: Membership & immutability -----------------------
print("yth" in "Python")     # True
print("java" in "Python")    # False

# Strings can't be changed in place:
# text[0] = "J"   # TypeError — strings are immutable
# To "change", make a new string:
text = "J" + text[1:]
print(text)


# =============================================================
# TRY IT YOURSELF:
#   1. Store your full name. Print first and last names via split.
#   2. Print initials in uppercase with an f-string.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 3) =====")
full = "Ada Lovelace"
first, last = full.split()
print(first, last)
print(f"{first[0].upper()}.{last[0].upper()}.")
