# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """

    def first(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        No need to reverse. Just sum from back and track carry overs.

        Time: O(l1 + l2)
        Space: O(1) for carry
        """

        carry = 0
        root = None
        cur = ListNode()
        while l1 or l2:
            value = carry
            if l1 and l2:
                value += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                value += l1.val
                l1 = l1.next
            else:
                value += l2.val
                l2 = l2.next

            if value >= 10:
                carry = 1
                value -= 10
            else:
                carry = 0

            if cur.next is None:
                cur.next = ListNode(value)
            if root is None:
                root = cur.next
            cur = cur.next

        if not carry:
            return root
        else:
            cur.next = ListNode(1)
        return root

    def second(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Recursive implementation.

        At every step, pass the carry and step forward.
        """

        def helper(n1, n2, carry):
            value = carry
            if not n1 and not n2:
                if carry:
                    return ListNode(1)
                return None

            if n1 and n2:
                value += n1.val + n2.val
                n1 = n1.next
                n2 = n2.next
            elif n1 and not n2:
                value += n1.val
                n1 = n1.next
            else:
                value += n2.val
                n2 = n2.next

            if value >= 10:
                carry = 1
                value -= 10
            else:
                carry = 0

            cur = ListNode(value)
            cur.next = helper(n1, n2, carry)
            return cur

        cur = ListNode()
        cur.next = helper(l1, l2, 0)
        return cur.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(9)
# l2.next.next.next = ListNode(9)

root = Solution().second(l1, l2)
while root:
    print(root.val)
    root = root.next
