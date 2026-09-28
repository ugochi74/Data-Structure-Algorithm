class Solution:

    def twoSum(self, nums, target):
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
solver = Solution()
result1 = solver.twoSum([2, 7, 11, 15], 9)
result2 = solver.twoSum([3, 2, 4], 6)
result3 = solver.twoSum([3, 3], 6)
print("Test1:", result1)
print("Test2:", result2)
print("Test3:",  result3)
    #print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    #print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
    #print(twoSum([3, 3], 6))          # Output: [0, 1]
