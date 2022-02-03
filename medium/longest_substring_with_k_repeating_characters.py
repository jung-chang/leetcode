# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/


from collections import defaultdict
from timeit import repeat


class Solution:
    """
    Given a string s and an integer k, return the length of the longest substring of s
    such that the frequency of each character in this substring is greater than or equal to k.
    """

    def longestSubstring(self, s: str, k: int) -> int:
        """
        Divide and conquer.

        Divide string into substrings

        longestSubstring(string) = longestSubstring(string[:mid]) + longestSubstring(string[mid+1:])

        ababcabaaadc, k=2
        ababcabaaa d c
        abab c abaaa
        abab(4) c a b aaa(3)
        """

        def helper(string: str) -> int:
            nonlocal s
            nonlocal k

            if not string:
                return 0

            letter_count = defaultdict(lambda: 0)
            for letter in string:
                letter_count[letter] += 1

            for i, letter in enumerate(string):
                if letter_count[letter] < k:
                    print(string[:i], string[i + 1 :])
                    return max(helper(string[:i]), helper(string[i + 1 :]))
            return len(string)

        if not s or len(s) < k:
            return 0
        return helper(s)

    def wrong(self, s: str, k: int) -> int:
        """
        aaaaaaaaaaaa b cdefghijklmnopqrstuvwzyz b

        aasdassdd k=3

        Tick off the repeating characters, then find the longest contiguous section

        ababbc, k=2
        -----c

        ababacb
        -----c-
        """

        def count_letters(string: str, k: int) -> int:
            """
            ababa -b-b-

            ababb -----
            """
            print("counter_letters", string)
            if not string:
                return 0
            letter_count = defaultdict(lambda: 0)
            for letter in string:
                letter_count[letter] += 1
            repeating_letters = set(
                [letter for letter, count in letter_count.items() if count >= k]
            )

            string = list(string)
            for i in range(len(string)):
                if string[i] in repeating_letters:
                    string[i] = "-"
            print(string)

            max_length = 0
            length = 0
            for i in range(len(string)):
                if string[i] == "-":
                    length += 1
                else:
                    max_length = max(max_length, length)
                    length = 0
            max_length = max(max_length, length)
            return max_length if max_length >= k else 0

        if not s:
            return 0
        if len(s) < k:
            return 0

        letter_count = defaultdict(lambda: 0)
        for letter in s:
            letter_count[letter] += 1
        repeating_letters = set(
            [letter for letter, count in letter_count.items() if count >= k]
        )

        start = 0
        end = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in repeating_letters:
                end = i
                continue
            else:
                if start == end:
                    continue
                end += 1
                max_length = max(max_length, count_letters(s[start:end], k))
                start = end
        print(start, end, s[start : end + 1])
        if end == len(s) - 1:
            max_length = max(max_length, count_letters(s[start : end + 1], k))
        return max_length

    def DFS(self, s: str, k: int) -> int:
        """
        s=asd k=1, sol=asd
        s=asd k=1, sol=
        s=aassd k=2, sol=aass
        s=asasd k=2, sol=asas
        s=dasasd k=2, sol=dasasd

        1. check every substring -> DFS
        Time exceeds
        """

        def get_length(string: str, k: int) -> bool:
            letter_count = defaultdict(lambda: 0)
            for letter in string:
                letter_count[letter] += 1

            for count in letter_count.values():
                if count < k:
                    return 0
            return len(string)

        if not s:
            return 0
        # (letter, i)
        max_length = 0
        queue = [(s[i], i) for i in range(len(s))]
        while queue:
            string, i = queue.pop(0)
            max_length = max(max_length, get_length(string, k))
            if i + 1 < len(s):
                queue.append((string + s[i + 1], i + 1))
        return max_length


s = "ababcabaaadc"
k = 2


print(Solution().longestSubstring(s, k))
