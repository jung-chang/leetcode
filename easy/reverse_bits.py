# https://leetcode.com/problems/reverse-bits/


class Solution:
    """
    Reverse bits of a given 32 bits unsigned integer.
    """

    def first(self, n: int) -> int:
        """
        Using string hacks instead of bit calculations.
        """
        bin_string = f"{n:b}"
        reversed_string = bin_string[::-1]
        suffix = "0" * (32 - len(reversed_string))
        reversed_string += suffix
        return int(reversed_string, 2)

    def second(self, n: int) -> int:
        """
        Use bit shifting. String manipulation is actually faster.
        """
        reversed_bits = 0
        for _ in range(32):
            reversed_bits <<= 1
            reversed_bits += n & 1
            n >>= 1
        return reversed_bits


print(Solution().first(4294967293))
print(Solution().second(4294967293))
