from __future__ import annotations
from dataclasses import dataclass

from typing import Optional, Generic, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional[Node[T]] = None


class PersistentStack(Generic[T]):
    def __init__(self, head: Optional[Node[T]] = None):
        self.head = head

    def push(self, value: T) -> PersistentStack[T]:
        return PersistentStack(Node(value, self.head))

    def pop(self) -> tuple[T, PersistentStack[T]]:
        if not self.head:
            raise IndexError("pop from empty stack")
        return self.head.value, PersistentStack(self.head.next)

    def peek(self) -> Optional[T]:
        return self.head.value if self.head else None
