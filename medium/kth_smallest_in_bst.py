# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    """
    Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Can do an in order traversal and select value at k.
        """

        if k < 1:
            return None
        if not root:
            return None

        traversal = []
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
                continue
            if stack:
                node = stack.pop()
                traversal.append(node)
                print(traversal)
                if len(traversal) == k:
                    return node.val
                node = node.right


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
# root.left.left = TreeNode(4)
root.left.right = TreeNode(2)

print(Solution().kthSmallest(root, 3))
