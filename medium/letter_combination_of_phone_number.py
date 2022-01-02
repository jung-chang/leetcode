# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    """
    Given a string containing digits from 2-9 inclusive,
    return all possible letter combinations that the number could represent.
    Return the answer in any order.

    1 2abc 3def
    4ghi 5jkl 6mno
    7pqrs 8tuv 9wxyz
    """

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Back trace forming new suffixes and adding the new letter.

        # 223 -> abc abc def
        # abc -> abc -> d, e, f
        # abc -> ad, ae, af, bd, be, bf, cd ce cf
        """
        num_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        results = []
        for digit in reversed(digits):
            if not results:
                results.extend([letter for letter in num_to_letters[digit]])
            else:
                new_results = []
                for new_letter in num_to_letters[digit]:
                    for suffix in results:
                        new_results.append(new_letter + suffix)
                results = new_results
        return results


print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("2"))
print(Solution().letterCombinations(""))
print(Solution().letterCombinations("22"))
