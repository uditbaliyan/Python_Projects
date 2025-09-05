"""
maximum sub array:
smaller sequence of the original array
"""

from typing import List


def all_possible_subarrays(arr: List[int]) -> None:
    """trying"""
    size = len(arr)
    prev = 0
    next = 1
    for i in range(0, size):
        prev, next = 0, i + 1
        while next <= size:
            print(arr[prev:next], f"arr[{prev}:{next}]")
            prev += 1
            next += 1
        # prev, next = 0, i + 2


def maximum_subarray_sum(arr: List[int]) -> int:
    size = len(arr)
    prev = 0
    next = 1
    max_sum = 0
    for i in range(0, size):
        prev, next = 0, i + 1
        while next <= size:
            max_sum = max(sum(arr[prev:next]), max_sum)
            next += 1
            prev += 1
    return max_sum


def maximum_subarray_sum_1(arr: List[int]) -> int:
    """Dynamic sliding window"""
    max_sum, temp_sum = 0, 0
    size = len(arr)
    for i in range(0, size):
        if temp_sum + arr[i] < 0:
            temp_sum = 0
            continue

        temp_sum += arr[i]
        max_sum = max(max_sum, temp_sum)
        print(temp_sum, max_sum, i)

    return max_sum


def main():
    # arr = [1, 2, 3, 4]
    # all_possible_subarrays(arr)
    # print(maximum_subarray_sum(arr=arr))
    print(maximum_subarray_sum_1(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == "__main__":
    main()
