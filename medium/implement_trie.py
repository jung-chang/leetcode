# https://leetcode.com/problems/implement-trie-prefix-tree/

from typing import Any, Optional, List


class Node:
    def __init__(self, val, end=False):
        self.val = val
        self.end = end
        self.letters = {}

    def add_child(self, node: Any):
        self.letters[node.val] = node

    def get_children(self) -> List[Any]:
        return self.letters.values()

    def get_child(self, val: str) -> Optional[Any]:
        return self.letters.get(val)

    def is_end(self) -> bool:
        return self.end

    def set_end(self, end) -> None:
        self.end = end


class Trie:
    """
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:

        Trie() Initializes the trie object.
        void insert(String word) Inserts the string word into the trie.
        boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
        boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

    """

    def __init__(self):
        self.roots = {}

    def insert(self, word: str) -> None:
        if not word:
            return
        if word[0] in self.roots:
            self._create_partial_word(word)
        else:
            root = Node(word[0])
            self.roots[word[0]] = root
            self._add_letters(root, word[1:])

    def search(self, word: str) -> bool:
        node = self._search(word)
        if not node:
            return False
        return node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node = self._search(prefix)
        return bool(node)

    def _search(self, word: str) -> Optional[Node]:
        """
        Returns last node found.
        """
        if not word:
            return None
        node = self.roots.get(word[0])
        if not node:
            return None
        for letter in word[1:]:
            child = node.get_child(letter)
            if not child:
                return None
            node = child
        return node

    def _add_letters(self, node: Node, letters: str) -> Node:
        prev = node
        for letter in letters:
            node = Node(letter)
            if prev:
                prev.add_child(node)
            prev = node
        prev.set_end(True)

    def _create_partial_word(self, word: str) -> None:
        node = self.roots[word[0]]
        i = 1
        while i < len(word):
            child = node.get_child(word[i])
            if not child:
                break
            node = child
            i += 1
        # print(node, word[1:])
        self._add_letters(node, word[i:])

    def get_words(self) -> List[str]:
        if not self.roots:
            return []
        words = []

        queue = [[node] for node in self.roots.values()]
        while queue:
            nodes = queue.pop(0)
            if nodes[-1].is_end():
                words.append("".join([node.val for node in nodes]))
            for child in nodes[-1].get_children():
                queue.append(nodes + [child])
        return words


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("a")
obj.insert("ap")
obj.insert("app")

print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
print(obj.startsWith("bp"))

print(obj.get_words())
