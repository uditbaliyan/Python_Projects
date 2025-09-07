"""
11. **Shape Hierarchy**
    - **Description**: Model geometric shapes with polymorphic methods.
    - **Requirements**:
      - Abstract `Shape` class (using `abc`) with `area()` and `perimeter()`.
      - Subclasses: `Circle`, `Rectangle`, `Triangle` with unique calculations.
      - Implement `__str__` for readable output.
    - **Constraints**: Validate geometric constraints (e.g., positive dimensions).

"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return math.isclose(self.area(), other.area())

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() < other.area()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with area={self.area():.2f} and perimeter={self.perimeter():.2f}"


class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, x: float, y: float) -> None:
        if x <= 0 or y <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self._width = x
        self._height = y

    @property
    def dimensions(self) -> tuple[float, float]:
        """Return the dimensions as a tuple (width, height)."""
        return self._width, self._height

    @property
    def is_square(self) -> bool:
        """Check if the rectangle is a square."""
        return self._width == self._height

    @property
    def height(self):
        """The height property."""
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self._height = value

    @property
    def width(self):
        """The width property."""
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self._width = value

    def area(self) -> float:
        return self._height * self._width

    def perimeter(self) -> float:
        return 2 * (self._height + self._width)


class Circle(Shape):
    """Circle shape with radius."""

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = value

    def area(self) -> float:
        return math.pi * (self._radius**2)

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius


class Triangle(Shape):
    """Triangle shape with three sides."""

    def __init__(self, a: float, b: float, c: float) -> None:
        if self.is_valid(a, b, c) is False:
            raise ValueError(
                "The sum of any two sides must be greater than the third side."
            )
        self._a = a
        self._b = b
        self._c = c

    @classmethod
    def is_valid(cls, a: float, b: float, c: float) -> bool:
        """Check if the sides can form a valid triangle."""
        return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

    @property
    def is_equilateral(self) -> bool:
        """Check if the triangle is equilateral."""
        return self._a == self._b == self._c

    @property
    def is_isosceles(self) -> bool:
        """Check if the triangle is isosceles."""
        return self._a == self._b or self._b == self._c or self._a == self._c

    @property
    def is_scalene(self) -> bool:
        """Check if the triangle is scalene."""
        return self._a != self._b and self._b != self._c and self._a != self._c

    @property
    def a(self):
        """Side a property."""
        return self._a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("Side a must be a positive number.")
        if value + self._b <= self._c or value + self._c <= self._b:
            raise ValueError(
                "The sum of any two sides must be greater than the third side."
            )
        self._a = value

    @property
    def b(self):
        """Side b property."""
        return self._b

    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("Side b must be a positive number.")
        if value + self._a <= self._c or value + self._c <= self._a:
            raise ValueError(
                "The sum of any two sides must be greater than the third side."
            )
        self._b = value

    @property
    def c(self):
        """Side c property."""
        return self._c

    @c.setter
    def c(self, value):
        if value <= 0:
            raise ValueError("Side c must be a positive number.")
        if value + self._a <= self._b or value + self._b <= self._a:
            raise ValueError(
                "The sum of any two sides must be greater than the third side."
            )
        self._c = value

    def area(self) -> float:
        s = (self._a + self._b + self._c) / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    def perimeter(self) -> float:
        return self._a + self._b + self._c


def main() -> None:
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
        Rectangle(5, 5),
        Circle(2.5),
        Triangle(6, 6, 6),
    ]

    for shape in shapes:
        print(shape)

    # Demonstrate comparison
    print("\nComparing shapes based on area:")
    shapes_sorted = sorted(shapes)
    for shape in shapes_sorted:
        print(f"{shape} with area {shape.area():.2f}")

    circles = [
        Circle(3),
        Circle(4),
        Circle(5),
        Circle(6),
        Circle(7),
        Circle(8),
        Circle(9),
    ]

    print("\nSorted Circles by area:")
    for circle in sorted(circles):
        print(f"{circle} with area {circle.area():.2f}")

    squares = [Rectangle(2, 2), Rectangle(3, 3), Rectangle(4, 4), Rectangle(5, 5)]
    print("\nSorted Squares by area:")
    for shape in sorted(squares):
        print(f"{shape} with area {shape.area():.2f}")

    rectangles = [Rectangle(2, 3), Rectangle(3, 4), Rectangle(4, 5), Rectangle(5, 6)]
    print("\nSorted Rectangles by area:")
    for shape in sorted(rectangles):
        print(f"{shape} with area {shape.area():.2f}")

    triangles = [Triangle(3, 4, 5), Triangle(5, 12, 13), Triangle(6, 8, 10)]
    print("\nSorted Triangles by area:")
    for shape in sorted(triangles):
        print(f"{shape} with area {shape.area():.2f}")


if __name__ == "__main__":
    main()
