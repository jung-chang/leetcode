# https://leetcode.com/problems/number-of-islands/

from typing import List, Set, Tuple


class Solution:
    """
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Islands are not connected diagonally.

        Keep a set of all coordinates making islands.
        """

        def bfs(row: int, col: int, grid: List[List[str]]) -> Set[Tuple[int, int]]:
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            queue = [(row, col)]
            visited = set()
            while queue:
                r, c = queue.pop(0)
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for x, y in directions:
                    new_r = r + y
                    new_c = c + x
                    if (
                        0 <= new_r < len(grid)
                        and 0 <= new_c < len(grid[new_r])
                        and grid[new_r][new_c] == "1"
                    ):
                        queue.append((new_r, new_c))
            return visited

        if not grid:
            return 0

        islands = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) in visited:
                    continue
                if grid[r][c] == "0":
                    continue
                island = bfs(r, c, grid)
                if island:
                    visited.update(island)
                    islands += 1
        return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

print(Solution().numIslands(grid))
