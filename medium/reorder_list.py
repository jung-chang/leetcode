# https://leetcode.com/problems/reorder-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __reprr__(self):
        return str(self.val)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Flip second half
        prev = None
        cur = slow.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        slow.next = None

        # Merge
        

    def first(self, head: Optional[ListNode]) -> None:
        """
        You are given the head of a singly linked-list. The list can be represented as:

        L0 → L1 → … → Ln - 1 → Ln

        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

        You may not modify the values in the list's nodes. Only nodes themselves may be changed.

        1 2 3 4
        1 4 2 3

        1 2 3 4 5
        1 5 2 3 4
        """

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        if len(nodes) <= 1:
            return

        start = 0
        end = len(nodes) - 1

        while start <= end:
            temp = nodes[start].next
            nodes[start].next = nodes[end]
            nodes[end].next = temp
            if start + 1 == end:
                temp.next = None
                break
            elif start == end:
                nodes[end + 1].next = nodes[start]
                nodes[start].next = None
                break
            start += 1
            end -= 1
        return nodes[0]


def create(arr):
    root = ListNode(0)
    cur = root
    for num in arr:
        node = ListNode(num)
        cur.next = node
        cur = node
    return root.next


def print_nodes(node):
    result = []
    cur = node
    while cur:
        result.append(cur.val)
        if len(result) >= 10:
            break
        cur = cur.next
    print(result)


print_nodes(Solution().reorderList(create([1, 2, 3, 4, 5])))
# print_nodes(Solution().reorderList(create([1, 2, 3, 4, 5, 6])))
