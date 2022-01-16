# https://leetcode.com/problems/factorial-trailing-zeroes/


class Solution:
    """
    Given an integer n, return the number of trailing zeroes in n!.

    Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
    """

    def trailingZeroes(self, n: int) -> int:
        """
        1! = 1
        2! = 2
        3! = 3 * 2! = 6
        4! = 4 * 2! = 24
        5! = 5 * 4! = 120
        6! = 6 * 5! = 720
        7! = 5040
        8! = 40320

        Can compute the factorial and count number of trailing 0s.
            - This would likely overflow or take too long to compute

        Trailing 0s are only there if there are factors of 10
            - We count the number 2 and 5 prime factors
            - We can eliminate counting factors of 2 since every even number has a factor of 2
            - Thus we just count the 5 factors
        """

        def is_factor(num: int, factor: int) -> bool:
            return num / factor == int(num / factor)

        if n < 5:
            return 0
        two_factors = 0
        five_factors = 0

        while n >= 1:
            number = n
            while is_factor(number, 5):
                five_factors += 1
                number /= 5
            while is_factor(number, 2):
                two_factors += 1
                number /= 2
            n -= 1
        return min(two_factors, five_factors)


print(Solution().trailingZeroes(10))
