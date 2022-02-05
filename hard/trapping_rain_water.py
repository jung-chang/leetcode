# https://leetcode.com/problems/trapping-rain-water/

from typing import List, Tuple


class Solution:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    """

    def trap(self, height: List[int]) -> int:
        """
        DP approach.
        Find max height looking from left. Do the same from right.
        """
        left = []
        right = []

        max_left = 0
        for i in range(len(height)):
            max_left = max(max_left, height[i])
            left.append(max_left)

        max_right = 0
        for i in range(len(height) - 1, -1, -1):
            max_right = max(max_right, height[i])
            right = [max_right] + right

        water = 0
        for i in range(len(height)):
            water += min(left[i], right[i]) - height[i]
        return water

    def levelIterate2(self, height: List[int]) -> int:
        """
        Simpler level iterate

        Also time limit exceeds...
        """
        max_height = max(height)
        length = len(height)

        water = 0
        for level in range(1, max_height + 1):
            level_heights = []
            first_one = None
            last_one = 0
            for i in range(length):
                if height[i] >= level:
                    level_heights.append(1)
                    if first_one is None:
                        first_one = i
                    last_one = i
                else:
                    level_heights.append(0)
            if first_one is None:
                first_one = 0
            level_heights = level_heights[first_one:last_one]
            water += level_heights.count(0)
        return water

    def levelIterate(self, height: List[int]) -> int:
        """
        Raise water level from 1 to max(height).
        At each level, determine if the water is trapped
            - if there are 2 walls on either side that trap the water
            - do this for every "hole" at the level

        Time limit exceed.
        """
        max_height = max(height)
        length = len(height)
        if not height or not max_height:
            return 0

        water = 0
        for level in range(1, max_height + 1):
            i = 0
            while i < length:

                # Find first wall
                if not height[i] >= level:
                    i += 1
                    continue

                # Find next wall
                j = i + 1
                while j < length and height[j] < level:
                    j += 1
                if j >= length:
                    break

                # Add trapped water
                water += j - i - 1
                i = j
        return water


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# print(Solution().trap([4, 2, 0, 3, 2, 5]))
