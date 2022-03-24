# https://leetcode.com/problems/ransom-note/

from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_to_freq = defaultdict(int)
        for letter in magazine:
            letter_to_freq[letter] += 1
        
        for letter in ransomNote:
            if letter_to_freq[letter] < 1:
                return False
            letter_to_freq[letter] -= 1
        return True