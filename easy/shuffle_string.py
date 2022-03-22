# https://leetcode.com/problems/shuffle-string/

from typing import List


class Solution:
    """
    You are given a string s and an integer array indices of the same length.
    The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

    Return the shuffled string.
    """

    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)
        for i, index in enumerate(indices):
            result[index] = s[i]
            print(result)
        return "".join(result)


s = "codeleet"
i = [4, 5, 6, 7, 0, 2, 1, 3]
print(Solution().restoreString(s, i))
