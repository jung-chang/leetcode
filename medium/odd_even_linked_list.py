# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

    The first node is considered odd, and the second node is even, and so on.

    Note that the relative order inside both the even and odd groups should remain as it was in the input.
    """

    def brute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Use O(n) space and keep track of the nodes in list or hashmap
        2. Recursively do this
        """
        if not head:
            return head

        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        head = nodes[0]
        cur = head
        for i in range(2, len(nodes), 2):
            cur.next = nodes[i]
            cur = cur.next
        for i in range(1, len(nodes), 2):
            cur.next = nodes[i]
            cur = cur.next
        cur.next = None
        return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive implementation
        """
        last_odd = None
        def link(odd: ListNode, even: ListNode) -> ListNode:
            nonlocal last_odd

            if not odd and not even:
                return
            if odd:
                if odd and odd.next and odd.next.next:
                    odd.next = odd.next.next
                else:
                    odd.next = None
                    last_odd = odd

            if even:
                if even.next and even.next.next:
                    even.next = even.next.next
                else:
                    even.next = None

            link(odd.next if odd else None, even.next if even else None)
            return odd, even

        if not head:
            return head
        odd, even = link(head, head.next)
        last_odd.next = even
        return odd
