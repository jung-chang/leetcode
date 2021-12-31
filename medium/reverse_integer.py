# https://leetcode.com/problems/reverse-integer/


class Solution:
    """
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    """

    def reverse(self, x: int) -> int:
        """
        Divide and mod for digits

        321 // 10 = 32
        321 % 10 = 1
        """
        negative = False
        if x < 0:
            negative = True
            x = x * -1

        total = 0
        max_neg = -(2 ** 31)
        max_pos = 2 ** 31 - 1
        while x:
            mod = x % 10
            if negative and -1 * total < (max_neg - mod) / 10:
                return 0
            if not negative and total > (max_pos - mod) / 10:
                return 0
            total *= 10
            total += mod
            x //= 10
        return -1 * total if negative else total


print(Solution().reverse(123))
print(Solution().reverse(-321))
print(Solution().reverse(-12000))
print(Solution().reverse(2147483648))
print(Solution().reverse(1000000003))
print(Solution().reverse(-1000000003))
