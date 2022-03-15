# https://leetcode.com/problems/peeking-iterator/

from typing import List


class Iterator:
    def __init__(self, nums: List[int]):
        """
        Initializes an iterator object to the beginning of a list.
        """

    def hasNext(self) -> bool:
        """
        Returns true if the iteration has more elements.
        """

    def next(self) -> int:
        """
        Returns the next element in the iteration.
        """


class PeekingIterator:
    """
    Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.
    """

    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here.
        """
        self.iterator = iterator
        self._update_top()

    def _update_top(self):
        if self.iterator.hasNext():
            self.top = self.iterator.next()
        else:
            self.top = None

    def peek(self) -> int:
        """
        Returns the next element in the iteration without advancing the iterator.
        """
        return self.top

    def next(self) -> int:
        temp = self.top
        self._update_top()
        return temp

    def hasNext(self) -> bool:
        if self.top is None:
            return self.iterator.hasNext()
        return True


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
