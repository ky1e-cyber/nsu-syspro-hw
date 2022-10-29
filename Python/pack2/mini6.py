from typing import List
from functools import reduce

def flatten(itr: List) -> List:
    """Return flattened nested list like if it was one-dimensional
    >>> flatten([1, 2, [4, 5], [6, [7]], 8])
    [1, 2, 4, 5, 6, 7, 8]
    """
    return reduce(
        lambda accum_list, next_item: 
            (accum_list + (flatten(next_item) if isinstance(next_item, List) else [next_item])), 
        itr, 
        []
    )

if __name__ == "__main__":
    import doctest
    doctest.testmod()