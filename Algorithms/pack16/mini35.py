from dataclasses import dataclass
from collections.abc import Sequence
from collections import namedtuple
from typing import Any, Dict

class UnionFind:


    def __init__(self):
        self._parents: Dict[Any, type(self).SetInfo] = {}
        self.sets_count = 0

    def find_representative(self, el) -> Any:
        pass

    def _merge_sets_roots(self, repr1: Any, root2: Any):
        pass

    def merge_sets(self, el1 )

@dataclass
class Task:
    deadline: int
    cost: int

def solution(sorted_tasks: Sequence[Task]) -> Sequence[Task]:
    pass
