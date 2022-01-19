# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    """
    Given an array, rotate the array to the right by k steps, where k is non-negative.
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        [1,2,3,4,5] k=3
        [3,4,5,1,2]
        """
        if len(nums) <= 1:
            return nums
        index_to_num = {}
        for i, num in enumerate(nums):
            new_index = (i + k) % len(nums)
            index_to_num[new_index] = num
        for key, val in index_to_num.items():
            nums[key] = val


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

Solution().rotate(nums, k)
print(nums)
