"""
📝 ComplexNumber Class Design Guide

Goal: Create a class that behaves like Python’s built-in complex numbers, but with your own implementation. This helps practice OOP + operator overloading.

Step 1: Basics

__init__(self, real, imag) → store real and imag parts.

__str__(self) → return a readable string like "3 + 4i" (handle signs correctly).

Step 2: Operator Overloading

Implement:

__add__(self, other) → (a+bi) + (c+di) = (a+c) + (b+d)i

__sub__(self, other) → (a+bi) - (c+di)

__mul__(self, other) → (a+bi)(c+di) = (ac - bd) + (ad + bc)i

__eq__(self, other) → check equality of real and imag parts.

Step 3: Useful Helpers

magnitude(self) → √(a² + b²)

conjugate(self) → a - bi

Step 4: Testing/Usage

Make sure the class supports:

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, -2)

print(c1)             # "3 + 4i"
print(c1 + c2)        # "4 + 2i"
print(c1 * c2)        # "11 - 2i"
print(c1 == c2)       # False
print(c1.magnitude()) # 5.0
"""

import math


class ComplexNumber:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __sub__(self, value):
        return ComplexNumber(self.x - value.x, self.y - value.y)

    def __add__(self, value):
        return ComplexNumber(self.x + value.x, self.y + value.y)

    def __mul__(self, value):
        real = self.x * value.x - self.y * value.y
        imag = self.x * value.y + self.y * value.x
        return ComplexNumber(real, imag)

    def __str__(self):
        sign = "+" if self.y >= 0 else "-"
        return f"{self.x} {sign} {abs(self.y)}i"

    def __hash__(self) -> int:
        return hash(self.x * self.y)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def conjugate(self):
        return ComplexNumber(self.x, -self.y)

    def __neg__(self):
        return ComplexNumber(-self.x, -self.y)

    def __abs__(self):
        return self.magnitude()

    def __truediv__(self, value):
        denom = value.x**2 + value.y**2
        real = (self.x * value.x + self.y * value.y) / denom
        imag = (self.y * value.x - self.x * value.y) / denom
        return ComplexNumber(real, imag)


def test_complex():
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(1, -2)

    # __str__
    assert str(c1) == "3 + 4i"
    assert str(c2) == "1 - 2i"

    # __neg__
    assert str(-c1) == "-3 - 4i"

    # addition
    assert (c1 + c2) == ComplexNumber(4, 2)

    # subtraction
    assert (c1 - c2) == ComplexNumber(2, 6)

    # multiplication
    assert (c1 * c2) == ComplexNumber(11, -2)

    # equality
    assert c1 == ComplexNumber(3, 4)
    assert c1 != c2

    # magnitude
    assert c1.magnitude() == 5.0

    # conjugate
    assert c2.conjugate() == ComplexNumber(1, 2)

    print("All tests passed ✅")


def main():
    test_complex()


if __name__ == "__main__":
    main()
