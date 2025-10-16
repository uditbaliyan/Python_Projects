# -------------------------------------------------------------
# LeetCode 121: Best Time to Buy and Sell Stock
# -------------------------------------------------------------
# Question:
# Given an array prices where prices[i] is the stock price on day i,
# choose one day to buy and a later day to sell to maximize profit.
# Return the maximum profit. If no profit is possible, return 0.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy at 1 (day 2), sell at 6 (day 5), profit = 5
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: No profit possible
#
# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
#
# Key Points:
# - Only one buy-sell transaction allowed
# - Must buy before sell
# - Optimal solution in one pass (O(n) time, O(1) space)
# -------------------------------------------------------------


# -------------------------------------------------------------
# Approach 1: One Pass
# Idea:
# - Track minimum price so far
# - Compute profit = current price - min_price
# - Update max profit
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class Solution:
    def maxProfit(self, prices):
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


# -------------------------------------------------------------
# Approach 2: Brute Force (Optional)
# Idea:
# - Try every pair i < j
# - Compute profit = prices[j] - prices[i]
# - Update max profit
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# -------------------------------------------------------------
class SolutionBruteForce:
    def maxProfit(self, prices):
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit


# -------------------------------------------------------------
# Recommended: One Pass O(n) solution
# -------------------------------------------------------------
if __name__ == "__main__":
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]

    print(Solution().maxProfit(prices1))  # 5
    print(Solution().maxProfit(prices2))  # 0

    print(SolutionBruteForce().maxProfit(prices1))  # 5
    print(SolutionBruteForce().maxProfit(prices2))  # 0
