# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """

    def first(self, prices: List[int]) -> int:
        """
        Can brute force it in O(n^2).

        Keep track of min price and max price.
        """
        # [7,1,5,3,6,4]
        # 1 2 3 4
        # 4 3 4 5
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)
        return max_profit


print(Solution().first([7, 3, 2, 1]))
