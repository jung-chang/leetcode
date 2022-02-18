# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    """
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    """

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        Recurisviely go through tree, forming a set of all children of a node and check if p and q are in there.
        """

        ancestor = None

        def get_children(node: TreeNode):
            nonlocal ancestor

            if not node:
                return set()

            children = set([node])
            if node.left:
                children.add(node.left)
                children.update(get_children(node.left))
            if node.right:
                children.add(node.right)
                children.update(get_children(node.right))

            if p in children and q in children and not ancestor:
                ancestor = node
            return children

        get_children(root)
        return ancestor if ancestor else root


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(Solution().second(root, root.left, root.left.right.right))
