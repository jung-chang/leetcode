# https://leetcode.com/problems/fraction-to-recurring-decimal/


class Solution:
    """
    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

    If the fractional part is repeating, enclose the repeating part in parentheses.

    If multiple answers are possible, return any of them.

    It is guaranteed that the length of the answer string is less than 104 for all the given inputs
    """

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return f"{int(numerator / denominator)}"

        remainder = numerator % denominator
        whole = numerator // denominator

        # 1/3 = 0.333333333
        # 10/3 -> 3 10//3 = 3
        while remainder:
            num = remainder * 10

        decimal = ""
        return f"{whole}.{decimal}"