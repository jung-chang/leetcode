# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        forward = [nums[0]]
        for i in range(1, len(nums)):
            forward.append(nums[i] * forward[i - 1])

        backward = [nums[-1]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            backward[i] = nums[i] * backward[i + 1]

        result = []
        for i in range(len(nums)):
            product = 1
            if 0 <= i - 1 < len(forward):
                product *= forward[i - 1]
            if 0 <= i + 1 < len(backward):
                product *= backward[i + 1]
            result.append(product)
        return result

        # [1 2 3 4]
        # f = [ 2 6 24]
        # b = [24 24 12 4]


print(Solution().productExceptSelf([1, 2, 3, 4]))
