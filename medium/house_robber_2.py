# https://leetcode.com/problems/house-robber-ii/

from typing import List


class Solution:
    """
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed.
    All houses at this place are arranged in a circle.
    That means the first house is the neighbor of the last one.

    Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    """

    def rob(self, nums: List[int]) -> int:
        """
        [1 2 3 4], rob 2,4
        [4 2 3 4], rob 3,4  -> 423 or 234

        dp=[4 2 ]

        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def get_max(nums: List[int]) -> int:
            if len(nums) <= 2:
                return max(nums)
            dp = nums[:2]
            values = []
            for i in range(2, len(nums)):
                values.extend([dp[i - 1], dp[i - 2] + nums[i]])
                if 0 <= i - 3:
                    values.append(dp[i - 3] + nums[i])
                dp.append(max(values))
            return dp[-1]

        # print(nums[1:], nums[: len(nums) - 1])
        one = get_max(nums[1:])
        two = get_max(nums[: len(nums) - 1])
        # print(one, two)
        return max(one, two)


print(Solution().rob([1, 3, 1, 3, 100]))
