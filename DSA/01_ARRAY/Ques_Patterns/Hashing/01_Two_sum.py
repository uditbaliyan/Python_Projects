# -------------------------------------------------------------
# LeetCode 1: Two Sum
# -------------------------------------------------------------
# Question:
# Given an array of integers nums and an integer target, return
# indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# Return the answer in any order.
#
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
#
# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
# Key Points:
# - Find indices (not values).
# - Only one unique pair exists.
# - Optimize from O(n^2) to O(n).
# -------------------------------------------------------------

from itertools import permutations


# -------------------------------------------------------------
# Approach 1: Brute Force (Nested Loops)
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# -------------------------------------------------------------
class SolutionBruteForce:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# -------------------------------------------------------------
# Approach 2: Using itertools.permutations
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# -------------------------------------------------------------


class SolutionPermutations:
    def twoSum(self, nums, target):
        for a, b in permutations(range(len(nums)), 2):
            if nums[a] + nums[b] == target:
                return [a, b]


# -------------------------------------------------------------
# Approach 3: Hash Map (Optimized Linear Solution)
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionHashMap:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


# -------------------------------------------------------------
# Approach 4: Two Pointer (For Sorted Arrays Only)
# Time Complexity: O(n log n)  [due to sorting]
# Space Complexity: O(n)
# Note: Works only if the array is sorted or you sort it manually.
# -------------------------------------------------------------
class SolutionTwoPointer:
    def twoSum(self, nums, target):
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()
        left, right = 0, len(arr) - 1

        while left < right:
            s = arr[left][0] + arr[right][0]
            if s == target:
                return [arr[left][1], arr[right][1]]
            elif s < target:
                left += 1
            else:
                right -= 1


# -------------------------------------------------------------
# Recommended: Hash Map approach (SolutionHashMap)
# -------------------------------------------------------------
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(SolutionBruteForce().twoSum(nums, target))
    print(SolutionPermutations().twoSum(nums, target))
    print(SolutionHashMap().twoSum(nums, target))
    print(SolutionTwoPointer().twoSum(nums, target))
