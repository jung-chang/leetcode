# https://leetcode.com/problems/guess-number-higher-or-lower/

def guess(n):
    return

class Solution:
    """
    We are playing the Guess Game. The game is as follows:

    I pick a number from 1 to n. You have to guess which number I picked.

    Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

    You call a pre-defined API int guess(int num), which returns three possible results:
        -1: Your guess is higher than the number I picked (i.e. num > pick).
        1: Your guess is lower than the number I picked (i.e. num < pick).
        0: your guess is equal to the number I picked (i.e. num == pick).

    Return the number that I picked.
    """
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n
        while start < end:
            mid = (start + end) // 2
            cur = guess(mid)
            if cur == 0:
                return mid
            if cur == 1:
                end = mid - 1
            elif cur == -1:
                start = mid + 1
        return start
