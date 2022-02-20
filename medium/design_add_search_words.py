# https://leetcode.com/problems/design-add-and-search-words-data-structure/

from collections import defaultdict


class Node:
    def __init__(self, end=False):
        self.children = {}
        self.end = end

    def add_child(self, val):
        node = Node()
        self.children[val] = node
        return node

    def has(self, val):
        return val in self.children

    def get_child(self, val):
        return self.children[val]


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word: str):
        if not word:
            return
        node = self.root
        for letter in word:
            if node.has(letter):
                node = node.get_child(letter)
            else:
                node = node.add_child(letter)
        node.end = True

    def search(self, word):
        # def dfs(node, i):
        #     if i == len(word):
        #         return node.end
        #     if word[i] == ".":
        #         for child in node.children.values():
        #             if dfs(child, i + 1):
        #                 return True
        #     if node.has(word[i]):
        #         return dfs(node.get_child(word[i]), i + 1)
        #     return False

        # return dfs(self.root, 0)

        stack = [(self.root, word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.end:
                    return True
            elif w[0] == ".":
                for child in node.children.values():
                    stack.append((child, w[1:]))
            else:
                if w[0] in node.children:
                    stack.append((node.children[w[0]], w[1:]))
        return False


class WordDictionary:
    """
    Design a data structure that supports adding new words and finding if a string matches any previously added string.
    """

    def __init__(self):
        """
        Use a trie to store words.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds word to the data structure, it can be matched later.
        """
        self.trie.add_word(word)

    def search(self, word: str) -> bool:
        """
        Returns true if there is any string in the data structure that matches word or false otherwise.
        *Word may contain dots '.' where dots can be matched with any letter.
        """
        return self.trie.search(word)


class WordDictionaryWrong:
    """
    Design a data structure that supports adding new words and finding if a string matches any previously added string.
    """

    def __init__(self):
        """
        Use a trie to store words.
        """
        # Nested dictionary representing a Trie
        # {"a": {"p": {"p": "l": {"e": {"end": True}}}}}
        self.trie = defaultdict(dict)

    def addWord(self, word: str) -> None:
        """
        Adds word to the data structure, it can be matched later.
        """
        if not word:
            return
        self._add_word(word)

    def _add_word(self, word: str):
        container = self.trie
        for letter in word:
            if letter in container:
                container = container[letter]
            else:
                next_level = {}
                container[letter] = next_level
                container = next_level
        container["end"] = {}

    def search(self, word: str) -> bool:
        """
        Returns true if there is any string in the data structure that matches word or false otherwise.
        *Word may contain dots '.' where dots can be matched with any letter.
        """
        if not word:
            return False
        stack = [(word, self.trie)]
        while stack:
            substring, container = stack.pop()
            # print("pop", substring, container)
            if not substring:
                return "end" in container
            if substring[0] == ".":
                for key, next_container in container.items():
                    if key == "end":
                        continue
                    # print(len(substring[1:]), substring[1:], next_container)
                    stack.append((substring[1:], next_container))
            elif substring[0] in container:
                stack.append((substring[1:], container[substring[0]]))
        return False

    def all_words(self):
        words = []
        stack = [(key, container) for key, container in self.trie.items()]
        while stack:
            substring, container = stack.pop()
            if "end" in container:
                words.append(substring)
            for letter, next_container in container.items():
                stack.append((substring + letter, next_container))
        return words


# temp = WordDictionary()
# for i, action in enumerate(actions):
#     if action == "addWord":
#         result = results[i][0]
#         print("add", result, end=" -> ")
#         temp.addWord(result)
#         print(temp.all_words())
#     elif action == "search":
#         result = results[i][0]
#         print("search", result, temp.search(result))


temp = WordDictionary()
for word in ["bat", "add", "an", "and", "at"]:
    temp.addWord(word)
# print(temp.trie.all_words())

print(temp.search("bat"))
print(temp.search(".at"))
print(temp.search("b.t"))
print(temp.search("ba."))
print(temp.search(".a."))
