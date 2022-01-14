# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    Given linked list of length n, each node consits of a random pointer to any node or null.

    Construct a deep copy of the list of all brand new nodes.
    """

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Questions
            - Random pointer point to a node not in list?

        Example
            (a,c) -> (b,a) -> (c,d) -> (d,a) -> N
            (a,) -> (b,d) -> (c,) -> (d,) -> N

        Solution
            - Do a pass constructing next pointers and putting nodes into a map keyed by val
            - Do another pass pointing random to val

        Improvements
            -
        """

        def from_end(node: Node) -> int:
            n = 0
            cur = node
            while cur:
                n += 1
                cur = cur.next
            return n

        new_head = None
        prev = None

        nodes = []
        cur = head
        while cur:
            node = Node(cur.val)
            nodes.append(node)
            if new_head is None:
                new_head = node
            if prev:
                prev.next = node
            prev = node
            cur = cur.next

        i = 0
        cur = head
        while cur:
            if cur.random:
                n = from_end(cur.random)
                nodes[i].random = nodes[len(nodes) - n]
            i += 1
            cur = cur.next

        return new_head

    def second(self, head: Optional[Node]) -> Optional[Node]:
        """
        Map random pointers to new nodes
        """
        # key is original node, value is duplicate
        node_map = {None: None}

        new_head = None
        cur = head
        while cur:
            node = Node(cur.val)
            node_map[cur] = node
            if new_head is None:
                new_head = node
            cur = cur.next

        cur = head
        while cur:
            node_map[cur].next = node_map[cur.next]
            if cur.random:
                node_map[cur].random = node_map[cur.random]
            cur = cur.next
        return new_head


head = Node(3)
three = Node(3, None, head)
two = Node(3, three)

cur = Solution().second(head)
while cur:
    print(cur)
    cur = cur.next
