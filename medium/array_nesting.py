# https://leetcode.com/problems/array-nesting/

from typing import List


class Solution:
    """
    You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

    You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

        The first element in s[k] starts with the selection of the element nums[k] of index = k.
        The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
        We stop adding right before a duplicate element occurs in s[k].

    Return the longest length of a set s[k].
    """

    def arrayNesting(self, nums: List[int]) -> int:
        length = 0
        visited = [None for _ in range(len(nums))]

        def dfs(i: int, array: List[int]):
            nonlocal length

            if nums[i] in array:
                length = max(length, len(array))
                return len(array)

            if visited[i] is not None:
                length = max(length, len(array) + visited[i])
                return len(array) + visited[i]

            dfs(nums[i], array + [nums[i]])

        for i in range(len(nums)):
            dfs(i, [i])
        return length


nums = [5, 4, 0, 3, 1, 6, 2]
print(Solution().arrayNesting(nums))
