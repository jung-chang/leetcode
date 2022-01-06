# https://leetcode.com/problems/powx-n/

import math


class Solution:
    """
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
    """

    def myPow(self, x: float, n: int) -> float:
        """
        Questions
            - How small/big can x or n be?
            - Are x and n integers?
            - What type of number do we want to return?
            - Are there any technical constraints?

        Examples
            - x=2 n=2 -> 2^2 = 4
            - z=2.5 n=2 -> (2 + 0.5)^2 -> 2^2 + 0.5^2
            - n can be +/-, x can +/- and decimals

        Case 1: 2^2, -2 ^ 2 = 2^2 * -1
        Case 2: 2^-2 = 1/2 ^ 2
        Case 3: 2.1^2 = 2^2 + 1/10 ^2
        Case 4: 2.1^-2 = 1 / (2.1 ^ 2)

        Case 1: x=2, -2, 2.1 , n=+
        Case 2: x=2, -2, 2.1 , n=-
        Case 3: x=float, n=+
        Case 4: x=float, n=-
        """

        def power(x: float, exp: int) -> float:
            # 2 10, 2 5, 2 2, 21
            if exp == 0:
                return 1
            if exp == 1:
                return x
            half = power(x, exp // 2)
            result = half * half
            if exp % 2 == 1:
                result *= x
            return result

        if n > 0:
            return power(x, n)
        return 1 / power(x, abs(n))


print(Solution().myPow(2, 2))
print(Solution().myPow(-2, 2))
print(Solution().myPow(-2, 3))
print(Solution().myPow(2.1, 2))
print(Solution().myPow(2.1, -2))
print(Solution().myPow(2, 5))
