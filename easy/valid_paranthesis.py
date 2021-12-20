# https://leetcode.com/problems/valid-parentheses/


class Solution:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
    """

    def first(self, s: str) -> bool:
        stack = []
        bracket_map = {"]": "[", "}": "{", ")": "("}
        if not s:
            return False
        stack.append(s[0])
        for bracket in s[1:]:
            if stack and bracket_map.get(bracket) == stack[-1]:
                stack.pop()
            else:
                stack.append(bracket)
        return not stack


print(Solution().first("{([])}"))
print(Solution().first("{([{{}}}}])}"))
