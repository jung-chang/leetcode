# https://leetcode.com/problems/symmetric-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    """

    def first(self, root: Optional[TreeNode]) -> bool:
        """
        Check that the left subtree is the same as right subtree recursively.
        """

        def helper(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None or right is None:
                return left == right
            return (
                left.val == right.val
                and helper(left.left, right.right)
                and helper(left.right, right.left)
            )

        if not root:
            return False
        return helper(root.left, root.right)

    def second(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative method. Store tuples of nodes to check equality for.
        """
        if not root:
            return False
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop(0)
            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
