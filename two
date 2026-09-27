def twoSum(nums: list[int], target: int) -> list[int]:
    # Stores seen numbers as keys and their indices as values
    seen = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        # If the complement is already in our map, we found the pair
        if complement in seen:
            return [seen[complement], index]
            
        # Otherwise, track the current number and its index
        seen[num] = index
        
    return []

# --- Quick Tests ---
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(twoSum([3, 3], 6))          # Output: [0, 1]
