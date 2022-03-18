# https://leetcode.com/problems/top-k-frequent-words/

from collections import defaultdict
import heapq
from typing import List


class Solution:
    """
    Given an array of strings words and an integer k, return the k most frequent strings.

    Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_to_count = defaultdict(int)
        for word in words:
            words_to_count[word] += 1
        max_heap = []
        for word, count in words_to_count.items():
            heapq.heappush(max_heap, (-1 * count, word))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])
        return result


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(Solution().topKFrequent(words, k))
