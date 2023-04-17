from collections import namedtuple
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BinaryHeap:

    Node = namedtuple("Node", ["key", "value"])

    def __init__(self):
        self._list: List[BinaryHeap.Node] = []

    def _swap_nodes(self, ind1, ind2):
        self._list[ind1], self._list[ind2] =\
            self._list[ind2], self._list[ind1] 

    def get_min(self):
        return self._list[0].value
    
    def _get_parrent(self, ind: int) -> int:
        if ind == 0:
            return -1
        return (ind - 1) // 2
    
    def _increase_key(self, ind: int, new_key: int):
        def max_ind(i):
            if len(self._list) < (2 * i):
                return -1

            if len(self._list) == (2 * i):
                return (2 * i)

            left = self._list[(2 * i + 1)]
            right = self._list[(2 * i + 2)]
            
            return (
                (2 * i + 1) if left.key > right.key 
                else (2 * i + 1)
            )
        
        self._list[ind].key = new_key

        new_ind = ind
        child_ind = max_ind(new_ind)

        while ((child_ind != -1) and 
               (self._list[new_ind].key > self._list[child_ind].key)):
            self._swap_nodes(new_ind, child_ind)
            new_ind = child_ind
            child_ind = max_ind(new_ind)


    def _decrease_key(self, ind: int, new_key: int):
        parr_ind = self._get_parrent(ind)

        self._list[ind].key = new_key

        while (parr_ind != -1) and (self._list[parr_ind].key > self._list[ind].key):
            self._swap_nodes(parr_ind, ind)
            ind = parr_ind
            parr_ind = self._get_parrent(parr_ind)

    def add(self, key, value):
        self._list.append(BinaryHeap.Node(key, value))
        self._decrease_key(len(self._list ) - 1, key)

    def pop(self):

        if len(self._list) == 0:
            return None

        res = self._list[0].value

        self._swap_nodes(0, len(self._list) - 1)
        self._list.pop()
        self._increase_key(0, self._list[0].key)

        return res
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        beap = BinaryHeap()

        for lst in lists:
            if lst:
                beap.add(lst.val, lst)
        
        nxt_node = beap.get_min()

        while 


