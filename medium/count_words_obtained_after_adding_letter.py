# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/


from collections import defaultdict
from typing import List, Dict


class Solution:
    """
    You are given two 0-indexed arrays of strings startWords and targetWords.
    Each string consists of lowercase English letters only.

    For each string in targetWords, check if it is possible to choose a string from startWords
    and perform a conversion operation on it to be equal to that from targetWords.

    Append any lowercase letter that is not present in the string to its end.
        For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'.
        If 'd' is added, the resulting string will be "abcd".

    Rearrange the letters of the new string in any arbitrary order.
        For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on.
        Note that it can also be rearranged to "abcd" itself.

    Return the number of strings in targetWords that can be obtained by performing the
    operations on any string of startWords.

    Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations.
    The strings in startWords do not actually change during this process.
    """

    def second(self, startWords: List[str], targetWords: List[str]) -> int:
        start_words = set()
        for word in startWords:
            start_words.add("".join(sorted(word)))

        count = 0
        targets = set()
        for target in targetWords:
            if target in targets:
                continue
            for i in range(len(target)):
                new_target = "".join(sorted(target[:i] + target[i + 1 :]))
                if new_target in start_words:
                    count += 1
                    break
        return count

    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        """
        Since we can rearrange the letters, we just need to validate if the frequencies of the letters are correct.
        Since we can only add letters not present in the string, each letter added can only occur max of 1 time.
        """

        def create_word_dict(word: str) -> Dict[str, int]:
            word_dict = defaultdict(int)
            for letter in word:
                word_dict[letter] += 1
            return word_dict

        word_to_dict = defaultdict(dict)
        target_to_count = defaultdict(int)
        length_to_start_word = defaultdict(list)
        word_to_letters = defaultdict(set)
        for word in startWords:
            word_to_dict[word] = create_word_dict(word)
            length_to_start_word[len(word)].append(word)
            word_to_letters[word] = set(word)
        for word in targetWords:
            word_to_dict[word] = create_word_dict(word)
            target_to_count[word] += 1
            word_to_letters[word] = set(word)

        targets = set()
        count = 0
        for target in targetWords:
            if target in targets:
                continue
            for word in length_to_start_word[len(target) - 1]:
                missing_letters = word_to_letters[target] - word_to_letters[word]
                if len(missing_letters) != 1:
                    continue
                letter = missing_letters.pop()
                if letter in word:
                    continue
                temp = word_to_dict[word].copy()
                temp[letter] = 1
                if temp != word_to_dict[target]:
                    continue
                count += target_to_count[target]
                targets.add(target)
                break
        return count


s = ["ant", "act", "tack"]
t = ["tack", "act", "acti"]

s = ["g", "vf", "ylpuk", "nyf", "gdj", "j", "fyqzg", "sizec"]
t = ["r", "am", "jg", "umhjo", "fov", "lujy", "b", "uz", "y"]

print(Solution().wordCount(s, t))
