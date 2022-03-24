# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
    """

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [[root]]
        while stack:
            level = stack.pop()
            result.append(max([node.val for node in level]))

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if not next_level:
                break
            stack.append(next_level)
        return result
