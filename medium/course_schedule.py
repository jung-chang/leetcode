# https://leetcode.com/problems/course-schedule/

from collections import defaultdict
from typing import List, Set


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

        Time limit exceed.
        """

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        if not graph:
            return True

        # 0=not visited, 1=all processed, -1=being processed
        state = [0] * numCourses

        def has_cycle(course: int, courses_taken: Set[int]):
            nonlocal graph
            if state[course] == 1:
                return False
            if state[course] == -1:
                return True

            state[course] = -1
            if course in courses_taken:
                return True
            courses_taken.add(course)
            for prereq in graph[course]:
                if has_cycle(prereq, courses_taken.copy()):
                    return True
            state[course] = 1
            return False

        for course in list(graph.keys()):
            if has_cycle(course, set([])):
                return False
        return True

    def iterative(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        if not graph:
            return True

        visited = set(list(graph.keys()))

        # no_prereqs = set([num for num in range(numCourses) if num not in graph.keys()])
        stack = [[num] for num in graph.keys()]
        while stack:
            path = stack.pop()
            for prereq in graph[path[-1]]:
                if prereq in path:
                    return False
                if prereq in visited:
                    continue
                visited.add(prereq)
                stack.append(path + [prereq])
        return True


n = 2
p = [[1, 0], [0, 1]]

# n = 5
# p = [[1, 4], [2, 4], [3, 1], [3, 2]]


print(Solution().iterative(n, p))
