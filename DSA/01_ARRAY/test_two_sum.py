from typing import List, Optional, Tuple


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


def test_two_sum_two_pointer():
    result = two_sum_two_pointer(arr=[1, 2, 3, 4, 5, 6, 7], target=10)
    assert result == (3, 7)
