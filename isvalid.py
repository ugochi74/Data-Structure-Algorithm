def isValid(s: str) -> bool:
    # Map open brackets to their corresponding closing brackets
    bracket_map = { '(': ')', '{': '}', '[': ']' }
    stack = []
    
    for char in s:
        # If it's an opening bracket, push its expected closer to the stack
        if char in bracket_map:
            stack.append(bracket_map[char])
        # If it's a closing bracket, check if it matches the latest expected closer
        else:
            if not stack or stack.pop() != char:
                return False
                
    # If the stack is empty, all brackets were correctly matched
    return len(stack) == 0

# --- Quick Tests ---
print(isValid("()"))      # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False
print(isValid("([])"))    # Output: True
print(isValid("([)]"))    # Output: False
