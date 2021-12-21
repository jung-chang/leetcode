# https://leetcode.com/problems/climbing-stairs/


class Solution:
    """
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """

    def first(self, n: int) -> int:
        """
        DP problem. Use array to keep track of number of ways to arrive at each step.
        """
        if n < 2:
            return 1
        ways = [1, 2]
        for i in range(2, n):
            ways.append(ways[i - 2] + ways[i - 1])
        return ways[-1]
