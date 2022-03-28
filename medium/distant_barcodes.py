# https://leetcode.com/problems/distant-barcodes/

from collections import defaultdict
import collections
import heapq
from typing import List


class Solution:
    """
    In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

    Rearrange the barcodes so that no two adjacent barcodes are equal.
    You may return any answer, and it is guaranteed an answer exists.

    Cases
    - 11112222
    - 111 222 333

    """

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcode_freq = defaultdict(int)
        for code in barcodes:
            barcode_freq[code] += 1

        max_heap = []
        for code, freq in barcode_freq.items():
            heapq.heappush(max_heap, (freq, code))

        common_order = []
        while max_heap:
            freq, code = heapq.heappop(max_heap)
            common_order += [code] * freq

        for i in range(0, len(barcodes), 2):
            barcodes[i] = common_order.pop()
        for i in range(1, len(barcodes), 2):
            barcodes[i] = common_order.pop()
        return barcodes


b = [1, 1, 1, 1, 2, 2, 3, 3]
print(Solution().rearrangeBarcodes(b))
