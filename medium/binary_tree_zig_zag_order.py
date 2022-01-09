# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
    (i.e., from left to right, then right to left for the next level and alternate between).
    left to right,
    right to le

        1
      2   3
    4  5 6  7

    r=True, [3,2]
    r=False,
    """

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = [[root]]
        is_reversed = True
        while levels[-1]:
            level = []
            cur_level = reversed(levels[-1])
            for node in cur_level:
                if is_reversed:
                    if node.right:
                        level.append(node.right)
                    if node.left:
                        level.append(node.left)
                else:
                    if node.left:
                        level.append(node.left)
                    if node.right:
                        level.append(node.right)
            if not level:
                break
            levels.append(level)
            is_reversed = not is_reversed

        for i in range(len(levels)):
            for j in range(len(levels[i])):
                levels[i][j] = levels[i][j].val
        return levels
