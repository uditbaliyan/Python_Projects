# -------------------------------------------------------------
# LeetCode 953: Verifying an Alien Dictionary
# -------------------------------------------------------------
# Question:
# In an alien language, lowercase letters may have a different order.
# Given a list of words and the order of the alien alphabet, determine
# if the words are sorted lexicographically according to this order.
#
# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: True
#
# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: False
#
# Example 3:
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: False
#
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters are lowercase English letters.
#
# Key Points:
# - Map each character to its index in the alien order.
# - Compare each consecutive pair of words.
# - Handle prefix case: "apple" > "app" because longer word comes after prefix.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Approach 1: Direct Comparison Using Mapping
# Time Complexity: O(n * k) where n = number of words, k = average word length
# Space Complexity: O(26) ~ O(1)
# -------------------------------------------------------------
class Solution:
    def isAlienSorted(self, words, order):
        # Map character to its order index
        order_index = {char: i for i, char in enumerate(order)}

        def in_correct_order(word1, word2):
            for c1, c2 in zip(word1, word2):
                if order_index[c1] < order_index[c2]:
                    return True
                elif order_index[c1] > order_index[c2]:
                    return False
            # If all characters so far are equal, shorter word should come first
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not in_correct_order(words[i], words[i + 1]):
                return False
        return True


# -------------------------------------------------------------
# Approach 2: Transform words to indices and compare
# Idea:
# Convert each word into a list of indices according to order
# Compare lists lexicographically
# Time Complexity: O(n * k)
# Space Complexity: O(n * k)
# -------------------------------------------------------------
class SolutionTransform:
    def isAlienSorted(self, words, order):
        order_index = {char: i for i, char in enumerate(order)}
        words_transformed = [[order_index[c] for c in word] for word in words]
        return all(
            words_transformed[i] <= words_transformed[i + 1]
            for i in range(len(words) - 1)
        )


# -------------------------------------------------------------
# Recommended: Approach 1 (Direct comparison) is simple and efficient
# -------------------------------------------------------------
if __name__ == "__main__":
    words1 = ["hello", "leetcode"]
    order1 = "hlabcdefgijkmnopqrstuvwxyz"
    words2 = ["word", "world", "row"]
    order2 = "worldabcefghijkmnpqstuvxyz"
    words3 = ["apple", "app"]
    order3 = "abcdefghijklmnopqrstuvwxyz"

    print(Solution().isAlienSorted(words1, order1))  # True
    print(Solution().isAlienSorted(words2, order2))  # False
    print(Solution().isAlienSorted(words3, order3))  # False

    print(SolutionTransform().isAlienSorted(words1, order1))  # True
    print(SolutionTransform().isAlienSorted(words2, order2))  # False
    print(SolutionTransform().isAlienSorted(words3, order3))  # False
