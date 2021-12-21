# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    """

    # [-2,1,-3,4,-1,2,1,-5,4]
    def first(self, nums: List[int]) -> int:
        """
        Brute force. Time limit exceeded
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_value = float("-inf")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                max_value = max(max_value, sum(nums[i:j]))
        return max_value

    def second(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_value = nums[0]
        cur_value = nums[0]
        for i in range(1, len(nums)):
            cur_value = max(nums[i], cur_value + nums[i])
            max_value = max(max_value, cur_value)
        return max_value


print(Solution().second([-2, -1]))
