from functools import reduce
from typing import Set, List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        encounterd = set()

        def f(acc_set: Set[str], dna_seq: str):
            if dna_seq in encounterd:
                acc_set.add(dna_seq)
            else:
                encounterd.add(dna_seq)
            return acc_set
            
        def get_dna_seq():
            for i in range(9, len(s)):
                yield s[i - 9:i + 1:]

        return list(reduce(f, get_dna_seq(), set()))