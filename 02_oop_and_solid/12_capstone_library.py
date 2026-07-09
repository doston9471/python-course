# =============================================================
# LESSON 12: CAPSTONE — A LIBRARY MANAGEMENT SYSTEM
# =============================================================
#
# This single program ties together EVERYTHING from the course.
# Tags [..] mark concepts in action.
# =============================================================

from abc import ABC, abstractmethod
from functools import total_ordering


# [MODULE/MIXIN] Auto-incrementing IDs for items and members.
class Identifiable:
    _next_id = 0

    def assign_id(self):
        type(self)._next_id += 1
        self.id = type(self)._next_id

    @classmethod
    def next_id_value(cls):
        return cls._next_id


# [ABSTRACTION] Abstract base class with template method.
@total_ordering
class LibraryItem(ABC, Identifiable):
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.checked_out = False
        self.assign_id()

    @abstractmethod
    def kind(self):
        pass

    @abstractmethod
    def loan_days(self):
        pass

    def describe(self):
        status = "OUT" if self.checked_out else "available"
        return (
            f"#{self.id} [{self.kind()}] \"{self.title}\" ({self.year}) "
            f"— {status}, {self.loan_days()}d loan"
        )

    def __lt__(self, other):
        return (self.year, self.title) < (other.year, other.title)

    def __eq__(self, other):
        return (self.year, self.title) == (other.year, other.title)

    def __str__(self):
        return self.describe()


# [INHERITANCE] + [POLYMORPHISM]
class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def kind(self):
        return "Book"

    def loan_days(self):
        return 21

    def describe(self):
        return f"{super().describe()} by {self.author}"


class DVD(LibraryItem):
    def kind(self):
        return "DVD"

    def loan_days(self):
        return 7


class Magazine(LibraryItem):
    def kind(self):
        return "Magazine"

    def loan_days(self):
        return 3


# [COMPOSITION] Swappable fine policy (Strategy pattern).
class StandardFinePolicy:
    RATE_PER_DAY = 0.50

    def fine_for(self, days_late):
        return max(days_late, 0) * self.RATE_PER_DAY


class GenerousFinePolicy:
    def fine_for(self, _days_late):
        return 0.0


# [ENCAPSULATION] Member protects its borrowed list.
class Member(Identifiable):
    def __init__(self, name):
        self.name = name
        self._borrowed = []
        self.assign_id()

    def borrow(self, item):
        self._borrowed.append(item)

    def return_item(self, item):
        self._borrowed.remove(item)

    @property
    def borrowed_count(self):
        return len(self._borrowed)

    def __str__(self):
        return f"Member #{self.id} {self.name} ({self.borrowed_count} items)"


# [COMPOSITION] + [ENUMERABLE via __iter__]
class Library:
    MAX_LOANS = 3

    def __init__(self, name, fine_policy=None):
        self._name = name
        self._catalog = []
        self._members = []
        self._fine_policy = fine_policy or StandardFinePolicy()

    def __iter__(self):
        return iter(self._catalog)

    def add_item(self, item):
        self._catalog.append(item)
        return item

    def register(self, member):
        self._members.append(member)
        return member

    def check_out(self, member, item):
        if item.checked_out:
            raise ValueError("Item is already out")
        if member.borrowed_count >= self.MAX_LOANS:
            raise ValueError(f"{member.name} hit the {self.MAX_LOANS}-item limit")
        item.checked_out = True
        member.borrow(item)
        return f"{member.name} checked out \"{item.title}\""

    def check_in(self, member, item, days_late=0):
        item.checked_out = False
        member.return_item(item)
        fine = self._fine_policy.fine_for(days_late)
        return "Returned, no fine" if fine == 0 else f"Returned, fine ${fine:.2f}"

    def catalog_report(self):
        lines = [f"  {item}" for item in sorted(self._catalog)]
        return f"== {self._name} catalog ==\n" + "\n".join(lines)

    def available(self):
        return [i for i in self if not i.checked_out]

    def by_kind(self, kind):
        return [i for i in self if i.kind() == kind]


# =============================================================
# DEMO
# =============================================================
lib = Library("City Library")

lib.add_item(Book("Ruby Under a Microscope", 2015, "Pat Shaughnessy"))
lib.add_item(Book("The Pragmatic Programmer", 1999, "Hunt & Thomas"))
lib.add_item(DVD("Inception", 2010))
lib.add_item(Magazine("Wired", 2026))

alice = lib.register(Member("Alice"))
bob = lib.register(Member("Bob"))

print(lib.catalog_report())
print("-" * 50)

try:
    LibraryItem("X", 2000)
except TypeError as e:
    print(f"Abstract check: {e}")
print("-" * 50)

book = next(i for i in lib if "Pragmatic" in i.title)
print(lib.check_out(alice, book))
print(f"Available now: {[i.title for i in lib.available()]}")

try:
    lib.check_out(bob, book)
except ValueError as e:
    print(f"Blocked: {e}")
print("-" * 50)

strict = Library("Strict Branch")
kind = Library("Kind Branch", fine_policy=GenerousFinePolicy())
d1 = strict.add_item(DVD("Dune", 2021))
d2 = kind.add_item(DVD("Dune", 2021))
m = strict.register(Member("Carol"))
n = kind.register(Member("Dave"))
strict.check_out(m, d1)
kind.check_out(n, d2)
print(f"Strict branch, 4 days late: {strict.check_in(m, d1, days_late=4)}")
print(f"Kind branch,   4 days late: {kind.check_in(n, d2, days_late=4)}")
print("-" * 50)

print(f"All Books: {[i.title for i in lib.by_kind('Book')]}")
print(f"Total items: {len(list(lib))}")
print(f"Newest item: {max(lib, key=lambda i: i.year).title}")
print("-" * 50)

print("""🎓 CONGRATULATIONS — you've completed OOP in Python!

  Next: SOLID principles in lessons 13–18.""")

# =============================================================
# ✅ SOLUTION / FINAL CHALLENGE
# =============================================================
print("\n===== SOLUTION (Lesson 12) =====")


class AudioBook(LibraryItem):
    def __init__(self, title, year, narrator):
        super().__init__(title, year)
        self.narrator = narrator

    def kind(self):
        return "AudioBook"

    def loan_days(self):
        return 14

    def describe(self):
        return f"{super().describe()} narrated by {self.narrator}"


class MemberWithFines(Member):
    def __init__(self, name):
        super().__init__(name)
        self._fines = []

    def add_fine(self, amount):
        self._fines.append(amount)

    @property
    def total_fines(self):
        return sum(self._fines)


class LibraryWithOverdue(Library):
    def overdue_report(self, overdue_items):
        if not overdue_items:
            return "No overdue items"
        return "Overdue:\n" + "\n".join(f"  {i.title}" for i in overdue_items)


branch = LibraryWithOverdue("Branch")
ab = branch.add_item(AudioBook("Dune (audio)", 2021, "Scott Brick"))
print(ab.describe())

eve = MemberWithFines("Eve")
eve.add_fine(1.50)
eve.add_fine(0.75)
print(f"{eve.name} total fines: ${eve.total_fines:.2f}")
print(branch.overdue_report([ab]))
