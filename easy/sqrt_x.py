# https://leetcode.com/problems/sqrtx/


class Solution:
    """
    Given a non-negative integer x, compute and return the square root of x.
    """

    def first(self, x: int) -> int:
        """
        Binary search for the number.
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        bottom = x // 2
        top = x // 2
        found = False
        while not found:
            square = bottom * bottom
            if square == x:
                found = True
            elif square > x:
                top = bottom
                bottom //= 2
            else:
                increment = (top - bottom) // 2
                if increment <= 0:
                    found = True
                else:
                    bottom += increment
        return bottom


print(Solution().first(29))
