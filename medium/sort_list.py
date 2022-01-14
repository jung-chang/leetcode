# https://leetcode.com/problems/sort-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given the head of a linked list, return the list after sorting it in ascending order.
    """

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Use n space and put them in a list and sort. Then re form the linked list

        Bubble up each node if smaller val.

        Boot head to where its supposed to be until no longer.

        Cases:
            - Empty head
            - Single node
            - Already sorted
            - Reversed sorted = Not sorted from the start
            - Sorted up to a point

        1 2 3 N
        3 2 1 N, 2 1 3 N, 1 2 3 N
        2 1 3 N, 1 2 3 N
        1 3 2 N


        1 7 2 4 5 6 N
        l c r
        h
        """
        if not head:
            return None


root = ListNode(6)

head = ListNode(-1)
root.next = head
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)

head = Solution().sortList(root)
while head:
    print(head.val)
    head = head.next
