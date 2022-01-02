# https://leetcode.com/problems/3sum/

from typing import List
from collections import defaultdict


class Solution:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    """

    def first(self, nums: List[int]) -> List[List[int]]:
        """
        Return 3 different indices that sum to 0.

        Brute force is to check every triplet. Don't repeat triplets.
        """

        if len(nums) < 3:
            return []

        num_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            num_to_indices[num].append(i)
        result = set()
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            for n, m in self.two_sum(num_to_indices, nums, -1 * nums[i], i):
                triplet = tuple(sorted((nums[i], n, m)))
                if triplet not in result:
                    result.add(triplet)
                    visited.add(nums[i])
        return list(result)

    def two_sum(self, num_to_indices, nums, target, skip):
        result = set()
        for i in range(len(nums)):
            indices = num_to_indices[target - nums[i]]
            for j in indices[:2]:
                if i == j or i == skip or j == skip:
                    continue
                pair = tuple(sorted([nums[i], nums[j]]))
                if pair not in result:
                    result.add(pair)
        return result

    def second(self, nums):
        """
        Sort the list and smartly iterate through.
        """

        nums.sort()
        result = []
        visited = set()
        i = 0
        while i < len(nums):
            if nums[i] in visited:
                i += 1
                continue

            visited.add(nums[i])

            # -4 -1 -1 0 0 1 2
            left = i + 1
            right = len(nums) - 1
            while left < right:
                triplet = (nums[i], nums[left], nums[right])
                total = sum(triplet)
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append(triplet)
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result


print(Solution().second([-1, 0, 1, 2, -1, -4]))
print(Solution().second([]))
print(Solution().second([-1]))
