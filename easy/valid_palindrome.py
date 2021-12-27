# https://leetcode.com/problems/valid-palindrome/


class Solution:
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    """

    def first(self, s: str) -> bool:
        phrase = ""
        numeric_range = range(ord("0"), ord("9") + 1)
        alphabet_range = range(ord("a"), ord("z") + 1)
        for char in s.lower():
            value = ord(char)
            if value in numeric_range or value in alphabet_range:
                phrase += char
        return phrase == phrase[::-1]


print(Solution().first("9,8"))
