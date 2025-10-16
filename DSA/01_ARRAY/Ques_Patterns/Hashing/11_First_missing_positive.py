# -------------------------------------------------------------
# LeetCode 41: First Missing Positive
# -------------------------------------------------------------
# Question:
# Given an unsorted integer array nums, return the smallest positive
# integer that is missing from nums.
#
# Must run in O(n) time and O(1) auxiliary space.
#
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
#
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
#
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
#
# Constraints:
# - Use constant extra space (in-place)
# - Linear time → cannot sort
#
# Key Points:
# - Only positive integers in range [1, n] matter
# - Place each number at its "correct" index: num[i] -> index num[i]-1
# - After rearranging, first index i where nums[i] != i+1 gives missing
# -------------------------------------------------------------


# -------------------------------------------------------------
# Approach: Cyclic Sort / Index Placement
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] to its correct position
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # After rearrangement, first index i where nums[i] != i+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positions are correct, missing number is n+1
        return n + 1


# -------------------------------------------------------------
# Approach 2: Using Set (O(n) time, O(n) space)
# Only for understanding, not O(1) space
# -------------------------------------------------------------
class SolutionSet:
    def firstMissingPositive(self, nums):
        num_set = set(nums)
        n = len(nums)
        for i in range(1, n + 1):
            if i not in num_set:
                return i
        return n + 1


# -------------------------------------------------------------
# Recommended: Cyclic Sort (O(n) time, O(1) space)
# -------------------------------------------------------------
if __name__ == "__main__":
    nums1 = [1, 2, 0]
    nums2 = [3, 4, -1, 1]
    nums3 = [7, 8, 9, 11, 12]

    print(Solution().firstMissingPositive(nums1))  # 3
    print(Solution().firstMissingPositive(nums2))  # 2
    print(Solution().firstMissingPositive(nums3))  # 1

    print(SolutionSet().firstMissingPositive(nums1))  # 3
    print(SolutionSet().firstMissingPositive(nums2))  # 2
    print(SolutionSet().firstMissingPositive(nums3))  # 1
