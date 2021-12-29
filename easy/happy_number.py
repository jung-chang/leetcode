# https://leetcode.com/problems/happy-number/

from typing import List


class Solution:
    """
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.
    """

    def first(self, n: int) -> bool:
        def getSumofSquaredDigits2(num: int) -> List[int]:
            digits = []
            while num >= 10:
                digits.append(num % 10)
                num //= 10
            digits.append(num)
            return sum([num ** 2 for num in digits])

        def getSumofSquaredDigits(num: int) -> int:
            total = 0
            while num >= 10:
                total += (num % 10) ** 2
                num //= 10
            return total + num ** 2

        if n <= 0:
            return False
        visited = set()
        while n != 1:
            n = getSumofSquaredDigits(n)
            if n in visited:
                break
            visited.add(n)
        return n == 1


print(Solution().first(19))
