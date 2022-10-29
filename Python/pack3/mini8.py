from functools import partial, wraps

def deprecated(f=None, *, since=None, will_be_removed=None):
    if f is None:
        return partial(deprecated, since=since, will_be_removed=will_be_removed)
    
    msg: str = "".join([
        f"Warning: function {f.__name__} is deprecated", 
        (f" since version {since}" if not (since is None) else ""), 
        ". It will be removed in ",
        (f"version {will_be_removed}." if not (will_be_removed is None) else "future versions.")
        ])

    @wraps(f)
    def _wraper(*args, **kwargs):
        print(msg)
        return f(*args, **kwargs)

    return _wraper

@deprecated
def sum_of_two(a, b):
    return a + b

@deprecated(since="1.0")
def ident(x):
    return x

@deprecated(will_be_removed="2.1")
def not_fast_inverse_sqrt(x):
    return 1 / (x ** 0.5)

@deprecated(since="0.4.5.1", will_be_removed="1.1a")
def hello_world():
    print("hello world")


if __name__ == "__main__":
    print(sum_of_two(2, 2))
    print(ident(1))
    print(not_fast_inverse_sqrt(4.20))
    hello_world()
