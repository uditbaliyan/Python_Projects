from abc import ABC, abstractmethod
from collections import UserList
from typing import List, Optional, Tuple


class Array25(ABC):
    @abstractmethod
    def two_sum(self, target: int) -> Optional[Tuple[int, int]]:
        pass

    @abstractmethod
    def three_sum(self, target: int) -> Optional[Tuple[int, int]]:
        """Docstring"""
        pass


class MyArray(UserList, Array25):
    """My array"""

    def __init__(self, arr: List[int]):
        super().__init__(arr)

    def two_sum(self, target: int) -> Optional[Tuple[int, int]]:
        seen = {}
        for i, num in enumerate(self.data):
            complement = target - num
            if complement in seen:
                return (seen[complement], i)
            seen[num] = i
        return None

    def three_sum(self, target: int) -> Optional[Tuple[int, int]]:
        """Docstring"""
        pass

    def bubble_sort(self):
        pass

    def insertion_sort(self) -> None:
        pass
