# https://leetcode.com/problems/camelcase-matching/

from collections import defaultdict
from typing import List, Dict, Tuple


class Solution:
    """
    Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

    A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that it equals the query. You may insert each character at any position and you may not insert any characters.
    """

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def matches(query: str, pattern: str):
            i = 0
            for letter in query:
                if i < len(pattern) and letter == pattern[i]:
                    i += 1
                elif letter.isupper():
                    return False
            return i == len(pattern)

        result = []
        for query in queries:
            result.append(matches(query, pattern))
        return result


q = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
p = "FB"

q = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
p = "FoBa"

# q = ["CompetitiveProgramming", "CounterPick", "ControlPanel"]
# p = "CooP"

# q = ["aksvbj L iknu T zqon","ksvjLimflkpnTzqn","mmkasvjLiknTxzqn","ksvjLiurknTzzqbn","ksvsjLctikgnTzqn","knzsvzjLiknTszqn"]
# p = "ksvj L ikn T zqn"

print(Solution().camelMatch(q, p))
