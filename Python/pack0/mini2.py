from collections.abc import Sequence
from typing import List

def my_zip(seq1: Sequence, seq2: Sequence):
    for i in range(min(len(seq1), len(seq2))):
        yield seq1[i], seq2[i]

def zip_list(seq1: Sequence, seq2: Sequence) -> List:
    return list(my_zip(seq1, seq2))