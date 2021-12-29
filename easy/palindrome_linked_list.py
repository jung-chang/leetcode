# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printList(self, node: ListNode):
        nodes = []
        while node:
            nodes.append(node.val)
            node = node.next
        print(nodes)

    def reverse(self, node: ListNode):
        # 1 2 3 N
        prev = None
        cur = node
        while cur.next:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        cur.next = prev
        return cur

    def first(self, head: Optional[ListNode]) -> bool:
        """
        Find total length, reverse half forward, iterate and compare.
        """
        if not head:
            return False
        if not head.next:
            return True

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        cur = head
        for _ in range(length // 2):
            cur = cur.next

        if length % 2 == 1:
            cur = cur.next
        cur = self.reverse(cur)

        cur2 = head
        self.printList(cur2)
        self.printList(cur)
        while cur:
            if cur is None and cur2 is None:
                continue
            if cur and not cur2:
                return False
            if cur.val != cur2.val:
                return False
            cur = cur.next
            cur2 = cur2.next
        return True


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(Solution().first(head))

# sol = Solution()
# sol.printList(sol.reverse(head))
