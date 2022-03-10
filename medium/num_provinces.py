# https://leetcode.com/problems/number-of-provinces/

from typing import List, Set


class Solution:
    """
    There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no other cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_cities = len(isConnected)
        if not num_cities:
            return 0

        def dfs(input_city: int):
            province = set()
            stack = [input_city]
            while stack:
                city = stack.pop()
                province.add(city)
                for i in range(num_cities):
                    if i in province:
                        continue
                    if isConnected[city][i]:
                        stack.append(i)
            return province

        def dfs_recur(input_city: int, province: Set[int]):
            for city in range(num_cities):
                if city in province:
                    continue
                if isConnected[input_city][city]:
                    province.add(city)
                    dfs_recur(city, province)
            return province

        visited = set()
        provinces = []
        for city in range(num_cities):
            if city in visited:
                continue
            # province = dfs(city)
            province = dfs_recur(city, set())
            visited.update(province)
            provinces.append(province)
        print(provinces)
        return len(provinces)


c = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
]

c = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1],
]


print(Solution().findCircleNum(c))
