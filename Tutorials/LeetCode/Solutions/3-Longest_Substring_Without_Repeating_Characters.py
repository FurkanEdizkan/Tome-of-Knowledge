class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l_p = 0
        output = 0
        for r_p in range(len(s)):
            while s[r_p] in char_set:
                char_set.remove(s[l_p])
                l_p += 1
            char_set.add(s[r_p])
            output = max(output, r_p - l_p +1)
        
        return output