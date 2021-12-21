# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    """
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
    The digits are ordered from most significant to least significant in left-to-right order.
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
    """

    def first(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits
        carry = 1
        for i in range(1, len(digits) + 1):
            total = digits[-i] + carry
            if total >= 10:
                digits[-i] = total - 10
                carry = total // 10
            else:
                digits[-i] += carry
                carry = 0
        return digits if not carry else [carry] + digits


print(Solution().first([1, 2, 3]))
