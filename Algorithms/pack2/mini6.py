from typing import List, Iterator

## https://leetcode.com/problems/wiggle-sort-ii/submissions/901549106/

class Solution:
    def shell_sort(self, arr: List[int]) -> List[int]:
        def k_sort_inplace(arr: List[int], k: int):
            for i in range(k, len(arr)):
                j = i
                while (j - k >= 0) and (arr[j - k] > arr[j]):
                    arr[j - k], arr[j] = arr[j], arr[j - k]
                    j -= k

        arr = arr.copy()
        seq = [701, 301, 132, 57, 23, 10, 4, 1]

        for k in seq:
            k_sort_inplace(arr, k)

        return arr

    def wiggleSort(self, nums: List[int]) -> None:
        sorted_nums = self.shell_sort(nums)

        l_nums = len(nums)

        inds: Iterator[int] = range(0, l_nums, 2)
        inds_left: Iterator[int] = reversed(range(l_nums // 2 + l_nums % 2))
        inds_right: Iterator[int] = reversed(range(l_nums // 2 + l_nums % 2, l_nums))

        for ind, ind_left, ind_right in zip(inds, inds_left, inds_right):
            nums[ind] = sorted_nums[ind_left]
            nums[ind + 1] = sorted_nums[ind_right]
        
        if l_nums % 2 != 0:
            nums[-1] = sorted_nums[0]
