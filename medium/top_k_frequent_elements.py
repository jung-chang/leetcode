# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
from typing import List
import heapq


class Solution:
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.
    """

    def hash(self, nums: List[int], k: int) -> List[int]:
        """
        Use a hashmap? O(n) time with O(n) space.
        """

        num_to_frequency = defaultdict(lambda: 0)
        for num in nums:
            num_to_frequency[num] += 1

        most_frequent = []
        for num, _ in sorted(
            num_to_frequency.items(), key=lambda x: x[1], reverse=True
        ):
            most_frequent.append(num)
            if len(most_frequent) == k:
                break
        return most_frequent

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Uses a max heap where priority is frequency.
        Python tuples in heap is (priority, task)
        """

        num_to_frequency = defaultdict(lambda: 0)
        for num in nums:
            num_to_frequency[num] += 1

        heap = []
        for num, freq in num_to_frequency.items():
            heapq.heappush(heap, (-1 * freq, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
