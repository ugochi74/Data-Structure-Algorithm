class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _index(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:                 # key exists: update
                bucket[i] = (key, value)
                return
        bucket.append((key, value))      # new key: insert
        self.count += 1
        if self.count / self.size > 0.75:
            self._resize()

    def get(self, key, default=None):
        bucket = self.buckets[self._index(key)]
        for k, v in bucket:
            if k == key:
                return v
        return default

    def delete(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def _resize(self):
        old = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old:
            for k, v in bucket:
                self.put(k, v)           # must re-hash: index depends on size

    def __repr__(self):
        return "\n".join(f"{i}: {b}" for i, b in enumerate(self.buckets))


ht = HashTable()
for name, age in [("Ann", 20), ("Bob", 22), ("Cid", 19), ("Dee", 25)]:
    ht.put(name, age)
print(ht)
print(ht.get("Bob"))       # 22
ht.delete("Bob")
print(ht.get("Bob"))       # None