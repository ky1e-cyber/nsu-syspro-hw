from typing import Dict, Optional
from collections import deque

class FreqStack:
    def __init__(self):
        ## (elem) -> freq
        self.freq: Dict[int, int] = dict()
        ## (freq) -> stack
        self.table: Dict[int, deque] = dict()
        self.max_freq = 0

    def push(self, val: int) -> None:

        frq: Optional[int] = self.freq.get(val)

        self.freq[val], frq = \
            ((1 if frq is None else frq + 1),) * 2

        self.max_freq = max(frq, self.max_freq)

        stack = self.table.get(frq)

        if stack is None:
            self.table[frq] = deque((val,))
        else:
            stack.append(val)


    def pop(self) -> int:
        el = self.table[self.max_freq].pop()
        self.freq[el] -= 1

        while self.max_freq != 0 and (not self.table[self.max_freq]):
            self.max_freq -= 1
        
        return el


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()