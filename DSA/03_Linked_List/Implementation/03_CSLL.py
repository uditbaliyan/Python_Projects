from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar, Iterator


T = TypeVar("T")


@dataclass
class CSLLNode(Generic[T]):
    value: T
    next: Optional[CSLLNode[T]] = None


class CircularSinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.tail: Optional[CSLLNode[T]] = None

    def append(self, value: T) -> None:
        node = CSLLNode(value)
        if not self.tail:
            node.next = node
            self.tail = node
            return
        node.next = self.tail.next
        self.tail.next = node
        self.tail = node

    def prepend(self, value: T) -> None:
        node = CSLLNode(value)
        if not self.tail:
            node.next = node
            self.tail = node
            return
        node.next = self.tail.next
        self.tail.next = node

    def __iter__(self) -> Iterator[T]:
        if not self.tail:
            return
        cur = self.tail.next
        while True:
            yield cur.value
            cur = cur.next
            if cur == self.tail.next:
                break


@dataclass
class CSLLNode_1(Generic[T]):
    value: T
    next: Optional[CSLLNode[T]] = None


class CircularSinglyLinkedList_1(Generic[T]):
    def __init__(self) -> None:
        self.tail: Optional[CSLLNode_1[T]] = None

    def append(self, value: T) -> None:
        node = CSLLNode_1(value)
        if not self.tail:
            node.next = node
            self.tail = node
            return
        node.next = self.tail.next
        self.tail.next = node
        self.tail = node

    def prepend(self, value: T) -> None:
        node = CSLLNode_1(value)
        if not self.tail:
            node.next = node
            self.tail = node
            return
        node.next = self.tail.next
        self.tail.next = node

    def __iter__(self) -> Iterator[T]:
        if not self.tail:
            return
        cur = self.tail.next
        while True:
            yield cur.value
            cur = cur.next
            if cur == self.tail.next:
                break


class FastCircularSLL(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[CSLLNode[T]] = None
        self.size = 0

    def append(self, value: T) -> None:
        node = CSLLNode(value)
        if not self.head:
            node.next = node
            self.head = node
        else:
            tail = self._find_tail()
            tail.next = node
            node.next = self.head
        self.size += 1

    def _find_tail(self) -> CSLLNode[T]:
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        return cur

    def __iter__(self) -> Iterator[T]:
        if not self.head:
            return
        cur = self.head
        for _ in range(self.size):
            yield cur.value
            cur = cur.next


class JosephusCircle(Generic[T]):
    def __init__(self, values: list[T]) -> None:
        self.tail: Optional[CSLLNode[T]] = None
        for v in values:
            self.append(v)

    def append(self, value: T) -> None:
        node = CSLLNode(value)
        if not self.tail:
            node.next = node
            self.tail = node
            return
        node.next = self.tail.next
        self.tail.next = node
        self.tail = node

    def step(self, k: int) -> T:
        cur = self.tail
        for _ in range(k):
            cur = cur.next
        removed = cur.next
        cur.next = removed.next
        if removed == self.tail:
            self.tail = cur
        return removed.value
