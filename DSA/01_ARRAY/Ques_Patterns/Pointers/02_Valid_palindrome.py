# -------------------------------------------------------------
# LeetCode 125: Valid Palindrome
# -------------------------------------------------------------
# Question:
# Given a string s, determine if it is a palindrome considering:
# - Ignore case (treat uppercase as lowercase)
# - Ignore non-alphanumeric characters
#
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
#
# Example 2:
# Input: s = "race a car"
# Output: False
#
# Example 3:
# Input: s = " "
# Output: True
#
# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists of printable ASCII characters
#
# Key Points:
# - Use two pointers to compare characters from both ends
# - Skip non-alphanumeric characters
# - Case-insensitive comparison
# -------------------------------------------------------------


# -------------------------------------------------------------
# Approach 1: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class SolutionTwoPointers:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            # Move left pointer to next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# -------------------------------------------------------------
# Approach 2: Clean and Compare
# Idea:
# - Remove all non-alphanumeric characters and lowercase
# - Compare string with its reverse
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class SolutionClean:
    def isPalindrome(self, s):
        filtered = "".join(c.lower() for c in s if c.isalnum())
        return filtered == filtered[::-1]


# -------------------------------------------------------------
# Recommended: Two Pointers (O(1) space)
# -------------------------------------------------------------
if __name__ == "__main__":
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = " "

    print(SolutionTwoPointers().isPalindrome(s1))  # True
    print(SolutionTwoPointers().isPalindrome(s2))  # False
    print(SolutionTwoPointers().isPalindrome(s3))  # True

    print(SolutionClean().isPalindrome(s1))  # True
    print(SolutionClean().isPalindrome(s2))  # False
    print(SolutionClean().isPalindrome(s3))  # True
