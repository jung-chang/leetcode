# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    """
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    """

    def first(self, nums: List[int]) -> int:
        """
        Generate list and substract.
        """
        target = set([i for i in range(len(nums) + 1)])
        return (target - set(nums)).pop()

    def second(self, nums: List[int]) -> int:
        """
        Sort and iterate and check.
        """
        length = len(nums)
        if length == 1:
            return 1 - nums[0]
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if i != num:
                return i
        if nums[-1] != length:
            return length


print(Solution().second([0]))
