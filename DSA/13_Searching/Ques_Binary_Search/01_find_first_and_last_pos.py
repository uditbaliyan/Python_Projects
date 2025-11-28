# -----------------------------------------------------------
# LeetCode 34. Find First and Last Position of Element in Sorted Array
# -----------------------------------------------------------
# Problem:
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i], target <= 10^9
# nums is sorted in non-decreasing order.
# -----------------------------------------------------------

from typing import List
import bisect


# -----------------------------------------------------------
# 🧩 Approach 1: Binary Search (Manual)
# -----------------------------------------------------------
# - Find the first occurrence using binary search.
# - Find the last occurrence using binary search.
# - Return both indices.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
# -----------------------------------------------------------
def searchRange_binary(nums: List[int], target: int) -> List[int]:
    def find_bound(is_first: bool) -> int:
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1  # Search on the left side
                else:
                    left = mid + 1  # Search on the right side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    first = find_bound(True)
    last = find_bound(False)
    return [first, last]


# -----------------------------------------------------------
# 🧩 Approach 2: Using bisect_left and bisect_right
# -----------------------------------------------------------
# - `bisect_left(nums, target)` gives the first index >= target
# - `bisect_right(nums, target)` gives the first index > target
# - If target exists, range = [left, right - 1]
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
# -----------------------------------------------------------
def searchRange_bisect(nums: List[int], target: int) -> List[int]:
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target) - 1

    if left < len(nums) and nums[left] == target:
        return [left, right]
    return [-1, -1]


# -----------------------------------------------------------
# 🧩 Approach 3: Combined Helper + Clean Wrapper
# -----------------------------------------------------------
# - Reuse bisect for elegant expression.
# - Wrapper simplifies readability.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
# -----------------------------------------------------------
def searchRange(nums: List[int], target: int) -> List[int]:
    start = bisect.bisect_left(nums, target)
    end = bisect.bisect_right(nums, target) - 1
    return [start, end] if start < len(nums) and nums[start] == target else [-1, -1]


# -----------------------------------------------------------
# ✅ Test Cases
# -----------------------------------------------------------
if __name__ == "__main__":
    tests = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([1, 2, 3, 3, 3, 4, 5], 3, [2, 4]),
        ([2, 2, 2, 2, 2], 2, [0, 4]),
        ([1, 2, 3, 4, 5], 10, [-1, -1]),
    ]

    print("Testing: Find First and Last Position of Element in Sorted Array\n")
    for nums, target, expected in tests:
        res1 = searchRange_binary(nums, target)
        res2 = searchRange_bisect(nums, target)
        res3 = searchRange(nums, target)
        print(f"nums = {nums}, target = {target}")
        print(f"Manual Binary Search: {res1}")
        print(f"Bisect Method:        {res2}")
        print(f"Clean Wrapper:        {res3}")
        print(f"Expected:             {expected}")
        print("-" * 55)
