# https://leetcode.com/problems/minimum-height-trees/

from collections import defaultdict
from typing import List, Dict, Tuple


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def __repr__(self):
        return str(self.val)


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()


class Solution:
    """
    Given a tree of n nodes labelled from 0 to n - 1,
    and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between
    the two nodes ai and bi in the tree, you can choose any node of the tree as the root.
    When you select a node x as the root, the result tree has height h.

    Among all possible rooted trees, those with minimum height (i.e. min(h)) are called minimum height trees (MHTs).

    Return a list of all MHTs' root labels. You can return the answer in any order.
    """

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Create a graph and find longest path from every starting node.
        """

        def path_length(start: Node, min_length: int) -> int:
            stack = [[start]]
            length = 0
            while stack:
                path = stack.pop()
                length = max(length, len(path))
                if length > min_length:
                    return min_length + 1
                for neighbor in path[-1].neighbors:
                    if neighbor not in path:
                        stack.append(path + [neighbor])
            return length

        def make_graph(edges: List[List[int]]) -> Dict[int, Node]:
            graph = {}
            for a, b in edges:
                if a not in graph:
                    node_a = Node(a)
                    graph[a] = node_a
                else:
                    node_a = graph[a]
                if b not in graph:
                    node_b = Node(b)
                    graph[b] = node_b
                else:
                    node_b = graph[b]
                node_a.neighbors.add(node_b)
                node_b.neighbors.add(node_a)
            return graph

        if not edges:
            return [i for i in range(n)]
        graph = make_graph(edges)
        length_to_node = defaultdict(list)
        min_length = float("inf")

        for start in graph.values():
            length = path_length(start, min_length)
            length_to_node[length].append(start)
            # print(start.val, length)
            min_length = min(min_length, length)
        return [node.val for node in length_to_node[min_length]]

    def findMinHeightTreess(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Steps
            - Construct trees
            - Calculate height of each tree
            - Track min trees
        """

        def make_tree(
            val: int, edges: List[List[int]], min_height: int
        ) -> Tuple[TreeNode, bool]:
            # [2,1],[3,1],[1,0]]
            root = TreeNode(val)
            val_to_node = {val: (root, 0)}
            i = 0
            while len(val_to_node) < len(edges) + 1:
                a, b = edges[i % len(edges)]
                if a in val_to_node and b in val_to_node:
                    i += 1
                    continue
                if a in val_to_node:
                    parent, height = val_to_node[a]
                    if height > min_height:
                        return root, False
                    child = TreeNode(b)
                    val_to_node[b] = (child, height + 1)
                    parent.children.append(child)
                    # print(a, b, val_to_node, edges)
                elif b in val_to_node:
                    parent, height = val_to_node[b]
                    if height > min_height:
                        return root, False
                    child = TreeNode(a)
                    val_to_node[a] = (child, height + 1)
                    parent.children.append(child)
                    # print(a, b, val_to_node, edges)
                i += 1

            return root, True

        def get_height(root: TreeNode, min_height: int) -> int:
            height = 0

            def _dfs(node: TreeNode, visited: List[TreeNode]):
                nonlocal height
                if len(visited) > min_height:
                    height = min_height + 1
                    return
                if not node.children:
                    height = max(height, len(visited))
                for child in node.children:
                    _dfs(child, visited + [node])

            _dfs(root, [])
            return height

        min_height = float("inf")
        heights_to_node = defaultdict(list)
        for i in range(n):
            root, valid = make_tree(i, edges, min_height)
            if not valid:
                continue
            height = get_height(root, min_height)
            # print("root", root.val, "height", height)
            min_height = min(min_height, height)
            heights_to_node[height].append(root)
        return [node.val for node in heights_to_node[min_height]]


n = 10
e = [[0, 1], [0, 2], [0, 3], [2, 4], [0, 5], [5, 6], [6, 7], [2, 8], [7, 9]]


# n = 7
# e = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]

print(Solution().findMinHeightTrees(n, e))
