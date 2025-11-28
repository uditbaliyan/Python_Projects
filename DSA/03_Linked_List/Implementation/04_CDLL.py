from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar, Iterator


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


class SentinelCDLL(Generic[T]):
    def __init__(self) -> None:
        self.sentinel = CDLLNode(None)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def append(self, value: T) -> None:
        node = CDLLNode(value)
        last = self.sentinel.prev
        last.next = node
        node.prev = last
        node.next = self.sentinel
        self.sentinel.prev = node

    def prepend(self, value: T) -> None:
        node = CDLLNode(value)
        first = self.sentinel.next
        self.sentinel.next = node
        node.prev = self.sentinel
        node.next = first
        first.prev = node

    def __iter__(self) -> Iterator[T]:
        cur = self.sentinel.next
        while cur != self.sentinel:
            yield cur.value
            cur = cur.next


class LRUNode(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.prev: Optional[LRUNode[T]] = None
        self.next: Optional[LRUNode[T]] = None


class LRUList(Generic[T]):
    def __init__(self) -> None:
        self.head = LRUNode(None)
        self.tail = LRUNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, node: LRUNode[T]) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: LRUNode[T]) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_last(self) -> LRUNode[T]:
        last = self.tail.prev
        self.remove(last)
        return last
