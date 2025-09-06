"""
geometry/circle.py

Advanced Circle class with numeric-stable geometry operations, caching,
optional immutability, serialization helpers, and utilities useful for CAD/plotting.

Author: ChatGPT (adapt & extend as needed)
"""

from __future__ import annotations
import math
import threading
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple
import json

# Try importing numpy for potential vectorized discretization; optional.
try:
    import numpy as np  # type: ignore
except Exception:
    np = None  # fallback to math-based loops


# ---- Exceptions ----
class InvalidRadiusError(ValueError):
    """Raised when radius is non-positive or invalid."""


class CircleOperationError(RuntimeError):
    """Generic error for unsupported operations on circles."""


class GeometryPrecisionError(RuntimeError):
    """Raised when numeric precision prevents a reliable geometric result."""


# ---- Helpers ----
def _is_finite_number(x: float) -> bool:
    return isinstance(x, (int, float)) and math.isfinite(float(x))


def _clamp(x: float, lo: float, hi: float) -> float:
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x


# ---- Circle class ----
class Circle:
    # Class-level constants
    EPSILON: float = 1e-9
    TAU: float = 2.0 * math.pi
    DEFAULT_NUM_SEGMENTS: int = 64

    def __init__(
        self,
        cx: float = 0.0,
        cy: float = 0.0,
        radius: float = 1.0,
        *,
        immutable: bool = False,
        tol: Optional[float] = None,
    ) -> None:
        """Create a Circle.

        Args:
            cx, cy: center coordinates
            radius: must be > 0
            immutable: if True, disallow in-place changes
            tol: per-instance tolerance override (EPSILON)
        """
        # Validate inputs
        if not _is_finite_number(cx) or not _is_finite_number(cy):
            raise ValueError("Center coordinates must be finite numbers.")
        if not _is_finite_number(radius) or radius <= 0.0:
            raise InvalidRadiusError("Radius must be > 0 and finite.")
        self._cx: float = float(cx)
        self._cy: float = float(cy)
        self._radius: float = float(radius)
        self._immutable: bool = bool(immutable)
        # Per-instance tolerance
        self.EPSILON = float(tol) if tol is not None else Circle.EPSILON

        # Internal cache and lock
        self._cache: Dict[str, Any] = {}
        self._cache_lock = threading.Lock()

        # Metadata
        self._created_at = datetime.now()

    # ----- Invariants helpers -----
    def _assert_mutable(self) -> None:
        if self._immutable:
            raise AttributeError(
                "Circle is immutable; in-place modifications are disallowed."
            )

    def _invalidate_cache(self) -> None:
        with self._cache_lock:
            self._cache.clear()

    def _validate_radius_value(self, value: float) -> float:
        if not _is_finite_number(value) or value <= 0.0:
            raise InvalidRadiusError("Radius must be > 0 and finite.")
        return float(value)

    # ----- Basic accessors -----
    @property
    def center(self) -> Tuple[float, float]:
        return (self._cx, self._cy)

    @property
    def cx(self) -> float:
        return self._cx

    @property
    def cy(self) -> float:
        return self._cy

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._assert_mutable()
        val = self._validate_radius_value(value)
        if abs(self._radius - val) > self.EPSILON:
            self._radius = val
            self._invalidate_cache()

    @property
    def diameter(self) -> float:
        key = "diameter"
        with self._cache_lock:
            if key in self._cache:
                return self._cache[key]
            d = 2.0 * self._radius
            self._cache[key] = d
            return d

    @property
    def area(self) -> float:
        key = "area"
        with self._cache_lock:
            if key in self._cache:
                return self._cache[key]
            a = math.pi * (self._radius**2)
            self._cache[key] = a
            return a

    @property
    def circumference(self) -> float:
        key = "circumference"
        with self._cache_lock:
            if key in self._cache:
                return self._cache[key]
            c = Circle.TAU * self._radius
            self._cache[key] = c
            return c

    @property
    def bounding_box(self) -> Tuple[float, float, float, float]:
        key = "bounding_box"
        with self._cache_lock:
            if key in self._cache:
                return self._cache[key]
            r = self._radius
            bbox = (self._cx - r, self._cy - r, self._cx + r, self._cy + r)
            self._cache[key] = bbox
            return bbox

    @property
    def is_unit(self) -> bool:
        return abs(self._radius - 1.0) <= self.EPSILON

    @property
    def created_at(self) -> datetime:
        return self._created_at

    # ----- Representation & comparison -----
    def __str__(self) -> str:
        return f"Circle(cx={self._cx:.6g}, cy={self._cy:.6g}, r={self._radius:.6g})"

    def __repr__(self) -> str:
        imm = ", immutable=True" if self._immutable else ""
        return f"Circle({self._cx!r}, {self._cy!r}, {self._radius!r}{imm})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return (
            abs(self._cx - other._cx) <= max(self.EPSILON, other.EPSILON)
            and abs(self._cy - other._cy) <= max(self.EPSILON, other.EPSILON)
            and abs(self._radius - other._radius) <= max(self.EPSILON, other.EPSILON)
        )

    def __lt__(self, other: "Circle") -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius - self.EPSILON

    def __le__(self, other: "Circle") -> bool:
        return self == other or self < other

    def __gt__(self, other: "Circle") -> bool:
        return not (self <= other)

    def __ge__(self, other: "Circle") -> bool:
        return not (self < other)

    # membership: point in circle
    def __contains__(self, point: Tuple[float, float]) -> bool:
        x, y = point
        return self.contains_point(x, y, inclusive=True)

    # scaling operators
    def __mul__(self, scale: float) -> "Circle":
        if not _is_finite_number(scale) or scale <= 0.0:
            raise ValueError("Scale must be > 0 and finite.")
        return Circle(
            self._cx, self._cy, self._radius * float(scale), immutable=self._immutable
        )

    def __rmul__(self, scale: float) -> "Circle":
        return self.__mul__(scale)

    # copying / immutability
    def copy(
        self,
        *,
        cx: Optional[float] = None,
        cy: Optional[float] = None,
        radius: Optional[float] = None,
        immutable: Optional[bool] = None,
    ) -> "Circle":
        return Circle(
            cx if cx is not None else self._cx,
            cy if cy is not None else self._cy,
            radius if radius is not None else self._radius,
            immutable=self._immutable if immutable is None else bool(immutable),
            tol=self.EPSILON,
        )

    # ----- Geometry queries -----
    def contains_point(self, x: float, y: float, *, inclusive: bool = True) -> bool:
        if not _is_finite_number(x) or not _is_finite_number(y):
            raise ValueError("Point coordinates must be finite numbers.")
        d = math.hypot(x - self._cx, y - self._cy)
        if inclusive:
            return d <= self._radius + self.EPSILON
        return d < self._radius - self.EPSILON

    def distance_to(self, other: "Circle") -> float:
        if not isinstance(other, Circle):
            raise TypeError("distance_to expects a Circle.")
        return math.hypot(self._cx - other._cx, self._cy - other._cy)

    def intersects(self, other: "Circle") -> bool:
        d = self.distance_to(other)
        r1, r2 = self._radius, other._radius
        # disjoint
        if d > r1 + r2 + self.EPSILON:
            return False
        # one strictly inside the other without touching
        if d + min(r1, r2) < max(r1, r2) - self.EPSILON:
            # contained (not intersecting boundaries) -> consider as intersecting only if we consider containment intersecting;
            # here we follow the spec: intersects = have any overlap (including containment), so return True.
            return True
        return True

    def intersection_area(self, other: "Circle") -> float:
        """Return overlap area. Handles disjoint, contained, tangent cases robustly."""
        if not isinstance(other, Circle):
            raise TypeError("intersection_area expects a Circle.")
        d = self.distance_to(other)
        r0 = self._radius
        r1 = other._radius

        # disjoint
        if d >= r0 + r1 - self.EPSILON:
            return 0.0

        # one contains the other
        if d <= abs(r0 - r1) + self.EPSILON:
            # smaller circle area
            return math.pi * (min(r0, r1) ** 2)

        # general case: use formula
        # clamp arguments for acos to [-1,1]
        try:
            # compute the angles
            # using law of cosines
            cos0 = _clamp((d**2 + r0**2 - r1**2) / (2 * d * r0), -1.0, 1.0)
            cos1 = _clamp((d**2 + r1**2 - r0**2) / (2 * d * r1), -1.0, 1.0)
            phi0 = math.acos(cos0) * 2.0
            phi1 = math.acos(cos1) * 2.0
            # segment areas
            area0 = 0.5 * r0**2 * (phi0 - math.sin(phi0))
            area1 = 0.5 * r1**2 * (phi1 - math.sin(phi1))
            return area0 + area1
        except ValueError as e:
            # possible numeric issues; raise a precision error
            raise GeometryPrecisionError(
                "Numeric failure computing intersection area."
            ) from e

    def intersection_points(self, other: "Circle") -> List[Tuple[float, float]]:
        """Return intersection points (0,1,2). Raises GeometryPrecisionError if numerically unstable."""
        if not isinstance(other, Circle):
            raise TypeError("intersection_points expects a Circle.")
        d = self.distance_to(other)
        r0 = self._radius
        r1 = other._radius

        # no intersection (disjoint or one inside the other without touching)
        if d > r0 + r1 + self.EPSILON or d < abs(r0 - r1) - self.EPSILON:
            return []

        # single intersection (tangent)
        if abs(d - (r0 + r1)) <= self.EPSILON or abs(d - abs(r0 - r1)) <= self.EPSILON:
            # compute single touching point
            # direction vector from self to other
            if d == 0.0:
                # concentric circles: infinite or zero intersections; treat as ambiguous
                raise GeometryPrecisionError(
                    "Concentric circles; intersection points undefined."
                )
            ux = (other._cx - self._cx) / d
            uy = (other._cy - self._cy) / d
            # touching point along the line at distance r0 from self center (toward other)
            px = self._cx + ux * r0
            py = self._cy + uy * r0
            return [(px, py)]

        # two intersection points
        # compute a: distance from self center to the line joining intersection points
        # formula: a = (r0^2 - r1^2 + d^2) / (2d)
        a = (r0**2 - r1**2 + d**2) / (2.0 * d)
        # height from that line to intersection points:
        h_sq = r0**2 - a**2
        if h_sq < -self.EPSILON:
            raise GeometryPrecisionError(
                "h^2 negative beyond tolerance while computing intersection points."
            )
        h = math.sqrt(max(0.0, h_sq))

        # point p2: base point
        xm = self._cx + a * (other._cx - self._cx) / d
        ym = self._cy + a * (other._cy - self._cy) / d

        rx = -(other._cy - self._cy) * (h / d)
        ry = (other._cx - self._cx) * (h / d)

        p1 = (xm + rx, ym + ry)
        p2 = (xm - rx, ym - ry)
        return [p1, p2]

    def tangent_points_from_external(
        self, px: float, py: float
    ) -> List[Tuple[float, float]]:
        """Return tangent contact points on this circle from external point (px,py).

        - 0 points if inside circle,
        - 1 point if on circle (returns that point),
        - 2 points if outside (returns both).
        """
        if not _is_finite_number(px) or not _is_finite_number(py):
            raise ValueError("Point must be finite numbers.")
        dx = px - self._cx
        dy = py - self._cy
        d2 = dx * dx + dy * dy
        r = self._radius
        r2 = r * r

        if d2 < r2 - self.EPSILON:
            return []  # inside
        if abs(d2 - r2) <= self.EPSILON:
            # exactly on the circle
            return [(px, py)]

        # outside: there are two tangents
        d = math.hypot(dx, dy)
        # angle from center to point
        base = math.atan2(dy, dx)
        # angle between base and tangent
        # cos(theta) = r / d
        cos_t = _clamp(r / d, -1.0, 1.0)
        theta = math.acos(cos_t)

        t1 = base + theta
        t2 = base - theta
        p1 = (self._cx + r * math.cos(t1), self._cy + r * math.sin(t1))
        p2 = (self._cx + r * math.cos(t2), self._cy + r * math.sin(t2))
        return [p1, p2]

    def circle_line_intersection(
        self, line: Tuple[Tuple[float, float], Tuple[float, float]]
    ) -> List[Tuple[float, float]]:
        """Intersect circle with an infinite line or segment defined by two points.
        The input is ((x1,y1),(x2,y2)).
        Returns intersections with the infinite line. If you want segment intersections,
        post-filter the returned points to lie within segment extents.
        """
        (x1, y1), (x2, y2) = line
        if not (
            _is_finite_number(x1)
            and _is_finite_number(y1)
            and _is_finite_number(x2)
            and _is_finite_number(y2)
        ):
            raise ValueError("Line coordinates must be finite.")

        # Represent line as p = p1 + t*(p2-p1)
        dx = x2 - x1
        dy = y2 - y1
        fx = x1 - self._cx
        fy = y1 - self._cy

        a = dx * dx + dy * dy
        b = 2.0 * (fx * dx + fy * dy)
        c = fx * fx + fy * fy - self._radius * self._radius

        # Solve at^2 + bt + c = 0
        disc = b * b - 4.0 * a * c
        if disc < -self.EPSILON:
            return []
        if abs(disc) <= self.EPSILON:
            t = -b / (2.0 * a)
            px = x1 + t * dx
            py = y1 + t * dy
            return [(px, py)]
        sqrt_disc = math.sqrt(max(0.0, disc))
        t1 = (-b + sqrt_disc) / (2.0 * a)
        t2 = (-b - sqrt_disc) / (2.0 * a)
        p1 = (x1 + t1 * dx, y1 + t1 * dy)
        p2 = (x1 + t2 * dx, y1 + t2 * dy)
        return [p1, p2]

    def arc_length(
        self, angle1: float, angle2: float, *, radians: bool = True
    ) -> float:
        """Arc length from angle1 to angle2 following the smaller positive rotation by default."""
        if not radians:
            angle1 = math.radians(angle1)
            angle2 = math.radians(angle2)
        # normalize angles to [0, 2pi)
        a1 = angle1 % Circle.TAU
        a2 = angle2 % Circle.TAU
        delta = (a2 - a1) % Circle.TAU
        # Use the shorter arc? The user did not explicitly ask for shortest vs directed arc;
        # here we return the positive (counter-clockwise) arc length.
        return self._radius * delta

    def point_on_circumference(
        self, angle: float, *, radians: bool = True
    ) -> Tuple[float, float]:
        if not radians:
            angle = math.radians(angle)
        return (
            self._cx + self._radius * math.cos(angle),
            self._cy + self._radius * math.sin(angle),
        )

    # ----- Discretization and rendering helpers -----
    def discretize(self, n: Optional[int] = None) -> List[Tuple[float, float]]:
        """Return ordered polygonal approximation of the circle (counter-clockwise)."""
        n = int(n) if n is not None else Circle.DEFAULT_NUM_SEGMENTS
        if n <= 2:
            raise ValueError("n must be >= 3 for discretization.")
        key = f"discretize:{n}"
        with self._cache_lock:
            if key in self._cache:
                return list(self._cache[key])  # return a shallow copy

        # Use numpy for speed if available
        if np is not None:
            angles = np.linspace(0.0, Circle.TAU, num=n, endpoint=False)
            xs = self._cx + self._radius * np.cos(angles)
            ys = self._cy + self._radius * np.sin(angles)
            pts = list(zip(xs.tolist(), ys.tolist()))
        else:
            pts = []
            for k in range(n):
                theta = (k * Circle.TAU) / n
                pts.append((
                    self._cx + self._radius * math.cos(theta),
                    self._cy + self._radius * math.sin(theta),
                ))

        with self._cache_lock:
            self._cache[key] = list(pts)
        return pts

    def to_svg_path(self) -> str:
        """Return a compact SVG <circle .../> element string for the circle."""
        # Escape/format numeric fields with reasonable precision
        return (
            f'<circle cx="{self._cx:.6f}" cy="{self._cy:.6f}" r="{self._radius:.6f}" />'
        )

    def to_wkt(self, precision: int = 6, *, n_segments: Optional[int] = None) -> str:
        """Return WKT 'POLYGON' approximation (string) with the specified precision."""
        pts = self.discretize(
            n_segments if n_segments is not None else Circle.DEFAULT_NUM_SEGMENTS
        )
        fmt = f"{{:.{precision}f}}"
        coords = ", ".join(
            " ".join((fmt.format(x), fmt.format(y))) for x, y in pts + [pts[0]]
        )
        return f"POLYGON(({coords}))"

    # ----- Set-algebra-ish helpers -----
    def buffer(self, delta: float) -> "Circle":
        new_r = self._radius + float(delta)
        if new_r <= 0.0:
            raise InvalidRadiusError("Resulting buffered radius must be > 0.")
        return Circle(
            self._cx, self._cy, new_r, immutable=self._immutable, tol=self.EPSILON
        )

    def contains_circle(self, other: "Circle") -> bool:
        d = self.distance_to(other)
        return d + other._radius <= self._radius + self.EPSILON

    def is_disjoint(self, other: "Circle") -> bool:
        d = self.distance_to(other)
        return d > (self._radius + other._radius) + self.EPSILON

    def approximate_union_polygon(
        self, other: "Circle", n_segments: Optional[int] = None
    ) -> List[Tuple[float, float]]:
        """Approximate union by merging discretized polygons and returning their convex/concave hull.
        This is a convenience method — for production-grade polygon union use shapely or CGAL.
        Here we simply return concatenated boundary points; user should post-process (e.g., via shapely).
        """
        pts1 = self.discretize(n_segments)
        pts2 = other.discretize(n_segments)
        return pts1 + pts2

    # ----- Serialization -----
    def to_dict(self, *, include_cache: bool = False) -> Dict[str, Any]:
        d = {
            "cx": self._cx,
            "cy": self._cy,
            "radius": self._radius,
            "immutable": self._immutable,
            "eps": self.EPSILON,
            "created_at": self._created_at.isoformat() + "Z",
        }
        if include_cache:
            with self._cache_lock:
                # shallow-copy cache (avoid non-serializable objects)
                d["_cache"] = {k: v for k, v in self._cache.items()}
        return d

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Circle":
        cx = float(d["cx"])
        cy = float(d["cy"])
        radius = float(d["radius"])
        immutable = bool(d.get("immutable", False))
        tol = d.get("eps", None)
        c = cls(cx, cy, radius, immutable=immutable, tol=tol)
        # created_at is metadata - optional restore
        if "created_at" in d:
            try:
                c._created_at = datetime.fromisoformat(d["created_at"].rstrip("Z"))
            except Exception:
                pass
        return c

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), separators=(",", ":"), sort_keys=True)

    @classmethod
    def from_json(cls, json_str: str) -> "Circle":
        d = json.loads(json_str)
        return cls.from_dict(d)

    # ----- Additional utilities -----
    def scale_inplace(self, scale: float) -> None:
        """Scale radius in-place (if mutable)."""
        self._assert_mutable()
        if not _is_finite_number(scale) or scale <= 0.0:
            raise ValueError("scale must be > 0 and finite.")
        new_r = self._radius * float(scale)
        if abs(new_r - self._radius) > self.EPSILON:
            self._radius = new_r
            self._invalidate_cache()
