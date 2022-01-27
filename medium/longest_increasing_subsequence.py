# https://leetcode.com/problems/longest-increasing-subsequence/

from collections import defaultdict
from typing import List


class Solution:
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        There are negative integers.
        """
        negatives = abs(min(nums))
        dp = [0] * (max(nums) + negatives + 1)
        for num in nums:
            index = negatives + num
            if dp[:index]:
                dp[index] = 1 + max(dp[:index])
            else:
                dp[index] = 1
        return max(dp)

    def bfs(self, nums: List[int]) -> int:
        nums_to_larger = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    nums_to_larger[i].append(j)

        max_length = 1
        queue = [[key] for key in nums_to_larger.keys()]
        while queue:
            seq = queue.pop(0)
            max_length = max(max_length, len(seq))
            for i in nums_to_larger[seq[-1]]:
                queue.append(seq + [i])
        return max_length


print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
