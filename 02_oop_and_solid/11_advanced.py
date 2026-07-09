# =============================================================
# LESSON 11: ADVANCED PYTHON OOP
#   __str__, operators, ordering, iteration, __getattr__
# =============================================================

from functools import total_ordering


# --- Step 1: __str__ and __repr__ ---------------------------
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


pt = Point(1, 2)
print(pt)
print(repr(pt))
print([pt, pt])

print("-" * 50)


# --- Step 2: Operator overloading ---------------------------
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


a = Vector(1, 2)
b = Vector(3, 4)
print(f"a + b = {a + b}")
print(f"b - a = {b - a}")
print(f"a * 3 = {a * 3}")
print(f"a == Vector(1,2)? {a == Vector(1, 2)}")

print("-" * 50)


# --- Step 3: __getitem__ and __setitem__ --------------------
class Grid:
    def __init__(self):
        self._cells = {}

    def __getitem__(self, key):
        row, col = key
        return self._cells.get((row, col), ".")

    def __setitem__(self, key, value):
        row, col = key
        self._cells[(row, col)] = value


g = Grid()
g[0, 0] = "X"
g[1, 2] = "O"
print(f"g[0,0] = {g[0, 0]}")
print(f"g[5,5] = {g[5, 5]}")

print("-" * 50)


# --- Step 4: __lt__ and @total_ordering ---------------------
@total_ordering
class Version:
    def __init__(self, text):
        self.major, self.minor = map(int, text.split("."))

    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)

    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)

    def __str__(self):
        return f"{self.major}.{self.minor}"


v1 = Version("1.4")
v2 = Version("2.0")
print(f"v1 < v2? {v1 < v2}")
print(f"v1 > v2? {v1 > v2}")
versions = [Version("2.1"), Version("1.0"), Version("1.5")]
print(f"sorted: {', '.join(str(v) for v in sorted(versions))}")

print("-" * 50)


# --- Step 5: __iter__ makes your class iterable -------------
class Playlist:
    def __init__(self):
        self._songs = []

    def add(self, song):
        self._songs.append(song)
        return self

    def __iter__(self):
        return iter(self._songs)


pl = Playlist()
pl.add("Song A (3)").add("Song B (5)").add("Song C (2)")
print(f"map:    {[s.upper() for s in pl]}")
print(f"select: {[s for s in pl if 'B' in s]}")
print(f"count:  {len(list(pl))}")
print(f"first:  {next(iter(pl))}")
print(f"sorted: {sorted(pl)}")

print("-" * 50)


# --- Step 6: __hash__ (using objects as dict keys) ----------
class Coord:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return isinstance(other, Coord) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


scores = {Coord(1, 1): "treasure"}
print(f"Lookup with equal Coord: {scores[Coord(1, 1)]}")

print("-" * 50)


# --- Step 7: frozen dataclass-style immutability (concept) ---
# tuple is immutable; for custom classes use @dataclass(frozen=True)
config = {"host": "localhost"}
try:
  # dict itself is mutable; immutability is a design choice
    pass
except Exception:
    pass

print("-" * 50)


# --- Step 8: __getattr__ (dynamic attributes) ---------------
class FlexibleConfig:
    def __init__(self):
        self._data = {}

    def __setattr__(self, name, value):
        if name == "_data":
            super().__setattr__(name, value)
        else:
            self._data[name] = value

    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        raise AttributeError(name)


cfg = FlexibleConfig()
cfg.timeout = 30
cfg.host = "localhost"
print(f"timeout = {cfg.timeout}")
print(f"host    = {cfg.host}")

print("-" * 50)


print("""ADVANCED RECAP
--------------
__str__ / __repr__ : friendly vs debug representations.
__add__, __eq__, etc.: operators are special methods.
__lt__ + @total_ordering: comparisons and sorting.
__iter__: make objects work in for-loops and comprehensions.
__hash__ + __eq__: valid dict/set keys.
__getattr__: intercept missing attribute access.""")
