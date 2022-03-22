# https://www.lintcode.com/problem/812/
# https://leetcode.com/problems/bold-words-in-string/

from collections import defaultdict
from typing import (
    List,
)


class Solution:
    """
    Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.
    The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

    Input:
    ["ab", "bc"]
    "aabcd"

    Output:
    "a<b>abc</b>d"

    Cases
    abc, bcde
    abcde
    """

    def bold_words(self, words: List[str], s: str) -> str:
        """
        Notes:
            - Not as simple as checking if word exists in list
            - Least number of tags indicate no nested bold tags
            - We need to identify the longest substrings in s that we can make with our list

        Solution
            - Identify all ranges of indices in s that should be bolded
            - Merge these ranges to find least number of tags

        """

        prefix_to_words = defaultdict(list)
        for word in words:
            prefix_to_words[word[0]].append(word)

        ranges = []
        for i, letter in enumerate(s):
            for word in prefix_to_words[letter]:
                left = i
                right = i + len(word)
                if s[left:right] == word:
                    if not ranges:
                        ranges.append((left, right))
                        continue
                    l, r = ranges[-1]
                    if r >= left:
                        ranges.pop()
                        ranges.append((min(l, left), max(r, right)))
                    else:
                        ranges.append((left, right))
        result = ""
        start = 0
        for l, r in ranges:
            result += s[start:l]
            result += "<b>"
            result += s[l:r]
            result += "</b>"
            start = r
        if start < len(s):
            result += s[start:]
        return result


w = ["ab", "bc"]
s = "aabcd"

w = [
    "bcccaeb",
    "b",
    "eedcbda",
    "aeebebebd",
    "ccd",
    "eabbbdcde",
    "deaaea",
    "aea",
    "accebbb",
    "d",
]
s = "ceaaabbbedabbecbcced"

w = []
s = "ASD"

w = ["abc", "bcde"]
s = "abcde"
print(Solution().bold_words(w, s))
