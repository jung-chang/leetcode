# https://leetcode.com/problems/count-and-say/


class Solution:
    """
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
        countAndSay(1) = "1"
        countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

    """

    def countAndSay(self, n: int) -> str:
        if not n:
            return ""
        term = "1"
        for _ in range(1, n):
            new_term = ""
            for char in term:
                pass
        return term
