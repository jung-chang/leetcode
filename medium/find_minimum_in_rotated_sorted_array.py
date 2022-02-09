# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.

    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    """

    def findMin(self, nums: List[int]) -> int:
        """
        Easy O(n) algorithm.

        Let's do binary search.
        3 cases:
            - Normal rotated
            - Strictly ascending
            - Strictly descending
        """

        def search(nums: List[int]) -> int:
            """
            [4 5 6] [7 0 1 2] -> [7 0] [1 2] -> [7] [0]
            [6 7 0] [1 2 4 5]
            """
            if not nums:
                return
            if len(nums) <= 2:
                return min(nums)

            mid = len(nums) // 2
            left_min, left_max = nums[0], nums[mid - 1]
            right_min, right_max = nums[mid], nums[len(nums) - 1]
            print(nums[:mid], nums[mid:])

            # [6 5 4] [3 2 1] asc
            # [1 2 3] [4 5 6] desc
            # [5 6 1] [2 3 4] rotated
            if left_min > left_max and left_max < right_max:
                return search(nums[:mid])
            elif right_min >= right_max and right_max < left_max:
                return search(nums[mid:])
            else:
                if left_min < right_min:
                    return search(nums[:mid])
                return search(nums[mid:])

        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        return search(nums)


print(Solution().findMin([6, 7, 5, 5, 6, 6, 6]))
print(Solution().findMin([6, 5, 4, 3, 2, 1]))
print(Solution().findMin([1, 2, 3, 4, 5, 6, 7]))
print(
    Solution().findMin(
        [
            4,
            5,
            6,
            7,
            1,
            2,
            3,
        ]
    )
)
