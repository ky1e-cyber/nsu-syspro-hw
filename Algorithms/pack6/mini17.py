from typing import Optional, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if head.next == None:
            return head

        def reverse_slice(slice_len) -> Tuple[ListNode, ListNode]:
            nonlocal curr
            new_tail = curr
            buff = None
            nxt = curr.next
            for _ in range(slice_len - 1):
                buff = curr
                curr = nxt

                nxt = curr.next
                curr.next = buff

            new_head = curr
            curr = nxt
            return new_head, new_tail 

        curr = head

        for _ in range(left - 2):
            curr = curr.next
        
        prev = None
        if left != 1:
            prev = curr
            curr = curr.next

        new_head, new_tail = reverse_slice(right - left + 1)
        
        new_tail.next = curr

        if prev:
            prev.next = new_head
        else:
            head = new_head

        return head
