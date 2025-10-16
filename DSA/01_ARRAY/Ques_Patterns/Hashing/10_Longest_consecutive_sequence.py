# -------------------------------------------------------------
# LeetCode 128: Longest Consecutive Sequence
# -------------------------------------------------------------
# Question:
# Given an unsorted array of integers nums, return the length of
# the longest consecutive elements sequence.
# Must run in O(n) time.
#
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive sequence is [1,2,3,4]
#
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3
#
# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
# Key Points:
# - O(n) time → cannot sort
# - Use a set to quickly check for consecutive numbers
# -------------------------------------------------------------


# -------------------------------------------------------------
# Approach 1: HashSet to find sequence starts
# Idea:
# - Put all numbers in a set
# - For each number, if num-1 not in set → it's a sequence start
# - Count consecutive numbers from that start
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest


# -------------------------------------------------------------
# Approach 2: Union-Find (Optional)
# Idea:
# - Each consecutive number belongs to the same set
# - Count size of sets
# Time Complexity: O(n α(n)) with path compression
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionUnionFind:
    def longestConsecutive(self, nums):
        parent = {}
        size = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
                size[root_x] += size[root_y]

        # Initialize
        for num in nums:
            parent[num] = num
            size[num] = 1

        # Union consecutive numbers
        for num in nums:
            if num + 1 in parent:
                union(num, num + 1)

        return max(size.values(), default=0)


# -------------------------------------------------------------
# Recommended: HashSet approach (simple and O(n))
# -------------------------------------------------------------
if __name__ == "__main__":
    nums1 = [100, 4, 200, 1, 3, 2]
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    nums3 = [1, 0, 1, 2]

    print(Solution().longestConsecutive(nums1))  # 4
    print(Solution().longestConsecutive(nums2))  # 9
    print(Solution().longestConsecutive(nums3))  # 3

    print(SolutionUnionFind().longestConsecutive(nums1))  # 4
    print(SolutionUnionFind().longestConsecutive(nums2))  # 9
    print(SolutionUnionFind().longestConsecutive(nums3))  # 3
