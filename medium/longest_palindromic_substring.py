# https://leetcode.com/problems/longest-palindromic-substring/

from collections import defaultdict


class Solution:
    """
    Given a string s, return the longest palindromic substring in s.
    """

    def first(self, s: str) -> str:
        """
        Can brute force this by going through very substring.
        """
        palindrome = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1] and len(substring) > len(palindrome):
                    palindrome = substring
        return palindrome

    def consecutive(self, i: int, s: str) -> str:
        """
        2. Repeated letters: a, aa, aaa
        3. Hybrids: baaab, baab
        """
        left = i
        right = i
        while left - 1 >= 0 and s[left - 1] == s[i]:
            left -= 1
        while right + 1 < len(s) and s[right + 1] == s[i]:
            right += 1

        while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
        return s[left : right + 1]

    def second(self, s: str) -> str:
        """
        Palindrome cases:

        1. Center letters: eca b ace
        2. Repeated letters: a, aa, aaa
        3. Hybrids: baaab, baab

        Iterate string, at each index check for each type of palindrome
        """

        if len(s) < 2:
            return s
        palindrome = ""
        for i in range(len(s)):
            sub = self.consecutive(i, s)
            if len(sub) > len(palindrome):
                palindrome = sub
        return palindrome


print(Solution().second(""))
print(Solution().second("ecabace"))
print(Solution().second("a"))
print(Solution().second("aa"))
print(Solution().second("aaa"))
print(Solution().second("aaab"))
print(Solution().second("baaab"))
