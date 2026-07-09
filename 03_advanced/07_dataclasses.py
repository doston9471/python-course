# =============================================================
# ADVANCED 7: DATACLASSES
# =============================================================
#
# BIG IDEA:
#   @dataclass auto-generates __init__, __repr__, __eq__, and more
#   for classes that mainly hold data. Less boilerplate than a
#   hand-written class — perfect after you know OOP.
# =============================================================

from dataclasses import dataclass, field, asdict, replace
from typing import ClassVar


# --- Step 1: The boring class vs dataclass -------------------
class PointManual:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PointManual(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return isinstance(other, PointManual) and self.x == other.x and self.y == other.y


@dataclass
class Point:
    x: float
    y: float


print(Point(1, 2))
print(Point(1, 2) == Point(1, 2))

print("-" * 50)


# --- Step 2: Defaults & default_factory ----------------------
@dataclass
class User:
    name: str
    active: bool = True
    tags: list[str] = field(default_factory=list)  # NOT = []  (mutable trap!)


u1 = User("Ada")
u2 = User("Grace", tags=["admin"])
u1.tags.append("reader")
print(u1)
print(u2)   # Grace's tags untouched — separate lists

print("-" * 50)


# --- Step 3: frozen / immutable data ------------------------
@dataclass(frozen=True)
class Money:
    cents: int
    currency: str = "USD"


price = Money(999)
print(price)
# price.cents = 10   # FrozenInstanceError

print("-" * 50)


# --- Step 4: Methods still work ------------------------------
@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height


print(Rectangle(3, 4).area())

print("-" * 50)


# --- Step 5: asdict, replace, ClassVar -----------------------
@dataclass
class Config:
    DEFAULT_HOST: ClassVar[str] = "localhost"  # not a field
    host: str = "localhost"
    port: int = 8000


cfg = Config(port=9000)
print(asdict(cfg))
cfg2 = replace(cfg, host="0.0.0.0")
print(cfg2)
print(Config.DEFAULT_HOST)

print("-" * 50)


# --- Step 6: order=True for sorting --------------------------
@dataclass(order=True)
class Version:
    major: int
    minor: int


versions = [Version(2, 0), Version(1, 5), Version(1, 2)]
print(sorted(versions))


# =============================================================
# TRY IT YOURSELF:
#   1. Make a frozen `@dataclass` Book(title, author, pages).
#   2. Create two equal books and prove == works.
#   3. Convert one to a dict with asdict.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Advanced 7) =====")


@dataclass(frozen=True)
class Book:
    title: str
    author: str
    pages: int


a = Book("Dune", "Herbert", 412)
b = Book("Dune", "Herbert", 412)
print(a == b)
print(asdict(a))
