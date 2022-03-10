# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_map = {}

        def helper(node: TreeNode, val: int, level: int):
            nonlocal level_map
            if not node:
                return

            if level not in level_map:
                level_map[level] = (val, node)
            else:
                cur_val, _ = level_map[level]
                if val > cur_val:
                    level_map[level] = (val, node)
            helper(node.left, val * 2 - 1, level + 1)
            helper(node.right, val * 2, level + 1)

        helper(root, 1, 1)
        print(level_map)
        result = []
        for key in sorted(level_map.keys()):
            result.append(level_map[key][1].val)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(Solution().rightSideView(root))
