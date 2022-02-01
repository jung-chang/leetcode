# https://leetcode.com/problems/sum-of-two-integers/
class Solution:
    """
    Given two integers a and b, return the sum of the two integers without using the operators + and -.
    """

    def getSum(self, a: int, b: int) -> int:
        """
        1. Bit manipulation and carry over. 2 + 4 = 0010 + 0100 = 0110

        If negative, add 2's complement.
        """

        def add_binary_strings(bin_a: str, bin_b: str) -> int:
            carry = False
            result = ""
            for i in range(1, len(bin_a) + 1):
                digit_a = bin_a[-i]
                digit_b = bin_b[-i]

                current = ""
                if digit_a == "1" and digit_b == "1":
                    if carry:
                        current = "1"
                    else:
                        current = "0"
                    carry = True
                elif digit_a == "0" and digit_b == "0":
                    if carry:
                        current = "1"
                    else:
                        current = "0"
                    carry = False
                else:
                    if carry:
                        current = "0"
                        carry = True
                    else:
                        current = "1"
                        carry = False
                result = f"{current}{result}"
            if carry:
                result = f"1{result}"
            return int(result, 2)

        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]
        if len(bin_a) > len(bin_b):
            bin_b = f"{'0'*(len(bin_a) - len(bin_b))}{bin_b}"
        elif len(bin_a) < len(bin_b):
            bin_a = f"{'0'*(len(bin_b) - len(bin_a))}{bin_a}"

        if a >= 0 and b >= 0:
            return add_binary_strings(bin_a, bin_b)
        elif a < 0 and b < 0:
            return -1 * add_binary_strings(bin_a[1:], bin_b[1:])
        else:
            if a < 0:
                a = ~a + 1
                bin_a = bin(a)[3:]
            else:
                b = ~b + 1
                bin_b = bin(b)[3:]
            return ~add_binary_strings(bin_a, bin_b) + 1


print(Solution().getSum(-4, 2))
