# https://leetcode.com/problems/flatten-nested-list-iterator/

from typing import List, Any


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> List[Any]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        # [ [1], 2, [3, [4]] ]
        self.nums = []
        self.i = -1
        self._flatten(nestedList)

    def _flatten(self, nestedList: List[NestedInteger]):
        if nestedList is None:
            return
        for i in range(len(nestedList)):
            if nestedList[i].isInteger():
                self.nums.append(nestedList[i].getInteger())
            else:
                self._flatten(nestedList[i].getList())

    def next(self) -> int:
        if not self.hasNext():
            return None
        self.i += 1
        return self.nums[self.i]

    def hasNext(self) -> bool:
        return self.i + 1 < len(self.nums)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
