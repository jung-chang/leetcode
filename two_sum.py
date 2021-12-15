# https://leetcode.com/problems/two-sum/

from collections import defaultdict
from typing import List


class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    """

    def first(self, nums: List[int], target: int) -> List[int]:
        """O(n^2) runtime"""
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

    def second(self, nums: List[int], target: int) -> List[int]:
        """
        For each index, value, find the complementary value to sum to target.

        Time complexity: O(n)
        Space complexity: O(n) from dict
        """
        num_to_index = defaultdict(list)
        for index, value in enumerate(nums):
            num_to_index[value].append(index)

        for index, value in enumerate(nums):
            complementary_indices = num_to_index.get(target - value)
            if complementary_indices is None:
                continue
            if value == target - value:
                if len(complementary_indices) > 1:
                    return complementary_indices[:2]
                else:
                    continue
            else:
                return [index, complementary_indices[0]]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(self.first(nums, target))
        print(self.second(nums, target))


Solution().twoSum([3, 2, 4], 6)
