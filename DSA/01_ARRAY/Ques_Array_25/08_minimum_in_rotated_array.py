from typing import List

""" 
Rotated array is also soreted ? 
Is there any duplicates [how to ]
"""


def min_in_rotated_array(arr: List[int]) -> int:
    """using simple loop"""
    minimum = 0
    for value in arr:
        if minimum < value:
            minimum = value
    return minimum


def min_in_rotated_array_1(arr: List[int]) -> int:
    """using min func"""
    return min(arr)


def min_in_rotated_array_2(arr: List[int]) -> int:
    """binary search"""
    start = 0
    end = len(arr) - 1
    minimum = arr[0]
    mid = 0
    if arr[start] < arr[end]:
        return arr[0]
    while start <= end:
        mid = (start + end) // 2
        if arr[start] < arr[end]:
            minimum = min(minimum, arr[start])
        if arr[start] <= arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        minimum = min(minimum, arr[start])
    return minimum


def main():
    arr = [3, 4, 5, 6, 7, 0, 1, 2]
    print(min_in_rotated_array_2(arr=arr))


if __name__ == "__main__":
    main()
