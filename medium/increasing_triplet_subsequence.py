# https://leetcode.com/problems/increasing-triplet-subsequence/

from collections import defaultdict
from socket import NI_NUMERICHOST
from typing import List


class Solution:
    """
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
    """

    def first(self, nums: List[int]) -> bool:
        """
        Let dp[num] = # of increasing indices
        if dp[num] == 3 -> return true
        else dp[num] = 1 + dp[0 to num-1] if > num

        Example
            [2 1 5 0 4 6] -> 246, 156, 046
            [1 1 2 1 2 3] -> dp matchin indices with nums

            [2 1 5 0 4 6]
            [0 1 1 1]
        """

        if len(nums) < 3:
            return False

        count = 0

        dp = [1]
        for i in range(1, len(nums)):
            max_increasing = 1
            for j in range(len(dp) - 1, -1, -1):
                count += 1
                if nums[i] <= nums[j]:
                    continue
                if dp[j] == 2:
                    return True
                max_increasing = max(max_increasing, dp[j] + 1)
                if max_increasing == 1:
                    break
            dp.append(max_increasing)
        print(len(nums), count)
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first = float("inf")
        second = float("inf")

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


n = [2, 1, 5, 0, 4, 6]
n = [5, 4, 3, 2, 1]
n = [20, 100, 10, 12, 5, 13]
# n = [1, 2] * 100


print(Solution().increasingTriplet(n))
