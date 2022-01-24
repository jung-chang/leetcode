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
        # Look at first row
        def binary_search(matrix: List[List[int]], row: int) -> int:
            pass
