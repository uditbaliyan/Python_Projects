from __future__ import annotations
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class StackList(Generic[T]):
    def __init__(self) -> None:
        self._data: list[T] = []

    def push(self, value: T) -> None:
        self._data.append(value)

    def pop(self) -> T:
        return self._data.pop()

    def peek(self) -> Optional[T]:
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        return len(self._data) == 0
