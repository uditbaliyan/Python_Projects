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


class StackDLL(DoublyLinkedList[T]):
    def push(self, value: T) -> None:
        self.append(value)

    def pop(self) -> T:
        if not self.tail:
            raise IndexError("pop from empty stack")
        val = self.tail.value
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = self.tail = None
        return val

    def peek(self) -> Optional[T]:
        return self.tail.value if self.tail else None
