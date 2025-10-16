# -------------------------------------------------------------
# LeetCode 238: Product of Array Except Self
# -------------------------------------------------------------
# Question:
# Given an integer array nums, return an array `answer` such that
# answer[i] = product of all elements of nums except nums[i].
#
# You must solve it in O(n) time without using the division operator.
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
# Constraints:
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product fits in a 32-bit integer.
#
# Follow up:
# Solve in O(1) extra space (output array doesn’t count as extra).
#
# Key Points:
# - No division allowed.
# - Need prefix and suffix products for each index.
# -------------------------------------------------------------

import math


# -------------------------------------------------------------
# Approach 1: Prefix and Suffix Arrays (O(n) space)
# Idea:
# - Compute prefix[i] = product of nums[0..i-1]
# - Compute suffix[i] = product of nums[i+1..n-1]
# - answer[i] = prefix[i] * suffix[i]
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionPrefixSuffix:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        ans = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            ans[i] = prefix[i] * suffix[i]

        return ans


# -------------------------------------------------------------
# Approach 2: Optimized Space Using One Array (O(1) extra space)
# Idea:
# - Use the output array to store prefix products first.
# - Then iterate backward while maintaining a running suffix product.
# - Multiply current prefix (in ans) by the suffix product.
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output array)
# -------------------------------------------------------------
class SolutionOptimized:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        # Step 1: Build prefix product
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # Step 2: Multiply with suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


# -------------------------------------------------------------
# Approach 3: Using math.prod with slicing (not allowed in interviews)
# Idea:
# - Brute force O(n²): recompute product excluding index i.
# - Only for understanding, not optimal.
# Time Complexity: O(n²)
# Space Complexity: O(1)
# -------------------------------------------------------------


class SolutionBruteForce:
    def productExceptSelf(self, nums):
        ans = []
        for i in range(len(nums)):
            temp = nums[:i] + nums[i + 1 :]
            ans.append(math.prod(temp))
        return ans


# -------------------------------------------------------------
# Recommended: SolutionOptimized (O(n) time, O(1) space)
# -------------------------------------------------------------
if __name__ == "__main__":
    nums1 = [1, 2, 3, 4]
    nums2 = [-1, 1, 0, -3, 3]

    print(SolutionPrefixSuffix().productExceptSelf(nums1))
    print(SolutionOptimized().productExceptSelf(nums1))
    print(SolutionBruteForce().productExceptSelf(nums2))
