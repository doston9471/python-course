# =============================================================
# ADVANCED 1: TYPE HINTS
# =============================================================
#
# BIG IDEA:
#   Type hints document what kinds of values a function expects and
#   returns. Python does NOT enforce them at runtime — tools like
#   mypy / pyright / IDEs use them. Optional, but professional code
#   uses them heavily.
#
#   Best studied after you're comfortable with functions + OOP.
# =============================================================

from __future__ import annotations  # nicer forward refs (optional)

from typing import Optional, Union, Callable, Any


# --- Step 1: Basic parameter & return hints ------------------
def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


print(greet("Ada"))
print(add(2, 3))

print("-" * 50)


# --- Step 2: Collections (modern Python 3.9+ syntax) ---------
def total(nums: list[int]) -> int:
    return sum(nums)


def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}


print(total([1, 2, 3]))
print(word_lengths(["hi", "python"]))

# Also: set[str], tuple[int, str], dict[str, list[int]]

print("-" * 50)


# --- Step 3: Optional and Union ------------------------------
# Optional[X] means X | None  (value or missing)
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Ada", 2: "Grace"}
    return users.get(user_id)   # may return None


# Python 3.10+ union with | :
def parse_id(value: str | int) -> int:
    return int(value)


print(find_user(1), find_user(99))
print(parse_id("42"), parse_id(7))

print("-" * 50)


# --- Step 4: Callable and Any --------------------------------
def apply_twice(fn: Callable[[int], int], n: int) -> int:
    return fn(fn(n))


print(apply_twice(lambda x: x + 1, 5))  # 7

def debug(value: Any) -> None:
    print(f"debug: {value!r}")


debug([1, 2, 3])

print("-" * 50)


# --- Step 5: Annotating classes ------------------------------
class User:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18


u = User("Ada", 36)
print(u.name, u.is_adult())

print("-" * 50)


# --- Step 6: Hints are NOT enforced --------------------------
# This runs fine — Python ignores the hints at runtime.
def double(n: int) -> int:
    return n * 2


print(double("ha"))   # "haha" — no TypeError!
# Use a type checker (mypy, pyright) to catch mistakes BEFORE running.


# =============================================================
# TRY IT YOURSELF:
#   1. Write `average(nums: list[float]) -> float`.
#   2. Write `lookup(data: dict[str, int], key: str) -> int | None`.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Advanced 1) =====")


def average(nums: list[float]) -> float:
    return sum(nums) / len(nums)


def lookup(data: dict[str, int], key: str) -> int | None:
    return data.get(key)


print(average([1.0, 2.0, 3.0]))
print(lookup({"a": 1}, "a"), lookup({"a": 1}, "z"))
