# https://leetcode.com/problems/excel-sheet-column-number/


class Solution:
    """
    Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
    """

    def first(self, columnTitle: str) -> int:
        """
                A = 1
                Z = 26
                AA = 27
                ABBA


                1 0
                AA
                26 1
        702
                A A A


        """
        count = 0
        ordA = ord("A")
        for i, letter in enumerate(reversed(columnTitle)):
            factor = 26 ** i
            value = ord(letter) - ordA + 1
            if factor == 0:
                factor = 1
            count += value * factor
            print(count)
        return count


# print(Solution().first("A"))
# print(Solution().first("B"))
# print(Solution().first("Z"))
print(Solution().first("ZY"))
print(Solution().first("FXSHRXW"))
