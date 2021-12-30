# https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    """
    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # w o r d
        start = 0
        end = len(s) - 1
        while start < end:
            print(s[start], s[end])
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1


Solution().reverseString(["h", "e", "l", "l", "o"])
