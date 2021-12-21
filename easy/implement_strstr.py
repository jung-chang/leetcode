# https://leetcode.com/problems/implement-strstr/


class Solution:
    """
    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    """

    def first(self, haystack: str, needle: str) -> int:
        # aaa
        # a
        def matches(short: str, longer: str) -> bool:
            if len(short) > len(longer):
                return False
            return short == longer[: len(short)]

        if not needle:
            return 0
        index = -1
        if len(needle) > len(haystack):
            return index
        for hi, h in enumerate(haystack):
            if h == needle[0]:
                if len(needle) > len(haystack[hi:]):
                    return index
                elif matches(needle, haystack[hi:]):
                    return hi
        return index


print(Solution().first("abcd", "cd"))
print(Solution().first("aaaa", "aaa"))
print(Solution().first("mississippi", "issipi"))
