# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    """
    The algorithm for myAtoi(string s) is as follows:

        1. Read in and ignore any leading whitespace.

        2. Check if the next character (if not already at the end of the string) is '-' or '+'.
        Read this character in if it is either. This determines if the final result is negative or positive respectively.
        Assume the result is positive if neither is present.

        3. Read in next the characters until the next non-digit character or the end of the input is reached.
        The rest of the string is ignored.

        4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
        If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

        5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the
        integer so that it remains in the range. Specifically, integers less than -231 should be
        clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.

        6. Return the integer as the final result.
    """

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        i = 0
        negative = False
        if s[i] == "-":
            negative = True
            i += 1
        elif s[i] == "+":
            i += 1
        s = s[i:]

        if not s:
            return 0

        # Trim all prefix 0s
        i = 0
        while i + 1 < len(s) and s[i] == "0":
            i += 1
        s = s[i:]

        max_neg = -(2 ** 31)
        max_pos = (2 ** 31) - 1
        num = 0
        num_range = range(ord("0"), ord("9") + 1)
        for digit in s:
            if ord(digit) not in num_range:
                break
            value = ord(digit) - ord("0")
            if negative and -1 * num < (max_neg + value) / 10:
                return max_neg
            if not negative and num > (max_pos - value) / 10:
                return max_pos
            num *= 10
            num += value
        return -1 * num if negative else num


print(Solution().myAtoi("00000-42a1234"))
