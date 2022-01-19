# https://leetcode.com/problems/count-primes/


class Solution:
    """
    Given an integer n, return the number of prime numbers that are strictly less than n.
    """

    def countPrimes(self, n: int) -> int:
        """
        1. Go from 1 to n and check if each is prime. Then count how many primes.
        2. Start from 2 to n and set all indices of multiples to false
        """
        if n <= 2:
            return 0
        table = [1] * n
        table[0] = 0
        table[1] = 0
        count = 0

        for i in range(2, n):
            if table[i] == 1:
                count += 1
                for j in range(2 * i, n, i):
                    table[j] = 0
        return count


print(Solution().countPrimes(10))
