# https://leetcode.com/problems/find-peak-element/

from typing import List


class Solution:
    """
    A peak element is an element that is strictly greater than its neighbors.

    Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

    You may imagine that nums[-1] = nums[n] = -∞.

    You must write an algorithm that runs in O(log n) time.
    """

    def findPeakElement(self, nums: List[int]) -> int:
        """
        Can easily be done in O(n).
        We have to compare triplets at a time to determine peaks.
        We can intelligently do this:
        [1 3 2 1,1], we have 2 potential triplets [1 2 3] and [2 3 1] and [3 1 1]

        l=5, mid=2 -> check 2 if not
        check 2//1, 2+5//2 = 3, check 1 and 3if not
        Cases
            - explicit peak
            - no peaks
        """
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        visited = set()

        def is_peak(mid: int) -> bool:
            if mid == 0:
                return nums[mid] > nums[mid + 1]
            if mid == len(nums) - 1:
                return nums[mid] > nums[mid - 1]
            if nums[mid] > max(nums[mid - 1], nums[mid + 1]):
                return True
            return False

        def helper(mid: int):
            if mid in visited:
                return -1
            visited.add(mid)
            if is_peak(mid):
                return mid
            return max(helper(mid // 2), helper((len(nums) + mid) // 2))

        result = helper(len(nums) // 2)
        return result if result >= 0 else None


print(Solution().findPeakElement([6, 5, 4, 3, 4, 3]))
