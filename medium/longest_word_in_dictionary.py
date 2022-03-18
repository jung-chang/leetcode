# https://leetcode.com/problems/longest-word-in-dictionary/

from collections import defaultdict
from typing import List


class Solution:
    """
    Given an array of strings words representing an English Dictionary,
    return the longest word in words that can be built one character at a time by other words in words.

    If there is more than one possible answer, return the longest word with the smallest lexicographical order.
    If there is no answer, return the empty string.
    """

    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        length_to_word = defaultdict(list)
        min_length = 0
        for word in word_set:
            print(word, min_length, length_to_word)
            if len(word) < min_length:
                continue
            add = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    add = False
                    break
            if add:
                length_to_word[len(word)].append(word)
                min_length = max(min_length, len(word))
        # print(min_length, length_to_word)
        if not length_to_word:
            return ""
        return sorted(length_to_word[min_length])[0]


words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
words = ["wo", "wor", "worl", "world"]

print(Solution().longestWord(words))
