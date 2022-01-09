# https://leetcode.com/problems/decode-ways/


class Solution:
    """
    Given a sequence of numbers, return the number of ways to decode it.

    A: 1
    B: 2
    ...
    Z: 26

    Therefore 11106 -> 1 1 10 6, 11 10 6

    Questions
        How long is s?
        Will there be invalid inputs?
        Technical constraints?

    Examples
        1. 112 -> 1 1 2, 11 2, 1 12
        2. 1011 -> 10 1 1, 10 11 -> zeroes can only be after 1 or 2

    Solution
        - BFS checking next one or two indices
    """

    def numDecodings(self, s: str) -> int:
        """
        time limit exceeded
        """
        if not s:
            return 0
        if s[0] == "0":
            return 0

        result = []
        queue = [([s[0]], s[1:])]
        while queue:
            way, string = queue.pop(0)
            print(way, string, queue)
            if not string:
                result.append(way)
                continue
            # Case [11] 1, [11] 0
            if len(way[-1]) > 1:
                if string[0] != "0":
                    queue.append((way + [string[0]], string[1:]))
            else:
                # Case [1] 0 and [2] 0
                if string[0] == "0" and way[-1][0] in ("1", "2"):
                    # print("1", way[: len(way) - 1] + [way[-1] + "0"], string[1:])
                    queue.append((way[: len(way) - 1] + [way[-1] + "0"], string[1:]))
                if string[0] != "0":
                    # Case [1] [1], [3] [1]
                    # print("2", way + [string[0]], string[1:])
                    queue.append((way + [string[0]], string[1:]))
                    new_decode = way[-1][0] + string[0]
                    # Case [11], [21], [26]
                    if 0 < int(new_decode) and int(new_decode) < 27:
                        # print("3", way[: len(way) - 1] + [new_decode], string[1:])
                        queue.append((way[: len(way) - 1] + [new_decode], string[1:]))
        print(result)
        return len(result)

    def second(self, s: str) -> int:
        """
        https://medium.com/tech-life-fun/leet-code-91-decode-ways-graphical-explained-python3-solution-60d97a0852c8

        If you start with [1,2] you get [1,2],[12]
        If you add [3] we can just decode [3] into "C" and have valid decodes [1,2] + [3], [12] + [3]
        However since 23 is a letter [1, 23] is valid -> it's one more way to decode on top of ways to decode at [1]

        Example
            Start [1,2,2] -> [1,2,2], [12,2], [1,22], i=2, dp=[1,2,3]
            Add [1] -> [1] can fit as is into the above 3 decode ways -> +3 ways
            [1] can also append to the previous [2] -> [21] -> [1,2,21] and [12, 21]. So it's every way before the prev [2] + [21] ways

            dp[i] = dp[i-1] + dp[i-2] if (1 <= s[i-2:i] <=26)

            What if there's a 0?
                1. Previous is 0
                    Do nothing since cant append 0. dp[i] = dp[i-1]
                2. s[i] is 0
                    if (1 <= s[i-2:i] <=26) -> dp[i] = dp[i-2]
        """
        if not s:
            return 0
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        # dp[i] = # ways to decode at s[i]
        dp = [1, 1]
        i = 1
        while i < len(s):
            ways = 0
            # Adding previous is a letter
            if s[i - 1] != "0" and 1 <= int(s[i - 1 : i + 1]) <= 26:
                ways += dp[-2]
            # Adding itself is a valid decode
            if s[i] != "0":
                ways += dp[-1]
            # If not decodable
            if not ways:
                return 0
            dp.append(ways)
            i += 1
        return dp[-1]

        # Test [1,2,2,1], dp=[1,2,0,0], i=2
        #


# print(Solution().numDecodings("1012320"))
# print(Solution().second("12"))
# print(Solution().second("226"))  # 2 2 6, 22 6, 2 26

# 1120 -> [1 1 20], [11 20]
# 1020 -> [10 20]
# print(Solution().second("1120"))
# print(Solution().second("1020"))

print(Solution().second("12"))  # [2 10 1]
