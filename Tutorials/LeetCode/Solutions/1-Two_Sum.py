class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            want = target - v
            if want in seen:
                return [seen[want], i]
            seen[v] = i
