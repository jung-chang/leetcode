# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
    """

    def search(self, nums: List[int], target: int) -> int:
        def bin_search(start: int, end: int):
            if start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                return bin_search(start, mid - 1)
            else:
                return bin_search(mid + 1, end)

        return bin_search(0, len(nums) - 1)


n = [-1, 0, 3, 5, 9, 12]
t = 5


print(Solution().search(n, t))
