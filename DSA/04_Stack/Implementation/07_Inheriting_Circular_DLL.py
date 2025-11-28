from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional, Iterator

T = TypeVar("T")


@dataclass
class CDLLNode(Generic[T]):
    value: T
    prev: Optional[CDLLNode[T]] = None
    next: Optional[CDLLNode[T]] = None


class CircularDoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[CDLLNode[T]] = None

    def append(self, value: T) -> None:
        node = CDLLNode(value)
        if not self.head:
            node.next = node.prev = node
            self.head = node
            return
        tail = self.head.prev
        tail.next = node
        node.prev = tail
        node.next = self.head
        self.head.prev = node

    def prepend(self, value: T) -> None:
        self.append(value)
        self.head = self.head.prev

    def __iter__(self) -> Iterator[T]:
        if not self.head:
            return
        cur = self.head
        while True:
            yield cur.value
            cur = cur.next
            if cur == self.head:
                break


class StackCDLL(CircularDoublyLinkedList[T]):
    def push(self, value: T) -> None:
        self.append(value)

    def pop(self) -> T:
        if not self.head:
            raise IndexError("pop from empty stack")
        tail = self.head.prev
        val = tail.value
        if tail == self.head:
            self.head = None
            return val
        tail.prev.next = self.head
        self.head.prev = tail.prev
        return val

    def peek(self) -> Optional[T]:
        return self.head.prev.value if self.head else None
