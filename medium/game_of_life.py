# https://leetcode.com/problems/game-of-life/

from typing import List


class Solution:
    """
    The board is made up of an m x n grid of cells, where each cell has an initial state:
        - live (represented by a 1)
        - dead (represented by a 0)

    Each cell interacts with its eight neighbors (horizontal, vertical, diagonal):
        Any live cell with fewer than two live neighbors dies as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
    Given the current state of the m x n grid board, return the next state.
    """

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return [[]]

        rows = len(board)
        cols = len(board[0])

        def get_lives(r: int, c: int, board_copy: List[List[int]]) -> int:
            directions = [
                [-1, -1],
                [-1, 0],
                [-1, 1],
                [0, 1],
                [1, 1],
                [1, 0],
                [1, -1],
                [0, -1],
            ]
            lives = 0
            for x, y in directions:
                row = y + r
                col = x + c
                if 0 <= row < rows and 0 <= col < cols:
                    lives += board_copy[row][col]
            return lives

        board_copy = [row[:] for row in board]
        for row in range(rows):
            for col in range(cols):
                lives = get_lives(row, col, board_copy)
                if board_copy[row][col]:
                    if 2 <= lives <= 3:
                        board[row][col] = 1
                    else:
                        board[row][col] = 0
                else:
                    if lives == 3:
                        board[row][col] = 1


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
Solution().gameOfLife(board)

for row in board:
    print(row)
