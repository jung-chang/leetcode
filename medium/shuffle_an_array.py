# https://leetcode.com/problems/shuffle-an-array/

from collections import defaultdict
from email.policy import default
import random
from typing import List, Dict


class Solution:
    """
    Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

    Implement the Solution class:
        Solution(int[] nums) Initializes the object with the integer array nums.
        int[] reset() Resets the array to its original configuration and returns it.
        int[] shuffle() Returns a random shuffling of the array.

    """

    def __init__(self, nums: List[int]):
        self.original_nums = nums
        self.nums = nums

        self.i_to_num = self._create_i_to_num(self.nums)

    def reset(self) -> List[int]:
        self.nums = self.original_nums
        self.i_to_num = self._create_i_to_num(self.nums)
        return self.nums

    def shuffle(self) -> List[int]:
        self.nums = []
        while self.i_to_num:
            i = random.choice(list(self.i_to_num))
            self.nums.append(self.i_to_num[i])
            self.i_to_num.pop(i)
        self.i_to_num = self._create_i_to_num(self.nums)
        return self.nums

    def _create_i_to_num(self, nums: List[int]) -> Dict[int, int]:
        i_to_num = {}
        for i, num in enumerate(nums):
            i_to_num[i] = num
        return i_to_num


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

sol = Solution([1, 2, 3])
table = defaultdict(lambda: 0)
for i in range(1000):
    shuffle = sol.shuffle()
    table[str(shuffle)] += 1

print(table)
