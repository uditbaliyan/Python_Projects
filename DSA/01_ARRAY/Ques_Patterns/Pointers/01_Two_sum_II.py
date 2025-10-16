# -------------------------------------------------------------
# LeetCode 167: Two Sum II - Input Array Is Sorted
# -------------------------------------------------------------
# Question:
# Given a 1-indexed array of integers 'numbers' sorted in non-decreasing order,
# find two numbers such that they add up to a target.
# Return the indices [index1, index2] (1-based) of the two numbers.
#
# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
#
# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
#
# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
#
# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order
# Exactly one solution exists
# Must use constant extra space
#
# Key Points:
# - Array is sorted → can use two pointers approach
# - Time Complexity: O(n)
# - Space Complexity: O(1)
# -------------------------------------------------------------

import bisect


# -------------------------------------------------------------
# Approach 1: Two Pointers
# Idea:
# - Start with left = 0, right = n-1
# - Compute current_sum = numbers[left] + numbers[right]
# - If sum == target → return [left+1, right+1]
# - If sum < target → move left pointer right
# - If sum > target → move right pointer left
# -------------------------------------------------------------
class SolutionTwoPointers:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []  # Not needed, as problem guarantees a solution


# -------------------------------------------------------------
# Approach 2: Binary Search (Optional)
# Idea:
# - For each number, search for complement = target - numbers[i] using binary search
# - Time Complexity: O(n log n)
# - Space Complexity: O(1)
# -------------------------------------------------------------


class SolutionBinarySearch:
    def twoSum(self, numbers, target):
        for i, num in enumerate(numbers):
            complement = target - num
            # search in numbers[i+1:]
            idx = bisect.bisect_left(numbers, complement, i + 1)
            if idx < len(numbers) and numbers[idx] == complement:
                return [i + 1, idx + 1]
        return []


# -------------------------------------------------------------
# Recommended: Two Pointers (O(n) time, O(1) space)
# -------------------------------------------------------------
if __name__ == "__main__":
    numbers1, target1 = [2, 7, 11, 15], 9
    numbers2, target2 = [2, 3, 4], 6
    numbers3, target3 = [-1, 0], -1

    print(SolutionTwoPointers().twoSum(numbers1, target1))  # [1,2]
    print(SolutionTwoPointers().twoSum(numbers2, target2))  # [1,3]
    print(SolutionTwoPointers().twoSum(numbers3, target3))  # [1,2]

    print(SolutionBinarySearch().twoSum(numbers1, target1))  # [1,2]
    print(SolutionBinarySearch().twoSum(numbers2, target2))  # [1,3]
    print(SolutionBinarySearch().twoSum(numbers3, target3))  # [1,2]
