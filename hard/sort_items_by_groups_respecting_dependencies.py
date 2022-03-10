# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

from collections import defaultdict
from typing import List, Dict


class Solution:
    """
    TODO
    There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group.
    The items and the groups are zero indexed. A group can have no item belonging to it.

    Return a sorted list of the items such that:

    The items that belong to the same group are next to each other in the sorted list.
    There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).

    Return any solution if there is more than one solution and return an empty list if there is no solution.
    """

    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        group_to_items = {-1: []}
        for i in range(m):
            group_to_items[i] = []
        for i in range(len(group)):
            g = group[i]
            group_to_items[g].append(i)
        print(group_to_items)

        group_to_before_groups = {}
        for g, items in group_to_items.items():
            if g not in group_to_before_groups:
                group_to_before_groups[g] = set()
            for item in items:
                for before_item in beforeItems[item]:
                    group_to_before_groups[g].add(group[before_item])
        print(group_to_before_groups)

        def topological_sort(graph: Dict[int, List[int]]):
            visited = [0 for _ in range(n)]
            result = []

            def dfs(item: int):
                if visited[item] == -1:
                    return False
                if visited[item] == 1:
                    return True
                visited[item] = -1
                for before in graph[item]:
                    if not dfs(before):
                        return False
                visited[item] = 1
                result.append(item)
                return True

            for i in range(n):
                if not dfs(i):
                    return []
            return result

        # sorted_groups = topological_sort(group_to_befores)
        # output = []
        # print(sorted_groups)

        # for group in sorted_groups:
        #     output.extend(group_to_items[group])

        # print(output)


n = 8
m = 2
group = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
print(Solution().sortItems(n, m, group, beforeItems))
