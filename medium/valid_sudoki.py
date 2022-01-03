# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution:
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Note:

        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Questions
            - Is the board filled?
            - Do we need to check if it's solvable?
            - Are there any technical constraints?
            - How is the board represented? -> 2D array of characters

        Board visualization:

        0 1 2   3 4 5  6 7 8
        _ _ _   _ _ _  _ _ _
        _ _ _
        _ _ _

        _
        _
        _

        _
        _
        _ _ _   _ _ _  _ _ _

        Solution
            - For every row,col we check 1-9. For every square check 1-9. 9x9 * 3 -> O(243)
            - Assuming each list in 2D array represents a row
        """

        def valid(nums: List[int]) -> bool:
            if len(nums) != 9:
                return False
            visited = set()
            for num in nums:
                if num in visited:
                    return False
                if num == ".":
                    continue
                if ord(num) < ord("0") or ord(num) > ord("9"):
                    return False
                visited.add(num)
            return True

        # Check all rows are valid: O(81)
        for row in board:
            if not valid([num for num in row]):
                return False
        # Check all columns are valid: O(81)
        for i in range(9):
            if not valid([row[i] for row in board]):
                return False
        # Check squares are valid
        sections = [[0, 3], [3, 6], [6, 9]]
        for s1, e1 in sections:
            for s2, e2 in sections:
                square = []
                for row in [row[s2:e2] for row in board[s1:e1]]:
                    square.extend(row)
                if not valid(square):
                    return False
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(Solution().isValidSudoku(board))
