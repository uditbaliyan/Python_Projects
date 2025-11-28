from __future__ import annotations
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional[Node[T]] = None):
        self.value = value
        self.next = next


class StackLL(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None

    def push(self, value: T) -> None:
        self.head = Node(value, next=self.head)

    def pop(self) -> T:
        if not self.head:
            raise IndexError("pop from empty stack")
        val = self.head.value
        self.head = self.head.next
        return val

    def peek(self) -> Optional[T]:
        return self.head.value if self.head else None

    def is_empty(self) -> bool:
        return self.head is None
