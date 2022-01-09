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
        https://leetcode.com/problems/decode-ways/discuss/1674198/Python-Dynamic-Programming-with-process.-Time%3A-O(n)-Space%3A-O(n)
        """
        if not s:
            return 0
        if s[0] == "0":
            return 0
        ways = [0] * (len(s) + 1)
        ways[0] = 1
        ways[1] = 1
        i = 2
        while i < len(s) + 1:
            # If s[i-1] + s[i] is [10,26]
            if 10 <= int(s[i - 2 : i]) <= 26:
                ways[i] += ways[i - 2]
            # If s[i] is [1,9]
            if 1 <= int(s[i - 1]) <= 9:
                ways[i] += ways[i - 1]
            i += 1
        print(ways)
        return max(1, ways[-1])

        # 1 1 2 2


# print(Solution().numDecodings("1012320"))
# print(Solution().second("12"))
# print(Solution().second("226"))  # 2 2 6, 22 6, 2 26

# 1120 -> [1 1 20], [11 20]
# 1020 -> [10 20]
# print(Solution().second("1120"))
# print(Solution().second("1020"))

print(Solution().second("1123"))  # 1 1 2 3, 11 2 3, 1 12 3, 1 1 23, 11 23
