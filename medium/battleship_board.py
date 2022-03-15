# https://leetcode.com/problems/battleships-in-a-board/

from typing import List


class Solution:
    """
    Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
    """

    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])

        def dfs(row: int, col: int):
            visited = set()
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                visited.add((r, c))
                for delta_r, delta_c in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    new_r, new_c = r + delta_r, c + delta_c
                    if (new_r, new_c) in visited:
                        continue
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        if board[new_r][new_c] == "X":
                            stack.append((new_r, new_c))
            return visited

        visited = set()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited:
                    continue
                if board[r][c] == "X":
                    ship = dfs(r, c)
                    print(r, c, ship)
                    if ship:
                        count += 1
                        visited.update(ship)
        return count


b = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
print(Solution().countBattleships(b))
