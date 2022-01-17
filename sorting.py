from typing import List
from collections import defaultdict


def merge_sort(nums: List[int]) -> List[int]:
    """
    Divides list into halves, sorts each half and then merge them when they bubble.
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


def radix_sort_with_buckets(nums: List[int]) -> List[int]:
    """
    Looks at each numbers digits starting from least significant, buckets and sorts them.

    Treat negative sign as own bucket.
    """
    if not nums:
        return nums
    buckets = defaultdict(list)
    max_num = max(nums)
    factor = 1
    while True:
        for num in nums:
            digit = num // factor % 10
            buckets[digit * (-1 if num < 0 else 1)].append(num)
        nums = []
        for key in sorted(buckets.keys()):
            nums.extend(buckets[key])
        buckets.clear()
        factor *= 10
        if factor > max_num:
            break
    # Reverse negative part
    i = 0
    while i < len(nums) and nums[i] < 0:
        i += 1
    return list(reversed(nums[:i])) + nums[i:]


def radix_sort(nums: List[int]) -> List[int]:
    """
    This uses counting sort.
    """
    pass


def counting_sort(nums: List[int]) -> List[int]:
    """
    Create a histogram by counting each number and incrementing the index.

    Expect nums to be non negative integers.
    """
    # Create the histogram
    counts = [0] * (max(nums) + 1)
    for num in nums:
        counts[num] += 1

    # Sum counts[i] = counts[i] + counts[i-1]
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    result = [0] * (len(nums) + 1)
    for num in nums:
        result[counts[num]] = num
        counts[num] -= 1
    return result[1:]


def insertion_sort(nums: List[int]) -> List[int]:
    """
    Iterate and bubble up each number to its correct position.
    """
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    sorted_i = 0
    while sorted_i < len(nums) - 1:
        i = sorted_i + 1
        while i > 0 and nums[i] < nums[i - 1]:
            temp = nums[i - 1]
            nums[i - 1] = nums[i]
            nums[i] = temp
            i -= 1
        sorted_i += 1
    return nums


def selection_sort(nums: List[int]) -> List[int]:
    """
    Move the minimum element to end of sorted index.

    O(n^2)
    """
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    sorted_i = -1
    while sorted_i < len(nums) - 1:
        min_i = sorted_i + 1
        for i in range(min_i + 1, len(nums)):
            if nums[i] < nums[min_i]:
                min_i = i
        temp = nums[sorted_i + 1]
        nums[sorted_i + 1] = nums[min_i]
        nums[min_i] = temp
        sorted_i += 1
    return nums


tests = [
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [1],
    [3, 1],
    [-1, -4, -2, 1000, 1231, 1, 4, 5, 6, 7],
]

for test in tests:
    # output = merge_sort(test)
    # output = radix_sort_with_buckets(test)
    # output = counting_sort(test)
    # output = insertion_sort(test)
    output = selection_sort(test)
    expected = sorted(test)
    print(output, expected)
    assert output == expected

# bubble sort
# quicksort
