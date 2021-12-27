from typing import List


class Solution:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.
    """

    def first(self, nums: List[int]) -> int:
        """
        Use a set.
        """
        track = set()
        for num in nums:
            if num in track:
                track.remove(num)
            else:
                track.add(num)
        return track.pop()
