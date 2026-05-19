class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        closing_to_opening = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in closing_to_opening:
                if not stack or stack[-1] != closing_to_opening[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
