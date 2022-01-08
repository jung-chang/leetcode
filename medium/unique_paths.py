# https://leetcode.com/problems/unique-paths/


class Solution:
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        """
        m = number of rows
        n = number of cols

        Dynamic programming question, for each down and right, next cell is +1 of current

        1 x x x x
        x x x x x
        x x x x x


        """
        if m == 0 or n == 0:
            return 0
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1

        visited = set()
        queue = [(0, 0)]
        while queue:
            row, col = queue.pop(0)
            if (row, col) in visited:
                continue
            # Check down
            if row + 1 < m:
                grid[row + 1][col] += grid[row][col]
                queue.append((row + 1, col))
            # Check right
            if col + 1 < n:
                grid[row][col + 1] += grid[row][col]
                queue.append((row, col + 1))
            visited.add((row, col))
        return grid[-1][-1]

    def recursive(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        # grid = [[0] * n for _ in range(m)]

        def helper(x: int, y: int, max_x: int, max_y: int) -> int:
            if x == 0 or y == 0:
                return 1
            if x < 0 or x >= max_x:
                return 0
            if y < 0 or y >= max_y:
                return 0
            return helper(x - 1, y, max_x, max_y) + helper(x, y - 1, max_x, max_y)

        return helper(m - 1, n - 1, m, n)


print(Solution().uniquePaths(3, 7))
print(Solution().recursive(3, 7))
