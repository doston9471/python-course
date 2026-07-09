# =============================================================
# LESSON 10: COMPOSITION vs INHERITANCE
# =============================================================
#
# BIG IDEA:
#   INHERITANCE ("IS-A"): a Car IS-A Vehicle.
#   COMPOSITION ("HAS-A"): a Car HAS-A Engine.
#
#   "Favor composition over inheritance."
# =============================================================


# --- Step 1: The trap of inheritance for reuse --------------
class Engine:
    def start(self):
        return "Engine starting (vroom)"

    def stop(self):
        return "Engine stopping"


class WrongCar(Engine):
    pass


print(f"WrongCar (bad design): {WrongCar().start()}")

print("-" * 50)


# --- Step 2: Composition — Car HAS-A Engine -----------------
class Car:
    def __init__(self):
        self._engine = Engine()

    def start(self):
        return f"Car ready. {self._engine.start()}"


print(Car().start())

print("-" * 50)


# --- Step 3: Swap parts easily ------------------------------
class ElectricEngine:
    def start(self):
        return "Electric motor humming (silent)"


class V8Engine:
    def start(self):
        return "V8 ROARING"


class FlexCar:
    def __init__(self, engine):
        self._engine = engine

    def start(self):
        return f"FlexCar: {self._engine.start()}"


print(FlexCar(ElectricEngine()).start())
print(FlexCar(V8Engine()).start())

print("-" * 50)


# --- Step 4: Build rich objects from many parts -------------
class Wheels:
    def roll(self):
        return "wheels rolling"


class GPS:
    def navigate(self, destination):
        return f"routing to {destination}"


class SmartCar:
    def __init__(self):
        self._engine = ElectricEngine()
        self._wheels = Wheels()
        self._gps = GPS()

    def drive(self, destination):
        return " | ".join([
            self._engine.start(),
            self._wheels.roll(),
            self._gps.navigate(destination),
        ])


print(SmartCar().drive("Airport"))

print("-" * 50)


# --- Step 5: Strategy pattern (swap behavior at runtime) ----
class Card:
    def pay(self, amount):
        return f"Paid ${amount} by credit card"


class Crypto:
    def pay(self, amount):
        return f"Paid ${amount} in crypto"


class Checkout:
    def __init__(self, payment):
        self.payment = payment

    def complete(self, amount):
        return self.payment.pay(amount)


co = Checkout(Card())
print(co.complete(50))
co.payment = Crypto()
print(co.complete(50))

print("-" * 50)


print("""CHOOSING: INHERITANCE vs COMPOSITION
------------------------------------
IS-A  -> inheritance MAY fit.
HAS-A -> composition.

Prefer COMPOSITION when you want to swap parts at runtime.""")
