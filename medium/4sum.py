# https://leetcode.com/problems/4sum/

from typing import List, Set, Tuple


class Solution:
    """
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

        0 <= a, b, c, d < n
        a, b, c, and d are distinct.
        nums[a] + nums[b] + nums[c] + nums[d] == target

    You may return the answer in any order.
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def get_two_sum(t: int, avoid: Set[int]) -> Set[Tuple[int, int]]:
            """
            [0 1 2 3 -2] t=2
            {2:0, 1:1, 0:2, -1:3, 0: 4}
            """
            result = set()
            diff_to_i = {}
            for i, num in enumerate(nums):
                diff_to_i[t - num] = i
            for i, num in enumerate(nums):
                if num in diff_to_i:
                    j = diff_to_i[num]
                    if i != j and i not in avoid and j not in avoid:
                        result.add((i, j))
            return result

        result = []
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                cur_sum = nums[i] + nums[j]
                # print(i, j, cur_sum)
                for x, y in get_two_sum(target - cur_sum, set([i, j])):
                    quad = sorted([nums[i], nums[j], nums[x], nums[y]])
                    if quad not in result:
                        # print(quad)
                        result.append(quad)
        return result


nums = [1, 0, -1, 0, -2, 2]
target = 0

print(Solution().fourSum(nums, target))
