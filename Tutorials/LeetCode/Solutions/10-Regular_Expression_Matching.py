
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(s_idx, p_idx):
            # Base cases
            if (s_idx, p_idx) in memo:
                return memo[(s_idx, p_idx)]
            
            # Pattern exhausted
            if p_idx == len(p):
                result = s_idx == len(s)
            else:
                # Check if current characters match
                first_match = s_idx < len(s) and (p[p_idx] == '.' or p[p_idx] == s[s_idx])
                
                # Check if next char in pattern is '*'
                if p_idx + 1 < len(p) and p[p_idx + 1] == '*':
                    # Two choices: skip this char+* or match and stay
                    result = dp(s_idx, p_idx + 2) or (first_match and dp(s_idx + 1, p_idx))
                else:
                    # No '*', must match current char and move both pointers
                    result = first_match and dp(s_idx + 1, p_idx + 1)
            
            memo[(s_idx, p_idx)] = result
            return result
        
        return dp(0, 0)

def main():
    sol = Solution()
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("mississippi", "mis*is*p*.", False),
        ("a", "a", True),
        ("", "", True),
        ("a", ".*", True),
        ("ab", ".*c", False),
    ]
    
    for s, p, expected in tests:
        result = sol.isMatch(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} isMatch(\"{s}\", \"{p}\") = {result} (expected {expected})")


if __name__ == "__main__":
    main()