# https://leetcode.com/problems/palindrome-number/


class Solution:
    """
    Given an integer x, return true if x is palindrome integer.
    """

    def first(self, x: int) -> bool:
        """
        Convert to string, use 2 pointers front and back and compare.

        Time: O(n) from str() and O(n/2) for iteration
        Space: O(2) for pointers

        Notes:
            - Negatives are not palindromes
        """
        number = str(x)
        start = 0
        end = len(number) - 1

        while start < end:
            if number[start] != number[end]:
                return False
            start += 1
            end -= 1
        return True

    def second(self, x: int) -> bool:
        """
        Revert the number and check for overflow.

        Time: O(n/2) iterating half of the numbers
        Space: O(1) from keeping numbers
        """
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False

        reversed_x = 0
        while reversed_x < x:
            modulo = x % 10
            x = x // 10
            reversed_x *= 10
            reversed_x += modulo
        return reversed_x == x or reversed_x // 10 == x


print(Solution().second(1235321))
print(Solution().second(100))
