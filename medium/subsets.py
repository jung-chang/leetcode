# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Questions
            - How many nums?
            - Is there an order?
            - Technical constraints?
            - We are simply just looking at combinations (subsets) from 1 to n?

        Examples
            - [0 1 2] -> [0, 1, 2, 01, 02, 12, 012]
            - [0 1 2 3] -> [0, 1, 2, 3, 01, 02, 03, 12, 13, 23, ]

        Solution
            - Create empty/single subsets. Iterate through them and add the next num, keeping track of the index.
        """

        if not nums:
            return []

        result = []
        queue = [([num], i) for i, num in enumerate(nums)]
        while queue:
            subset, i = queue.pop(0)
            if i >= len(nums) - 1:
                result.append(subset)
            else:
                result.append(subset)
                for j in range(i + 1, len(nums)):
                    new_subset = subset + [nums[j]]
                    queue.append((new_subset, j))
        return [[]] + result


print(Solution().subsets([0, 1, 2, 3]))
