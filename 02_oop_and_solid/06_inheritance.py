# =============================================================
# LESSON 6: INHERITANCE  (Pillar #3 of OOP)
# =============================================================
#
# BIG IDEA:
#   Inheritance lets a new class REUSE and SPECIALIZE an existing
#   class. The subclass automatically gets the parent's methods and
#   can add to or change them.
#
#   It models an "IS-A" relationship:
#     a Dog IS-A Animal, a Car IS-A Vehicle, a Manager IS-A Employee.
#
#   Syntax:  class Child(Parent):
# =============================================================


# --- Step 1: Basic inheritance ------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f"{self.name} is breathing"

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    pass


d = Dog("Rex")
print(d.breathe())
print(d.speak())
print(f"Dog bases: {Dog.__bases__}")

print("-" * 50)


# --- Step 2: Overriding a method ----------------------------
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"


print(Cat("Felix").speak())
print(Cat("Felix").breathe())

print("-" * 50)


# --- Step 3: super() — call the parent's version ------------
class Bird(Animal):
    def speak(self):
        base = super().speak()
        return f"{base}, specifically a tweet"


print(Bird("Robin").speak())

print("-" * 50)


# --- Step 4: super() in __init__ (extending state) ----------
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
        self.speed = 0

    def describe(self):
        return f"{self.wheels}-wheeled vehicle"


class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(4)
        self.brand = brand

    def describe(self):
        return f"{super().describe()} — a {self.brand}"


car = Car("Toyota")
print(car.describe())
print(f"Wheels: {car.wheels}")

print("-" * 50)


# --- Step 5: super() with explicit arguments ----------------
class Base:
    def greet(self, name):
        return f"Hello, {name}"


class Loud(Base):
    def greet(self, name):
        return super().greet(name).upper()


class Quiet(Base):
    def greet(self, name):
        return super().greet("friend")


print(Loud().greet("ada"))
print(Quiet().greet("ada"))

print("-" * 50)


# --- Step 6: Method Resolution Order (MRO) ------------------
print(f"Cat MRO: {[c.__name__ for c in Cat.mro()]}")

felix = Cat("Felix")
print("isinstance checks the whole chain:")
print(f"  isinstance(felix, Cat)?    {isinstance(felix, Cat)}")
print(f"  isinstance(felix, Animal)? {isinstance(felix, Animal)}")
print(f"  isinstance(felix, object)? {isinstance(felix, object)}")

print("-" * 50)


print("""USE INHERITANCE ONLY FOR TRUE "IS-A" RELATIONSHIPS.
  Good: Dog(Animal), SavingsAccount(Account).
  Bad : Car(Engine) — a car HAS an engine, it is NOT an engine.
  For "HAS-A" relationships, use COMPOSITION instead (Lesson 10).""")
