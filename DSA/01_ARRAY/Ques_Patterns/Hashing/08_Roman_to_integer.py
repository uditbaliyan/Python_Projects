# -------------------------------------------------------------
# LeetCode 13: Roman to Integer
# -------------------------------------------------------------
# Question:
# Given a Roman numeral string s, convert it to an integer.
#
# Roman numerals symbols:
# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
# Subtractive notation:
# - I before V or X → 4, 9
# - X before L or C → 40, 90
# - C before D or M → 400, 900
#
# Example 1:
# Input: s = "III"
# Output: 3
#
# Example 2:
# Input: s = "LVIII"
# Output: 58
#
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
#
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters I, V, X, L, C, D, M
# s is guaranteed to be a valid Roman numeral in range [1,3999]
#
# Key Points:
# - Use a mapping of characters to values
# - Iterate left to right: if current < next, subtract; else add
# -------------------------------------------------------------


# -------------------------------------------------------------
# Approach 1: Left to Right with Subtraction Rule
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class Solution:
    def romanToInt(self, s):
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        n = len(s)
        for i in range(n):
            value = roman_map[s[i]]
            # If next numeral is larger, subtract current
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= value
            else:
                total += value
        return total


# -------------------------------------------------------------
# Alternative Approach 2: Right to Left
# Idea:
# Iterate from right to left, add value if >= previous, else subtract
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class SolutionRightToLeft:
    def romanToInt(self, s):
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        prev_value = 0
        for ch in reversed(s):
            value = roman_map[ch]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total


# -------------------------------------------------------------
# Recommended: Either approach is O(n) and efficient
# -------------------------------------------------------------
if __name__ == "__main__":
    s1 = "III"
    s2 = "LVIII"
    s3 = "MCMXCIV"

    print(Solution().romanToInt(s1))  # 3
    print(Solution().romanToInt(s2))  # 58
    print(Solution().romanToInt(s3))  # 1994

    print(SolutionRightToLeft().romanToInt(s1))  # 3
    print(SolutionRightToLeft().romanToInt(s2))  # 58
    print(SolutionRightToLeft().romanToInt(s3))  # 1994
