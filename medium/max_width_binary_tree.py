# https://leetcode.com/problems/maximum-width-of-binary-tree

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
    Given the root of a binary tree, return the maximum width of the given tree.

    The maximum width of a tree is the maximum width among all levels.

    The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

    It is guaranteed that the answer will in the range of 32-bit signed integer.
    """

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Keep track of min/max at each level.
        """
        if not root:
            return 0
        level_map = {}

        def helper(node: TreeNode, val: int, level: int):
            nonlocal level_map

            if not node:
                return

            if level not in level_map:
                level_map[level] = (val, val)
            else:
                l, r = level_map[level]
                level_map[level] = (min(l, val), max(r, val))

            if node.left:
                helper(node.left, val * 2 - 1, level + 1)
            if node.right:
                helper(node.right, val * 2, level + 1)

        helper(root, 1, 1)
        print(level_map)
        width = 1
        for l, r in level_map.values():
            width = max(width, r - l + 1)
        return width

    def first(self, root: Optional[TreeNode]) -> int:
        """
        Solutions
            - Level order traverse, find largest level. Will have to fill with None nodes.
            - Keep track of node numbers some how
        """
        if not root:
            return 0

        width = 1

        def prune(level: List[Optional[TreeNode]]) -> List[Optional[TreeNode]]:
            i = 0
            while i < len(level) and not level[i]:
                i += 1
            j = len(level) - 1
            while i < j and not level[j]:
                j -= 1
            return level[i : j + 1]

        def helper(level: List[Optional[TreeNode]]):
            nonlocal width

            if not level:
                return
            level = prune(level)
            width = max(width, len(level))
            cur_level = []
            has_level = False
            for node in level:
                if not node:
                    cur_level.extend([None, None])
                else:
                    has_level = True
                    cur_level.append(node.left)
                    cur_level.append(node.right)
            if not has_level:
                return
            helper(cur_level)

        helper([root])
        return width


root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(9)
print(Solution().widthOfBinaryTree(root))
