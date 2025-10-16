# -------------------------------------------------------------
# LeetCode 347: Top K Frequent Elements
# -------------------------------------------------------------
# Question:
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in [1, number of unique elements]
# Answer is guaranteed to be unique.
#
# Follow-up:
# Must achieve better than O(n log n) time complexity.
#
# Key Points:
# - Count frequency of elements.
# - We can solve this using:
#   1. Sorting (O(n log n))
#   2. Heap (O(n log k))
#   3. Bucket sort (O(n)) → optimal
# -------------------------------------------------------------


from collections import Counter
import heapq


# -------------------------------------------------------------
# Approach 1: Sorting by Frequency (Simple)
# Idea:
# Use Counter to count frequencies, sort by count descending, and take top k.
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionSorting:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        return [
            num
            for num, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]
        ]


# -------------------------------------------------------------
# Approach 2: Heap (Min-Heap of Size k)
# Idea:
# Use a heap to store top k frequent elements.
# Time Complexity: O(n log k)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionHeap:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]


# -------------------------------------------------------------
# Approach 3: Bucket Sort (O(n)) — Optimal
# Idea:
# - Create buckets where index = frequency.
# - Append numbers to the bucket corresponding to their frequency.
# - Traverse buckets in reverse order to collect top k.
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionBucketSort:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        max_freq = max(freq.values())

        buckets = [[] for _ in range(max_freq + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        res = []
        for i in range(max_freq, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


# -------------------------------------------------------------
# Recommended: Bucket Sort (O(n)) – Best for large input
# -------------------------------------------------------------
if __name__ == "__main__":
    nums1 = [1, 1, 1, 2, 2, 3]
    nums2 = [1]
    nums3 = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k1, k2, k3 = 2, 1, 2

    print(SolutionSorting().topKFrequent(nums1, k1))  # [1, 2]
    print(SolutionHeap().topKFrequent(nums1, k1))  # [1, 2]
    print(SolutionBucketSort().topKFrequent(nums3, k3))  # [1, 2]
