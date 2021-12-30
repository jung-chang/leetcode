# https://leetcode.com/problems/power-of-three/


class Solution:
    """
    Given an integer n, return true if it is a power of three. Otherwise, return false.

    An integer n is a power of three, if there exists an integer x such that n == 3x.
    """

    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            n = n / 3
            if n != int(n):
                return False
        return n == 1


print(Solution().isPowerOfThree(45))
print(Solution().isPowerOfThree(0))
print(Solution().isPowerOfThree(1))
