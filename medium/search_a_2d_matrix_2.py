# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


class Solution:
    """
    Write an efficient algorithm that searches for a target value in an m x n integer matrix.

    The matrix has the following properties:
        Integers in each row are sorted in ascending from left to right.
        Integers in each column are sorted in ascending from top to bottom
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search each row and column.
        """

        def binary_search(arr: List[int], target: int) -> bool:
            if not arr:
                return False
            mid = len(arr) // 2
            if arr[mid] == target:
                return True
            if target < arr[mid]:
                return binary_search(arr[:mid], target)
            return binary_search(arr[mid + 1 :], target)

        # Look at first/last row to determine column
        if not matrix:
            return False

        if len(matrix) == 1:
            pass

        rows = len(matrix)
        cols = len(matrix[0])

        cols_to_check = []
        for col in range(cols):
            if matrix[0][col] == target or matrix[rows - 1][col] == target:
                return True
            if matrix[0][col] < target < matrix[rows - 1][col]:
                cols_to_check.append(col)

        for col in cols_to_check:
            if binary_search([matrix[r][col] for r in range(rows)], target):
                return True
        return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 500

print(Solution().searchMatrix(matrix, target))
