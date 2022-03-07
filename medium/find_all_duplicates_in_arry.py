# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List


class Solution:
    """
    Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice,
    return an array of all the integers that appears twice.

    You must write an algorithm that runs in O(n) time and uses only constant extra space.
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Solutions
            - Sort and iterate = O(n log n) time, O(1) space
            - Iterate and use set = O(n) time, O(n) space

        Zone in on 'once or twice'

        [1 2 1]
        - bit manipulation? possibly
        - hash function? same as using n space
        - sliding window? Cant do, window ill have to be n size
        - Is there someway to encode 1 <= n <= 10^5 numbers in constant space?
        - Use array space
        """

        result = []
        if not nums:
            return result

        nums = [0] + nums
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num] <= 0:
                result.append(num)
            else:
                nums[num] *= -1
        if not result:
            return []
        return result[1:]


print(Solution().findDuplicates([1, 1, 2]))
