# https://leetcode.com/problems/repeated-string-match/


from collections import defaultdict


class Solution:
    """
    Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it.
    If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

    Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".
    """

    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        Fulfill letter frequency and ordering
        """
        if not b:
            return 0
        if a == b:
            return 1
        if b in a:
            return 1

        temp = ""
        count = 0
        while len(temp) < len(b):
            temp += a
            count += 1
            if b in temp:
                return count
        temp += a
        if b in temp:
            return count + 1
        return -1


a = "abcd"
b = "cdabcdab"

a = "aaaaaaaaaaaaaaaaaaaaaab"
b = "ba"

print(Solution().repeatedStringMatch(a, b))
