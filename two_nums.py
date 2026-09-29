def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 5, 11, 3, 5, 10], 13))