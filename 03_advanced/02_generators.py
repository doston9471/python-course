# =============================================================
# ADVANCED 2: GENERATORS & YIELD
# =============================================================
#
# BIG IDEA:
#   A generator produces values ONE AT A TIME instead of building a
#   whole list in memory. Use `yield` instead of `return`.
#
#   Great for large (or infinite) streams of data.
# =============================================================


# --- Step 1: Generator function ------------------------------
def count_up_to(n):
    i = 1
    while i <= n:
        yield i          # pause here, give i to the caller
        i += 1


gen = count_up_to(3)
print(next(gen))         # 1
print(next(gen))         # 2
print(next(gen))         # 3
# print(next(gen))       # StopIteration

# Usually you just loop:
print(list(count_up_to(5)))

print("-" * 50)


# --- Step 2: Why not just return a list? ---------------------
def squares_list(n):
    return [i * i for i in range(n)]     # all in memory at once


def squares_gen(n):
    for i in range(n):
        yield i * i                      # one value at a time


print(squares_list(5))
print(list(squares_gen(5)))
# For range(10_000_000), the generator wins on memory.

print("-" * 50)


# --- Step 3: Generator expressions ---------------------------
# Like a list comprehension, but with () — lazy like a generator.
squares = (n * n for n in range(6))
print(squares)                # <generator object ...>
print(list(squares))          # consume it

# Often used directly in sum/max/any:
print(sum(n * n for n in range(5)))

print("-" * 50)


# --- Step 4: Pipelines (compose generators) ------------------
def numbers(n):
    for i in range(n):
        yield i


def evens(seq):
    for n in seq:
        if n % 2 == 0:
            yield n


def doubled(seq):
    for n in seq:
        yield n * 2


pipeline = doubled(evens(numbers(10)))
print(list(pipeline))   # [0, 4, 8, 12, 16]

print("-" * 50)


# --- Step 5: yield from --------------------------------------
def chain(*iters):
    for it in iters:
        yield from it     # delegate to another iterable/generator


print(list(chain([1, 2], (3, 4), range(5, 7))))


# =============================================================
# TRY IT YOURSELF:
#   1. Write `countdown(n)` that yields n, n-1, ... 1.
#   2. Write a generator expression for only the odd squares of 0..9.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Advanced 2) =====")


def countdown(n):
    while n > 0:
        yield n
        n -= 1


print(list(countdown(5)))
print(list(n * n for n in range(10) if n % 2 == 1))
