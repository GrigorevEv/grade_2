class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for _ in range(self.size)]
        self.count = 0

    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    def __setitem__(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)

        # избегание коллизий
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size

        self.count += 1
        self.slots[h] = item

    def __getitem__(self, key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size
        return None


if __name__ == '__main__':
    ht = HashTable()
    ht["good"] = "eggs"
    ht["better"] = "ham"
    ht["best"] = "spam"
    ht["ad"] = "do not"
    ht["ga"] = "collide"

    for k in ('good', 'better', 'best', 'worst', 'ad', 'ga'):
        v = ht[k]
        print(v)
