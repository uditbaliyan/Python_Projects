"""
4. **Polygon Geometry Engine**
   - **Description**: Represent 2D polygons with `Point2D` vertices.
   - **Requirements**:
     - Compute area (shoelace formula), perimeter, and centroid.
     - Test if a point lies inside (ray-casting algorithm).
     - Detect intersections with another polygon.
   - **Constraints**: Support convex/concave polygons; optimize for large vertex counts.

"""


# try stack and queue
class Queue:
    """FIFO"""

    def __init__(self) -> None:
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.isempty:
            raise ValueError("Queue is empty")
        self.data.pop(0)

    @property
    def isempty(self):
        # return not self.data
        return not any(self.data)

    @property
    def peek(self):
        if self.isempty:
            raise ValueError("Queue is empty")
        return self.data[0]


class Stack:
    """Last IN First Out(LIFO)"""

    def __init__(self) -> None:
        self.data = []

    def push(self, value) -> None:
        self.data.append(value)

    def pop(self) -> None:
        if self.isempty:
            raise ValueError("Stack is empty")
        self.data.pop()

    def peek(self):
        if self.isempty:
            return "Stack is empty"
        self.data[-1]

    @property
    def size(self):
        return len(self.data)

    @property
    def isempty(self):
        return bool(~(len(self.data)))

    @property
    def isfull(self):
        return bool(~(len(self.data)))

    def __str__(self) -> str:
        return f"Stack contains {self.size}"

    def __repr__(self):
        return f"Stack contains {self.data}"
