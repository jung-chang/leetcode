# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict
from typing import List, Dict, Set


class Node:
    def __init__(self, course: int):
        self.course = course
        self.edges = []


class Solution:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

    Return the ordering of courses you should take to finish all courses.
    If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dag = defaultdict(list)
        for course, prereq in prerequisites:
            dag[prereq].append(course)
        for i in range(numCourses):
            if i not in dag:
                dag[i] = []

        def topological_sort(dag: Dict[int, List[int]]):
            # 0=not visited, 1=all processed, -1=being processed
            visited = [0 for _ in range(len(dag))]
            result = []

            def dfs(prereq: int):
                if visited[prereq] == -1:
                    return False
                if visited[prereq] == 1:
                    return True
                visited[prereq] = -1
                for course in dag[prereq]:
                    if not dfs(course):
                        return []
                visited[prereq] = 1
                result.append(prereq)
                return True

            for prereq in dag.keys():
                if not dfs(prereq):
                    return []
            return result[::-1]

        return topological_sort(dag)


n = 4
p = [[1, 0], [2, 0], [3, 1], [3, 2]]

# n = 2
# p = [[0, 1], [1, 0]]


print(Solution().findOrder(n, p))
