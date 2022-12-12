from typing import List, Iterable

def chain(*iters: List[Iterable]) -> Iterable:
    for i in iters:
        yield from i


if __name__ == "__main__":
    c = chain(range(10), [420, 69], (1337,))
    expected = list(range(10)) + [420, 69, 1337]

    assert list(c) == expected