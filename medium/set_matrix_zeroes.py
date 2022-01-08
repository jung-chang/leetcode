# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


class Solution:
    """
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Time: O(m*n + # zerooes * (m+n))
        Space: O(m*n)
        """
        zeroes = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    zeroes.add((row, col))

        for row, col in zeroes:
            # Set entire row
            for i in range(len(matrix[row])):
                matrix[row][i] = 0
            # Set entire col
            for i in range(len(matrix)):
                matrix[i][col] = 0

    def second(self, matrix: List[List[int]]) -> None:
        """
        Keep track of the indices we want to add zeroes for.
        """

        new_zeroes = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    for i in range(len(matrix[row])):
                        new_zeroes.add((row, i))
                    for i in range(len(matrix)):
                        new_zeroes.add((i, col))

        for row, col in new_zeroes:
            matrix[row][col] = 0

    def third(self, matrix: List[List[int]]) -> None:
        """
        Constant space solution?

        Keep track of cols and rows that need all zeroes

        Time: O(m*n)

        Space O(m+n)
        """
        rows = set()
        cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        for row in rows:
            for i in range(len(matrix[row])):
                matrix[row][i] = 0
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0

    def fourth(self, matrix: List[List[int]]) -> None:
        """
        Use 0th indices in matrix itself as indicators to change entire row/col into zeroes
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[row])):
                    matrix[row][col] = 0

        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0


matrix = [[0, 1, 2, 0], [3, 4, 0, 2], [1, 3, 1, 5]]
Solution().fourth(matrix)
for row in matrix:
    print(row)
