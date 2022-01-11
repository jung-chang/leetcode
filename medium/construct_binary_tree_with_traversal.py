# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            1
          2   3
        4  5  6 7

        pre = 1 2 3 4 5 6 7
        in = 4 2 5 1 6 3 7

        node(1) -> left=425, right=637
        node(2) -> left=4, right=5
        node(3) -> left=6, right=7

            1
          2   3
        4  5

        pre = 1 2 4 5 3
        in = 4 2 5 1 3

        node(1) -> left=425, r=3
        node(2) ...
        node(3)

        - Root is always pre[0] and left/right subtrees defined in inorder.
        - Level order construction
        - Assume integers are unique
        """

        if not preorder or not not inorder:
            return None

        index_map = {}
        for i, num in enumerate(inorder):
            index_map[num] = i

        pre = 0

        def helper(left, right):
            if left > right:
                return None
            nonlocal pre
            node = TreeNode(preorder[pre])
            pre += 1

            node.left = helper(left, index_map[node.val] - 1)
            node.right = helper(index_map[node.val] + 1, right)
            return node

        return helper(0, len(preorder) - 1)

    def second(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Doesnt work. Hard problem
        """

        if not preorder or not inorder:
            return None

        index_map = {}
        for i, num in enumerate(inorder):
            index_map[num] = i

        def helper(inor: List[int]):
            if not inor:
                return None

            node = TreeNode(preorder[0])
            preorder.pop(0)

            node.left = helper(inor[: index_map[node.val]])
            node.right = helper(inor[index_map[node.val] + 1 :])
            return node

        return helper(inorder)
