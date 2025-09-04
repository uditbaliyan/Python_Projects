import json
import math
from typing import Any

"""
class PointNDGeometricOperations:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def mname(self) -> None:
        pass

    def __add__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Points must have the same number of dimensions")
        return PointNDGeometricOperations(
            *(a + b for a, b in zip(self.coordinates, other.coordinates, strict=False))
        )

    def __sub__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Points must have the same number of dimensions")
        return PointNDGeometricOperations(
            *(a - b for a, b in zip(self.coordinates, other.coordinates, strict=False))
        )

    def __mul__(self, scalar):
        return PointNDGeometricOperations(*(a * scalar for a in self.coordinates))

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return PointNDGeometricOperations(*(a / scalar for a in self.coordinates))

    def __repr__(self):
        return f"PointNDGeometricOperations{self.coordinates}"
"""


class Point2D:
    """Represents a 2D point with vector operations and distance metrics."""

    __FLOAT_TOLERANCE = 1e-6  # Default tolerance for equality comparison

    def __init__(self, x: float, y: float) -> None:
        """Initializes a 2D point.

        Args:
            x (float): X-coordinate.
            y (float): Y-coordinate.

        Raises:
            TypeError: If x or y is not a float or int.
        """
        self._validate_number(x, "x")
        self._validate_number(y, "y")
        self.x = float(x)
        self.y = float(y)

    def euclidean_distance(self, other: "Point2D") -> float:
        """Calculates the Euclidean distance to another point.

        Args:
            other (Point2D): Another 2D point.

        Returns:
            float: Euclidean distance.

        Raises:
            TypeError: If other is not a Point2D.
        """
        self._validate_point(other)
        return math.hypot(self.x - other.x, self.y - other.y)

    def manhattan_distance(self, other: "Point2D") -> float:
        """Calculates the Manhattan (L1) distance to another point."""
        self._validate_point(other)
        return abs(self.x - other.x) + abs(self.y - other.y)

    def minkowski_distance(self, other: "Point2D", p: float) -> float:
        """Calculates the Minkowski distance to another point.

        Args:
            other (Point2D): Another 2D point.
            p (float): Order of the norm (must be > 0).

        Returns:
            float: Minkowski distance.

        Raises:
            ValueError: If p <= 0.
            TypeError: If other is not a Point2D or p is not numeric.
        """
        self._validate_point(other)
        self._validate_number(p, "p")
        if p <= 0:
            raise ValueError("Order 'p' must be greater than 0.")

        return (abs(self.x - other.x) ** p + abs(self.y - other.y) ** p) ** (1 / p)

    def dot(self, other: "Point2D") -> float:
        """Calculates the dot product with another point."""
        self._validate_point(other)
        return self.x * other.x + self.y * other.y

    def __add__(self, other: "Point2D") -> "Point2D":
        """Adds two points coordinate-wise."""
        self._validate_point(other)
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point2D") -> "Point2D":
        """Subtracts two points coordinate-wise."""
        self._validate_point(other)
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Point2D":
        """Multiplies the point by a scalar."""
        self._validate_number(scalar, "scalar")
        return Point2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Point2D":
        """Supports scalar multiplication from the left: scalar * point."""
        return self.__mul__(scalar)

    def __eq__(self, other: Any) -> bool:
        """Checks equality with another point within a tolerance."""
        if not isinstance(other, Point2D):
            return NotImplemented
        return math.isclose(
            self.x, other.x, rel_tol=self.__FLOAT_TOLERANCE
        ) and math.isclose(self.y, other.y, rel_tol=self.__FLOAT_TOLERANCE)

    def __hash__(self) -> int:
        """Returns a hash based on rounded coordinates."""
        return hash((
            round(self.x / self.__FLOAT_TOLERANCE),
            round(self.y / self.__FLOAT_TOLERANCE),
        ))

    def to_json(self) -> str:
        """Serializes the point to a JSON string.

        Returns:
            str: JSON representation of the point.
        """
        return json.dumps({"x": self.x, "y": self.y})

    @classmethod
    def from_json(cls, json_str: str) -> "Point2D":
        """Deserializes a Point2D from a JSON string.

        Args:
            json_str (str): JSON string with 'x' and 'y' fields.

        Returns:
            Point2D: The resulting Point2D object.

        Raises:
            ValueError: If JSON is invalid or missing keys.
        """
        try:
            data = json.loads(json_str)
            return cls(data["x"], data["y"])
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            raise ValueError("Invalid JSON for Point2D") from e

    def __repr__(self) -> str:
        """Returns the official string representation of the point."""
        return f"Point2D(x={self.x}, y={self.y})"

    # ---------------------
    # Internal Helper Methods
    # ---------------------

    @staticmethod
    def _validate_point(point: Any) -> None:
        """Ensures the argument is a Point2D instance."""
        if not isinstance(point, Point2D):
            raise TypeError(f"Expected Point2D, got {type(point).__name__}")

    @staticmethod
    def _validate_number(value: Any, name: str) -> None:
        """Ensures a value is a float or int."""
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"{name} must be (int or float), got {type(value).__name__}"
            )


"""
class Point_2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def euclidean_distance(self, other: "Point2D") -> float:
        pass

    def manhattan_distance(self, other: "Point2D") -> float:
        pass

    def minkowski_distance(self, other: "Point2D", p: float) -> float:
        pass

    def __add__(self, other: "Point2D") -> "Point2D":
        return Point2D(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: "Point2D") -> "Point2D":
        return Point2D(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, scalar: float) -> "Point2D":
        return Point2D(x=self.x * other.x, y=self.y * other.y)

    def dot(self, other: "Point2D") -> float:
        pass

    def __eq__(self, other: "Point2D", tolerance: float = 1e-6) -> bool:
        return bool(self.x == other.x and self.y == other.y)
        # return True if self.x == other.x and self.y == other.y else False

    def to_json(self) -> str:
        pass


class Point3D:
    def __init__(self, x: float, y: float, z: float):
        pass

    def euclidean_distance(self, other: "Point3D") -> float:
        pass

    def manhattan_distance(self, other: "Point3D") -> float:
        pass

    def minkowski_distance(self, other: "Point3D", p: float) -> float:
        pass

    def __add__(self, other: "Point3D") -> "Point3D":
        pass

    def __sub__(self, other: "Point3D") -> "Point3D":
        pass

    def __mul__(self, scalar: float) -> "Point3D":
        pass

    def dot(self, other: "Point3D") -> float:
        pass

    def __eq__(self, other: "Point3D", tolerance: float = 1e-6) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def to_json(self) -> str:
        pass


class PointND:
    def __init__(self, coordinates: list[float]):
        pass

    def euclidean_distance(self, other: "PointND") -> float:
        pass

    def manhattan_distance(self, other: "PointND") -> float:
        pass

    def minkowski_distance(self, other: "PointND", p: float) -> float:
        pass

    def __add__(self, other: "PointND") -> "PointND":
        pass

    def __sub__(self, other: "PointND") -> "PointND":
        pass

    def __mul__(self, scalar: float) -> "PointND":
        pass

    def dot(self, other: "PointND") -> float:
        pass

    def __eq__(self, other: "PointND", tolerance: float = 1e-6) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def to_json(self) -> str:
        pass
"""
