# =============================================================
# LESSON 7: POLYMORPHISM & DUCK TYPING  (Pillar #4 of OOP)
# =============================================================
#
# BIG IDEA:
#   "Polymorphism" = "many forms". The SAME message (method call)
#   can produce DIFFERENT behavior depending on the object that
#   receives it.
# =============================================================


# --- Step 1: Polymorphism via inheritance -------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("subclass must define speak")


class Dog(Animal):
    def speak(self):
        return f"{self.name}: Woof"


class Cat(Animal):
    def speak(self):
        return f"{self.name}: Meow"


class Cow(Animal):
    def speak(self):
        return f"{self.name}: Moo"


animals = [Dog("Rex"), Cat("Felix"), Cow("Bessie")]
for a in animals:
    print(a.speak())

print("-" * 50)


# --- Step 2: Why this beats if/else type checking -----------
class Sheep(Animal):
    def speak(self):
        return f"{self.name}: Baa"


print(Sheep("Dolly").speak())

print("-" * 50)


# --- Step 3: DUCK TYPING ------------------------------------
class Invoice:
    def to_pdf(self):
        return "[PDF of an invoice]"


class Report:
    def to_pdf(self):
        return "[PDF of a report]"


class Photo:
    def to_pdf(self):
        return "[PDF of a photo]"


def print_document(doc):
    print(f"Printing: {doc.to_pdf()}")


for doc in [Invoice(), Report(), Photo()]:
    print_document(doc)

print("-" * 50)


# --- Step 4: Polymorphism you already use every day ---------
print("String +: " + ("foo" + "bar"))
print(f"List  +: {[1, 2] + [3, 4]}")
print(f"Int   +: {2 + 3}")

for x in [1, 2]:
    print(x, end=" ")
print()
for k, v in {"a": 1, "b": 2}.items():
    print(f"{k}={v}", end=" ")
print()

print("-" * 50)


# --- Step 5: Defensive duck typing with hasattr -------------
class Robot:
    def to_pdf(self):
        return "[PDF of robot specs]"


class Rock:
    pass


def safe_print(doc):
    if hasattr(doc, "to_pdf"):
        print(f"OK: {doc.to_pdf()}")
    else:
        print(f"Skipping {type(doc).__name__}: can't be turned into a PDF")


safe_print(Robot())
safe_print(Rock())

print("-" * 50)


print("""POLYMORPHISM MENTAL MODEL
-------------------------
- Caller sends a MESSAGE ("speak", "to_pdf", "+").
- Each object decides HOW to respond.
- In Python: inheritance OR duck typing (capability matters, not class).""")
