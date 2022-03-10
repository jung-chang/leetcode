# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from collections import defaultdict
from typing import List, Dict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def __repr__(self):
        return str(self.val)


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Create a graph from the tree
        """
        if not root:
            return []

        treenode_to_node = {}

        def create_nodes(tree_node: TreeNode):
            nonlocal treenode_to_node
            if not tree_node:
                return
            node = Node(tree_node.val)
            treenode_to_node[tree_node] = node
            create_nodes(tree_node.left)
            create_nodes(tree_node.right)

        def connect_neighbors(tree_node: TreeNode):
            nonlocal treenode_to_node
            if not tree_node:
                return
            node = treenode_to_node[tree_node]
            if tree_node.left in treenode_to_node:
                neighbor = treenode_to_node[tree_node.left]
                node.neighbors.append(neighbor)
                neighbor.neighbors.append(node)
            if tree_node.right in treenode_to_node:
                neighbor = treenode_to_node[tree_node.right]
                node.neighbors.append(neighbor)
                neighbor.neighbors.append(node)
            connect_neighbors(tree_node.left)
            connect_neighbors(tree_node.right)

        create_nodes(root)
        connect_neighbors(root)

        target_node = treenode_to_node[target]
        result = []
        stack = [[target_node]]
        while stack:
            path = stack.pop()
            path_length = len(path) - 1  # account for itself
            if path_length == k:
                result.append(path[-1].val)
            for n in path[-1].neighbors:
                if n not in path and path_length + 1 <= k:
                    stack.append(path + [n])

        print(treenode_to_node[root].neighbors)
        print(treenode_to_node[target].neighbors)
        return result


root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(Solution().distanceK(root, root.left, 2))
