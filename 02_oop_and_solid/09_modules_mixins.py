# =============================================================
# LESSON 9: MIXINS & MULTIPLE INHERITANCE
# =============================================================
#
# BIG IDEA:
#   Python supports multiple inheritance. A MIXIN is a small class
#   that adds reusable behavior without being a full "is-a" parent.
#
#   Mixins serve two jobs:
#     1. SHARE behavior across unrelated classes
#     2. NAMESPACES — group related classes under a package/module
# =============================================================


# --- Step 1: Mixins add instance methods ----------------------
class Walkable:
    def walk(self):
        return f"{self.name} is walking"


class Swimmable:
    def swim(self):
        return f"{self.name} is swimming"


class Person(Walkable):
    def __init__(self, name):
        self.name = name


class Duck(Walkable, Swimmable):
    def __init__(self, name):
        self.name = name


print(Person("Ada").walk())
print(Duck("Donald").walk())
print(Duck("Donald").swim())

print("-" * 50)


# --- Step 2: MRO (Method Resolution Order) ------------------
print(f"Duck MRO: {[c.__name__ for c in Duck.mro()]}")

print("-" * 50)


# --- Step 3: Class methods via mixin + @classmethod -----------
class Findable:
    @classmethod
    def find(cls, record_id):
        return f"Looking up record #{record_id}"


class Product(Findable):
    pass


print(Product.find(42))

print("-" * 50)


# --- Step 4: prepend-like wrapping with super() --------------
class Logged:
    def save(self):
        print("  [log] about to save...")
        result = super().save()
        print("  [log] done saving")
        return result


class Document(Logged):
    def save(self):
        return "saved!"


print(Document().save())

print("-" * 50)


# --- Step 5: namespaces with packages/modules ---------------
# In real projects you'd use separate files:
#   geometry/circle.py  -> geometry.Circle
#   networking/circle.py -> networking.Circle
#
# Here we simulate with nested classes:

class Geometry:
    PI = 3.14159

    class Circle:
        def __init__(self, r):
            self.r = r

        def area(self):
            return Geometry.PI * self.r ** 2


class Networking:
    class Circle:
        def describe(self):
            return "a network ring topology"


print(f"Geometry.Circle area: {Geometry.Circle(2).area():.2f}")
print(f"Networking.Circle:    {Networking.Circle().describe()}")

print("-" * 50)


# --- Step 6: module-level utility functions -----------------
def double(n):
    return n * 2


def triple(n):
    return n * 3


print(f"double(10) = {double(10)}")
print(f"triple(10) = {triple(10)}")

print("-" * 50)


print("""MIXIN CHEAT SHEET
-----------------
class Child(MixinA, MixinB, Parent):  # mixins listed before parent
super() in a mixin can wrap the next class in the MRO.
Use mixins for shared behavior WITHOUT deep inheritance trees.""")
