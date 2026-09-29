# def top_k(items, k):
#     freq = {}
#     for x in items:
#         freq[x] = freq.get(x, 0) + 1
#     return sorted(freq.items(), key=lambda pair: pair[1], reverse=True)[:k]

# print(top_k("confidence", 3))
# [('a', 3), ('n', 2), ('b', 1)]


word = "confidence"

# manual
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)                 # {'b': 1, 'a': 3, 'n': 2}

# built-in
from collections import Counter, defaultdict
print(Counter(word))
print(Counter(word).most_common(3))   # [('a', 3)]

# defaultdict removes the .get boilerplate
freq = defaultdict(int)
for ch in word:
    freq[ch] += 1