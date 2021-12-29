# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    """

    def first(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Iterative"""
        cur = head
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next

        cur = None
        root = None
        while stack:
            node = stack.pop()
            if root is None:
                root = node
            if cur is None:
                cur = node
            else:
                cur.next = node
                cur = node
        cur.next = None
        return root

    def second(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive"""

        def helper(node: Optional[ListNode]):
            # 1 2 3 N
            if not node.next:
                return node, node
            next_node, root = helper(node.next)
            next_node.next = node
            return node, root

        if not head:
            return None
        _, root = helper(head)
        head.next = None
        return root


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

root = Solution().second(head)

while root:
    print(root.val)
    root = root.next
