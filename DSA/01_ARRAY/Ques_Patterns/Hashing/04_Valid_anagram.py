# -------------------------------------------------------------
# LeetCode 242: Valid Anagram
# -------------------------------------------------------------
# Question:
# Given two strings s and t, return True if t is an anagram of s,
# and False otherwise.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: True
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: False
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
# Follow-up:
# What if the inputs contain Unicode characters?
# (Hint: use a dictionary or Counter to handle arbitrary characters.)
#
# Key Points:
# - Two strings are anagrams if they contain the same characters
#   with the same frequencies.
# - Several ways to solve: sorting, counting, hashmap, etc.
# -------------------------------------------------------------

from collections import Counter


# -------------------------------------------------------------
# Approach 1: Sorting
# Idea:
# If two strings are anagrams, sorting them will make them identical.
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sorting implementation.
# -------------------------------------------------------------
class SolutionSorting:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


# -------------------------------------------------------------
# Approach 2: Hash Map (Manual Frequency Count)
# Idea:
# Count frequency of each character in both strings and compare.
# Time Complexity: O(n)
# Space Complexity: O(1) [only 26 lowercase letters]
# -------------------------------------------------------------
class SolutionHashMap:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}

        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        return freq_s == freq_t


# -------------------------------------------------------------
# Approach 3: Using Counter from collections
# Idea:
# Counter automatically counts characters; compare directly.
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------


class SolutionCounter:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


# -------------------------------------------------------------
# Approach 4: Using Array (Optimized for lowercase English letters)
# Idea:
# Since only 'a' to 'z' are present, use an array of length 26.
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class SolutionArrayCount:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1
        for ch in t:
            count[ord(ch) - ord("a")] -= 1

        return all(c == 0 for c in count)


# -------------------------------------------------------------
# Approach 5: Unicode Support (Generalized version)
# Idea:
# Use Counter or a dictionary that can handle any Unicode characters.
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionUnicode:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True


# -------------------------------------------------------------
# Recommended: Counter or Array approach (O(n))
# -------------------------------------------------------------
if __name__ == "__main__":
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"

    print(SolutionSorting().isAnagram(s1, t1))  # True
    print(SolutionHashMap().isAnagram(s1, t2))  # False
    print(SolutionCounter().isAnagram(s1, t1))  # True
    print(SolutionArrayCount().isAnagram(s1, t1))  # True
    print(SolutionUnicode().isAnagram(s2, t2))  # False
