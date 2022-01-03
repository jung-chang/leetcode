# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List, Tuple


class Solution:
    """
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Questions
            - Ascending of integers
            - Target value = integer
            - Implies repeating integers in the list
            - How long is the list? How big/small are the numbers?

        Example
            - [1 1 2 3 4 5 5], t=5, out=[5,6]
            - t=1, out=[0, 1]

        Solution
            - Iterate through list, if target, start counting and end. O(n)
            - Can we use sorted to our advantage.
            - Binary search, search for the target start and end

        Tests
            - [1 2 3 4 4 5 5], t=5
            - mid=3, nums[3]=4 -> [1 2 3] [4 5 5]
            - mid=1, nums[1]=5 -> [4] 5 [5] -> iterate left and right
            4 cases, out = [mid, mid], [<mid, mid], [mid, >mid], [<mid, >mid]
        """
        # Test 1: [1,2,2,3,4,4,4], t=4, l=7
        # mid=3, [1 2 2] 3 [4 4 4], result
        # offset=4, mid=1, [4] 4 [4], result=[5,5]
        #   left: offset=4, mid=0, [4] result[4,5]
        #   right: offset6, mid=0 [4] result [4,6]

        result = [len(nums) - 1, 0]

        def helper(nums: List[int], target: int, offset=0) -> List[int]:
            if not nums:
                return
            mid = len(nums) // 2
            if nums[mid] == target:
                result[0] = min(result[0], offset + mid)
                result[1] = max(result[1], offset + mid)
                helper(nums[:mid], target, offset=offset)
                helper(nums[mid + 1 :], target, offset=offset + mid + 1)
            elif target < nums[mid]:
                helper(nums[:mid], target, offset=offset)
            else:
                helper(nums[mid + 1 :], target, offset=offset + mid + 1)

        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        helper(nums, target)
        if result[1] < result[0]:
            return [-1, -1]
        return result


print(Solution().searchRange([1, 2, 2, 3, 4, 4, 4], 4))
