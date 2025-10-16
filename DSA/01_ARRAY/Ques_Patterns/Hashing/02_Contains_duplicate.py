# -------------------------------------------------------------
# LeetCode 217: Contains Duplicate
# -------------------------------------------------------------
# Question:
# Given an integer array nums, return True if any value appears
# at least twice in the array, and return False if every element
# is distinct.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: True
# Explanation: The element 1 occurs twice.
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: False
# Explanation: All elements are distinct.
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
# Key Points:
# - Need to detect duplicates efficiently.
# - Brute-force gives O(n^2), optimized approaches can do O(n log n) or O(n).
# -------------------------------------------------------------


from collections import Counter


# -------------------------------------------------------------
# Approach 1: Brute Force (Nested Loops)
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# -------------------------------------------------------------
class SolutionBruteForce:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# -------------------------------------------------------------
# Approach 2: Using Sorting
# Idea: Sort the array; if any two adjacent elements are equal,
#       there's a duplicate.
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sorting implementation.
# -------------------------------------------------------------
class SolutionSorting:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


# -------------------------------------------------------------
# Approach 3: Using HashSet (Optimized)
# Idea: Keep inserting elements into a set.
#       If an element already exists, return True.
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionHashSet:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# -------------------------------------------------------------
# Approach 4: Using Length Comparison Trick
# Idea: Convert nums into a set (which removes duplicates).
#       If length changes, duplicates exist.
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionSetLength:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


# -------------------------------------------------------------
# Approach 5: Using Counter from collections
# Idea: Use Counter to count occurrences.
#       If any count > 1, return True.
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------


class SolutionCounter:
    def containsDuplicate(self, nums):
        freq = Counter(nums)
        for count in freq.values():
            if count > 1:
                return True
        return False


# -------------------------------------------------------------
# Recommended: HashSet or Set-Length approach (O(n))
# -------------------------------------------------------------
if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    print(SolutionBruteForce().containsDuplicate(nums1))  # True
    print(SolutionSorting().containsDuplicate(nums2))  # False
    print(SolutionHashSet().containsDuplicate(nums3))  # True
    print(SolutionSetLength().containsDuplicate(nums3))  # True
    print(SolutionCounter().containsDuplicate(nums2))  # False
