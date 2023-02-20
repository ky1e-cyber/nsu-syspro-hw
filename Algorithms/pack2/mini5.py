from typing import List

## https://leetcode.com/problems/h-index/submissions/901549912/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def shell_sort(arr: List[int]) -> List[int]:
            def k_sort_inplace(arr: List[int], k: int):
                for i in range(k, len(arr)):
                    j = i
                    while (j - k >= 0) and (arr[j - k] < arr[j]):
                        arr[j - k], arr[j] = arr[j], arr[j - k]
                        j -= k

            arr = arr.copy()
            seq = [701, 301, 132, 57, 23, 10, 4, 1]

            for k in seq:
                k_sort_inplace(arr, k)
            return arr

        citations = shell_sort(citations)
        
        h_ind = 0

        for i, cit in enumerate(citations, start=1):
            if i <= cit:
                h_ind = i
        
        return h_ind

