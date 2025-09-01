from typing import List

MIN_ELEMENTS_REQUIRED = 2


def largest_builtin(arr: List[int]) -> int:
    """
    Find the largest element in a list using Python's built-in max().

    Args:
        arr (List[int]): List of integers.

    Returns:
        int: The largest element.

    Raises:
        ValueError: If the list is empty.
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    return max(arr)


def largest_iterative(arr: List[int]) -> int:
    """
    Find the largest element in a list using an iterative approach.

    Args:
        arr (List[int]): List of integers.

    Returns:
        int: The largest element.

    Raises:
        ValueError: If the list is empty.
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    largest = arr[0]
    for value in arr:
        largest = max(value, largest)
    return largest


def second_largest_sorted(arr: List[int]) -> int:
    """
    Find the second largest element in a list (assuming no duplicates).
    Uses sorting (O(n log n)).

    Args:
        arr (List[int]): List of integers (at least 2 elements, no duplicates).

    Returns:
        int: The second largest element.

    Raises:
        ValueError: If the list has fewer than 2 elements.
    """

    if len(arr) < MIN_ELEMENTS_REQUIRED:
        raise ValueError("Array must contain at least two elements")
    return sorted(arr)[-2]


def second_largest_iterative(arr: List[int]) -> int:
    """
    Find the second largest element in a list (assuming no duplicates).
    Uses a single-pass O(n) iteration.

    Args:
        arr (List[int]): List of integers (at least 2 elements, no duplicates).

    Returns:
        int: The second largest element.

    Raises:
        ValueError: If the list has fewer than 2 elements.
    """
    if len(arr) < MIN_ELEMENTS_REQUIRED:
        raise ValueError("Array must contain at least two elements")

    largest = second_largest = float("-inf")
    for value in arr:
        if value > largest:
            second_largest, largest = largest, value
        elif value > second_largest:
            second_largest = value
    return second_largest


def second_largest_with_duplicates(arr: List[int]) -> int:
    """
    Find the second largest element in a list (handles duplicates).
    Uses a single-pass O(n) iteration.

    Args:
        arr (List[int]): List of integers (at least 2 elements).

    Returns:
        int: The second largest unique element.

    Raises:
        ValueError: If the list has fewer than 2 unique elements.
    """
    if len(arr) < MIN_ELEMENTS_REQUIRED:
        raise ValueError("Array must contain at least two elements")

    largest = second_largest = float("-inf")
    for value in arr:
        if value > largest:
            second_largest, largest = largest, value
        elif value > second_largest and value != largest:
            second_largest = value

    if second_largest == float("-inf"):
        raise ValueError("Array must contain at least two unique elements")
    return second_largest
