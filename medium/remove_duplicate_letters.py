# https://leetcode.com/problems/remove-duplicate-letters/


from collections import defaultdict
from typing import List


class Solution:
    """
    Given a string s, remove duplicate letters so that every letter appears once and only once.
    You must make sure your result is the smallest in lexicographical order among all possible results.
    """

    def removeDuplicateLetters(self, s: str) -> str:
        """
        Keep last occurence of each letter.
        Use stack and add one by one, checking for lexicogrpahic order

        """
        last_i = {letter: i for i, letter in enumerate(s)}
        visited = set()
        stack = []

        for i in range(len(s)):
            symbol = s[i]
            if not stack:
                visited.add(symbol)
                stack.append(symbol)
                continue
            if symbol in visited:
                continue

            # cacbc
            while stack and symbol < stack[-1] and last_i[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(symbol)
            visited.add(symbol)
        return "".join(stack)

    def first(self, s: str) -> str:
        """
        Smallest lexicographically -> figure out which duplicates to remove

        cabc -> abc or cab

        Solutions
            - Iterate string, find duplicates, for each duplicate find the best one to keep
            - Do a search for smallest result string, each step with removed duplicates

        Cases

        cacbc -> cab, acb, abc -> keep last c
        abaca -> abc, bac, bca -> keep first a

        """

        def get_substrings(string: str, letter: str) -> List[str]:
            substrings = set()
            letter_indices = [i for i, let in enumerate(string) if let == letter]
            # print(string, letter, letter_indices)
            for i in letter_indices:
                substring = ""
                for j in range(len(string)):
                    if j == i:
                        substring += string[j]
                    if j not in letter_indices:
                        substring += string[j]
                substrings.add(substring)
            return list(substrings)

        if len(s) <= 1:
            return s

        letter_to_i = defaultdict(list)
        for i, letter in enumerate(s):
            letter_to_i[letter].append(i)
        duplicates = set(
            [letter for letter, indices in letter_to_i.items() if len(indices) > 1]
        )

        substring_cache = {}

        smallest = s
        stack = [(s, [])]
        while stack:
            cur_str, removed = stack.pop()
            has_duplicate = False
            for letter in cur_str:
                if letter in removed:
                    continue
                if letter in duplicates:
                    has_duplicate = True
                    key = f"{cur_str} {letter}"
                    if key in substring_cache:
                        substrings = substring_cache[key]
                    else:
                        substrings = get_substrings(cur_str, letter)
                        substring_cache[key] = substrings
                    for substring in substrings:
                        stack.append((substring, removed + [letter]))
            if not has_duplicate:
                if len(cur_str) < len(smallest):
                    smallest = cur_str
                else:
                    smallest = min(smallest, cur_str)
        return smallest


print(Solution().removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))
