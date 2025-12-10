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
    
# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("", True),
        ("{[]}", True),
        ("([{}])", True),
        ("([)]", False),
    ]
    
    for s, expected in test_cases:
        result = solution.isValid(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} isValid('{s}') = {result} (expected {expected})")