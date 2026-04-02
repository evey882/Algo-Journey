"""
Best Time to Buy and Sell Stock - LeetCode Easy
Day 3 of 10,950 | April 2, 2026

Problem:
You are given an array prices where prices[i] is the price of a given stock on the
ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

# ============================================
# APPROACH
# ============================================
# Grab the min price, so far and compare it with the highest value seen post selection to get max profit
# decreasing values will result in zero, there has to be an increase somewhere
#
# Brute Force:
# - Nested loop, compared each value with the other and calculates the max profit when the larger
# - value is found
# - Time: O(n^2)
# - Space: O(1)
#
# Optimized:
# - Grabs the smallest value and if the following values are greater, compares for the max profit
# - and returns the max earnings
# - Time: O(n)
# - Space: O(1)
#
# ============================================

from typing import List

def maxProfit(prices: List[int]) -> int:
    """
    Calculates the maximum profit of buying a stock one day,
    and selling it another. Based on changing stock prices.
    Does this in one pass, using constant variables.
    """
    min_cost = float("inf")
    max_profit = 0

    for stock in prices:
        if stock < min_cost: min_cost = stock

        max_profit = max(stock - min_cost, max_profit)
    return max_profit


# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    # Test 1: Example from problem
    assert maxProfit([7,1,5,3,6,4]) == 5

    # Test 2: Example from problem
    assert maxProfit([7,6,4,3,1]) == 0

    # Test 3: Edge case - [One price in array]
    assert maxProfit([20]) == 0

    print("All tests passed! ✅")