# =============================================================
# LESSON 16: SOLID — I = INTERFACE SEGREGATION PRINCIPLE (ISP)
# =============================================================


# --- Step 1: The VIOLATION (a fat interface) ----------------
class FatWorker:
    def work(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError

    def sleep(self):
        raise NotImplementedError


class Human(FatWorker):
    def work(self):
        return "human working"

    def eat(self):
        return "human eating"

    def sleep(self):
        return "human sleeping"


class Robot(FatWorker):
    def work(self):
        return "robot working"

    def eat(self):
        raise RuntimeError("robots don't eat")

    def sleep(self):
        raise RuntimeError("robots don't sleep")


print("--- Fat interface (violates ISP) ---")
print(Human().work())
print(Robot().work())
try:
    Robot().eat()
except RuntimeError as e:
    print(f"Robot forced to implement eat: {e}")

print("-" * 50)


# --- Step 2: The FIX — split into small role interfaces -----
class Workable:
    def work(self):
        return f"{self.name}: working"


class Eater:
    def eat(self):
        return f"{self.name}: eating"


class Sleeper:
    def sleep(self):
        return f"{self.name}: sleeping"


class HumanWorker(Workable, Eater, Sleeper):
    def __init__(self, name):
        self.name = name


class RobotWorker(Workable):
    def __init__(self, name):
        self.name = name


alice = HumanWorker("Alice")
r2d2 = RobotWorker("R2D2")
print("--- Segregated roles (ISP-compliant) ---")
print(alice.work())
print(alice.eat())
print(r2d2.work())
print(f"Robot responds to eat? {hasattr(r2d2, 'eat')}  (correctly false)")

print("-" * 50)


def lunch_break(person):
    if not hasattr(person, "eat"):
        return f"{type(person).__name__} skips lunch"
    return f"{person.eat()}, then {person.sleep()}"


def run_shift(worker):
    return worker.work()


print(lunch_break(alice))
print(lunch_break(r2d2))
print(run_shift(alice))
print(run_shift(r2d2))

print("-" * 50)


class Cyborg(Workable, Eater):
    def __init__(self, name):
        self.name = name


cy = Cyborg("Cy")
print(f"{cy.work()} | {cy.eat()} | sleeps? {hasattr(cy, 'sleep')}")

print("-" * 50)


print("""ISP RECAP
---------
Don't force classes to implement methods they don't need.""")
