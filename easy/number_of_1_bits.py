# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    """
    Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
    """

    def first(self, n: int) -> int:
        """
        String manipulation
        """
        count = 0
        for bit in f"{n:b}":
            if bit == "1":
                count += 1
        return count

    def second(self, n: int) -> int:
        """
        Bitwise operator
        """
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
