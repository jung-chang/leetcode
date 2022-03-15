# https://leetcode.com/problems/max-area-of-island/

from typing import List, Set, Tuple


class Solution:
    """
    You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
    You may assume all four edges of the grid are surrounded by water.

    The area of an island is the number of cells with a value 1 in the island.

    Return the maximum area of an island in grid. If there is no island, return 0.
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        max_area = 0

        def get_island(start_x: int, start_y: int) -> Set[Tuple[int, int]]:
            island = set([(start_x, start_y)])

            def dfs(start_x: int, start_y: int):
                for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    new_x = start_x + x
                    new_y = start_y + y
                    if not 0 <= new_x < len(grid):
                        continue
                    if not 0 <= new_y < len(grid[new_x]):
                        continue
                    if (new_x, new_y) in island:
                        continue
                    if (new_x, new_y) in visited:
                        continue
                    if grid[new_x][new_y] == 1:
                        island.add((new_x, new_y))
                        dfs(new_x, new_y)

            def dfs_iter(start_x: int, start_y: int):
                stack = [(start_x, start_y)]
                while stack:
                    x, y = stack.pop()
                    for delta_x, delta_y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        new_x = x + delta_x
                        new_y = y + delta_y
                        if not 0 <= new_x < len(grid):
                            continue
                        if not 0 <= new_y < len(grid[new_x]):
                            continue
                        if (new_x, new_y) in island:
                            continue
                        if (new_x, new_y) in visited:
                            continue
                        if grid[new_x][new_y] == 1:
                            island.add((new_x, new_y))
                            stack.append((new_x, new_y))

            dfs_iter(start_x, start_y)
            return island

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if (x, y) in visited:
                    continue
                if grid[x][y] == 0:
                    continue
                island = get_island(x, y)
                visited.update(island)
                max_area = max(max_area, len(island))
        return max_area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
# grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
grid = [[1]]

print(Solution().maxAreaOfIsland(grid))
