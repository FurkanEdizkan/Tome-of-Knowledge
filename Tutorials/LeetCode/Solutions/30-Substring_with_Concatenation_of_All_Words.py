from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        result = []
        
        word_freq = Counter(words)
        
        for i in range(len(s) - total_len + 1):
            substring = s[i:i + total_len]

            seen = Counter()
            for j in range(0, total_len, word_len):
                word = substring[j:j + word_len]
                seen[word] += 1
            
            if seen == word_freq:
                result.append(i)
        
        return result