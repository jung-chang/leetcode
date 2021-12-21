# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    """
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
    """

    def first(self, nums: List[int]) -> int:
        """
        Keep 2 indices, end of the array and current comparison
        """
        # 1 2 3 4
        # 1 2 2 3
        #   e   c
        end = 0
        cur = end + 1
        while cur < len(nums):
            if nums[cur] != "_" and nums[cur] > nums[end]:
                if cur - end == 1:
                    end += 1
                    cur += 1
                else:
                    nums[end + 1] = nums[cur]
                    nums[cur] = "_"
                    end += 1
            else:
                nums[cur] = "_"
                cur += 1
        return end + 1, nums


print(Solution().first([1, 1, 2]))
