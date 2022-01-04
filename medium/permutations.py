# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    """
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        [1,2] [2,1]

        [1,2,3]

        [1,2,3], [1,3,2]
        [2,1,3] [2,3,1]
        [3,1,2] [3,2,1]

        Can do this iteratively or recursively.

        Recursive implementation:
            - For every num in nums, prefix to all permutations to sub array.
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        permutations = []
        for i in range(len(nums)):
            sub_permutations = self.permute(nums[:i] + nums[i + 1 :])
            for permutation in sub_permutations:
                permutations.append([nums[i]] + permutation)
        return permutations

    def second(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative, add a prefix to all sub permutations.

        For each number, add subsequent numbers in between every index.
        1
            21
                321 231 213
            12
                312 132 123
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        permutations = []
        sub_permutations = [[nums[0]]]
        while sub_permutations:
            sub = sub_permutations.pop(0)
            if len(sub) == len(nums):
                permutations.append(sub)
                continue
            for j in range(len(sub) + 1):
                num = nums[len(sub)]
                sub_permutations.append(sub[:j] + [num] + sub[j:])
        return permutations


print(Solution().second([1, 2, 3, 4]))
