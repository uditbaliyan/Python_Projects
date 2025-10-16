# -------------------------------------------------------------
# Imports
# -------------------------------------------------------------
from typing import List


# -------------------------------------------------------------
# LeetCode 26: Remove Duplicates from Sorted Array
# -------------------------------------------------------------
# Description:
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element
# appears only once and return the number of unique elements.
#
# Constraints:
# - 1 <= nums.length <= 3 * 10^4
# - -100 <= nums[i] <= 100
# - nums is sorted in non-decreasing order.
# -------------------------------------------------------------


# -------------------------------------------------------------
# 🔹 Approach 1: Two Pointer Technique (In-place)
# -------------------------------------------------------------
# Idea:
# Use one pointer (slow) to track the position of the last unique element
# and another pointer (fast) to scan through the array.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 0  # index of last unique element
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


# -------------------------------------------------------------
# 🔹 Approach 2: Using Python Set (Not in-place - for comparison)
# -------------------------------------------------------------
# This approach is not valid per LeetCode requirements
# but demonstrates the simpler way using set + sort.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionUsingSet:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        for i in range(len(unique)):
            nums[i] = unique[i]
        return len(unique)


# -------------------------------------------------------------
# 🔹 Example Run
# -------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2], [1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
        ([1, 1, 1, 1, 1], [1], 1),
    ]

    solver = Solution()
    for nums, expected_arr, expected_k in test_cases:
        nums_copy = nums.copy()
        k = solver.removeDuplicates(nums_copy)
        print(f"Input: {nums}")
        print(
            f"Output k: {k}, nums: {nums_copy[:k]} | Expected: {expected_arr}, k = {expected_k}\n"
        )
