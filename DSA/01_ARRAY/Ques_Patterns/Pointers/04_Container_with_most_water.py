# -------------------------------------------------------------
# Imports
# -------------------------------------------------------------
from typing import List


# -------------------------------------------------------------
# LeetCode 11: Container With Most Water
# -------------------------------------------------------------
# Description:
# Given an integer array `height` of length n representing the heights
# of vertical lines drawn at each index, find two lines that form a
# container that holds the most water.
#
# You may not slant the container.
#
# Constraints:
# - 2 <= n <= 10^5
# - 0 <= height[i] <= 10^4
# -------------------------------------------------------------


# -------------------------------------------------------------
# 🔹 Approach 1: Brute Force (O(n²))
# -------------------------------------------------------------
class SolutionBruteForce:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)

        return max_area


# -------------------------------------------------------------
# 🔹 Approach 2: Two Pointer (Optimal O(n))
# -------------------------------------------------------------
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)

            # Move pointer with smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# -------------------------------------------------------------
# 🔹 Example Run
# -------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]

    solver = Solution()
    for heights, expected in test_cases:
        result = solver.maxArea(heights)
        print(f"Input: {heights}\nOutput: {result} | Expected: {expected}\n")
