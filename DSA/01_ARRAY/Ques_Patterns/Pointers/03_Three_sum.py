# -------------------------------------------------------------
# LeetCode 15: 3Sum
# -------------------------------------------------------------
# Question:
# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
# such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
# The solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = [0,1,1]
# Output: []
#
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
#
# Constraints:
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
# Key Points:
# - Avoid duplicates
# - Sorted array helps using two pointers approach
# - Time Complexity: O(n^2)
# - Space Complexity: O(1) extra (not counting output)
# -------------------------------------------------------------


# -------------------------------------------------------------
# Approach: Sorting + Two Pointers
# Idea:
# - Sort nums
# - For each nums[i], use two pointers left=i+1, right=n-1
# - Move pointers to find sums equal to 0
# - Skip duplicates
# -------------------------------------------------------------
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates for i

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res


# -------------------------------------------------------------
# Recommended: Sorting + Two Pointers (O(n^2) time, O(1) extra space)
# -------------------------------------------------------------
if __name__ == "__main__":
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = [0, 1, 1]
    nums3 = [0, 0, 0]

    print(Solution().threeSum(nums1))  # [[-1,-1,2],[-1,0,1]]
    print(Solution().threeSum(nums2))  # []
    print(Solution().threeSum(nums3))  # [[0,0,0]]
