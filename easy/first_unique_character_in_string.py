# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import defaultdict


class Solution:
    """
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
    """

    def firstUniqChar(self, s: str) -> int:
        """
        Index map and get min index of chracters that only appear once.
        """
        if not s:
            return -1
        index_map = {}
        count_map = defaultdict(lambda: 0)

        for i, letter in enumerate(s):
            if index_map.get(letter) is None:
                index_map[letter] = i
            count_map[letter] += 1

        uniques = [letter for letter, count in count_map.items() if count == 1]
        min_index = None
        for letter in uniques:
            if min_index is None:
                min_index = index_map[letter]
            else:
                min_index = min(index_map[letter], min_index)
        return -1 if min_index is None else min_index


print(Solution().second("loveleetcode"))
