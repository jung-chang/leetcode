# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List


class Solution:
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        [7,1,5,3,6,4]
        buy at 1, sell at 5
        buy at 3, sell at 6
        max = 7

        Iterate through prices. Buy each day, if next day is less, sell on current day.
        [7] max_profit0, min_buy=7
        [7 1], max=0, min=1
        [7 1 5], max=4, min=1
        [7 1 5 3 6 4], max=4, min=1

        [1 2 2 3 3 20]

        max at i is max i-1 + profit at i/i-1

        """
        dp = [0]
        i = 1
        while i < len(prices):
            profit = 0
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            dp.append(dp[i - 1] + profit)
            i += 1
        print(dp)
        return dp[-1]


print(Solution().maxProfit([1, 2, 2, 3, 3, 20]))
