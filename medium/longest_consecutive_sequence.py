# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [4,2,3,1,200,201,899,900,901,902]
        Make index map, and check +- until doesn't exist.
        """

        if not nums:
            return 0

        nums_set = set(nums)
        visited = set()
        length = 0

        n = 0
        for n in range(len(nums)):
            if nums[n] in visited:
                continue

            visited.add(nums[n])
            local_length = 1

            left = nums[n] - 1
            while left in nums_set and left not in visited:
                local_length += 1
                visited.add(left)
                left -= 1

            right = nums[n] + 1
            while right in nums_set and right not in visited:
                local_length += 1
                visited.add(right)
                right += 1

            length = max(length, local_length)
        return length


print(
    Solution().longestConsecutive(
        [4, 2, 3, 1, 200, 201, 899, 900, 901, 902, 124, 237, 903, 904]
    )
)
