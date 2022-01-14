# https://leetcode.com/problems/gas-station/

from typing import List


class Solution:
    """
    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Examples
        gas=[1 2 3]
        cost=[1 2 3], dp=[0, 0, 0]
        cost=[3,2,1], dp=[-2, -4, 0]

        dp[i] = dp[i-1] + gas-cost

        i=0, has 1 gas, it takes 5 gas to get to i=1

        Return -1 if cant complete circuit.

        Solution
            - Iterate through gas[] and cost[], determine if you can get from i to i+1 with gas + gas[i] - cost[i]
            - sum(gas[i...j]) = amount of accumulated gas from i to j
            - sum(cost[i...j]) = amount of gas needed to get from i to j

        Is there a case where you have to start at i instead <i or >i
        gas = [1 2 3]
        cost = [3 2 1]
        start i=2, gas=3, cost=1 -> gas=2

        Improvements
            - "jump" from i to j with leftover gas

        gas = [1,2,3,4,5,1]
        cost =[3,4,5,1,2,3]
        dp[i] = gas at ith day after filling
        dp = [1, 0, -1, -2, 2, 1, -1]
        """

        # start: (end, leftover gas)
        jump_map = {}

        def can_complete(start: int) -> bool:
            """
            [1 2 2], start=1, len=3
            [3 2 3]
            """
            cur = start
            total_gas = gas[start] - cost[start]
            while total_gas >= 0 and (cur + 1) % len(cost) != start:
                cur += 1
                cur = cur % len(cost)
                total_gas += gas[cur] - cost[cur]
            return total_gas >= 0

        for i in range(len(gas)):
            completed, gas_left, end = can_complete(i)
            if completed:
                return i

            if jump_map.get(i) is not None:
                map_end, _ = jump_map[i]
                if end > map_end:
                    jump_map[i] = (end, gas_left)
            else:
                jump_map[i] = (end, gas_left)
            print(jump_map)
        return -1

    def second(self, gas: List[int], cost: List[int]) -> int:
        """
        g=[1 2 3, 2, 3]
        c=[3 2 1, 4, 1]
        dp=[-2, 0, 2, -2, 2]

        g=[1 2 1]
        c=[3 2 1]
        dp=[-2 0 0]

        g=[5,1,2,3,4]
        c=[4,4,1,5,1]
        d=[1,-3,1,-2,3]

        Gas costs has to sum to >= 0 t be valid.
        Keep track of minimum gas amount accumulated. Just start one station after that one.\
        """

        lowest_gas = gas[0]
        lowest_gas_index = 0
        total_gas = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            if total_gas < lowest_gas:
                lowest_gas = total_gas
                lowest_gas_index = i
        if total_gas < 0:
            return -1
        return (lowest_gas_index + 1) % len(gas)


print(
    Solution().canCompleteCircuit(
        [5, 1, 2, 3, 4, 1, 2, 6, 8, 4, 3, 2, 5], [4, 4, 1, 5, 1, 1, 2, 3, 4, 5, 6, 7, 8]
    )
)
