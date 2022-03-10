# https://leetcode.com/problems/path-sum-iii/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    """
    Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

    The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
    """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0

        def dfs(total: int, length: int, node: TreeNode):
            nonlocal count

            if total == targetSum:
                count += 1
            if node.left:
                dfs(total + node.left.val, length + 1, node.left)
                if length == 1:
                    dfs(node.left.val, 1, node.left)
            if node.right:
                dfs(total + node.right.val, length + 1, node.right)
                if length == 1:
                    dfs(node.right.val, 1, node.right)

        if not root:
            return 0
        dfs(root.val, 1, root)
        return count

    def first(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = []

        def dfs(path: List[TreeNode]):
            if sum([node.val for node in path]) == targetSum:
                result.append(path)

            node = path[-1]
            if node.left:
                dfs(path + [node.left])
                if len(path) == 1:
                    dfs([node.left])
            if node.right:
                dfs(path + [node.right])
                if len(path) == 1:
                    dfs([node.right])

        if not root:
            return 0
        dfs([root])
        print(result)
        return len(result)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)

root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# root.right.right.right = TreeNode(4)
# root.right.right.right.right = TreeNode(5)

print(Solution().pathSum(root, 8))
