# https://leetcode.com/problems/most-frequent-subtree-sum/

from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, return the most frequent subtree sum.
    If there is a tie, return all the values with the highest frequency in any order.

    The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node
    (including the node itself).
    """

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_to_freq = defaultdict(int)

        def sum_at_node(node: TreeNode):
            if not node.left and not node.right:
                sum_to_freq[node.val] += 1
                return node.val

            left_total = 0
            right_total = 0

            if node.left:
                left_total = sum_at_node(node.left)
            if node.right:
                right_total = sum_at_node(node.right)

            total = node.val + left_total + right_total
            sum_to_freq[total] += 1
            return total

        sum_at_node(root)
        print(sum_to_freq)
        max_freq = sorted(sum_to_freq.values())[-1]
        return [total for total, freq in sum_to_freq.items() if freq == max_freq]


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
print(Solution().findFrequentTreeSum(root))
