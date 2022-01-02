# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    """

    def generateParenthesis(self, n: int) -> List[str]:
        """
        How to generate valid parantheses?
        - ((())) and ()()() are easy
        - (())() = ()(())
        - (()()())

        Build up results for each n starting at 1.

        n=1, ()
        n=2, (()), ()()
        n=3, ((())), (()()), (())(), ()(()), ()()()

        Time: O(n) * O()
        """

        if not n:
            return []
        results = set(["()"])
        if n == 1:
            return results
        for _ in range(1, n):
            new_results = set()
            for result in results:
                new_results.add(result + "()")
                for i in range(len(result)):
                    if result[i] == "(":
                        new_result = result[: i + 1] + "()" + result[i + 1 :]
                        new_results.add(new_result)
            results = new_results
        return results

    def second(self, n):
        results = []

        def backtrack(result, left, right):
            if left == n and right == n:
                results.append(result)
            if left < n:
                backtrack(result + "(", left + 1, right)
            if right < left:
                backtrack(result + ")", left, right + 1)

        backtrack("", 0, 0)
        return results


print(Solution().second(4))
