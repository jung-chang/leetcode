# https://leetcode.com/problems/coin-change/

from typing import List, Tuple


class Solution:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        DP problem.

        Make dp array up to amount.

        dp[value] = 1 if value in coins, BFS every coin less than i while using dp -> Time exceed

        Example
            coins = [2 3], amount = 5
            0 1 2 3 4 5 6
            0-1 1 1 2 2 2
        """

        def bfs(value: int, coins: List[int], dp: List[int]) -> int:
            queue = [(coin, 1) for coin in coins]
            min_coins = float("inf")
            while queue:
                total, num = queue.pop(0)
                if total == value:
                    min_coins = min(min_coins, num)
                    continue
                for coin in coins:
                    if total + coin > value:
                        continue
                    queue.append((total + coin, num + dp[coin]))

        coin_set = set(coins)
        desc_coins = sorted(coins, reverse=True)
        if amount < 0:
            return -1
        if not amount:
            return 0

        dp = []
        for i in range(amount + 1):
            if i in coin_set:
                dp.append(1)
            else:
                min_coins = float("inf")
                for coin in desc_coins:
                    if coin > len(dp):
                        continue
                    if dp[coin] > 0 and dp[i - coin] > 0:
                        min_coins = min(min_coins, dp[coin] + dp[i - coin])
                dp.append(min_coins if min_coins != float("inf") else -1)
        return dp[-1]


c = [3, 7, 405, 436]
a = 8839


print(Solution().coinChange(c, a))
