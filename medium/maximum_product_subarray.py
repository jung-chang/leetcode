# https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class Solution:
    """
    Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.

    A subarray is a contiguous subsequence of the array.
    """

    def maxProduct(self, nums: List[int]) -> int:
        """
        Brute force generating all contiguous subarrays from 1 to n.

        DP approach where dp[i] is the max product up to i

        dp[i] = nums[i] * dp[i-1] if nums[i]

        [1,2,3,0,10]
        dp=[1,2,6,0,]
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        maxes = [nums[0]]  # maxes[i] is max number from 0 to i
        mins = [nums[0]]  # mins[i] is min number from 0 to i
        for i in range(1, len(nums)):
            max_num = nums[i] * maxes[i - 1]
            min_num = nums[i] * mins[i - 1]
            maxes.append(max(nums[i], max_num, min_num))
            mins.append(min(nums[i], max_num, min_num))
        return max(mins + maxes)


# print(Solution().maxProduct([-2, 3, -4]))
print(Solution().maxProduct([1, -5, -2, -4, 3]))
# maxes=[1 1 10 8 24
# mins=[1 -5 -2 -4 -4