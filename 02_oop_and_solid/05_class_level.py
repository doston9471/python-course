# =============================================================
# LESSON 5: CLASS-LEVEL FEATURES
#   (class methods, class variables, constants)
# =============================================================
#
# BIG IDEA:
#   So far everything belonged to INSTANCES (individual objects).
#   But the CLASS ITSELF can have its own methods and data.
#
#   Two different "levels":
#     - INSTANCE level: unique to each object (self.name)
#     - CLASS level:    shared by all instances, or on the blueprint
# =============================================================


# --- Step 1: @classmethod ------------------------------------
class MathUtils:
    @classmethod
    def square(cls, n):
        return n * n

    @classmethod
    def cube(cls, n):
        return n ** 3


print(f"square(5) = {MathUtils.square(5)}")
print(f"cube(3)   = {MathUtils.cube(3)}")

print("-" * 50)


# --- Step 2: Factory methods (alternative constructors) -------
class Date2:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def new_years_day(cls, year):
        return cls(year, 1, 1)

    @classmethod
    def from_string(cls, text):
        y, m, d = map(int, text.split("-"))
        return cls(y, m, d)

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


print(f"Factory 1: {Date2.new_years_day(2026)}")
print(f"Factory 2: {Date2.from_string('2026-06-26')}")

print("-" * 50)


# --- Step 3: Class variables shared across instances ----------
class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def total(cls):
        return cls.count


User("Ann")
User("Bob")
User("Cy")
print(f"Total users created: {User.total()}")

print("-" * 50)


# --- Step 4: Class-level counter via class variable -----------
class Widget:
    _count = 0

    @classmethod
    @property
    def count(cls):
        return cls._count

    def __init__(self):
        type(self)._count += 1


Widget()
Widget()
print(f"Widgets: {Widget._count}")

print("-" * 50)


# --- Step 5: Constants ----------------------------------------
class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2


c = Circle(2)
print(f"Area: {c.area()}")
print(f"Access constant from outside: Circle.PI = {Circle.PI}")

print("-" * 50)


# --- Step 6: Putting levels side by side ----------------------
class Counter:
    _all = []

    def __init__(self, name):
        self.name = name
        self.value = 0
        Counter._all.append(self)

    def tick(self):
        self.value += 1
        return self

    @classmethod
    def report(cls):
        return ", ".join(f"{c.name}={c.value}" for c in cls._all)


a = Counter("a")
b = Counter("b")
a.tick().tick()
b.tick()
print(f"Report -> {Counter.report()}")
