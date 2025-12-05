from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mnp",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, current: str) -> None:
            if index == len(digits):
                result.append(current)
                return
            
            letters = digit_map[digits[index]]
            for letter in letters:
                backtrack(index +1, current + letter)
        
        backtrack(0, "")
        
        return result
    
if __name__ == '__main__':
    tests = [
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("2", ["a","b","c"]),
        ("234", ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]),
        ("", []),
    ]
    
    for digits, expected in tests:
        result = Solution().letterCombinations(digits=digits)
        status = "✓" if result == expected else "✗"
        print(f"{status} letterCombinations(\"{digits}\") = {result}")
        if result != expected:
            print(f"   Expected: {expected}")