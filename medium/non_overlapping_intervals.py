# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


class Solution:
    """
    Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        length = len(intervals)
        intervals.sort(key=lambda x: (x[0], x[1]))
        results = [intervals[0]]

        for i in range(1, length):
            prev_start, prev_end = results[-1]
            cur_start, cur_end = intervals[i]
            if prev_start == cur_start:
                if prev_end <= cur_end:
                    continue
                else:
                    results[-1] = intervals[i]
            elif prev_start <= cur_start < prev_end:
                if prev_end <= cur_end:
                    continue
                else:
                    results[-1] = intervals[i]
            else:
                results.append(intervals[i])
        return length - len(results)

    def first(self, intervals: List[List[int]]) -> int:
        """
        Cases
         - [1 2] [1 2], delete 1
         - [1 2] [2 3], delete 0
         - [1 3] [2 4], delete 1
         - [1 3] [2 5] [3 4], delete [2 5] over [3 4]
         - [1 3] [1 4] [2 3] [2 4]
         - [1 4] [3 5]

        - Categorize ranges by starting value, only keep smallest range. This eliminates dupes
        """
        if len(intervals) == 1:
            return 0
        length = len(intervals)
        intervals.sort(key=lambda x: (x[0], x[1]))
        print(intervals)
        i = 1
        while i < len(intervals):
            prev_start, prev_end = intervals[i - 1]
            cur_start, cur_end = intervals[i]
            if prev_start == cur_start:
                if prev_end <= cur_end:
                    intervals.pop(i)
                else:
                    intervals.pop(i - 1)
            elif prev_start <= cur_start < prev_end:
                if prev_end <= cur_end:
                    intervals.pop(i)
                else:
                    intervals.pop(i - 1)
            else:
                i += 1
        print(intervals)
        return length - len(intervals)


# print(Solution().eraseOverlapIntervals([[1, 3], [1, 4], [2, 3], [2, 4]]))

print(Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]))
