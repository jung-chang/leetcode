# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

from typing import Any, List


class Node:
    def __init__(
        self, val: int = 0, left: Any = None, right: Any = None, next: Any = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    """
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.
    """

    def connect(self, root: Node) -> Node:
        def helper(level: List[Node]):
            if not level:
                return

            next_level = []
            for i in range(1, len(level)):
                level[i - 1].next = level[i]

            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print(level, next_level)
            helper(next_level)

        if not root:
            return None
        helper([root])
        return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

print(Solution().connect(root))
