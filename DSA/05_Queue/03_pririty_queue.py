"""
priority_queue.py

A collection of Priority Queue implementations in Python.
Includes three progressively improved approaches:

1. BruteForcePriorityQueue
   - Simple list-based implementation.
   - Slow removals (O(n)).
   - Good for learning the concept.

2. HeapPriorityQueue
   - Uses Python's built-in `heapq` module.
   - Efficient O(log n) operations.
   - Standard choice for DSA and competitive coding.

3. AdvancedPriorityQueue
   - Uses `dataclasses` for clean priority/value separation.
   - Stable ordering via a counter (FIFO for equal priorities).
   - Ideal for schedulers, task processors, and simulations.

Each implementation provides:
    - push(...)
    - pop(...)
    - peek(...)
    - __len__()
"""

from __future__ import annotations
import heapq
from dataclasses import dataclass, field
from typing import Any, List
# ============================================================
# 1. BRUTE FORCE PRIORITY QUEUE
# ============================================================


class BruteForcePriorityQueue:
    """
    A simple Priority Queue implemented using a Python list.

    Insert: O(1)
    Pop:    O(n)  — searches entire list for minimum element
    Peek:   O(n)

    This class is meant for conceptual clarity, not performance.
    """

    def __init__(self) -> None:
        self.data: List[Any] = []

    def push(self, item: Any) -> None:
        """Insert an item into the queue."""
        self.data.append(item)

    def pop(self) -> Any:
        """Remove and return the smallest item."""
        if not self.data:
            raise IndexError("pop from empty priority queue")
        min_idx = 0
        for i in range(1, len(self.data)):
            if self.data[i] < self.data[min_idx]:
                min_idx = i
        return self.data.pop(min_idx)

    def peek(self) -> Any:
        """Return the smallest item without removing it."""
        if not self.data:
            raise IndexError("peek from empty priority queue")
        return min(self.data)

    def __len__(self) -> int:
        return len(self.data)


# ============================================================
# 2. HEAP-BASED PRIORITY QUEUE (STANDARD)
# ============================================================


class HeapPriorityQueue:
    """
    Priority Queue implemented using Python's built-in `heapq`,
    which provides a binary min-heap.

    Insert: O(log n)
    Pop:    O(log n)
    Peek:   O(1)

    This is the recommended implementation for most scenarios.
    """

    def __init__(self) -> None:
        self.heap: List[Any] = []

    def push(self, item: Any) -> None:
        """Insert an item using heap push."""
        heapq.heappush(self.heap, item)

    def pop(self) -> Any:
        """Remove and return the smallest item."""
        if not self.heap:
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self.heap)

    def peek(self) -> Any:
        """Return the smallest item without removing it."""
        if not self.heap:
            raise IndexError("peek from empty priority queue")
        return self.heap[0]

    def __len__(self) -> int:
        return len(self.heap)


# ============================================================
# 3. ADVANCED PRIORITY QUEUE (STABLE + DATACLASS)
# ============================================================


@dataclass(order=True)
class PrioritizedItem:
    """
    Wraps (priority, counter, item) so that items are ordered only
    by priority and counter — not by the actual item content.
    """

    priority: int
    counter: int
    item: Any = field(compare=False)


class AdvancedPriorityQueue:
    """
    A stable priority queue using:

        (priority, counter, actual_item)

    The counter ensures that if two items share the same priority,
    they come out in FIFO order.

    Insert: O(log n)
    Pop:    O(log n)
    Peek:   O(1)

    Ideal for:
        - task schedulers
        - event simulation
        - A* / Dijkstra variants
        - multi-priority job queues
    """

    def __init__(self) -> None:
        self.heap: List[PrioritizedItem] = []
        self.counter: int = 0

    def push(self, priority: int, item: Any) -> None:
        """Insert an item with a priority value."""
        heapq.heappush(self.heap, PrioritizedItem(priority, self.counter, item))
        self.counter += 1

    def pop(self) -> Any:
        """Remove and return the item with smallest priority."""
        if not self.heap:
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self.heap).item

    def peek(self) -> Any:
        """Return the next item without removing it."""
        if not self.heap:
            raise IndexError("peek from empty priority queue")
        return self.heap[0].item

    def __len__(self) -> int:
        return len(self.heap)


# ============================================================
# EXAMPLE USAGE
# (Uncomment to run directly)
# ============================================================

if __name__ == "__main__":
    print("=== Brute Force PQ ===")
    bf = BruteForcePriorityQueue()
    bf.push(5)
    bf.push(1)
    bf.push(3)
    print(bf.pop())  # 1

    print("\n=== Heap PQ ===")
    hp = HeapPriorityQueue()
    hp.push(5)
    hp.push(1)
    hp.push(3)
    print(hp.pop())  # 1

    print("\n=== Advanced PQ ===")
    ap = AdvancedPriorityQueue()
    ap.push(5, "slow")
    ap.push(1, "urgent")
    ap.push(3, "normal")
    print(ap.pop())  # "urgent"
