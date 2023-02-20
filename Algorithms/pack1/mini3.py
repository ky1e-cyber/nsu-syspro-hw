from typing import List

## https://leetcode.com/problems/binary-search/submissions/900835544/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_bound = -1
        right_bound = len(nums)
        while left_bound < right_bound - 1:
            pivot: int = (right_bound + left_bound) // 2

            if nums[pivot] == target:
                return pivot

            if nums[pivot] < target:
                left_bound = pivot
            else:
                right_bound = pivot
        
        return -1