from mini18 import LinkedList
from typing import Optional

class MinStack:
    def __init__(self, type=int): ## рантайм дженерики - сила
        self._main_stack: LinkedList = LinkedList()
        self._mins_stack: LinkedList = LinkedList()
        self._current_min: Optional[type] = None

    def add(self, value):
        self._main_stack.add(value)
        if not (self._current_min is None) and (self._current_min < value):
            return
        
        self._mins_stack.add(value)
        self._current_min = value


    def pop(self):
        value = self._main_stack.pop()
        if value == self._current_min:
            _ = self._mins_stack.pop()
            self._current_min = (
                None if self._mins_stack.head is None 
                else self._mins_stack.head.value
            )
        return value

    def get_min(self):
        return self._current_min


if __name__ == "__main__":
    a = MinStack()

    a.add(10)
    a.add(11)
    a.add(0)
    a.add(999)
    a.add(1000)

    print(a.get_min())

    for _ in range(3):
        a.pop()

    print(a.get_min())