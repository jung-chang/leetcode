# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    """
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.

    """

    #       3
    #      1 5
    #    0 2 4 6

    #   5
    #  3  7
    # 2 6 4 8

    # h(n4, 7) and h(n9, 7)
    def first(self, root: Optional[TreeNode]) -> bool:
        """
        Do an in order traversal and check that its sorted in order.
        """

        def inorder_dfs_recursive(root: TreeNode):
            if not root:
                return []
            return (
                inorder_dfs_recursive(root.left)
                + [root]
                + inorder_dfs_recursive(root.right)
            )

        inorder = inorder_dfs_recursive(root)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False
        return True

    def recursive(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def helper(node, lower, upper):
            if not node:
                return True
            return (
                lower < node.val < upper
                and helper(node.left, lower, node.val)
                and helper(node.right, node.val, upper)
            )

        return helper(root, -math.inf, math.inf)

    def iterative(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative approach.

            5
           3  7
          2 6 4 8

        Change lower/upper bounds in subtrees.
        """
        if not root:
            return False
        queue = [(root, -math.inf, math.inf)]
        while queue:
            node, lower, upper = queue.pop(0)
            if not lower < node.val < upper:
                return False

            if node.left:
                queue.append(node.left, lower, node.val)
            if node.right:
                queue.append(node.right, node.val, upper)
        return True


#     32
#  26    47
# 19   N   N   56
# N 27

# 32 in [-inf, inf]
# left in [-inf, 32], right in [32, inf]
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(4)
root.right.right = TreeNode(8)
print(Solution().isValidBST(root))