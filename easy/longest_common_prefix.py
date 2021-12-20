# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    """

    def first(self, strs: List[str]) -> str:
        """
        Sort strings by length and go through shorted string.

        Time: O(n log n) + O(n)
        Space: None?

        Notes:
            - Are there only lowercase letters?
            - How many strings are there?
            - What are the length of the words?
        """

        def shortest_prefix(a: str, b: str) -> str:
            prefix = ""
            for i in range(len(min(a, b))):
                if a[i] != b[i]:
                    break
                prefix += a[i]
            return prefix

        if not strs:
            return ""
        strs.sort(reverse=True, key=len)
        prefix = strs[0]
        for string in strs[1:]:
            prefix = shortest_prefix(prefix, string)
            if not prefix:
                return prefix
        return prefix


print(Solution().first(["aaaa", "aaas", "aa", "asd"]))
