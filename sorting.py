from typing import List
from collections import defaultdict
import random


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


def bubble_sort(nums: List[int]) -> List[int]:
    """
    Check every adjacent pair and swap larger to back. Do until no swaps.

    Worst: O(n^2)
    Best: O(n) with O(1) swaps
    Avg: O(n^2)
    """
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    while True:
        swapped = False
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
                swapped = True
        if not swapped:
            break
    return nums


def quick_sort(nums: List[int]) -> List[int]:
    """
    Recursively partition the array, choose a pivot and move less/greater values before/after pivot.

    Divide and conquer algorithm.

    Worst: O(n^2)
    Best: O(n log n)
    Avg: O(n log n)
    """

    if len(nums) <= 1:
        return nums

    less = []
    equal = []
    greater = []
    pivot = 0
    for num in nums:
        if num < nums[pivot]:
            less.append(num)
        elif num == nums[pivot]:
            equal.append(num)
        else:
            greater.append(num)
    return quick_sort(less) + equal + quick_sort(greater)


def heap_sort(nums: List[int]) -> List[int]:
    """
    Binary heap is a complete binary tree where parent val is greater (max) or smaller (min) than values of its children.
    Array representation is parent at i with children 2*i + 1 and 2*i + 2.

    O(n log n)
    """
    nums = nums.copy()

    def heapify(i: int, nums: List[int]) -> List[int]:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(nums) and nums[left] > nums[largest]:
            largest = left
        if right < len(nums) and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(largest, nums)

    # Build a max heap.
    i = len(nums) // 2
    while i >= 0:
        heapify(i, nums)
        i -= 1

    print(nums)

    # Pop the root element and replace with last item Rebuild heap.
    result = []
    while nums:
        result.append(nums.pop(0))
        heapify(0, nums)

    return result[::-1]


tests = [
    [1, 12, 9, 5, 6, 10],
    [-1, -4, -2, 1000, 1231, 1, 4, 5, 6, 7],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [1],
    [3, 1],
]

for test in tests:
    # output = merge_sort(test)
    # output = radix_sort_with_buckets(test)
    # output = counting_sort(test)
    # output = insertion_sort(test)
    # output = selection_sort(test)
    # output = bubble_sort(test)
    # output = quick_sort(test)
    output = heap_sort(test)
    expected = sorted(test)
    print(output, expected)
    assert output == expected
