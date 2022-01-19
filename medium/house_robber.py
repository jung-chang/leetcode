# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    """
    Along the street, each house has money.

    Security system will alarm if two adjacent houses were broken into the same night.

    nums=amount of money in each house
    """

    def rob(self, nums: List[int]) -> int:
        """
        DP problem where we have to consider adjacent houses.
        Let dp[i] = the maximum money obtained by considering the robbing of all houses from 0 to i-1

        Cases
        [1 2 3] -> max(dp[i-1], nums[i] + dp[i-2]) = 4
        [1 2 3 4] max(dp[i-1], nums[i] + dp[i-2]) = max(4, 6) = 6

        [2,7,9,3,1], dp=[2 7]

        [2 7 9], dp[2 7 11]
        [2 7 9 3], dp[2 7 11 11]
        [2 7 9 3 1], dp[2 7 11 11 12]

        [2 1 1 2] dp[2 1 3 2]
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        i = 2
        while i < len(nums):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            if i >= 3:
                dp[i] = max(dp[i], nums[i] + dp[i - 3])
            i += 1
        return dp[-1]


print(Solution().rob([2, 1, 1, 0, 0, 0, 0, 2]))
