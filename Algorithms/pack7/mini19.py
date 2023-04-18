from typing import Optional, List, Any
from dataclasses import dataclass

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        h = self
        l = []
        while h:
            l.append(h.val)
            h = h.next

        return "[" + " ".join(map(str, l)) + "]"

class BinaryHeap:

    @dataclass
    class Node:
        key: int
        value: Any

    def __init__(self):
        self._list: List[BinaryHeap.Node] = []

    def _swap_nodes(self, ind1, ind2):
        self._list[ind1], self._list[ind2] =\
            self._list[ind2], self._list[ind1] 

    def get_min(self):
        return (
            self._list[0].value if self._list
            else None
        )
    
    def _get_parrent(self, ind: int) -> int:
        if ind == 0:
            return -1
        return (ind - 1) // 2
    
    ## TODO:
    def increase_key(self, ind: int, new_key: int):
        def max_ind(i):
            if len(self._list) < (2 * i) + 2:
                return -1

            if len(self._list)  == (2 * i) + 2:
                return 2 * i + 1

            left = self._list[(2 * i + 1)]
            right = self._list[(2 * i + 2)]
            
            return (
                (2 * i + 1) if left.key > right.key 
                else (2 * i + 2)
            )
        
        self._list[ind].key = new_key

        new_ind = ind
        child_ind = max_ind(new_ind)

        while ((child_ind != -1) and 
               (self._list[new_ind].key > self._list[child_ind].key)):
            self._swap_nodes(new_ind, child_ind)
            new_ind = child_ind
            child_ind = max_ind(new_ind)


    def decrease_key(self, ind: int, new_key: int):
        parr_ind = self._get_parrent(ind)

        self._list[ind].key = new_key

        while (parr_ind != -1) and (self._list[parr_ind].key > self._list[ind].key):
            self._swap_nodes(parr_ind, ind)
            ind = parr_ind
            parr_ind = self._get_parrent(parr_ind)

    def add(self, key, value):
        self._list.append(BinaryHeap.Node(key, value))
        self.decrease_key(len(self._list ) - 1, key)

    def pop(self):
        if len(self._list) == 0:
            return None

        if len(self._list) == 1:
            return self._list.pop().value

        res = self._list[0].value

        self._swap_nodes(0, len(self._list) - 1)
        self._list.pop()
        self.increase_key(0, self._list[0].key)

        return res


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        beap = BinaryHeap()

        for lst in lists:
            if lst:
                beap.add(lst.val, lst)

        curr_node = beap.get_min()

        res = ListNode(val=curr_node.val) 
        res_head = res
    

        while True:
            if curr_node.next is None:
                beap.pop()
            else:
                beap._list[0].value = curr_node.next
                beap.increase_key(
                    0, 
                    beap._list[0]
                        .value
                        .val
                )

            curr_node = beap.get_min()

            if curr_node is None:
                break

            res.next = ListNode(val=curr_node.val)
            res = res.next

        return res_head


s = Solution()

l1 = ListNode(val=1)
l1.next = ListNode(val=4)
l1.next.next = ListNode(val=5)


l2 = ListNode(val=1)
l2.next = ListNode(val=3)
l2.next.next = ListNode(val=4)

l3 = ListNode(val=6)
l3.next = ListNode(val=7)

print(s.mergeKLists([l1, l2, l3]))

