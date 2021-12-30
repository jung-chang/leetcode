# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Bubble up non zero numbers.
        """
        zero_i = 0
        while zero_i < len(nums) - 1 and nums[zero_i] != 0:
            zero_i += 1
        if zero_i >= len(nums) - 1:
            return

        i = zero_i
        while i < len(nums):
            if nums[i] != 0:
                nums[zero_i] = nums[i]
                nums[i] = 0
                zero_i += 1
            i += 1


Solution().moveZeroes([1, 2])
Solution().moveZeroes([1])
Solution().moveZeroes([0])
Solution().moveZeroes([0, 0])
Solution().moveZeroes([0, 0, 1, 2, 0, 0, 0, 3, 1, 0])
