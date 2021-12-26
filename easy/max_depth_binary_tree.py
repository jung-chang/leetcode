# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    """

    def first(self, root: Optional[TreeNode]) -> int:
        """
        DFS and keep count of max depth. Recursive implementation.
        """

        def helper(node: Optional[TreeNode], depth):
            if not node:
                return depth
            return max(helper(node.left, depth + 1), helper(node.right, depth + 1))

        if not root:
            return 0
        return max(helper(root.left, 1), helper(root.right, 1))

    def second(self, root: Optional[TreeNode]) -> int:
        """
        DFS and keep count of max depth. Iterative implementation.
        """
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth
