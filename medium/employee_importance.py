# https://leetcode.com/problems/employee-importance/

from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:

        id_to_employee = {}

        def get_importance(employee: Employee) -> int:
            importance = 0

            def dfs(employee: Employee):
                nonlocal importance
                importance += employee.importance
                for id in employee.subordinates:
                    dfs(id_to_employee[id])

            dfs(employee)
            return importance

        for employee in employees:
            id_to_employee[employee.id] = employee
        return get_importance(id_to_employee[id])
