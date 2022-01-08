# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:
    """
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
    with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Questions
          - How many items in nums?
          - Technical constraints?
          - Isn't this just a regular ascending sort?

        Examples
        [0 1 2 0 1 2] -> [0 0 1 1 2 2]
        [0 0 2 1 1 2]

        Solution
          - We can use O(3) space and sort this in O(n) time by keeping track of number of each color
        """
        reds = 0
        whites = 0
        blues = 0

        for num in nums:
            if num == 0:
                reds += 1
            elif num == 1:
                whites += 1
            else:
                blues += 1

        for i in range(len(nums)):
          if i < reds:
            nums[i] = 0
          elif reds <= i and i < reds + whites:
            nums[i] = 1
          elif i >= reds + whites:
            nums[i] = 2

    def second(self, nums: List[int]) -> None:
        """
        [0 1 2 0 1 2]

        When cur < cur - 1, bubble up.
        """

        # Test 1: [0 1 2 0 1 2]
        # cur = 3, [0 1 0 2 1 2],
        # cur = 2, [0 0 1 2 1 2], cur = 3
        # cur=4, [0 0 1 1 2 2]

        if not nums:
            return []
        cur = 1
        while cur < len(nums):
            while cur - 1 >= 0 and nums[cur] < nums[cur - 1]:
                temp = nums[cur - 1]
                nums[cur - 1] = nums[cur]
                nums[cur] = temp
                cur -= 1
            cur += 1
        print(nums)

Solution().second([0,1,2,0,1,2])