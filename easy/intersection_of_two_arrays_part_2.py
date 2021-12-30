# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List
from collections import defaultdict


class Solution:
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        aMap = defaultdict(lambda: 0)
        for num in nums1:
            aMap[num] += 1

        bMap = defaultdict(lambda: 0)
        for num in nums2:
            bMap[num] += 1

        intersection = set(aMap.keys()).intersection(set(bMap.keys()))
        intersect = []
        for num in intersection:
            intersect.extend([num] * min(aMap[num], bMap[num]))
        return intersect

    def second(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Sort and iterate.
        """
        nums1.sort()
        nums2.sort()
        i1 = 0
        i2 = 0
        intersect = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                intersect.append(nums1[i1])
                i1 += 1
                i2 += 1
        return intersect
