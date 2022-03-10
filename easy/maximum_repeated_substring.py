# https://leetcode.com/problems/maximum-repeating-substring/

from collections import defaultdict


class Solution:
    """
    For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. 
    The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. 
    If word is not a substring of sequence, word's maximum k-repeating value is 0.

    Given strings sequence and word, return the maximum k-repeating value of word in sequence.
    """
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        ababc, ab
        """
        prefix_length = 2
        prefix = word[:prefix_length]
        prefix_to_i = defaultdict(list)
        for i in range(len(sequence)):
            if sequence[i:i+prefix_length] == prefix:
                prefix_to_i[prefix].append(i)
        
        max_repeats = 0
        repeats = 0
        i = 0
        j = 0
        for i in range(len(sequence)):
            if sequence[i] == word[j]:
                if j == len(word) - 1:
                    repeats += 1
                    j = 0
                else:
                    j += 1
            else:
                max_repeats = max(max_repeats, repeats)
                repeats = 0
                j = 0
        max_repeats = max(max_repeats, repeats)
        return max_repeats

a="aaaba aaaba aabaaaabaaaabaaaabaaaaba"
b="aaaba"

print(Solution().maxRepeating(a, b))