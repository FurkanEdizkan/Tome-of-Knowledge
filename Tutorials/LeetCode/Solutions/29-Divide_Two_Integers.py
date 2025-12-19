class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        
        # Exponential search with bit shifting
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            
            # Double until we exceed dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract and accumulate
            dividend -= temp_divisor
            quotient += multiple
        
        # Apply sign and return
        return -quotient if negative else quotient
