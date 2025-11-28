from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterator, Generic, TypeVar

T = TypeVar("T")


@dataclass
class SLLNode(Generic[T]):
    value: T
    next: Optional[SLLNode[T]] = None


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[SLLNode[T]] = None

    def append(self, value: T) -> None:
        node = SLLNode(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def prepend(self, value: T) -> None:
        node = SLLNode(value, next=self.head)
        self.head = node

    def __iter__(self) -> Iterator[T]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next


class StackFromSLL(SinglyLinkedList[T]):
    def push(self, value: T) -> None:
        self.prepend(value)

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
