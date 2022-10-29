from typing import List
from functools import reduce

def flatten(itr: List, depth: int = -1) -> List:
    """Return flattened nested list like if it was nested with provided depth
    >>> flatten([1, 2, [4, 5], [6, [7]], 8], depth=1)
    [1, 2, 4, 5, 6, [7], 8]
    >>> flatten([1, 2, [3, [4, 5], 6], 7, [8, [9, [10], 11]]], depth = 2)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, [10], 11]

    """
    if depth == 0:
        return itr

    return reduce(
        lambda accum_list, next_item: 
            (accum_list + (flatten(next_item, depth = depth - 1) if isinstance(next_item, List) else [next_item])), 
        itr, 
        []
    )

if __name__ == "__main__":
    import doctest
    doctest.testmod()