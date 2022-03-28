# https://leetcode.com/problems/word-subsets/

from collections import defaultdict
from typing import List, Dict


class Solution:
    """
    You are given two string arrays words1 and words2.

    A string b is a subset of string a if every letter in b occurs in a including multiplicity.
    For example, "wrr" is a subset of "warrior" but is not a subset of "world".

    A string a from words1 is universal if for every string b in words2, b is a subset of a.
    Return an array of all the universal strings in words1. You may return the answer in any order.
    """

    def second(self, words1: List[str], words2: List[str]) -> List[str]:
        def create_word_map(word: str) -> Dict[str, int]:
            word_map = defaultdict(int)
            for letter in word:
                word_map[letter] += 1
            return word_map

        def is_subset(map1, map2) -> bool:
            for letter, freq in map2.items():
                if letter not in map1:
                    return False
                if map1[letter] < freq:
                    return False
            return True

        words_to_maps = defaultdict(int)
        for word in words1:
            words_to_maps[word] = create_word_map(word)

        bmax_map = defaultdict(int)
        for word in words2:
            word_map = create_word_map(word)
            for letter, freq in word_map.items():
                bmax_map[letter] = max(bmax_map[letter], freq)

        result = []
        for word1 in words1:
            if is_subset(words_to_maps[word1], bmax_map):
                result.append(word1)
        return result

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def create_word_map(word: str) -> Dict[str, int]:
            word_map = defaultdict(int)
            for letter in word:
                word_map[letter] += 1
            return word_map

        words_to_maps = defaultdict(int)
        for word in words1:
            words_to_maps[word] = create_word_map(word)
        for word in words2:
            words_to_maps[word] = create_word_map(word)

        def is_subset(word: str, sub: str) -> str:
            word_map = words_to_maps[word]
            for letter, freq in words_to_maps[sub].items():
                if letter not in word_map:
                    return False
                if word_map[letter] < freq:
                    return False
            return True

        result = []
        for word1 in words1:
            subset = True
            for word2 in words2:
                if not is_subset(word1, word2):
                    subset = False
                    break
            if subset:
                result.append(word1)
        return result


w1 = ["amazon", "apple", "facebook", "google", "leetcode"]
w2 = ["e", "o"]
print(Solution().wordSubsets(w1, w2))
