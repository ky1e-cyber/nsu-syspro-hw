from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(ind1: int, ind2: int) -> None:
            nums[ind1], nums[ind2] = \
                nums[ind2], nums[ind1]

        right_bound = len(nums) - 1
        left_bound = 0
        i = 0

        while i <= right_bound:
            if nums[i] == 2:
                swap(i, right_bound)
                right_bound -= 1
                continue
            elif nums[i] == 0:
                swap(i, left_bound)
                left_bound += 1
            i += 1
