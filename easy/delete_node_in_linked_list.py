# https://leetcode.com/problems/delete-node-in-a-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Write a function to delete a node in a singly-linked list.
    You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

    It is guaranteed that the node to be deleted is not a tail node in the list.
    """

    def first(self, node: ListNode):
        """
        Cant use prev and skip current node. Have to replace all nodes after given with next one.
        """
        # 1 2 N
        # n t
        if not node:
            return
        if not node.next:
            return
        node.val = node.next.val
        node.next = node.next.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

Solution().first(head.next)

while head:
    print(head.val)
    head = head.next
