from dataclasses import dataclass
from itertools import chain
from typing import Callable

class LinkedList:
    class _Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
    
    def __init__(self):
        self.head = None

    def add(self, value):
        if not self.head:
            self.head = self._Node(value)
            return

        self.head = self._Node(
            value, 
            next=self.head
        )

    def pop(self):
        if not self.head:
            return None

        head = self.head
        self.head = self.head.next
        return head.value

    def sequnce(self):
        head = self.head
        while head:
            yield head
            head = head.next


Stack = LinkedList ## yes

@dataclass
class OperatorInfo:
    left_assoc: bool
    precedence: int
    arity: int
    fun: Callable

operator = {
    "~":    OperatorInfo(False, 0),##, 1, lambda x: ~x),
    "!":    OperatorInfo(False, 0),##, 1, lambda x: not x),
    "%":    OperatorInfo(True, 1),##, 2, lambda x, y: x % y),
    "/":    OperatorInfo(True, 1),##, 2, lambda x, y: x // y),
    "*":    OperatorInfo(True, 1), ##, 2, lambda x, y: x * y),
    "+":    OperatorInfo(True, 2), ##, 2, lambda x, y: x  + y), 
    "-":    OperatorInfo(True, 2),
    "<<":   OperatorInfo(True, 3),
    ">>":   OperatorInfo(True, 3),
    "&":    OperatorInfo(True, 4),
    "^":    OperatorInfo(True, 5),
    "|":    OperatorInfo(True, 6),
    "&&":   OperatorInfo(True, 7),
    "||":   OperatorInfo(True, 8)
}

def to_rpn(expr: str) -> str:
    out = Stack()

    expr_iter = chain(("(",), expr.split(), (")"))

    def handle_expr():
        curr_ops = Stack()

        for token in expr_iter:
            if token == ")":
                while curr_ops.head:
                    out.add(curr_ops.pop())
                return
            
            if token == "(":
                handle_expr()
                continue
            
            if token.isnumeric():
                out.add(token)
            else:
                new_op = operator.get(token)
                if not new_op:
                    continue

                if not curr_ops.head:
                    curr_ops.add(token)
                    continue

                ops_head = operator.get(curr_ops.head.value)

                while ( (new_op.precedence > ops_head.precedence) or
                        (new_op.precedence == ops_head.precedence and new_op.left_assoc) ):
                    out.add(curr_ops.pop())
                    if not curr_ops.head:
                        break
                    ops_head = operator.get(curr_ops.head.value)
            
                curr_ops.add(token)

    handle_expr()

    return " ".join(reversed([node.value for node in out.sequnce()]))

def eval_rpn(expr: str) -> int:
    stack = reversed(expr.split())

print("3 + 2 * 21 - 3 * (2 + 9)")