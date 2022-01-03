# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    """
    Array sorted in ascending order, distinct integers.

    Possibly rotated on a pivot index, k (i <= k <= length)

    [0,1,2,3,4,5,6,7]
    [4,5,6,7,0,1,2,3]

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    """

    def first(self, nums: List[int], target: int) -> int:
        """
        Questions:
            - How many numbers are there in the list?
            - How big/small can the numbers be?
            - Are there repeating numbers?

        Construct non rotated list and binary search. O(n) + O(log2 n)
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            if nums[i] <= nums[i - 1]:
                break
            i += 1

        if i >= len(nums):
            return -1

        if target > nums[i]:
            index = self.binary_search(nums[i:], target)
            if index == -1:
                return index
            return i + index
        else:
            return self.binary_search(nums[:i], target)

    def binary_search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        middle = len(nums) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            index = self.binary_search(nums[middle:], target)
            return index if index == -1 else index + middle
        else:
            return self.binary_search(nums[:middle], target)

    def search(self, nums: List[int], target: int) -> int:
        """
        Worst is not rotated. O(n)
        Best is rotated at max pivot [9 0 1 2 3 4 5], or if target in the front

        [4 5 6 7 0 1 2], length=7, target=1
        mid=3, nums[3]=7, nums[:3]= [3 4 5] + [7 0 1 2]
        if nums[:mid][0] > target or nums[:mid][-1] < target -> search right
        else search left

        [7 0 1 2], length=4, target=7
        mid=2, nums[mid]=1, nums[:mid]=[7]
        """

        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        mid = len(nums) // 2
        if nums[mid] == target:
            return mid

        # [7, 8, 1, 2, 3, 4, 5, 6], mid=4, target=2
        left = nums[:mid]  # 7 8 1 2
        right = nums[mid + 1 :]  # 4 5 6

        index = -1
        adds = 0
        if right and right[0] <= right[-1]:
            if target >= right[0] and target <= right[-1]:
                index = self.search(right, target)
                adds = mid + 1
            else:
                index = self.search(left, target)
        elif left and left[0] <= left[-1]:
            if target >= left[0] and target <= left[-1]:
                index = self.search(left, target)
            else:
                index = self.search(right, target)
                adds = mid + 1

        if index == -1:
            return index
        return index + adds


print(Solution().search([1, 3], 3))
