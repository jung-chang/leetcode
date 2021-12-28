# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.
    """

    def first(self, head: Optional[ListNode]) -> bool:
        """
        Keep 2 pointers. Advance at different rate and check if they land on same node.
        """
        if not head:
            return False
        i = head
        j = head.next
        while j is not None and i != j:
            i = i.next
            j = j.next
            if j:
                j = j.next
        return i == j


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(Solution().first(head))
