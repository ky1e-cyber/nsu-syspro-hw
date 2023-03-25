import random as rng
from typing import List

def swap(xs: List, ind1: int, ind2: int) -> None:
    xs[ind1], xs[ind2] = \
        xs[ind2], xs[ind1]

def quicksort(nums: List[int], l: int, r: int) -> None:
    if (r - l) <= 0:
        return
    if ((l + 1) == r):
        if nums[l] > nums[r]:
            swap(nums, l, r)
        return

    pivot = rng.randint(l, r)
    swap(nums, pivot, l)
    i = l + 1

    for j in range(l + 1, r + 1):
        if nums[j] <= nums[l]:
            swap(nums, i, j)
            i += 1

    swap(nums, l, i - 1)
    quicksort(nums, i, r)
    quicksort(nums, l, i - 2)

    return

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quicksort(nums, 0, len(nums) - 1)
        return nums
