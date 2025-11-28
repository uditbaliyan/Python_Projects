from __future__ import annotations
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


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


class StackLRU(Generic[T]):
    def __init__(self) -> None:
        self.head = LRUNode(None)
        self.tail = LRUNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, value: T) -> None:
        node = LRUNode(value)
        self._insert_front(node)

    def _insert_front(self, node: LRUNode[T]) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def pop(self) -> T:
        first = self.head.next
        if first == self.tail:
            raise IndexError("pop from empty stack")
        self._remove(first)
        return first.value

    def _remove(self, node: LRUNode[T]) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def peek(self) -> Optional[T]:
        first = self.head.next
        return None if first == self.tail else first.value
