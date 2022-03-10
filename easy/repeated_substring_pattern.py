# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    """
    Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Examples
            - abab
            - ababab
            - abcabc
        """

        for i in range(1, len(s)):
            substring = s[:i]
            multiplier = len(s) // len(substring)
            if substring * multiplier == s:
                return True
        return False


print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("ababab"))
print(Solution().repeatedSubstringPattern("abababab"))
print(Solution().repeatedSubstringPattern("ababababc"))
        