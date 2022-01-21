# https://leetcode.com/problems/kth-largest-element-in-an-array/


from collections import defaultdict
from typing import List
import heapq


class Solution:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    """

    def first(self, nums: List[int], k: int) -> int:
        """
        Just sort it and iterate OR sort it and binary search. -> O(n log n)
        """
        return sorted(list(nums))[-k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return

        pivot = nums[0]
        less = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        greater = [num for num in nums if num > pivot]

        if k <= len(greater):
            return self.findKthLargest(greater, k)
        elif k > len(greater) + len(equal):
            return self.findKthLargest(less, k - len(greater) - len(equal))
        else:
            return equal[0]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
