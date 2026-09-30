def first_unique(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):      # scan the string, not the dict
        if counts[ch] == 1:
            return i
    return -1

print(first_unique("leetcode"))     # 0
print(first_unique("aabb"))         # -1
print(first_unique("confidencec"))
print(first_unique("essential"))
print(first_unique("mmasi"))