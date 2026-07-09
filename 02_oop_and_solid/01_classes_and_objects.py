# =============================================================
# LESSON 1: CLASSES & OBJECTS
# =============================================================
#
# BIG IDEA:
#   Object-Oriented Programming (OOP) is a way of organizing code
#   around "objects" — little bundles that combine:
#     - DATA (what they know / their state)
#     - BEHAVIOR (what they can do / their methods)
#
#   A CLASS is the blueprint. An OBJECT (or "instance") is a real
#   thing built from that blueprint.
#
#   Analogy: "Dog" is a class (the concept). Your specific dog
#   "Rex" is an object (one real instance of that concept).
# =============================================================


# --- Step 1: The simplest possible class ---------------------
class Dog:
    pass


# Create objects (instances) from the class
rex = Dog()
fido = Dog()

print(f"rex is a: {type(rex)}")        # => <class '__main__.Dog'>
print(f"fido is a: {type(fido)}")

# Even though both are Dogs, they are DIFFERENT objects.
# id() is a unique number Python gives every object.
print(f"rex id:  {id(rex)}")
print(f"fido id: {id(fido)}")
print(f"same object? {rex is fido}")   # => False

print("-" * 50)


# --- Step 2: Giving the class some behavior (a method) -------
class Cat:
    def speak(self):
        return "Meow!"


whiskers = Cat()
print(f"The cat says: {whiskers.speak()}")

print("-" * 50)


# --- Step 3: "Everything is an object" in Python -------------
# Numbers, strings, even classes themselves are objects.
print(f"42 is a {type(42)}")             # => <class 'int'>
print(f"3.14 is a {type(3.14)}")         # => <class 'float'>
print(f"'hi' is a {type('hi')}")         # => <class 'str'>
print(f"True is a {type(True)}")         # => <class 'bool'>
print(f"None is a {type(None)}")         # => <class 'NoneType'>
print(f"[] is a {type([])}")             # => <class 'list'>
print(f"Dog (the class) is a {type(Dog)}")  # => <class 'type'>

print("-" * 50)


# --- Step 4: Sending "messages" to objects ------------------
# In OOP we say we "send a message" to an object by calling a
# method on it with the dot. The object decides how to respond.
print("hello".upper())        # the str object responds to .upper()
print(sorted([3, 1, 2]))
print(list(range(10)))

# You can even ask an object what it can do:
print(f"Does a Cat respond to speak? {hasattr(whiskers, 'speak')}")
print(f"Does a Cat respond to fly?   {hasattr(whiskers, 'fly')}")


# =============================================================
# TRY IT YOURSELF:
#   1. Make a class `Car` with a method `honk` that returns "Beep!".
#   2. Create two Car objects and call honk on each.
#   3. Print the class of each car.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Lesson 1) =====")


class Car:
    def honk(self):
        return "Beep!"


car1 = Car()
car2 = Car()
print(car1.honk())
print(car2.honk())
print(f"car1 is a {type(car1)}, car2 is a {type(car2)}")
