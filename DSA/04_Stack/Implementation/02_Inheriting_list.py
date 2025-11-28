from __future__ import annotations
from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class StackListInherit(list, Generic[T]):
    def push(self, value: T) -> None:
        self.append(value)

    def peek(self) -> Optional[T]:
        return self[-1] if self else None

    def is_empty(self) -> bool:
        return len(self) == 0
