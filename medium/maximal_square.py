# https://leetcode.com/problems/maximal-square/

from collections import defaultdict
from typing import List


class Solution:
    """
    Given an m x n binary matrix filled with 0's and 1's,
    find the largest square containing only 1's and return its area.
    """

    # def find_diagonals(self, matrix: List[List[str]]) -> int:
    #     rows = len(matrix)
    #     cols = len(matrix[0])

    #     def get_diagonal(row: int, col: int):
    #         count = 1
    #         diagonal = set([(row, col)])
    #         while row + 1 < rows and col + 1 < cols:
    #             row += 1
    #             col += 1
    #             if matrix[row][col] == "0":
    #                 break
    #             diagonal.add((row, col))
    #             count += 1
    #         return diagonal, count

    #     diagonals_to_len = {}
    #     visited = set()
    #     for r in range(rows):
    #         for c in range(cols):
    #             if (r, c) in visited:
    #                 continue
    #             diagonal, length = get_diagonal(r, c)
    #             visited.update(diagonal)
    #             diagonals_to_len[(r, c)] = max(diagonals_to_len[(r, c)], length)

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        def get_square(row: int, col: int) -> int:
            diagonal = 1
            square = set([(row, col)])

            while row + diagonal < rows and col + diagonal < cols:
                new_row = row + diagonal
                new_col = col + diagonal
                is_square = True

                # check column
                i = new_col
                while i >= col:
                    if matrix[new_row][i] == "0":
                        is_square = False
                        break
                    square.add((new_row, i))
                    i -= 1
                if not is_square:
                    break

                # check row
                i = new_row
                while i >= row:
                    if matrix[i][new_col] == "0":
                        is_square = False
                        break
                    square.add((i, new_col))
                    i -= 1
                if not is_square:
                    break

                diagonal += 1
            return square, diagonal * diagonal

        max_area = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "0":
                    continue
                if (r, c) in visited:
                    continue
                square, area = get_square(r, c)
                max_area = max(max_area, area)
                if area > 1:
                    visited.update(square)
        return max_area


m = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]

# m = [["0", "1"], ["1", "0"]]
# m = [["0"]]
# m = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["0", "0", "1", "1", "1"],
# ]

m = [
    ["0", "0", "0", "1"],
    ["1", "1", "0", "1"],
    ["1", "1", "1", "1"],
    ["0", "1", "1", "1"],
    ["0", "1", "1", "1"],
]

print(Solution().maximalSquare(m))
