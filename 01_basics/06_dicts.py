# =============================================================
# BASICS 6: DICTS (hashes / maps)
# =============================================================
#
# BIG IDEA:
#   A dict maps keys -> values. Think Ruby Hash / JS Object.
#   Keys must be immutable (usually strings or numbers).
# =============================================================


# --- Step 1: Creating dicts ----------------------------------
empty = {}
person = {
    "name": "Ada",
    "age": 36,
    "languages": ["Python", "Math"],
}
print(person)

# dict() constructor:
point = dict(x=1, y=2)
print(point)

print("-" * 50)


# --- Step 2: Accessing & updating ----------------------------
print(person["name"])            # Ada
# print(person["city"])          # KeyError if missing!

print(person.get("city"))        # None (safe)
print(person.get("city", "N/A")) # default if missing

person["age"] = 37               # update
person["city"] = "London"        # add new key
print(person)

del person["city"]               # remove key
print(person)

print("-" * 50)


# --- Step 3: Keys, values, items -----------------------------
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))

print("-" * 50)


# --- Step 4: Iterating ----------------------------------------
for key in person:
    print(f"  {key} => {person[key]}")

print("---")
for key, value in person.items():
    print(f"  {key} => {value}")

print("-" * 50)


# --- Step 5: Nested dicts ------------------------------------
users = {
    "u1": {"name": "Ann", "score": 10},
    "u2": {"name": "Bob", "score": 20},
}
print(users["u2"]["name"])
users["u1"]["score"] += 5
print(users)

print("-" * 50)


# --- Step 6: Useful methods ----------------------------------
config = {"host": "localhost", "port": 5432}
print("host" in config)                 # True
config.update({"port": 3306, "ssl": True})
print(config)
print(config.pop("ssl"))                # remove & return
print(len(config))


# =============================================================
# TRY IT YOURSELF:
#   1. Make a dict for a book: title, author, pages, tags (list).
#   2. Add a "year" key, print author, and loop over items.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Basics 6) =====")
book = {
    "title": "The Hobbit",
    "author": "Tolkien",
    "pages": 310,
    "tags": ["fantasy", "classic"],
}
book["year"] = 1937
print(book["author"])
for k, v in book.items():
    print(f"  {k}: {v}")
