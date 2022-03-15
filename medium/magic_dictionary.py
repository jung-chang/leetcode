# https://leetcode.com/problems/implement-magic-dictionary/

from collections import defaultdict
from typing import List, Dict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = True

    def search(self, word):
        def dfs(node, i, diffs):
            if i == len(word):
                return node.end_node and diffs == 1
            if diffs > 1:
                return False

            found = False
            for child in node.children:
                new_diffs = diffs + 1 if child != word[i] else diffs
                found = found or dfs(node.children[child], i + 1, new_diffs)
            return found

        return dfs(self.root, 0, 0)


class MagicDictionary:
    """
    Design a data structure that is initialized with a list of different words.

    Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.
    """

    def __init__(self):
        self.length_to_words = defaultdict(list)
        self.trie = Trie()

    def _matching_words(self, worda: str, wordb: str) -> bool:
        i = 0
        diffs = 0
        while i < len(worda):
            if worda[i] != wordb[i]:
                diffs += 1
            i += 1
        return diffs == 1

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            # self.length_to_words[len(word)].append(word)
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        # for word in self.length_to_words[len(searchWord)]:
        #     if self._matching_words(searchWord, word):
        #         return True
        # return False
        return self.trie.search(searchWord)


# Your MagicDictionary object will be instantiated and called as such:
magic = MagicDictionary()
dictionary = ["hello", "hallo", "leetcode"]
magic.buildDict(dictionary)
print(magic.search("hello"))
print(magic.search("hhllo"))
print(magic.search("hhhlo"))
print(magic.search("hllo"))
