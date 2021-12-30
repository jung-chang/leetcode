# https://leetcode.com/problems/valid-anagram/

from collections import defaultdict


class Solution:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    """

    def first(self, s: str, t: str) -> bool:
        """
        Sort strings and compare.

        Time: O(n log n) for sorting.
        Space: No space needed
        """
        return sorted(s) == sorted(t)

    def second(self, s: str, t: str) -> bool:
        """
        Hash map counter

        Time: O(s + t)
        Space :O(s + t)
        """
        sMap = defaultdict(lambda: 0)
        for letter in s:
            sMap[letter] += 1
        tMap = defaultdict(0)
        for letter in t:
            tMap[letter] += 1
        return sMap == tMap
