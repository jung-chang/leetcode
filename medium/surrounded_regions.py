# https://leetcode.com/problems/surrounded-regions/

from typing import List, Set, Tuple


class Solution:
    """
    Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Cases
            - What if O at corners? No need to check
            - what if O stuck to walls? No need to check
            - All Os?

        Solution
            - For all O cells, check 4 directions and determine if change
            - Augment by, if comes across another O, add it to be changed

        Examples

        x x o
        x o x
        x x x

        o o o
        x x x

        o x
        o x
        o x

        For an 'O' at r,c change if there exists 'x' at i,j where i<r,c and i>r,c and r,j<c and r,j>c

        Time: O(m*n + m + n)
        Space: O(m*n)

        Solving the wrong problem here. Misinterpreted 'surrounding 4-directionally'
        """

        def surrounded(row: int, col: int, board: List[List[str]]):
            has_left = has_right = has_up = has_down = False
            # Up
            i = row - 1
            while i >= 0:
                if board[i][col] == "X":
                    has_up = True
                    break
                i -= 1
            # Down
            i = row + 1
            while i < len(board):
                if board[i][col] == "X":
                    has_down = True
                    break
                i += 1
            # Left
            j = col - 1
            while j >= 0:
                if board[row][j] == "X":
                    has_left = True
                    break
                j -= 1
            # Right
            j = col + 1
            while j < len(board[row]):
                if board[row][j] == "X":
                    has_right = True
                    break
                j += 1
            print(row, col, has_left, has_right, has_up, has_down)
            return has_left and has_right and has_up and has_down

        if not board:
            return None

        if len(board) <= 2 or len(board[0]) <= 2:
            return None

        change_to_x = set()
        # board is at least 3x3
        for row in range(1, len(board) - 1):
            for col in range(1, len(board[row]) - 1):
                if board[row][col] != "O":
                    continue
                if (row, col) in change_to_x:
                    continue
                if surrounded(row, col, board):
                    change_to_x.add((row, col))

        for row, col in change_to_x:
            board[row][col] = "X"

    def second(self, board: List[List[str]]) -> None:
        def surrounded(row, col, visited) -> bool:
            """
            x x x x
            x o o o
            x x x x
            """
            # If at the edges and still searching, not surrounded
            if not 0 < row < len(board) - 1 or not 0 < col < len(board[row]) - 1:
                return False, visited

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            is_surrounded = True
            for x, y in directions:
                new_row = row + x
                new_col = col + y
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[new_row]):
                    if (new_row, new_col) in visited:
                        continue
                    if board[new_row][new_col] == "O":
                        visited.add((new_row, new_col))
                        r_is_surrounded, r_visited = surrounded(
                            new_row, new_col, visited
                        )
                        is_surrounded = is_surrounded and r_is_surrounded
                        visited.update(r_visited)
            return is_surrounded, visited

        if not board:
            return None

        if len(board) <= 2 or len(board[0]) <= 2:
            return None

        change_to_x = set()
        # board is at least 3x3
        for row in range(1, len(board) - 1):
            for col in range(1, len(board[row]) - 1):
                if board[row][col] != "O":
                    continue
                if (row, col) in change_to_x:
                    continue
                is_surrounded, visited = surrounded(row, col, set([(row, col)]))
                if is_surrounded:
                    change_to_x.update(visited)

        for row, col in change_to_x:
            board[row][col] = "X"

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
Solution().second(board)

for row in board:
    print(row)

# [
#     ["O", "X", "X", "O", "X"],
#     ["X", "X", "X", "X", "O"],
#     ["X", "X", "X", "O", "X"],
#     ["O", "X", "O", "O", "O"],
#     ["X", "X", "O", "X", "O"],
# ]
