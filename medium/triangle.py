# https://leetcode.com/problems/triangle/

from typing import List


class Solution:
    """
    Given a triangle array, return the minimum path sum from top to bottom.

    For each step, you may move to an adjacent number of the row below.
    More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
    """

    def DP(self, triangle: List[List[int]]) -> int:
        level = 1
        while level < len(triangle):
            prev = level - 1
            for i in range(len(triangle[level])):
                if i == 0:
                    triangle[level][i] += triangle[prev][0]
                elif i == len(triangle[level]) - 1:
                    triangle[level][i] += triangle[prev][-1]
                else:
                    triangle[level][i] += min(triangle[prev][i - 1], triangle[prev][i])
            level += 1
        return min(triangle[-1])


t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Solution().minimumTotal(t))
