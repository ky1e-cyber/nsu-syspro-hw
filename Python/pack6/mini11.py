from typing import Optional

class Singleton:

    instance = None

    def _init_make(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        Singleton.__init__ = Singleton._init_get

    def _init_get(self, *args, **kwargs):
        pass

    def _new_make(cls, *args, **kwargs):
        Singleton.instance = super().__new__(cls, *args, **kwargs)
        Singleton.__new__ = Singleton._new_get
        return Singleton.instance

    def _new_get(cls, *args, **kwargs):
        return Singleton.instance

    def __new__(cls, *args, **kwargs):
        return Singleton._new_make(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        Singleton._init_make(self, *args, **kwargs)

    def __del__(self):
        Singleton.instance = None
        Singleton.__new__ = Singleton._new_make
        Singleton.__init__ = Singleton._init_make

if __name__ == "__main__":
    from collections import UserList

    class LameList(Singleton, UserList):
        pass

    l1 = LameList()

    l1.extend([1, 2, 3])

    l2 = LameList()

    assert id(l1) == id(l2)
    assert l1 == l2