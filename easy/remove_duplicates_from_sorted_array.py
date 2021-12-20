# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    """
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
    """

    def first(self, nums: List[int]) -> int:
        # 1 1 1 2 3
        if not nums:
            return nums
        end = 1
        cur = end + 1
        end_val = nums[0]
        while cur < len(nums):
            if nums[cur] > end_val:

                end_val = nums[i]
                end = i + 1
