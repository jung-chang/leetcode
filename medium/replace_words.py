# https://leetcode.com/problems/replace-words/

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for letter in word:
            node = node.children.setdefault(letter, TrieNode())
        node.end = True

    def get_shorted_prefix(self, word: str) -> str:
        def dfs(i: int, node: TrieNode):
            if i == len(word):
                return i
            if node.end:
                return i
            for letter, child in node.children.items():
                if letter == word[i]:
                    return dfs(i + 1, child)

        i = dfs(0, self.root)
        print(word, word[:i])
        return word[:i]


class Solution:
    """
    In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor.
    For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

    Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it.
    If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

    Return the sentence after the replacement.
    """

    def triesecond(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split(" ")
        for i in range(len(words)):
            root = trie.get_shorted_prefix(words[i])
            words[i] = root
        return " ".join(words)

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        Check prefix of seach string in sentence and see if it can be replaced by a word in the dictionary.

        Solution
            - Brute force = O(words in sentence * words in dictionary)
            - Possibly use a Trie to check prefixes O(words in sentence * length of matching prefix)
        """

        dictionary_set = set(dictionary)

        def get_root(successor: str) -> str:
            for i in range(1, len(successor)):
                if successor[:i] in dictionary_set:
                    return successor[:i]
            return successor

        words = sentence.split(" ")
        for i in range(len(words)):
            successor = words[i]
            root = get_root(successor)
            if root:
                words[i] = root
        return " ".join(words)


d = ["cat", "bat", "rat"]
s = "the cattle was rattled by the battery"

# d = ["a", "b", "c"]
# s = "aadsfasf absbs bbab cadsfafs"

print(Solution().triesecond(d, s))
