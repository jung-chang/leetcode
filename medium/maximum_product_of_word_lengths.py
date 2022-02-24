# https://leetcode.com/problems/maximum-product-of-word-lengths/

from collections import defaultdict
from typing import List


class Solution:
    """
    Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
    If no such two words exist, return 0.
    """

    def maxProduct(self, words: List[str]) -> int:
        def mask(word: str) -> int:
            result = 0
            for w in word:
                result |= 1 << (ord(w) - ord("a"))
            return result

        i_to_mask = {i: mask(word) for i, word in enumerate(words)}

        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if i_to_mask[i] & i_to_mask[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product

    def first(self, words: List[str]) -> int:
        def overlaps(a: str, b: str) -> bool:
            small = a
            big = b
            if len(a) > len(b):
                big = a
                small = b
            big_set = set(big)
            for c in small:
                if c in big_set:
                    return True
            return False

        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                i_len = len(words[i])
                j_len = len(words[j])
                product = i_len * j_len
                if product <= max_product:
                    continue
                if not overlaps(words[i], words[j]):
                    # print(words[i], words[j])
                    max_product = max(max_product, product)
        return max_product


print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
