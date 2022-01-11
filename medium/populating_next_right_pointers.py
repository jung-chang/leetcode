# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


from typing import Optional, List


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.
    """

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        """
        Traverse tree level by level, set pointers.

            1
          2   3
        4  5 6  7
        """

        if not root:
            return None

        level = [root]
        while level:
            next_level = []
            for i in range(len(level)):
                if i + 1 < len(level):
                    level[i].next = level[i + 1]
                if level[i].left:
                    next_level.append(level[i].left)
                if level[i].right:
                    next_level.append(level[i].right)
            level = next_level
        return root

    def recursive(self, root: Optional[Node]) -> Optional[Node]:
        def helper(level: List[Node]):
            if not level:
                return

            next_level = []
            for i in range(len(level)):
                if i + 1 < len(level):
                    level[i].next = level[i + 1]
                if level[i].left:
                    next_level.append(level[i].left)
                if level[i].right:
                    next_level.append(level[i].right)
            helper(next_level)

        if not root:
            return None
        helper([root])
        return root
