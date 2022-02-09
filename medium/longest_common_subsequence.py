# https://leetcode.com/problems/longest-common-subsequence/

from typing import Tuple


class Solution:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

        For example, "ace" is a subsequence of "abcde".

    """

    def recursive(self, text1: str, text2: str) -> int:
        """Compare every sub string of text1 and text2"""

        def helper(t1, t2, i1, i2):
            if i1 >= len(t1) or i2 >= len(t2):
                return 0
            if t1[i1] == t2[i2]:
                return 1 + helper(t1, t2, i1 + 1, i2 + 1)
            else:
                return max(helper(t1, t2, i1 + 1, i2), helper(t1, t2, i1, i2 + 1))

        if not text1 or not text2:
            return 0
        if text1 == text2:
            return len(text1)
        return helper(text1, text2, 0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp[i][j] = longest common subsequence of text1[0..i] and text2[0..j]

        'ace' in 'abcde'
        dp[0][0] = 1, dp[0][1] = 1

        a, a
        a, ab
        a, abc
        a, abcde

        ac, a
        ac, ab
        ac, abc
        ac, abcd
        ac, abcde

        ace, a
        ace, ab
        ace, abc
        ace, abcd
        ace, abcde

        dp[i][j] = max()
        """
        if not text1 or not text2:
            return 0
        if text1 == text2:
            return len(text1)

        dp = [[0] * (len(text2) + 1)] * (len(text1) + 1)
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        #         print(text1[: i + 1], text2[: j + 1], dp[i][j])
        # print(dp)
        return dp[-1][-1]

    def first(self, text1: str, text2: str) -> int:
        """
        'ace' in 'ace'
        'fetabc' in 'abcfetca'
        """
        if not text1 or not text2:
            return 0

        if len(text1) <= len(text2):
            smaller = text1
            larger = text2
        else:
            smaller = text2
            larger = text1

        smaller = "".join([letter for letter in smaller if letter in set(larger)])
        if not smaller:
            return 0

        print(smaller, larger)

        # Stores (length of seq, index in larger string)
        # [(0,6), (1,4), (2,5), (1,0), (2,1),(3,2)]

        def get_index(start: int, letter: str, string: str) -> int:
            i = start + 1
            while i < len(string):
                if letter == string[i]:
                    return i
                i += 1
            return i

        dp = []
        for i in range(len(smaller)):
            if not dp:
                length = 0
                index = get_index(0, smaller[i], larger)
            else:
                length, start = dp[i - 1]
                if length:
                    index = get_index(start, smaller[i], larger)
                else:
                    index = get_index(0, smaller[i], larger)

            if index < len(larger):
                dp.append((length + 1, index))
            else:
                index_at_start = get_index(0, smaller[i], larger)
                if index_at_start < len(larger):
                    dp.append((1, index_at_start))
                else:
                    dp.append((0, index_at_start))
        return max([length for length, _ in dp])


# print(Solution().longestCommonSubsequence("fdetabc", "abcfetc"))
print(Solution().longestCommonSubsequence("ace", "abcde"))
# print(Solution().longestCommonSubsequence("abc", "def"))

# t1 = "hofubmnylkra"
# t2 = "pqhgxgdofcvmr"

# t1 = "bsbininm"
# t2 = "jmjkbkjkv"

t1 = "ezupkr"
t2 = "ubmrapg"
print(Solution().longestCommonSubsequence(t1, t2))
