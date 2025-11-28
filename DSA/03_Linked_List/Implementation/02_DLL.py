from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar, Iterator


T = TypeVar("T")


@dataclass
class DLLNode(Generic[T]):
    value: T
    prev: Optional[DLLNode[T]] = None
    next: Optional[DLLNode[T]] = None


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[DLLNode[T]] = None
        self.tail: Optional[DLLNode[T]] = None

    def append(self, value: T) -> None:
        node = DLLNode(value)
        if not self.tail:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def prepend(self, value: T) -> None:
        node = DLLNode(value)
        if not self.head:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def __iter__(self) -> Iterator[T]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next


@dataclass
class DLLNode_1(Generic[T]):
    value: Optional[T] = None
    prev: Optional[DLLNode_1[T]] = None
    next: Optional[DLLNode_1[T]] = None


class DoublyLinkedList_1(Generic[T]):
    def __init__(self) -> None:
        self.head = DLLNode_1[T]()  # sentinel head
        self.tail = DLLNode_1[T]()  # sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, value: T) -> None:
        node = DLLNode_1(value)
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def prepend(self, value: T) -> None:
        node = DLLNode_1(value)
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

    def __iter__(self) -> Iterator[T]:
        cur = self.head.next
        while cur is not self.tail:
            yield cur.value  # value is guaranteed not None here
            cur = cur.next


class FNode(Generic[T]):
    def __init__(self, value: T, prev: Optional[FNode[T]], nxt: Optional[FNode[T]]):
        self.value = value
        self.prev = prev
        self.next = nxt


class FunctionalDLL(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[FNode[T]] = None
        self.tail: Optional[FNode[T]] = None

    def append(self, value: T) -> None:
        new = FNode(value, self.tail, None)
        if not self.tail:
            self.head = self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def prepend(self, value: T) -> None:
        new = FNode(value, None, self.head)
        if not self.head:
            self.head = self.tail = new
            return
        self.head.prev = new
        self.head = new

    def iter_reverse(self) -> Iterator[T]:
        cur = self.tail
        while cur:
            yield cur.value
            cur = cur.prev

    def __iter__(self) -> Iterator[T]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next
