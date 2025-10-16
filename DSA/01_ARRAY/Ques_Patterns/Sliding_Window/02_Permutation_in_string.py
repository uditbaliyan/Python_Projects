# -------------------------------------------------------------
# LeetCode 567: Permutation in String
# -------------------------------------------------------------
# Question:
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# otherwise return false. A permutation is any rearrangement of s1's characters.
#
# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains "ba", which is a permutation of s1
#
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: False
#
# Constraints:
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters
#
# Key Points:
# - Sliding window of size len(s1) over s2
# - Compare character counts efficiently
# - Time Complexity: O(n)
# - Space Complexity: O(26) ~ O(1)
# -------------------------------------------------------------


# -------------------------------------------------------------
# Approach: Sliding Window + Count Array
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        count1 = Counter(s1)
        count2 = Counter(s2[:len1])

        if count1 == count2:
            return True

        for i in range(len1, len2):
            count2[s2[i]] += 1
            count2[s2[i - len1]] -= 1
            if count2[s2[i - len1]] == 0:
                del count2[s2[i - len1]]
            if count1 == count2:
                return True

        return False


# -------------------------------------------------------------
# Alternative: Using fixed-size array instead of Counter
# -------------------------------------------------------------
class SolutionArray:
    def checkInclusion(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len1):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        for i in range(len2 - len1):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[i]) - ord("a")] -= 1
            s2_count[ord(s2[i + len1]) - ord("a")] += 1

        return s1_count == s2_count


# -------------------------------------------------------------
# Recommended: Sliding Window with Counter or array (O(n) time)
# -------------------------------------------------------------
if __name__ == "__main__":
    s1_1, s2_1 = "ab", "eidbaooo"
    s1_2, s2_2 = "ab", "eidboaoo"

    print(Solution().checkInclusion(s1_1, s2_1))  # True
    print(Solution().checkInclusion(s1_2, s2_2))  # False

    print(SolutionArray().checkInclusion(s1_1, s2_1))  # True
    print(SolutionArray().checkInclusion(s1_2, s2_2))  # False
