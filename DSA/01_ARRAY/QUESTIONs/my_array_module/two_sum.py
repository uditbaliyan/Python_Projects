from typing import List, Optional, Tuple


# Two-pointer approach (returns values)
def two_sum(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    arr.sort()
    ptr_start, ptr_end = 0, len(arr) - 1
    while ptr_start < ptr_end:
        current_sum = arr[ptr_start] + arr[ptr_end]
        if current_sum == target:
            return (arr[ptr_start], arr[ptr_end])
        elif current_sum < target:
            ptr_start += 1
        else:
            ptr_end -= 1
    return None


# Hashmap approach (returns indices)
def two_sum_2(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    seen = {}
    for idx, value in enumerate(arr):
        complement = target - value
        if complement in seen:
            return (seen[complement], idx)
        seen[value] = idx
    return None


# One-liner existence check
def two_sum_3(arr: List[int], target: int) -> bool:
    return any((target - value) in arr[idx + 1 :] for idx, value in enumerate(arr))
