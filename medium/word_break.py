# https://leetcode.com/problems/word-break/

from typing import List
from collections import defaultdict


class Solution:
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        abc, [a, b, c]
        a -> bc, [a b c]
        b -> c [a,b,c]

        gabc, [a b c w]
        g -> [abcw], bc [abcw]

        catsandog [cats dog sand and cat]
        cats + andog []
        and + og[] || an [] + dog

        Solution
            - Recursively try to form substrings with wordDict

        Time:
        """

        word_map = {}

        @cache
        def can_break(local_s) -> bool:
            nonlocal word_map

            if not local_s:
                return True

            for i in range(len(local_s)):
                for word in word_map[local_s[i]]:
                    if len(word) > len(local_s):
                        continue
                    if local_s == word:
                        return True
                    if local_s[: len(word)] == word and can_break(local_s[len(word) :]):
                        return True
            return False

        word_map = defaultdict(list)
        for word in wordDict:
            word_map[word[0]].append(word)
        return can_break(s)

    def second(self, s: str, wordDict: List[str]) -> bool:
        """
        With custom cache and wordidct set

        doesnt work.
        """
        words = set(wordDict)
        broken_words = set()

        def can_break(local_s) -> bool:
            nonlocal broken_words

            if not local_s:
                return True

            for i in range(1, len(local_s) + 1):
                subword = local_s[:i]
                if subword in broken_words:
                    return True
                if subword in words:
                    broken_words.add(subword)
                    if can_break(local_s[len(subword) :]):
                        return True
            return False

        return can_break(s)


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
w = [
    "a",
    "aa",
    "aaa",
    "aaaa",
    "aaaaa",
    "aaaaaa",
    "aaaaaaa",
    "aaaaaaaa",
    "aaaaaaaaa",
    "aaaaaaaaaa",
]


print(Solution().second(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
