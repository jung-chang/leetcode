# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
    """

    def first(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Go through both linked lists while storing one set of nodes.

        Uses lots of space.
        """
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next
        while headB:
            if headB in visited:
                return headB
            headB = headB.next
        return None

    def first(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Get lengths of both lists and then iterate again.
        """
        if not headB and not headA:
            return None

        def _GetLength(node: ListNode) -> int:
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        lenA = _GetLength(headA)
        lenB = _GetLength(headB)

        if lenA <= lenB:
            for _ in range(lenB - lenA):
                headB = headB.next
        else:
            for _ in range(lenA - lenB):
                headA = headA.next

        while headA or headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
