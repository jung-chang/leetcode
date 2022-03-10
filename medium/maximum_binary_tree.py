# https://leetcode.com/problems/maximum-binary-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

    Create a root node whose value is the maximum value in nums.
    Recursively build the left subtree on the subarray prefix to the left of the maximum value.
    Recursively build the right subtree on the subarray suffix to the right of the maximum value.

    Return the maximum binary tree built from nums.
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def find_max_i(nums: List[int]):
            i = 0
            max_num = nums[0]
            for j in range(1, len(nums)):
                if nums[j] > max_num:
                    i = j
                    max_num = nums[j]
            return i

        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        max_i = find_max_i(nums)
        node = TreeNode(nums[max_i])
        node.left = self.constructMaximumBinaryTree(nums[:max_i])
        node.right = self.constructMaximumBinaryTree(nums[max_i + 1 :])
        return node
