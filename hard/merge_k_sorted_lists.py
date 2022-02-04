# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __repr__(self):
    #     return f"{self.val}"


class Solution:
    """
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        node_to_i = {}
        min_heap = []
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(min_heap, (lists[i].val, lists[i]))
            node_to_i[lists[i]] = i

        head = ListNode()
        cur = head
        while min_heap:
            _, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next

            i = node_to_i[node]
            lists[i] = lists[i].next
            if lists[i] is not None:
                heapq.heappush(min_heap, (lists[i].val, lists[i]))
                node_to_i[lists[i]] = i
            node_to_i.pop(node)
        return head.next


def create_list(nums):
    head = ListNode()
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next


def print_list(root):
    nums = []
    cur = root
    while cur:
        nums.append(cur.val)
        cur = cur.next
    print(nums)


a = create_list([1, 3, 5])
b = create_list([2, 4, 6, 7, 8, 8, 9, 9, 10])

root = Solution().mergeKLists([a, b])
print_list(root)
