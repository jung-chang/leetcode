# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        """
        1. Sort this and iterate O(n + n log n) with no space
        2. Use a set O(n) with O(n) space
        4. Negative markings. Flip nums[i] negative for integer i
        5. Turtle and hare shit, use num has the next index.
        """
        slow = nums[nums[0]]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # Slow and fast now at intersection point
        # Reset slow, move at same speed and slow/fast will meet at entrace of cycle -> duplicate.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast


print(Solution().findDuplicate([3, 1, 3, 4, 2]))
