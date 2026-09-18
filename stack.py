def is_balanced(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:          # nothing to pop — a ) with no matching (
                return False
            stack.pop()
    
    return len(stack) == 0         # True only if every ( got closed


# Test cases
print(is_balanced("(a(b)c)"))   # True
print(is_balanced("(a(b)c"))    # False
print(is_balanced("a)b(c"))     # False
print(is_balanced("()()"))      # True
print(is_balanced(")("))        # False