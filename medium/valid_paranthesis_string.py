# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    """
    Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
    """

    def second(self, s: str) -> bool:
        """
        Count the 'balance' of open brackets

        Encoutering (, you need at least 1 )
        Encountering (*( you need at 1, 2 or 3 )
        """
        bmin = bmax = 0
        for symbol in s:
            if symbol == "(":
                bmin += 1
                bmax += 1
            elif symbol == ")":
                bmin = max(bmin - 1, 0)
                bmax -= 1
            elif symbol == "*":
                bmin = max(bmin - 1, 0)
                bmax += 1
            if bmax < 0:
                return False
        return bmin == 0

    def checkValidString(self, s: str) -> bool:
        """
        Sub each * with all combinations

        Cases
            - () valid
            - (*) star=empty
            - (*(*)) -> ((())) or ()(())
            - (*())) star=(
            - ((()*) star=)

        Not valid
        ())
        * = (, ) or empty

        left=(
        right=)
        """
        if not s:
            return True

        lefts = s.count("(")
        rights = s.count(")")

        stack = [s[0]]
        i = 1
        while stack and i < len(s):
            symbol = s[i]
            if symbol == "(":
                stack.append(symbol)
            elif symbol == ")":
                if stack[-1] == "(":
                    stack.pop()
                elif stack[-1] == "*" and rights > lefts:
                    stack.pop()
                else:
                    stack.append(")")
            elif symbol == "*":
                if lefts == rights:
                    pass
                if stack[-1] == "(" and lefts > rights:
                    stack.pop()
            i += 1
        return len(stack) == 0


# print(Solution().checkValidString("()"))
print(Solution().checkValidString("(*)"))
print(Solution().checkValidString("(*()))"))
print(Solution().checkValidString("((()*)"))
print(Solution().checkValidString("(*(*))"))
