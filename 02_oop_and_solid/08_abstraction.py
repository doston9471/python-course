# =============================================================
# LESSON 8: ABSTRACTION  (Pillar #2 of OOP)
# =============================================================
#
# BIG IDEA:
#   Abstraction = expose a SIMPLE interface while hiding the
#   complicated details behind it.
# =============================================================

from abc import ABC, abstractmethod


# --- Step 1: Abstraction in action (a simple facade) --------
class Car:
    def start(self):
        self._check_fuel()
        self._engage_battery()
        self._ignite()
        return "Engine running 🚗"

    def _check_fuel(self):
        pass

    def _engage_battery(self):
        pass

    def _ignite(self):
        pass


print(Car().start())

print("-" * 50)


# --- Step 2: Abstract base classes (ABC) --------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return f"{type(self).__name__} with area {self.area():.2f}"


try:
    Shape()
except TypeError as e:
    print(f"Can't make a bare Shape: {e}")

print("-" * 50)


# --- Step 3: Concrete subclasses fill in the abstract method -
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


for s in [Circle(2), Rectangle(3, 4)]:
    print(s.describe())

print("-" * 50)


# --- Step 4: Abstraction as a STABLE CONTRACT ---------------
class FileStorage:
    def read(self, key):
        return f"reading '{key}' from disk"


class CloudStorage:
    def read(self, key):
        return f"reading '{key}' from the cloud"


class MemoryStorage:
    def read(self, key):
        return f"reading '{key}' from RAM"


class App:
    def __init__(self, storage):
        self._storage = storage

    def load_config(self):
        return self._storage.read("config.yml")


for backend in [FileStorage(), CloudStorage(), MemoryStorage()]:
    print(App(backend).load_config())

print("-" * 50)


print("""ABSTRACTION RECAP
-----------------
- Show a small interface; hide messy details.
- ABC + @abstractmethod: template you subclass but never instantiate.
- Program to an ability, not a concrete class.""")
