# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Track each level and append to result. Iterative.
        """
        if not root:
            return []
        levels = [[root]]
        while levels[-1]:
            level = []
            for node in levels[-1]:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if not level:
                break
            levels.append(level)

        for i in range(len(levels)):
            for j in range(len(levels[i])):
                levels[i][j] = levels[i][j].val
        return levels

    def recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(level: List[TreeNode]) -> List[TreeNode]:
            if not level:
                return []
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            return [[next_level]] + [helper(next_level)]

        levels = [[root]] + helper([root])
        for i in range(len(levels)):
            for j in range(len(levels[i])):
                levels[i][j] = levels[i][j].val
        return levels