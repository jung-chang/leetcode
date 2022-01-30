# https://leetcode.com/problems/wiggle-sort-ii/

from typing import List


class Solution:
    """
    Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
    """

    def iterative(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Examples
          [1 2 3 4 5]
          [1 3 2 5 4]

        1. Sort, divide in half, and interleave. Doesn't work.
        2. Split array until <= 3
        """

        nums.sort()
        mid = len(nums) // 2

        small = nums[:mid][::-1]
        big = nums[mid:][::-1]

        i = 0
        while small and big:
            if i % 2 == 0:
                nums[i] = small.pop(0)
                i += 1
            else:
                nums[i] = big.pop(0)
                i += 1

        if big:
            for j in range(len(big)):
                nums[i + j] = big[j]
        elif small:
            for j in range(len(small)):
                nums[i + j] = small[j]

    def wiggleSort(self, nums: List[int]) -> None:
        arr = sorted(nums)
        for i in range(1, len(nums), 2):
            nums[i] = arr.pop()
        for i in range(0, len(nums), 2):
            nums[i] = arr.pop()


# a < b > c < d > e...
# 1 1 2 2 3 3
# 1 2 1 2 3 3
n = [1, 3, 2, 2, 3, 1]
n = [1, 1, 2, 1, 2, 2, 1]


Solution().wiggleSort(n)
