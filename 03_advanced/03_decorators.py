# =============================================================
# ADVANCED 3: DECORATORS
# =============================================================
#
# BIG IDEA:
#   A decorator is a function that WRAPS another function to add
#   behavior (logging, timing, access checks…) without editing the
#   original body.
#
#   Syntax sugar:
#     @decorator
#     def f(): ...
#   means:
#     def f(): ...
#     f = decorator(f)
# =============================================================

import time
from functools import wraps


# --- Step 1: Functions are objects you can pass around -------
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def speak(style, text):
    return style(text)


print(speak(shout, "Hello"))
print(speak(whisper, "Hello"))

print("-" * 50)


# --- Step 2: A simple decorator ------------------------------
def trace(fn):
    def wrapper(*args, **kwargs):
        print(f"  calling {fn.__name__}{args}")
        result = fn(*args, **kwargs)
        print(f"  -> {result}")
        return result
    return wrapper


@trace
def add(a, b):
    return a + b


print(add(2, 3))

print("-" * 50)


# --- Step 3: Preserve metadata with @wraps -------------------
def timer(fn):
    @wraps(fn)            # keeps __name__, __doc__ of the original
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {fn.__name__} took {elapsed:.6f}s")
        return result
    return wrapper


@timer
def slow_sum(n):
    """Sum 0..n-1 the hard way."""
    total = 0
    for i in range(n):
        total += i
    return total


print(slow_sum(100_000))
print(slow_sum.__name__, slow_sum.__doc__)

print("-" * 50)


# --- Step 4: Decorator with arguments ------------------------
def repeat(times):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def hello(name):
    print(f"  Hi, {name}!")


hello("Ada")

print("-" * 50)


# --- Step 5: Stacking & method decorators --------------------
# You already know @classmethod, @staticmethod, @property —
# those ARE decorators built into Python.

class Counter:
    def __init__(self):
        self._n = 0

    @property
    def n(self):
        return self._n

    @timer
    def tick(self):
        self._n += 1
        return self._n


c = Counter()
c.tick()
c.tick()
print(f"count = {c.n}")


# =============================================================
# TRY IT YOURSELF:
#   1. Write `@shout_result` that uppercases a string return value.
#   2. Decorate a `greet(name)` function with it.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Advanced 3) =====")


def shout_result(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return str(fn(*args, **kwargs)).upper()
    return wrapper


@shout_result
def greet(name):
    return f"hello, {name}"


print(greet("Ada"))
