# https://leetcode.com/problems/minimum-path-sum/

import heapq
from typing import List


class Solution:
    """
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        min_total = float("inf")

        while heap:
            total, row, col = heapq.heappop(heap)
            if row == len(grid) - 1 and col == len(grid[row]) - 1:
                min_total = min(min_total, total)
                continue
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if col + 1 < len(grid[row]):
                heapq.heappush(heap, (total + grid[row][col + 1], row, col + 1))
            if row + 1 < len(grid):
                heapq.heappush(heap, (total + grid[row + 1][col], row + 1, col))

        return min_total


g = [[1, 2, 3], [4, 5, 6]]
print(Solution().minPathSum(g))
