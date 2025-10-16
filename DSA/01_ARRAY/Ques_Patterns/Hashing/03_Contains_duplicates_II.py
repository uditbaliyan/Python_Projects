# -------------------------------------------------------------
# LeetCode 219: Contains Duplicate II
# -------------------------------------------------------------
# Question:
# Given an integer array nums and an integer k, return True if
# there are two distinct indices i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k.
#
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: True
#
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: True
#
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: False
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
# Key Points:
# - Need to check for duplicates that are "close" in index distance.
# - Difference from problem 217: we must also ensure abs(i - j) <= k.
# -------------------------------------------------------------

from collections import Counter


# -------------------------------------------------------------
# Approach 1: Brute Force
# Check every pair (i, j) where abs(i - j) <= k.
# Time Complexity: O(n * k)
# Space Complexity: O(1)
# -------------------------------------------------------------
class SolutionBruteForce:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                if nums[i] == nums[j]:
                    return True
        return False


# -------------------------------------------------------------
# Approach 2: HashMap (Optimized)
# Store each number's latest index.
# If we see the same number again and the distance <= k, return True.
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionHashMap:
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}
        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i
        return False


# -------------------------------------------------------------
# Approach 3: Sliding Window with HashSet
# Keep a set of at most k elements (the recent k numbers).
# If a number already exists in the set → duplicate within k distance.
# Time Complexity: O(n)
# Space Complexity: O(k)
# -------------------------------------------------------------
class SolutionSlidingWindow:
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False


# -------------------------------------------------------------
# Approach 4: Using Counter (Not efficient but for completeness)
# Use a counter on a sliding window of size k.
# Check duplicates within each window.
# Time Complexity: O(n * k)
# Space Complexity: O(k)
# -------------------------------------------------------------


class SolutionCounter:
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums)):
            window = nums[i + 1 : i + k + 1]
            count = Counter(window)
            if nums[i] in count:
                return True
        return False


# -------------------------------------------------------------
# Recommended: HashMap or Sliding Window (O(n))
# -------------------------------------------------------------
if __name__ == "__main__":
    nums1, k1 = [1, 2, 3, 1], 3
    nums2, k2 = [1, 0, 1, 1], 1
    nums3, k3 = [1, 2, 3, 1, 2, 3], 2

    print(SolutionBruteForce().containsNearbyDuplicate(nums1, k1))  # True
    print(SolutionHashMap().containsNearbyDuplicate(nums2, k2))  # True
    print(SolutionSlidingWindow().containsNearbyDuplicate(nums3, k3))  # False
    print(SolutionCounter().containsNearbyDuplicate(nums2, k2))  # True
