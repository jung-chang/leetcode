# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. 
    No two characters may map to the same character, but a character may map to itself.
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        def encode(string: str) -> str:
            letter_map = {}
            i = 0
            result = []
            for letter in string:
                if letter in letter_map:
                    result.append(letter_map[letter])
                else:
                    letter_map[letter] = i
                    result.append(letter_map[letter])
                    i += 1
            return result
        print(encode(s), encode(t))
        return encode(s) == encode(t)


s="abcdefghijklmnopqrstuvwxyzva"
t="abcdefghijklmnopqrstuvwxyzck"
print(Solution().isIsomorphic(s, t))