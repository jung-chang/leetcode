# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List, Dict


class Solution:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Questions
            - How do we want to group the anagrams?
            - Can strs contain empty strings?
            - How long is the max string length?
            - Are there any techinical constraints?
            - What is the output that we want?

        Examples
            - Input: strs = ["eat","tea","tan","ate","nat","bat"]
            - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Notes
            - Group strings together that are anagrams of each other. eat=tea=ate, bat=atb...
            - How do we identify if 2 strings are anagrams?
            - are_anagrams(a,b) -> bool: O(a+b)
            - for every pair of strings in strs -> are_anagrams(pair)
            - sort the string and check equality
            - How to categorize anagrams

        Solution
            - Iterate through strs, count number of letters, compare with other strs.

        Time:
        """

        # Test 1: [abc, def, ghi, bac, fed, ihg]
        # abc: key=a1b1c1 -> {a1b1c1: [abc]}
        # def: key=d1e1f1 -> {d1e1f1: [def]}
        # bac: key=a1b1c1 -> {a1b1c1: [abc, bac]}

        # Test 2 get_letter_dict_key(abc)
        # letter_dict = {a:1,b:1,c:1}
        # keys=[a,b,c] -> key=a1b1c1

        # Test 3 empty strings
        # key="", key_to_strings = {"": ["", "", ""]}

        # abc = bac = bca
        def get_letter_dict_key(string) -> str:
            """ate -> a1e1t1  letter followed by occurence"""
            letter_dict = get_letter_dict(string)
            key = ""
            for letter in sorted(letter_dict.keys()):
                key += f"{letter}{letter_dict[letter]}"
            return key

        def get_letter_dict(string) -> Dict[str, int]:
            """ate -> a1e1t1  letter followed by occurence"""
            letter_dict = defaultdict(lambda: 0)
            for letter in string:
                letter_dict[letter] += 1
            return letter_dict

        key_to_strings = defaultdict(list)
        for string in strs:
            key = get_letter_dict_key(string)
            key_to_strings[key].append(string)

        return [strings for strings in key_to_strings.values()]

    def second(self, strs: List[str]) -> List[List[str]]:
        """
        Iterate through strs, create dict of unique anagrams, with list as values and compare.

        Time limit exceeded.
        """

        # Test 1: [abc, def, bac, fed]
        # string_to_anagrams={abc: [abc, bac], def: [def]}
        #

        # O(string)
        string_to_letter_dict = {}

        def get_letter_dict(string) -> Dict[str, int]:
            """ate -> a1e1t1  letter followed by occurence"""
            letter_dict = defaultdict(lambda: 0)
            for letter in string:
                letter_dict[letter] += 1
            return letter_dict

        # O(a+b)
        def are_anagrams(a, b) -> bool:
            if string_to_letter_dict.get(a):
                dict_a = string_to_letter_dict[a]
            else:
                dict_a = get_letter_dict(a)
                string_to_letter_dict[a] = dict_a

            if string_to_letter_dict.get(b):
                dict_b = string_to_letter_dict[b]
            else:
                dict_b = get_letter_dict(b)
                string_to_letter_dict[b] = dict_b
            return dict_a == dict_b

        if not strs:
            return [[""]]
        string_to_anagrams = defaultdict(list)  # {abc: [abc]}
        # O(n * n)
        for i in range(len(strs)):
            found_anagram = False
            for key in list(string_to_anagrams.keys()):
                if are_anagrams(key, strs[i]):
                    string_to_anagrams[key].append(strs[i])
                    found_anagram = True
                    break
            if not found_anagram:
                string_to_anagrams[strs[i]].append(strs[i])

        return [strings for strings in string_to_anagrams.values()]


# O(n * mlogm) = O(n*m) where n is len(strs) and m is average length of word
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().second(["eat", "tea", "tan", "ate", "nat", "bat"]))
