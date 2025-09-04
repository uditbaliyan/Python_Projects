from typing import Dict, List


def contains_duplicates_count(arr: List[int]) -> bool:
    """
    Checks for duplicates using the count() method.
    Time complexity: O(n^2) – not efficient for large arrays.
    """
    return any(arr.count(value) > 1 for value in arr)


def contains_duplicates_sort_inplace(arr: List[int]) -> bool:
    """
    Checks for duplicates by sorting the array in-place.
    Time complexity: O(n log n)
    Space complexity: O(1) (excluding input)
    WARNING: Modifies original array.
    """
    arr.sort()
    return any(arr[i] == arr[i - 1] for i in range(1, len(arr)))


def contains_duplicates_sorted_copy(arr: List[int]) -> bool:
    """
    Checks for duplicates by creating a sorted copy.
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    prev = None
    for value in sorted(arr):
        if value == prev:
            return True
        prev = value
    return False


def contains_duplicates_set(arr: List[int]) -> bool:
    """
    Checks for duplicates using a set.
    Time complexity: O(n)
    Space complexity: O(n)
    Most efficient and Pythonic solution.
    """
    seen = set()
    for value in arr:
        if value in seen:
            return True
        seen.add(value)
    return False


def contains_duplicates_dict(arr: List[int]) -> bool:
    """
    Checks for duplicates using a dictionary (manual hashing).
    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen: Dict[int, int] = {}
    for value in arr:
        if value in seen:
            return True
        seen[value] = 1
    return False


def contains_duplicates_len_compare(arr: List[int]) -> bool:
    """
    Checks for duplicates by comparing lengths of list and set.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    return len(arr) != len(set(arr))


# Optional: benchmarking
def main():
    test_cases = [
        [1, 2, 3, 4],  # No duplicates
        [1, 2, 3, 1],  # Has duplicates
        [],  # Empty list
        [5],  # Single element
        [1, 1, 1, 1],  # All duplicates
        [1, 2, 3, 4, 5, 5],  # Duplicate at end
    ]

    methods = [
        contains_duplicates_count,
        contains_duplicates_sort_inplace,
        contains_duplicates_sorted_copy,
        contains_duplicates_set,
        contains_duplicates_dict,
        contains_duplicates_len_compare,
    ]

    for i, test_case in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {test_case}")
        for method in methods:
            result = method(test_case.copy())
            print(f"{method.__name__}: {result}")


if __name__ == "__main__":
    main()
