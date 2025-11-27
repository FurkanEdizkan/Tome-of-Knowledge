from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            want = target - v
            if want in seen:
                return [seen[want], i]
            seen[v] = i

def main():
    nums = [2,7,11,15]
    target = 9

    solver = Solution()
    output = solver.twoSum(nums=nums, target=target)
    print(output)
    
if __name__ == "__main__":    
    main()