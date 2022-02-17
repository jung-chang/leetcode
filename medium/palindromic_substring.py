# https://leetcode.com/problems/palindromic-substrings/


from itertools import count


class Solution:
    """
    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome w  hen it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.
    """

    def countSubstrings(self, s: str) -> int:
        """
        Go through all substrings and check if they are palindromes. O(n^2)

        Cases
        - single letters e.g 'a'
        - double letters with same letter e.g 'aa'
        - more if forward == backward e.g 'aba', 'abba', 'abbba'

        dp[i][j] = 1 if s[i:j+1] is a palindrome.

        Go in reverse to have correct dp ordering.
        """
        if not s:
            return 0

        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1

        print(dp)

        # xabbbax
        for i in reversed(range(length)):
            for j in range(i, length):
                print(i, j, s[i : j + 1])
                if i == j:
                    if i + 1 < length and s[i] == s[i + 1]:
                        dp[i][i + 1] = 1
                        # l, r = check_sides(i, i + 1)

                    if i - 1 >= 0 and s[i] == s[i - 1]:
                        dp[i - 1][i] = 1
                    continue
                l = i + 1
                r = j - 1
                if l >= length or r < 0 or l > r:
                    continue
                print("qwe", i, j, l, r)
                if dp[l][r] and s[i] == s[j]:
                    print("add", s[i : j + 1], s[l : r + 1])
                    dp[i][j] = 1
        # print(dp)

        temp = []
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j]:
                    temp.append(s[i : j + 1])
        print(temp)
        return sum([row.count(1) for row in dp])


print(Solution().countSubstrings("abbabba"))
# abba, bb, bab, aba
