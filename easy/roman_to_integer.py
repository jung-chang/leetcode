# https://leetcode.com/problems/roman-to-integer/


class Solution:
    """
    Given a roman numeral, convert it to an integer.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    """

    def first(self, s: str) -> int:
        """
        Have a buffer keeping the previous value, read current value and decide on conversion.
        """
        symbol_to_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        prev_symbol = ""
        for symbol in s:
            if not prev_symbol:
                prev_symbol = symbol
            else:
                if prev_symbol == "I":
                    if symbol == "V" or symbol == "X":
                        total += (
                            symbol_to_values[symbol] - symbol_to_values[prev_symbol]
                        )
                        prev_symbol = ""
                elif prev_symbol == "X":
                    if symbol == "L" or symbol == "C":
                        total += (
                            symbol_to_values[symbol] - symbol_to_values[prev_symbol]
                        )
                        prev_symbol = ""
                elif prev_symbol == "C":
                    if symbol == "D" or symbol == "M":
                        total += (
                            symbol_to_values[symbol] - symbol_to_values[prev_symbol]
                        )
                        prev_symbol = ""
                if prev_symbol:
                    total += symbol_to_values[prev_symbol]
                    prev_symbol = symbol
        if prev_symbol:
            total += symbol_to_values[prev_symbol]
        return total


print(Solution().first("III"))
print(Solution().first("MCMXCIV"))
print(Solution().first("LVIII"))
