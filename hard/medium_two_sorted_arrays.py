# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Median is the middle number or if middles, the avg of that.

        Merge and binary search middle -> O(m+n)
        2 4 6
        1 3 5 7
        1 2 3 4 5 6 7 -> 4

        1 2 3
        4 5 6

        2 cases:
            - lists do not overlap -> easy just figure out where the median is
            - lists overlap ->

        2 4 6 7, 24 67
        1 3 5 7, 13 57



        mid -> all nums < mid, check total length
        """

        def helper(a: List[int], b: List[int], k: int) -> int:
            if not a:
                return b[k]
            if not b:
                return a[k]

            mid_a = len(a) // 2
            mid_b = len(b) // 2
            ma, mb = a[mid_a], b[mid_b]

            if mid_a + mid_b < k:
                # b's first half doesnt include k
                if ma > mb:
                    return helper(a, b[mid_b + 1 :], k - mid_b - 1)
                # a's first half doesnt include k
                else:
                    return helper(a[mid_a + 1 :], b, k - mid_a - 1)
            else:
                # a's latter half doesnt include k
                if ma > mb:
                    return helper(a[:mid_a], b, k)
                # b's latter half doesnt include k
                else:
                    return helper(a, b[:mid_b], k)

        l1, l2 = len(nums1), len(nums2)
        length = l1 + l2
        if not l1 and not l2:
            return 0

        mid = length // 2
        if length % 2 == 0:
            return (helper(nums1, nums2, mid) + helper(nums1, nums2, mid - 1)) / 2
        else:
            return helper(nums1, nums2, mid)


print(Solution().findMedianSortedArrays([2, 4, 6], [1, 3, 5]))
