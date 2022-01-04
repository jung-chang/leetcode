# https://leetcode.com/problems/count-and-say/


from typing import OrderedDict


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
            ordered_tuples = []
            count = 0
            cur = None
            for char in term:
                if cur is None or char == cur:
                    cur = char
                    count += 1
                else:
                    ordered_tuples.append((cur, count))
                    cur = char
                    count = 1
            ordered_tuples.append((cur, count))
            new_term = ""
            for char, count in ordered_tuples:
                new_term += str(count) + char
            term = new_term
        return term

    def second(self, n: int) -> str:
        """
        Removed ordered_tuples and just added inline
        """
        if not n:
            return ""
        term = "1"
        for _ in range(1, n):
            count = 0
            cur = None
            new_term = ""
            for char in term:
                if cur is None or char == cur:
                    cur = char
                    count += 1
                else:
                    new_term += str(count) + cur
                    cur = char
                    count = 1
            new_term += str(count) + cur
            term = new_term
        return term


# print(Solution().second(2))
# print(Solution().second(3))
print(Solution().second(6))
# print(Solution().second(5))
# print(Solution().second(6))
# print(Solution().second(7))
