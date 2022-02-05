# https://leetcode.com/problems/first-missing-positive/

from typing import List


class Solution:
    """
    Given an unsorted integer array nums, return the smallest missing positive integer.

    You must implement an algorithm that runs in O(n) time and uses constant extra space.
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        7 6 5 2 4 1

        4 3 2 1 8

        1. Keep track of min/max ranges?
        2. set the numth element

        """
        for i in range(len(nums)):
            if isinstance(nums[i], tuple):
                _, num = nums[i]
            else:
                num = nums[i]
            if num <= 0:
                continue
            if 0 <= num - 1 < len(nums):
                if isinstance(nums[num - 1], tuple):
                    continue
                print(num - 1)
                nums[num - 1] = (1, nums[num - 1])

        i = 0
        while i < len(nums):
            if not isinstance(nums[i], tuple):
                return i + 1
            i += 1
        return i + 1

    def nlogn(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        for num in nums:
            if num <= 0:
                continue
            if num == i:
                i += 1
        return i


print(Solution().firstMissingPositive([3, 4, -1, 1]))
