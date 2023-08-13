class Solution(object):
    def isValid(self, s):
     stack = []
     bracket_pairs = {')': '(', '}': '{', ']': '['}
    
     for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    
     return not stack  # Return True if the stack is empty, False otherwise
        