# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict
from typing import List


class Solution:
    """
    Return the ordering of courses you should take to finish all courses.
    If there are many valid answers, return any of them.
    If it is impossible to finish all courses, return an empty array.
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Time limit exceed
        """
        to_prereqs = defaultdict(set)
        to_courses = defaultdict(set)
        for course, prereq in prerequisites:
            to_prereqs[course].add(prereq)
            to_courses[prereq].add(course)

        def has_all_prereqs(course: int, taken: List[int]) -> int:
            taken_set = set(taken)
            prereq_set = set(to_prereqs[course])
            return taken_set.issuperset(prereq_set)

        def courses_can_take(taken: List[int]) -> List[int]:
            potential_courses = set()
            for course in taken:
                potential_courses.update(to_courses[course])

            cant_take = set()
            for course in potential_courses:
                if not has_all_prereqs(course, taken):
                    cant_take.add(course)
            return potential_courses - cant_take - set(taken)

        no_prereqs = [num for num in range(numCourses) if num not in to_prereqs]
        if not to_prereqs:
            return no_prereqs

        taken = no_prereqs
        while True:
            to_take = courses_can_take(taken)
            print(to_take)
            if not to_take:
                return []
            for course in to_take:
                to_prereqs.pop(course)
                taken.append(course)
            if len(taken) == numCourses:
                return taken

    def recursive(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for course, prereq in prerequisites:
            graph[course].add(prereq)
        no_prereqs = [num for num in range(numCourses) if num not in graph]
        if not graph:
            return no_prereqs

        result = []
        # 0=not visited, 1=all processed, -1=being processed
        visited = [0] * numCourses

        def DFS(course: int):
            nonlocal result
            nonlocal visited

            # A cycle has occured
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1
            for prereq in graph[course]:
                if not DFS(prereq):
                    return []
            visited[course] = 1
            result.append(course)
            return True

        for course in range(numCourses):
            if not DFS(course):
                return []
        return result


n = 2
p = [[1, 0]]
print(Solution().recursive(n, p))
