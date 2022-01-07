# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    """
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.
    """

    def canJump(self, nums: List[int]) -> bool:
        """
        Questions
            Are there negative integers? Can you jump backwards?
            What does it mean if it's 0? We return false?
            Does max jump length indicate I can choose to jump from 1 - max? Yes
            How long is nums?
            Technical constraints?
            What if nums is empty?
            Is there a case where I should choose not to jump? Don't think so

        Examples
            [1,1,1,1] True
            [1,1,0,1], [True, True, True, False]
            [1,2,0,1], [True, True, True, True]

        Cases
            [] False
            [n] True
            [n1, n2, ...]

        Solution
            Iterate i through len(nums)
            For nums[i] can_arrive where can_arrive[j] = i + range(0, nums[i] + 1)
            Check can_arrive during iteration

        Time: O(n * m), n=len(nums), m=avg(nums[i])
        Space: O(n)
        """

        # Test [3,2,0,4,1], l=5, can_arrive=[t f f f f]
        # i=0, jumps=3, for i+j=[1,3], can_arrive=[t t t t f]
        # i=1, jumps=2, for i+j=[2, 3], can_arrive=[t t t t f]
        # i=2, jumps=0, can_arrive=[t t t t f]
        # i=3, jumps=4, can_arrive=[t t t t t]

        # Test [0,0,0] l=3, can_arrive=[t f f]
        # i=0, jumps=0

        if not nums:
            return False
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        can_arrive = [False] * len(nums)
        can_arrive[0] = True
        for i in range(len(nums)):
            max_jump = nums[i]
            for j in range(1, max_jump + 1):
                if i + j < len(can_arrive):
                    can_arrive[i + j] = True and can_arrive[i]
                    if i + j == len(can_arrive) - 1 and can_arrive[i + j]:
                        return True
        return can_arrive[-1]

    def second(self, nums: List[int]) -> bool:
        def helper(i: int, nums: List[int]) -> int:
            if i == len(nums) - 1:
                return i
            max_i = i
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    max_i = max(max_i, helper(i + j, nums))
            return max_i

        if not nums:
            return False
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        max_i = helper(0, nums)
        return max_i == len(nums) - 1

    def third(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        stack = [0]
        while stack:
            i = stack.pop()
            if i == len(nums) - 1:
                return True
            for j in range(nums[i], 0, -1):
                if i + j == len(nums) - 1:
                    return True
                if i + j < len(nums):
                    stack.append(i + j)
        return False

    def fourth(self, nums: List[int]) -> bool:
        """
        [2,3,1,1,4]
        [1 0 1 0]
        [2 0 0]
        """
        if not nums:
            return False
        if len(nums) == 1:
            return True

        reach = 0
        for i in range(len(nums)):
            if reach < i:
                return False
            reach = max(reach, i + nums[i])
        return reach >= len(nums) - 1


print(Solution().fourth([1, 0, 1, 0]))
print(Solution().fourth([2, 3, 1, 1, 4]))
print(Solution().fourth([3, 2, 1, 0, 4]))
