import dataclasses
from typing import Deque


@dataclasses.dataclass
class Element:
    value: int
    priority: int


def main(*arg):
    deque = Deque()
    deque.append(10)
    print(deque)
    deque.appendleft(9)
    print(deque)
    deque.extend([11, 12, 13, 14, 15, 16])
    print(deque)
    deque.extendleft([1, 2, 3, 4, 5, 6, 7, 8])
    print(deque)
    deque.pop()
    print(deque)
    deque.popleft()
    print(deque)


if __name__ == "__main__":
    main()
