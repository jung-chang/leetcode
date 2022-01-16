from typing import List
from collections import defaultdict


def merge_sort(nums: List[int]) -> List[int]:
    """
    Divices list into halves, sorts each half and then merge them when they bubble.
    """

    def merge(left: List[int], right: List[int]) -> List[int]:
        l = r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        if l < len(left):
            result.extend(left[l:])
        elif r <= len(right):
            result.extend(right[r:])
        return result

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def radix_sort(nums: List[int]) -> List[int]:
    """
    Looks at each numbers digits starting from least significant, buckets and sorts them.
    """
    if not nums:
        return nums
    buckets = defaultdict(list)
    max_num = max(nums)
    factor = 10
    while True:
        for num in nums:
            digit = num % factor
            buckets[digit].append(num)
        print(buckets)
        nums = []
        for key in sorted(buckets.keys()):
            nums.extend(buckets[key])
        buckets.clear()
        factor *= 10
        if factor > max_num:
            break
    return nums


tests = [
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [],
    [1],
    [3, 1],
    [-1, -4, -2, 1000, 1231, 1, 4, 5, 6, 7],
]

# for test in tests:
#     output = merge_sort(test)
#     expected = sorted(test)
#     print(output, expected)
#     assert output == expected

for test in tests:
    output = radix_sort(test)
    expected = sorted(test)
    print(output, expected)
    assert output == expected