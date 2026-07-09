# =============================================================
# LESSON 3: BEHAVIOR & SELF
# =============================================================
#
# BIG IDEA:
#   State (Lesson 2) is what an object KNOWS.
#   Behavior is what an object DOES with that knowledge.
#   Good methods combine state + logic to answer questions and
#   change the world in controlled ways.
#
#   `self` is the first parameter of every instance method — it
#   refers to "the current object". Understanding self unlocks Python OOP.
# =============================================================


# --- Step 1: Methods that USE state to decide ---------------
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount
        return self

    def withdraw(self, amount):
        if amount > self._balance:
            print("  Declined: insufficient funds")
            return self
        self._balance -= amount
        return self

    def is_overdrawn(self):
        return self._balance < 0


acct = BankAccount(100)
acct.deposit(50)
acct.withdraw(30)
print(f"Balance: {acct.balance}")
print(f"Overdrawn? {acct.is_overdrawn()}")

print("-" * 50)


# --- Step 2: What is `self`? --------------------------------
class Probe:
    def show_self(self):
        return f"self is a {type(self)}, id={id(self)}"


pr = Probe()
print(pr.show_self())
print(f"pr id = {id(pr)}   (matches the one above)")

print("-" * 50)


# --- Step 3: Calling other methods on self --------------------
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.full_intro()}"

    def full_intro(self):
        return f"{self.name} the Great"


print(Greeter("Zog").greet())

print("-" * 50)


# --- Step 4: Returning self for method chaining -------------
acct2 = BankAccount(0)
acct2.deposit(100).deposit(50).withdraw(30)
print(f"Chained balance: {acct2.balance}")

print("-" * 50)


# --- Step 5: self is REQUIRED for setters ---------------------
# Writing `celsius = 5` inside a method creates a LOCAL variable.
# To call your own setter you MUST write self.celsius = 5.
class Temperature:
    def __init__(self, c):
        self.celsius = c

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    def heat_up_broken(self, by):
        celsius = self._celsius + by   # BUG: local var; @celsius unchanged

    def heat_up_correct(self, by):
        self.celsius = self.celsius + by


t = Temperature(20)
t.heat_up_broken(100)
print(f"After broken heat_up:  {t.celsius}  (still 20 — the bug!)")
t.heat_up_correct(5)
print(f"After correct heat_up: {t.celsius}  (now 25)")

print("-" * 50)


# --- Step 6: Naming conventions for methods -----------------
class Word:
    def __init__(self, text):
        self._text = text

    @property
    def text(self):
        return self._text

    def is_empty(self):
        return not self._text.strip()

    def shout(self):
        return self._text.upper()

    def shout_inplace(self):
        self._text = self._text.upper()
        return self


w = Word("hello")
print(f"empty? {w.is_empty()}")
print(f"shout (non-mutating): {w.shout()}, original still: {w.text}")
w.shout_inplace()
print(f"after shout_inplace: {w.text}")


# =============================================================
# TRY IT YOURSELF:
#   1. Build a `Counter` with count starting at 0.
#   2. Methods: increment, decrement, reset (return self), is_zero().
#   3. Chain: c.increment().increment().increment().decrement()
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Lesson 3) =====")


class Counter:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def increment(self):
        self._count += 1
        return self

    def decrement(self):
        self._count -= 1
        return self

    def reset(self):
        self._count = 0
        return self

    def is_zero(self):
        return self._count == 0


c = Counter()
c.increment().increment().increment().decrement()
print(f"count = {c.count}")
print(f"zero? {c.is_zero()}")
print(f"after reset zero? {c.reset().is_zero()}")
