# https://leetcode.com/problems/validate-binary-tree-nodes/

from collections import defaultdict
from typing import List, Set


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    """
    You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i],
    return true if and only if all the given nodes form exactly one valid binary tree.

    If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

    Note that the nodes have no values and that we only use the node numbers in this problem.
    """

    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        """
        Find parents of each node.
        A valid tree must have nodes with only one parent and exactly one node with no parent.
        """
        # Find parent node
        root = 0
        children = set(leftChild + rightChild)
        for i in range(n):
            if i not in children:
                root = i

        queue = [root]
        visited = set()
        while queue:
            cur = queue.pop(0)
            if cur in visited:
                return False
            visited.add(cur)
            if leftChild[cur] != -1:
                queue.append(leftChild[cur])
            if rightChild[cur] != -1:
                queue.append(rightChild[cur])

        if len(visited) != n:
            return False

        return True


n = 6
l = [1, -1, -1, 4, -1, -1]
r = [2, -1, -1, 5, -1, -1]

n = 4
l = [3, -1, 1, -1]
r = [-1, -1, 0, -1]


print(Solution().validateBinaryTreeNodes(n, l, r))
