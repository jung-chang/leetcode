# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict
import heapq
from typing import List


class Solution:
    """ "
    There are n cities connected by some number of flights.
    You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight
    from city fromi to city toi with cost pricei.

    You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
    If there is no such route, return -1.
    """

    def disjktra(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """
        DP approach.
        dp[toi] = min price from src to toi
        dp[toi] =
        """
        flight_map = defaultdict(list)
        for fromi, toi, pricei in flights:
            flight_map[fromi].append((toi, pricei))

        visited = {}
        min_heap = [(0, src, 0)]
        while min_heap:
            price, city, stops = heapq.heappop(min_heap)
            if stops - 1 > k:
                continue
            if city == dst:
                return price
            if city not in visited or visited[city] > stops:
                visited[city] = stops
                for toi, pricei in flight_map[city]:
                    heapq.heappush(min_heap, (price + pricei, toi, stops + 1))
        return -1

    def findCheapestPrice2(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """
        Min price to get to dst is min
        """
        flight_map = defaultdict(list)
        for fromi, toi, pricei in flights:
            flight_map[fromi].append((toi, pricei))

        dst_to_min_price = {}

        def dfs(path: List[int], price: int):
            cur = path[-1]

            if cur in dst_to_min_price:
                dst_to_min_price[cur] = min(price, dst_to_min_price[cur])
            else:
                dst_to_min_price[cur] = price

            if cur == dst:
                return

            if len(path) - 1 > k:
                return

            for toi, pricei in flight_map[cur]:
                if toi not in path:
                    dfs(path + [toi], price + pricei)

        dfs([src], 0)
        return dst_to_min_price[dst] if dst in dst_to_min_price else -1


n = 4
f = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
src = 0
dst = 3
k = 1

print(Solution().disjktra(n, f, src, dst, k))
