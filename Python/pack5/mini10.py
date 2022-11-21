from collections import OrderedDict
from typing import Any

class LRUCache:
    def __init__(self, capacity=16):
        self._capacity = capacity
        self._cache_map: OrderedDict[Any, Any] = OrderedDict()

    def put(self, key, value):
        self._cache_map[key] = value
        if len(self._cache_map) >= self._capacity:
            self.put = self._put_full

    def _put_full(self, key, value):
        if key not in self._cache_map:
            self._cache_map.popitem(last=False)
            self._cache_map[key] = value

    def get(self, key):
        if key in self._cache_map:
            self._cache_map.move_to_end(key)
            return self._cache_map[key]
        return None

if __name__ == "__main__":
    cache = LRUCache(capacity=3)
    for i in range(3):
        cache.put(i, i)
    cache.put(30, 20)
    assert cache._cache_map == {1:1, 2:2, 30:20}
    cache.get(1)
    cache.get(2)
    cache.put(6, 6)
    assert cache._cache_map == {1:1, 2:2, 6:6}

