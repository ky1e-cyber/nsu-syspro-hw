import random as rng
from typing import List


def quicksort(nums: List[int], l: int, r: int) -> None:
    if (r - l) <= 0:
        return
    if ((l + 1) == r):
        if nums[l] > nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
        return
    pivot = rng.randint(l, r)
            

class Solution:
    

    def sortArray(self, nums: List[int]) -> List[int]:
        pass