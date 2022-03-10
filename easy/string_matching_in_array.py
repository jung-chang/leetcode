# https://leetcode.com/problems/string-matching-in-an-array/

from typing import List

class Solution:
    """
    Given an array of string words. Return all strings in words which is substring of another word in any order. 

    String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
    """
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if len(words[i]) >= len(words[j]):
                    continue
                if words[i] in result:
                    continue
                if words[i] in words[j]:
                    result.add(words[i])
        return list(result)
    

print(Solution().stringMatching(["leetcoder","leetcode","od","hamlet","am"]))