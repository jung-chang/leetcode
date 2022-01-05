# https://leetcode.com/problems/rotate-image/

from typing import List
import math


class Solution:
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Start at each corner, rotate each four numbers, and then do it to the left one

        00 01 02 03
        10 11 12 13
        20 21 22 23
        30 31 32 33

        00, 03, 33, 30
        01, 13, 31, 10
        02, 23, 32, 20

        11 12 21 22

        1 0
        2 1
        3 2
        4 2
        5 3
        """

        for row in matrix:
            print(row)

        n = len(matrix)  # 4
        max_i = n - 1  # 3
        for i in range(math.ceil(n / 2)):
            for j in range(n // 2):  # j=1
                temp = matrix[i][j]  # top left=01
                matrix[i][j] = matrix[max_i - j][i]  # bottom left: 01 = 20
                matrix[max_i - j][i] = matrix[max_i - i][
                    max_i - j
                ]  # bottom right: 20=32
                matrix[max_i - i][max_i - j] = matrix[j][max_i - i]  # top right: 32=03
                matrix[j][max_i - i] = temp  # 03=01


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2], [3, 4]]
Solution().rotate(matrix)

print()
for row in matrix:
    print(row)
