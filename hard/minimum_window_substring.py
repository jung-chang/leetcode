# https://leetcode.com/problems/minimum-window-substring/


class Solution:
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
    If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.
    """

    def minWindow(self, s: str, t: str) -> str:
        """
        Brute: Go to every substring and check if the substring contains all of t.
        """
