# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


class Solution:
    """
    Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

    A palindrome string is a string that reads the same backward as forward.
    """

    def partition(self, s: str) -> List[List[str]]:
        """
        Every single letter is a palindrome substring. need to partition the string

        Case 1:
            aa -> [a a], [aa]
            aaa -> [a a a], [a, aa], [aa, a], [aaa]
            caaa -> [c a a a], [c a aa], [caa a], [caaa]
            acaaa -> [a c a a a], [a c a aa], [a caa a],


        """

        if not s:
            return []
        if len(s) == 1:
            return [[s[0]]]

        partitions = []
        for i in range(1, len(s)):
            string = s[:i]
            if string == string[::-1]:
                new_partitions = self.partition(s[i:])
                for part in new_partitions:
                    partitions += [[string] + part]

        if s == s[::-1]:
            partitions.append([s])
        return partitions


print(Solution().partition("baaab"))
