# https://leetcode.com/problems/perfect-squares/


class Solution:
    """
    Given an integer n, return the least number of perfect square numbers that sum to n.

    A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
    """

    def numSquares(self, n: int) -> int:
        """
        dp[i] = minimum number of perfect squares that sum to i
        dp[i] = min(1 + dp[i - root], 1 if perfect square, )

        12 - 9 - 1 -1 -1
        12 - 4 - 4 - 4
        """

        if n <= 3:
            return n
        dp = [0, 1, 2, 3]
        perfect_squares = []
        for i in range(4, n + 1):
            root = int(i ** 0.5)
            if root * root == i:
                dp.append(1)
                perfect_squares.append(i)
                continue
            possible = [1 + dp[i - 1]]
            if i % 2 == 0:
                possible.append(dp[i // 2] * 2)
            if i % 3 == 0:
                possible.append(dp[i // 3] * 3)
            for square in perfect_squares:
                possible.append(1 + dp[i - square])
            dp.append(min(possible))
        print(dp)
        return dp[-1]

    def BFS(self, n: int) -> int:
        # 1 4 9 16 25
        if n <= 0:
            return 0
        perfect_squares = []
        squares_set = set(perfect_squares)
        i = 1
        while i * i <= n:
            perfect_squares.append(i * i)
            i += 1
        # 12 [9 1 1 1]
        # 12 [4 4 1 1 1 1]
        min_squares = float("inf")
        queue = [(n - square, 1) for square in perfect_squares if square]
        while queue:
            result, num_squares = queue.pop(0)
            if result == 0:
                min_squares = min(min_squares, num_squares)
                continue
            if result in squares_set:
                min_squares = min(min_squares, num_squares + 1)
                continue
            for square in perfect_squares[::-1]:
                if square > result:
                    continue
                queue.append((result - square, num_squares + 1))
        return min_squares


print(Solution().numSquares(20))
