from typing import Optional

## Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        slow = head.next

        if slow == None:
            return None

        fast = slow.next

        while ((fast != None) and (slow != None)) and fast != slow:
            fast = fast.next
            if fast != None:
                fast = fast.next
            slow = slow.next

        if fast == None or slow == None:
            return None
        
        new_slow = head
        
        while new_slow != slow:
            new_slow = new_slow.next
            slow = slow.next

        return new_slow