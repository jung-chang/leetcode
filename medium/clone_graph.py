# https://leetcode.com/problems/clone-graph/

from typing import Set


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val}, n={[n.val for n in self.neighbors]})"


class Solution:
    """
    Given a reference of a node in a connected undirected graph.

    Return a deep copy (clone) of the graph.

    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
    """

    def recursive(self, node: Node) -> Node:
        def helper(original: Node, visited: Set[Node]):
            copy = Node(original.val)
            visited.add(original)
            for neighbor in original.neighbors:
                if neighbor not in visited:
                    copied_neighbor = helper(neighbor, visited)
                    print(copied_neighbor)
                    copy.neighbors.append(copied_neighbor)
                    copied_neighbor.neighbors.append(copy)
            return copy

        return helper(node, set())

    def cloneGraph(self, node: Node) -> Node:
        """
        Graph traversal by saving states.
        """

        if not node:
            return None

        # Original to copy
        node_map = {}
        stack = [node]
        while stack:
            original = stack.pop()
            copy = Node(original.val)
            node_map[original] = copy
            for neighbor in original.neighbors:
                if neighbor not in node_map:
                    stack.append(neighbor)

        for original, copy in node_map.items():
            for neighbor in original.neighbors:
                copy.neighbors.append(node_map[neighbor])
        return node_map[node]


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

root = Solution().recursive(node1)
print(str(root))
print(root.neighbors[0])
print(root.neighbors[1])
