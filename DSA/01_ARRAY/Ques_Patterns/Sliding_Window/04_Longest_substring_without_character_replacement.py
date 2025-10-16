# -----------------------------------------------------------
# LeetCode 3. Longest Substring Without Repeating Characters
# -----------------------------------------------------------
# Problem:
# Given a string s, find the length of the longest substring
# without repeating characters.
#
# Example:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc" (length 3).
#
# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# -----------------------------------------------------------


# -----------------------------------------------------------
# 🧩 Approach 1: Brute Force (Inefficient)
# -----------------------------------------------------------
# - Generate all substrings.
# - Check each for duplicate characters.
# - Keep track of the longest valid substring.
#
# Time Complexity: O(n^3)
# Space Complexity: O(min(n, charset))
# -----------------------------------------------------------
def lengthOfLongestSubstring_bruteforce(s: str) -> int:
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i : j + 1]
            if len(set(substring)) == len(substring):  # No duplicates
                max_len = max(max_len, j - i + 1)
    return max_len


# -----------------------------------------------------------
# 🧩 Approach 2: Sliding Window + Set
# -----------------------------------------------------------
# - Use two pointers (left, right).
# - Use a set to store current window characters.
# - Move right pointer to expand window.
# - If duplicate found → move left pointer until duplicate removed.
#
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))
# -----------------------------------------------------------
def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    res = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        res = max(res, right - left + 1)

    return res


# -----------------------------------------------------------
# 🧩 Approach 3: Sliding Window + HashMap (Index Tracking)
# -----------------------------------------------------------
# - Store each character’s most recent index.
# - If duplicate found, shift left pointer to max(left, last_seen[ch] + 1)
# - Ensures O(n) time by skipping useless iterations.
#
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))
# -----------------------------------------------------------
def lengthOfLongestSubstring_optimized(s: str) -> int:
    last_seen = {}
    left = 0
    res = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        res = max(res, right - left + 1)

    return res


# -----------------------------------------------------------
# ✅ Test Cases
# -----------------------------------------------------------
if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("dvdf", 3),
        ("abba", 2),
        ("tmmzuxt", 5),
    ]

    print("Testing Longest Substring Without Repeating Characters:\n")
    for s, expected in tests:
        result = lengthOfLongestSubstring_optimized(s)
        print(f"Input: '{s}' | Output: {result} | Expected: {expected}")
        print("-" * 50)
