# =============================================================
# LESSON 15: SOLID — L = LISKOV SUBSTITUTION PRINCIPLE (LSP)
# =============================================================


# --- Step 1: The classic VIOLATION (Rectangle/Square) -------
class Rectangle:
    def __init__(self, w, h):
        self.width, self.height = w, h

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = self._height = w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._width = self._height = h


def resize_and_check(rect):
    rect.width = 5
    rect.height = 4
    expected = 20
    got = rect.area()
    ok = "OK" if got == expected else "!! LSP VIOLATION"
    return f"expected {expected}, got {got}  {ok}"


print(f"Rectangle: {resize_and_check(Rectangle(1, 1))}")
print(f"Square:    {resize_and_check(Square(1))}")

print("-" * 50)


# --- Step 2: The FIX — model the real abstraction -----------
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rect(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


class Square2(Shape):
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size * self.size


for s in [Rect(5, 4), Square2(3)]:
    print(f"{type(s).__name__}: area={s.area()}")

print("-" * 50)


# --- Step 3: Another VIOLATION — throwing in a subclass -----
class Bird:
    def fly(self):
        return "flying high"


class Penguin(Bird):
    def fly(self):
        raise RuntimeError("penguins can't fly!")


def make_it_fly(bird):
    try:
        return bird.fly()
    except Exception as e:
        return f"CRASH: {e}  (LSP violation)"


print(f"Sparrow: {make_it_fly(Bird())}")
print(f"Penguin: {make_it_fly(Penguin())}")

print("-" * 50)


# --- Step 4: Split the hierarchy by capability --------------
class Flyable:
    def fly(self):
        return f"{self.name} is flying"


class Bird2:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"


class Sparrow(Bird2, Flyable):
    pass


class Penguin2(Bird2):
    def swim(self):
        return f"{self.name} is swimming"


for b in [Sparrow("Jack"), Penguin2("Pingu")]:
    print(b.eat())
    print(b.fly() if hasattr(b, "fly") else f"  ({b.name} doesn't fly)")

print("-" * 50)


print("""LSP RECAP
---------
Subtypes must be substitutable for their base types without surprises.""")
