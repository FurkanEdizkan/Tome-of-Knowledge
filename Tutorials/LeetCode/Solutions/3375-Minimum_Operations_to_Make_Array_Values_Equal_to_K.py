class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1
        
        if all(num == k for num in nums):
            return 0
        
        unique_above_k = set(num for num in nums if num > k)
    
        return len(unique_above_k)
        