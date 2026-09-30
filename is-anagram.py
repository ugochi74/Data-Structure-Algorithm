def is_anagram(s, t):
    if len(s) != len(t):
        return False
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True

print(is_anagram("listen", "silent"))   # True
print(is_anagram("slot", "lots"))
print(is_anagram("lean", "learner"))
# shortcut: Counter(s) == Counter(t)