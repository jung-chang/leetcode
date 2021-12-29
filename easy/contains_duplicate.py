# https://leetcode.com/problems/contains-duplicate/


from typing import List


class Solution:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    """

    def first(self, nums: List[int]) -> bool:
        "Hash map counter"
        counter = {}
        for num in nums:
            if counter.get(num) is None:
                counter[num] = 1
            else:
                counter[num] += 1
                if counter[num] > 1:
                    return True
        return False

    def second(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
