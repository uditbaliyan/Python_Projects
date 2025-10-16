# -----------------------------------------------------------
# LeetCode 209. Minimum Size Subarray Sum
# -----------------------------------------------------------
# Problem:
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is >= target.
# Return 0 if no such subarray exists.
#
# Example:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has minimal length.
#
# Constraints:
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# -----------------------------------------------------------

from typing import List
import bisect
import math


# -----------------------------------------------------------
# 🧩 Approach 1: Sliding Window (Optimal)
# -----------------------------------------------------------
# - Keep two pointers (start, end) and a running sum.
# - Expand end until sum >= target.
# - Shrink start to minimize window while sum >= target.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------------
def minSubArrayLen_sliding_window(target: int, nums: List[int]) -> int:
    n = len(nums)
    min_len = math.inf
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += nums[end]
        while current_sum >= target:
            min_len = min(min_len, end - start + 1)
            current_sum -= nums[start]
            start += 1

    return min_len if min_len != math.inf else 0


# -----------------------------------------------------------
# 🧩 Approach 2: Prefix Sum + Binary Search
# -----------------------------------------------------------
# - Compute prefix sum array.
# - For each start index, find minimal end using binary search.
# - Time Complexity: O(n log n)
# - Space Complexity: O(n)
# -----------------------------------------------------------
def minSubArrayLen_binary_search(target: int, nums: List[int]) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    min_len = math.inf
    for i in range(n):
        # Find smallest j such that prefix_sum[j] - prefix_sum[i] >= target
        desired = target + prefix_sum[i]
        j = bisect.bisect_left(prefix_sum, desired)
        if j <= n:
            min_len = min(min_len, j - i)

    return min_len if min_len != math.inf else 0


# -----------------------------------------------------------
# ✅ Test Cases
# -----------------------------------------------------------
if __name__ == "__main__":
    tests = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (15, [1, 2, 3, 4, 5], 5),
        (3, [1, 1], 2),
        (100, [1, 2, 3, 4, 5], 0),
    ]

    print("Testing Minimum Size Subarray Sum:\n")
    for target, nums, expected in tests:
        result = minSubArrayLen_sliding_window(target, nums)
        print(f"target = {target}, nums = {nums}")
        print(f"Output (Sliding Window):   {result}")
        result_bs = minSubArrayLen_binary_search(target, nums)
        print(f"Output (Binary Search):    {result_bs}")
        print(f"Expected:                  {expected}")
        print("-" * 50)
