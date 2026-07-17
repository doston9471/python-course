# =============================================================
# BASICS 1: HELLO & PRINT
# =============================================================
#
# BIG IDEA:
#   A Python program is just a .py file that runs top to bottom.
#   `print()` sends text (or any value) to the terminal.
# =============================================================


# --- Step 1: Your first program ------------------------------
print("Hello, Python!")

# --- Step 2: Comments ----------------------------------------
# This is a comment. Python ignores everything after #.


# --- Step 3: Printing multiple things ------------------------
print("Name:", "Ada")
print(1, 2, 3)                    # spaces between by default
print("a", "b", "c", sep="-")    # custom separator
print("Hello", end=" ")          # don't end with newline
print("world!")

print("-" * 50)


# --- Step 4: Blank lines & readability -----------------------
# Blank lines don't matter to Python — use them to group ideas.
print("Lesson 1 complete.")


# =============================================================
# TRY IT YOURSELF:
#   1. Print your name.
#   2. Print three cities on one line, separated by " | ".
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 1) =====")
print("Tony")
print("Tashkent", "Seoul", "Tokyo", sep=" | ")
