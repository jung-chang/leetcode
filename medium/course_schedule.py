# https://leetcode.com/problems/course-schedule/

from collections import defaultdict
from typing import List


class Solution:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

    Return true if you can finish all courses. Otherwise, return false.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Create a directed graph and check if there are any cycles.

        Use a hash map to represent the grpah. Node as key, edges as values.
        """

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for starting_course in range(numCourses):
            queue = [[starting_course]]
            while queue:
                path = queue.pop(0)
                for prereq in graph[course]:
                    if prereq in path:
                        return False
                    queue.append(path + [prereq])
        return True


numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(Solution().canFinish(2, prerequisites))
