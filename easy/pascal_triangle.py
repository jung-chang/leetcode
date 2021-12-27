# https://leetcode.com/problems/pascals-triangle/


from typing import List


class Solution:
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.

    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    """

    def first(self, numRows: int) -> List[List[int]]:
        """
        Look at previous row and generate next row.
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        triangle = [[1], [1, 1]]
        for _ in range(2, numRows):
            prev_row = triangle[-1]
            row = []
            for j in range(len(prev_row)):
                if j + 1 >= len(prev_row):
                    break
                row.append(prev_row[j] + prev_row[j + 1])
            triangle.append([1] + row + [1])
        return triangle


print(Solution().first(10))
