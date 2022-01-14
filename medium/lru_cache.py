# https://leetcode.com/problems/lru-cache/

from typing import Optional


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        return f"Node({self.key})"


class LRUCache:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
    The functions get and put must each run in O(1) average time complexity.

    Thoughts
        - O(1) -> dictionary involved for get/put
        - Keys are discarded in the order of least recently used
        - Use some sort of counter and track the min

    Case
        - get on empty
        - get on non exists
        - get success will update LRU
        - put on size = capacity
        - put on existing key
        - put success will update LRU
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity.
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.node_map = {}

    def get(self, key: int) -> int:
        """
        Return the value of the key if the key exists, otherwise return -1.
        """
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        """
        if key in self.node_map:
            self._remove(self.node_map[key])
            self.node_map.pop(key)

        node = Node(key, value)
        self._add(node)
        self.node_map[key] = node
        if len(self.node_map) > self.capacity:
            self.node_map.pop(self.tail.key)
            self._remove(self.tail)

    def _remove(self, node: Node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
            return
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            return

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def _add(self, node: Node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node


command = [
    "LRUCache",
    "put",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "put",
    "get",
    "put",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "get",
    "get",
    "put",
    "put",
    "get",
    "get",
    "get",
    "put",
    "put",
    "get",
    "put",
    "get",
    "put",
    "get",
    "get",
    "get",
    "put",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "get",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "get",
    "put",
    "get",
    "get",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "put",
    "get",
    "get",
    "get",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "get",
    "get",
    "get",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "put",
    "put",
    "put",
    "put",
]
argument = [
    [10],
    [10, 13],
    [3, 17],
    [6, 11],
    [10, 5],
    [9, 10],
    [13],
    [2, 19],
    [2],
    [3],
    [5, 25],
    [8],
    [9, 22],
    [5, 5],
    [1, 30],
    [11],
    [9, 12],
    [7],
    [5],
    [8],
    [9],
    [4, 30],
    [9, 3],
    [9],
    [10],
    [10],
    [6, 14],
    [3, 1],
    [3],
    [10, 11],
    [8],
    [2, 14],
    [1],
    [5],
    [4],
    [11, 4],
    [12, 24],
    [5, 18],
    [13],
    [7, 23],
    [8],
    [12],
    [3, 27],
    [2, 12],
    [5],
    [2, 9],
    [13, 4],
    [8, 18],
    [1, 7],
    [6],
    [9, 29],
    [8, 21],
    [5],
    [6, 30],
    [1, 12],
    [10],
    [4, 15],
    [7, 22],
    [11, 26],
    [8, 17],
    [9, 29],
    [5],
    [3, 4],
    [11, 30],
    [12],
    [4, 29],
    [3],
    [9],
    [6],
    [3, 4],
    [1],
    [10],
    [3, 29],
    [10, 28],
    [1, 20],
    [11, 13],
    [3],
    [3, 12],
    [3, 8],
    [10, 9],
    [3, 26],
    [8],
    [7],
    [5],
    [13, 17],
    [2, 27],
    [11, 15],
    [12],
    [9, 19],
    [2, 15],
    [3, 16],
    [1],
    [12, 17],
    [9, 1],
    [6, 19],
    [4],
    [5],
    [5],
    [8, 1],
    [11, 7],
    [5, 2],
    [9, 28],
    [1],
    [2, 2],
    [7, 4],
    [4, 22],
    [7, 24],
    [9, 26],
    [13, 28],
    [11, 26],
]
expected = [
    None,
    None,
    None,
    None,
    None,
    None,
    -1,
    None,
    19,
    17,
    None,
    -1,
    None,
    None,
    None,
    -1,
    None,
    -1,
    5,
    -1,
    12,
    None,
    None,
    3,
    5,
    5,
    None,
    None,
    1,
    None,
    -1,
    None,
    30,
    5,
    30,
    None,
    None,
    None,
    -1,
    None,
    -1,
    24,
    None,
    None,
    18,
    None,
    None,
    None,
    None,
    -1,
    None,
    None,
    18,
    None,
    None,
    -1,
    None,
    None,
    None,
    None,
    None,
    18,
    None,
    None,
    -1,
    None,
    4,
    29,
    30,
    None,
    12,
    -1,
    None,
    None,
    None,
    None,
    29,
    None,
    None,
    None,
    None,
    17,
    22,
    18,
    None,
    None,
    None,
    -1,
    None,
    None,
    None,
    20,
    None,
    None,
    None,
    -1,
    18,
    18,
    None,
    None,
    None,
    None,
    20,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]

cache = None
for i, c in enumerate(command):
    if c == "LRUCache":
        cache = LRUCache(argument[i][0])
    elif c == "put":
        key, val = argument[i]
        print("put", key, val)
        cache.put(key, val)
    elif c == "get":
        print("get", argument[i][0], end=" ")
        got = cache.get(argument[i][0])
        print(got, "=", expected[i])
        assert got == expected[i]
    print()
