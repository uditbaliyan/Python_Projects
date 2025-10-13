from typing import List, Optional, Tuple
from itertools import combinations


def two_sum_two_pointer(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Finds a pair of numbers that add up to the target using the two-pointer technique.
    NOTE: Returns the actual values, not indices.
    Time complexity: O(n log n) due to sorting.
    WARNING: Modifies the input array.
    """
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None


def two_sum_hashmap(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Finds a pair of indices where the values sum up to the target using a hash map.
    Returns the indices (i, j) such that arr[i] + arr[j] == target.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen = {}

    for idx, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return (seen[complement], idx)
        seen[num] = idx

    return None


def two_sum_exists_oneliner(arr: List[int], target: int) -> bool:
    """
    Returns True if any two elements in arr sum to the target.
    Uses a one-liner with a generator expression.
    Time complexity: O(n^2) in worst case.
    """
    return any((target - val) in arr[i + 1 :] for i, val in enumerate(arr))


def two_sum_set_lookup(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Similar to hashmap method but stores values instead of indices.
    Returns a pair of values if found.
    Time complexity: O(n)
    """
    seen = set()

    for value in arr:
        complement = target - value
        if complement in seen:
            return (complement, value)
        seen.add(value)

    return None


def two_sum_brute_force(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Naive brute-force approach. Checks all pairs.
    Time complexity: O(n^2)
    Only for learning or very small input.
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None


def two_sum_brute_force_2(arr: list[int], target: int) -> bool:
    """
    Naive brute-force using itertools,
    combinations fuction.
    Time complexity:

    """
    for combination in combinations(arr, 2):
        if sum(combination) == target:
            return True
    return False


def main():
    test_cases = [
        ([2, 7, 11, 15], 9),  # Expected: (2, 7) or indices (0, 1)
        ([3, 2, 4], 6),  # Expected: (2, 4) or indices (1, 2)
        ([3, 3], 6),  # Expected: (3, 3) or indices (0, 1)
        ([1, 2, 3, 4, 5], 10),  # No pair
        ([1, 5, 1, 5], 10),  # Multiple pairs possible
        ([], 0),  # Empty array
        ([1], 1),  # Single element
    ]

    methods = [
        two_sum_two_pointer,
        two_sum_hashmap,
        two_sum_exists_oneliner,
        two_sum_set_lookup,
        two_sum_brute_force,
        two_sum_brute_force_2,
    ]

    for i, (arr, target) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: arr = {arr}, target = {target}")
        for method in methods:
            result = method(arr.copy(), target)
            print(f"{method.__name__}: {result}")


if __name__ == "__main__":
    main()
