# =============================================================
# LESSON 2: STATE (instance attributes, __init__, @property)
# =============================================================
#
# BIG IDEA:
#   In Lesson 1 our objects could DO things but couldn't REMEMBER
#   anything. State is the data an object carries with it.
#
#   Each object gets its OWN copy of its state, stored in
#   instance attributes — typically self.name, self.age, etc.
# =============================================================


# --- Step 1: Why we need state ------------------------------
class DogV1:
    def speak(self):
        return "Woof"


# We can't tell two DogV1 objects apart. Let's fix that.
print("-" * 50)


# --- Step 2: __init__ — the constructor -----------------------
# __init__ is a SPECIAL method Python calls automatically when
# you create an instance. Whatever you pass to Dog(...) comes here.
class Dog:
    def __init__(self, name, age):
        self.name = name   # instance attribute: belongs to THIS dog
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"


rex = Dog("Rex", 3)
fido = Dog("Fido", 7)

print(rex.describe())    # => Rex is 3 years old
print(fido.describe())   # => Fido is 7 years old
# Each object remembers its OWN name and age.

print("-" * 50)


# --- Step 3: Attributes are public by default -----------------
# Unlike Ruby's @vars, Python attributes are reachable from outside
# unless you deliberately hide them (Lesson 4).
#
#   print(rex.name)   # works — but often we want controlled access
#
# For controlled access, use @property (getters/setters).

print("-" * 50)


# --- Step 4: Manual getters and setters -----------------------
class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount


acct = Account(100)
print(f"balance: {acct.balance}")   # getter
acct.balance = 250                   # setter
print(f"balance: {acct.balance}")

print("-" * 50)


# --- Step 5: @property for read-only and read-write -----------
#   @property           -> getter only (read)
#   @x.setter           -> adds a setter (read/write)
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self._id = person_id

    @property
    def id(self):
        return self._id


p1 = Person("Ada", 1001)
print(f"name: {p1.name}")
p1.name = "Ada Lovelace"
print(f"name: {p1.name}")
print(f"id:   {p1.id}")
# p1.id = 2   # would ERROR: no setter defined

print("-" * 50)


# --- Step 6: Proof that state is per-object -----------------
people = [
    Person("Grace", 1),
    Person("Alan", 2),
    Person("Edsger", 3),
]
for person in people:
    print(f"{person.id} => {person.name}")


# =============================================================
# TRY IT YOURSELF:
#   1. Make a class `Book` with `title`, `author`, and `pages`.
#   2. Use read-only @property for title/author, read-write for pages.
#   3. Create a book, print a summary, then change its pages and
#      print again.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Lesson 2) =====")


class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self.pages = pages

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    def summary(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"


book = Book("The Hobbit", "Tolkien", 310)
print(book.summary())
book.pages = 320
print(book.summary())
# book.title = "X"   # would error: title has no setter
