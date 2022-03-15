# https://leetcode.com/problems/course-schedule-iv/

from collections import defaultdict
from typing import List, Set


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:

        course_to_prereqs = {}
        course_to_all_prereqs = {}

        def dfs(course: int) -> Set[int]:
            visited = set()

            def helper(course: int):
                visited.add(course)
                for prereq in course_to_prereqs[course]:
                    if prereq not in visited:
                        helper(prereq)

            helper(course)
            course_to_all_prereqs[course] = visited
            return visited

        for i in range(numCourses):
            course_to_prereqs[i] = []
        for prereq, course in prerequisites:
            course_to_prereqs[course].append(prereq)

        result = []
        for prereq, course in queries:
            if course in course_to_all_prereqs:
                result.append(prereq in course_to_all_prereqs[course])
            else:
                all_prereqs = dfs(course)
                result.append(prereq in all_prereqs)
        return result


n = 3
p = [[1, 2], [1, 0], [2, 0]]
q = [[1, 0], [1, 2]]
print(Solution().checkIfPrerequisite(n, p, q))
