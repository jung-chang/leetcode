# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq
from typing import List


class Solution:
    """
    Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

    Note that it is the kth smallest element in the sorted order, not the kth distinct element.

    You must find a solution with a memory complexity better than O(n2).
    """

    def bin_search(self, nums: List[int], k: int) -> int:
        print(nums)
        if k > len(nums):
            return None

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        if k == 1:
            return nums[0]
        elif len(left) < k:
            return self.bin_search(right, k - len(left))
        else:
            return self.bin_search(left, k)

    def bin(self, matrix: List[List[int]], k: int) -> int:
        """
        k = 5, r=4

        1 3 4
        2 4 6
        5 6 7

        if k > n*n, is there a result?

        - Find which row the kth smallest is in, then binary search that row
        """

        # 1 3 5 6, k=3

        if not matrix:
            return None

        return self.bin_search(sorted([num for row in matrix for num in row]), k)

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                heapq.heappush(min_heap, matrix[r][c])
        for _ in range(k - 1):
            heapq.heappop(min_heap)
        return heapq.heappop(min_heap)


matrix = [[1, 2], [1, 3]]
k = 2


# print(Solution().bin_search([1, 1, 2, 3], k=2))
# print(Solution().bin_search([1, 2, 3, 4, 5], k=2))
# print(Solution().bin_search([1, 2, 3, 4, 5], k=3))
# print(Solution().bin_search([1, 2, 3, 4, 5], k=4))
# print(Solution().bin_search([1, 2, 3, 4, 5], k=5))
# print(Solution().bin_search([1, 2, 3, 4, 5], k=6))

print(Solution().kthSmallest(matrix, k))
