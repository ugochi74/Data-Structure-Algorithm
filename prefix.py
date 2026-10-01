def longestCommonPrefix(strs: list[str]) -> str:
    # If the input list is empty, return an empty string
    if not strs:
        return ""
    
    # Sort the array alphabetically
    strs.sort()
    
    # Compare the first and last strings
    first = strs[0]
    last = strs[-1]
    
    prefix = []
    # Loop through the characters of the first string
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            prefix.append(first[i])
        else:
            break
            
    return "".join(prefix)


example1 = ["flower", "flow", "flight"]
result1 = longestCommonPrefix(example1)
print(f"Input: {example1}")
print(f"Output: '{result1}'\n")

# Example 2
example2 = ["dog", "racecar", "car"]
result2 = longestCommonPrefix(example2)
print(f"Input: {example2}")
print(f"Output: '{result2}'")

