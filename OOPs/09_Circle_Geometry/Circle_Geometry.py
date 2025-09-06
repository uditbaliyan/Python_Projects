import datetime
import math
from typing import Any, Dict


class InvalidRadiusError(Exception):
    pass


class CircleOperationError(Exception):
    pass


class GeometryPrecisionError(Exception):
    pass


class Circle:
    TAU = 2 * math.pi
    EPSILON = "10e - 9"
    DEFAULT_NUM_SEGMENTS = 64

    def __init__(
        self, cx: float, cy: float, radius: Any[float, int], immutable: bool, tol: float
    ) -> None:
        if radius > 0:
            self._radius: float = radius
            self._cy: float = cy

            self._cx: float = cx

            self._immutable: bool = immutable
            self._cache: Dict[str, float] = {}
            self._created_at = datetime.datetime.now()
            self._tol: float = tol
        else:
            raise InvalidRadiusError("Radius must be whole number .")

    @property
    def center(self):
        return (self._cx, self._cy)

    @property
    def radius(self):
        """The  property."""
        return self._radius

    @radius.setter
    def radius(self, value):
        if self._immutable:
            if value > 0:
                self._ = value
            else:
                raise InvalidRadiusError("Radius must be greater that 0.")
        else:
            raise AttributeError

    @property
    def cy(self):
        """The  property."""
        return self._cy

    @cy.setter
    def cy(self, value):
        self._cy = value

    @property
    def cx(self):
        """The  property."""
        return self._cx

    @cx.setter
    def cx(self, value):
        self._cx = value

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def area(self):
        return self.TAU * pow(self._radius, 2)

    @property
    def circumference(self):
        return self.TAU * self._radius

    @property
    def bound_box(self):
        pass

    @property
    def created_at(self):
        return self._created_at

    @property
    def is_unit(self):
        pass

    def __str__(self) -> str:
        return f"Circle(cx={self._cx},cy={self._cy},radius={self._radius})"

    def __repr__(self) -> str:
        return f"Circle(cx={self._cx},cy={self._cy},radius={self._radius},immutablity={self._immutable})"

    def __lt__(self):
        pass

    def __mul__(self):
        pass

    def __eq__(self, value: object, /) -> bool:
        pass

    def copy(self):
        return Circle(
            cx=self._cx,
            cy=self._cy,
            radius=self._radius,
            immutable=self._immutable,
            tol=self._tol,
        )
