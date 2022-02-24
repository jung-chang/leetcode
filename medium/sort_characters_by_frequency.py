# https://leetcode.com/problems/sort-characters-by-frequency/


from collections import defaultdict
import heapq


class Solution:
    """
    Given a string s, sort it in decreasing order based on the frequency of the characters.
    The frequency of a character is the number of times it appears in the string.

    Return the sorted string. If there are multiple answers, return any of them.
    """

    def frequencySort(self, s: str) -> str:
        char_to_freq = defaultdict(int)
        for c in s:
            char_to_freq[c] += 1

        max_heap = []
        for char, freq in char_to_freq.items():
            heapq.heappush(max_heap, (-freq, char))

        result = ""
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result += char * (-1 * freq)
        return result


print(Solution().frequencySort("cccaaa"))
