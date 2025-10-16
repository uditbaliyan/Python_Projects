# -------------------------------------------------------------
# Imports
# -------------------------------------------------------------
from typing import List


# -------------------------------------------------------------
# LeetCode 42: Trapping Rain Water
# -------------------------------------------------------------
# Description:
# Given n non-negative integers representing an elevation map where
# the width of each bar is 1, compute how much water it can trap after raining.
#
# Constraints:
# - 1 <= n <= 2 * 10^4
# - 0 <= height[i] <= 10^5
# -------------------------------------------------------------


# -------------------------------------------------------------
# 🔹 Approach 1: Brute Force (O(n²))
# -------------------------------------------------------------
# For each element, find the maximum height to its left and right,
# then take the min(left_max, right_max) - height[i] as trapped water.
class SolutionBruteForce:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0

        for i in range(n):
            left_max = max(height[: i + 1])
            right_max = max(height[i:])
            water += min(left_max, right_max) - height[i]

        return water


# -------------------------------------------------------------
# 🔹 Approach 2: Dynamic Programming (O(n) Time, O(n) Space)
# -------------------------------------------------------------
# Precompute left_max and right_max arrays to avoid recalculating.
class SolutionDP:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water


# -------------------------------------------------------------
# 🔹 Approach 3: Two Pointers (Optimal O(n) Time, O(1) Space)
# -------------------------------------------------------------
# Move inward from both sides, maintaining left_max and right_max.
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


# -------------------------------------------------------------
# 🔹 Example Run
# -------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 0, 2, 1, 0, 1, 3], 5),
        ([2, 0, 2], 2),
    ]

    solver = Solution()
    for heights, expected in test_cases:
        result = solver.trap(heights)
        print(f"Input: {heights}\nOutput: {result} | Expected: {expected}\n")
