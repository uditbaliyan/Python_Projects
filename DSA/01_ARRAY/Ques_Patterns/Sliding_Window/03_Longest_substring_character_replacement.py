# -----------------------------------------------------------
# LeetCode 424. Longest Repeating Character Replacement
# -----------------------------------------------------------
# Problem:
# You are given a string s and an integer k.
# You can choose any character of the string and change it to
# any other uppercase English character at most k times.
#
# Return the length of the longest substring containing the same
# letter you can get after performing the above operations.
#
# Example:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace one 'A' with 'B' -> "AABBBBA", longest = "BBBB"
#
# Constraints:
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# -----------------------------------------------------------

from collections import defaultdict


# -----------------------------------------------------------
# 🧩 Approach 1: Brute Force (Inefficient)
# -----------------------------------------------------------
# - For each substring, count frequency of each char.
# - Compute how many replacements needed: len(sub) - max_freq
# - If <= k, track maximum length.
#
# Time Complexity: O(n^3)
# Space Complexity: O(1)
# Not suitable for large input (used for concept understanding only).
# -----------------------------------------------------------
def characterReplacement_bruteforce(s: str, k: int) -> int:
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i : j + 1]
            freq = [0] * 26
            for ch in sub:
                freq[ord(ch) - ord("A")] += 1
            maxf = max(freq)
            if len(sub) - maxf <= k:
                res = max(res, len(sub))
    return res


# -----------------------------------------------------------
# 🧩 Approach 2: Sliding Window + Frequency Count (Optimal)
# -----------------------------------------------------------
# Idea:
# - Maintain a sliding window [left, right]
# - Track counts of characters in the window
# - Keep track of the most frequent character count (max_freq)
# - If (window_size - max_freq) > k ⇒ shrink window from left
#
# The trick:
# Even if max_freq isn't updated when the left shrinks,
# the result remains valid since max_freq only ever increases.
#
# Time Complexity: O(n)
# Space Complexity: O(1)  (26 characters only)
# -----------------------------------------------------------
def characterReplacement(s: str, k: int) -> int:
    count = defaultdict(int)
    left = 0
    max_freq = 0
    res = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        # If replacements needed > k → shrink window
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


# -----------------------------------------------------------
# ✅ Test Cases
# -----------------------------------------------------------
if __name__ == "__main__":
    tests = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("ABCDEF", 1, 2),
        ("BAAAB", 2, 5),
    ]

    for s, k, expected in tests:
        print(f"Input: s='{s}', k={k}")
        result = characterReplacement(s, k)
        print(f"Output: {result}  |  Expected: {expected}")
        print("-" * 40)
