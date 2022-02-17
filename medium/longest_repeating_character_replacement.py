# https://leetcode.com/problems/longest-repeating-character-replacement/


from collections import defaultdict


class Solution:
    """
    You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.
    """

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding window, calcualte replacement cost

        replacement cost = length of window - highest freq repeated char length
        if replacement cost <= k, increase substring
        otherwise shift window right, update counts dict

        BAAAB, k=2

        window_length > 5

        """
        max_length = max(1, k)
        counts = defaultdict(int)
        counts[s[0]] += 1
        l = 0

        for r in range(1, len(s)):
            counts[s[r]] += 1
            if r - l + 1 - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length

    def first(self, s: str, k: int) -> int:
        """
        Cases
        - k=0, find the longest substring
        - AABA k=1, replace B
        - AABAABAAA k=1, replace last B
        - ABCABC k=2
        - BAAAB, k=2
        - CBAAAB, k=2

        Which letters to change.
        Where to change the letters.
        """

        def crawl(s: str, k: int, start: int):
            letter = s[start]
            end = start
            while start > 0 and k:
                if s[start - 1] == letter:
                    start -= 1
                else:
                    k -= 1
                    start -= 1
            while end + 1 < len(s) and k:
                if s[end + 1] == letter:
                    end += 1
                else:
                    k -= 1
                    end += 1
            while start - 1 > 0 and s[start - 1] == letter:
                start -= 1
            while end + 1 < len(s) and s[end + 1] == letter:
                end += 1
            return (end + 1) - start

        if len(s) <= 1:
            return len(s)
        max_length = 1
        i = 0
        while i < len(s):
            if i == 0 or s[i] != s[i - 1]:
                length = crawl(s, k, i)
                max_length = max(max_length, length)
            i += 1
        return max_length


print(Solution().characterReplacement("AAAB", 1))
print(Solution().characterReplacement("BAAAB", 2))
print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("ABBB", 2))
