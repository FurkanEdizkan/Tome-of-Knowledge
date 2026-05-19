class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Skip leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Step 2: Check sign
        sign = 1
        if i < len(s) and s[i] in ['+', '-']:
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Read digits and convert
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result = sign * result
        
        # Step 4: Clamp to 32-bit range
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result
