# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Recursive implementation, keeping track of nth number.
        """

        # 1 2 3 4 N
        # 2nd from last -> 4 - 2 = 2
        # 1st from last -> 4 - 1 = 3
        # 3rd from last -> 4 - 3 = 1
        # 4th from last -> 4 - 4 = 0

        # n = 3

        def helper(node, nth, n):
            if not node.next:
                return node, nth
            # 1, 4
            next_node, max_nth = helper(node.next, nth + 1, n)
            if max_nth - n == nth:
                node.next = next_node.next
            return node, max_nth

        if not head:
            return None
        if not n:
            return head
        _, max_nth = helper(head, 1, n)
        if max_nth == n:
            return head.next
        return head

    def iterative(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Iterative implementation. Find total length, and then iterate again.
        """
        if not head:
            return None
        if not n:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length == n:
            return head.next

        node = head
        for _ in range(length - n - 1):
            node = node.next
        node.next = node.next.next
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

root = Solution().iterative(head, 3)
while root:
    print(root.val)
    root = root.next
