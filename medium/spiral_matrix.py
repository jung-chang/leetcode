# https://leetcode.com/problems/spiral-matrix/

from typing import List
import math


class Solution:
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Questions
            - How small/big can m and n be?
            - What are the values in each cell?
            - Techinical constraints?
            - What's the output type?

        Example
            m=rows, n=cols

            a b c d
            e f g h
            i j k l
            a a a a

            abcdhlkjiefg

            a b
            c d

        Notes
            - start at 0,0, at e make a right
        """

        # Test 2: rows=cols=2
        # offset=0, col=[0,1], row=[1, 1]
        # col=[1,0], 1,1 1,0
        # row = 1,0

        # Test3 a b c d
        # offset=0 col=[0,3]
        # row=[1, 1], col=[2, 0] -> (0,2 0,1)

        # a b c d

        if not matrix:
            return []
        result = []
        offset = 0
        rows = len(matrix)
        cols = len(matrix[0])
        while len(result) < rows * cols:
            # Top going right
            for col in range(offset, cols - offset):
                result.append(matrix[offset][col])
            # Right going down
            for row in range(offset + 1, rows - offset):
                result.append(matrix[row][cols - offset - 1])
            # Bottom going left
            if rows - 1 - offset > offset:
                for col in range(cols - offset - 2, offset - 1, -1):
                    result.append(matrix[rows - 1 - offset][col])
            # Left going up
            if cols - offset - 1 > offset:
                for row in range(rows - offset - 2, offset - 1, -1):
                    if row == offset:
                        break
                    result.append(matrix[row][offset])
            offset += 1
        return result


print(Solution().spiralOrder([["a", "b", "c", "d"]]))
print(Solution().spiralOrder([["a"], ["b"], ["c"], ["d"], ["e"]]))
print(Solution().spiralOrder([["a", "b"], ["c", "d"]]))
print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
