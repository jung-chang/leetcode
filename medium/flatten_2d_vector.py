# https://leetcode.com/problems/flatten-2d-vector/
# https://aaronice.gitbook.io/lintcode/data_structure/flatten-2d-vector

from typing import List


class Vector:
    """
    Design and implement an iterator to flatten a 2d vector. It should support the following operations:nextandhasNext.

    Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

    iterator.next(); // return 1
    iterator.next(); // return 2
    iterator.next(); // return 3
    iterator.hasNext(); // return true
    iterator.hasNext(); // return true
    iterator.next(); // return 4
    iterator.hasNext(); // return false
    """

    def __init__(self, nums: List[List[int]]):
        i = 0
        j = 0

    def next(self):
        pass

    def hasNext(self):
        pass
