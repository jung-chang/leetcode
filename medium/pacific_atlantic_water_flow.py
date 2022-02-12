# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List, Tuple, Set


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Return a list of row,col coordinates that can flow to both top/left or bottom/right.

        For each cell, DFS  and find paths to top/left and bottom/right.
        Memo the coordinates's ability to flow to each ocean
        """

        rows = len(heights)
        cols = len(heights[0])

        can_reach_top_left = set()
        can_reach_bot_right = set()

        def dfs(row: int, col: int) -> Tuple[List[int], List[int]]:
            """Returns tuple of (top/left path, bottom/right path"""
            nonlocal can_reach_bot_right
            nonlocal can_reach_top_left

            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            top_left_path = []
            bot_right_path = []
            stack = [[(row, col)]]
            while stack and not (top_left_path and bot_right_path):
                path = stack.pop()
                r, c = path[-1]
                for x, y in directions:
                    new_r = r + y
                    new_c = c + x
                    if (
                        0 <= new_r < rows
                        and 0 <= new_c < cols
                        and (new_r, new_c) not in path
                    ):
                        if heights[new_r][new_c] <= heights[r][c]:
                            stack.append(path + [(new_r, new_c)])
                            if (new_r, new_c) in can_reach_top_left:
                                top_left_path = path
                            if (new_r, new_c) in can_reach_bot_right:
                                bot_right_path = path
                    else:
                        if (new_r == -1 or new_c == -1) and not top_left_path:
                            top_left_path = path
                        if (new_r == rows or new_c == cols) and not bot_right_path:
                            bot_right_path = path
            return top_left_path, bot_right_path

        def update_memo(path: List[int], memo: Set[int]):
            for r, c in path:
                memo.add((r, c))

        result = set()
        for r in range(rows):
            for c in range(cols):
                if (r, c) in result:
                    continue
                top_left_path, bot_right_path = dfs(r, c)
                print((r, c), top_left_path, bot_right_path, result)
                if top_left_path and bot_right_path:
                    result.add((r, c))

                if top_left_path:
                    update_memo(top_left_path, can_reach_top_left)
                if bot_right_path:
                    update_memo(bot_right_path, can_reach_bot_right)
        return sorted([[r, c] for r, c in result], key=lambda x: (x[0], x[1]))


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
heights = [[2, 1], [1, 2]]
print(Solution().pacificAtlantic(heights))
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]