# https://leetcode.com/problems/combinations/
from typing import List


class Solution:
    """
    Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
    """

    def recur(self, n: int, k: int) -> List[List[int]]:
        def helper(start: int, k: int):
            if k == 0:
                return [[]]
            combinations = []
            for i in range(start, n + 1):
                combs = helper(i + 1, k - 1)
                for comb in combs:
                    combinations.append([i] + comb)
            return combinations

        return helper(1, k)

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        n = 4, k = 3
        [1 2 3 4]
        123, 124, 234
        """
        if k < 1:
            return []
        if n < 1:
            return []

        combinations = []
        stack = [[i] for i in range(1, n + 1)]
        while stack:
            comb = stack.pop()
            if len(comb) == k:
                combinations.append(comb)
                continue
            for j in range(comb[-1] + 1, n + 1):
                stack.append(comb + [j])
        return combinations


print(Solution().combine(4, 3))
print(Solution().recur(3, 2))
