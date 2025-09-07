from abc import ABC, abstractmethod
import math
from typing import Tuple


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    def __init__(self, immutable: bool = False) -> None:
        self._immutable = immutable

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass

    # -------------------- Dunder Methods --------------------

    def __eq__(self, other: object) -> bool:
        """Shapes are equal if they are the same type and dimensions match."""
        if not isinstance(other, Shape):
            return NotImplemented
        return type(self) is type(other) and self.__dict__ == other.__dict__

    def __lt__(self, other: object) -> bool:
        """Order shapes by area."""
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() < other.area()

    def __repr__(self) -> str:
        """Unambiguous representation for debugging."""
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

    def __str__(self) -> str:
        """User-friendly representation."""
        return (
            f"{self.__class__.__name__} with area={self.area():.2f} "
            f"and perimeter={self.perimeter():.2f}"
        )


# -------------------- Rectangle --------------------
class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, width: float, height: float, immutable: bool = False) -> None:
        super().__init__(immutable)
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self._width: float = width
        self._height: float = height

    @property
    def dimensions(self) -> Tuple[float, float]:
        return self._width, self._height

    @property
    def is_square(self) -> bool:
        return self._width == self._height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if self._immutable:
            raise AttributeError("This Rectangle is immutable.")
        if value <= 0:
            raise ValueError("Width must be positive.")
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if self._immutable:
            raise AttributeError("This Rectangle is immutable.")
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)


# -------------------- Circle --------------------
class Circle(Shape):
    """Circle shape with radius."""

    def __init__(self, radius: float, immutable: bool = False) -> None:
        super().__init__(immutable)
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self._radius: float = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if self._immutable:
            raise AttributeError("This Circle is immutable.")
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    def area(self) -> float:
        return math.pi * (self._radius**2)

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

    @classmethod
    def from_diameter(cls, diameter: float) -> "Circle":
        """Alternate constructor to create a Circle from its diameter."""
        return cls(diameter / 2)


# -------------------- Triangle --------------------
class Triangle(Shape):
    """Triangle shape with three sides."""

    def __init__(self, a: float, b: float, c: float, immutable: bool = False) -> None:
        super().__init__(immutable)
        if not self.is_valid(a, b, c):
            raise ValueError("Invalid triangle sides.")
        self._a: float = a
        self._b: float = b
        self._c: float = c

    # ---- Validation helper ----
    @staticmethod
    def is_valid(a: float, b: float, c: float) -> bool:
        return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

    # ---- Properties ----
    @property
    def sides(self) -> Tuple[float, float, float]:
        return self._a, self._b, self._c

    @property
    def is_equilateral(self) -> bool:
        return self._a == self._b == self._c

    @property
    def is_isosceles(self) -> bool:
        return len({self._a, self._b, self._c}) == 2

    @property
    def is_scalene(self) -> bool:
        return len({self._a, self._b, self._c}) == 3

    # ---- Side setters with validation ----
    def _check_mutability(self) -> None:
        if self._immutable:
            raise AttributeError("This Triangle is immutable.")

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._check_mutability()
        if not self.is_valid(value, self._b, self._c):
            raise ValueError("Invalid triangle sides.")
        self._a = value

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, value: float) -> None:
        self._check_mutability()
        if not self.is_valid(self._a, value, self._c):
            raise ValueError("Invalid triangle sides.")
        self._b = value

    @property
    def c(self) -> float:
        return self._c

    @c.setter
    def c(self, value: float) -> None:
        self._check_mutability()
        if not self.is_valid(self._a, self._b, value):
            raise ValueError("Invalid triangle sides.")
        self._c = value

    # ---- Area & Perimeter ----
    def area(self) -> float:
        s = (self._a + self._b + self._c) / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    def perimeter(self) -> float:
        return self._a + self._b + self._c


def main():
    print("=== Shape Hierarchy Demo ===")

    # ----- Circle -----
    c1 = Circle(5)
    c2 = Circle.from_diameter(10)  # same as radius=5
    print("\nCircle examples:")
    print(c1)  # user-friendly str
    print(repr(c2))  # debugging repr
    print("Equal?", c1 == c2)
    print("Perimeter of c1:", c1.perimeter())

    # ----- Rectangle -----
    r1 = Rectangle(4, 6)
    r2 = Rectangle(5, 5, immutable=True)  # square, immutable
    print("\nRectangle examples:")
    print(r1)
    print("Is r2 a square?", r2.is_square)

    # Try mutating immutable rectangle
    try:
        r2.width = 10
    except AttributeError as e:
        print("Mutation blocked:", e)

    # ----- Triangle -----
    t1 = Triangle(3, 4, 5)  # classic right triangle
    t2 = Triangle(2, 2, 3)
    print("\nTriangle examples:")
    print(t1)
    print("Sides:", t1.sides)
    print("Is t2 isosceles?", t2.is_isosceles)

    # ----- Comparisons & Sorting -----
    shapes = [c1, r1, t1, r2, t2]
    print("\nSorting shapes by area:")
    for s in sorted(shapes):
        print(f"{s.__class__.__name__}: area={s.area():.2f}")

    # ----- Equality checks -----
    print("\nEquality checks:")
    print("t1 == t2?", t1 == t2)
    print("c1 == c2?", c1 == c2)

    # ----- Using repr for debugging -----
    print("\nDebug representations:")
    for s in shapes:
        print(repr(s))


if __name__ == "__main__":
    main()
