# https://leetcode.com/problems/combination-sum-iv/

from typing import List


class Solution:
    """
    Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
    """

    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        dp[i] = # unique combinations to sum to i
        dp[i] = dp[i]

        dp[0] = 0
        dp[1] = (1) = 1
        dp[2] = (1,1) (2) = 2
        dp[3] = (1,1,1) (2,1) (1,2), (3) = 4
        dp[4] = (1,1,1,1) (1,1,2) (1,2,1) (2,1,1) (2,2) (1,3) (3,1) = 7

        dp[4] = dp[1] + dp[2] + dp[3]
        """
        nums.sort()

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            # i=4, nums=[1 2 3]
            for num in nums:
                if num > i:
                    break
                if num == i:
                    dp[i] += 1
                if num < i:
                    # dp[i-num] = all combinations that are missing num to become target
                    dp[i] += dp[i - num]
        print(dp)
        return dp[target]

    def recursive(self, nums: List[int], target: int) -> int:
        """
        Can re use integers.

        [1 2 3 4 5], t=4
        (1,1,1,1)
        (1,1,2)
        (2,2)
        (1,3)
        (4)

        comb(4) = comb(3) + comb(1) or comb(2) + comb(2)

        dp[i] = combinations to sum to i
        """
        nums.sort()
        nums_set = set(nums)
        combinations = []
        memo = [0] * (target + 1)
        memo[1] = 1

        def helper(nums: List[int], target: int, combination: List[int]):
            nonlocal nums_set
            nonlocal combinations

            if target == 0:
                combinations.append(combination)

            for num in nums:
                if num > target:
                    continue
                diff = target - num

                if num in nums_set:
                    helper(nums, diff, combination + [num])

        for i in range(2, target + 1):
            helper(nums, i, [])
            memo[i] = len(combinations)
            combinations = []
        return memo[target]


print(Solution().combinationSum4([1, 2, 3, 4], 10))
# print(Solution().combinationSum4([1, 2], 89))
