# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import math
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
    """

    def first(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Start root at half the array, binary search down the halves and make subtrees.
        """
        if not nums:
            return None
        half = len(nums) // 2
        node = TreeNode(nums[half])
        node.left = self.first(nums[:half])
        node.right = self.first(nums[half + 1 :])
        return node


root = Solution().first([-10, -3, 0, 5, 9])
print(root.val)
print(root.left.val, root.right.val)
print(root.left.left.val, root.left.right)
