from functools import wraps
from typing import Callable


def coroutine(coroutine_generator: Callable) -> Callable:
    @wraps(coroutine_generator)
    def _wrapper(*args, **kwargs):
        crtine = coroutine_generator(*args, **kwargs)
        next(crtine)
        
        return crtine

    return _wrapper

if __name__ == "__main__":
    @coroutine
    def storage():
        values = set()
        was_there = False

        while True:
            val = yield was_there
            was_there = val in values
            if not was_there:
                values.add(val)

    st = storage()

    print(st.send(42)) # False
    print(st.send(42)) # True