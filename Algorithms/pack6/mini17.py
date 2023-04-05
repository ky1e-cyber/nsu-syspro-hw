from typing import Optional, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_slice(slice_len) -> Tuple[ListNode, ListNode]:
            nonlocal curr
            new_tail = curr
            buff = None
            for _ in range(slice_len - 1):
                buff = curr
                curr = curr.next
                curr.next = buff

            new_head = curr
            curr = curr.next
            return new_head, new_tail 

        curr = head

        for _ in range(left - 2):
            curr = curr.next
        
        prev = curr
        curr = curr.next

        new_head, new_tail = reverse_slice(right - left + 1)
        
        prev.next = new_head
        new_tail.next = curr

        return head