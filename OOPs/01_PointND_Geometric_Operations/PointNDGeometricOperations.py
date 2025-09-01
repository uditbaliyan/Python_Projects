class PointNDGeometricOperations:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

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
