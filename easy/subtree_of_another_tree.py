# https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
    """

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        if not root and not subRoot:
            return True

        def is_same_tree(node1, node2):
            if node1 and not node2:
                return False
            if not node1 and node2:
                return False
            if not node1 and not node2:
                return True
            return (
                node1.val == node2.val
                and is_same_tree(node1.left, node2.left)
                and is_same_tree(node1.right, node2.right)
            )

        same_tree = False
        if root.val == subRoot.val:
            same_tree = is_same_tree(root, subRoot)
        return (
            same_tree
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
