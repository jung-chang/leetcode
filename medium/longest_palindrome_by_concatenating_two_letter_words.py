# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from collections import defaultdict
from typing import List


class Solution:
    """
    You are given an array of strings words. Each element of words consists of two lowercase English letters.

    Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

    Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
    """

    def longestPalindrome(self, words: List[str]) -> int:
        """
        Brute force is to try all permutations of words and check if palindrome.

        Solution
            - Have a map of reverse 2 letters
            - Of the ones that have no reverse, if palindrome themselves, we may potentially use.
        """

        word_to_count = defaultdict(int)
        for word in words:
            word_to_count[word] += 1

        length = 0
        print(word_to_count)
        for word, count in word_to_count.items():
            if word[0] == word[1]:
                if count % 2 == 0:
                    length += count * 2
                    word_to_count[word] = 0
                else:
                    length += (count - 1) * 2
                    word_to_count[word] = 1
        print(word_to_count)

        has_double = False
        for word in word_to_count.keys():
            if word_to_count[word] <= 0:
                continue
            rev = word[::-1]
            if word == rev:
                has_double = True
                continue
            if rev in word_to_count and word_to_count[rev] >= 1:
                times = min(word_to_count[rev], word_to_count[word])
                length += times * 4
                word_to_count[word] -= times
                word_to_count[rev] -= times
        if has_double:
            length += 2
        print(word_to_count)
        return length


words = ["ab", "ty", "yt", "lc", "cl", "ab"]
# words = ["lc", "cl", "gg"]
# words = ["cc", "ll", "xx"]
# words = [
#     "dd",
#     "aa",
#     "bb",
#     "dd",
#     "aa",
#     "dd",
#     "bb",
#     "dd",
#     "aa",
#     "cc",
#     "bb",
#     "cc",
#     "dd",
#     "cc",
# ]


print(Solution().longestPalindrome(words))
