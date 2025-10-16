# -------------------------------------------------------------
# LeetCode 49: Group Anagrams
# -------------------------------------------------------------
# Question:
# Given an array of strings `strs`, group the anagrams together.
# You can return the answer in any order.
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
# Key Points:
# - Strings are anagrams if they have identical character counts.
# - We must group words with the same character frequency pattern.
# - Common ways:
#   1. Sort the string → use as a key.
#   2. Use character frequency tuple (O(26 * n)).
# -------------------------------------------------------------


# -------------------------------------------------------------
# Approach 1: Sorting Based Key
# Idea:
# Sort each word — all anagrams become identical after sorting.
# Use sorted string as key in a dictionary.
# Time Complexity: O(N * K log K)
# Space Complexity: O(N * K)
# -------------------------------------------------------------
from collections import defaultdict

from collections import Counter


class SolutionSorting:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())


# -------------------------------------------------------------
# Approach 2: Character Frequency Tuple Key
# Idea:
# Instead of sorting (O(K log K)), we use a frequency count of 26 letters.
# Each word is represented by a 26-length tuple of counts.
# Time Complexity: O(N * K)
# Space Complexity: O(N)
# -------------------------------------------------------------
class SolutionCharCount:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            anagrams[tuple(count)].append(word)
        return list(anagrams.values())


# -------------------------------------------------------------
# Approach 3: Using Counter as Key (less efficient)
# Idea:
# Use collections.Counter for each word, convert to tuple to make hashable.
# Time Complexity: O(N * K)
# Space Complexity: O(N * K)
# -------------------------------------------------------------


class SolutionCounter:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            anagrams[key].append(word)
        return list(anagrams.values())


# -------------------------------------------------------------
# Recommended: Character Count approach (fastest)
# -------------------------------------------------------------
if __name__ == "__main__":
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs2 = [""]
    strs3 = ["a"]

    print(SolutionSorting().groupAnagrams(strs1))
    print(SolutionCharCount().groupAnagrams(strs1))
    print(SolutionCounter().groupAnagrams(strs1))
    print(SolutionSorting().groupAnagrams(strs2))
    print(SolutionCharCount().groupAnagrams(strs3))
