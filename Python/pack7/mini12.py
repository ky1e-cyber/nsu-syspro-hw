from typing import Iterable

def cycle(itr: Iterable):
    while True:
        yield from itr



if __name__ == "__main__":
    c = cycle([1, 2, 3])

    l = [next(c) for _ in range(30)]

    assert l[:15] == l[15::]