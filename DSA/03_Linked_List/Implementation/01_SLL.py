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


class FastSinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[SLLNode[T]] = None
        self.tail: Optional[SLLNode[T]] = None

    def append(self, value: T) -> None:
        node = SLLNode(value)
        if not self.head:
            self.head = self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def prepend(self, value: T) -> None:
        node = SLLNode(value, next=self.head)
        self.head = node
        if not self.tail:
            self.tail = node

    def __iter__(self) -> Iterator[T]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next


class FunctionalSLL(Generic[T]):
    def __init__(self, head: Optional[SLLNode[T]] = None) -> None:
        self.head = head

    def prepend(self, value: T) -> FunctionalSLL[T]:
        return FunctionalSLL(SLLNode(value, self.head))

    def __iter__(self) -> Iterator[T]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next
