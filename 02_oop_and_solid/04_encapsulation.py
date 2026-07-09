# =============================================================
# LESSON 4: ENCAPSULATION (public / private / protected)
# =============================================================
#
# BIG IDEA (Pillar #1 of OOP):
#   Encapsulation = bundle data + behavior together, and HIDE the
#   internal details behind a controlled "public interface".
#
#   Python uses NAMING CONVENTIONS (not strict keywords like Ruby):
#     name      -> public
#     _name     -> "protected" / internal (convention)
#     __name    -> name-mangled (harder to access from outside)
# =============================================================


# --- Step 1: private helpers with a single underscore --------
class CoffeeMachine:
    def __init__(self, beans):
        self._beans = beans

    def brew(self):
        if self._enough_beans():
            self._grind()
            self._beans -= 7
            return f"Here is your coffee ☕ ({self._beans}g beans left)"
        return "Not enough beans!"

    def _enough_beans(self):
        return self._beans >= 7

    def _grind(self):
        return "grinding..."


machine = CoffeeMachine(20)
print(machine.brew())
print(machine.brew())
print(machine.brew())

# Convention says don't call _grind from outside, but Python won't stop you:
print(f"(You *can* call _grind: {machine._grind()!r} — but you shouldn't)")

print("-" * 50)


# --- Step 2: private protects INVARIANTS ---------------------
class SafeAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._validate(amount)
        self._balance += amount
        return self

    def withdraw(self, amount):
        self._validate(amount)
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self

    def _validate(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")


a = SafeAccount()
a.deposit(100).withdraw(30)
print(f"Balance: {a.balance}")
try:
    a.deposit(-5)
except ValueError as e:
    print(f"Rejected: {e}")

print("-" * 50)


# --- Step 3: "protected" — comparing two objects --------------
class Money:
    def __init__(self, cents):
        self._cents = cents

    def __gt__(self, other):
        return self._cents > other._cents

    def __str__(self):
        return f"${self._cents / 100:.2f}"


wallet = Money(1500)
price = Money(999)
print(f"{wallet} > {price}? {wallet > price}")
# _cents is "internal" — callers should use the public interface.

print("-" * 50)


# --- Step 4: name mangling with double underscore ------------
class Vault:
    def __init__(self, secret):
        self.__secret = secret   # becomes _Vault__secret

    def reveal(self):
        return self.__secret


v = Vault("top-secret")
print(v.reveal())
# print(v.__secret)  # AttributeError — mangled name hides it

print("-" * 50)


print("""VISIBILITY CHEAT SHEET
----------------------
public    : normal names. Your object's official API.
_single_  : internal by convention; still accessible.
__double_ : name-mangled inside the class hierarchy.

Rule of thumb: expose a small public API; keep helpers private.""")
