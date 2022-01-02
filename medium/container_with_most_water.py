# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
    """

    def first(self, height: List[int]) -> int:
        """
        Effectively trying to maximize A(1,2) = min(y1, y2) * abs(x1 - x2)

        Can brute each pair of walls to find area.

        Time exceeded
        """
        max_area = 0
        visited = set()
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height):
                if i == j:
                    continue
                y = min(h1, h2)
                x = abs(j - i)
                if (x, y) in visited:
                    continue
                max_area = max(x * y, max_area)
                visited.add((x, y))
                visited.add((y, x))
        return max_area

    def second(self, height: List[int]) -> int:
        """
        Raise water levels and check which areas are valid

        With fixed height, find the furthest pairs of walls up to that height.

        Still very slow
        """
        if len(height) < 2:
            return 0
        max_area = 0
        for water in range(max(height) + 1):
            left = 0
            right = len(height) - 1
            while left < right:
                if height[left] >= water and height[right] >= water:
                    break
                if height[left] < water:
                    left += 1
                if height[right] < water:
                    right -= 1
            max_area = max(max_area, water * abs(right - left))
        return max_area

    def second(self, height: List[int]) -> int:
        """
        Raise water levels and check which areas are valid


        With fixed height, find the furthest pairs of walls up to that height.

        Still very slow.
        """
        if len(height) < 2:
            return 0
        max_area = 0
        for water in reversed(range(max(height) + 1)):
            if water * len(height) < max_area:
                continue
            left = 0
            right = len(height) - 1
            while left < right:
                if height[left] >= water and height[right] >= water:
                    break
                if height[left] < water:
                    left += 1
                if height[right] < water:
                    right -= 1
            max_area = max(max_area, water * abs(right - left))
        return max_area

    def third(self, height: List[int]) -> int:
        """
        Shifting 2 pointers left and right. Only move if it makes sense to.
        """
        if len(height) < 2:
            return 0
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            x = abs(right - left)
            y = min(height[left], height[right])
            max_area = max(max_area, x * y)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area


print(Solution().third([1, 1]))
