# https://leetcode.com/problems/basic-calculator-ii/


class Solution:
    """
    Given a string s which represents an expression, evaluate this expression and return its value.

    The integer division should truncate toward zero.

    You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
    """

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        equation = []

        num = ""
        for char in s:
            if "0" <= char <= "9":
                num += char
            else:
                equation.append(int(num))
                equation.append(char)
                num = ""
        equation.append(int(num))

        stack = [equation[0]]
        i = 1
        while stack and i < len(equation):
            print(stack, equation[i])
            if equation[i] == "/":
                stack.append(stack.pop() // equation[i + 1])
                i += 1
            elif equation[i] == "*":
                stack.append(stack.pop() * equation[i + 1])
                i += 1
            else:
                stack.append(equation[i])
            i += 1
        print(stack)

        if len(stack) == 1:
            return stack[0]
        equation = stack
        stack = [equation[0]]
        i = 1
        while stack and i < len(equation):
            print(stack, equation[i])
            if equation[i] == "+":
                stack.append(stack.pop() + equation[i + 1])
                i += 1
            elif equation[i] == "-":
                stack.append(stack.pop() - equation[i + 1])
                i += 1
            else:
                stack.append(equation[i])
            i += 1
        return stack[0]


print(Solution().calculate("3+2*2"))
