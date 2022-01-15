# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    """
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

    Note that division between two integers should truncate toward zero.

    It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
    """

    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            if token == "+":
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif token == "-":
                first = num_stack.pop()
                second = num_stack.pop()
                num_stack.append(second - first)
            elif token == "*":
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif token == "/":
                first = num_stack.pop()
                second = num_stack.pop()
                num_stack.append(int(second / first))
            else:
                num_stack.append(int(token))
        return num_stack[-1]


print(
    Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
