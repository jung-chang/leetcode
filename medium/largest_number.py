# https://leetcode.com/problems/largest-number/

from typing import List
from collections import defaultdict
import functools


class Solution:
    """
    Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

    Since the result may be very large, so you need to return a string instead of an integer.
    """

    def largestNumber(self, nums: List[int]) -> str:
        """
        Cases
            - single digit 9 > 8 > ...0
            - mulyiple digits, 302, 9, 83, 9092 -> 9909283302, 9839092302

        Radix sort, shorter numbers take priority, 98, 988 -> 98988 or 98898

        Doesnt work with tricky numbers
            - [432, 43243]
            - [34323, 3432]
        """

        def to_digits(num: int) -> List[int]:
            if num < 10:
                return [num]
            digits = []
            while num:
                digits = [num % 10] + digits
                num //= 10
            return digits

        def radix_sort(nums: List[int]) -> List[int]:
            """
            This sorts by the most significant digit.
            """
            num_digits = [to_digits(num) for num in nums]
            max_index = max([len(digits) for digits in num_digits])
            index = -1
            while abs(index) <= max_index:
                buckets = defaultdict(list)
                for i in range(len(num_digits)):
                    num = num_digits[i]
                    if abs(index) > len(num):
                        buckets[num[-1]].append(num)
                        continue
                    digit = num[index]
                    buckets[digit].append(num)
                print(dict(buckets))
                index -= 1
                num_digits = []
                for key in sorted(buckets.keys(), reverse=True):
                    num_digits.extend(buckets[key])
                buckets.clear()
            print(list(num_digits))
            return num_digits

        if not nums:
            return ""
        if len(nums) == 1:
            return str(nums[0])

        result = ""
        for num in radix_sort(nums):
            num_string = ""
            for digit in num:
                num_string += str(digit)
            result += num_string
        return result

    def second(self, nums: List[int]) -> str:
        """
        For 2 intergers: a,b. Sort by a+b > b+a/
        If for integer c where b+c > c+b, then transitively a+c > c+a
        """

        def compare(a: str, b: str) -> bool:
            if a + b > b + a:
                return 1
            elif a + b < b + a:
                return -1
            else:
                return 0

        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        result = "".join(nums)
        if result[0] == "0":
            return "0"
        return result


print(Solution().second([10, 2]))  # 432 43 243, 43243 432
print()
print(Solution().second([34323, 3432]))
# [34323,3432]
# 3432 3 3432
# 3432 34323