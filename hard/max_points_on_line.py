# https://leetcode.com/problems/max-points-on-a-line/

from collections import defaultdict
from typing import List
import math


class Solution:
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
    return the maximum number of points that lie on the same straight line.
    """

    def maxPoints(self, points: List[List[int]]) -> int:
        def get_angle(point2, point1) -> float:
            """
            Uses arctan to get tangle between horizontal and point = arctan(y/x)
            Cases
                - if x > 0, return angle
                - if x < 0, angle + pi if >=0 else - pi
                - if x=y=0, just a center point
                - if x=0, pi/2 if y > 0 else -pi/2
            """
            x2, y2 = point2
            x1, y1 = point1
            radians = math.atan2(y2 - y1, x2 - x1)
            return math.degrees(radians)

        if len(points) <= 1:
            return len(points)

        max_points = 0
        for i in range(len(points)):
            angle_to_points = defaultdict(list)
            for j in range(len(points)):
                if i == j:
                    continue
                if points[j] == points[i]:
                    for angle in angle_to_points.keys():
                        angle_to_points[angle].append(points[j])
                        continue
                angle = get_angle(points[j], points[i])
                angle_to_points[angle].append(points[j])
            if angle_to_points:
                # print(points[i], angle_to_points)
                max_points = max(
                    max_points,
                    max([len(values) for values in angle_to_points.values()]) + 1,
                )
        return max_points


points = [[1, 0], [0, 0]]
print(Solution().maxPoints(points))
