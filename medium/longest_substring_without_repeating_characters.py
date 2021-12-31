# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """

    def first(self, s: str) -> int:
        """
        Use a sliding window from first unique character, pop front if repeated.

        Time: O(n)
        Space: O(2 * length) for set and queue
        """
        # sdveavf
        # dvdf
        length = 0
        if not s:
            return length
        queue = []
        visited = set()
        for letter in s:
            if letter in visited:
                length = max(length, len(queue))
                while queue and queue[0] != letter:
                    queue.pop(0)
                queue.pop(0)
                queue.append(letter)
                visited = set(queue)
            else:
                queue.append(letter)
                visited.add(letter)
        return max(length, len(queue))


# print(Solution().first("abcabcbb"))
# print(Solution().first("bbbb"))
# print(Solution().first("pwwkew"))
print(Solution().first("dvdf"))
