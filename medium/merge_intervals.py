# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Examples
            [0, 3] [1, 2] [2, 5] [7, 8]
            [0 5] [7 8]
            [[1,3],[2,6],[8,10],[15,18]]

        Questions
            Negative integers are present?
            How many intervals are there in total?
            Any technical constraints?
            Can I assume that starti < endi?

        [0, 3] [1, 2] [2, 5] [7, 8]
        Iterative through intervals, checking if cur interval is
            1. within an interval
            2. expands an interval (left, right, both)
            3. not within an interval, add this interval

        [1,2] [4,5] [2,3] -> [1,5]
        Issues
            How to find the interval we want to compare to
            Once we merge, consider merging of the new interval to other intervals

        Solution
            1. Make one big list of numbers in all intervals, and then chop the intervals
        """
        # Test 1
        # [1 3] [4 5] [4 9] [7 12]
        # a b = 1 3, c d = 4 5
        # result = [1 5] [4 9] [7 12]
        # ab=15, cd=49, result = [1 9] [7 12]
        # ab=19, cd=7 12, result= [1 12]

        # Test 2
        # [1 3] [5 8] [6 8] [10 11]
        # ab=13, cd=58, result same
        # resut= [1 3] [5 8]
        if not intervals:
            return [[]]
        intervals = sorted(intervals, key=lambda r: r[0])
        result = []
        r = 0
        while r < len(intervals):
            if not result:
                result.append(intervals[r])
                r += 1
                continue
            a, b = result[-1]
            c, d = intervals[r]
            if (b >= c and b <= d) or (c >= a and c <= b):
                result[-1] = [min(a, c), max(b, d)]
            else:
                result.append([c, d])
            r += 1
        return result


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 4], [4, 5]]))
