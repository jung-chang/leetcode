# https://leetcode.com/problems/4sum-ii/

from collections import defaultdict
from typing import List


class Solution:
    """
    Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

    """

    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        """
        All the same length

        Fix 3 ijk, and find l
            - find sum of ijk and see if negative is in l
            -   would need all permutations of ijk

        Fix 2 ij and find kl
            - sum ij and find negative sum kl
            - determine how many permutations sum to x in each ij and -x in kl
        """
        n = len(nums1)
        if not n:
            return 0
        sum_ij = defaultdict(lambda: 0)
        sum_kl = defaultdict(lambda: 0)
        for i in range(n):
            for j in range(n):
                ij = nums1[i] + nums2[j]
                kl = nums3[i] + nums4[j]
                sum_ij[ij] += 1
                sum_kl[kl] += 1

        result = 0
        for num, count in sum_ij.items():
            result += count * sum_kl[-1 * num]
        return result


n1 = [1, 2]
n2 = [-2, -1]
n3 = [-1, 2]
n4 = [0, 2]
print(Solution().fourSumCount(n1, n2, n3, n4))
