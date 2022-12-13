from typing import Optional

class Singleton:

    instance = None

    def _new_get(cls, *args, **kwargs):
        return cls.instance

    def _init_get(self, *args, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        type(self).__init__ = Singleton._init_get ## bruh

    def __new__(cls, *args, **kwargs):
        cls.instance = super().__new__(cls, *args, **kwargs)
        cls.__new__ = cls._new_get
        return cls.instance

if __name__ == "__main__":
    from collections import UserList

    class LameList(Singleton, UserList):
        pass

    l1 = LameList()

    l1.extend([1, 2, 3])

    l2 = LameList()

    assert id(l1) == id(l2)
    assert l1 == l2
