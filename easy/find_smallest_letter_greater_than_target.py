# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List

class Solution:
    """
    Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

    Note that the letters wrap around.

    For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

    [c f g] t= a

    """
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        def search(low: int, hi: int):
            if low > hi:
                return
            mid = (hi + low) // 2

            if letters[mid] == target:
                return search(mid + 1, hi)
            if target < letters[mid]:
                return search(low, mid - 1)
            elif target > letters[mid]:
                return search(mid + 1, hi)