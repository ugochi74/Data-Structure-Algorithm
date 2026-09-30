from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))     # "eat","tea","ate" -> "aet"
        groups[key].append(w)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat", "tab", "pit", "tip"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]