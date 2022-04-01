# https://leetcode.com/problems/my-calendar-i/

from __future__ import annotations
from collections import defaultdict


class Block:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def overlaps_with(self, event: Block) -> bool:
        """
          [   )
            [   )
        [   )
            [)
        """
        if event.start <= self.start < event.end:
            return True
        if event.start < self.end <= event.end:
            return True
        if event.start >= self.start and event.end <= self.end:
            return True
        return False


class MyCalendar:
    """
    You are implementing a program to use as your calendar.
    We can add a new event if adding the event will not cause a double booking.
    A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

    The event can be represented as a pair of integers start and end that represents a booking on the half-open interval
    [start, end), the range of real numbers x such that start <= x < end.
    """

    def __init__(self):
        """
        Questions
            - Times are given as ints. Is there a concept of today/yesterday/tomorrow?
            - These can also be abstracted away by using time since epoch

        Event times are represented with [start, end). Double books mean start overlaps with end.

        2 types of overlaps:
            - partial overlaps
            - complete overlaps

        Data structure
            - What information do we have at book time (start, end)
            - To determine overlap, we need to compare events that start around same time
            - Ordered list of start,end times. Iterate through the list and check for overlaps
            - Similar to merge intervals questions
        """
        self.events = []
        pass

    def book(self, start: int, end: int) -> bool:
        """
        Returns true if the event can be added to the calendar successfully without causing a double booking.
        Otherwise, return false and do not add the event to the calendar.
        """
        new_event = Block(start, end)
        for i, event in enumerate(self.blocks):
            if event.overlaps_with(new_event):
                return False
        return True


class Node:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, node):
        if self.end <= node.start:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        return False


class MyCalendar:
    """
    Use balanced tree.
    """

    def __init__(self):
        self.root = None

    def _insert_node(self, node: Node):
        return self.root.insert(node)

    def book(self, start: int, end: int) -> bool:
        """
        Returns true if the event can be added to the calendar successfully without causing a double booking.
        Otherwise, return false and do not add the event to the calendar.
        """
        node = Node(start, end)
        if not self.root:
            self.root = node
            return True
        return self._insert_node(node)


cal = MyCalendar()
print(cal.book(10, 20))
print(cal.events)

print(cal.book(15, 25))
print(cal.events)

print(cal.book(20, 30))
print(cal.events)

print(cal.book(20, 21))
print(cal.events)
