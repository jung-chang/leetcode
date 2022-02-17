# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return
            if node:
                temp = node.right
                node.right = node.left
                node.left = temp

            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        helper(root)
        return root
