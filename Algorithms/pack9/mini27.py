
from functools import reduce
from typing import Set


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s = set()

        def f(acc_set: Set[str], dna_seq: str):
            if dna_seq in s:
                acc_set.add(dna_seq)
            return acc_set
            
        def gen(dna: str):

        
        return list(reduce(f, ))