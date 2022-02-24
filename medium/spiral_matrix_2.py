# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Solution:
    """
    Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
    """

    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [1]

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        r = 0
        c = 0
        num = 2
        matrix[0][0] = 1

        while num <= n * n:
            # Right
            while c + 1 < n and matrix[r][c + 1] == 0:
                matrix[r][c + 1] = num
                c += 1
                num += 1
            # Down
            while r + 1 < n and matrix[r + 1][c] == 0:
                matrix[r + 1][c] = num
                r += 1
                num += 1
            # Left
            while c - 1 >= 0 and matrix[r][c - 1] == 0:
                matrix[r][c - 1] = num
                c -= 1
                num += 1
            # Up
            while r - 1 >= 0 and matrix[r - 1][c] == 0:
                matrix[r - 1][c] = num
                r -= 1
                num += 1
        return matrix


matrix = Solution().generateMatrix(1)
for row in matrix:
    print(row)
