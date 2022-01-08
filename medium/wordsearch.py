# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        How big is mxn?
        Technical constraints?
        How long is the word?
        Are there only letters?

        Solution
            Find indices of first letter, and start a search at each.

        Time: O(mn * 4 * (mn)) = O(mn ^ 2)
        Space:
        """

        def search(
            row: int, col: int, visited: set, word: str, board: List[List[str]]
        ) -> bool:
            if not word:
                return True
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            found = False

            for r, c in directions:
                new_row = row + r
                new_col = col + c

                if (new_row, new_col) in visited:
                    continue
                if (
                    0 <= new_row
                    and new_row < len(board)
                    and 0 <= new_col
                    and new_col < len(board[new_row])
                ):
                    if board[new_row][new_col] == word[0]:
                        visited_copy = visited.copy()
                        visited_copy.add((new_row, new_col))
                        print(visited_copy, word)
                        found = found or search(
                            new_row, new_col, visited_copy, word[1:], board
                        )
            return found

        if not word:
            return False
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if search(row, col, set([(row, col)]), word[1:], board):
                        return True
        return False

    def second(self, board: List[List[str]], word: str) -> bool:
        """
        How big is mxn?
        Technical constraints?
        How long is the word?
        Are there only letters?

        Solution
            Find indices of first letter, and start a search at each.

        Time: O(mn * 4 * (mn)) = O(mn ^ 2)
        Space:
        """

        def search(row: int, col: int, word: str, board: List[List[str]]) -> bool:
            stack = [(row, col, word, set())]
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while stack:
                cur_row, cur_col, string, visited = stack.pop()
                print(cur_row, cur_col, string, visited)
                visited.add((cur_row, cur_col))
                for r, c in directions:
                    new_row = cur_row + r
                    new_col = cur_col + c
                    print(new_row, new_col)
                    if (new_row, new_col) in visited:
                        continue
                    if (
                        0 <= new_row
                        and new_row < len(board)
                        and 0 <= new_col
                        and new_col < len(board[new_row])
                        and board[new_row][new_col] == string[0]
                    ):

                        if not string[1:]:
                            return True
                        stack.append((new_row, new_col, string[1:], visited))
            return False

        if not word:
            return False
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if search(row, col, word[1:], board):
                        return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]

for row in board:
    print(row)

print(
    Solution().second(
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"
    )
)
