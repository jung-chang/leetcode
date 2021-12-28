# https://leetcode.com/problems/majority-element/


from typing import List


class Solution:
    """
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    """

    def first(self, nums: List[int]) -> int:
        if not nums:
            return None
        counter = {}
        majority = (len(nums) // 2) + 1
        for num in nums:
            if counter.get(num) is None:
                counter[num] = 1
            else:
                counter[num] += 1
            if counter[num] >= majority:
                return num
        return None
