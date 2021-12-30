# https://leetcode.com/problems/fizz-buzz/

from typing import List


class Solution:
    """
    Given an integer n, return a string array answer (1-indexed) where:

        answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        answer[i] == "Fizz" if i is divisible by 3.
        answer[i] == "Buzz" if i is divisible by 5.
        answer[i] == i (as a string) if none of the above conditions are true.

    """

    def fizzBuzz(self, n: int) -> List[str]:
        """r u srs"""
        answer = []
        for i in range(1, n + 1):
            mod3 = i % 3
            mod5 = i % 5
            if mod3 == 0 and mod5 == 0:
                answer.append("FizzBuzz")
            elif mod3 == 0:
                answer.append("Fizz")
            elif mod5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer


print(Solution().fizzBuzz(3))
