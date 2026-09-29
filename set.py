seen = set()
seen.add(3)
seen.add(3)            # ignored
print(3 in seen)       # True, O(1)
seen.discard(3)        # no error if missing
print(set([1, 2, 2, 3, 3, 4, 6, 5, 7, 8, 8, 9, 10]))   # {1, 2, 3}s