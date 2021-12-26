# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


def create_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Creates a tree from int values where children of k is 2k, 2k+1
    """
    if not values:
        return None
    root = TreeNode(values[0])
    nodes = [root]
    for i in range(len(values)):
        node = nodes.pop(0)
        if not node:
            continue
        left_i = 2 * i + 1
        right_i = left_i + 1
        if left_i < len(values) and values[left_i] is not None:
            node.left = TreeNode(values[left_i])
        if right_i < len(values) and values[right_i] is not None:
            node.right = TreeNode(values[right_i])
        nodes.extend([node.left, node.right])
    return root


def print_tree(root: TreeNode) -> None:
    """
    Prints tree out per level. Similar to breadth first search.
    """
    levels = [[root]]
    while levels[-1]:
        cur_level = []
        for node in levels[-1]:
            if node is None:
                cur_level.extend([None, None])
            else:
                cur_level.append(node.left)
                cur_level.append(node.right)
        if cur_level == [None] * len(cur_level):
            break
        levels.append(cur_level)
    for level in levels:
        for node in level:
            print(node.val if node else "N", end=" ")
        print()


def breadth_first_traversal(root: TreeNode):
    queue = [root]
    path = []
    while queue:
        node = queue.pop(0)
        path.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return path


def breadth_first_traversal_recursive(root: TreeNode, q=None):
    if q is None:
        q = [root]
    if not q:
        return []
    node = q.pop(0)
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)
    return [node] + breadth_first_traversal_recursive(root, q)


def preorder_dfs_recursive(root: TreeNode):
    if not root:
        return []
    return (
        [root] + preorder_dfs_recursive(root.left) + preorder_dfs_recursive(root.right)
    )


def inorder_dfs_recursive(root: TreeNode):
    if not root:
        return []
    return inorder_dfs_recursive(root.left) + [root] + inorder_dfs_recursive(root.right)


def postorder_dfs_recursive(root: TreeNode):
    if not root:
        return []
    return (
        postorder_dfs_recursive(root.left)
        + postorder_dfs_recursive(root.right)
        + [root]
    )


def preorder_dfs(root: TreeNode):
    stack = [root]
    path = []
    while stack:
        node = stack.pop()
        path.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return path


def postorder_dfs(root: TreeNode):
    stack = [root]
    path = []
    while stack:
        node = stack.pop()
        path.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return path


lvls = 4
root = create_tree([i for i in range(1, 2 ** lvls)])
print_tree(root)

print("BFS", breadth_first_traversal(root))
print("DFS preorder", preorder_dfs_recursive(root))
print("DFS inorder", inorder_dfs_recursive(root))
print("DFS postorder", postorder_dfs_recursive(root))

print("BFS recursive", breadth_first_traversal_recursive(root))
print("DFS preorder recursive", preorder_dfs_recursive(root))
