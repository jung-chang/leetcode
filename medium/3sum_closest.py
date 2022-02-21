# https://leetcode.com/problems/3sum-closest/

from typing import List, Tuple


class Solution:
    """
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        [-4,-1,1,2]

        """
        if len(nums) < 3:
            return 0

        nums.sort()
        min_diff = float("inf")
        result_sum = None
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                diff = target - three_sum
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    result_sum = three_sum
                if diff < 0:
                    k -= 1
                elif diff > 0:
                    j += 1
                else:
                    return three_sum
        return result_sum


nums = [-1, 0, 1, 1, 55]
target = 3
print(Solution().threeSumClosest(nums, target))
