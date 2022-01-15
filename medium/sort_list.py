# https://leetcode.com/problems/sort-list/

from typing import Optional
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"


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
        """
        if not head:
            return None

        done = False
        while not done:
            done = True
            left = None
            cur = head
            right = cur.next
            print(head, left, cur, right)
            while right and cur.val <= right.val:
                left = cur
                cur = right
                right = right.next
                continue

            while right and cur.val > right.val:
                print()
                print("swap", cur, right)
                done = False
                temp = right.next
                right.next = cur
                cur.next = temp
                if left:
                    left.next = right
                if cur == head:
                    head = right
                left = right
                right = cur.next
                print_list(head)
                print(head, left, cur, right)
        return head

    def second(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Use dictionary.
        """
        if not head:
            return None
        nodes = defaultdict(list)
        cur = head
        while cur:
            nodes[cur.val].append(cur)
            cur = cur.next

        node_list = []
        for key in sorted(nodes.keys()):
            node_list.extend(nodes[key])

        head = node_list[0]
        prev = head
        for i in range(1, len(node_list)):
            prev.next = node_list[i]
            prev = prev.next
        node_list[-1].next = None
        return head

    def merge_sort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left: Optional[ListNode], right: Optional[ListNode]):
            l = left
            r = right
            head = ListNode()
            cur = head
            while l and r:
                if l.val <= r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            if l:
                cur.next = l
            if r:
                cur.next = r
            return head.next

        def get_mid(node: ListNode):
            length = 0
            cur = node
            while cur:
                length += 1
                cur = cur.next
            prev = None
            cur = node
            for _ in range(length // 2):
                prev = cur
                cur = cur.next
            prev.next = None
            return cur

        if not head:
            return None
        if not head.next:
            return head
        mid = get_mid(head)
        return merge(self.merge_sort(head), self.merge_sort(mid))


def print_list(node):
    cur = node
    while cur:
        print(cur, end=" ")
        cur = cur.next
    print()


def create_list(vals):
    head = None
    prev = None
    for val in vals:
        node = ListNode(val)
        if not head:
            head = node
        if not prev:
            prev = node
        else:
            prev.next = node
            prev = prev.next
    return head


head = create_list([6, 2, 7, -1, -2, 3, -2, -3])

print("Original")
print_list(head)

head = Solution().merge_sort(head)
print("Sorted")
print_list(head)
