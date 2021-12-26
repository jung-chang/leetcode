# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    """
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    """

    def first(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Keep to pointers for each list, swap back and forth the smallest value

        Time: O(m+n)
        Space: O(m)
        Notes:
            - Lots of tricky edge cases
        """
        if not nums2:
            return nums1
        if not m:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
        nums1_trunc = nums1[:m]
        print(nums1_trunc)
        end_index = 0
        nums1_i = 0
        nums2_i = 0

        # nums1 = [1,2,3,0,0,0], m = 3,
        # # nums2 = [2,2,6], n = 3
        while end_index < m + n:
            if nums2_i >= len(nums2):
                for i in range(nums1_i, len(nums1_trunc)):
                    nums1[end_index] = nums1_trunc[i]
                    end_index += 1
                break
            if nums1_i >= len(nums1_trunc):
                for i in range(nums2_i, len(nums2)):
                    nums1[end_index] = nums2[i]
                    end_index += 1
                break
            if nums1_i < len(nums1_trunc) and nums1_trunc[nums1_i] <= nums2[nums2_i]:
                nums1[end_index] = nums1_trunc[nums1_i]
                nums1_i += 1
            elif nums2_i < len(nums2):
                nums1[end_index] = nums2[nums2_i]
                nums2_i += 1
            end_index += 1
        return nums1


# print(Solution().first([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(Solution().first([2, 0], 1, [1], 1))
