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

        negative = True if numerator * denominator < 0 else False
        numerator = abs(numerator)
        denominator = abs(denominator)
        remainder = numerator % denominator
        whole = int(numerator / denominator)

        print(whole, remainder)

        decimal = ""
        repeating_index = None
        visited = []
        while remainder:
            remainder *= 10
            if remainder in visited:
                repeating_index = visited.index(remainder)
                break
            else:
                visited.append(remainder)
            division = int(remainder / denominator)
            decimal += str(division)
            remainder -= division * denominator

        if repeating_index is not None:
            print("repeating_index", repeating_index)
            non_repating_part = decimal[:repeating_index]
            repating_part = decimal[repeating_index:]
            return (
                f"{'-' if negative else ''}{whole}.{non_repating_part}({repating_part})"
            )
        return f"{'-' if negative else ''}{whole}.{decimal}"


print(Solution().fractionToDecimal(-50, 8))
# print(Solution().fractionToDecimal(1, 3))
# print(Solution().fractionToDecimal(2, 1))
# print(Solution().fractionToDecimal(1, 6))
