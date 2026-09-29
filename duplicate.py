def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

# one-liner: len(set(nums)) != len(nums)
# Example 1: A list with duplicates (The number 3 appears twice)
example_1 = [1, 2, 3, 3, 4]
result_1 = contains_duplicate(example_1)
print(f"List: {example_1} -> Contains duplicate? {result_1}")  



# Example 2: A list where every number is completely unique
example_2 = [10, 20, 30, 40, 50]
#result_2 = contains_duplicate(example_2)
print(contains_duplicate(example_2))


# Example 3: An empty list (Edge case)
example_3 = []
result_3 = contains_duplicate(example_3)
print(f"List: {example_3} -> Contains duplicate? {result_3}")  
