class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            new_value = (self.dict[key][0] + 1, self.dict[key][1])
            self.dict[key] = new_value
            return self.dict[key][1]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self.dict) >= self.capacity:
            lru_key = self._get_lru_key()
            self.dict.pop(lru_key, None)

        self.dict[key] = (0, value)

    def _get_lru_key(self):
        lru_key = None
        lru_value = None
        for k, val in self.dict.items():
            if lru_value is None or val[0] < lru_value:
                lru_value = val[0]
                lru_key = k
        return lru_key


if __name__ == '__main__':
    cache = LRUCache(2)
    result = [
        cache.put(1, 1),
        cache.put(2, 2),
        cache.get(1),
        cache.put(3, 3),
        cache.get(2),
        cache.put(4, 4),
        cache.get(1),
        cache.get(3),
        cache.get(4),
    ]
    print(result)
