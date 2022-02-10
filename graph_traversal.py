from typing import List, Set


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def __repr__(self):
        return str(self.val)


def create_graph(adj_list: List[List[int]]) -> Node:
    # [[2,4], [1,3], [2,4], [1,3]]
    # Means node 1 has neighbors node 2 and node 4...and so on
    val_to_node = {}
    for i in range(len(adj_list)):
        val = i + 1
        node = Node(val)
        val_to_node[val] = node

    for i, neighbors in enumerate(adj_list):
        val = i + 1
        for neighbor in neighbors:
            if neighbor in val_to_node:
                val_to_node[val].neighbors.append(val_to_node[neighbor])
    return val_to_node[1]


def dfs_recursive(node: Node) -> List[Node]:
    def helper(current: Node, visited: List[Node]):
        visited.append(current)
        for neighbor in current.neighbors:
            if neighbor not in visited:
                helper(neighbor, visited)

    if not node:
        return []
    visited = []
    helper(node, visited)
    return visited


def dfs_iterative(node: Node) -> List[Node]:
    if not node:
        return []
    stack = [node]
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        for neighbor in current.neighbors:
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)
    return visited


def cycle_detection(node: Node) -> bool:
    if not node:
        return False

    visited = set()
    stack = [node]
    while stack:
        current = stack.pop()
        if current in visited:
            return True
        visited.add(current)
        for neighbor in current.neighbors:
            stack.append(neighbor)
    return False


node = create_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
print("dfs_recursive", dfs_recursive(node))
print("dfs_iterative", dfs_iterative(node))
print("cycle_detection", cycle_detection(node))
