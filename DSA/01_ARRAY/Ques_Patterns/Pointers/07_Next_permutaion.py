# -------------------------------------------------------------
# Imports
# -------------------------------------------------------------
from typing import List


# -------------------------------------------------------------
# LeetCode 31: Next Permutation
# -------------------------------------------------------------
# Description:
# Rearrange numbers into the lexicographically next greater permutation.
# If no such arrangement exists (the array is in descending order),
# rearrange it as the lowest possible order (sorted ascending).
#
# Constraints:
# - 1 <= nums.length <= 100
# - 0 <= nums[i] <= 100
#
# The algorithm must:
# ✅ Modify nums in-place
# ✅ Use O(1) extra space
# ✅ Run in O(n) time
# -------------------------------------------------------------


# -------------------------------------------------------------
# 🔹 Approach: Single Pass from Right (Optimal O(n))
# -------------------------------------------------------------
# Logic:
# 1️⃣ Traverse from right to find the first decreasing element `i`
#     such that nums[i] < nums[i + 1].
# 2️⃣ If found, traverse again from the right to find the smallest
#     number greater than nums[i], and swap them.
# 3️⃣ Reverse the subarray nums[i+1:] to make it the next smallest order.
#
# Example:
# nums = [1, 2, 3]
# Step 1: i = 1 (nums[1]=2 < nums[2]=3)
# Step 2: Swap nums[1], nums[2] -> [1,3,2]
# Step 3: Reverse right part (none needed)
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to get the next lexicographical permutation.
        """
        n = len(nums)
        i = n - 2

        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If found, swap with next larger element from right
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the elements after i
        nums[i + 1 :] = reversed(nums[i + 1 :])


# -------------------------------------------------------------
# 🔹 Example Run
# -------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 3, 2], [2, 1, 3]),
        ([2, 3, 1], [3, 1, 2]),
    ]

    solver = Solution()
    for nums, expected in test_cases:
        nums_copy = nums.copy()
        solver.nextPermutation(nums_copy)
        print(f"Input: {nums} → Output: {nums_copy} | Expected: {expected}")
