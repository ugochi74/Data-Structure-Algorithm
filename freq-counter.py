def frequency(items):
    freq = {}
    for x in items:
        freq[x] = freq.get(x, 0) + 1
    return freq

def most_frequent(items):
    freq = frequency(items)
    #     return max(freq, key=freq.get)

    max_count = max(freq.values())
    return [key for key, count in freq.items() if count == max_count]

print(frequency([1, 2, 2, 3, 3, 3]))    # {1: 1, 2: 2, 3: 3}
print(most_frequent([1, 2, 2, 3, 3, 3]))  # 3
print(frequency([3, 7, 1, 5, 8, 3, 5, 1, 9, 8, 8, 2, 4, 2, 4, 3]))
print(most_frequent([3, 7, 1, 5, 8, 3, 5, 1, 9, 8, 8, 2, 4, 2, 4, 3]))