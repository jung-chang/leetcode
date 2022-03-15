# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/


from collections import defaultdict
import heapq
from typing import List, Set


class Solution:
    """
    There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti]
    represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

    Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold,
    If there are multiple such cities, return the city with the greatest number.

    Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
    """

    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        graph = defaultdict(list)
        for fromi, toi, weighti in edges:
            graph[fromi].append((toi, weighti))
            graph[toi].append((fromi, weighti))

        def get_reachable(start_city: int) -> int:
            min_heap = [(0, start_city)]
            dist = {}

            while min_heap:
                current_distance, city = heapq.heappop(min_heap)
                if city in dist:
                    continue
                dist[city] = current_distance
                for next_city, distance in graph[city]:
                    if next_city in dist:
                        continue
                    if current_distance + distance <= distanceThreshold:
                        heapq.heappush(
                            min_heap, (current_distance + distance, next_city)
                        )
            print(start_city, dist)
            return len(dist)

        reachable_to_cities = defaultdict(list)
        min_reachable = n
        for i in range(n):
            reachable = get_reachable(i)
            reachable_to_cities[reachable].append(i)
            min_reachable = min(min_reachable, reachable)
        print(reachable_to_cities)
        return sorted(reachable_to_cities[min_reachable], reverse=True)[0]

    def first(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        edges_map = defaultdict(dict)
        for fromi, toi, weighti in edges:
            edges_map[fromi][toi] = weighti
            edges_map[toi][fromi] = weighti

        def dfs(city: int) -> Set[int]:
            reachable = set()

            def helper(reached: List[int], threshold: int):
                if threshold > distanceThreshold:
                    return
                city = reached[-1]
                if (city, threshold) in reachable:
                    return
                reachable.add((city, threshold))
                for toi, weighti in edges_map[city].items():
                    if toi not in reached:
                        helper(reached + [toi], threshold + weighti)

            helper([city], 0)
            return set([city for city, _ in reachable]) - set([city])

        reachable_to_city = defaultdict(list)
        min_reachable = n
        for city in range(n):
            reachable = dfs(city)
            print(city, reachable)
            min_reachable = min(min_reachable, len(reachable))
            reachable_to_city[len(reachable)].append(city)

        print(reachable_to_city, min_reachable)
        return sorted(reachable_to_city[min_reachable], reverse=True)[0]


n = 6
e = [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]]
d = 20


# n = 5
# e = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
# d = 2

# n = 8
# e = [
#     [3, 5, 9558],
#     [1, 2, 1079],
#     [1, 3, 8040],
#     [0, 1, 9258],
#     [4, 7, 7558],
#     [5, 6, 8196],
#     [3, 4, 7284],
#     [1, 5, 6327],
#     [0, 4, 5966],
#     [3, 6, 8575],
#     [2, 5, 8604],
#     [1, 7, 7782],
#     [4, 6, 2857],
#     [3, 7, 2336],
#     [0, 6, 6],
#     [5, 7, 2870],
#     [4, 5, 5055],
#     [0, 7, 2904],
#     [1, 6, 2458],
#     [0, 5, 3399],
#     [6, 7, 2202],
#     [0, 2, 3996],
#     [0, 3, 7495],
#     [1, 4, 2262],
#     [2, 6, 1390],
# ]
# d = 7937


print(Solution().findTheCity(n, e, d))
