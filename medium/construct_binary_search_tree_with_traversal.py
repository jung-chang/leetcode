# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given two integer arrays preorder and inorder where preorder is the preorder traversal
    of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
    8534
        1
       2  3
     4  5 6 7

    pre = 1 2 4 5 3 6 7
    in = 4 2 5 1 6 3 7

        1
      2   3

    pre = 1 2 3
    in = 2 1 3

    1
      2
        3

    if number have smaller index in inorder, left subtree

    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass