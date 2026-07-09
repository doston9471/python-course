# =============================================================
# LESSON 14: SOLID — O = OPEN/CLOSED PRINCIPLE (OCP)
# =============================================================


# --- Step 1: The VIOLATION ----------------------------------
class AreaCalculatorBad:
    def area_of(self, shape):
        if shape["type"] == "rectangle":
            return shape["w"] * shape["h"]
        if shape["type"] == "circle":
            return 3.14159 * shape["r"] ** 2
        raise ValueError(f"unknown shape {shape['type']}")


calc = AreaCalculatorBad()
print(f"Rect:   {calc.area_of({'type': 'rectangle', 'w': 3, 'h': 4})}")
print(f"Circle: {calc.area_of({'type': 'circle', 'r': 2}):.2f}")

print("-" * 50)


# --- Step 2: The FIX — extend via polymorphism --------------
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2


class AreaCalculator:
    def total_area(self, shapes):
        return sum(s.area() for s in shapes)


shapes = [Rectangle(3, 4), Circle(2)]
print(f"Total area: {AreaCalculator().total_area(shapes):.2f}")

print("-" * 50)


class Triangle:
    def __init__(self, base, height):
        self.base, self.height = base, height

    def area(self):
        return 0.5 * self.base * self.height


shapes.append(Triangle(6, 4))
print(f"Total with triangle: {AreaCalculator().total_area(shapes):.2f}")

print("-" * 50)


class NoDiscount:
    def apply(self, total):
        return total


class PercentageDiscount:
    def __init__(self, pct):
        self.pct = pct

    def apply(self, total):
        return total - (total * self.pct / 100.0)


class Checkout:
    def __init__(self, discount=None):
        self._discount = discount or NoDiscount()

    def final_price(self, total):
        return self._discount.apply(total)


print(f"No discount:   ${Checkout().final_price(100)}")
print(f"10% discount:  ${Checkout(PercentageDiscount(10)).final_price(100)}")


class BuyOneGetFixed:
    def __init__(self, amount):
        self.amount = amount

    def apply(self, total):
        return max(total - self.amount, 0)


print(f"$15 off:       ${Checkout(BuyOneGetFixed(15)).final_price(100)}")

print("-" * 50)


print("""OCP RECAP
---------
Open for extension, closed for modification.""")
