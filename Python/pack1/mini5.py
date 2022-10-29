from typing import Callable

def sum_of_two(x, y):
    return x + y

def specialize(callable: Callable, *args, **kwargs) -> Callable:
    """Returns function that calls provided callable with provided arguments applied

    >>> (specialize(abs, -10))() == abs(-10)
    True

    >>> (specialize(sum_of_two, y = 22))(45) == sum_of_two(45, y = 22)
    True

    >>> (specialize(sum_of_two, 11, 12))() == sum_of_two(11, 12)
    True

    >>> (specialize(pow, 5))(4) == pow(5, 4)
    True

    >>> specialize(sum, start = 4)([2, 10, 11, 22, 22, 41, 11]) == sum([2, 10, 11, 22, 22, 41, 11], start = 4)
    True
    """
    def _wrapper(*wrapper_args, **wrapper_kwargs):
        return callable(*args, *wrapper_args, **kwargs, **wrapper_kwargs)

    return _wrapper


if __name__ == "__main__":
    import doctest
    doctest.testmod()