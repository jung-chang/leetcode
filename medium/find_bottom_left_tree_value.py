# https://leetcode.com/problems/find-bottom-left-tree-value/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, return the leftmost value in the last row of the tree.
    """

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        lefts = 0
        rows = 0
        value = root.val

        def dfs(node: TreeNode, left_count: int, row_count: int):
            nonlocal lefts
            nonlocal rows
            nonlocal value

            if not node:
                return

            if row_count > rows:
                rows = row_count
                lefts = left_count
                value = node.val
            elif row_count == rows:
                if left_count > lefts:
                    lefts = left_count
                    value = node.val

            dfs(node.left, left_count + 1, row_count + 1)
            dfs(node.right, left_count, row_count + 1)

        dfs(root, 0, 0)
        print(lefts, rows, value)
        return value


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.left.left = TreeNode(7)
root.right.right = TreeNode(6)
print(Solution().findBottomLeftValue(root))
